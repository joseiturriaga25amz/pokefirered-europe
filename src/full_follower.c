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

static bool8 sFollowerEnabled = TRUE;
static u16 sFollowerSpecies = SPECIES_NONE;
// The graphics slot is 8-bit; the selected species is held only at runtime.
static u8 sFollowerGraphicsId = OBJ_EVENT_GFX_PIKACHU;

static void Task_FullFollower(u8 taskId);
static struct ObjectEvent *FindFollowerObject(void);
static u8 GetPrototypeFollowerGraphicsId(u16 species);
static u16 GetEligiblePrototypeFollowerSpecies(void);
static bool8 ShouldSuppressFollower(void);
static void PositionFollowerBehindPlayer(struct ObjectEvent *follower, s16 x, s16 y);
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

    // The caller separately checks the party lead and the on/off preference.
    if (TestPlayerAvatarFlags(PLAYER_AVATAR_FLAG_MACH_BIKE
                            | PLAYER_AVATAR_FLAG_ACRO_BIKE
                            | PLAYER_AVATAR_FLAG_SURFING))
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
}

static void RefreshFollower(void)
{
    struct ObjectEvent *follower = FindFollowerObject();
    u16 species = GetEligiblePrototypeFollowerSpecies();
    u8 graphicsId;

    if (!sFollowerEnabled || species == SPECIES_NONE || ShouldSuppressFollower())
    {
        // Suppressed presentation must release its object slot AND sprite/OAM
        // allocation, not leave a hidden object behind through bike/Surf/scripts.
        // Remove the runtime-only object, never a saved map object or flag.
        sFollowerSpecies = SPECIES_NONE;
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
            MOVEMENT_TYPE_COPY_PLAYER,
            OBJ_EVENT_ID_FULL_FOLLOWER,
            player->currentCoords.x,
            player->currentCoords.y,
            player->currentElevation);

        if (objectEventId >= OBJECT_EVENTS_COUNT)
            return;

        follower = &gObjectEvents[objectEventId];
        PositionFollowerBehindPlayer(follower, spawnX, spawnY);
    }

    // The object-event engine owns sprite invisibility/off-screen culling.
    // Forcing invisible = FALSE here could expose an off-screen sprite.
}

static void Task_FullFollower(u8 taskId)
{
    (void)taskId;
    RefreshFollower();
}

void FullFollower_DiscardForLink(void)
{
    struct ObjectEvent *follower = FindFollowerObject();

    // ResumeMap(TRUE) resets sprite memory immediately afterward. Only drop
    // the transient object-event state here; no sprite teardown or save flag.
    if (follower != NULL)
        follower->active = FALSE;
    sFollowerSpecies = SPECIES_NONE;
}

void FullFollower_OnLocalMapReady(void)
{
    // Local map loading can run during Quest Log playback.
    if (QL_IS_PLAYBACK_STATE)
        return;
    if (FindTaskIdByFunc(Task_FullFollower) == TASK_NONE)
        CreateTask(Task_FullFollower, FOLLOWER_TASK_PRIORITY);

    RefreshFollower();
}
