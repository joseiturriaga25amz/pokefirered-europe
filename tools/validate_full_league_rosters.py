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
        held_match=re.search(r"\.heldItem\s*=\s*ITEM_([A-Z0-9_]+)",body)
        held=held_match.group(1) if held_match else "NONE"
        moves=tuple(re.findall(r"MOVE_([A-Z0-9_]+)", req(r"\.moves\s*=\s*\{([^}]*)\}","moves")))
        out.append((species,lvl,iv,held,moves))
    return out

P0=0
P50=50
P83=83
P99=99
P116=116
P149=149
P198=198
P206=206
P214=214
P223=223
P231=231
P239=239
P247=247
EXPECTED={
" sParty_RivalOaksLabSquirtle".strip():[
("SQUIRTLE",5,P0,"NONE",("TACKLE","TAIL_WHIP","NONE","NONE")),
],
"sParty_RivalRoute22EarlySquirtle":[
("PIDGEY",10,P50,"NONE",("TACKLE","SAND_ATTACK","GUST","NONE")),
("SQUIRTLE",12,P50,"NONE",("TACKLE","TAIL_WHIP","BUBBLE","WITHDRAW")),
],
"sParty_RivalCeruleanSquirtle":[
("ABRA",18,P83,"NONE",("PSYCHIC","REFLECT","LIGHT_SCREEN","TELEPORT")),
("RATTATA",19,P83,"NONE",("HYPER_FANG","QUICK_ATTACK","TAIL_WHIP","TACKLE")),
("PIDGEOTTO",20,P83,"NONE",("QUICK_ATTACK","GUST","SAND_ATTACK","WHIRLWIND")),
("SQUIRTLE",22,P83,"NONE",("WATER_GUN","BITE","WITHDRAW","BUBBLE")),
],
"sParty_RivalSsAnneSquirtle":[
("KRABBY",24,P99,"NONE",("MUD_SHOT","VICE_GRIP","BUBBLE","HARDEN")),
("PIDGEOTTO",25,P99,"NONE",("AERIAL_ACE","QUICK_ATTACK","SAND_ATTACK","WHIRLWIND")),
("KADABRA",25,P99,"NONE",("PSYBEAM","RECOVER","REFLECT","DISABLE")),
("WARTORTLE",28,P99,"NONE",("WATER_PULSE","BITE","RAPID_SPIN","PROTECT")),
],
"sParty_RivalPokemonTowerSquirtle":[
("EXEGGCUTE",30,P116,"NONE",("PSYCHIC","GIGA_DRAIN","STUN_SPORE","LEECH_SEED")),
("PIDGEOTTO",31,P116,"NONE",("AERIAL_ACE","RETURN","SAND_ATTACK","WHIRLWIND")),
("GROWLITHE",31,P116,"NONE",("FLAME_WHEEL","TAKE_DOWN","BITE","ROAR")),
("KADABRA",32,P116,"NONE",("PSYBEAM","RECOVER","REFLECT","FUTURE_SIGHT")),
("WARTORTLE",34,P116,"NONE",("WATER_PULSE","BITE","PROTECT","RAPID_SPIN")),
],
"sParty_RivalSilphSquirtle":[
("EXEGGUTOR",43,P149,"NONE",("PSYCHIC","GIGA_DRAIN","SLEEP_POWDER","REFLECT")),
("PIDGEOT",44,P149,"NONE",("AERIAL_ACE","RETURN","FEATHER_DANCE","SAND_ATTACK")),
("GROWLITHE",44,P149,"NONE",("FLAMETHROWER","BITE","TAKE_DOWN","ROAR")),
("ALAKAZAM",46,P149,"NONE",("PSYCHIC","CALM_MIND","RECOVER","REFLECT")),
("BLASTOISE",49,P149,"SITRUS_BERRY",("SURF","ICE_BEAM","BITE","PROTECT")),
],
"sParty_RivalRoute22LateSquirtle":[
("RHYHORN",56,P198,"NONE",("EARTHQUAKE","ROCK_SLIDE","DOUBLE_EDGE","IRON_TAIL")),
("PIDGEOT",56,P198,"NONE",("AERIAL_ACE","RETURN","STEEL_WING","FEATHER_DANCE")),
("NIDOKING",57,P198,"NONE",("EARTHQUAKE","MEGAHORN","ICE_BEAM","THUNDERBOLT")),
("ALAKAZAM",58,P198,"NONE",("PSYCHIC","CALM_MIND","RECOVER","SHOCK_WAVE")),
("ARCANINE",59,P198,"NONE",("FLAMETHROWER","EXTREME_SPEED","IRON_TAIL","BITE")),
("BLASTOISE",61,P198,"MYSTIC_WATER",("SURF","ICE_BEAM","EARTHQUAKE","RAIN_DANCE")),
],
"sParty_EliteFourLorelei":[
("DEWGONG",57,P198,"NONE",("ICE_BEAM","SURF","HAIL","SAFEGUARD")),
("SLOWBRO",58,P198,"NONE",("SURF","PSYCHIC","ICE_BEAM","AMNESIA")),
("JYNX",59,P198,"NONE",("ICE_BEAM","PSYCHIC","LOVELY_KISS","ATTRACT")),
("CLOYSTER",60,P198,"NEVER_MELT_ICE",("ICE_BEAM","SURF","SPIKES","PROTECT")),
("LAPRAS",61,P198,"SITRUS_BERRY",("ICE_BEAM","SURF","THUNDERBOLT","BODY_SLAM")),
],
"sParty_EliteFourBruno":[
("ONIX",58,P206,"NONE",("EARTHQUAKE","ROCK_TOMB","IRON_TAIL","SANDSTORM")),
("HITMONCHAN",59,P206,"FOCUS_BAND",("SKY_UPPERCUT","MACH_PUNCH","ICE_PUNCH","THUNDER_PUNCH")),
("HITMONLEE",60,P206,"NONE",("BRICK_BREAK","MEGA_KICK","ROCK_SLIDE","EARTHQUAKE")),
("ONIX",60,P206,"NONE",("EARTHQUAKE","ROCK_SLIDE","DOUBLE_EDGE","IRON_TAIL")),
("MACHAMP",62,P206,"BLACK_BELT",("CROSS_CHOP","BULK_UP","ROCK_SLIDE","EARTHQUAKE")),
],
"sParty_EliteFourAgatha":[
("HAUNTER",59,P214,"NONE",("SHADOW_BALL","HYPNOSIS","DREAM_EATER","MEAN_LOOK")),
("GENGAR",60,P214,"NONE",("SHADOW_BALL","PSYCHIC","CONFUSE_RAY","TOXIC")),
("GOLBAT",60,P214,"NONE",("AERIAL_ACE","POISON_FANG","BITE","CONFUSE_RAY")),
("ARBOK",61,P214,"NONE",("POISON_FANG","EARTHQUAKE","ROCK_SLIDE","GLARE")),
("GENGAR",63,P214,"SPELL_TAG",("SHADOW_BALL","SLUDGE_BOMB","THUNDERBOLT","HYPNOSIS")),
],
"sParty_EliteFourLance":[
("GYARADOS",61,P223,"NONE",("WATERFALL","DRAGON_DANCE","EARTHQUAKE","HYPER_BEAM")),
("DRAGONAIR",61,P223,"NONE",("OUTRAGE","THUNDER_WAVE","ICE_BEAM","SAFEGUARD")),
("DRAGONAIR",62,P223,"NONE",("OUTRAGE","FLAMETHROWER","THUNDERBOLT","THUNDER_WAVE")),
("AERODACTYL",63,P223,"HARD_STONE",("ROCK_SLIDE","AERIAL_ACE","EARTHQUAKE","DOUBLE_EDGE")),
("DRAGONITE",65,P223,"DRAGON_FANG",("OUTRAGE","AERIAL_ACE","ICE_BEAM","FLAMETHROWER")),
],
"sParty_ChampionFirstSquirtle":[
("PIDGEOT",64,P231,"NONE",("AERIAL_ACE","RETURN","STEEL_WING","FEATHER_DANCE")),
("ALAKAZAM",65,P231,"NONE",("PSYCHIC","CALM_MIND","RECOVER","SHOCK_WAVE")),
("NIDOKING",65,P231,"NONE",("EARTHQUAKE","MEGAHORN","ICE_BEAM","THUNDERBOLT")),
("RHYDON",66,P231,"SOFT_SAND",("EARTHQUAKE","ROCK_SLIDE","MEGAHORN","DOUBLE_EDGE")),
("ARCANINE",67,P231,"CHARCOAL",("FLAMETHROWER","EXTREME_SPEED","IRON_TAIL","BITE")),
("BLASTOISE",69,P247,"LEFTOVERS",("HYDRO_PUMP","ICE_BEAM","EARTHQUAKE","RAIN_DANCE")),
],
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
    gary_bases = (
        "sParty_RivalOaksLabSquirtle",
        "sParty_RivalRoute22EarlySquirtle",
        "sParty_RivalCeruleanSquirtle",
        "sParty_RivalSsAnneSquirtle",
        "sParty_RivalPokemonTowerSquirtle",
        "sParty_RivalSilphSquirtle",
        "sParty_RivalRoute22LateSquirtle",
        "sParty_ChampionFirstSquirtle",
        "sParty_ChampionRematchSquirtle",
    )
    for name in gary_bases:
        base=block(name)
        for suffix in ("Bulbasaur","Charmander"):
            other=block(name.replace("Squirtle", suffix))
            assert re.sub(r"\s+"," ",other).strip()==re.sub(r"\s+"," ",base).strip(), (name, suffix)

    print(
        "Boss RC PASS: Gary progression plus first/rematch League "
        "rosters/levels/IVs/items/moves exactly match freeze."
    )

if __name__=="__main__":
    main()
