#include "global.h"
#include "gflib.h"
#include "gba/flash_internal.h"
#include "load_save.h"
#include "pokemon.h"
#include "pokemon_storage_system.h"
#include "random.h"
#include "item.h"
#include "save_location.h"
#include "berry_powder.h"
#include "overworld.h"
#include "quest_log.h"
#include "sloopsvc.h"
#include "event_data.h"
#include "pokedex.h"
#include "roamer.h"
#include "constants/flags.h"
#include "constants/items.h"
#include "constants/pokedex.h"
#include "constants/vars.h"

#define SAVEBLOCK_MOVE_RANGE    128

#define FULL_SAVE_SCHEMA_VERSION 2
#define FULL_SAVE_SCHEMA_V1      1

static const u8 sFullSaveMagic[4] = {'R', 'F', 'F', 'L'};

struct LoadedSaveData
{
 /*0x0000*/ struct ItemSlot items[BAG_ITEMS_COUNT];
 /*0x0078*/ struct ItemSlot keyItems[BAG_KEYITEMS_COUNT];
 /*0x00F0*/ struct ItemSlot pokeBalls[BAG_POKEBALLS_COUNT];
 /*0x0130*/ struct ItemSlot TMsHMs[BAG_TMHM_COUNT];
 /*0x0230*/ struct ItemSlot berries[BAG_BERRIES_COUNT];
 /*0x02E8*/ struct Mail mail[MAIL_COUNT];
};

// EWRAM DATA
EWRAM_DATA struct SaveBlock2 gSaveBlock2 = {0};
EWRAM_DATA u8 gSaveBlock2_DMA[SAVEBLOCK_MOVE_RANGE] = {0};

EWRAM_DATA struct SaveBlock1 gSaveBlock1 = {0};
EWRAM_DATA u8 gSaveBlock1_DMA[SAVEBLOCK_MOVE_RANGE] = {0};

EWRAM_DATA struct PokemonStorage gPokemonStorage = {0};
EWRAM_DATA u8 gSaveBlock3_DMA[SAVEBLOCK_MOVE_RANGE] = {0};

EWRAM_DATA struct LoadedSaveData gLoadedSaveData = {0};
EWRAM_DATA u32 gLastEncryptionKey = 0;

// IWRAM common
COMMON_DATA bool32 gFlashMemoryPresent = 0;
COMMON_DATA struct SaveBlock1 *gSaveBlock1Ptr = NULL;
COMMON_DATA struct SaveBlock2 *gSaveBlock2Ptr = NULL;
COMMON_DATA struct PokemonStorage *gPokemonStoragePtr = NULL;

void CheckForFlashMemory(void)
{
    if (!IdentifyFlash())
    {
        gFlashMemoryPresent = TRUE;
        InitFlashTimer();
    }
    else
    {
        gFlashMemoryPresent = FALSE;
    }
}

void ClearSav2(void)
{
    CpuFill16(0, &gSaveBlock2, sizeof(struct SaveBlock2) + sizeof(gSaveBlock2_DMA));
}

void ClearSav1(void)
{
    CpuFill16(0, &gSaveBlock1, sizeof(struct SaveBlock1) + sizeof(gSaveBlock1_DMA));
}

static bool32 HasFullSaveMagic(void)
{
    return gSaveBlock1Ptr->fullHeader.magic[0] == sFullSaveMagic[0]
        && gSaveBlock1Ptr->fullHeader.magic[1] == sFullSaveMagic[1]
        && gSaveBlock1Ptr->fullHeader.magic[2] == sFullSaveMagic[2]
        && gSaveBlock1Ptr->fullHeader.magic[3] == sFullSaveMagic[3];
}

static void FullMarkRoamingBeastsSeen(void)
{
    GetSetPokedexFlag(NATIONAL_DEX_SUICUNE, FLAG_SET_SEEN);
    GetSetPokedexFlag(NATIONAL_DEX_RAIKOU, FLAG_SET_SEEN);
    GetSetPokedexFlag(NATIONAL_DEX_ENTEI, FLAG_SET_SEEN);
}

static bool32 FullRestoreEarnedTicket(u16 item, u16 receivedFlag, u16 shipFlag)
{
    FlagSet(receivedFlag);
    FlagSet(shipFlag);
    if (CheckBagHasItem(item, 1))
        return TRUE;
    return AddBagItem(item, 1);
}

static void MigrateFullSaveV1ToV2(void)
{
    u16 mysticState = VarGet(VAR_FULL_MYSTIC_QUEST);
    u16 auroraState = VarGet(VAR_FULL_AURORA_QUEST);
    u16 celebiState = VarGet(VAR_FULL_CELEBI_QUEST);
    u16 roamerSequence = VarGet(VAR_FULL_ROAMER_SEQUENCE);

    // V1 Mystic state 1 meant Celio had already awarded the ticket.
    if (mysticState != 0
     || FlagGet(FLAG_RECEIVED_MYSTIC_TICKET)
     || FlagGet(FLAG_ENABLE_SHIP_NAVEL_ROCK)
     || CheckBagHasItem(ITEM_MYSTIC_TICKET, 1))
    {
        if (FullRestoreEarnedTicket(ITEM_MYSTIC_TICKET, FLAG_RECEIVED_MYSTIC_TICKET, FLAG_ENABLE_SHIP_NAVEL_ROCK))
            VarSet(VAR_FULL_MYSTIC_QUEST, 2);
        else
            VarSet(VAR_FULL_MYSTIC_QUEST, 1);
    }

    // V1 Aurora states 1/2 were the Celio -> Museum -> Celio investigation.
    // Preserve partial progress at the autonomous Museum investigation; state 3
    // (or any canonical receipt evidence) remains a completed award.
    if (auroraState >= 3
     || FlagGet(FLAG_RECEIVED_AURORA_TICKET)
     || FlagGet(FLAG_ENABLE_SHIP_BIRTH_ISLAND)
     || CheckBagHasItem(ITEM_AURORA_TICKET, 1))
    {
        if (FullRestoreEarnedTicket(ITEM_AURORA_TICKET, FLAG_RECEIVED_AURORA_TICKET, FLAG_ENABLE_SHIP_BIRTH_ISLAND))
            VarSet(VAR_FULL_AURORA_QUEST, 2);
        else
            VarSet(VAR_FULL_AURORA_QUEST, 1);
    }
    else if (auroraState != 0)
    {
        VarSet(VAR_FULL_AURORA_QUEST, 1);
    }

    // Preserve terminal Celebi results. A fled V1 encounter becomes an
    // investigation-complete, retryable V2 encounter rather than a softlock.
    if (FlagGet(FLAG_FULL_CELEBI_CAUGHT) || FlagGet(FLAG_FULL_CELEBI_KO_PENDING))
        VarSet(VAR_FULL_CELEBI_QUEST, 3);
    else if (celebiState != 0)
        VarSet(VAR_FULL_CELEBI_QUEST, 2);

    // Old Full saves activated the first roamer immediately when Celio restored
    // the Network Machine. Treat that legacy activation as the V2 first contact
    // having already occurred, so migration never duplicates or replaces a roamer.
    if (FlagGet(FLAG_SYS_CAN_LINK_WITH_RS))
    {
        VarSet(VAR_FULL_BEAST_INTRO, 2);
        FlagSet(FLAG_FULL_HIDE_BEAST_FIRST_CONTACT);
        FullMarkRoamingBeastsSeen();
        if (roamerSequence < 3 && !gSaveBlock1Ptr->roamer.active)
            InitRoamer();
    }

    // Ho-Oh must remain accessible for advanced saves that already captured it
    // or have its old KO-pending state, without fabricating beast progress.
    if (roamerSequence >= 3
     || FlagGet(FLAG_FOUGHT_HO_OH)
     || FlagGet(FLAG_HO_OH_FLEW_AWAY))
        FlagSet(FLAG_FULL_HO_OH_UNLOCKED);
}

bool32 IsFullSaveDataInitialized(void)
{
    return HasFullSaveMagic()
        && gSaveBlock1Ptr->fullHeader.schemaVersion == FULL_SAVE_SCHEMA_VERSION;
}

void InitFullSaveData(void)
{
    if (!HasFullSaveMagic())
    {
        // Schema 0 import: initialize only the Full-owned 16-byte header.
        // Vanilla bag data and all standard save fields remain untouched.
        memset(&gSaveBlock1Ptr->fullHeader, 0, sizeof(gSaveBlock1Ptr->fullHeader));
        gSaveBlock1Ptr->fullHeader.magic[0] = sFullSaveMagic[0];
        gSaveBlock1Ptr->fullHeader.magic[1] = sFullSaveMagic[1];
        gSaveBlock1Ptr->fullHeader.magic[2] = sFullSaveMagic[2];
        gSaveBlock1Ptr->fullHeader.magic[3] = sFullSaveMagic[3];
        gSaveBlock1Ptr->fullHeader.schemaVersion = FULL_SAVE_SCHEMA_VERSION;
        return;
    }

    if (gSaveBlock1Ptr->fullHeader.schemaVersion == FULL_SAVE_SCHEMA_V1)
    {
        MigrateFullSaveV1ToV2();
        gSaveBlock1Ptr->fullHeader.schemaVersion = FULL_SAVE_SCHEMA_VERSION;
    }
}

void SetSaveBlocksPointers(void)
{
    u32 offset;
    struct SaveBlock1** sav1_LocalVar = &gSaveBlock1Ptr;
    void *oldSave = (void *)gSaveBlock1Ptr;

    offset = (Random()) & ((SAVEBLOCK_MOVE_RANGE - 1) & ~3);

    gSaveBlock2Ptr = (void *)(&gSaveBlock2) + offset;
    *sav1_LocalVar = (void *)(&gSaveBlock1) + offset;
    gPokemonStoragePtr = (void *)(&gPokemonStorage) + offset;

    SetBagPocketsPointers();
    QL_AddASLROffset(oldSave);
}

void MoveSaveBlocks_ResetHeap(void)
{
    void *vblankCB, *hblankCB;
    u32 encryptionKey;
    struct SaveBlock2 *saveBlock2Copy;
    struct SaveBlock1 *saveBlock1Copy;
    struct PokemonStorage *pokemonStorageCopy;

    // save interrupt functions and turn them off
    vblankCB = gMain.vblankCallback;
    hblankCB = gMain.hblankCallback;
    gMain.vblankCallback = NULL;
    gMain.hblankCallback = NULL;
    gMain.vblankCounter1 = NULL;
    
    saveBlock2Copy = (struct SaveBlock2 *)(gHeap);
    saveBlock1Copy = (struct SaveBlock1 *)(gHeap + sizeof(struct SaveBlock2));
    pokemonStorageCopy = (struct PokemonStorage *)(gHeap + sizeof(struct SaveBlock2) + sizeof(struct SaveBlock1));

    // backup the saves.
    *saveBlock2Copy = *gSaveBlock2Ptr;
    *saveBlock1Copy = *gSaveBlock1Ptr;
    *pokemonStorageCopy = *gPokemonStoragePtr;

    // change saveblocks' pointers
    SetSaveBlocksPointers(); // unlike Emerald, this does not use
                             // the trainer ID sum for an offset.

    // restore saveblock data since the pointers changed
    *gSaveBlock2Ptr = *saveBlock2Copy;
    *gSaveBlock1Ptr = *saveBlock1Copy;
    *gPokemonStoragePtr = *pokemonStorageCopy;

    // heap was destroyed in the copying process, so reset it
    InitHeap(gHeap, HEAP_SIZE);

    // restore interrupt functions
    gMain.hblankCallback = hblankCB;
    gMain.vblankCallback = vblankCB;

    // create a new encryption key
    encryptionKey = (Random() << 0x10) + (Random());
    ApplyNewEncryptionKeyToAllEncryptedData(encryptionKey);
    gSaveBlock2Ptr->encryptionKey = encryptionKey;
#if REVISION >= 0xA
    svc_SetSaveBlock2(gSaveBlock2Ptr);
#endif
}

u32 UseContinueGameWarp(void)
{
    return gSaveBlock2Ptr->specialSaveWarpFlags & CONTINUE_GAME_WARP;
}

void ClearContinueGameWarpStatus(void)
{
    gSaveBlock2Ptr->specialSaveWarpFlags &= ~CONTINUE_GAME_WARP;
}

void SetContinueGameWarpStatus(void)
{
    gSaveBlock2Ptr->specialSaveWarpFlags |= CONTINUE_GAME_WARP;
}

void SetContinueGameWarpStatusToDynamicWarp(void)
{
    SetContinueGameWarpToDynamicWarp(0);
    gSaveBlock2Ptr->specialSaveWarpFlags |= CONTINUE_GAME_WARP;
}

void ClearContinueGameWarpStatus2(void)
{
    gSaveBlock2Ptr->specialSaveWarpFlags &= ~CONTINUE_GAME_WARP;
}

void SavePlayerParty(void)
{
    int i;

    gSaveBlock1Ptr->playerPartyCount = gPlayerPartyCount;

    for (i = 0; i < PARTY_SIZE; i++)
        gSaveBlock1Ptr->playerParty[i] = gPlayerParty[i];
}

void LoadPlayerParty(void)
{
    int i;

    gPlayerPartyCount = gSaveBlock1Ptr->playerPartyCount;

    for (i = 0; i < PARTY_SIZE; i++)
        gPlayerParty[i] = gSaveBlock1Ptr->playerParty[i];
}

void SaveObjectEvents(void)
{
    int i;

    for (i = 0; i < OBJECT_EVENTS_COUNT; i++)
        gSaveBlock1Ptr->objectEvents[i] = gObjectEvents[i];
}

void LoadObjectEvents(void)
{
    int i;

    for (i = 0; i < OBJECT_EVENTS_COUNT; i++)
        gObjectEvents[i] = gSaveBlock1Ptr->objectEvents[i];
}

void SaveSerializedGame(void)
{
    SavePlayerParty();
    SaveObjectEvents();
}

void LoadSerializedGame(void)
{
    LoadPlayerParty();
    LoadObjectEvents();
}

void LoadPlayerBag(void)
{
    int i;

    // load player items.
    for (i = 0; i < BAG_ITEMS_COUNT; i++)
        gLoadedSaveData.items[i] = gSaveBlock1Ptr->bagPocket_Items[i];

    // load player key items.
    for (i = 0; i < BAG_KEYITEMS_COUNT; i++)
        gLoadedSaveData.keyItems[i] = gSaveBlock1Ptr->bagPocket_KeyItems[i];

    // load player pokeballs.
    for (i = 0; i < BAG_POKEBALLS_COUNT; i++)
        gLoadedSaveData.pokeBalls[i] = gSaveBlock1Ptr->bagPocket_PokeBalls[i];

    // load player TMs and HMs.
    for (i = 0; i < BAG_TMHM_COUNT; i++)
        gLoadedSaveData.TMsHMs[i] = gSaveBlock1Ptr->bagPocket_TMHM[i];

    // load player berries.
    for (i = 0; i < BAG_BERRIES_COUNT; i++)
        gLoadedSaveData.berries[i] = gSaveBlock1Ptr->bagPocket_Berries[i];

    // load mail.
    for (i = 0; i < MAIL_COUNT; i++)
        gLoadedSaveData.mail[i] = gSaveBlock1Ptr->mail[i];

    gLastEncryptionKey = gSaveBlock2Ptr->encryptionKey;
}

void SavePlayerBag(void)
{
    int i;
    u32 encryptionKeyBackup;

    // save player items.
    for (i = 0; i < BAG_ITEMS_COUNT; i++)
        gSaveBlock1Ptr->bagPocket_Items[i] = gLoadedSaveData.items[i];

    // save player key items.
    for (i = 0; i < BAG_KEYITEMS_COUNT; i++)
        gSaveBlock1Ptr->bagPocket_KeyItems[i] = gLoadedSaveData.keyItems[i];

    // save player pokeballs.
    for (i = 0; i < BAG_POKEBALLS_COUNT; i++)
        gSaveBlock1Ptr->bagPocket_PokeBalls[i] = gLoadedSaveData.pokeBalls[i];

    // save player TMs and HMs.
    for (i = 0; i < BAG_TMHM_COUNT; i++)
        gSaveBlock1Ptr->bagPocket_TMHM[i] = gLoadedSaveData.TMsHMs[i];

    // save player berries.
    for (i = 0; i < BAG_BERRIES_COUNT; i++)
        gSaveBlock1Ptr->bagPocket_Berries[i] = gLoadedSaveData.berries[i];

    // save mail.
    for (i = 0; i < MAIL_COUNT; i++)
        gSaveBlock1Ptr->mail[i] = gLoadedSaveData.mail[i];

    encryptionKeyBackup = gSaveBlock2Ptr->encryptionKey;
    gSaveBlock2Ptr->encryptionKey = gLastEncryptionKey;
    ApplyNewEncryptionKeyToBagItems(encryptionKeyBackup);
    gSaveBlock2Ptr->encryptionKey = encryptionKeyBackup;
}

void ApplyNewEncryptionKeyToHword(u16 *hWord, u32 newKey)
{
    *hWord ^= gSaveBlock2Ptr->encryptionKey;
    *hWord ^= newKey;
}

void ApplyNewEncryptionKeyToWord(u32 *word, u32 newKey)
{
    *word ^= gSaveBlock2Ptr->encryptionKey;
    *word ^= newKey;
}

void ApplyNewEncryptionKeyToAllEncryptedData(u32 encryptionKey)
{
    int i;

    for(i = 0; i < NUM_TOWER_CHALLENGE_TYPES; i++)
        ApplyNewEncryptionKeyToWord(&gSaveBlock1Ptr->trainerTower[i].bestTime, encryptionKey);

    ApplyNewEncryptionKeyToGameStats(encryptionKey);
    ApplyNewEncryptionKeyToBagItems_(encryptionKey);
    ApplyNewEncryptionKeyToBerryPowder(encryptionKey);
    ApplyNewEncryptionKeyToWord(&gSaveBlock1Ptr->money, encryptionKey);
    ApplyNewEncryptionKeyToHword(&gSaveBlock1Ptr->coins, encryptionKey);
}
