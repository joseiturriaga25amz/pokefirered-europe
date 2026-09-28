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


    # After the beast first-contact scene, One Island provides state-aware
    # environmental guidance for the currently active roamer and a non-spoiler
    # golden-light hint once the trio is complete.
    one_island = read("data/maps/OneIsland/scripts.inc")
    one_island_text = read("data/maps/OneIsland/text_es.inc")
    old_man = block(one_island, "OneIsland_EventScript_OldMan")
    assert "goto_if_eq VAR_FULL_BEAST_INTRO, 2, OneIsland_EventScript_OldManBeastArc" in old_man
    beast_arc = block(one_island, "OneIsland_EventScript_OldManBeastArc")
    assert "goto_if_eq VAR_FULL_ROAMER_SEQUENCE, 0, OneIsland_EventScript_OldManTrackSuicune" in beast_arc
    assert "goto_if_eq VAR_FULL_ROAMER_SEQUENCE, 1, OneIsland_EventScript_OldManTrackRaikou" in beast_arc
    assert "goto_if_eq VAR_FULL_ROAMER_SEQUENCE, 2, OneIsland_EventScript_OldManTrackEntei" in beast_arc
    for label in (
        "OneIsland_Text_FullBeastTrackSuicune::",
        "OneIsland_Text_FullBeastTrackRaikou::",
        "OneIsland_Text_FullBeastTrackEntei::",
        "OneIsland_Text_FullBeastArcComplete::",
    ):
        assert label in one_island_text
    assert "POKéDEX" in one_island_text
    assert "brillo" in one_island_text.lower()


    # Existing legendary presentation already satisfies B7 for the remaining
    # arcs; lock those cues instead of adding redundant presentation layers.
    celebi_scripts = read("data/maps/ThreeIsland_BerryForest/scripts.inc")
    celebi_text = read("data/maps/ThreeIsland_BerryForest/text_es.inc")
    celebi_event = block(celebi_scripts, "ThreeIsland_BerryForest_EventScript_FullCelebi")
    assert "playmoncry SPECIES_CELEBI, CRY_MODE_ENCOUNTER" in celebi_event
    assert "ThreeIsland_BerryForest_Text_FullCelebiAppears" in celebi_event
    assert "Las hojas comienzan a agitarse" in celebi_text
    assert "Una luz verde rodea el árbol." in celebi_text
    assert "VAR_FULL_CELEBI_QUEST" in celebi_scripts

    lugia = read("data/maps/NavelRock_Base/scripts.inc")
    lugia_event = block(lugia, "NavelRock_Base_EventScript_Lugia")
    assert lugia_event.count("special ShakeScreen") >= 2
    assert "playmoncry SPECIES_LUGIA, CRY_MODE_ENCOUNTER" in lugia_event
    assert "seteventmon SPECIES_LUGIA, 70" in lugia_event

    hooh = read("data/maps/NavelRock_Summit/scripts.inc")
    hooh_event = block(hooh, "NavelRock_Summit_EventScript_HoOh")
    assert "special SpawnCameraObject" in hooh_event
    assert "special LoopWingFlapSound" in hooh_event
    assert "Movement_CameraPanUp" in hooh_event
    assert "playmoncry SPECIES_HO_OH, CRY_MODE_ENCOUNTER" in hooh_event
    assert "seteventmon SPECIES_HO_OH, 70" in hooh_event

    deoxys = read("data/maps/BirthIsland_Exterior/scripts.inc")
    deoxys_event = block(deoxys, "BirthIsland_Exterior_EventScript_Deoxys")
    assert "FLDEFF_DESTROY_DEOXYS_ROCK" in deoxys_event
    assert "playbgm MUS_ENCOUNTER_DEOXYS" in deoxys_event
    assert "Movement_DeoxysApproach" in deoxys_event
    assert "playmoncry SPECIES_DEOXYS, CRY_MODE_ENCOUNTER" in deoxys_event
    assert "seteventmon SPECIES_DEOXYS, 50" in deoxys_event

    print("B7 legendary presentation PASS: Mew, Mystic/Aurora NPC context, beasts, Celebi, Lugia, Ho-Oh and Deoxys presentation gates are coherent.")


if __name__ == "__main__":
    main()
