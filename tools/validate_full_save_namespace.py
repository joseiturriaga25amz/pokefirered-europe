#!/usr/bin/env python3
"""Static ownership checks for Pokémon Rojo Fuego Full persistent save namespaces."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def source_files():
    roots = ["src", "data", "include"]
    for root in roots:
        for path in (ROOT / root).rglob("*"):
            if path.is_file() and path.suffix in {".c", ".h", ".s", ".inc", ".json"}:
                yield path


def main():
    flags_h = read("include/constants/flags.h")
    vars_h = read("include/constants/vars.h")

    expected_flags = {
        "FLAG_FULL_DOJO_CHOSE_HITMONLEE": 0x8C3,
        "FLAG_FULL_DOJO_SECOND_REWARD": 0x8C4,
        "FLAG_FULL_ZAPDOS_KO_PENDING": 0x8C5,
        "FLAG_FULL_ARTICUNO_KO_PENDING": 0x8C6,
        "FLAG_FULL_MOLTRES_KO_PENDING": 0x8C7,
        "FLAG_FULL_MEWTWO_KO_PENDING": 0x8C8,
        "FLAG_FULL_MEW_CAUGHT": 0x8C9,
        "FLAG_FULL_MEW_KO_PENDING": 0x8CA,
        "FLAG_FULL_CELEBI_CAUGHT": 0x8CB,
        "FLAG_FULL_CELEBI_KO_PENDING": 0x8CC,
    }
    for name, value in expected_flags.items():
        pattern = rf"^#define\s+{name}\s+0x{value:X}\s*$"
        assert re.search(pattern, flags_h, re.MULTILINE), f"{name} != 0x{value:X}"
    assert len(set(expected_flags.values())) == len(expected_flags)
    assert "#define FLAG_FULL_START" in flags_h and "FLAG_0x8C3" in flags_h
    assert re.search(r"^#define\s+FLAG_FULL_END\s+0x8E2\s*$", flags_h, re.MULTILINE)

    expected_vars = {
        "VAR_FULL_MYSTIC_QUEST": 0x408C,
        "VAR_FULL_AURORA_QUEST": 0x408D,
        "VAR_FULL_MEW_QUEST": 0x408E,
        "VAR_FULL_CELEBI_QUEST": 0x408F,
        "VAR_FULL_ROAMER_SEQUENCE": 0x4090,
        "VAR_FULL_LAST_REPEL": 0x4091,
    }
    for name, value in expected_vars.items():
        pattern = rf"^#define\s+{name}\s+0x{value:X}\s*$"
        assert re.search(pattern, vars_h, re.MULTILINE), f"{name} != 0x{value:X}"
    assert len(set(expected_vars.values())) == len(expected_vars)
    assert re.search(r"^#define\s+VAR_FULL_START\s+0x408C\s*$", vars_h, re.MULTILINE)
    assert re.search(r"^#define\s+VAR_FULL_END\s+0x409B\s*$", vars_h, re.MULTILINE)

    # The numeric FLAG_0x*/VAR_0x* aliases are vanilla names for unused reserved
    # slots. They may remain declared, but no live source/data path may still use
    # one inside a Full-owned range or it would alias Full persistent state.
    forbidden = [
        *(f"FLAG_0x{x:X}" for x in range(0x8C3, 0x8E3)),
        *(f"VAR_0x{x:X}" for x in range(0x408C, 0x409C)),
    ]
    declarations = {
        ROOT / "include/constants/flags.h",
        ROOT / "include/constants/vars.h",
    }
    collisions = []
    for path in source_files():
        if path in declarations:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for token in forbidden:
            if re.search(rf"\b{re.escape(token)}\b", text):
                collisions.append(f"{path.relative_to(ROOT)}:{token}")
    assert not collisions, "Full namespace aliases are live elsewhere: " + ", ".join(collisions)

    load_save = read("src/load_save.c")
    start = load_save.index("void InitFullSaveData(void)")
    end = load_save.index("\n}", start) + 2
    init_full = load_save[start:end]
    assert "memset(&gSaveBlock1Ptr->fullHeader, 0, sizeof(gSaveBlock1Ptr->fullHeader));" in init_full
    assert "gSaveBlock1Ptr->bagPocket_Items" not in init_full
    assert "unused_348C" not in init_full

    print(
        "Full save namespace PASS: flags 0x8C3-0x8E2 and vars 0x408C-0x409B "
        "have no live vanilla-alias consumers; migration writes only the Full header."
    )


if __name__ == "__main__":
    main()
