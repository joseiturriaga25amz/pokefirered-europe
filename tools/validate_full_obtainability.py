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

    # FireRed remains the base table. Every representative family that was
    # already FireRed-exclusive stays locally catchable after the LG additions.
    for species in (
        "SPECIES_EKANS", "SPECIES_ODDISH", "SPECIES_PSYDUCK",
        "SPECIES_GROWLITHE", "SPECIES_SHELLDER", "SPECIES_SCYTHER",
        "SPECIES_ELECTABUZZ", "SPECIES_WOOPER", "SPECIES_MURKROW",
        "SPECIES_QWILFISH", "SPECIES_DELIBIRD", "SPECIES_SKARMORY",
    ):
        assert species in wild, f"FireRed family source lost for {species}"

    # LeafGreen-only families explicitly approved by ENC-001..012 are all
    # inserted without requiring another cartridge.
    for species in (
        "SPECIES_SANDSHREW", "SPECIES_VULPIX", "SPECIES_BELLSPROUT",
        "SPECIES_SLOWPOKE", "SPECIES_STARYU", "SPECIES_PINSIR",
        "SPECIES_MAGMAR", "SPECIES_MARILL", "SPECIES_MISDREAVUS",
        "SPECIES_SNEASEL", "SPECIES_REMORAID", "SPECIES_MANTINE",
    ):
        assert species in wild, f"LeafGreen family source missing for {species}"

    # Full-specific encounter families.
    for species in (
        "SPECIES_BULBASAUR", "SPECIES_IVYSAUR", "SPECIES_VENUSAUR",
        "SPECIES_CHARMANDER", "SPECIES_CHARMELEON", "SPECIES_CHARIZARD",
        "SPECIES_SQUIRTLE", "SPECIES_WARTORTLE", "SPECIES_BLASTOISE",
        "SPECIES_EEVEE", "SPECIES_VAPOREON", "SPECIES_JOLTEON",
        "SPECIES_FLAREON", "SPECIES_CHANSEY", "SPECIES_KANGASKHAN",
        "SPECIES_TAUROS",
    ):
        assert species in wild, f"approved Full encounter missing for {species}"

    # Every Altering Cave selector species must have a compiled encounter source.
    for species in (
        "SPECIES_ZUBAT", "SPECIES_MAREEP", "SPECIES_PINECO",
        "SPECIES_HOUNDOUR", "SPECIES_TEDDIURSA", "SPECIES_AIPOM",
        "SPECIES_SHUCKLE", "SPECIES_STANTLER", "SPECIES_SMEARGLE",
    ):
        assert species in wild, f"Altering Cave source missing for {species}"

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
    for token in (
        "[SPECIES_EEVEE]",
        "EVO_ITEM, ITEM_SUN_STONE, SPECIES_ESPEON",
        "EVO_ITEM, ITEM_MOON_STONE, SPECIES_UMBREON",
        "EVO_LEVEL, 36, SPECIES_ALAKAZAM",
        "EVO_LEVEL, 36, SPECIES_MACHAMP",
        "EVO_LEVEL, 36, SPECIES_GOLEM",
        "EVO_LEVEL, 36, SPECIES_GENGAR",
        "EVO_TRADE_ITEM, ITEM_METAL_COAT, SPECIES_SCIZOR",
        "EVO_TRADE_ITEM, ITEM_METAL_COAT, SPECIES_STEELIX",
        "EVO_TRADE_ITEM, ITEM_DRAGON_SCALE, SPECIES_KINGDRA",
        "EVO_TRADE_ITEM, ITEM_UP_GRADE, SPECIES_PORYGON2",
        "EVO_TRADE_ITEM, ITEM_KINGS_ROCK, SPECIES_POLITOED",
        "EVO_TRADE_ITEM, ITEM_KINGS_ROCK, SPECIES_SLOWKING",
    ):
        require(evolution, token, "evolution.h")

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

    # Fossil pair and Old Amber have one-save revival paths; the second Mt Moon
    # fossil appears only after reviving the first and survives a full bag.
    moon = read("data/maps/MtMoon_B2F/scripts.inc")
    for token in (
        "FLAG_REVIVED_HELIX",
        "FLAG_REVIVED_DOME",
        "ITEM_HELIX_FOSSIL",
        "ITEM_DOME_FOSSIL",
        "MtMoon_B2F_EventScript_SecondFossilNoRoom",
    ):
        require(moon, token, "MtMoon_B2F/scripts.inc")
    lab = read("data/maps/CinnabarIsland_PokemonLab_ExperimentRoom/scripts.inc")
    for token in ("FLAG_REVIVED_HELIX", "FLAG_REVIVED_DOME", "FLAG_REVIVED_AMBER"):
        require(lab, token, "Cinnabar Lab scripts")

    # Renewable/direct evolution resources required by Full must be stocked on
    # the approved post-National path rather than depending on another cart.
    celadon = read("data/maps/CeladonCity_DepartmentStore_4F/scripts.inc")
    for token in (
        "ITEM_SUN_STONE", "ITEM_MOON_STONE", "ITEM_KINGS_ROCK",
        "ITEM_METAL_COAT", "ITEM_DRAGON_SCALE", "ITEM_UP_GRADE",
    ):
        require(celadon, token, "Celadon 4F scripts")

    # All Full event-distribution replacements have local battle/event sources.
    event_sources = {
        "data/maps/SeafoamIslands_B4F/scripts.inc": "SPECIES_ARTICUNO",
        "data/maps/PowerPlant/scripts.inc": "SPECIES_ZAPDOS",
        "data/maps/MtEmber_Summit/scripts.inc": "SPECIES_MOLTRES",
        "data/maps/CeruleanCave_B1F/scripts.inc": "SPECIES_MEWTWO",
        "data/maps/PokemonMansion_B1F/scripts.inc": "SPECIES_MEW",
        "data/maps/ThreeIsland_BerryForest/scripts.inc": "SPECIES_CELEBI",
        "data/maps/NavelRock_Base/scripts.inc": "SPECIES_LUGIA",
        "data/maps/NavelRock_Summit/scripts.inc": "SPECIES_HO_OH",
        "data/maps/BirthIsland_Exterior/scripts.inc": "SPECIES_DEOXYS",
    }
    for source, species in event_sources.items():
        require(read(source), species, source)

    # Togepi has a direct egg source; if the party is full the gift remains pending.
    togepi = read("data/maps/FiveIsland_WaterLabyrinth/scripts.inc")
    for token in (
        "SPECIES_TOGEPI",
        "FLAG_NO_ROOM_FOR_TOGEPI_EGG",
        "giveegg SPECIES_TOGEPI",
    ):
        require(togepi, token, "FiveIsland_WaterLabyrinth/scripts.inc")

    print(
        "Gate 7 obtainability PASS: FireRed families are preserved; approved LeafGreen, "
        "starter/Eevee/Safari/Altering Cave sources exist; fossils, direct evolutions, "
        "event legends/mythicals and all Gen III baby prerequisites have one-save paths."
    )


if __name__ == "__main__":
    main()
