#!/usr/bin/env python3
"""Validate approved symbolic ace identity across Full boss progression."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TEXT = (ROOT / "src/data/trainer_parties.h").read_text(encoding="utf-8")

def block(name):
    m = re.search(r"static const struct [^ ]+ " + re.escape(name) + r"\[\] = \{(.*?)\n\};", TEXT, re.S)
    assert m, f"missing party {name}"
    return m.group(1)

def rows(name):
    out=[]
    for m in re.finditer(r"\{(.*?)\n\s*\},", block(name), re.S):
        body=m.group(1)
        def req(pattern,label):
            x=re.search(pattern,body)
            assert x, f"{name}: missing {label}"
            return x.group(1)
        out.append({
            "iv": int(req(r"\.iv\s*=\s*(\d+)","iv")),
            "lvl": int(req(r"\.lvl\s*=\s*(\d+)","lvl")),
            "species": req(r"\.species\s*=\s*SPECIES_([A-Z0-9_]+)","species"),
            "item": req(r"\.heldItem\s*=\s*ITEM_([A-Z0-9_]+)","item") if ".heldItem" in body else "NONE",
            "moves": tuple(
                x.strip().removeprefix("MOVE_")
                for x in req(r"\.moves\s*=\s*\{([^}]*)\}","moves").split(",")
            ),
        })
    return out

def exact_mon(name, species, level):
    matches=[m for m in rows(name) if m["species"] == species and m["lvl"] == level]
    assert len(matches) == 1, (name, species, level, matches)
    return matches[0]

def assert_top(name, species, level, allow_tie=False):
    mons=rows(name)
    mon=exact_mon(name,species,level)
    peak=max(x["lvl"] for x in mons)
    assert mon["lvl"] == peak, (name, species, mon["lvl"], peak)
    if not allow_tie:
        assert sum(x["lvl"] == peak for x in mons) == 1, (name, "ace level tie", peak)

def main():
    # Gym Leaders: first encounter -> postgame rematch.
    # Misty's rematch intentionally separates visual identity from battle ace:
    # Starmie remains her signature companion, while Gyarados is the unique highest-level ace.
    gym_aces = [
        ("sParty_LeaderBrock","ONIX",17,False),
        ("sParty_RSAromaLady","STEELIX",68,False),
        ("sParty_LeaderMisty","STARMIE",26,False),
        ("sParty_RSRuinManiac","GYARADOS",68,False),
        ("sParty_LeaderLtSurge","RAICHU",30,False),
        ("sParty_RSTuberF","RAICHU",69,False),
        ("sParty_LeaderErika","GLOOM",35,False),
        ("sParty_RSTuberM","VILEPLUME",69,False),
        ("sParty_LeaderKoga","GOLBAT",44,False),
        ("sParty_RSCooltrainerM","CROBAT",71,False),
        ("sParty_LeaderSabrina","KADABRA",47,False),
        ("sParty_RSCooltrainerF","ALAKAZAM",72,False),
        ("sParty_LeaderBlaine","MAGMAR",52,False),
        ("sParty_RSLady","MAGMAR",73,False),
        # Mewtwo is an intentional narrative superweapon tied at Lv56; Rhydon is Giovanni's trainer ace.
        ("sParty_LeaderGiovanni","RHYDON",56,True),
        ("sParty_RSBeauty","RHYDON",74,False),
    ]
    for args in gym_aces:
        assert_top(*args)

    # Giovanni's pre-Gym story progression.
    assert_top("sParty_BossGiovanni","KANGASKHAN",33,False)
    assert_top("sParty_BossGiovanni2","NIDOQUEEN",49,False)

    # Elite Four first League and strengthened League.
    league_aces = [
        ("sParty_EliteFourLorelei","LAPRAS",61,False),
        ("sParty_EliteFourLorelei2","LAPRAS",79,False),
        ("sParty_EliteFourBruno","MACHAMP",62,False),
        ("sParty_EliteFourBruno2","MACHAMP",80,False),
        ("sParty_EliteFourAgatha","GENGAR",63,False),
        ("sParty_EliteFourAgatha2","GENGAR",81,False),
        ("sParty_EliteFourLance","DRAGONITE",65,False),
        ("sParty_EliteFourLance2","DRAGONITE",82,False),
    ]
    for args in league_aces:
        assert_top(*args)

    # Gary/Blue: anime-faithful Squirtle -> Wartortle -> Blastoise remains his ace throughout.
    gary = [
        ("sParty_RivalOaksLabSquirtle","SQUIRTLE",5),
        ("sParty_RivalRoute22EarlySquirtle","SQUIRTLE",12),
        ("sParty_RivalCeruleanSquirtle","SQUIRTLE",22),
        ("sParty_RivalSsAnneSquirtle","WARTORTLE",28),
        ("sParty_RivalPokemonTowerSquirtle","WARTORTLE",34),
        ("sParty_RivalSilphSquirtle","BLASTOISE",49),
        ("sParty_RivalRoute22LateSquirtle","BLASTOISE",61),
        ("sParty_ChampionFirstSquirtle","BLASTOISE",69),
        ("sParty_ChampionRematchSquirtle","BLASTOISE",85),
    ]
    for name,species,level in gary:
        assert_top(name,species,level,False)

    # Intermediate-stage symbolic aces deliberately receive maximum trainer IVs plus a meaningful item.
    special = [
        ("sParty_LeaderErika","GLOOM",35,"SITRUS_BERRY"),
        ("sParty_LeaderSabrina","KADABRA",47,"TWISTED_SPOON"),
        ("sParty_LeaderKoga","GOLBAT",44,"SHARP_BEAK"),
    ]
    for name,species,level,item in special:
        mon=exact_mon(name,species,level)
        assert mon["iv"] == 255, (name,species,"expected max IV",mon["iv"])
        assert mon["item"] == item, (name,species,"expected item",item,mon["item"])

    # Giovanni keeps Rhydon as the combat ace; Mewtwo is a separate narrative superweapon.
    giovanni_story_ace = exact_mon("sParty_LeaderGiovanni","RHYDON",56)
    assert giovanni_story_ace["item"] == "SOFT_SAND", ("sParty_LeaderGiovanni","RHYDON","expected item","SOFT_SAND",giovanni_story_ace["item"])
    giovanni_rematch_ace = exact_mon("sParty_RSBeauty","RHYDON",74)
    assert giovanni_rematch_ace["item"] == "SOFT_SAND", ("sParty_RSBeauty","RHYDON","expected item","SOFT_SAND",giovanni_rematch_ace["item"])
    giovanni_mewtwo = exact_mon("sParty_LeaderGiovanni","MEWTWO",56)
    assert giovanni_mewtwo["iv"] == 255, ("sParty_LeaderGiovanni","MEWTWO","expected max IV",giovanni_mewtwo["iv"])
    assert giovanni_mewtwo["item"] == "NONE", ("sParty_LeaderGiovanni","MEWTWO","expected no item",giovanni_mewtwo["item"])

    # A-016 Lorelei: Lapras is the sole held-item user in both League encounters.
    lorelei_story_ace = exact_mon("sParty_EliteFourLorelei","LAPRAS",61)
    assert lorelei_story_ace["item"] == "SITRUS_BERRY", ("sParty_EliteFourLorelei","LAPRAS","expected item","SITRUS_BERRY",lorelei_story_ace["item"])
    lorelei_rematch_ace = exact_mon("sParty_EliteFourLorelei2","LAPRAS",79)
    assert lorelei_rematch_ace["item"] == "LEFTOVERS", ("sParty_EliteFourLorelei2","LAPRAS","expected item","LEFTOVERS",lorelei_rematch_ace["item"])
    for party_name, ace_species in (("sParty_EliteFourLorelei","LAPRAS"),("sParty_EliteFourLorelei2","LAPRAS")):
        for mon in parties[party_name]:
            if mon["species"] != ace_species:
                assert mon["item"] == "NONE", (party_name, mon["species"], "non-ace held item", mon["item"])

    # Sabrina's evolved rematch ace uses the normal rematch IV tier.
    sabrina_rematch_ace = exact_mon("sParty_RSCooltrainerF","ALAKAZAM",72)
    assert sabrina_rematch_ace["iv"] == 231, ("sParty_RSCooltrainerF","ALAKAZAM","expected normal rematch IV",sabrina_rematch_ace["iv"])
    assert sabrina_rematch_ace["item"] == "TWISTED_SPOON", ("sParty_RSCooltrainerF","ALAKAZAM","expected item","TWISTED_SPOON",sabrina_rematch_ace["item"])

    # Erika's evolved rematch ace no longer needs intermediate-stage max-IV compensation.
    erika_rematch_ace = exact_mon("sParty_RSTuberM","VILEPLUME",69)
    assert erika_rematch_ace["iv"] == 214, ("sParty_RSTuberM","VILEPLUME","expected normal rematch IV",erika_rematch_ace["iv"])
    assert erika_rematch_ace["item"] == "MIRACLE_SEED", ("sParty_RSTuberM","VILEPLUME","expected item","MIRACLE_SEED",erika_rematch_ace["item"])

    # Lance's Gyarados is the same canonical Red Gyarados in both League encounters.
    battle_main = (ROOT / "src/battle_main.c").read_text(encoding="utf-8")
    shiny_scope = battle_main[battle_main.index("// Full canon identity: Lance owns the Red Gyarados"):
                              battle_main.index("gBattleTypeFlags |= gTrainers[trainerNum].doubleBattle;")]
    assert "TRAINER_ELITE_FOUR_LANCE" in shiny_scope
    assert "TRAINER_ELITE_FOUR_LANCE_2" in shiny_scope
    assert "SPECIES_GYARADOS" in shiny_scope
    assert "MON_DATA_OT_ID" in shiny_scope
    assert "MON_DATA_PERSONALITY" in shiny_scope
    assert "SHINY_ODDS" not in shiny_scope
    assert "Random()" not in shiny_scope
    assert "Random32()" not in shiny_scope

    # Koga first-battle ace identity: anime-priority Golbat remains the max-IV signature ace.
    koga_text = block("sParty_LeaderKoga")
    assert "MOVE_WING_ATTACK" in koga_text
    assert "MOVE_SLUDGE_BOMB" in koga_text[koga_text.index("SPECIES_GOLBAT"):]
    assert "MOVE_TOXIC" in koga_text[koga_text.index("SPECIES_GOLBAT"):]

    # Freeze the current user-approved ace movesets. Erika was intentionally amended after the 2026-09-28 pass.
    approved_moves = {
        ("sParty_LeaderErika", "GLOOM", 35): ("PETAL_DANCE", "ACID", "POISON_POWDER", "SLEEP_POWDER"),
        ("sParty_RSTuberM", "VILEPLUME", 69): ("SOLAR_BEAM", "SLUDGE_BOMB", "SYNTHESIS", "SUNNY_DAY"),
        ("sParty_LeaderKoga", "GOLBAT", 44): ("SLUDGE_BOMB", "WING_ATTACK", "BITE", "TOXIC"),
        ("sParty_RSCooltrainerM", "CROBAT", 71): ("SLUDGE_BOMB", "AERIAL_ACE", "DOUBLE_TEAM", "TOXIC"),
        ("sParty_LeaderSabrina", "KADABRA", 47): ("PSYCHIC", "REFLECT", "CALM_MIND", "RECOVER"),
        ("sParty_RSCooltrainerF", "ALAKAZAM", 72): ("PSYCHIC", "SHADOW_BALL", "CALM_MIND", "RECOVER"),
        ("sParty_LeaderBlaine", "MAGMAR", 52): ("FIRE_BLAST", "FLAMETHROWER", "FIRE_PUNCH", "STRENGTH"),
        ("sParty_RSLady", "MAGMAR", 73): ("FLAMETHROWER", "FIRE_BLAST", "PSYCHIC", "BRICK_BREAK"),
        ("sParty_EliteFourLorelei", "LAPRAS", 61): ("ICE_BEAM", "SURF", "BODY_SLAM", "CONFUSE_RAY"),
        ("sParty_EliteFourLorelei2", "LAPRAS", 79): ("SURF", "BLIZZARD", "THUNDERBOLT", "PROTECT"),
        ("sParty_LeaderGiovanni", "RHYDON", 56): ("EARTHQUAKE", "ROCK_SLIDE", "DOUBLE_EDGE", "BRICK_BREAK"),
        ("sParty_RSBeauty", "RHYDON", 74): ("EARTHQUAKE", "ROCK_SLIDE", "DOUBLE_EDGE", "MEGAHORN"),
        ("sParty_LeaderGiovanni", "MEWTWO", 56): ("PSYCHIC", "SHADOW_BALL", "SWIFT", "RECOVER"),
        ("sParty_EliteFourLance", "DRAGONITE", 65): ("DRAGON_CLAW", "AERIAL_ACE", "ICE_BEAM", "FLAMETHROWER"),
        ("sParty_EliteFourLance2", "DRAGONITE", 82): ("OUTRAGE", "THUNDERBOLT", "ICE_BEAM", "FLAMETHROWER"),
    }
    for (party, species, level), moves in approved_moves.items():
        mon = exact_mon(party, species, level)
        assert mon["moves"] == moves, (party, species, level, mon["moves"], moves)

    print("B3 global ace identity PASS: leaders, Giovanni, Elite Four, Gary progression and Lance Red Gyarados identity match approved rules.")

if __name__ == "__main__":
    main()
