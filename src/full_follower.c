#include "global.h"
#include "event_object_movement.h"
#include "field_player_avatar.h"
#include "full_follower.h"
#include "pokemon.h"
#include "quest_log.h"
#include "script.h"
#include "task.h"
#include "constants/event_object_movement.h"
#include "constants/event_objects.h"
#include "constants/pokemon.h"

#define FOLLOWER_TASK_PRIORITY 0x51
#define FOLLOWER_TRAIL_CAPACITY 8

static bool8 sFollowerEnabled = TRUE;
static u16 sFollowerSpecies = SPECIES_NONE;
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

static void Task_FullFollower(u8 taskId);
static struct ObjectEvent *FindFollowerObject(void);
static u8 GetPrototypeFollowerGraphicsId(u16 species);
static u16 GetEligiblePrototypeFollowerSpecies(void);
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

static u8 GetPrototypeFollowerGraphicsId(u16 species)
{
    // Prototype deliberately uses only overworld assets already present in FireRed Full.
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

static u16 GetEligiblePrototypeFollowerSpecies(void)
{
    u32 i;

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
            return species;
        }
    }

    return SPECIES_NONE;
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

static bool8 ShouldSuppressFollower(void)
{
    // Quest Log playback uses a fixed NPC movement table; follower ID 254
    // is never a map-template NPC and must not enter that playback path.
    if (QL_IS_PLAYBACK_STATE)
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

    if (ArePlayerFieldControlsLocked())
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
    if (ScriptContext_IsEnabled())
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
    u16 species = GetEligiblePrototypeFollowerSpecies();
    u8 graphicsId;

    if (ShouldSuppressFollower() || !sFollowerEnabled || species == SPECIES_NONE)
    {
        // Suppressed presentation must release its object slot AND sprite/OAM
        // allocation, not leave a hidden object behind through bike/Surf/scripts.
        // Remove the runtime-only object, never a saved map object or flag.
        sFollowerSpecies = SPECIES_NONE;
        sTrailCount = 0;
        if (follower != NULL)
            RemoveFullFollowerObjectEvent(follower);
        return;
    }

    graphicsId = GetPrototypeFollowerGraphicsId(species);

    // The graphics slot is resolved through the current runtime species.
    // Destroy the OLD sprite while the slot still resolves to its old graphics:
    // otherwise its tile cleanup could use the NEW species' frame dimensions.
    if (follower != NULL
     && (follower->graphicsId != OBJ_EVENT_GFX_FULL_FOLLOWER
      || sFollowerSpecies != species
      || sFollowerGraphicsId != graphicsId))
    {
        RemoveFullFollowerObjectEvent(follower);
        follower = NULL;
    }

    sFollowerSpecies = species;
    sFollowerGraphicsId = graphicsId;

    if (follower == NULL)
    {
        struct ObjectEvent *player = &gObjectEvents[gPlayerAvatar.objectEventId];
        s16 spawnX;
        s16 spawnY;
        int objectEventId;

        // This also covers safe indoor reappearance after doors/warps.
        // If the tile behind the player is blocked, retry on a later frame.
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
    }

    if (!FollowRecordedPlayerSteps(follower))
    {
        RemoveFullFollowerObjectEvent(follower);
        sFollowerSpecies = SPECIES_NONE;
        sTrailCount = 0;
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

    sFollowerWarpTransition = TRUE;
    sFollowerExitLockObserved = FALSE;
    if (follower != NULL)
        RemoveFullFollowerObjectEvent(follower);
    sFollowerSpecies = SPECIES_NONE;
    sTrailCount = 0;
}

void FullFollower_DiscardForLink(void)
{
    struct ObjectEvent *follower = FindFollowerObject();

    // ResumeMap(TRUE) resets sprite memory immediately afterward. Only drop
    // the transient object-event state here; no sprite teardown or save flag.
    if (follower != NULL)
        follower->active = FALSE;
    sFollowerSpecies = SPECIES_NONE;
    sTrailCount = 0;
    sFollowerWarpTransition = FALSE;
    sFollowerExitLockObserved = FALSE;
}

void FullFollower_OnLocalMapReady(void)
{
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
