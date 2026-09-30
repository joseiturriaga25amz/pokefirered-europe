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
        ("sParty_RSTuberM","GLOOM",69,False),
        ("sParty_LeaderKoga","GOLBAT",46,False),
        ("sParty_RSCooltrainerM","CROBAT",71,False),
        ("sParty_LeaderSabrina","KADABRA",47,False),
        ("sParty_RSCooltrainerF","KADABRA",72,False),
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
        ("sParty_RSTuberM","GLOOM",69,"MIRACLE_SEED"),
        ("sParty_LeaderSabrina","KADABRA",47,"TWISTED_SPOON"),
        ("sParty_RSCooltrainerF","KADABRA",72,"TWISTED_SPOON"),
        ("sParty_LeaderKoga","GOLBAT",46,"SHARP_BEAK"),
    ]
    for name,species,level,item in special:
        mon=exact_mon(name,species,level)
        assert mon["iv"] == 255, (name,species,"expected max IV",mon["iv"])
        assert mon["item"] == item, (name,species,"expected item",item,mon["item"])

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

    # Koga first-battle ace identity: preserve anime Wing Attack + Screech core.
    koga_text = block("sParty_LeaderKoga")
    assert "MOVE_WING_ATTACK" in koga_text
    assert "MOVE_SCREECH" in koga_text
    assert "MOVE_TOXIC" not in koga_text[koga_text.index("SPECIES_GOLBAT"):]

    # Freeze the exact user-approved ace movesets from the 2026-09-28 transversal pass.
    approved_moves = {
        ("sParty_LeaderErika", "GLOOM", 35): ("PETAL_DANCE", "SLEEP_POWDER", "MOONLIGHT", "ACID"),
        ("sParty_RSTuberM", "GLOOM", 69): ("SOLAR_BEAM", "SLUDGE_BOMB", "SLEEP_POWDER", "SUNNY_DAY"),
        ("sParty_LeaderKoga", "GOLBAT", 46): ("WING_ATTACK", "BITE", "CONFUSE_RAY", "SCREECH"),
        ("sParty_RSCooltrainerM", "CROBAT", 71): ("AERIAL_ACE", "POISON_FANG", "BITE", "CONFUSE_RAY"),
        ("sParty_LeaderSabrina", "KADABRA", 47): ("PSYCHIC", "CALM_MIND", "RECOVER", "REFLECT"),
        ("sParty_RSCooltrainerF", "KADABRA", 72): ("PSYCHIC", "CALM_MIND", "RECOVER", "REFLECT"),
        ("sParty_LeaderBlaine", "MAGMAR", 52): ("FIRE_BLAST", "FLAMETHROWER", "FIRE_PUNCH", "BRICK_BREAK"),
        ("sParty_RSLady", "MAGMAR", 73): ("FLAMETHROWER", "FIRE_BLAST", "BRICK_BREAK", "CONFUSE_RAY"),
        ("sParty_EliteFourLance", "DRAGONITE", 65): ("DRAGON_CLAW", "AERIAL_ACE", "ICE_BEAM", "FLAMETHROWER"),
        ("sParty_EliteFourLance2", "DRAGONITE", 82): ("OUTRAGE", "THUNDERBOLT", "ICE_BEAM", "FLAMETHROWER"),
    }
    for (party, species, level), moves in approved_moves.items():
        mon = exact_mon(party, species, level)
        assert mon["moves"] == moves, (party, species, level, mon["moves"], moves)

    print("B3 global ace identity PASS: leaders, Giovanni, Elite Four, Gary progression and Lance Red Gyarados identity match approved rules.")

if __name__ == "__main__":
    main()
