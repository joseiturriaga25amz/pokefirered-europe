#!/usr/bin/env python3
"""Lock frozen Elite Four/Champion RC rosters beyond mere move legality."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTIES = (ROOT / "src/data/trainer_parties.h").read_text(encoding="utf-8")

def block(name):
    m = re.search(r"static const struct [^ ]+ " + re.escape(name) + r"\[\] = \{(.*?)\n\};", PARTIES, re.S)
    assert m, f"missing party {name}"
    return m.group(1)

def rows(name):
    out=[]
    for mon in re.finditer(r"\{(.*?)\n\s*\},", block(name), re.S):
        body=mon.group(1)
        def req(pattern,label):
            m=re.search(pattern,body)
            assert m, f"{name}: missing {label}"
            return m.group(1)
        iv=int(req(r"\.iv\s*=\s*(\d+)","iv"))
        lvl=int(req(r"\.lvl\s*=\s*(\d+)","level"))
        species=req(r"\.species\s*=\s*SPECIES_([A-Z0-9_]+)","species")
        held=req(r"\.heldItem\s*=\s*ITEM_([A-Z0-9_]+)","held item")
        moves=tuple(re.findall(r"MOVE_([A-Z0-9_]+)", req(r"\.moves\s*=\s*\{([^}]*)\}","moves")))
        out.append((species,lvl,iv,held,moves))
    return out

P239=239
P247=247
EXPECTED={
"sParty_EliteFourLorelei2":[
("DEWGONG",74,P239,"NEVER_MELT_ICE",("ICE_BEAM","SURF","HAIL","SAFEGUARD")),
("CLOYSTER",75,P239,"NONE",("ICE_BEAM","SURF","SPIKES","PROTECT")),
("SLOWBRO",75,P239,"TWISTED_SPOON",("SURF","PSYCHIC","ICE_BEAM","CALM_MIND")),
("PILOSWINE",76,P239,"NONE",("EARTHQUAKE","ROCK_SLIDE","BLIZZARD","HAIL")),
("JYNX",77,P239,"NONE",("ICE_BEAM","PSYCHIC","LOVELY_KISS","CALM_MIND")),
("LAPRAS",79,P247,"LEFTOVERS",("ICE_BEAM","SURF","THUNDERBOLT","BODY_SLAM")),
],
"sParty_EliteFourBruno2":[
("ONIX",75,P239,"HARD_STONE",("EARTHQUAKE","ROCK_SLIDE","IRON_TAIL","SANDSTORM")),
("STEELIX",76,P239,"NONE",("EARTHQUAKE","ROCK_SLIDE","IRON_TAIL","CRUNCH")),
("HITMONCHAN",76,P239,"BLACK_BELT",("SKY_UPPERCUT","MACH_PUNCH","ICE_PUNCH","THUNDER_PUNCH")),
("HITMONLEE",77,P239,"NONE",("BRICK_BREAK","MEGA_KICK","ROCK_SLIDE","EARTHQUAKE")),
("HITMONTOP",78,P239,"FOCUS_BAND",("TRIPLE_KICK","ROCK_SLIDE","COUNTER","BULK_UP")),
("MACHAMP",80,P247,"LEFTOVERS",("CROSS_CHOP","BULK_UP","ROCK_SLIDE","EARTHQUAKE")),
],
"sParty_EliteFourAgatha2":[
("GENGAR",76,P247,"NONE",("SHADOW_BALL","PSYCHIC","HYPNOSIS","DREAM_EATER")),
("CROBAT",77,P239,"SHARP_BEAK",("AERIAL_ACE","POISON_FANG","BITE","CONFUSE_RAY")),
("MISDREAVUS",77,P239,"SPELL_TAG",("SHADOW_BALL","PSYCHIC","THUNDERBOLT","PERISH_SONG")),
("ARBOK",79,P239,"POISON_BARB",("POISON_FANG","EARTHQUAKE","ROCK_SLIDE","GLARE")),
("GENGAR",81,P247,"LEFTOVERS",("SHADOW_BALL","SLUDGE_BOMB","THUNDERBOLT","HYPNOSIS")),
],
"sParty_EliteFourLance2":[
("GYARADOS",78,P239,"MYSTIC_WATER",("WATERFALL","DRAGON_DANCE","EARTHQUAKE","HYPER_BEAM")),
("KINGDRA",79,P239,"NONE",("WATERFALL","ICE_BEAM","DRAGON_DANCE","HYPER_BEAM")),
("DRAGONITE",79,P247,"DRAGON_FANG",("EARTHQUAKE","DRAGON_CLAW","FLAMETHROWER","ICE_BEAM")),
("AERODACTYL",81,P239,"HARD_STONE",("ROCK_SLIDE","AERIAL_ACE","EARTHQUAKE","DOUBLE_EDGE")),
("DRAGONITE",82,P247,"LEFTOVERS",("OUTRAGE","THUNDERBOLT","ICE_BEAM","FLAMETHROWER")),
],
"sParty_ChampionRematchSquirtle":[
("NIDOQUEEN",80,P239,"SOFT_SAND",("EARTHQUAKE","SUPERPOWER","ICE_BEAM","THUNDERBOLT")),
("MAGMAR",80,P239,"CHARCOAL",("FLAMETHROWER","FIRE_BLAST","BRICK_BREAK","CONFUSE_RAY")),
("GOLEM",81,P239,"HARD_STONE",("EARTHQUAKE","ROCK_SLIDE","DOUBLE_EDGE","EXPLOSION")),
("SCIZOR",82,P239,"METAL_COAT",("SWORDS_DANCE","STEEL_WING","AERIAL_ACE","QUICK_ATTACK")),
("ARCANINE",83,P239,"NONE",("FLAMETHROWER","EXTREME_SPEED","IRON_TAIL","BITE")),
("BLASTOISE",85,P247,"LEFTOVERS",("HYDRO_PUMP","ICE_BEAM","EARTHQUAKE","RAIN_DANCE")),
],
}

def main():
    for name,want in EXPECTED.items():
        got=rows(name)
        assert got==want, f"{name} drift:\nGOT {got}\nWANT {want}"
    base=block("sParty_ChampionRematchSquirtle")
    for suffix in ("Bulbasaur","Charmander"):
        other=block("sParty_ChampionRematch"+suffix)
        assert re.sub(r"\s+"," ",other).strip()==re.sub(r"\s+"," ",base).strip(), suffix
    print("Boss RC PASS: Elite Four rematch and Champion rematch rosters/levels/IVs/items/moves exactly match freeze.")

if __name__=="__main__":
    main()
