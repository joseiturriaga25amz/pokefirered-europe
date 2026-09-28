#!/usr/bin/env python3
"""B7 presentation gates: visible/interactable Mew without changing battle/save identity."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def block(text, label):
    marker = label + "::"
    start = text.index(marker)
    end = text.find("\n\n", start)
    return text[start:] if end == -1 else text[start:end]


def main():
    map_data = json.loads(read("data/maps/PokemonMansion_B1F/map.json"))
    scripts = read("data/maps/PokemonMansion_B1F/scripts.inc")
    text_es = read("data/maps/PokemonMansion_B1F/text_es.inc")

    # Three non-interactive overworld sightings lead the player deeper through
    # the mansion before the final B1F interaction.
    sighting_specs = (
        ("PokemonMansion_1F", "LOCALID_FULL_MEW_SIGHTING_1F", 1, (7, 6)),
        ("PokemonMansion_2F", "LOCALID_FULL_MEW_SIGHTING_2F", 2, (8, 30)),
        ("PokemonMansion_3F", "LOCALID_FULL_MEW_SIGHTING_3F", 3, (10, 16)),
    )
    for map_name, local_id, quest_state, coords in sighting_specs:
        data = json.loads(read(f"data/maps/{map_name}/map.json"))
        map_scripts = read(f"data/maps/{map_name}/scripts.inc")
        objects = [obj for obj in data["object_events"] if obj.get("local_id") == local_id]
        assert len(objects) == 1, (map_name, local_id)
        obj = objects[0]
        assert obj["graphics_id"] == "OBJ_EVENT_GFX_MEW"
        assert obj["script"] == "0x0"
        assert (obj["x"], obj["y"]) == coords
        assert not any((w["x"], w["y"]) == coords for w in data["warp_events"])
        updater = block(map_scripts, f"{map_name}_EventScript_UpdateFullMewSighting")
        assert f"goto_if_ne VAR_FULL_MEW_QUEST, {quest_state}" in updater
        assert f"showobjectat {local_id}" in updater
        assert "StartLegendaryBattle" not in updater

    mew_objects = [
        obj for obj in map_data["object_events"]
        if obj.get("local_id") == "LOCALID_FULL_MEW_FINAL"
    ]
    assert len(mew_objects) == 1
    mew = mew_objects[0]
    assert mew["graphics_id"] == "OBJ_EVENT_GFX_MEW"
    assert mew["script"] == "PokemonMansion_B1F_EventScript_FullMewObject"
    assert mew["flag"] == "0"

    on_load = block(scripts, "PokemonMansion_B1F_OnLoad")
    assert "PokemonMansion_B1F_EventScript_UpdateFullMewVisibility" in on_load

    update = block(scripts, "PokemonMansion_B1F_EventScript_UpdateFullMewVisibility")
    assert "goto_if_ne VAR_FULL_MEW_QUEST, 4" in update
    assert "FLAG_FULL_MEW_CAUGHT" in update
    assert "FLAG_FULL_MEW_KO_PENDING" in update
    assert "showobjectat LOCALID_FULL_MEW_FINAL" in update

    diary = block(scripts, "PokemonMansion_B1F_EventScript_DiarySep1st")
    assert "PokemonMansion_B1F_EventScript_FullMewBattle" not in diary
    assert "PokemonMansion_B1F_EventScript_FullMewFinalAppearance" in diary

    appearance = block(scripts, "PokemonMansion_B1F_EventScript_FullMewFinalAppearance")
    assert "setvar VAR_FULL_MEW_QUEST, 4" in appearance
    assert "showobjectat LOCALID_FULL_MEW_FINAL" in appearance
    assert "playmoncry SPECIES_MEW" in appearance
    assert "StartLegendaryBattle" not in appearance

    interaction = block(scripts, "PokemonMansion_B1F_EventScript_FullMewObject")
    assert "goto_if_ne VAR_FULL_MEW_QUEST, 4" in interaction
    assert "faceplayer" in interaction
    assert "PokemonMansion_B1F_EventScript_FullMewBattle" in interaction

    battle = block(scripts, "PokemonMansion_B1F_EventScript_FullMewBattle")
    assert "special Full_CreateMewEventMon" in battle
    assert "special StartLegendaryBattle" in battle

    caught = block(scripts, "PokemonMansion_B1F_EventScript_FullMewCaught")
    defeated = block(scripts, "PokemonMansion_B1F_EventScript_FullMewDefeated")
    assert "hideobjectat LOCALID_FULL_MEW_FINAL" in caught
    assert "hideobjectat LOCALID_FULL_MEW_FINAL" in defeated

    # Preserve the canonical final diary content as the historical anchor.
    assert "Diario: 1 de septiembre." in text_es
    assert "MEWTWO es demasiado poderoso." in text_es

    # Quest NPCs retain contextual identity after the first clue/handoff instead
    # of immediately falling back to unrelated vanilla dialogue.
    vermilion = read("data/maps/VermilionCity/scripts.inc")
    ferry = block(vermilion, "VermilionCity_EventScript_FerrySailor")
    assert "goto_if_eq VAR_FULL_MYSTIC_QUEST, 1, VermilionCity_EventScript_FerrySailorMysticReminder" in ferry
    mystic_reminder = block(vermilion, "VermilionCity_EventScript_FerrySailorMysticReminder")
    assert "VermilionCity_Text_FullMaritimeBirdClue" in mystic_reminder

    pewter = read("data/maps/PewterCity_Museum_1F/scripts.inc")
    scientist = block(pewter, "PewterCity_Museum_1F_EventScript_Scientist2")
    assert "goto_if_eq VAR_FULL_AURORA_QUEST, 2, PewterCity_Museum_1F_EventScript_FullAuroraFollowup" in scientist
    aurora_followup = block(pewter, "PewterCity_Museum_1F_EventScript_FullAuroraFollowup")
    assert "PewterCity_Museum_1F_Text_FullAuroraSignal" in aurora_followup

    print("B7 Mew presentation PASS: three overworld sightings lead to a final interactable Mew; battle starts only by interaction.")


if __name__ == "__main__":
    main()
