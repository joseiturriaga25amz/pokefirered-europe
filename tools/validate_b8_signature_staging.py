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
    onix = [o for o in brock_objs if o.get("local_id") == "LOCALID_FULL_BROCK_ONIX"]
    assert len(onix) == 1
    onix = onix[0]
    assert onix["graphics_id"] == "OBJ_EVENT_GFX_ONIX"
    assert (onix["x"], onix["y"]) == (4, 5)
    assert onix["script"] == "0x0"
    assert onix["trainer_type"] == "TRAINER_TYPE_NONE"
    assert onix["x"] != 6
    assert not any((w["x"], w["y"]) == (onix["x"], onix["y"]) for w in brock["warp_events"])

    event_objects = (ROOT / "include/constants/event_objects.h").read_text(encoding="utf-8")
    movement = (ROOT / "src/event_object_movement.c").read_text(encoding="utf-8")
    graphics = (ROOT / "src/data/object_events/object_event_graphics.h").read_text(encoding="utf-8")
    info = (ROOT / "src/data/object_events/object_event_graphics_info.h").read_text(encoding="utf-8")
    pointers = (ROOT / "src/data/object_events/object_event_graphics_info_pointers.h").read_text(encoding="utf-8")
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "OBJ_EVENT_PAL_TAG_MON_ICON_2" in movement
    assert "gMonIconPalettes[2]" in movement
    assert 'graphics/pokemon/onix/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Onix" in info
    assert ".paletteSlot = PALSLOT_NPC_SPECIAL" in info
    assert "[OBJ_EVENT_GFX_ONIX]" in pointers

    print("B8 signature staging PASS: Lorelei/Lapras and Brock/Onix pilots are static, nonblocking and palette-safe.")


if __name__ == "__main__":
    main()
