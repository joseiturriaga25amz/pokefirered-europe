#!/usr/bin/env python3
"""Static RC audit gates for frozen Full-gameplay requirements."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text()


def main() -> None:
    prices = {
        "ITEM_CHERI_BERRY": 200,
        "ITEM_CHESTO_BERRY": 200,
        "ITEM_PECHA_BERRY": 200,
        "ITEM_RAWST_BERRY": 200,
        "ITEM_ASPEAR_BERRY": 200,
        "ITEM_PERSIM_BERRY": 300,
        "ITEM_ORAN_BERRY": 300,
        "ITEM_LEPPA_BERRY": 500,
        "ITEM_SITRUS_BERRY": 800,
        "ITEM_LUM_BERRY": 1200,
        "ITEM_FIGY_BERRY": 600,
        "ITEM_WIKI_BERRY": 600,
        "ITEM_MAGO_BERRY": 600,
        "ITEM_AGUAV_BERRY": 600,
        "ITEM_IAPAPA_BERRY": 600,
        "ITEM_POMEG_BERRY": 1500,
        "ITEM_KELPSY_BERRY": 1500,
        "ITEM_QUALOT_BERRY": 1500,
        "ITEM_HONDEW_BERRY": 1500,
        "ITEM_GREPA_BERRY": 1500,
        "ITEM_TAMATO_BERRY": 1500,
        "ITEM_LIECHI_BERRY": 2500,
        "ITEM_GANLON_BERRY": 2500,
        "ITEM_SALAC_BERRY": 2500,
        "ITEM_PETAYA_BERRY": 2500,
        "ITEM_APICOT_BERRY": 2500,
        "ITEM_LANSAT_BERRY": 5000,
        "ITEM_STARF_BERRY": 5000,
    }

    items = json.loads(read("src/data/items.json"))["items"]
    by_id = {item["itemId"]: item for item in items}
    for item_id, expected in prices.items():
        assert by_id[item_id]["price"] == expected, (
            item_id,
            by_id[item_id]["price"],
            expected,
        )

    frozen_item_prices = {
        "ITEM_SOFT_SAND": 3000, "ITEM_HARD_STONE": 3000,
        "ITEM_MIRACLE_SEED": 3000, "ITEM_BLACK_GLASSES": 3000,
        "ITEM_BLACK_BELT": 3000, "ITEM_MAGNET": 3000,
        "ITEM_MYSTIC_WATER": 3000, "ITEM_SHARP_BEAK": 3000,
        "ITEM_POISON_BARB": 3000, "ITEM_NEVER_MELT_ICE": 3000,
        "ITEM_SPELL_TAG": 3000, "ITEM_TWISTED_SPOON": 3000,
        "ITEM_CHARCOAL": 3000, "ITEM_DRAGON_FANG": 3000,
        "ITEM_SILK_SCARF": 3000, "ITEM_SILVER_POWDER": 3000,
        "ITEM_QUICK_CLAW": 4000, "ITEM_LUCKY_PUNCH": 4000,
        "ITEM_STICK": 4000, "ITEM_SCOPE_LENS": 5000,
        "ITEM_FOCUS_BAND": 5000, "ITEM_METAL_POWDER": 6000,
        "ITEM_SHELL_BELL": 6000, "ITEM_BRIGHT_POWDER": 7500,
        "ITEM_LIGHT_BALL": 8000, "ITEM_LEFTOVERS": 12000,
        "ITEM_THICK_CLUB": 12000, "ITEM_CHOICE_BAND": 15000,
        "ITEM_SUN_STONE": 3000, "ITEM_MOON_STONE": 3000,
        "ITEM_KINGS_ROCK": 5000, "ITEM_METAL_COAT": 5000,
        "ITEM_DRAGON_SCALE": 5000, "ITEM_UP_GRADE": 7500,
        "ITEM_PP_UP": 9800, "ITEM_ETHER": 1200,
        "ITEM_MAX_ETHER": 2000, "ITEM_ELIXIR": 3000,
        "ITEM_MAX_ELIXIR": 4500, "ITEM_LUCKY_EGG": 30000,
        "ITEM_TM44": 3000,
    }
    for item_id, expected in frozen_item_prices.items():
        assert by_id[item_id]["price"] == expected, (
            item_id,
            by_id[item_id]["price"],
            expected,
        )

    celadon = read("data/maps/CeladonCity_DepartmentStore_4F/scripts.inc")
    assert "goto_if_set FLAG_SYS_NATIONAL_DEX" in celadon
    pre_nat = celadon[
        celadon.index("CeladonCity_DepartmentStore_4F_Items::"):
        celadon.index("CeladonCity_DepartmentStore_4F_PostNationalItems::")
    ]
    post_nat = celadon[celadon.index("CeladonCity_DepartmentStore_4F_PostNationalItems::"):]
    for item_id in (
        "ITEM_SUN_STONE", "ITEM_MOON_STONE", "ITEM_KINGS_ROCK",
        "ITEM_METAL_COAT", "ITEM_DRAGON_SCALE", "ITEM_UP_GRADE",
        "ITEM_LUCKY_EGG", "ITEM_ETHER", "ITEM_MAX_ETHER",
        "ITEM_ELIXIR", "ITEM_MAX_ELIXIR",
    ):
        assert item_id not in pre_nat, item_id
        assert item_id in post_nat, item_id

    for item_id in (
        "ITEM_EXP_SHARE", "ITEM_AMULET_COIN", "ITEM_SOOTHE_BELL", "ITEM_MACHO_BRACE"
    ):
        assert item_id not in celadon, item_id

    ev_berries = (
        "ITEM_POMEG_BERRY",
        "ITEM_KELPSY_BERRY",
        "ITEM_QUALOT_BERRY",
        "ITEM_HONDEW_BERRY",
        "ITEM_GREPA_BERRY",
        "ITEM_TAMATO_BERRY",
    )
    for item_id in ev_berries:
        item = by_id[item_id]
        assert item["type"] == "ITEM_TYPE_PARTY_MENU", item_id
        assert item["fieldUseFunc"] == "FieldUseFunc_Medicine", item_id

    effects = read("src/data/pokemon/item_effects.h")
    assert effects.count("ITEM6_SUBTRACT_EV") >= 6
    for name in ("Pomeg", "Kelpsy", "Qualot", "Hondew", "Grepa", "Tamato"):
        assert f"sItemEffect_{name}Berry" in effects, name

    pokemon = read("src/pokemon.c")
    assert "s8 evChange;" in pokemon
    assert "bool8 friendshipOnly = FALSE;" in pokemon
    assert "item >= ITEM_POMEG_BERRY && item <= ITEM_TAMATO_BERRY" in pokemon

    # A-002 / SAVE-001 / SAVE-004: vanilla bag layout and Full save migration.
    global_h = read("include/global.h")
    assert "/*0x348C*/ u8 unused_348C[400];" in global_h
    assert "/*0x3D24*/ struct FullSaveHeader fullHeader;" in global_h
    assert "sizeof(struct SaveBlock1) == 0x3D68" in global_h
    assert "FullHeaderOffset" in global_h

    load_save = read("src/load_save.c")
    assert "static const u8 sFullSaveMagic[4] = {'R', 'F', 'F', 'L'};" in load_save
    assert "FULL_SAVE_SCHEMA_VERSION 1" in load_save
    init_start = load_save.index("void InitFullSaveData(void)")
    init_end = load_save.index("void SetSaveBlocksPointers(void)", init_start)
    init_full = load_save[init_start:init_end]
    assert "memset(&gSaveBlock1Ptr->fullHeader" in init_full
    assert "bagPocket_Items" not in init_full
    assert "unused_348C" not in init_full

    # QOL-001 / unique-TM economy: TMs are permanent single-copy unlocks.
    item_c = read("src/item.c")
    assert "if (pocket == POCKET_TM_CASE - 1 && itemId < ITEM_HM01)" in item_c
    assert "if (count != 1 || CheckBagHasItem(itemId, 1))" in item_c
    assert "if (pocket == POCKET_TM_CASE - 1 && itemId < ITEM_HM01 && count != 1)" in item_c

    shop_c = read("src/shop.c")
    assert "if (itemId >= ITEM_TM01 && itemId < ITEM_HM01 && BagGetQuantityByItemId(itemId) > 0)" in shop_c
    assert "if (tItemId >= ITEM_TM01 && tItemId < ITEM_HM01)" in shop_c
    assert "sShopData.maxQuantity = 1;" in shop_c

    tm_case = read("src/tm_case.c")
    assert "static void Task_SelectedTMHM_Sell" in tm_case
    sell_start = tm_case.index("static void Task_SelectedTMHM_Sell(u8 taskId)")
    sell_end = tm_case.index("\n}", sell_start) + 2
    sell_func = tm_case[sell_start:sell_end]
    assert "RemoveBagItem" not in sell_func
    assert "gText_OhNoICantBuyThat" in sell_func

    # COMP-001: do not extend Gen III species/move/item ID spaces.
    species_h = read("include/constants/species.h")
    moves_h = read("include/constants/moves.h")
    items_h = read("include/constants/items.h")
    assert "#define SPECIES_EGG 412" in species_h
    assert "#define NUM_SPECIES SPECIES_EGG" in species_h
    assert "#define MOVES_COUNT 355" in moves_h
    assert "#define ITEMS_COUNT 375" in items_h

    two_island = read("data/maps/TwoIsland/scripts.inc")
    assert (
        two_island.count(
            "goto_if_set FLAG_SYS_NATIONAL_DEX, "
            "TwoIsland_EventScript_ShopPostNational"
        )
        == 4
    )
    for item_id in prices:
        assert item_id in two_island, item_id

    mt_moon = read("data/maps/MtMoon_B2F/scripts.inc")
    assert "goto_if_unset FLAG_REVIVED_HELIX" in mt_moon
    assert "goto_if_unset FLAG_REVIVED_DOME" in mt_moon
    assert "MtMoon_B2F_EventScript_SecondFossilNoRoom" in mt_moon

    lab = read("data/maps/CinnabarIsland_PokemonLab_ExperimentRoom/scripts.inc")
    for flag in ("FLAG_REVIVED_HELIX", "FLAG_REVIVED_DOME", "FLAG_REVIVED_AMBER"):
        assert flag in lab, flag

    dojo = read("data/maps/SaffronCity_Dojo/scripts.inc")
    for token in (
        "FLAG_FULL_DOJO_CHOSE_HITMONLEE",
        "FLAG_FULL_DOJO_SECOND_REWARD",
        "TRAINER_RS_BLACK_BELT",
        "SaffronCity_Dojo_EventScript_SecondRewardNoRoom",
    ):
        assert token in dojo, token

    celio = read("data/maps/OneIsland_PokemonCenter_1F/scripts.inc")
    for token in (
        "setflag FLAG_RECEIVED_MYSTIC_TICKET",
        "setflag FLAG_ENABLE_SHIP_NAVEL_ROCK",
        "setflag FLAG_RECEIVED_AURORA_TICKET",
        "setflag FLAG_ENABLE_SHIP_BIRTH_ISLAND",
    ):
        assert token in celio, token
    assert celio.count("special InitRoamer") == 1

    evo = read("src/data/pokemon/evolution.h")
    for token in (
        "{EVO_ITEM, ITEM_SUN_STONE, SPECIES_ESPEON}",
        "{EVO_ITEM, ITEM_MOON_STONE, SPECIES_UMBREON}",
        "[SPECIES_GOLBAT]     = {{EVO_FRIENDSHIP, 0, SPECIES_CROBAT}}",
        "[SPECIES_KADABRA]    = {{EVO_LEVEL, 36, SPECIES_ALAKAZAM}}",
        "[SPECIES_MACHOKE]    = {{EVO_LEVEL, 36, SPECIES_MACHAMP}}",
        "[SPECIES_GRAVELER]   = {{EVO_LEVEL, 36, SPECIES_GOLEM}}",
        "[SPECIES_HAUNTER]    = {{EVO_LEVEL, 36, SPECIES_GENGAR}}",
    ):
        assert token in evo, token

    wild = json.loads(read("src/data/wild_encounters.json"))
    encounters = wild["wild_encounter_groups"][0]["encounters"]
    cave = [
        encounter
        for encounter in encounters
        if encounter.get("map") == "MAP_SIX_ISLAND_ALTERING_CAVE"
        and "FireRed" in encounter.get("base_label", "")
    ]
    expected_species = (
        "SPECIES_ZUBAT",
        "SPECIES_MAREEP",
        "SPECIES_PINECO",
        "SPECIES_HOUNDOUR",
        "SPECIES_TEDDIURSA",
        "SPECIES_AIPOM",
        "SPECIES_SHUCKLE",
        "SPECIES_STANTLER",
        "SPECIES_SMEARGLE",
    )
    assert len(cave) == 9, len(cave)
    for encounter, species in zip(cave, expected_species):
        mons = encounter["land_mons"]["mons"]
        assert mons and all(mon["species"] == species for mon in mons), (
            encounter["base_label"],
            species,
        )

    cave_script = read("data/maps/SixIsland_AlteringCave/scripts.inc")
    for value in range(9):
        assert f"setvar VAR_ALTERING_CAVE_WILD_SET, {value}" in cave_script, value

    game_corner = read("data/maps/CeladonCity_GameCorner_PrizeRoom/scripts.inc")
    start = game_corner.index("CeladonCity_GameCorner_PrizeRoom_EventScript_Porygon::")
    porygon = game_corner[start:]
    assert "setvar VAR_TEMP_2, 5000" in porygon

    print(
        "RC freeze validator passed: Gen III ID/save compatibility, frozen economy, "
        "berry effects, fossils, Dojo, Altering Cave, evolutions and Porygon."
    )


if __name__ == "__main__":
    main()
