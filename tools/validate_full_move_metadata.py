#!/usr/bin/env python3
"""Lock exhaustive Gen I-III move category/contact metadata used by Full.

Canonical vectors audited 2026-09-20 against Pokémon Showdown data/moves.ts
blob b854cfba94211266a5251c00036158269cf47fe0. Move IDs are Gen III IDs
1..354, so the gate is independent of aliases/spelling.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORY_VECTOR = "PPPPPPPPPPPPSTPSPTPPPPPPPPPTPPPPPPPPPPTPPPTPTTTTSTSSSTSSSSSSSSSPPPPPPPSSTTPSTTTSTSSSSTSPPPPTSSTTTPPTSTTTTTTTTTTTTTTTPTTPPPSSPSPPSPPPTTTPTSTPPTPTSPTTSTTPPPPTPPTTSPPTPTPPTTTPSTPTSTPTSTPTPTTSSSTSTTTSTPTPTSTTPPTTPPPTTTTPPPTTPPPPSTTPPTPPPTTTSPSTTPSTPSSSPSPPSTSTSTTTTTPPPTTTTTTTTTTPTTPPTPPSTTTTTPPPTTSSTTPTPPTSPPSSPPSTTSSTPSTTTTSSPSPPSSPPPTTTPSTPSPPPSTTPTPSSSS"  # P=physical, S=special, T=status
CONTACT_IDS = {1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 15, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 44, 64, 65, 66, 67, 68, 69, 70, 80, 91, 98, 99, 117, 122, 127, 128, 130, 132, 136, 141, 146, 152, 154, 158, 162, 163, 165, 167, 168, 172, 175, 179, 183, 185, 200, 205, 206, 209, 210, 211, 216, 218, 223, 224, 228, 229, 231, 232, 233, 238, 242, 245, 249, 252, 263, 264, 265, 276, 279, 280, 282, 283, 291, 292, 299, 301, 302, 305, 306, 309, 310, 325, 327, 332, 337, 340, 342, 343, 344, 348}


def main():
    moves_h = (ROOT / "include/constants/moves.h").read_text(encoding="utf-8")
    battle = (ROOT / "src/data/battle_moves.h").read_text(encoding="utf-8")

    by_id = {}
    for name, number in re.findall(r"^#define\s+(MOVE_[A-Z0-9_]+)\s+(\d+)", moves_h, re.MULTILINE):
        number = int(number)
        if 1 <= number <= 354:
            by_id[number] = name
    assert len(by_id) == 354, f"expected 354 Gen III move IDs, got {len(by_id)}"

    blocks = {}
    for match in re.finditer(
        r"\[(MOVE_[A-Z0-9_]+)\]\s*=\s*\{(.*?)(?=\n\s*\[MOVE_|\n\};)",
        battle,
        re.DOTALL,
    ):
        blocks[match.group(1)] = match.group(2)

    symbols = {"PHYSICAL": "P", "SPECIAL": "S", "STATUS": "T"}
    actual_categories = []
    actual_contacts = set()
    for move_id in range(1, 355):
        name = by_id[move_id]
        assert name in blocks, f"battle metadata missing for {name} (ID {move_id})"
        body = blocks[name]
        match = re.search(r"\.category\s*=\s*MOVE_CATEGORY_(PHYSICAL|SPECIAL|STATUS)", body)
        assert match, f"category missing for {name}"
        actual_categories.append(symbols[match.group(1)])
        if "FLAG_MAKES_CONTACT" in body:
            actual_contacts.add(move_id)

    actual_vector = "".join(actual_categories)
    assert len(CATEGORY_VECTOR) == 354
    assert actual_vector == CATEGORY_VECTOR, (
        "move-category drift at IDs: "
        + ", ".join(
            str(i + 1)
            for i, (got, want) in enumerate(zip(actual_vector, CATEGORY_VECTOR))
            if got != want
        )
    )
    assert actual_contacts == CONTACT_IDS, (
        f"contact metadata drift: added={sorted(actual_contacts - CONTACT_IDS)}, "
        f"removed={sorted(CONTACT_IDS - actual_contacts)}"
    )

    print(
        "Battle metadata PASS: all 354 Gen III move categories and contact flags "
        "match the audited modern vectors."
    )


if __name__ == "__main__":
    main()
