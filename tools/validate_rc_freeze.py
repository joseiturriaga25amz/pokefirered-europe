#!/usr/bin/env python3
"""Static RC audit gates for frozen Full-gameplay requirements."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text()


def c_function(text: str, signature: str) -> str:
    """Return the complete function definition, skipping forward declarations."""
    start = text.find(signature)
    while start != -1:
        pos = start + len(signature)
        while pos < len(text) and text[pos].isspace():
            pos += 1
        if pos < len(text) and text[pos] == "{":
            open_brace = pos
            depth = 0
            for i in range(open_brace, len(text)):
                ch = text[i]
                if ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                    if depth == 0:
                        return text[start:i + 1]
            raise AssertionError(f"unterminated function: {signature}")
        start = text.find(signature, start + 1)
    raise AssertionError(f"function definition not found: {signature}")


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

    # ECO-001/QOL-014: history availability must exist, not merely the
    # correct item price in items.json.
    for item_id in (
        "ITEM_SOFT_SAND", "ITEM_HARD_STONE", "ITEM_MIRACLE_SEED",
        "ITEM_BLACK_GLASSES", "ITEM_BLACK_BELT", "ITEM_MAGNET",
        "ITEM_MYSTIC_WATER", "ITEM_SHARP_BEAK", "ITEM_POISON_BARB",
        "ITEM_NEVER_MELT_ICE", "ITEM_SPELL_TAG", "ITEM_TWISTED_SPOON",
        "ITEM_CHARCOAL", "ITEM_DRAGON_FANG", "ITEM_SILK_SCARF",
        "ITEM_SILVER_POWDER",
    ):
        assert item_id in pre_nat, item_id

    celadon_2f = read("data/maps/CeladonCity_DepartmentStore_2F/scripts.inc")
    assert "ITEM_TM44" in celadon_2f
    celadon_5f = read("data/maps/CeladonCity_DepartmentStore_5F/scripts.inc")
    assert "ITEM_PP_UP" in celadon_5f

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

    # QOL-007: validate the Spanish script actually compiled by firered_es_modern.
    repel = read("data/scripts/spanish/repel.inc")
    for token in (
        "checkitem ITEM_REPEL",
        "checkitem ITEM_SUPER_REPEL",
        "checkitem ITEM_MAX_REPEL",
        "msgbox Text_FullUseAnotherRepel, MSGBOX_YESNO",
        "compare VAR_FULL_LAST_REPEL, ITEM_REPEL",
        "compare VAR_FULL_LAST_REPEL, ITEM_SUPER_REPEL",
        "compare VAR_FULL_LAST_REPEL, ITEM_MAX_REPEL",
        "removeitem ITEM_REPEL",
        "removeitem ITEM_SUPER_REPEL",
        "removeitem ITEM_MAX_REPEL",
        "setvar VAR_REPEL_STEP_COUNT, 100",
        "setvar VAR_REPEL_STEP_COUNT, 200",
        "setvar VAR_REPEL_STEP_COUNT, 250",
    ):
        assert token in repel, token
    assert "goto_if_eq VAR_RESULT, NO, EventScript_FullRepelEnd" in repel
    assert "goto EventScript_FullUseFallbackRepel" in repel

    # QOL-001 / unique-TM economy: TMs are permanent single-copy unlocks.
    item_c = read("src/item.c")
    assert "if (pocket == POCKET_TM_CASE - 1 && itemId < ITEM_HM01)" in item_c
    assert "if (count != 1 || CheckBagHasItem(itemId, 1))" in item_c
    assert "if (pocket == POCKET_TM_CASE - 1 && itemId < ITEM_HM01 && count != 1)" in item_c

    shop_c = read("src/shop.c")
    assert "if (itemId >= ITEM_TM01 && itemId < ITEM_HM01 && BagGetQuantityByItemId(itemId) > 0)" in shop_c
    assert "if (tItemId >= ITEM_TM01 && tItemId < ITEM_HM01)" in shop_c
    assert "sShopData.maxQuantity = 1;" in shop_c

    # QOL-VEND-001: Celadon vending reuses the shop quantity selector.
    for item_id, expected in (
        ("ITEM_FRESH_WATER", 200),
        ("ITEM_SODA_POP", 300),
        ("ITEM_LEMONADE", 350),
    ):
        assert by_id[item_id]["price"] == expected, (item_id, by_id[item_id]["price"], expected)
    assert "MART_TYPE_VENDING" in shop_c
    assert "static const struct MenuAction sVendingMenuActions[]" in shop_c
    vending_actions = shop_c[shop_c.index("static const struct MenuAction sVendingMenuActions[]"):shop_c.index("static const u16 sVendingMachineItems[]")]
    assert "{gText_ShopSell" not in vending_actions
    assert "AdjustQuantityAccordingToDPadInput(&tItemCount, sShopData.maxQuantity)" in shop_c
    assert "AddBagItem(tItemId, tItemCount) == TRUE" in shop_c
    assert "RemoveMoney(&gSaveBlock1Ptr->money, sShopData.itemPrice)" in shop_c

    vending = read("data/maps/CeladonCity_DepartmentStore_Roof/scripts.inc")
    vending_start = vending.index("CeladonCity_DepartmentStore_Roof_EventScript_VendingMachine::")
    vending_runtime = vending[vending_start:]
    assert "callnative CreateVendingMachineMenu" in vending_runtime
    assert "waitstate" in vending_runtime
    assert "checkmoney 200" not in vending_runtime
    assert "additem VAR_TEMP_0" not in vending_runtime
    assert "CeladonCity_DepartmentStore_Roof_EventScript_AskGiveFreshWater::" in vending
    assert "CeladonCity_DepartmentStore_Roof_EventScript_GiveLemonade::" in vending

    tm_case = read("src/tm_case.c")
    assert "static void Task_SelectedTMHM_Sell" in tm_case
    party_menu = read("src/party_menu.c")
    learned_func = c_function(party_menu, "static void Task_LearnedMove(u8 taskId)")
    assert "RemoveBagItem" not in learned_func

    replace_func = c_function(party_menu, "static void Task_ReplaceMoveWithTMHM(u8 taskId)")
    assert "RemoveBagItem" not in replace_func

    sell_func = c_function(tm_case, "static void Task_SelectedTMHM_Sell(u8 taskId)")
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

    # A-005 supersedes the old Celio-owned ticket/roamer handoff. B0 must not
    # preserve that pre-A-005 implementation as acceptance truth. The V2
    # narrative is validated by its dedicated implementation block; this
    # freeze validator continues to protect structural/save compatibility only.

    # EVO-005..010: direct-use trade-evolution items must be recognized as
    # Pokemon-usable items and carry the evolution-stone effect bit.
    items_h = read("include/constants/items.h")
    for token in (
        "ITEM_KINGS_ROCK",
        "ITEM_METAL_COAT",
        "ITEM_DRAGON_SCALE",
        "ITEM_UP_GRADE",
    ):
        assert token in items_h
    assert "(item) == ITEM_KINGS_ROCK" in items_h
    assert "(item) == ITEM_METAL_COAT" in items_h
    assert "(item) == ITEM_DRAGON_SCALE" in items_h
    assert "(item) == ITEM_UP_GRADE" in items_h

    item_effects = read("src/data/pokemon/item_effects.h")
    for token in (
        "[ITEM_KINGS_ROCK - ITEM_POTION]    = sItemEffect_KingsRock",
        "[ITEM_METAL_COAT - ITEM_POTION]    = sItemEffect_MetalCoat",
        "[ITEM_DRAGON_SCALE - ITEM_POTION]  = sItemEffect_DragonScale",
        "[ITEM_UP_GRADE - ITEM_POTION]      = sItemEffect_UpGrade",
    ):
        assert token in item_effects
    assert item_effects.count("[4] = ITEM4_EVO_STONE") >= 10

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

    # RC-F040 / EVO-013: Full normal evolution scenes must not re-apply
    # vanilla's National-Dex animation-time cancellation after a valid target
    # (e.g. Golbat -> Crobat) has already been selected.
    evolution_scene = read("src/evolution_scene.c")
    normal_evolution_scene = c_function(
        evolution_scene, "static void Task_EvolutionScene(u8 taskId)"
    )
    assert "gTasks[taskId].tPostEvoSpecies > SPECIES_MEW" not in normal_evolution_scene
    assert "Automatically cancel if the Pokemon would evolve" not in normal_evolution_scene

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
    assert "setvar VAR_TEMP_2, 5500" in porygon

    script_menu = read("src/script_menu.c")
    assert 'sText_FullPorygon5500Coins' in script_menu
    assert 'PORYGON  5.500 FICHAS' in script_menu

    oak_lab = read("data/maps/PalletTown_ProfessorOaksLab/scripts.inc")
    natdex = oak_lab[oak_lab.index("PalletTown_ProfessorOaksLab_EventScript_TryStartNationalDexScene::"):oak_lab.index("PalletTown_ProfessorOaksLab_EventScript_DontStartNationalDexScene::")]
    assert "goto_if_lt VAR_0x8009, 60" not in natdex
    assert "goto_if_unset FLAG_WORLD_MAP_ONE_ISLAND" in natdex

    reminder_text = read("data/maps/TwoIsland_House/text.inc")
    assert "2.000" in reminder_text
    active_reminder = reminder_text[reminder_text.index("TwoIsland_House_Text_WantMeToTeachMove::"):reminder_text.index("TwoIsland_House_Text_TutorWhichMon::")]
    assert "MUSHROOM" not in active_reminder

    summary_ui = read("src/pokemon_summary_screen.c")
    assert "ShowOrHideHpBarObjs(sMonSummaryScreen->showFullEvView);" in summary_ui
    assert "ShowOrHideExpBarObjs(sMonSummaryScreen->showFullEvView);" in summary_ui
    assert 'sText_FullMoveCategoryPhysical[] = _("FISICO")' in summary_ui
    assert 'sText_FullMoveCategorySpecial[] = _("ESPECIAL")' in summary_ui
    assert 'sText_FullMoveCategoryStatus[] = _("ESTADO")' in summary_ui
    assert "category = gBattleMoves[move].category;" in summary_ui
    assert "sText_FullMoveCategories[category]" in summary_ui

    aide_rules = (
        ("data/maps/Route2_EastBuilding/scripts.inc", "FLAG_BADGE02_GET", "FLAG_GOT_HM05", "ITEM_HM05", "MEDALLA CASCADA"),
        ("data/maps/Route10_PokemonCenter_1F/scripts.inc", "FLAG_BADGE03_GET", "FLAG_GOT_EVERSTONE_FROM_OAKS_AIDE", "ITEM_EVERSTONE", "MEDALLA TRUENO"),
        ("data/maps/Route11_EastEntrance_2F/scripts.inc", "FLAG_BADGE03_GET", "FLAG_GOT_ITEMFINDER", "ITEM_ITEMFINDER", "MEDALLA TRUENO"),
        ("data/maps/Route16_NorthEntrance_2F/scripts.inc", "FLAG_BADGE04_GET", "FLAG_GOT_AMULET_COIN_FROM_OAKS_AIDE", "ITEM_AMULET_COIN", "MEDALLA ARCOIRIS"),
        ("data/maps/Route15_WestEntrance_2F/scripts.inc", "FLAG_BADGE04_GET", "FLAG_GOT_EXP_SHARE_FROM_OAKS_AIDE", "ITEM_EXP_SHARE", "MEDALLA ARCOIRIS"),
    )
    for path, badge, reward_flag, item, badge_text in aide_rules:
        aide_script = read(path)
        assert "GetPokedexCount" not in aide_script, path
        assert "REQUIRED_SEEN_MONS" not in aide_script, path
        assert "REQUIRED_OWNED_MONS" not in aide_script, path
        assert "REQUIRED_CAUGHT_MONS" not in aide_script, path
        assert f"goto_if_unset {badge}" in aide_script, path
        assert f"goto_if_set {reward_flag}" in aide_script, path
        assert f"checkitemspace {item}" in aide_script, path
        aide_text = read(path.replace("scripts.inc", "text_es.inc"))
        assert badge_text in aide_text, path
        assert "caught or owned" not in aide_text, path

    # ECO-008: Resort Gorgeous can form the intended ~30k VS Seeker circuit.
    trainers = json.loads(read("src/data/trainers.json"))["trainers"]
    by_trainer = {t["id"]: t for t in trainers}
    for trainer_id in (
        "TRAINER_LADY_JACKI",
        "TRAINER_LADY_GILLIAN",
        "TRAINER_PAINTER_CELINA",
    ):
        assert by_trainer[trainer_id]["trainerClass"] == "TRAINER_CLASS_LADY", trainer_id

    parties = read("src/data/trainer_parties.h")
    jacki_party = parties[
        parties.index("sParty_LadyJacki"):parties.index("sParty_PainterCelina")
    ]
    assert ".lvl = 50" in jacki_party
    celina_party = parties[
        parties.index("sParty_PainterCelina"):parties.index("sParty_PainterRayna")
    ]
    assert ".lvl = 50" in celina_party
    gillian_party = parties[
        parties.index("sParty_LadyGillian"):parties.index("sParty_YoungsterDestin")
    ]
    assert ".lvl = 49" in gillian_party

    battle_main = read("src/battle_main.c")
    assert "{TRAINER_CLASS_LADY, 50}" in battle_main
    battle_commands = read("src/battle_script_commands.c")
    assert "moneyReward = 4 * lastMonLevel" in battle_commands

    resort_map = json.loads(read("data/maps/FiveIsland_ResortGorgeous/map.json"))
    wanted_scripts = {
        "FiveIsland_ResortGorgeous_EventScript_Jacki",
        "FiveIsland_ResortGorgeous_EventScript_Gillian",
        "FiveIsland_ResortGorgeous_EventScript_Celina",
    }
    coords = [
        (obj["x"], obj["y"])
        for obj in resort_map["object_events"]
        if obj.get("script") in wanted_scripts
    ]
    assert len(coords) == 3, coords
    x_lo = max(x - 7 for x, _ in coords)
    x_hi = min(x + 7 for x, _ in coords)
    y_lo = max(y - 5 for _, y in coords)
    y_hi = min(y + 5 for _, y in coords)
    assert x_lo <= x_hi and y_lo <= y_hi, (coords, (x_lo, x_hi, y_lo, y_hi))

    vs_seeker = read("src/vs_seeker.c")
    assert "vsSeekerChargeSteps == 100" in vs_seeker

    print(
        "RC freeze validator passed: Gen III ID/save compatibility, frozen economy, "
        "berry effects, fossils, Dojo, Altering Cave, evolutions and Porygon."
    )


if __name__ == "__main__":
    main()
