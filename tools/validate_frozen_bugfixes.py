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

    # BUG-012: the Ruby object belongs to B5F. The script may remain physically
    # declared in the B3F script include, but B3F must not own the object.
    b3 = json.loads(read("data/maps/MtEmber_RubyPath_B3F/map.json"))
    b5 = json.loads(read("data/maps/MtEmber_RubyPath_B5F/map.json"))
    b3_ids = {obj["local_id"] for obj in b3.get("object_events", [])}
    b5_ids = {obj["local_id"] for obj in b5.get("object_events", [])}
    assert "LOCALID_RUBY" not in b3_ids, "BUG-012: Ruby object still lives on B3F"
    assert "LOCALID_RUBY" in b5_ids, "BUG-012: Ruby object missing from B5F"

    print("BUG-001..BUG-012 static audit PASS: all frozen technical repairs remain present.")


if __name__ == "__main__":
    main()
