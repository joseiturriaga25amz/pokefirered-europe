#!/usr/bin/env python3
"""Lock exact blobs for high-risk gameplay data after semantic RC audit.

These hashes are not substitutes for semantic checks. They prevent collateral
drift after the baseline-vs-Full diff for each file has been reviewed.
"""

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "src/data/wild_encounters.json": "af87662ffce34ba48bc3d84e585a1f645bb1846f",
    "src/data/items.json": "0da4e1b54b0e33e439215635621ccef3dd9a5c5a",
    "src/data/pokemon/level_up_learnsets.h": "111723e9856d26f2a8ce96d901bec89ccdb39e51",
    "src/data/pokemon/evolution.h": "503be88f5381f51718a9f269aa2ed854ca67fbb4",
    "src/data/battle_moves.h": "5dac9c551a0a555b04ee885105b9a9d1b6071157",
    "src/trade.c": "50c4b149ea999c8282af1a670c7238e8d3afe0d7",
    "src/data/trainers.json": "a8dc3198085098e94cc685bc8c2b3276f735403e",
    "src/data/trainer_parties.h": "7f83fac9b672d9dc9c84ca24153b578cf5823f93",
    "data/scripts/spanish/hall_of_fame.inc": "9e2c9bb7e8b0bb3537aa313bae9ffcf405f1630c",
    "data/scripts/spanish/repel.inc": "d0255413c6a5453d5e1af15201b41d8b4663f22b",
    "data/scripts/spanish/move_tutors.inc": "f6fc0e15f3c7225bef69ae4d6362fced3c0e60f1",
    "src/script_menu.c": "d0939bf7f3c0c8b6409bad5f6b1508cdb3814836",
    "data/maps/SixIsland_AlteringCave/scripts.inc": "da91f6e0f72a0a360b53abdc839dc6f11a0b903a",
    "data/maps/SixIsland_AlteringCave/map.json": "0e2358007cc22f8d31bc93226e2801b9a8f06d81",
    "src/wild_encounter.c": "293caa0f44694ce9aefc734cde02256467e2fa9f",
    "include/constants/menu.h": "d289c2c922a25a8195dc3c6df5a80aa9ecd147ee",
    "include/wild_encounter.h": "b730103069f14a7d7147547d5bfad82bf082a6de",
    "src/battle_message.c": "0dfa1ca983f767357c78520d848febac39c5d8c8",
    "src/text.c": "d6c29153581a3421e84222eab47d513e1bc8545c",
    "graphics_file_rules.mk": "64f20a72bc51d80ef5f44606c3126918c4144980",
    "tools/gbagfx/font.c": "ac4a0dd97ccb4e6a98efd80667a3e694b2d33379",
    "tools/gbagfx/font.h": "9a3ba2c7f48ac440bcd0b05f7acb33b03afb0687",
    "tools/gbagfx/main.c": "bfd0d043540b0b603f34b5ff671d29c37e6e6ed1",
}


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main():
    for path, expected in EXPECTED.items():
        data = (ROOT / path).read_bytes()
        actual = git_blob_sha(data)
        assert actual == expected, f"{path}: audited blob drifted: {actual} != {expected}"
    print(f"Audited data blob PASS: {len(EXPECTED)} high-risk data files remain exact.")


if __name__ == "__main__":
    main()
