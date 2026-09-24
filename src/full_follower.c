#include "global.h"
#include "event_object_movement.h"
#include "field_player_avatar.h"
#include "full_follower.h"
#include "pokemon.h"
#include "script.h"
#include "task.h"
#include "constants/event_object_movement.h"
#include "constants/event_objects.h"
#include "constants/pokemon.h"

#define FOLLOWER_TASK_PRIORITY 0x51

static bool8 sFollowerEnabled = TRUE;
static u16 sFollowerSpecies = SPECIES_NONE;
static u8 sFollowerGraphicsId = OBJ_EVENT_GFX_PIKACHU;

static void Task_FullFollower(u8 taskId);
static struct ObjectEvent *FindFollowerObject(void);
static u8 GetPrototypeFollowerGraphicsId(u16 species);
static u16 GetEligiblePrototypeFollowerSpecies(void);
static bool8 ShouldHideFollower(void);
static void PositionFollowerBehindPlayer(struct ObjectEvent *follower);
static void RefreshFollower(void);

void FullFollower_SetEnabled(bool8 enabled)
{
    sFollowerEnabled = enabled;
}

bool8 FullFollower_IsEnabled(void)
{
    return sFollowerEnabled;
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

        if (species != SPECIES_NONE
         && hp != 0
         && !isEgg
         && GetPrototypeFollowerGraphicsId(species) != 0xFF)
            return species;
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

static bool8 ShouldHideFollower(void)
{
    if (!sFollowerEnabled || sFollowerSpecies == SPECIES_NONE)
        return TRUE;

    if (TestPlayerAvatarFlags(PLAYER_AVATAR_FLAG_MACH_BIKE
                            | PLAYER_AVATAR_FLAG_ACRO_BIKE
                            | PLAYER_AVATAR_FLAG_SURFING))
        return TRUE;

    // The prototype suppresses presentation during scripted field control.
    // This keeps follower state out of cutscenes/trainer-sight/link-sensitive scripts.
    if (ScriptContext2_IsEnabled())
        return TRUE;

    return FALSE;
}

static void PositionFollowerBehindPlayer(struct ObjectEvent *follower)
{
    struct ObjectEvent *player = &gObjectEvents[gPlayerAvatar.objectEventId];
    s16 x = player->currentCoords.x;
    s16 y = player->currentCoords.y;

    switch (player->facingDirection)
    {
    case DIR_NORTH:
        y++;
        break;
    case DIR_SOUTH:
        y--;
        break;
    case DIR_WEST:
        x++;
        break;
    case DIR_EAST:
        x--;
        break;
    }

    MoveObjectEventToMapCoords(follower, x, y);
    follower->currentElevation = player->currentElevation;
    follower->previousElevation = player->currentElevation;
}

static void RefreshFollower(void)
{
    struct ObjectEvent *follower = FindFollowerObject();
    u16 species = GetEligiblePrototypeFollowerSpecies();
    u8 graphicsId;

    if (species == SPECIES_NONE)
    {
        sFollowerSpecies = SPECIES_NONE;
        if (follower != NULL)
            gSprites[follower->spriteId].invisible = TRUE;
        return;
    }

    graphicsId = GetPrototypeFollowerGraphicsId(species);
    sFollowerSpecies = species;
    sFollowerGraphicsId = graphicsId;

    if (follower == NULL)
    {
        struct ObjectEvent *player = &gObjectEvents[gPlayerAvatar.objectEventId];
        int objectEventId = SpawnSpecialObjectEventParameterized(
            graphicsId,
            MOVEMENT_TYPE_COPY_PLAYER,
            OBJ_EVENT_ID_FULL_FOLLOWER,
            player->currentCoords.x,
            player->currentCoords.y,
            player->currentElevation);

        if (objectEventId >= OBJECT_EVENTS_COUNT)
            return;

        follower = &gObjectEvents[objectEventId];
        PositionFollowerBehindPlayer(follower);
    }
    else if (follower->graphicsId != graphicsId)
    {
        ObjectEventSetGraphicsId(follower, graphicsId);
        PositionFollowerBehindPlayer(follower);
    }

    gSprites[follower->spriteId].invisible = ShouldHideFollower();
}

static void Task_FullFollower(u8 taskId)
{
    (void)taskId;
    RefreshFollower();
}

void FullFollower_OnLocalMapReady(void)
{
    // Link maps never call this hook. The prototype is deliberately local-only.
    if (FindTaskIdByFunc(Task_FullFollower) == TASK_NONE)
        CreateTask(Task_FullFollower, FOLLOWER_TASK_PRIORITY);

    RefreshFollower();
}
