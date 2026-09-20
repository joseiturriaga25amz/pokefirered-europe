#!/usr/bin/env python3
"""Static obtainability audit for ENC-022 baby Pokémon and hidden breeding prerequisites."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def wild_species():
    data = json.loads(read("src/data/wild_encounters.json"))
    found = set()

    def walk(node):
        if isinstance(node, dict):
            species = node.get("species")
            if isinstance(species, str) and species.startswith("SPECIES_"):
                found.add(species)
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(data)
    return found


def require(text, token, source):
    assert token in text, f"{source}: missing {token}"


def main():
    wild = wild_species()

    # Every ordinary breeding route below can be completed on one FireRed Full
    # save because Ditto is catchable and every required parent has a local source.
    for species in (
        "SPECIES_DITTO",
        "SPECIES_PIKACHU",
        "SPECIES_CLEFAIRY",
        "SPECIES_JIGGLYPUFF",
        "SPECIES_ELECTABUZZ",
        "SPECIES_MAGMAR",
        "SPECIES_MARILL",
        "SPECIES_WOBBUFFET",
    ):
        assert species in wild, f"wild source missing for {species}"

    evolution = read("src/data/pokemon/evolution.h")
    baby_to_parent = {
        "SPECIES_PICHU": "SPECIES_PIKACHU",
        "SPECIES_CLEFFA": "SPECIES_CLEFAIRY",
        "SPECIES_IGGLYBUFF": "SPECIES_JIGGLYPUFF",
        "SPECIES_TOGEPI": "SPECIES_TOGETIC",
        "SPECIES_TYROGUE": "SPECIES_HITMONLEE",
        "SPECIES_SMOOCHUM": "SPECIES_JYNX",
        "SPECIES_ELEKID": "SPECIES_ELECTABUZZ",
        "SPECIES_MAGBY": "SPECIES_MAGMAR",
        "SPECIES_AZURILL": "SPECIES_MARILL",
        "SPECIES_WYNAUT": "SPECIES_WOBBUFFET",
    }
    for baby, parent in baby_to_parent.items():
        require(evolution, f"[{baby}]", "evolution.h")
        require(evolution, parent, "evolution.h")

    daycare = read("src/daycare.c")
    for token in (
        "static u16 GetEggSpecies(u16 species)",
        "gEvolutionTable[j][k].targetSpecies == species",
        "AlterEggSpeciesWithIncenseItem",
        "SPECIES_WYNAUT",
        "ITEM_LAX_INCENSE",
        "SPECIES_AZURILL",
        "ITEM_SEA_INCENSE",
    ):
        require(daycare, token, "daycare.c")

    item_balls = read("data/scripts/item_ball_scripts.inc")
    require(item_balls, "ITEM_LAX_INCENSE", "item_ball_scripts.inc")
    require(item_balls, "ITEM_SEA_INCENSE", "item_ball_scripts.inc")

    # Smoochum: Jynx is obtainable by the vanilla in-game trade; its requested
    # Poliwhirl is itself reachable from catchable Poliwag.
    trades = read("src/data/ingame_trades.h")
    require(trades, "INGAME_TRADE_JYNX", "ingame_trades.h")
    require(trades, ".species = SPECIES_JYNX", "ingame_trades.h")
    require(trades, ".requestedSpecies = SPECIES_POLIWHIRL", "ingame_trades.h")
    assert "SPECIES_POLIWAG" in wild, "Poliwag source missing for Jynx trade prerequisite"
    require(evolution, "SPECIES_POLIWHIRL", "evolution.h")

    # Tyrogue: either original Dojo choice is obtainable, and the second trial
    # makes the opposite Hitmon available without external trading.
    dojo = read("data/maps/SaffronCity_Dojo/scripts.inc")
    for token in (
        "SPECIES_HITMONLEE",
        "SPECIES_HITMONCHAN",
        "SaffronCity_Dojo_EventScript_GiveSecondHitmon",
        "SaffronCity_Dojo_EventScript_SecondRewardNoRoom",
    ):
        require(dojo, token, "SaffronCity_Dojo/scripts.inc")

    # Togepi has a direct egg source; if the party is full the gift remains pending.
    togepi = read("data/maps/FiveIsland_WaterLabyrinth/scripts.inc")
    for token in (
        "SPECIES_TOGEPI",
        "FLAG_NO_ROOM_FOR_TOGEPI_EGG",
        "giveegg SPECIES_TOGEPI",
    ):
        require(togepi, token, "FiveIsland_WaterLabyrinth/scripts.inc")

    print(
        "ENC-022 obtainability PASS: Pichu, Cleffa, Igglybuff, Togepi, Tyrogue, "
        "Smoochum, Elekid, Magby, Azurill and Wynaut have one-save parent/resource paths."
    )


if __name__ == "__main__":
    main()
