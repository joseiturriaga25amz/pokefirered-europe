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
"sParty_RivalOaksLabSquirtle":[
("SQUIRTLE",5,0,"NONE",("TACKLE","TAIL_WHIP","NONE","NONE")),
],
"sParty_RivalRoute22EarlySquirtle":[
("PIDGEY",10,50,"NONE",("GUST","TACKLE","SAND_ATTACK","NONE")),
("SQUIRTLE",12,50,"NONE",("BUBBLE","TACKLE","WITHDRAW","TAIL_WHIP")),
],
"sParty_RivalCeruleanSquirtle":[
("PIDGEOTTO",20,83,"NONE",("QUICK_ATTACK","GUST","SAND_ATTACK","WHIRLWIND")),
("NIDORINO",19,83,"NONE",("PECK","DOUBLE_KICK","POISON_STING","FOCUS_ENERGY")),
("KADABRA",18,83,"NONE",("CONFUSION","DISABLE","KINESIS","TELEPORT")),
("WARTORTLE",22,83,"NONE",("WATER_GUN","BITE","WITHDRAW","TAIL_WHIP")),
],
"sParty_RivalSsAnneSquirtle":[
("NIDORINO",24,99,"NONE",("HORN_ATTACK","DOUBLE_KICK","POISON_STING","FOCUS_ENERGY")),
("PIDGEOTTO",25,99,"NONE",("QUICK_ATTACK","GUST","SAND_ATTACK","WHIRLWIND")),
("KADABRA",25,99,"NONE",("PSYBEAM","RECOVER","DISABLE","REFLECT")),
("WARTORTLE",28,99,"NONE",("WATER_PULSE","BITE","PROTECT","RAPID_SPIN")),
],
"sParty_RivalPokemonTowerSquirtle":[
("EXEGGCUTE",30,116,"NONE",("CONFUSION","HYPNOSIS","LEECH_SEED","REFLECT")),
("PIDGEOTTO",31,116,"NONE",("QUICK_ATTACK","GUST","WING_ATTACK","WHIRLWIND")),
("GROWLITHE",31,116,"NONE",("FLAME_WHEEL","TAKE_DOWN","EMBER","ROAR")),
("NIDOKING",30,116,"NONE",("PECK","HORN_ATTACK","DIG","DOUBLE_KICK")),
("KADABRA",32,116,"NONE",("PSYBEAM","RECOVER","FUTURE_SIGHT","REFLECT")),
("WARTORTLE",34,116,"NONE",("WATER_PULSE","BITE","PROTECT","RAPID_SPIN")),
],
"sParty_RivalSilphSquirtle":[
("PIDGEOT",44,149,"NONE",("QUICK_ATTACK","FEATHER_DANCE","AERIAL_ACE","WHIRLWIND")),
("NIDOKING",43,149,"NONE",("EARTHQUAKE","HORN_ATTACK","MEGAHORN","DOUBLE_KICK")),
("EXEGGUTOR",43,149,"NONE",("PSYCHIC","GIGA_DRAIN","EGG_BOMB","HYPNOSIS")),
("ARCANINE",44,149,"NONE",("FLAME_WHEEL","TAKE_DOWN","FLAMETHROWER","ROAR")),
("ALAKAZAM",46,149,"NONE",("PSYCHIC","CALM_MIND","REFLECT","RECOVER")),
("BLASTOISE",49,149,"SITRUS_BERRY",("RAIN_DANCE","PROTECT","BITE","SURF")),
],
"sParty_RivalRoute22LateSquirtle":[
("EXEGGUTOR",56,198,"NONE",("PSYCHIC","GIGA_DRAIN","EGG_BOMB","HYPNOSIS")),
("PIDGEOT",56,198,"NONE",("QUICK_ATTACK","FEATHER_DANCE","AERIAL_ACE","AGILITY")),
("NIDOKING",57,198,"NONE",("EARTHQUAKE","MEGAHORN","TOXIC","BRICK_BREAK")),
("ALAKAZAM",58,198,"NONE",("PSYCHIC","CALM_MIND","SHOCK_WAVE","RECOVER")),
("ARCANINE",59,198,"NONE",("FLAMETHROWER","EXTREME_SPEED","BITE","ROAR")),
("BLASTOISE",61,198,"MYSTIC_WATER",("RAIN_DANCE","ICE_BEAM","BITE","SURF")),
],
"sParty_EliteFourLorelei":[
("DEWGONG",57,P198,"NONE",("ICE_BEAM","SURF","HAIL","AURORA_BEAM")),
("CLOYSTER",58,P198,"NONE",("DIVE","SPIKES","HAIL","PROTECT")),
("SLOWPOKE",56,P198,"NONE",("PSYCHIC","HEADBUTT","AMNESIA","DISABLE")),
("SLOWBRO",59,P198,"NONE",("ICE_BEAM","SURF","AMNESIA","YAWN")),
("JYNX",60,P198,"NONE",("ICE_BEAM","DOUBLE_SLAP","LOVELY_KISS","ATTRACT")),
("LAPRAS",61,P198,"SITRUS_BERRY",("ICE_BEAM","SURF","BODY_SLAM","CONFUSE_RAY")),
],
"sParty_EliteFourBruno":[
("ONIX",58,206,"NONE",("EARTHQUAKE","IRON_TAIL","ROAR","ROCK_TOMB")),
("HITMONCHAN",59,206,"NONE",("SKY_UPPERCUT","MACH_PUNCH","ROCK_TOMB","COUNTER")),
("HITMONLEE",60,206,"NONE",("MEGA_KICK","FORESIGHT","BRICK_BREAK","FACADE")),
("ONIX",60,206,"NONE",("DOUBLE_EDGE","EARTHQUAKE","IRON_TAIL","SAND_TOMB")),
("MACHAMP",62,206,"SITRUS_BERRY",("CROSS_CHOP","ROCK_TOMB","SCARY_FACE","BULK_UP")),
],
"sParty_EliteFourAgatha":[
("GENGAR",59,P214,"NONE",("CONFUSE_RAY","SHADOW_BALL","DOUBLE_TEAM","TOXIC")),
("GOLBAT",60,P214,"NONE",("CONFUSE_RAY","BITE","WING_ATTACK","TOXIC")),
("HAUNTER",60,P214,"NONE",("MEAN_LOOK","PROTECT","HYPNOSIS","DREAM_EATER")),
("ARBOK",61,P214,"NONE",("BITE","SLUDGE_BOMB","SCREECH","IRON_TAIL")),
("GENGAR",63,P214,"SITRUS_BERRY",("SHADOW_BALL","SLUDGE_BOMB","HYPNOSIS","NIGHTMARE")),
],
"sParty_EliteFourLance":[
("GYARADOS",64,P223,"NONE",("WATERFALL","DRAGON_DANCE","EARTHQUAKE","DOUBLE_EDGE")),
("DRAGONAIR",61,P223,"NONE",("DRAGON_BREATH","THUNDER_WAVE","ICE_BEAM","SAFEGUARD")),
("AERODACTYL",63,P223,"NONE",("ROCK_SLIDE","AERIAL_ACE","EARTHQUAKE","DOUBLE_EDGE")),
("DRAGONAIR",62,P223,"NONE",("OUTRAGE","FLAMETHROWER","THUNDERBOLT","THUNDER_WAVE")),
("DRAGONITE",65,P223,"SITRUS_BERRY",("DRAGON_CLAW","AERIAL_ACE","ICE_BEAM","FLAMETHROWER")),
],
"sParty_ChampionFirstSquirtle":[
("PIDGEOT",64,231,"NONE",("AERIAL_ACE","DOUBLE_EDGE","STEEL_WING","FEATHER_DANCE")),
("NIDOKING",65,231,"NONE",("EARTHQUAKE","ROCK_SLIDE","BRICK_BREAK","TOXIC")),
("ALAKAZAM",65,231,"NONE",("PSYCHIC","SHADOW_BALL","RECOVER","CALM_MIND")),
("ARCANINE",67,231,"NONE",("EXTREME_SPEED","FLAMETHROWER","DIG","SUNNY_DAY")),
("EXEGGUTOR",66,231,"NONE",("SOLAR_BEAM","GIGA_DRAIN","PSYCHIC","HYPNOSIS")),
("BLASTOISE",69,247,"LEFTOVERS",("HYDRO_PUMP","ICE_BEAM","EARTHQUAKE","RAIN_DANCE")),
],
"sParty_EliteFourLorelei2":[
("DEWGONG",75,P239,"NONE",("ICE_BEAM","SURF","SIGNAL_BEAM","SAFEGUARD")),
("CLOYSTER",77,P239,"NONE",("SURF","ICE_BEAM","SPIKES","PROTECT")),
("PILOSWINE",74,P239,"NONE",("BLIZZARD","EARTHQUAKE","DOUBLE_EDGE","ROCK_SLIDE")),
("SLOWKING",76,P239,"NONE",("PSYCHIC","SURF","ICE_BEAM","DISABLE")),
("JYNX",75,P239,"NONE",("ICE_BEAM","PSYCHIC","LOVELY_KISS","ATTRACT")),
("LAPRAS",79,P247,"LEFTOVERS",("SURF","BLIZZARD","THUNDERBOLT","PROTECT")),
],
"sParty_EliteFourBruno2":[
("HITMONTOP",75,239,"NONE",("BRICK_BREAK","STRENGTH","ROLLING_KICK","DETECT")),
("HITMONCHAN",76,239,"NONE",("BRICK_BREAK","FIRE_PUNCH","ICE_PUNCH","THUNDER_PUNCH")),
("HITMONLEE",76,239,"NONE",("BRICK_BREAK","MEGA_KICK","HI_JUMP_KICK","DETECT")),
("HARIYAMA",77,239,"NONE",("FAKE_OUT","VITAL_THROW","STRENGTH","SEISMIC_TOSS")),
("STEELIX",78,239,"NONE",("IRON_TAIL","EARTHQUAKE","CRUNCH","DIG")),
("MACHAMP",80,247,"BLACK_BELT",("CROSS_CHOP","ROCK_SLIDE","DOUBLE_EDGE","BULK_UP")),
],
"sParty_EliteFourAgatha2":[
("GENGAR",76,P247,"NONE",("SHADOW_BALL","PSYCHIC","HYPNOSIS","CONFUSE_RAY")),
("MISDREAVUS",77,P239,"NONE",("SHADOW_BALL","PSYCHIC","THUNDERBOLT","MEAN_LOOK")),
("ARBOK",77,P239,"NONE",("SLUDGE_BOMB","EARTHQUAKE","SCREECH","TOXIC")),
("SABLEYE",78,P239,"NONE",("SHADOW_BALL","FAINT_ATTACK","DETECT","CONFUSE_RAY")),
("CROBAT",79,P239,"NONE",("AERIAL_ACE","SLUDGE_BOMB","TOXIC","CONFUSE_RAY")),
("GENGAR",81,P247,"SPELL_TAG",("SHADOW_BALL","SLUDGE_BOMB","THUNDERBOLT","PSYCHIC")),
],
"sParty_EliteFourLance2":[
("GYARADOS",81,P239,"NONE",("WATERFALL","DRAGON_DANCE","EARTHQUAKE","DOUBLE_EDGE")),
("KINGDRA",79,P239,"NONE",("WATERFALL","DRAGON_DANCE","ICE_BEAM","DRAGON_BREATH")),
("CHARIZARD",80,P239,"NONE",("FLAMETHROWER","DRAGON_CLAW","AERIAL_ACE","EARTHQUAKE")),
("SALAMENCE",80,P239,"NONE",("DRAGON_CLAW","FLAMETHROWER","EARTHQUAKE","ROCK_SLIDE")),
("AERODACTYL",80,P239,"NONE",("ROCK_SLIDE","AERIAL_ACE","EARTHQUAKE","DOUBLE_EDGE")),
("DRAGONITE",82,P247,"LEFTOVERS",("DRAGON_DANCE","DRAGON_CLAW","EARTHQUAKE","FLAMETHROWER")),
],
"sParty_ChampionRematchSquirtle":[
("UMBREON",80,239,"NONE",("BITE","TOXIC","CONFUSE_RAY","MOONLIGHT")),
("GOLEM",81,239,"NONE",("EARTHQUAKE","EXPLOSION","DOUBLE_EDGE","ROCK_SLIDE")),
("NIDOQUEEN",80,239,"NONE",("EARTHQUAKE","SLUDGE_BOMB","ICE_BEAM","THUNDERBOLT")),
("SCIZOR",82,239,"NONE",("STEEL_WING","AERIAL_ACE","QUICK_ATTACK","SWORDS_DANCE")),
("ARCANINE",83,239,"NONE",("FIRE_BLAST","EXTREME_SPEED","DIG","FLAMETHROWER")),
("BLASTOISE",85,247,"LEFTOVERS",("HYDRO_PUMP","ICE_BEAM","EARTHQUAKE","RAIN_DANCE")),
],
}

def main():
    oak_lab = (ROOT / "data/maps/PalletTown_ProfessorOaksLab/scripts.inc").read_text(encoding="utf-8")
    assert oak_lab.count("setvar RIVAL_STARTER_SPECIES, SPECIES_SQUIRTLE") == 3
    assert "setvar RIVAL_STARTER_SPECIES, SPECIES_BULBASAUR" not in oak_lab
    assert "setvar RIVAL_STARTER_SPECIES, SPECIES_CHARMANDER" not in oak_lab

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

    # RIV-001: every actual Gary battle route must use the Squirtle branch,
    # independent of the player's starter. The old Bulbasaur/Charmander party
    # definitions may remain as inert compatibility data, but scripts must not select them.
    script_paths = (
        "data/maps/PalletTown_ProfessorOaksLab/scripts.inc",
        "data/maps/Route22/scripts.inc",
        "data/maps/CeruleanCity/scripts.inc",
        "data/maps/SSAnne_2F_Corridor/scripts.inc",
        "data/maps/PokemonTower_2F/scripts.inc",
        "data/maps/SilphCo_7F/scripts.inc",
        "data/maps/PokemonLeague_ChampionsRoom/scripts.inc",
    )
    for script_path in script_paths:
        text = (ROOT / script_path).read_text(encoding="utf-8")
        for forbidden in (
            "TRAINER_RIVAL_OAKS_LAB_BULBASAUR",
            "TRAINER_RIVAL_OAKS_LAB_CHARMANDER",
            "TRAINER_RIVAL_ROUTE22_EARLY_BULBASAUR",
            "TRAINER_RIVAL_ROUTE22_EARLY_CHARMANDER",
            "TRAINER_RIVAL_ROUTE22_LATE_BULBASAUR",
            "TRAINER_RIVAL_ROUTE22_LATE_CHARMANDER",
            "TRAINER_RIVAL_CERULEAN_BULBASAUR",
            "TRAINER_RIVAL_CERULEAN_CHARMANDER",
            "TRAINER_RIVAL_SS_ANNE_BULBASAUR",
            "TRAINER_RIVAL_SS_ANNE_CHARMANDER",
            "TRAINER_RIVAL_POKEMON_TOWER_BULBASAUR",
            "TRAINER_RIVAL_POKEMON_TOWER_CHARMANDER",
            "TRAINER_RIVAL_SILPH_BULBASAUR",
            "TRAINER_RIVAL_SILPH_CHARMANDER",
            "TRAINER_CHAMPION_FIRST_BULBASAUR",
            "TRAINER_CHAMPION_FIRST_CHARMANDER",
            "TRAINER_CHAMPION_REMATCH_BULBASAUR",
            "TRAINER_CHAMPION_REMATCH_CHARMANDER",
        ):
            assert forbidden not in text, (script_path, forbidden)

    print(
        "Boss RC PASS: Gary progression plus first/rematch League "
        "rosters/levels/IVs/items/moves and fixed Squirtle battle routing match freeze."
    )

if __name__=="__main__":
    main()
