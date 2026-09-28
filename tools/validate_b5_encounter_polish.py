#!/usr/bin/env python3
"""Validate B5 Altering Cave rotation and A-009 special encounter rarity."""

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]

ALTERING_SPECIES = (
    "SPECIES_ZUBAT",
    "SPECIES_MAREEP",
    "SPECIES_PINECO",
    "SPECIES_HOUNDOUR",
    "SPECIES_TEDDIURSA",
    "SPECIES_AIPOM",
    "SPECIES_SHUCKLE",
    "SPECIES_STANTLER",
    "SPECIES_SMEARGLE",
)

RATES = {
    "land_mons": (20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1),
    "water_mons": (60, 30, 5, 4, 1),
    "fishing_mons": (70, 30, 60, 20, 20, 40, 40, 15, 4, 1),
}


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def encounter_rate(encounters, label: str, kind: str, species: str) -> int:
    entry = encounters[label]
    mons = entry[kind]["mons"]
    return sum(
        weight
        for mon, weight in zip(mons, RATES[kind])
        if mon["species"] == species
    )


def main() -> None:
    # A-009: no manual selector; rotate the existing variable once per cave entry.
    script = read("data/maps/SixIsland_AlteringCave/scripts.inc")
    assert "multichoice" not in script, "manual Altering Cave species selector returned"
    assert "SixIsland_AlteringCave_EventScript_SelectPage" not in script
    assert "ResearcherChanged" not in script
    assert "switch VAR_ALTERING_CAVE_WILD_SET" in script

    expected_rotation = {
        0: 1, 1: 2, 2: 3, 3: 4, 4: 5,
        5: 6, 6: 7, 7: 8, 8: 0,
    }
    for current, nxt in expected_rotation.items():
        assert (
            f"case {current}, SixIsland_AlteringCave_EventScript_RotateTo{nxt}"
            in script
        ), (current, nxt)
        label = f"SixIsland_AlteringCave_EventScript_RotateTo{nxt}::"
        pos = script.index(label)
        body = script[pos: script.find("\n\n", pos)]
        assert f"setvar VAR_ALTERING_CAVE_WILD_SET, {nxt}" in body, (current, nxt)

    # Researcher is informational and reports every active table rather than mutating it.
    researcher_pos = script.index("SixIsland_AlteringCave_EventScript_Researcher::")
    report_pos = script.index("SixIsland_AlteringCave_EventScript_ReportZubat::")
    researcher = script[researcher_pos:report_pos]
    assert "setvar VAR_ALTERING_CAVE_WILD_SET" not in researcher
    for idx, name in enumerate(("Zubat","Mareep","Pineco","Houndour","Teddiursa","Aipom","Shuckle","Stantler","Smeargle")):
        assert f"case {idx}, SixIsland_AlteringCave_EventScript_Report{name}" in researcher

    # Existing encounter table IDs/order remain exactly nine per version.
    data = json.loads(read("src/data/wild_encounters.json"))
    group = next(g for g in data["wild_encounter_groups"] if g["label"] == "gWildMonHeaders")
    for version in ("FireRed", "LeafGreen"):
        tables = [
            e for e in group["encounters"]
            if e.get("map") == "MAP_SIX_ISLAND_ALTERING_CAVE"
            and e.get("base_label", "").endswith(f"_{version}")
        ]
        assert len(tables) == 9, (version, len(tables))
        for idx, (table, species) in enumerate(zip(tables, ALTERING_SPECIES), start=1):
            expected_label = (
                f"sSixIslandAlteringCave_{version}"
                if idx == 1
                else f"sSixIslandAlteringCave_{idx}_{version}"
            )
            assert table["base_label"] == expected_label, (
                version, idx, table["base_label"], expected_label
            )
            assert table["land_mons"]["encounter_rate"] == 7
            found = {m["species"] for m in table["land_mons"]["mons"]}
            assert found == {species}, (version, idx, found, species)

    # Engine still consumes the same 0..8 variable; no encounter ABI change.
    engine = read("src/wild_encounter.c")
    for token in (
        "VarGet(VAR_ALTERING_CAVE_WILD_SET)",
        "alteringCaveId >= NUM_ALTERING_CAVE_TABLES",
        "alteringCaveId = 0;",
        "i += alteringCaveId;",
    ):
        assert token in engine, token

    area = read("src/wild_pokemon_area.c")
    assert "VarGet(VAR_ALTERING_CAVE_WILD_SET)" in area
    assert "alteringCaveNum >= NUM_ALTERING_CAVE_TABLES" in area

    encounters = {e["base_label"]: e for e in group["encounters"]}

    expected = (
        ("sSafariZoneCenter_FireRed", "land_mons", "SPECIES_SCYTHER", 10),
        ("sSafariZoneCenter_FireRed", "land_mons", "SPECIES_PINSIR", 10),
        ("sSafariZoneEast_FireRed", "land_mons", "SPECIES_KANGASKHAN", 10),
        ("sSafariZoneNorth_FireRed", "land_mons", "SPECIES_CHANSEY", 10),
        ("sSafariZoneWest_FireRed", "land_mons", "SPECIES_TAUROS", 10),
        ("sSafariZoneCenter_FireRed", "water_mons", "SPECIES_DRATINI", 10),
        ("sSafariZoneCenter_FireRed", "fishing_mons", "SPECIES_DRATINI", 4),
        ("sSafariZoneCenter_FireRed", "fishing_mons", "SPECIES_DRAGONAIR", 1),
        ("sThreeIslandBerryForest_FireRed", "land_mons", "SPECIES_BULBASAUR", 10),
        ("sThreeIslandBerryForest_FireRed", "land_mons", "SPECIES_IVYSAUR", 4),
        ("sThreeIslandBerryForest_FireRed", "land_mons", "SPECIES_VENUSAUR", 1),
        ("sMtEmberExterior_FireRed", "land_mons", "SPECIES_CHARMANDER", 10),
        ("sMtEmberExterior_FireRed", "land_mons", "SPECIES_CHARMELEON", 4),
        ("sMtEmberExterior_FireRed", "land_mons", "SPECIES_CHARIZARD", 1),
        ("sSeafoamIslandsB1F_FireRed", "land_mons", "SPECIES_SQUIRTLE", 10),
        ("sSeafoamIslandsB1F_FireRed", "land_mons", "SPECIES_WARTORTLE", 4),
        ("sSeafoamIslandsB1F_FireRed", "land_mons", "SPECIES_BLASTOISE", 1),
        ("sMtEmberExterior_FireRed", "land_mons", "SPECIES_MAGMAR", 4),
        ("sPowerPlant_FireRed", "land_mons", "SPECIES_ELECTABUZZ", 4),
    )
    for label, kind, species, want in expected:
        got = encounter_rate(encounters, label, kind, species)
        assert got == want, (label, kind, species, got, want)

    # Dratini's 10% Surf table is its best Safari availability; Dragonair remains rarer.
    for label in (
        "sSafariZoneCenter_FireRed",
        "sSafariZoneEast_FireRed",
        "sSafariZoneNorth_FireRed",
        "sSafariZoneWest_FireRed",
    ):
        assert encounter_rate(encounters, label, "fishing_mons", "SPECIES_DRATINI") == 4
        assert encounter_rate(encounters, label, "fishing_mons", "SPECIES_DRAGONAIR") == 1

    print(
        "B5 encounter polish PASS: Altering Cave automatically rotates all nine stable "
        "tables without a manual selector, and A-009 rarity targets are exact."
    )


if __name__ == "__main__":
    main()
