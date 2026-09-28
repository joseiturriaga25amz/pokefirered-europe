#!/usr/bin/env python3
"""Validate B4 specialty Ball availability, prices, and vanilla capture semantics."""

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]

SPECIALTY = (
    "ITEM_NET_BALL",
    "ITEM_NEST_BALL",
    "ITEM_REPEAT_BALL",
    "ITEM_TIMER_BALL",
    "ITEM_LUXURY_BALL",
    "ITEM_DIVE_BALL",
    "ITEM_PREMIER_BALL",
)

STAGED = {
    "data/maps/VermilionCity_Mart/scripts.inc": ("ITEM_NET_BALL",),
    "data/maps/FuchsiaCity_Mart/scripts.inc": ("ITEM_NEST_BALL",),
    "data/maps/SaffronCity_Mart/scripts.inc": ("ITEM_TIMER_BALL",),
    "data/maps/CinnabarIsland_Mart/scripts.inc": ("ITEM_REPEAT_BALL",),
    "data/maps/CeladonCity_DepartmentStore_2F/scripts.inc": (
        "ITEM_LUXURY_BALL",
        "ITEM_PREMIER_BALL",
    ),
    "data/maps/FourIsland_Mart/scripts.inc": ("ITEM_DIVE_BALL",),
}

LATE_SHOP = "data/maps/SevenIsland_Mart/scripts.inc"


def inventory(path: str) -> tuple[str, ...]:
    text = (ROOT / path).read_text(encoding="utf-8")
    return tuple(re.findall(r"\.2byte\s+(ITEM_[A-Z0-9_]+)", text))


def main() -> None:
    # Staged Kanto / Sevii availability.
    for path, required in STAGED.items():
        items = inventory(path)
        for item in required:
            assert item in items, (path, item, items)
        assert "ITEM_MASTER_BALL" not in items, path
        assert "ITEM_SAFARI_BALL" not in items, path

    # Seven Island is the legitimate late/postgame consolidated stock.
    seven = inventory(LATE_SHOP)
    for item in SPECIALTY:
        assert item in seven, (LATE_SHOP, item, seven)
    assert "ITEM_MASTER_BALL" not in seven
    assert "ITEM_SAFARI_BALL" not in seven

    # Existing item metadata/prices remain the authoritative Gen III data.
    data = json.loads((ROOT / "src/data/items.json").read_text(encoding="utf-8"))["items"]
    by_id = {x["itemId"]: x for x in data}
    expected_prices = {
        "ITEM_NET_BALL": 1000,
        "ITEM_NEST_BALL": 1000,
        "ITEM_REPEAT_BALL": 1000,
        "ITEM_TIMER_BALL": 1000,
        "ITEM_LUXURY_BALL": 1000,
        "ITEM_DIVE_BALL": 1000,
        "ITEM_PREMIER_BALL": 200,
    }
    expected_secondary = {
        "ITEM_NET_BALL": 5,
        "ITEM_DIVE_BALL": 6,
        "ITEM_NEST_BALL": 7,
        "ITEM_REPEAT_BALL": 8,
        "ITEM_TIMER_BALL": 9,
        "ITEM_LUXURY_BALL": 10,
        "ITEM_PREMIER_BALL": 11,
    }
    for item in SPECIALTY:
        row = by_id[item]
        assert row["price"] == expected_prices[item], (item, row["price"])
        assert row["pocket"] == "POCKET_POKE_BALLS", item
        assert row["battleUseFunc"] == "BattleUseFunc_PokeBallEtc", item
        assert row["secondaryId"] == expected_secondary[item], (item, row["secondaryId"])

    # Preserve original Gen III Dive Ball behavior: 3.5x only underwater, 1x elsewhere.
    battle = (ROOT / "src/battle_script_commands.c").read_text(encoding="utf-8")
    m = re.search(
        r"case ITEM_DIVE_BALL:(.*?)break;",
        battle,
        re.S,
    )
    assert m, "Dive Ball capture branch missing"
    dive = m.group(1)
    assert "GetCurrentMapType() == MAP_TYPE_UNDERWATER" in dive
    assert "ballMultiplier = 35;" in dive
    assert "ballMultiplier = 10;" in dive

    print(
        "B4 specialty Ball PASS: seven Balls are staged, Seven Island consolidates "
        "late stock, prices/metadata remain canonical, and Dive Ball mechanics are unchanged."
    )


if __name__ == "__main__":
    main()
