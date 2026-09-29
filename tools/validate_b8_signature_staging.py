#!/usr/bin/env python3
"""B8 signature Pokémon staging checks."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main():
    lorelei = read_json("data/maps/PokemonLeague_LoreleisRoom/map.json")
    objects = lorelei["object_events"]

    trainer = [o for o in objects if o.get("graphics_id") == "OBJ_EVENT_GFX_LORELEI"]
    assert len(trainer) == 1
    assert (trainer[0]["x"], trainer[0]["y"]) == (6, 5)

    companions = [o for o in objects if o.get("local_id") == "LOCALID_FULL_LORELEI_LAPRAS"]
    assert len(companions) == 1
    lapras = companions[0]
    assert lapras["graphics_id"] == "OBJ_EVENT_GFX_LAPRAS"
    assert (lapras["x"], lapras["y"]) == (4, 5)
    assert lapras["script"] == "0x0"
    assert lapras["flag"] == "0"
    assert lapras["trainer_type"] == "TRAINER_TYPE_NONE"

    # Keep the central League approach/exit lane unobstructed.
    assert lapras["x"] != 6
    assert not any(
        (warp["x"], warp["y"]) == (lapras["x"], lapras["y"])
        for warp in lorelei["warp_events"]
    )

    brock = read_json("data/maps/PewterCity_Gym/map.json")
    brock_objs = brock["object_events"]
    signature = [o for o in brock_objs if o.get("local_id") == "LOCALID_FULL_BROCK_SIGNATURE"]
    assert len(signature) == 1
    signature = signature[0]
    assert signature["graphics_id"] == "OBJ_EVENT_GFX_VAR_0"
    assert (signature["x"], signature["y"]) == (4, 5)
    assert signature["script"] == "0x0"
    assert signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert signature["x"] != 6
    assert not any((w["x"], w["y"]) == (signature["x"], signature["y"]) for w in brock["warp_events"])

    event_objects = (ROOT / "include/constants/event_objects.h").read_text(encoding="utf-8")
    movement = (ROOT / "src/event_object_movement.c").read_text(encoding="utf-8")
    graphics = (ROOT / "src/data/object_events/object_event_graphics.h").read_text(encoding="utf-8")
    info = (ROOT / "src/data/object_events/object_event_graphics_info.h").read_text(encoding="utf-8")
    pointers = (ROOT / "src/data/object_events/object_event_graphics_info_pointers.h").read_text(encoding="utf-8")
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "#define OBJ_EVENT_GFX_STEELIX 153" in event_objects
    assert "#define NUM_OBJ_EVENT_GFX     156" in event_objects
    assert "OBJ_EVENT_PAL_TAG_MON_ICON_2" in movement
    assert "gMonIconPalettes[2]" in movement
    assert 'graphics/pokemon/onix/icon.4bpp' in graphics
    assert 'graphics/pokemon/steelix/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Onix" in info
    assert "gObjectEventGraphicsInfo_Steelix" in info
    assert ".paletteSlot = PALSLOT_NPC_SPECIAL" in info
    assert "[OBJ_EVENT_GFX_ONIX]" in pointers
    assert "[OBJ_EVENT_GFX_STEELIX]" in pointers

    brock_scripts = (ROOT / "data/maps/PewterCity_Gym/scripts.inc").read_text(encoding="utf-8")
    assert "setvar VAR_OBJ_GFX_ID_0, OBJ_EVENT_GFX_ONIX" in brock_scripts
    assert "goto_if_unset FLAG_SYS_GAME_CLEAR" in brock_scripts
    assert "goto_if_unset FLAG_GOT_TM39_FROM_BROCK" in brock_scripts
    assert "setvar VAR_OBJ_GFX_ID_0, OBJ_EVENT_GFX_STEELIX" in brock_scripts

    koga = read_json("data/maps/FuchsiaCity_Gym/map.json")
    koga_objs = koga["object_events"]
    koga_signature = [o for o in koga_objs if o.get("local_id") == "LOCALID_FULL_KOGA_SIGNATURE"]
    assert len(koga_signature) == 1
    koga_signature = koga_signature[0]
    assert koga_signature["graphics_id"] == "OBJ_EVENT_GFX_VAR_1"
    assert (koga_signature["x"], koga_signature["y"]) == (5, 13)
    assert koga_signature["script"] == "0x0"
    assert koga_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert not any((w["x"], w["y"]) == (koga_signature["x"], koga_signature["y"]) for w in koga["warp_events"])

    assert "#define OBJ_EVENT_GFX_GOLBAT 154" in event_objects
    assert "#define OBJ_EVENT_GFX_CROBAT 155" in event_objects
    assert "#define NUM_OBJ_EVENT_GFX     156" in event_objects
    assert 'graphics/pokemon/golbat/icon.4bpp' in graphics
    assert 'graphics/pokemon/crobat/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Golbat" in info
    assert "gObjectEventGraphicsInfo_Crobat" in info
    assert "[OBJ_EVENT_GFX_GOLBAT]" in pointers
    assert "[OBJ_EVENT_GFX_CROBAT]" in pointers

    koga_scripts = (ROOT / "data/maps/FuchsiaCity_Gym/scripts.inc").read_text(encoding="utf-8")
    assert "setvar VAR_OBJ_GFX_ID_1, OBJ_EVENT_GFX_GOLBAT" in koga_scripts
    assert "goto_if_unset FLAG_SYS_GAME_CLEAR" in koga_scripts
    assert "goto_if_unset FLAG_GOT_TM06_FROM_KOGA" in koga_scripts
    assert "setvar VAR_OBJ_GFX_ID_1, OBJ_EVENT_GFX_CROBAT" in koga_scripts

    print("B8 signature staging PASS: Lorelei/Lapras stable; Brock Onix->Steelix and Koga Golbat->Crobat are stage-aware and nonblocking.")


if __name__ == "__main__":
    main()
