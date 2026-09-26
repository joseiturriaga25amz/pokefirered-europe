#!/usr/bin/env python3
"""Validate B3 Gym Leader rematch unlock and dialogue identity."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

GYMS = {
    "PewterCity_Gym": "TRAINER_RS_AROMA_LADY",
    "CeruleanCity_Gym": "TRAINER_RS_RUIN_MANIAC",
    "VermilionCity_Gym": "TRAINER_RS_TUBER_F",
    "CeladonCity_Gym": "TRAINER_RS_TUBER_M",
    "FuchsiaCity_Gym": "TRAINER_RS_COOLTRAINER_M",
    "SaffronCity_Gym": "TRAINER_RS_COOLTRAINER_F",
    "CinnabarIsland_Gym": "TRAINER_RS_LADY",
    "ViridianCity_Gym": "TRAINER_RS_BEAUTY",
}

LABEL_SUFFIXES = (
    "Text_FullRematchOffer",
    "Text_FullRematchIntro",
    "Text_FullRematchDefeat",
    "Text_FullRematchAfter",
)

def extract_string_block(text: str, label: str) -> str:
    m = re.search(
        rf"{re.escape(label)}::\n((?:\t\.string .*\n?)+)",
        text,
        re.S,
    )
    assert m, f"missing label {label}"
    values = re.findall(r'\.string "([^"]*)"', m.group(1))
    assert values, f"empty label {label}"
    return "\n".join(values)

def main() -> None:
    dialogue_sets = []

    for gym, trainer in GYMS.items():
        path = ROOT / f"data/maps/{gym}/scripts.inc"
        text = path.read_text(encoding="utf-8")

        assert "FLAG_SYS_GAME_CLEAR" in text, f"{gym}: missing game-clear gate"
        assert "FLAG_SYS_NATIONAL_DEX" not in text, f"{gym}: National Dex still gates rematch"
        assert f"cleartrainerflag {trainer}" in text, f"{gym}: rematch repeatability reset missing"
        assert trainer in text, f"{gym}: rematch trainer missing"

        values = tuple(
            extract_string_block(text, f"{gym}_{suffix}")
            for suffix in LABEL_SUFFIXES
        )
        dialogue_sets.append(values)

    assert len(set(dialogue_sets)) == len(GYMS), "leader rematch dialogue sets are not unique"

    print(
        "B3 Gym rematch identity PASS: first Hall-of-Fame unlock, "
        "repeatable trainer reset, and eight unique dialogue sets."
    )

if __name__ == "__main__":
    main()
