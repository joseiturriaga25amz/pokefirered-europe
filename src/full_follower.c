#include "global.h"
#include "gflib.h"
#include "event_object_movement.h"
#include "field_player_avatar.h"
#include "full_follower.h"
#include "pokemon.h"
#include "quest_log.h"
#include "script.h"
#include "start_menu.h"
#include "strings.h"
#include "task.h"
#include "trainer_see.h"
#include "constants/event_object_movement.h"
#include "constants/event_objects.h"
#include "constants/pokemon.h"

extern const u8 EventScript_FullFollowerFriendship0[];
extern const u8 EventScript_FullFollowerFriendship1[];
extern const u8 EventScript_FullFollowerFriendship2[];
extern const u8 EventScript_FullFollowerFriendship3[];
extern const u8 EventScript_FullFollowerFriendship4[];
extern const u8 EventScript_FullFollowerFriendship5[];
extern const u8 EventScript_FullFollowerFriendship6[];
extern const u8 PokemonTower_2F_EventScript_RivalTriggerRight[];
extern const u8 PokemonTower_2F_EventScript_RivalTriggerDown[];
extern const u8 SilphCo_7F_EventScript_RivalTriggerBottom[];

#define FOLLOWER_TASK_PRIORITY 0x51
#define FOLLOWER_TRAIL_CAPACITY 8

// Runtime-only visual intent, never stored in the save or copied into link.
enum FollowerPresentationState
{
    FOLLOWER_PRESENTATION_FOLLOW,
    FOLLOWER_PRESENTATION_HOLD_VISIBLE,
    FOLLOWER_PRESENTATION_REPOSITION,
    FOLLOWER_PRESENTATION_TRANSITION,
    FOLLOWER_PRESENTATION_RECALLED,
};

// Direct text-only script grammar, matching asm/macros/event.inc. Never
// follow branches or calls; reject scripts with movement, flags or battles.
#define FOLLOWER_CMD_END        0x02
#define FOLLOWER_CMD_LOADWORD   0x0F
#define FOLLOWER_CMD_CALLSTD    0x09
#define FOLLOWER_CMD_FACEPLAYER 0x5A
#define FOLLOWER_CMD_LOCKALL    0x69
#define FOLLOWER_CMD_LOCK      0x6A
#define FOLLOWER_CMD_RELEASEALL 0x6B
#define FOLLOWER_CMD_RELEASE    0x6C
#define FOLLOWER_MSGBOX_NPC     2
#define FOLLOWER_MSGBOX_SIGN    3
#define FOLLOWER_MSGBOX_DEFAULT 4

static bool8 sFollowerEnabled = TRUE;
static u16 sFollowerSpecies = SPECIES_NONE;
// Visual variant comes from the actual first eligible party Pokémon.
static bool8 sFollowerIsShiny = FALSE;
// The graphics slot is 8-bit; the selected species is held only at runtime.
static u8 sFollowerGraphicsId = OBJ_EVENT_GFX_PIKACHU;
// Unsaved, bounded history of the player's vacated map tiles.
static s16 sTrailX[FOLLOWER_TRAIL_CAPACITY];
static s16 sTrailY[FOLLOWER_TRAIL_CAPACITY];
static s16 sLastPlayerX;
static s16 sLastPlayerY;
static u8 sTrailHead;
static u8 sTrailCount;
// Transient gate: source warp -> locked destination entrance -> player control.
static bool8 sFollowerWarpTransition;
static bool8 sFollowerExitLockObserved;
// Unsaved and valid only during a verified, single-message field interaction.
static bool8 sFollowerSafeDialogue;
// An explicit trainer-intro speech owns this hold, not arbitrary script locks.
static bool8 sFollowerTrainerIntro;
// Only explicitly vetted, stationary Gary scenes own this unsaved presentation hold.
static bool8 sFollowerGarySceneHold;
// Battle graphics teardown must not respawn the follower before field return.
static bool8 sFollowerBattleTransition;
static enum FollowerPresentationState sFollowerPresentationState = FOLLOWER_PRESENTATION_RECALLED;

static void Task_FullFollower(u8 taskId);
static struct ObjectEvent *FindFollowerObject(void);
static u8 GetPrototypeFollowerGraphicsId(u16 species);
static u16 GetEligiblePrototypeFollowerSpecies(bool8 *isShiny);
static bool8 ShouldSuppressFollower(void);
static void PositionFollowerBehindPlayer(struct ObjectEvent *follower, s16 x, s16 y);
static void ResetFollowerTrail(const struct ObjectEvent *player);
static bool8 FollowRecordedPlayerSteps(struct ObjectEvent *follower);
static void RefreshFollower(void);

void FullFollower_SetEnabled(bool8 enabled)
{
    sFollowerEnabled = enabled;
}

bool8 FullFollower_IsEnabled(void)
{
    return sFollowerEnabled;
}

u8 FullFollower_GetSpriteGraphicsId(void)
{
    return sFollowerGraphicsId;
}

bool8 FullFollower_IsShiny(void)
{
    return sFollowerIsShiny;
}

u16 FullFollower_GetSpecies(void)
{
    // Gen III Hoenn internal species IDs are not National Dex numbers.
    // The generated sprite registry is indexed by National Dex 1..386.
    if (sFollowerSpecies == SPECIES_NONE)
        return 0;
    return SpeciesToNationalPokedexNum(sFollowerSpecies);
}

bool8 FullFollower_UsesPilotGraphics(void)
{
    return sFollowerGraphicsId == OBJ_EVENT_GFX_PIKACHU
        || sFollowerGraphicsId == OBJ_EVENT_GFX_SNORLAX
        || sFollowerGraphicsId == OBJ_EVENT_GFX_MEW
        || FullFollower_HasRegisteredGraphics(FullFollower_GetSpecies());
}

static u8 GetPrototypeFollowerGraphicsId(u16 species)
{
    // A generated National Dex species reuses the existing 8-bit follower ID.
    // Proxy is only a fallback; graphics resolve through the National key.
    if (FullFollower_HasRegisteredGraphics(SpeciesToNationalPokedexNum(species)))
        return OBJ_EVENT_GFX_PIKACHU;

    // Prototype otherwise uses only overworld assets already present in FireRed Full.
    switch (species)
    {
    case SPECIES_PIKACHU:
        return OBJ_EVENT_GFX_PIKACHU;
    case SPECIES_SNORLAX:
        return OBJ_EVENT_GFX_SNORLAX;
    case SPECIES_MEW:
        return OBJ_EVENT_GFX_MEW;
    case SPECIES_SUICUNE:
        return OBJ_EVENT_GFX_SUICUNE;
    case SPECIES_PIDGEY:
        return OBJ_EVENT_GFX_PIDGEY;
    case SPECIES_SPEAROW:
        return OBJ_EVENT_GFX_SPEAROW;
    default:
        return 0xFF;
    }
}

static u16 GetEligiblePrototypeFollowerSpecies(bool8 *isShiny)
{
    u32 i;

    *isShiny = FALSE;
    for (i = 0; i < PARTY_SIZE; i++)
    {
        u16 species = GetMonData(&gPlayerParty[i], MON_DATA_SPECIES);
        u16 hp = GetMonData(&gPlayerParty[i], MON_DATA_HP);
        bool8 isEgg = GetMonData(&gPlayerParty[i], MON_DATA_IS_EGG);

        if (species != SPECIES_NONE && hp != 0 && !isEgg)
        {
            // The follower represents the first eligible party Pokémon, not
            // the first one with a prototype sprite. Hide unsupported leads.
            if (GetPrototypeFollowerGraphicsId(species) == 0xFF)
                return SPECIES_NONE;
            *isShiny = IsMonShiny(&gPlayerParty[i]);
            return species;
        }
    }

    return SPECIES_NONE;
}

// This is evaluated on A press, before the dialogue locks field controls.
// Read the same first healthy, non-egg Pokémon that selected the visible
// follower; GetLeadMonFriendship would incorrectly use a fainted lead.
const u8 *FullFollower_GetFriendshipInteractionScript(void)
{
    static const u8 *const sFriendshipScripts[] = {
        EventScript_FullFollowerFriendship0,
        EventScript_FullFollowerFriendship1,
        EventScript_FullFollowerFriendship2,
        EventScript_FullFollowerFriendship3,
        EventScript_FullFollowerFriendship4,
        EventScript_FullFollowerFriendship5,
        EventScript_FullFollowerFriendship6,
    };
    bool8 isShiny = FALSE;
    u16 species = GetEligiblePrototypeFollowerSpecies(&isShiny);
    u32 i;

    // Never open a dialog for a stale sprite after a party/variant switch.
    if (!sFollowerEnabled || species == SPECIES_NONE
     || species != sFollowerSpecies || isShiny != sFollowerIsShiny)
        return NULL;

    for (i = 0; i < PARTY_SIZE; i++)
    {
        struct Pokemon *mon = &gPlayerParty[i];
        u16 monSpecies = GetMonData(mon, MON_DATA_SPECIES);

        if (monSpecies != SPECIES_NONE
         && GetMonData(mon, MON_DATA_HP) != 0
         && !GetMonData(mon, MON_DATA_IS_EGG))
        {
            u8 friendship;
            u8 tier;

            if (monSpecies != species)
                return NULL;
            GetMonData(mon, MON_DATA_NICKNAME, gStringVar1);
            friendship = GetMonData(mon, MON_DATA_FRIENDSHIP);
            if (friendship == 255)
                tier = 6;
            else if (friendship >= 200)
                tier = 5;
            else if (friendship >= 150)
                tier = 4;
            else if (friendship >= 100)
                tier = 3;
            else if (friendship >= 50)
                tier = 2;
            else if (friendship > 0)
                tier = 1;
            else
                tier = 0;
            return sFriendshipScripts[tier];
        }
    }
    return NULL;
}

static struct ObjectEvent *FindFollowerObject(void)
{
    u32 i;

    for (i = 0; i < OBJECT_EVENTS_COUNT; i++)
    {
        if (gObjectEvents[i].active
         && gObjectEvents[i].localId == OBJ_EVENT_ID_FULL_FOLLOWER)
            return &gObjectEvents[i];
    }

    return NULL;
}

// Only straight-line text scripts may keep an existing follower on-screen.
// Up to four consecutive messages are allowed; branches, movement, specials,
// gifts and battle opcodes are rejected. The 64-byte margin keeps every read
// in mapped ROM even if the script starts at the end of the cartridge.
#define FOLLOWER_MAX_SAFE_MESSAGES 4
static bool8 IsSafeFollowerDialogueScript(const u8 *script)
{
    uintptr_t address = (uintptr_t)script;
    u8 i = 0;
    u8 messages;

    if (address < 0x08000000 || address > 0x09FFFFC0)
        return FALSE;

    if (script[i] == FOLLOWER_CMD_LOCK || script[i] == FOLLOWER_CMD_LOCKALL)
        i++;
    if (script[i] == FOLLOWER_CMD_FACEPLAYER)
        i++;

    for (messages = 0; messages < FOLLOWER_MAX_SAFE_MESSAGES; messages++)
    {
        if (script[i] != FOLLOWER_CMD_LOADWORD)
            break;
        if (script[i + 1] != 0)
            return FALSE;
        i += 6; // command, buffer slot and four-byte text pointer
        if (script[i++] != FOLLOWER_CMD_CALLSTD)
            return FALSE;
        if (script[i] != FOLLOWER_MSGBOX_NPC
         && script[i] != FOLLOWER_MSGBOX_SIGN
         && script[i] != FOLLOWER_MSGBOX_DEFAULT)
            return FALSE;
        i++;
    }

    if (messages == 0)
        return FALSE;
    if (script[i] == FOLLOWER_CMD_RELEASE || script[i] == FOLLOWER_CMD_RELEASEALL)
        i++;
    return script[i] == FOLLOWER_CMD_END;
}

void FullFollower_ClearSafeDialogue(void)
{
    sFollowerSafeDialogue = FALSE;
    sFollowerTrainerIntro = FALSE;
    sFollowerGarySceneHold = FALSE;
}

// Permit HOLD for exactly vetted Gary coordinate-trigger scripts where the
// player stays put and the rival cannot enter the follower's trailing tile.
// Silph 7F TOP is intentionally excluded: Gary walks into the possible trail.
// Never spawn a follower under an active field script lock.
void FullFollower_BeginScriptedGaryScene(const u8 *script)
{
    sFollowerGarySceneHold = (script == PokemonTower_2F_EventScript_RivalTriggerRight
                           || script == PokemonTower_2F_EventScript_RivalTriggerDown
                           || script == SilphCo_7F_EventScript_RivalTriggerBottom)
                          && sFollowerEnabled
                          && FindFollowerObject() != NULL
                          && !sFollowerWarpTransition
                          && !sFollowerBattleTransition
                          && !QL_IS_PLAYBACK_STATE
                          && !IsUpdateLinkStateCBActive()
                          && !InUnionRoom()
                          && !gPaletteFade.active;
}

// Only the engine's trainer intro speech can open this presentation window.
// Retain an existing follower; never allocate one in the middle of a script.
void FullFollower_BeginTrainerIntro(void)
{
    sFollowerTrainerIntro = sFollowerEnabled
                         && FindFollowerObject() != NULL
                         && !sFollowerWarpTransition
                         && !sFollowerBattleTransition
                         && !QL_IS_PLAYBACK_STATE
                         && !IsUpdateLinkStateCBActive()
                         && !InUnionRoom()
                         && !gPaletteFade.active;
}

// The battle scene does not own field sprites or local-ID 254. Remove it
// before the transition effect allocates graphics/OAM; no warp lock needed.
void FullFollower_RecallForBattle(void)
{
    struct ObjectEvent *follower = FindFollowerObject();

    FullFollower_ClearSafeDialogue();
    sFollowerBattleTransition = TRUE;
    sFollowerPresentationState = FOLLOWER_PRESENTATION_TRANSITION;
    if (follower != NULL)
        RemoveFullFollowerObjectEvent(follower);
    sFollowerSpecies = SPECIES_NONE;
    sFollowerIsShiny = FALSE;
    sTrailCount = 0;
}

void FullFollower_BeginSafeDialogue(const u8 *script)
{
    // Called exclusively after a player A-button interaction starts.
    // An absent follower must never materialize just for a message.
    sFollowerSafeDialogue = FindFollowerObject() != NULL
                         && !QL_IS_PLAYBACK_STATE
                         && !gPaletteFade.active
                         && IsSafeFollowerDialogueScript(script);
}

static bool8 ShouldSuppressFollower(void)
{
    // Quest Log playback uses a fixed NPC movement table; follower ID 254
    // is never a map-template NPC and must not enter that playback path.
    if (QL_IS_PLAYBACK_STATE)
        return TRUE;
    if (sFollowerBattleTransition)
        return TRUE;

    // A warp is not finished until destination entrance controls unlock.
    // The field-control lock is independent of ScriptContext_IsEnabled().
    if (sFollowerWarpTransition)
    {
        if (ArePlayerFieldControlsLocked())
            sFollowerExitLockObserved = TRUE;
        if (!sFollowerExitLockObserved || ArePlayerFieldControlsLocked())
            return TRUE;
        sFollowerWarpTransition = FALSE;
        sFollowerExitLockObserved = FALSE;
    }

    // A verified trainer-sight task may hold the existing follower through
    // the exclamation mark and approach, even while its own script runs.
    // An unrelated script without this task remains suppressed.
    if (ArePlayerFieldControlsLocked()
     && !StartMenu_IsSafeForFollower()
     && !sFollowerSafeDialogue
     && !sFollowerTrainerIntro
     && !sFollowerGarySceneHold
     && !TrainerSee_IsApproachActive())
        return TRUE;

    // The caller separately checks the party lead and the on/off preference.
    if (TestPlayerAvatarFlags(PLAYER_AVATAR_FLAG_MACH_BIKE
                            | PLAYER_AVATAR_FLAG_ACRO_BIKE
                            | PLAYER_AVATAR_FLAG_SURFING))
        return TRUE;

    // Two-tile ledge jumps are not ordinary trail steps. Hide while the
    // native player jump is still animating; return only after it finishes.
    // Copyable movement 8 is set by PlayerJumpLedge/acro jumps.
    if (PlayerGetCopyableMovement() == 8
     && ObjectEventCheckHeldMovementStatus(&gObjectEvents[gPlayerAvatar.objectEventId]) == 0)
        return TRUE;

    // The prototype suppresses presentation during scripted field control.
    // This keeps follower state out of cutscenes/trainer-sight/link-sensitive scripts.
    if (ScriptContext_IsEnabled()
     && !sFollowerSafeDialogue
     && !sFollowerTrainerIntro
     && !sFollowerGarySceneHold
     && !TrainerSee_IsApproachActive())
        return TRUE;

    // Text-only scripts do not perform fades. If an independent transition
    // starts, abandon the exception rather than retain an unsafe sprite.
    if (gPaletteFade.active
     && (sFollowerSafeDialogue || sFollowerTrainerIntro || sFollowerGarySceneHold || TrainerSee_IsApproachActive()))
        return TRUE;

    return FALSE;
}

static bool8 GetSafeFollowerSpawnCoords(s16 *x, s16 *y)
{
    struct ObjectEvent *player = &gObjectEvents[gPlayerAvatar.objectEventId];
    u8 direction;

    if (player->facingDirection < DIR_SOUTH || player->facingDirection > DIR_EAST)
        return FALSE;

    direction = GetOppositeDirection(player->facingDirection);
    *x = player->currentCoords.x;
    *y = player->currentCoords.y;
    MoveCoords(direction, x, y);

    // Use the player's normal map/NPC collision rules for the initial tile.
    // A follower is nonblocking once spawned, so testing its own collision
    // would not detect an occupied tile. Do not spawn into walls or NPCs.
    return GetCollisionAtCoords(player, *x, *y, direction) == COLLISION_NONE;
}

static void PositionFollowerBehindPlayer(struct ObjectEvent *follower, s16 x, s16 y)
{
    struct ObjectEvent *player = &gObjectEvents[gPlayerAvatar.objectEventId];

    MoveObjectEventToMapCoords(follower, x, y);
    follower->currentElevation = player->currentElevation;
    follower->previousElevation = player->currentElevation;

    // The next move is selected from the player's vacated tiles.
}


static void ResetFollowerTrail(const struct ObjectEvent *player)
{
    sTrailHead = 0;
    sTrailCount = 0;
    sLastPlayerX = player->currentCoords.x;
    sLastPlayerY = player->currentCoords.y;
}

void FullFollower_OnCameraCoordsShift(s16 dx, s16 dy)
{
    u8 i;
    if (FindFollowerObject() == NULL)
        return;

    sLastPlayerX -= dx;
    sLastPlayerY -= dy;
    for (i = 0; i < sTrailCount; i++)
    {
        u8 index = (sTrailHead + i) % FOLLOWER_TRAIL_CAPACITY;
        sTrailX[index] -= dx;
        sTrailY[index] -= dy;
    }
}

static bool8 FollowRecordedPlayerSteps(struct ObjectEvent *follower)
{
    const struct ObjectEvent *player = &gObjectEvents[gPlayerAvatar.objectEventId];
    s16 x;
    s16 y;
    s16 dx = player->currentCoords.x - sLastPlayerX;
    s16 dy = player->currentCoords.y - sLastPlayerY;
    u8 direction;
    u8 collision;
    u8 movementAction;

    if (dx != 0 || dy != 0)
    {
        u8 next;

        // Jump, warp or lost history: recall instead of cutting corners.
        if ((dx != 0 && dy != 0) || dx > 1 || dx < -1 || dy > 1 || dy < -1
         || sTrailCount == FOLLOWER_TRAIL_CAPACITY)
            return FALSE;

        next = (sTrailHead + sTrailCount) % FOLLOWER_TRAIL_CAPACITY;
        sTrailX[next] = sLastPlayerX;
        sTrailY[next] = sLastPlayerY;
        sTrailCount++;
        sLastPlayerX = player->currentCoords.x;
        sLastPlayerY = player->currentCoords.y;
    }

    // MOVEMENT_TYPE_NONE executes held movements in the native sprite callback.
    if (ObjectEventClearHeldMovementIfFinished(follower) == 0)
        return TRUE;
    if (sTrailCount == 0)
        return TRUE;

    x = sTrailX[sTrailHead];
    y = sTrailY[sTrailHead];
    if (follower->currentCoords.x == x && follower->currentCoords.y == y)
    {
        sTrailHead = (sTrailHead + 1) % FOLLOWER_TRAIL_CAPACITY;
        sTrailCount--;
        return TRUE;
    }

    if (follower->currentCoords.x == x && follower->currentCoords.y + 1 == y)
        direction = DIR_SOUTH;
    else if (follower->currentCoords.x == x && follower->currentCoords.y - 1 == y)
        direction = DIR_NORTH;
    else if (follower->currentCoords.x + 1 == x && follower->currentCoords.y == y)
        direction = DIR_EAST;
    else if (follower->currentCoords.x - 1 == x && follower->currentCoords.y == y)
        direction = DIR_WEST;
    else
        return FALSE;

    // Dynamic NPC occupancy can clear on a later frame. Terrain, elevation
    // and map borders cannot be resolved by waiting on the same invalid step;
    // recall and retry safe spawning instead of filling the trail indefinitely.
    collision = GetCollisionAtCoords(follower, x, y, direction);
    if (collision == COLLISION_OBJECT_EVENT)
        return TRUE;
    if (collision != COLLISION_NONE)
        return FALSE;

    // Running shoes use the native 8-frame run step. A 16-frame follower
    // walk would fall increasingly behind and overflow the bounded trail.
    // Use the ordinary 8-frame NPC walk animation; do not apply player gfx.
    if (player->movementActionId >= MOVEMENT_ACTION_PLAYER_RUN_DOWN
     && player->movementActionId <= MOVEMENT_ACTION_PLAYER_RUN_RIGHT)
        movementAction = GetWalkFastMovementAction(direction);
    else
        movementAction = GetWalkNormalMovementAction(direction);

    if (!ObjectEventSetHeldMovement(follower, movementAction))
    {
        sTrailHead = (sTrailHead + 1) % FOLLOWER_TRAIL_CAPACITY;
        sTrailCount--;
    }
    return TRUE;
}

static void RefreshFollower(void)
{
    struct ObjectEvent *follower = FindFollowerObject();
    bool8 isShiny = FALSE;
    u16 species = GetEligiblePrototypeFollowerSpecies(&isShiny);
    u8 graphicsId;

    if (sFollowerSafeDialogue
     && !ArePlayerFieldControlsLocked()
     && !ScriptContext_IsEnabled())
        sFollowerSafeDialogue = FALSE;

    if (ShouldSuppressFollower() || !sFollowerEnabled || species == SPECIES_NONE)
    {
        sFollowerPresentationState = sFollowerWarpTransition
                                   ? FOLLOWER_PRESENTATION_TRANSITION
                                   : FOLLOWER_PRESENTATION_RECALLED;
        // Suppressed presentation must release its object slot AND sprite/OAM
        // allocation, not leave a hidden object behind through bike/Surf/scripts.
        // Remove the runtime-only object, never a saved map object or flag.
        if (follower != NULL)
            RemoveFullFollowerObjectEvent(follower);
        sFollowerSpecies = SPECIES_NONE;
        sFollowerIsShiny = FALSE;
        sTrailCount = 0;
        return;
    }

    // HOLD works for Start/Save, vetted text dialogue, local trainer
    // approach and its engine-owned intro speech. Never advance the trail.
    // Never create one while the player is in a locked field interface.
    sFollowerPresentationState = (StartMenu_IsSafeForFollower()
                               || sFollowerSafeDialogue
                               || sFollowerTrainerIntro
                               || sFollowerGarySceneHold
                               || TrainerSee_IsApproachActive())
                               ? FOLLOWER_PRESENTATION_HOLD_VISIBLE
                               : FOLLOWER_PRESENTATION_FOLLOW;
    if (sFollowerPresentationState == FOLLOWER_PRESENTATION_HOLD_VISIBLE)
    {
        // Do not retain a stale Pokémon or shiny variant if the party changes.
        if (follower != NULL
         && (sFollowerSpecies != species || sFollowerIsShiny != isShiny))
        {
            RemoveFullFollowerObjectEvent(follower);
            sFollowerSpecies = SPECIES_NONE;
            sFollowerIsShiny = FALSE;
            sTrailCount = 0;
        }
        return;
    }

    graphicsId = GetPrototypeFollowerGraphicsId(species);

    // The graphics slot is resolved through the current runtime species.
    // Destroy the OLD sprite while the slot still resolves to its old graphics:
    // otherwise its tile cleanup could use the NEW species' frame dimensions.
    if (follower != NULL
     && (follower->graphicsId != OBJ_EVENT_GFX_FULL_FOLLOWER
      || sFollowerSpecies != species
      || sFollowerIsShiny != isShiny
      || sFollowerGraphicsId != graphicsId))
    {
        RemoveFullFollowerObjectEvent(follower);
        follower = NULL;
    }

    sFollowerSpecies = species;
    sFollowerIsShiny = isShiny;
    sFollowerGraphicsId = graphicsId;

    if (follower == NULL)
    {
        struct ObjectEvent *player = &gObjectEvents[gPlayerAvatar.objectEventId];
        s16 spawnX;
        s16 spawnY;
        int objectEventId;

        // REPOSITION retries a legal unoccupied tile after a map return.
        sFollowerPresentationState = FOLLOWER_PRESENTATION_REPOSITION;
        if (!GetSafeFollowerSpawnCoords(&spawnX, &spawnY))
            return;

        objectEventId = SpawnSpecialObjectEventParameterized(
            OBJ_EVENT_GFX_FULL_FOLLOWER,
            MOVEMENT_TYPE_NONE,
            OBJ_EVENT_ID_FULL_FOLLOWER,
            player->currentCoords.x,
            player->currentCoords.y,
            player->currentElevation);

        if (objectEventId >= OBJECT_EVENTS_COUNT)
            return;

        follower = &gObjectEvents[objectEventId];
        PositionFollowerBehindPlayer(follower, spawnX, spawnY);
        ResetFollowerTrail(player);
        sFollowerPresentationState = FOLLOWER_PRESENTATION_FOLLOW;
    }

    if (!FollowRecordedPlayerSteps(follower))
    {
        RemoveFullFollowerObjectEvent(follower);
        sFollowerSpecies = SPECIES_NONE;
        sFollowerIsShiny = FALSE;
        sTrailCount = 0;
        sFollowerPresentationState = FOLLOWER_PRESENTATION_REPOSITION;
    }

    // The object-event engine owns sprite invisibility/off-screen culling.
    // Forcing invisible = FALSE here could expose an off-screen sprite.
}

static void Task_FullFollower(u8 taskId)
{
    (void)taskId;
    RefreshFollower();
}

void FullFollower_RecallForWarp(void)
{
    struct ObjectEvent *follower = FindFollowerObject();

    FullFollower_ClearSafeDialogue();

    sFollowerWarpTransition = TRUE;
    sFollowerExitLockObserved = FALSE;
    sFollowerPresentationState = FOLLOWER_PRESENTATION_TRANSITION;
    if (follower != NULL)
        RemoveFullFollowerObjectEvent(follower);
    sFollowerSpecies = SPECIES_NONE;
    sFollowerIsShiny = FALSE;
    sTrailCount = 0;
}

void FullFollower_DiscardForLocalReload(void)
{
    struct ObjectEvent *follower = FindFollowerObject();

    FullFollower_ClearSafeDialogue();

    // ResumeMap resets sprite memory before rebuilding surviving objects.
    // Invalidate the transient follower so that the object reconstruction
    // cannot recreate a stale sprite. Preserve any pending warp entrance gate.
    if (follower != NULL)
        follower->active = FALSE;
    sFollowerPresentationState = FOLLOWER_PRESENTATION_RECALLED;
    sFollowerSpecies = SPECIES_NONE;
    sFollowerIsShiny = FALSE;
    sTrailCount = 0;
}

void FullFollower_DiscardForLink(void)
{
    FullFollower_DiscardForLocalReload();
    sFollowerBattleTransition = FALSE;
    sFollowerWarpTransition = FALSE;
    sFollowerExitLockObserved = FALSE;
}

void FullFollower_OnLocalMapReady(void)
{
    // Restore presentation only after the field returns from battle; scene
    // sprites and object-events are already reconstructed by map loading.
    sFollowerBattleTransition = FALSE;
    // Local map loading can run during Quest Log playback.
    if (QL_IS_PLAYBACK_STATE)
        return;
    if (sFollowerWarpTransition)
        sFollowerExitLockObserved = FALSE;
    if (FindTaskIdByFunc(Task_FullFollower) == TASK_NONE)
        CreateTask(Task_FullFollower, FOLLOWER_TASK_PRIORITY);

    // Map-load and local-return callers invoke this before RunFieldCallback.
    // Never allocate or move a follower before the entrance callback locks
    // controls; the task handles suppression and safe return afterward.
}
