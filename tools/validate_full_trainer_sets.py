#!/usr/bin/env python3
"""Static legality audit for Pokemon Rojo Fuego Full trainer sets.

Checks the frozen Full boss/rival parties against the actual FRLG/Full data:
- species/move/item identifiers exist;
- level and trainer-IV byte are valid;
- each custom move is obtainable by level-up, TM/HM, tutor, egg move,
  or through an evolutionary ancestor using those same methods.

This intentionally validates mechanics from repository data instead of
maintaining a second hand-written learnability table.
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PARTIES = [
    # Story leaders
    "sParty_LeaderBrock",
    "sParty_LeaderMisty",
    "sParty_LeaderLtSurge",
    "sParty_LeaderErika",
    "sParty_LeaderKoga",
    "sParty_LeaderSabrina",
    "sParty_LeaderBlaine",
    "sParty_LeaderGiovanni",
    # Giovanni Rocket boss progression
    "sParty_BossGiovanni",
    "sParty_BossGiovanni2",
    # First League
    "sParty_EliteFourLorelei",
    "sParty_EliteFourBruno",
    "sParty_EliteFourAgatha",
    "sParty_EliteFourLance",
    # Leader rematches
    "sParty_RSAromaLady",
    "sParty_RSRuinManiac",
    "sParty_RSTuberF",
    "sParty_RSTuberM",
    "sParty_RSCooltrainerM",
    "sParty_RSCooltrainerF",
    "sParty_RSLady",
    "sParty_RSBeauty",
    # League rematches
    "sParty_EliteFourLorelei2",
    "sParty_EliteFourBruno2",
    "sParty_EliteFourAgatha2",
    "sParty_EliteFourLance2",
    # Gary: Squirtle branch is canonical; CI separately proves the other
    # two branches are byte-for-byte roster clones of it.
    "sParty_RivalOaksLabSquirtle",
    "sParty_RivalRoute22EarlySquirtle",
    "sParty_RivalCeruleanSquirtle",
    "sParty_RivalSsAnneSquirtle",
    "sParty_RivalPokemonTowerSquirtle",
    "sParty_RivalSilphSquirtle",
    "sParty_RivalRoute22LateSquirtle",
    "sParty_ChampionFirstSquirtle",
    "sParty_ChampionRematchSquirtle",
    # Second Fighting Dojo challenge
    "sParty_RSBlackBelt",
]

# Strict design exceptions approved during the B2 first-cycle audit.
# These are deliberately narrow: party + species + level + move must all match.
BROCK_EXPECTED = {
    "sParty_LeaderBrock": [
        ("SPECIES_ZUBAT", 13, "ITEM_NONE", ("MOVE_WING_ATTACK", "MOVE_LEECH_LIFE", "MOVE_WHIRLWIND", "MOVE_SUPERSONIC")),
        ("SPECIES_VULPIX", 14, "ITEM_NONE", ("MOVE_EMBER", "MOVE_QUICK_ATTACK", "MOVE_FIRE_SPIN", "MOVE_AGILITY")),
        ("SPECIES_GEODUDE", 15, "ITEM_NONE", ("MOVE_ROCK_THROW", "MOVE_TACKLE", "MOVE_REVENGE", "MOVE_DEFENSE_CURL")),
        ("SPECIES_ONIX", 17, "ITEM_ORAN_BERRY", ("MOVE_ROCK_TOMB", "MOVE_TACKLE", "MOVE_BIND", "MOVE_SCREECH")),
    ],
    "sParty_RSAromaLady": [
        ("SPECIES_MARSHTOMP", 60, "ITEM_NONE", ("MOVE_EARTHQUAKE", "MOVE_MUDDY_WATER", "MOVE_MUD_SHOT", "MOVE_PROTECT")),
        ("SPECIES_LUDICOLO", 61, "ITEM_NONE", ("MOVE_SURF", "MOVE_GIGA_DRAIN", "MOVE_ICE_BEAM", "MOVE_BULLET_SEED")),
        ("SPECIES_FORRETRESS", 62, "ITEM_NONE", ("MOVE_RAPID_SPIN", "MOVE_SPIKES", "MOVE_PROTECT", "MOVE_EXPLOSION")),
        ("SPECIES_GOLEM", 63, "ITEM_NONE", ("MOVE_EARTHQUAKE", "MOVE_ROCK_SLIDE", "MOVE_ROLLOUT", "MOVE_DEFENSE_CURL")),
        ("SPECIES_CROBAT", 64, "ITEM_NONE", ("MOVE_SLUDGE_BOMB", "MOVE_AERIAL_ACE", "MOVE_BITE", "MOVE_CONFUSE_RAY")),
        ("SPECIES_STEELIX", 68, "ITEM_METAL_COAT", ("MOVE_EARTHQUAKE", "MOVE_IRON_TAIL", "MOVE_CRUNCH", "MOVE_DRAGON_BREATH")),
    ],
    "sParty_LeaderMisty": [
        ("SPECIES_PSYDUCK", 20, "ITEM_NONE", ("MOVE_WATER_GUN", "MOVE_CONFUSION", "MOVE_DISABLE", "MOVE_SCRATCH")),
        ("SPECIES_POLIWAG", 21, "ITEM_NONE", ("MOVE_WATER_GUN", "MOVE_BUBBLE", "MOVE_DOUBLE_SLAP", "MOVE_HYPNOSIS")),
        ("SPECIES_STARYU", 23, "ITEM_NONE", ("MOVE_WATER_PULSE", "MOVE_SWIFT", "MOVE_RAPID_SPIN", "MOVE_PROTECT")),
        ("SPECIES_STARMIE", 26, "ITEM_MYSTIC_WATER", ("MOVE_WATER_PULSE", "MOVE_SWIFT", "MOVE_RAPID_SPIN", "MOVE_RECOVER")),
    ],
    "sParty_RSRuinManiac": [
        ("SPECIES_STARYU", 62, "ITEM_NONE", ("MOVE_SURF", "MOVE_ICE_BEAM", "MOVE_DOUBLE_EDGE", "MOVE_RECOVER")),
        ("SPECIES_TOGETIC", 61, "ITEM_NONE", ("MOVE_HIDDEN_POWER", "MOVE_METRONOME", "MOVE_SAFEGUARD", "MOVE_PROTECT")),
        ("SPECIES_POLITOED", 63, "ITEM_NONE", ("MOVE_SURF", "MOVE_BRICK_BREAK", "MOVE_MEGA_PUNCH", "MOVE_BOUNCE")),
        ("SPECIES_CORSOLA", 64, "ITEM_NONE", ("MOVE_SURF", "MOVE_SPIKE_CANNON", "MOVE_MIRROR_COAT", "MOVE_RECOVER")),
        ("SPECIES_STARMIE", 66, "ITEM_NONE", ("MOVE_SURF", "MOVE_PSYCHIC", "MOVE_PROTECT", "MOVE_RECOVER")),
        ("SPECIES_GYARADOS", 68, "ITEM_MYSTIC_WATER", ("MOVE_WATERFALL", "MOVE_EARTHQUAKE", "MOVE_RAIN_DANCE", "MOVE_PROTECT")),
    ],
    "sParty_LeaderLtSurge": [
        ("SPECIES_VOLTORB", 26, "ITEM_NONE", ("MOVE_SHOCK_WAVE", "MOVE_TACKLE", "MOVE_SONIC_BOOM", "MOVE_SCREECH")),
        ("SPECIES_PIKACHU", 25, "ITEM_NONE", ("MOVE_THUNDER_SHOCK", "MOVE_QUICK_ATTACK", "MOVE_DOUBLE_TEAM", "MOVE_THUNDER_WAVE")),
        ("SPECIES_MAGNEMITE", 24, "ITEM_NONE", ("MOVE_THUNDER_SHOCK", "MOVE_TACKLE", "MOVE_SUPERSONIC", "MOVE_METAL_SOUND")),
        ("SPECIES_RAICHU", 30, "ITEM_SITRUS_BERRY", ("MOVE_SHOCK_WAVE", "MOVE_MEGA_PUNCH", "MOVE_SLAM", "MOVE_THUNDER_WAVE")),
    ],
    "sParty_RSTuberF": [
        ("SPECIES_PIKACHU", 62, "ITEM_NONE", ("MOVE_THUNDERBOLT", "MOVE_IRON_TAIL", "MOVE_QUICK_ATTACK", "MOVE_DOUBLE_TEAM")),
        ("SPECIES_ELECTRODE", 64, "ITEM_NONE", ("MOVE_THUNDERBOLT", "MOVE_ROLLOUT", "MOVE_LIGHT_SCREEN", "MOVE_EXPLOSION")),
        ("SPECIES_MAGNETON", 65, "ITEM_NONE", ("MOVE_THUNDERBOLT", "MOVE_TRI_ATTACK", "MOVE_THUNDER_WAVE", "MOVE_METAL_SOUND")),
        ("SPECIES_MANECTRIC", 66, "ITEM_NONE", ("MOVE_THUNDERBOLT", "MOVE_BITE", "MOVE_THUNDER_WAVE", "MOVE_ROAR")),
        ("SPECIES_ELECTABUZZ", 67, "ITEM_NONE", ("MOVE_THUNDERBOLT", "MOVE_THUNDER_PUNCH", "MOVE_BRICK_BREAK", "MOVE_LIGHT_SCREEN")),
        ("SPECIES_RAICHU", 69, "ITEM_MAGNET", ("MOVE_THUNDER", "MOVE_THUNDERBOLT", "MOVE_MEGA_PUNCH", "MOVE_BODY_SLAM")),
    ],
    "sParty_LeaderErika": [
        ("SPECIES_VICTREEBEL", 31, "ITEM_NONE", ("MOVE_GIGA_DRAIN", "MOVE_ACID", "MOVE_POISON_POWDER", "MOVE_SLEEP_POWDER")),
        ("SPECIES_ODDISH", 29, "ITEM_NONE", ("MOVE_ABSORB", "MOVE_ACID", "MOVE_POISON_POWDER", "MOVE_STUN_SPORE")),
        ("SPECIES_TANGELA", 33, "ITEM_NONE", ("MOVE_GIGA_DRAIN", "MOVE_BIND", "MOVE_STUN_SPORE", "MOVE_GROWTH")),
        ("SPECIES_GLOOM", 35, "ITEM_SITRUS_BERRY", ("MOVE_PETAL_DANCE", "MOVE_ACID", "MOVE_POISON_POWDER", "MOVE_SLEEP_POWDER")),
    ],
    "sParty_RSTuberM": [
        ("SPECIES_TANGELA", 62, "ITEM_NONE", ("MOVE_GIGA_DRAIN", "MOVE_TICKLE", "MOVE_POISON_POWDER", "MOVE_SLEEP_POWDER")),
        ("SPECIES_JUMPLUFF", 63, "ITEM_NONE", ("MOVE_GIGA_DRAIN", "MOVE_LEECH_SEED", "MOVE_SLEEP_POWDER", "MOVE_SUNNY_DAY")),
        ("SPECIES_BELLOSSOM", 64, "ITEM_NONE", ("MOVE_SOLAR_BEAM", "MOVE_PETAL_DANCE", "MOVE_SYNTHESIS", "MOVE_SUNNY_DAY")),
        ("SPECIES_CRADILY", 65, "ITEM_NONE", ("MOVE_ROCK_SLIDE", "MOVE_GIGA_DRAIN", "MOVE_CONFUSE_RAY", "MOVE_RECOVER")),
        ("SPECIES_VICTREEBEL", 66, "ITEM_NONE", ("MOVE_GIGA_DRAIN", "MOVE_SLUDGE_BOMB", "MOVE_RAZOR_LEAF", "MOVE_POISON_POWDER")),
        ("SPECIES_VILEPLUME", 69, "ITEM_MIRACLE_SEED", ("MOVE_SOLAR_BEAM", "MOVE_SLUDGE_BOMB", "MOVE_SYNTHESIS", "MOVE_SUNNY_DAY")),
    ],
}

APPROVED_MOVE_EXCEPTIONS = {
    ("sParty_LeaderBrock", "SPECIES_GEODUDE", 15, "MOVE_REVENGE"),
    ("sParty_LeaderBrock", "SPECIES_VULPIX", 14, "MOVE_AGILITY"),
    ("sParty_LeaderBrock", "SPECIES_VULPIX", 14, "MOVE_FIRE_SPIN"),
    ("sParty_LeaderBrock", "SPECIES_ZUBAT", 13, "MOVE_WING_ATTACK"),
    ("sParty_LeaderMisty", "SPECIES_PSYDUCK", 20, "MOVE_WATER_GUN"),
    ("sParty_LeaderMisty", "SPECIES_STARYU", 23, "MOVE_SWIFT"),
    ("sParty_RSRuinManiac", "SPECIES_POLITOED", 63, "MOVE_BOUNCE"),

    ("sParty_LeaderErika", "SPECIES_GLOOM", 35, "MOVE_PETAL_DANCE"),
    ("sParty_LeaderErika", "SPECIES_TANGELA", 33, "MOVE_STUN_SPORE"),
    ("sParty_LeaderSabrina", "SPECIES_MR_MIME", 42, "MOVE_BATON_PASS"),
    ("sParty_RSLady", "SPECIES_MAGCARGO", 68, "MOVE_CURSE"),
    ("sParty_BossGiovanni", "SPECIES_RHYHORN", 30, "MOVE_SAND_ATTACK"),
    ("sParty_EliteFourBruno2", "SPECIES_HITMONLEE", 76, "MOVE_DETECT"),
}

CONST_RE = re.compile(r"^\s*#define\s+([A-Z][A-Z0-9_]+)\b", re.M)
MON_RE = re.compile(r"\{(.*?)\n\s*\}", re.S)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def constants(path: str, prefix: str) -> set[str]:
    return {m.group(1) for m in CONST_RE.finditer(read(path)) if m.group(1).startswith(prefix)}


def array_block(text: str, name: str) -> str:
    m = re.search(
        r"static const struct\s+\w+\s+" + re.escape(name) + r"\[\]\s*=\s*\{(.*?)\n\};",
        text,
        re.S,
    )
    if not m:
        raise AssertionError(f"trainer party array not found: {name}")
    return m.group(1)


def parse_level_up() -> dict[str, list[tuple[int, str]]]:
    learnsets = read("src/data/pokemon/level_up_learnsets.h")
    pointers = read("src/data/pokemon/level_up_learnset_pointers.h")

    by_array: dict[str, list[tuple[int, str]]] = {}
    for m in re.finditer(
        r"static const u16\s+(s[A-Za-z0-9_]+LevelUpLearnset)\[\]\s*=\s*\{(.*?)\n\};",
        learnsets,
        re.S,
    ):
        moves = [
            (int(level), move)
            for level, move in re.findall(r"LEVEL_UP_MOVE\((\d+),\s*(MOVE_[A-Z0-9_]+)\)", m.group(2))
        ]
        by_array[m.group(1)] = moves

    out: dict[str, list[tuple[int, str]]] = {}
    for species, arr in re.findall(
        r"\[(SPECIES_[A-Z0-9_]+)\]\s*=\s*(s[A-Za-z0-9_]+LevelUpLearnset)",
        pointers,
    ):
        out[species] = by_array.get(arr, [])
    return out


def parse_tmhm() -> dict[str, set[str]]:
    text = read("src/data/pokemon/tmhm_learnsets.h")
    starts = list(re.finditer(r"^\s*\[(SPECIES_[A-Z0-9_]+)\]\s*=\s*TMHM_LEARNSET\(", text, re.M))
    out: dict[str, set[str]] = defaultdict(set)

    for i, m in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else text.find("};", m.end())
        body = text[m.end():end]
        for machine in re.findall(r"TMHM\((?:TM|HM)\d+_([A-Z0-9_]+)\)", body):
            out[m.group(1)].add("MOVE_" + machine)
    return out


def parse_tutors() -> dict[str, set[str]]:
    text = read("src/data/pokemon/tutor_learnsets.h")
    starts = list(re.finditer(r"^\s*\[(SPECIES_[A-Z0-9_]+)\]\s*=", text, re.M))
    out: dict[str, set[str]] = defaultdict(set)

    for i, m in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else text.find("};", m.end())
        body = text[m.end():end]
        out[m.group(1)].update(re.findall(r"TUTOR\((MOVE_[A-Z0-9_]+)\)", body))
    return out


def parse_egg_moves() -> dict[str, set[str]]:
    text = read("src/data/pokemon/egg_moves.h")
    out: dict[str, set[str]] = defaultdict(set)
    for m in re.finditer(r"egg_moves\(([A-Z0-9_]+),(.*?)\),", text, re.S):
        out["SPECIES_" + m.group(1)].update(re.findall(r"MOVE_[A-Z0-9_]+", m.group(2)))
    return out


def parse_pre_evolutions() -> dict[str, set[str]]:
    text = read("src/data/pokemon/evolution.h")
    reverse: dict[str, set[str]] = defaultdict(set)
    current = None
    buf: list[str] = []

    def flush() -> None:
        nonlocal current, buf
        if current is None:
            return
        body = " ".join(buf)
        for target in re.findall(r"(SPECIES_[A-Z0-9_]+)\s*\}", body):
            reverse[target].add(current)
        current = None
        buf = []

    for line in text.splitlines():
        m = re.match(r"\s*\[(SPECIES_[A-Z0-9_]+)\]\s*=", line)
        if m:
            flush()
            current = m.group(1)
            buf = [line.split("=", 1)[1]]
        elif current is not None:
            buf.append(line)
        if current is not None and "}}," in line:
            flush()
    flush()
    return reverse


def lineage(species: str, reverse: dict[str, set[str]]) -> set[str]:
    seen: set[str] = set()
    stack = [species]
    while stack:
        cur = stack.pop()
        if cur in seen:
            continue
        seen.add(cur)
        stack.extend(reverse.get(cur, ()))
    return seen


def allowed_moves(
    species: str,
    level: int,
    level_up: dict[str, list[tuple[int, str]]],
    tmhm: dict[str, set[str]],
    tutors: dict[str, set[str]],
    eggs: dict[str, set[str]],
    reverse: dict[str, set[str]],
) -> set[str]:
    allowed: set[str] = set()
    for form in lineage(species, reverse):
        allowed.update(move for lvl, move in level_up.get(form, ()) if lvl <= level)
        allowed.update(tmhm.get(form, ()))
        allowed.update(tutors.get(form, ()))
        allowed.update(eggs.get(form, ()))
    return allowed


def validate_prima_spanish_localization() -> None:
    """A localized display name must not rewrite Lorelei's internal identity."""
    import json

    data = json.loads(read("src/data/trainers.json"))
    trainers = data.get("trainers", data)
    by_id = {trainer["id"]: trainer for trainer in trainers}
    for trainer_id in ("TRAINER_ELITE_FOUR_LORELEI", "TRAINER_ELITE_FOUR_LORELEI_2"):
        trainer = by_id[trainer_id]
        assert trainer["trainerName_spanish"] == "PRIMA", trainer_id
        assert trainer["trainerName_english"] == "LORELEI", trainer_id
        assert trainer["trainerName_italian"] == "LORELEI", trainer_id
        assert trainer["trainerName_german"] == "LORELEI", trainer_id
        assert trainer["trainerName_french"] == "OLGA", trainer_id

    localized = {
        "data/maps/PokemonLeague_LoreleisRoom/text_es.inc": 2,
        "data/maps/FourIsland_LoreleisHouse/text_es.inc": 2,
        "data/maps/FourIsland_IcefallCave_Back/text_es.inc": 4,
        "data/maps/FourIsland_Mart/text_es.inc": 1,
        "data/text/spanish/fame_checker.inc": 11,
    }
    for path, expected in localized.items():
        lines = read(path).splitlines()
        visible = [line for line in lines if line.lstrip().startswith(".string ")]
        assert sum(line.count("PRIMA") for line in visible) >= expected, path
        assert all("LORELEI" not in line for line in visible), path

    # The pre-existing name of One Island is unrelated to the character.
    assert 'ISLA PRIMA' in read("src/data/text/strings_1_es.h")


def main() -> None:
    validate_prima_spanish_localization()

    species_ids = constants("include/constants/species.h", "SPECIES_")
    move_ids = constants("include/constants/moves.h", "MOVE_")
    item_ids = constants("include/constants/items.h", "ITEM_")

    level_up = parse_level_up()
    tmhm = parse_tmhm()
    tutors = parse_tutors()
    eggs = parse_egg_moves()
    reverse = parse_pre_evolutions()

    trainer_text = read("src/data/trainer_parties.h")

    for party_name, expected in BROCK_EXPECTED.items():
        block = array_block(trainer_text, party_name)
        mons = MON_RE.findall(block)
        actual = []
        for mon in mons:
            species = re.search(r"\.species\s*=\s*(SPECIES_[A-Z0-9_]+)", mon).group(1)
            level = int(re.search(r"\.lvl\s*=\s*(\d+)", mon).group(1))
            item_match = re.search(r"\.heldItem\s*=\s*(ITEM_[A-Z0-9_]+)", mon)
            item = item_match.group(1) if item_match else "ITEM_NONE"
            moves_match = re.search(r"\.moves\s*=\s*\{([^}]*)\}", mon, re.S)
            moves = tuple(re.findall(r"MOVE_[A-Z0-9_]+", moves_match.group(1))) if moves_match else ()
            actual.append((species, level, item, moves))
        assert actual == expected, f"{party_name}: Brock roster drifted: {actual!r}"

    errors: list[str] = []
    used_exceptions: set[tuple[str, str, int, str]] = set()
    checked_mons = 0
    checked_moves = 0

    for party_name in PARTIES:
        block = array_block(trainer_text, party_name)
        mons = MON_RE.findall(block)
        if not mons:
            errors.append(f"{party_name}: no Pokemon entries parsed")
            continue

        for index, mon in enumerate(mons, 1):
            def field(pattern: str) -> str | None:
                m = re.search(pattern, mon)
                return m.group(1) if m else None

            species = field(r"\.species\s*=\s*(SPECIES_[A-Z0-9_]+)")
            level_s = field(r"\.lvl\s*=\s*(\d+)")
            iv_s = field(r"\.iv\s*=\s*(\d+)")
            item = field(r"\.heldItem\s*=\s*(ITEM_[A-Z0-9_]+)")

            if species is None or level_s is None:
                errors.append(f"{party_name}[{index}]: missing species or level")
                continue

            checked_mons += 1
            level = int(level_s)

            if species not in species_ids:
                errors.append(f"{party_name}[{index}]: unknown species {species}")
            if not 1 <= level <= 100:
                errors.append(f"{party_name}[{index}]: invalid level {level}")
            if iv_s is not None and not 0 <= int(iv_s) <= 255:
                errors.append(f"{party_name}[{index}]: invalid trainer IV byte {iv_s}")
            if item is not None and item not in item_ids:
                errors.append(f"{party_name}[{index}]: unknown held item {item}")

            moves_match = re.search(r"\.moves\s*=\s*\{([^}]*)\}", mon, re.S)
            if not moves_match:
                continue

            moves = re.findall(r"MOVE_[A-Z0-9_]+", moves_match.group(1))
            legal = allowed_moves(species, level, level_up, tmhm, tutors, eggs, reverse)

            for move in moves:
                checked_moves += 1
                if move not in move_ids:
                    errors.append(f"{party_name}[{index}] {species} Lv{level}: unknown move {move}")
                elif move != "MOVE_NONE" and move not in legal:
                    exception = (party_name, species, level, move)
                    if exception in APPROVED_MOVE_EXCEPTIONS:
                        used_exceptions.add(exception)
                    else:
                        errors.append(
                            f"{party_name}[{index}] {species} Lv{level}: {move} not learnable "
                            "by level/TM-HM/tutor/egg ancestry"
                        )

    missing_exceptions = APPROVED_MOVE_EXCEPTIONS - used_exceptions
    if missing_exceptions:
        for exception in sorted(missing_exceptions):
            errors.append(f"approved move exception not exercised exactly: {exception}")

    if errors:
        print(f"Full trainer legality audit FAILED with {len(errors)} issue(s):")
        for error in errors:
            print(" -", error)
        raise SystemExit(1)

    print(
        f"Full trainer legality audit PASS: {len(PARTIES)} parties, "
        f"{checked_mons} Pokemon, {checked_moves} custom moves."
    )


if __name__ == "__main__":
    main()
