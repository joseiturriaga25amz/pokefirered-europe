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


def c_function(text, signature):
    start = text.index(signature)
    end = text.index("\n}\n", start) + 2
    return text[start:end]


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

    hof = read("data/scripts/spanish/hall_of_fame.inc")
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

    # RC-F041: Koichi is a sight-range trainer object. FireRed's approach engine
    # parses script+1 directly as trainerbattle data, so the first executable
    # opcode must remain trainerbattle rather than a conditional wrapper.
    koichi = block(dojo, "SaffronCity_Dojo_EventScript_MasterKoichi")
    koichi_lines = [line.strip() for line in koichi.splitlines()[1:] if line.strip() and not line.lstrip().startswith("@")]
    assert koichi_lines[0].startswith(
        "trainerbattle_single TRAINER_BLACK_BELT_KOICHI,"
    ), koichi_lines[0]

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

    # Sequential roamers: capture advances Suicune -> Raikou -> Entei -> done,
    # while KO heals/repositions the same identity and InitRoamer cannot restart a
    # completed sequence.
    roamer = read("src/roamer.c")
    require(
        roamer,
        "case 0:\n        return SPECIES_SUICUNE;",
        "case 1:\n        return SPECIES_RAIKOU;",
        "case 2:\n        return SPECIES_ENTEI;",
        "if (ROAMER->active || VarGet(VAR_FULL_ROAMER_SEQUENCE) >= 3)",
        "if (ROAMER->hp == 0)",
        "ROAMER->hp = GetMonData(mon, MON_DATA_MAX_HP);",
        "RoamerMoveToOtherLocationSet();",
        "VarSet(VAR_FULL_ROAMER_SEQUENCE, sequence + 1);",
        "CreateInitialRoamerMon();",
        "VarSet(VAR_FULL_ROAMER_SEQUENCE, 3);",
    )
    update = c_function(roamer, "void UpdateRoamerHPStatus(struct Pokemon *mon)")
    assert "VAR_FULL_ROAMER_SEQUENCE" not in update
    inactive = c_function(roamer, "void SetRoamerInactive(void)")
    assert inactive.index("VarSet(VAR_FULL_ROAMER_SEQUENCE, sequence + 1);") < inactive.index("CreateInitialRoamerMon();")

    # Aurora quest is a 0 -> 1 (Celio signal) -> 2 (Pewter analysis) -> 3
    # (ticket delivered) machine. A full bag must not advance the final state.
    museum = read("data/maps/PewterCity_Museum_1F/scripts.inc")
    require(
        celio,
        "goto_if_eq VAR_FULL_AURORA_QUEST, 0, OneIsland_PokemonCenter_1F_EventScript_FullDetectAuroraSignal",
        "goto_if_eq VAR_FULL_AURORA_QUEST, 2, OneIsland_PokemonCenter_1F_EventScript_FullGiveAuroraTicket",
        "setvar VAR_FULL_AURORA_QUEST, 1",
        "setvar VAR_FULL_AURORA_QUEST, 3",
    )
    require(
        museum,
        "goto_if_eq VAR_FULL_AURORA_QUEST, 1, PewterCity_Museum_1F_EventScript_FullAnalyzeAuroraSignal",
        "setvar VAR_FULL_AURORA_QUEST, 2",
    )
    ticket_no_room = block(celio, "OneIsland_PokemonCenter_1F_EventScript_FullTicketNoRoom")
    assert "setvar VAR_FULL_MYSTIC_QUEST" not in ticket_no_room
    assert "setvar VAR_FULL_AURORA_QUEST" not in ticket_no_room

    # MysticTicket is gated by all three captured birds, not merely prior fights
    # that are still waiting for Hall-of-Fame KO recovery.
    mystic = block(celio, "OneIsland_PokemonCenter_1F_EventScript_FullPostgameQuests")
    for species in ("ARTICUNO", "ZAPDOS", "MOLTRES"):
        require(
            mystic,
            f"goto_if_unset FLAG_FOUGHT_{species}",
            f"goto_if_set FLAG_FULL_{species}_KO_PENDING",
        )
    require(
        celio,
        "setflag FLAG_RECEIVED_MYSTIC_TICKET",
        "setflag FLAG_ENABLE_SHIP_NAVEL_ROCK",
        "setvar VAR_FULL_MYSTIC_QUEST, 1",
    )

    # Altering Cave selector persists one of the nine original table indices.
    cave = read("data/maps/SixIsland_AlteringCave/scripts.inc")
    altering_species = (
        "Zubat", "Mareep", "Pineco", "Houndour", "Teddiursa",
        "Aipom", "Shuckle", "Stantler", "Smeargle",
    )
    for value, species in enumerate(altering_species):
        require(
            cave,
            f"SixIsland_AlteringCave_EventScript_Set{species}::",
            f"setvar VAR_ALTERING_CAVE_WILD_SET, {value}",
        )
    require(
        cave,
        "case 127, SixIsland_AlteringCave_EventScript_ResearcherEnd",
        "SixIsland_AlteringCave_EventScript_ResearcherChanged::",
    )

    # Porygon remains a repeatable coin purchase: the species-specific branch
    # sets the frozen price and returns to the generic prize path without a
    # one-time ownership flag; successful party/PC awards both remove coins.
    game_corner = read("data/maps/CeladonCity_GameCorner_PrizeRoom/scripts.inc")
    porygon = block(game_corner, "CeladonCity_GameCorner_PrizeRoom_EventScript_Porygon")
    require(porygon, "SPECIES_PORYGON", "setvar VAR_TEMP_2, 5000")
    assert "setflag " not in porygon
    require(
        game_corner,
        "CeladonCity_GameCorner_PrizeRoom_EventScript_GivePorygon::",
        "givemon VAR_TEMP_1, 26",
    )
    for label in (
        "CeladonCity_GameCorner_PrizeRoom_EventScript_ReceivedMonParty",
        "CeladonCity_GameCorner_PrizeRoom_EventScript_ReceivedMonPC",
    ):
        require(block(game_corner, label), "removecoins VAR_TEMP_2")

    # The 15 ordinary move tutors are first-use-free and repeat-paid. Their
    # persisted vanilla tutor flag selects the repeat branch; payment happens
    # only after a successful repeat teaching choice.
    tutors = read("data/scripts/spanish/move_tutors.inc")
    tutor_states = (
        ("DoubleEdge", "FLAG_TUTOR_DOUBLE_EDGE", 5000),
        ("ThunderWave", "FLAG_TUTOR_THUNDER_WAVE", 6500),
        ("RockSlide", "FLAG_TUTOR_ROCK_SLIDE", 7500),
        ("Explosion", "FLAG_TUTOR_EXPLOSION", 6000),
        ("MegaPunch", "FLAG_TUTOR_MEGA_PUNCH", 1500),
        ("MegaKick", "FLAG_TUTOR_MEGA_KICK", 2500),
        ("DreamEater", "FLAG_TUTOR_DREAM_EATER", 3000),
        ("Softboiled", "FLAG_TUTOR_SOFT_BOILED", 5000),
        ("Substitute", "FLAG_TUTOR_SUBSTITUTE", 8000),
        ("SwordsDance", "FLAG_TUTOR_SWORDS_DANCE", 10000),
        ("SeismicToss", "FLAG_TUTOR_SEISMIC_TOSS", 3500),
        ("Counter", "FLAG_TUTOR_COUNTER", 4000),
        ("Metronome", "FLAG_TUTOR_METRONOME", 1000),
        ("Mimic", "FLAG_TUTOR_MIMIC", 2000),
        ("BodySlam", "FLAG_TUTOR_BODY_SLAM", 6000),
    )
    for name, flag, price in tutor_states:
        require(tutors, f"goto_if_set {flag}, EventScript_{name}Repeat", f"setflag {flag}")
        repeat = block(tutors, f"EventScript_{name}Repeat")
        require(repeat, f"checkmoney {price}", f"removemoney {price}")
        assert repeat.index(f"checkmoney {price}") < repeat.index(f"removemoney {price}")
    require(
        tutors,
        "CapeBrinkTutor_EventScript_RepeatOffer::",
        "checkmoney 10000",
        "CapeBrinkTutor_EventScript_ChargeRepeat::",
        "removemoney 10000",
    )

    # Two Island berry shop progression retains its staged vanilla flags and
    # switches every stage to the common post-National stock after National Dex.
    two_island = read("data/maps/TwoIsland/scripts.inc")
    for value in range(1, 5):
        require(two_island, f"setvar VAR_MAP_SCENE_TWO_ISLAND, {value}")
    for flag in (
        "FLAG_TWO_ISLAND_SHOP_INTRODUCED",
        "FLAG_TWO_ISLAND_SHOP_EXPANDED_1",
        "FLAG_TWO_ISLAND_SHOP_EXPANDED_2",
        "FLAG_TWO_ISLAND_SHOP_EXPANDED_3",
    ):
        require(two_island, f"setflag {flag}")
    assert two_island.count(
        "goto_if_set FLAG_SYS_NATIONAL_DEX, TwoIsland_EventScript_ShopPostNational"
    ) == 4
    for berry in (
        "ITEM_POMEG_BERRY", "ITEM_KELPSY_BERRY", "ITEM_QUALOT_BERRY",
        "ITEM_HONDEW_BERRY", "ITEM_GREPA_BERRY", "ITEM_TAMATO_BERRY",
        "ITEM_LIECHI_BERRY", "ITEM_GANLON_BERRY", "ITEM_SALAC_BERRY",
        "ITEM_PETAYA_BERRY", "ITEM_APICOT_BERRY", "ITEM_LANSAT_BERRY",
        "ITEM_STARF_BERRY",
    ):
        require(two_island, berry)

    # BOSS-002: all eight Gym Leader rematches remain indefinitely repeatable.
    # Each post-National leader route must clear its repurposed trainer flag
    # immediately before battle and must not persist a one-shot rematch flag.
    gym_rematches = (
        ("PewterCity_Gym", "Brock", "FLAG_GOT_TM39_FROM_BROCK", "TRAINER_RS_AROMA_LADY"),
        ("CeruleanCity_Gym", "Misty", "FLAG_GOT_TM03_FROM_MISTY", "TRAINER_RS_RUIN_MANIAC"),
        ("VermilionCity_Gym", "LtSurge", "FLAG_GOT_TM34_FROM_SURGE", "TRAINER_RS_TUBER_F"),
        ("CeladonCity_Gym", "Erika", "FLAG_GOT_TM19_FROM_ERIKA", "TRAINER_RS_TUBER_M"),
        ("FuchsiaCity_Gym", "Koga", "FLAG_GOT_TM06_FROM_KOGA", "TRAINER_RS_COOLTRAINER_M"),
        ("SaffronCity_Gym", "Sabrina", "FLAG_GOT_TM04_FROM_SABRINA", "TRAINER_RS_COOLTRAINER_F"),
        ("CinnabarIsland_Gym", "Blaine", "FLAG_GOT_TM38_FROM_BLAINE", "TRAINER_RS_LADY"),
        ("ViridianCity_Gym", "Giovanni", "FLAG_GOT_TM26_FROM_GIOVANNI", "TRAINER_RS_BEAUTY"),
    )
    for map_name, leader, tm_flag, trainer in gym_rematches:
        script = read(f"data/maps/{map_name}/scripts.inc")
        require(
            script,
            "goto_if_unset FLAG_SYS_NATIONAL_DEX",
            f"goto_if_unset {tm_flag}",
            f"cleartrainerflag {trainer}",
            f"trainerbattle_single {trainer}",
        )
        offer = block(script, f"{map_name}_EventScript_FullRematchOffer")
        assert offer.index(f"cleartrainerflag {trainer}") < offer.index(f"trainerbattle_single {trainer}")
        assert "setflag FLAG_FULL" not in offer
        assert "setvar VAR_FULL" not in offer

    print("Persistent event-state audit PASS: terminal branches and recovery transitions are locked.")


if __name__ == "__main__":
    main()
