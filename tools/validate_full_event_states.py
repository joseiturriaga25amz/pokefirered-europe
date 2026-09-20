#!/usr/bin/env python3
"""Static transition audit for persistent Full event state machines."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def require(text, *tokens):
    for token in tokens:
        assert token in text, f"missing transition token: {token}"


def block(text, label):
    marker = label + "::"
    start = text.index(marker)
    next_label = text.find("\n\n", start)
    if next_label == -1:
        return text[start:]
    return text[start:next_label]


def check_kanto_static(path, prefix, species, fought, pending):
    text = read(path)
    main = block(text, f"{prefix}_EventScript_{species.title().replace('_', '')}")
    require(
        main,
        "B_OUTCOME_CAUGHT",
        "B_OUTCOME_WON",
        "B_OUTCOME_RAN",
        "B_OUTCOME_PLAYER_TELEPORTED",
    )
    caught = block(text, f"{prefix}_EventScript_Captured{species.title().replace('_', '')}")
    defeated = block(text, f"{prefix}_EventScript_Defeated{species.title().replace('_', '')}")
    ran = block(text, f"{prefix}_EventScript_RanFrom{species.title().replace('_', '')}")
    require(caught, f"clearflag {pending}", f"setflag {fought}")
    require(defeated, f"setflag {pending}", f"setflag {fought}", "EventScript_RemoveStaticMon")
    require(ran, f"SPECIES_{species.upper()}", "EventScript_MonFlewAway")
    assert f"setflag {fought}" not in ran
    assert f"setflag {pending}" not in ran


def main():
    # Kanto statics: flee is retry-now, KO is HOF-pending, capture is terminal.
    checks = [
        ("data/maps/SeafoamIslands_B4F/scripts.inc", "SeafoamIslands_B4F", "Articuno",
         "FLAG_FOUGHT_ARTICUNO", "FLAG_FULL_ARTICUNO_KO_PENDING"),
        ("data/maps/PowerPlant/scripts.inc", "PowerPlant", "Zapdos",
         "FLAG_FOUGHT_ZAPDOS", "FLAG_FULL_ZAPDOS_KO_PENDING"),
        ("data/maps/MtEmber_Summit/scripts.inc", "MtEmber_Summit", "Moltres",
         "FLAG_FOUGHT_MOLTRES", "FLAG_FULL_MOLTRES_KO_PENDING"),
        ("data/maps/CeruleanCave_B1F/scripts.inc", "CeruleanCave_B1F", "Mewtwo",
         "FLAG_FOUGHT_MEWTWO", "FLAG_FULL_MEWTWO_KO_PENDING"),
    ]
    for path, prefix, species, fought, pending in checks:
        check_kanto_static(path, prefix, species, fought, pending)

    hof = read("data/scripts/hall_of_fame.inc")
    for species in ("ZAPDOS", "ARTICUNO", "MOLTRES", "MEWTWO"):
        require(
            hof,
            f"call_if_set FLAG_FULL_{species}_KO_PENDING",
            f"clearflag FLAG_FOUGHT_{species}",
            f"clearflag FLAG_FULL_{species}_KO_PENDING",
        )

    # Event-island legends: capture sets FOUGHT, KO uses vanilla FLEW_AWAY,
    # flee/teleport does not consume the encounter; HOF clears FLEW_AWAY.
    event_legends = [
        ("data/maps/NavelRock_Base/scripts.inc", "LUGIA", "70"),
        ("data/maps/NavelRock_Summit/scripts.inc", "HO_OH", "70"),
        ("data/maps/BirthIsland_Exterior/scripts.inc", "DEOXYS", "50"),
    ]
    for path, species, level in event_legends:
        text = read(path)
        require(
            text,
            f"seteventmon SPECIES_{species}, {level}",
            "B_OUTCOME_WON",
            "B_OUTCOME_RAN",
            "B_OUTCOME_PLAYER_TELEPORTED",
            f"setflag FLAG_FOUGHT_{species}",
            f"setflag FLAG_{species}_FLEW_AWAY",
        )
        require(hof, f"clearflag FLAG_{species}_FLEW_AWAY")

    # Mew: flee leaves battle-ready state 4, KO parks at 5+pending, HOF restores 4.
    mew = read("data/maps/PokemonMansion_B1F/scripts.inc")
    require(
        mew,
        "goto_if_eq VAR_FULL_MEW_QUEST, 4, PokemonMansion_B1F_EventScript_FullMewBattle",
        "B_OUTCOME_CAUGHT, PokemonMansion_B1F_EventScript_FullMewCaught",
        "B_OUTCOME_WON, PokemonMansion_B1F_EventScript_FullMewDefeated",
        "setflag FLAG_FULL_MEW_CAUGHT",
        "clearflag FLAG_FULL_MEW_KO_PENDING",
        "setflag FLAG_FULL_MEW_KO_PENDING",
        "setvar VAR_FULL_MEW_QUEST, 5",
    )
    assert mew.count("setvar VAR_FULL_MEW_QUEST, 5") == 2
    require(hof, "clearflag FLAG_FULL_MEW_KO_PENDING", "setvar VAR_FULL_MEW_QUEST, 4")

    # Celebi: requirements gate the tree; flee leaves event available, KO waits for HOF.
    celebi = read("data/maps/ThreeIsland_BerryForest/scripts.inc")
    require(
        celebi,
        "goto_if_set FLAG_FULL_CELEBI_CAUGHT",
        "goto_if_set FLAG_FULL_CELEBI_KO_PENDING",
        "IsNationalPokedexEnabled",
        "FLAG_SYS_CAN_LINK_WITH_RS",
        "VAR_FULL_ROAMER_SEQUENCE, 3",
        "B_OUTCOME_CAUGHT, ThreeIsland_BerryForest_EventScript_FullCelebiCaught",
        "B_OUTCOME_WON, ThreeIsland_BerryForest_EventScript_FullCelebiDefeated",
        "setflag FLAG_FULL_CELEBI_CAUGHT",
        "setflag FLAG_FULL_CELEBI_KO_PENDING",
    )
    require(hof, "clearflag FLAG_FULL_CELEBI_KO_PENDING", "setvar VAR_FULL_CELEBI_QUEST, 0")

    # Second Dojo reward: opposite species and no-room branch must not consume reward.
    dojo = read("data/maps/SaffronCity_Dojo/scripts.inc")
    require(
        dojo,
        "goto_if_unset FLAG_DEFEATED_SABRINA",
        "goto_if_set FLAG_FULL_DOJO_SECOND_REWARD",
        "goto_if_set FLAG_FULL_DOJO_CHOSE_HITMONLEE",
        "setvar VAR_TEMP_1, SPECIES_HITMONLEE",
        "setvar VAR_TEMP_1, SPECIES_HITMONCHAN",
        "goto_if_eq VAR_RESULT, 2, SaffronCity_Dojo_EventScript_SecondRewardNoRoom",
        "setflag FLAG_FULL_DOJO_SECOND_REWARD",
    )
    no_room = block(dojo, "SaffronCity_Dojo_EventScript_SecondRewardNoRoom")
    assert "FLAG_FULL_DOJO_SECOND_REWARD" not in no_room

    # Second fossil: first fossil must be revived; no-room branch cannot set GOT/HIDE.
    moon = read("data/maps/MtMoon_B2F/scripts.inc")
    require(
        moon,
        "goto_if_unset FLAG_REVIVED_HELIX",
        "goto_if_unset FLAG_REVIVED_DOME",
        "checkitemspace ITEM_DOME_FOSSIL, 1",
        "checkitemspace ITEM_HELIX_FOSSIL, 1",
        "MtMoon_B2F_EventScript_SecondFossilNoRoom",
    )
    fossil_no_room = block(moon, "MtMoon_B2F_EventScript_SecondFossilNoRoom")
    assert "FLAG_GOT_DOME_FOSSIL" not in fossil_no_room
    assert "FLAG_GOT_HELIX_FOSSIL" not in fossil_no_room

    # Ticket quests: successful delivery must keep original item + receipt + ferry state.
    celio = read("data/maps/OneIsland_PokemonCenter_1F/scripts.inc")
    for token in (
        "ITEM_MYSTIC_TICKET",
        "setflag FLAG_RECEIVED_MYSTIC_TICKET",
        "setflag FLAG_ENABLE_SHIP_NAVEL_ROCK",
        "ITEM_AURORA_TICKET",
        "setflag FLAG_RECEIVED_AURORA_TICKET",
        "setflag FLAG_ENABLE_SHIP_BIRTH_ISLAND",
    ):
        require(celio, token)
    museum = read("data/maps/PewterCity_Museum_1F/scripts.inc")
    require(museum, "VAR_FULL_AURORA_QUEST, 1", "setvar VAR_FULL_AURORA_QUEST, 2")

    print("Persistent event-state audit PASS: terminal branches and recovery transitions are locked.")


if __name__ == "__main__":
    main()
