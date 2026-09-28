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

    print("B8 signature staging PASS: Lorelei has a static, nonblocking Lapras companion.")


if __name__ == "__main__":
    main()
