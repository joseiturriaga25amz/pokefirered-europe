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
