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


def main() -> None:
    species_ids = constants("include/constants/species.h", "SPECIES_")
    move_ids = constants("include/constants/moves.h", "MOVE_")
    item_ids = constants("include/constants/items.h", "ITEM_")

    level_up = parse_level_up()
    tmhm = parse_tmhm()
    tutors = parse_tutors()
    eggs = parse_egg_moves()
    reverse = parse_pre_evolutions()

    trainer_text = read("src/data/trainer_parties.h")
    errors: list[str] = []
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
                    errors.append(
                        f"{party_name}[{index}] {species} Lv{level}: {move} not learnable "
                        "by level/TM-HM/tutor/egg ancestry"
                    )

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
