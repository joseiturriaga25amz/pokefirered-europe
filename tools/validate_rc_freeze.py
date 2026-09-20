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
        "RC freeze validator passed: save layout/migration, berry economy/effects, "
        "fossils, Dojo, Altering Cave, evolutions and Porygon."
    )


if __name__ == "__main__":
    main()
