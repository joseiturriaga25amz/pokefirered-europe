#!/usr/bin/env python3
"""Lock the 12 frozen technical bugfixes required by BUG-001..BUG-012."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def req(text, token, label):
    assert token in text, f"{label}: missing {token}"


def main():
    config = read("include/config.h")
    req(config, "#if MODERN", "BUG-011")
    req(config, "#define BUGFIX", "BUG-011")
    req(config, "#define UBFIX", "BUG-011")

    pokemon = read("src/pokemon.c")
    for token in (
        "u32 ivs = data[0] | (data[1] << 8) | (data[2] << 16) | (data[3] << 24);",
        "if (currentHP <= 0)",
        "currentHP = 1;",
    ):
        req(pokemon, token, "BUG-001/006")

    roamer = read("src/roamer.c")
    for token in (
        "u32 status;",
        "status = ROAMER->status;",
        "SetMonData(mon, MON_DATA_STATUS, &status);",
        "ROAMER->ivs = GetMonData(mon, MON_DATA_IVS);",
    ):
        req(roamer, token, "BUG-001/003")
    battle = read("src/battle_main.c")
    req(battle, "UpdateRoamerHPStatus(&gEnemyParty[0]);", "BUG-002")
    # Roar/ordinary escape must not permanently deactivate the roamer.
    capture_guard = """#if defined(BUGFIX) || REVISION >= 0xA
            if (gBattleOutcome == B_OUTCOME_CAUGHT)"""
    req(battle, capture_guard, "BUG-002")
    req(battle, "SetRoamerInactive();", "BUG-002")

    area = read("src/wild_pokemon_area.c")
    req(
        area,
        "IsSpeciesInEncounterTable(data->fishingMonsInfo, species, FISH_WILD_COUNT)",
        "BUG-004",
    )

    trade = read("src/trade.c")
    req(trade, "if (species2[monIdx] == SPECIES_EGG)", "BUG-005")
    req(trade, "return CANT_TRADE_EGG_YET;", "BUG-005")

    reminder = read("src/learn_move.c")
    req(reminder, "sMoveRelearner->spriteIds[0] = CreateSprite", "BUG-007")
    req(reminder, "sMoveRelearner->spriteIds[1] = CreateSprite", "BUG-007")
    req(reminder, "gSprites[sMoveRelearner->spriteIds[1]].data[2] = 1;", "BUG-007")

    main_c = read("src/main.c")
    req(main_c, "gMain.heldKeysRaw == keyInput", "BUG-008")
    req(main_c, "gMain.newAndRepeatedKeys |= A_BUTTON;", "BUG-008")

    party = read("src/party_menu.c")
    req(party, "Free(sSlot1TilemapBuffer);", "BUG-009")
    req(party, "Free(sSlot2TilemapBuffer);", "BUG-009")

    berry = read("src/berry_crush.c")
    req(berry, "#define field sparkleAmount", "BUG-010")
    req(berry, "game->field = 2;", "BUG-010")
    req(berry, "game->field = 3;", "BUG-010")

    # Gate 2A / RC-F028: current pret/pokefirered upstream analysis identified
    # doubles-AI history aliasing and out-of-bounds move-history reads. Full forces
    # BUGFIX, so the safe per-battler path must remain compiled.
    battle_h = read("include/battle.h")
    req(battle_h, "struct UsedMoves usedMoves[MAX_BATTLERS_COUNT];", "RC-F028")
    req(battle_h, "u8 abilities[MAX_BATTLERS_COUNT];", "RC-F028")
    req(battle_h, "u8 itemEffects[MAX_BATTLERS_COUNT];", "RC-F028")

    ai = read("src/battle_ai_script_commands.c")
    for token in (
        "BATTLE_HISTORY->usedMoves[gBattlerTarget].moves[i]",
        "for (i = 0; i < MAX_MON_MOVES; i++)",
        "BATTLE_HISTORY->abilities[battlerId] = abilityId;",
        "BATTLE_HISTORY->itemEffects[battlerId] = itemEffect;",
        "(GetBattlerSide(gActiveBattler) ^ BIT_SIDE)",
        "AI_THINKING_STRUCT->funcResult = BATTLE_HISTORY->itemEffects[battlerId];",
    ):
        req(ai, token, "RC-F028/RC-F030")
    # The BUGFIX branches may preserve vanilla code under #ifndef BUGFIX, but the
    # active path must never index an actual four-move array with the old 0..7 loop.
    assert "gBattleMons[gBattlerAttacker].moves[i] != 0 && gBattleMoves[BATTLE_HISTORY->usedMoves[gBattlerTarget].moves[i]]" not in ai

    # Gate 12 pre-runtime hardening / RC-F032: Full builds MODERN with REVISION=0,
    # so tested revision-0xA link fixes must also be enabled by BUGFIX.
    overworld_h = read("include/overworld.h")
    req(overworld_h, "#if defined(BUGFIX) || REVISION >= 0xA", "RC-F032")
    req(overworld_h, "void ClearFieldCallback(void);", "RC-F032")

    overworld_c = read("src/overworld.c")
    req(overworld_c, "#if defined(BUGFIX) || REVISION >= 0xA\nvoid ClearFieldCallback(void)", "RC-F032")

    link_c = read("src/link.c")
    req(link_c, "#if defined(BUGFIX) || REVISION >= 0xA\n    ClearFieldCallback();", "RC-F032")

    battle_player = read("src/battle_controller_player.c")
    req(battle_player, "#if !(defined(BUGFIX) || REVISION >= 0xA)", "RC-F032")
    req(battle_player, "#if defined(BUGFIX) || REVISION >= 0xA\n            if (!IsLinkTaskFinished() || gPaletteFade.active) return;", "RC-F032")

    battle_main = read("src/battle_main.c")
    req(battle_main, "#if defined(BUGFIX) || REVISION >= 0xA\n        if (IsLinkTaskFinished() && !gPaletteFade.active)", "RC-F032")

    cable = read("src/cable_club.c")
    assert cable.count("#if defined(BUGFIX) || REVISION >= 0xA\n        if (!IsLinkTaskFinished()) break;") >= 2

    save_c = read("src/save.c")
    assert save_c.count("#if defined(BUGFIX) || REVISION >= 0xA\n        if (!IsLinkTaskFinished()) break;") >= 3

    trade_c = read("src/trade.c")
    req(trade_c, "#if defined(BUGFIX) || REVISION >= 0xA\n    if (IsLinkTaskFinished() && !gPaletteFade.active)", "RC-F032")

    union_battle = read("src/union_room_battle.c")
    assert union_battle.count("#if defined(BUGFIX) || REVISION >= 0xA") >= 3

    # Gate 2A / RC-F033: UBFIX must not rely on two-argument functions being
    # aliases of three-argument functions with incompatible signatures.
    pokemon_h = read("include/pokemon.h")
    for token in (
        "static inline u32 GetMonData2(struct Pokemon *mon, s32 field)",
        "return GetMonData3(mon, field, NULL);",
        "static inline u32 GetBoxMonData2(struct BoxPokemon *boxMon, s32 field)",
        "return GetBoxMonData3(boxMon, field, NULL);",
    ):
        req(pokemon_h, token, "RC-F033")

    pokemon_c = read("src/pokemon.c")
    req(
        pokemon_c,
        '#ifndef UBFIX\nu32 GetMonData2(struct Pokemon *mon, s32 field) __attribute__((alias("GetMonData3")));',
        "RC-F033",
    )
    req(
        pokemon_c,
        '#ifndef UBFIX\nu32 GetBoxMonData2(struct BoxPokemon *boxMon, s32 field) __attribute__((alias("GetBoxMonData3")));',
        "RC-F033",
    )

    # Gate 12 pre-runtime hardening / RC-F034: wireless status accounting must
    # not index group-count arrays with NUM_GROUPTYPES or GROUPTYPE_NONE under UBFIX.
    wireless_status = read("src/wireless_communication_status_screen.c")
    for token in (
        "#if defined(UBFIX) || REVISION >= 0xA\n    {ACTIVITY_POKEMON_JUMP",
        "#if defined(UBFIX) || REVISION >= 0xA\n    {ACTIVITY_RECORD_CORNER",
        "if (type < NUM_GROUPTYPES && activity == group_activity(i))",
        "groupCounts[type] += k;",
        "#if defined(UBFIX) || REVISION >= 0xA\n    if (HaveCountsChanged(groupCountBuffer, prevGroupCounts))",
        "+ groupCounts[GROUPTYPE_TOTAL];",
    ):
        req(wireless_status, token, "RC-F034")

    # Gate 2A / RC-F037: localized Spanish strings must use color changes
    # rather than JP-font control codes when BUGFIX is enabled.
    roof_text = read("data/maps/CeladonCity_DepartmentStore_Roof/text_es.inc")
    req(roof_text, '#ifdef BUGFIX\n    .string "{COLOR DARK_GRAY}¿Le das algo de beber?$"', "RC-F037")

    fossil_text = read("data/maps/CinnabarIsland_PokemonLab_ExperimentRoom/text_es.inc")
    req(
        fossil_text,
        '#ifdef BUGFIX\n    .string "{COLOR DARK_GRAY}¡{PLAYER} le dio {STR_VAR_2}\\\\n"',
        "RC-F037",
    )

    vermilion_text = read("data/maps/VermilionCity/text_es.inc")
    for token in (
        '#ifdef BUGFIX\n    .string "{COLOR DARK_GRAY}¡{PLAYER} enseñó el TICKET\\\\n"',
        '#ifdef BUGFIX\n    .string "{COLOR BLUE}¡OK!\\\\n"',
        '#ifdef BUGFIX\n    .string "{COLOR DARK_GRAY}{PLAYER} no tiene el TICKET del\\\\n"',
        '#ifdef BUGFIX\n    .string "{COLOR BLUE}¡Lo siento!\\\\p"',
    ):
        req(vermilion_text, token, "RC-F037")

    # BUG-012: the Ruby object belongs to B5F. The script may remain physically
    # declared in the B3F script include, but B3F must not own the object.
    b3 = json.loads(read("data/maps/MtEmber_RubyPath_B3F/map.json"))
    b5 = json.loads(read("data/maps/MtEmber_RubyPath_B5F/map.json"))
    b3_ids = {
        obj["local_id"] for obj in b3.get("object_events", []) if "local_id" in obj
    }
    b5_ids = {
        obj["local_id"] for obj in b5.get("object_events", []) if "local_id" in obj
    }
    assert "LOCALID_RUBY" not in b3_ids, "BUG-012: Ruby object still lives on B3F"
    assert "LOCALID_RUBY" in b5_ids, "BUG-012: Ruby object missing from B5F"

    print("BUG-001..BUG-012 + RC-F028/030/032/033/034 static audit PASS: frozen, AI, link and UBFIX repairs remain present.")


if __name__ == "__main__":
    main()
