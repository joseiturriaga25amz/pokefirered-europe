#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

def require(text, *needles):
    for needle in needles:
        assert needle in text, f"missing invariant: {needle}"

def forbid(text, *needles):
    for needle in needles:
        assert needle not in text, f"forbidden stale invariant: {needle}"

def main():
    celio = read("data/maps/OneIsland_PokemonCenter_1F/scripts.inc")
    vermilion = read("data/maps/VermilionCity/scripts.inc")
    one_harbor = read("data/maps/OneIsland_Harbor/scripts.inc")
    pewter_1f = read("data/maps/PewterCity_Museum_1F/scripts.inc")
    pewter_2f = read("data/maps/PewterCity_Museum_2F/scripts.inc")
    berry = read("data/maps/ThreeIsland_BerryForest/scripts.inc")
    one_island = read("data/maps/OneIsland/scripts.inc")
    one_map = read("data/maps/OneIsland/map.json")
    roamer = read("src/roamer.c")
    summit = read("data/maps/NavelRock_Summit/scripts.inc")
    ferry = vermilion
    load = read("src/load_save.c")
    util = read("src/script_pokemon_util.c")
    species_info = read("src/data/pokemon/species_info.h")

    # A-005: Celio is network-only. Legendary ticket ownership and roamer
    # activation must not leak back into his postgame dialogue.
    forbid(
        celio,
        "ITEM_MYSTIC_TICKET",
        "ITEM_AURORA_TICKET",
        "VAR_FULL_MYSTIC_QUEST",
        "VAR_FULL_AURORA_QUEST",
        "special InitRoamer",
        "EventScript_FullPostgameQuests",
    )

    # Mystic arc: all three birds SEEN -> maritime clue -> original ticket.
    require(
        util,
        "NATIONAL_DEX_ARTICUNO, FLAG_GET_SEEN",
        "NATIONAL_DEX_ZAPDOS, FLAG_GET_SEEN",
        "NATIONAL_DEX_MOLTRES, FLAG_GET_SEEN",
    )
    require(
        vermilion,
        "specialvar VAR_RESULT, Full_AreLegendaryBirdsSeen",
        "setvar VAR_FULL_MYSTIC_QUEST, 1",
    )
    require(
        one_harbor,
        "ITEM_MYSTIC_TICKET",
        "setflag FLAG_RECEIVED_MYSTIC_TICKET",
        "setflag FLAG_ENABLE_SHIP_NAVEL_ROCK",
        "setvar VAR_FULL_MYSTIC_QUEST, 2",
    )
    require(
        ferry,
        "goto_if_unset FLAG_ENABLE_SHIP_NAVEL_ROCK",
        "checkitem ITEM_MYSTIC_TICKET",
        "EventScript_SailToNavelRock",
    )

    # Aurora arc: autonomous Pewter investigation -> original Aurora Ticket.
    require(
        pewter_2f,
        "FLAG_SYS_CAN_LINK_WITH_RS",
        "setvar VAR_FULL_AURORA_QUEST, 1",
        "PewterCity_Museum_1F_Text_FullSpaceAnomaly",
    )
    require(
        pewter_1f,
        "ITEM_AURORA_TICKET",
        "setflag FLAG_RECEIVED_AURORA_TICKET",
        "setflag FLAG_ENABLE_SHIP_BIRTH_ISLAND",
        "setvar VAR_FULL_AURORA_QUEST, 2",
    )
    require(
        ferry,
        "goto_if_unset FLAG_ENABLE_SHIP_BIRTH_ISLAND",
        "checkitem ITEM_AURORA_TICKET",
        "EventScript_SailToBirthIsland",
    )

    # Celebi is a Berry Forest investigation, never a reward for capturing beasts.
    forbid(berry, "VAR_FULL_ROAMER_SEQUENCE")
    require(
        berry,
        "setvar VAR_FULL_CELEBI_QUEST, 1",
        "setvar VAR_FULL_CELEBI_QUEST, 2",
        "setvar VAR_FULL_CELEBI_QUEST, 3",
        "FLAG_FULL_CELEBI_CAUGHT",
        "FLAG_FULL_CELEBI_KO_PENDING",
    )

    # First contact shows all three beasts without battle, marks standard Dex
    # seen flags, then activates only Suicune through the vanilla roamer slot.
    require(
        one_map,
        "OBJ_EVENT_GFX_SUICUNE",
        "OBJ_EVENT_GFX_RAIKOU",
        "OBJ_EVENT_GFX_ENTEI",
        "FLAG_FULL_HIDE_BEAST_FIRST_CONTACT",
    )
    require(
        one_island,
        "VAR_FULL_BEAST_INTRO",
        "special Full_MarkRoamingBeastsSeen",
        "special InitRoamer",
        "setvar VAR_FULL_BEAST_INTRO, 2",
    )
    require(
        util,
        "NATIONAL_DEX_SUICUNE, FLAG_SET_SEEN",
        "NATIONAL_DEX_RAIKOU, FLAG_SET_SEEN",
        "NATIONAL_DEX_ENTEI, FLAG_SET_SEEN",
    )
    require(
        roamer,
        "return SPECIES_SUICUNE",
        "return SPECIES_RAIKOU",
        "return SPECIES_ENTEI",
        "VarSet(VAR_FULL_ROAMER_SEQUENCE, 3)",
        "FlagSet(FLAG_FULL_HO_OH_UNLOCKED)",
    )

    # Ho-Oh is independently gated at Navel Rock, while legacy caught/KO states
    # can unlock it during migration without fabricating roamer completion.
    require(
        summit,
        "goto_if_unset FLAG_FULL_HO_OH_UNLOCKED",
        "FLAG_FOUGHT_HO_OH",
        "FLAG_HO_OH_FLEW_AWAY",
    )

    # A-009: core legendaries use the B6 catch-rate polish value; Mew/Celebi
    # retain their existing friendlier 45 rate.
    for species in ("ARTICUNO", "ZAPDOS", "MOLTRES", "MEWTWO", "RAIKOU", "ENTEI", "SUICUNE", "LUGIA", "HO_OH", "DEOXYS"):
        start = species_info.index(f"[SPECIES_{species}]")
        end = species_info.find("\\n    [SPECIES_", start + 1)
        block = species_info[start:] if end == -1 else species_info[start:end]
        assert ".catchRate = 15," in block, species
    for species in ("MEW", "CELEBI"):
        start = species_info.index(f"[SPECIES_{species}]")
        end = species_info.find("\\n    [SPECIES_", start + 1)
        block = species_info[start:] if end == -1 else species_info[start:end]
        assert ".catchRate = 45," in block, species
    require(roamer, "(Random() % 2) == 0")

    # Save schema v2 migration preserves tickets, partial investigations, old
    # roamer activation, and Ho-Oh KO/capture evidence.
    require(
        load,
        "#define FULL_SAVE_SCHEMA_VERSION 2",
        "MigrateFullSaveV1ToV2",
        "FullRestoreEarnedTicket",
        "FLAG_RECEIVED_MYSTIC_TICKET",
        "FLAG_ENABLE_SHIP_NAVEL_ROCK",
        "FLAG_RECEIVED_AURORA_TICKET",
        "FLAG_ENABLE_SHIP_BIRTH_ISLAND",
        "VarSet(VAR_FULL_BEAST_INTRO, 2)",
        "FLAG_FOUGHT_HO_OH",
        "FLAG_HO_OH_FLEW_AWAY",
        "FlagSet(FLAG_FULL_HO_OH_UNLOCKED)",
    )

    print("B6 Legendary Narrative V2 state, migration, and ownership invariants validated")

if __name__ == "__main__":
    main()
