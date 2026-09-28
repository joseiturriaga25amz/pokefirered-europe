#!/usr/bin/env python3
"""Validate B3 postgame progression bridge and strengthened League gating."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

FINAL_TIERS = {
    "TRAINER_CRUSH_KIN_MIK_KIA_3": ("sParty_CrushKinMikKia3", (64, 64)),
    "TRAINER_COOLTRAINER_LEROY_2": ("sParty_CooltrainerLeroy2", (64, 65, 64, 65, 67)),
    "TRAINER_PKMN_RANGER_JACKSON_2": ("sParty_PkmnRangerJackson2", (65, 66, 67)),
    "TRAINER_COOLTRAINER_MICHELLE_2": ("sParty_CooltrainerMichelle2", (65, 65, 66, 67, 69)),
    "TRAINER_PKMN_RANGER_KATELYN_2": ("sParty_PkmnRangerKatelyn2", (68,)),
    "TRAINER_COOL_COUPLE_LEX_NYA_2": ("sParty_CoolCoupleLexNya2", (70, 70)),
}

def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")

def party_levels(text: str, name: str) -> tuple[int, ...]:
    m = re.search(
        rf"static const struct\s+\w+\s+{re.escape(name)}\[\]\s*=\s*\{{(.*?)\n\}};",
        text,
        re.S,
    )
    assert m, name
    return tuple(int(x) for x in re.findall(r"\.lvl\s*=\s*(\d+)", m.group(1)))

def main() -> None:
    vs = read("src/vs_seeker.c")
    parties = read("src/data/trainer_parties.h")
    lorelei = read("data/maps/PokemonLeague_LoreleisRoom/scripts.inc")
    indigo = read("data/maps/IndigoPlateau_PokemonCenter_1F/scripts.inc")

    # Story progression: post-Hall-of-Fame tier at index 4; Network Machine tier at index 5.
    assert re.search(
        r"case 4:.*?FLAG_SYS_GAME_CLEAR.*?case 5:.*?FLAG_SYS_CAN_LINK_WITH_RS",
        vs,
        re.S,
    ), "VS Seeker progression gates drifted"

    for trainer, (party_name, expected_levels) in FINAL_TIERS.items():
        # Each selected trainer must actually occupy a Network-era final rematch slot.
        assert re.search(
            rf"\{{\s*\{{[^}}]*\b{re.escape(trainer)}\b\s*\}}\s*,\s*MAP\(",
            vs,
            re.S,
        ), f"{trainer}: not in VS Seeker table"
        entry = re.search(
            rf"\{{\s*\{{([^}}]*\b{re.escape(trainer)}\b[^}}]*)\}}\s*,\s*MAP\(",
            vs,
            re.S,
        )
        ids = [x.strip() for x in entry.group(1).split(",")]
        assert len(ids) >= 6 and ids[5] == trainer, f"{trainer}: must be Network final tier"
        assert party_levels(parties, party_name) == expected_levels, (
            trainer,
            party_levels(parties, party_name),
            expected_levels,
        )

    # The strengthened League remains a later Network-Machine tier.
    assert "call_if_set FLAG_SYS_CAN_LINK_WITH_RS, PokemonLeague_LoreleisRoom_EventScript_Rematch" in lorelei
    assert "call_if_unset FLAG_SYS_CAN_LINK_WITH_RS, PokemonLeague_LoreleisRoom_EventScript_Battle" in lorelei
    assert "goto_if_set FLAG_SYS_CAN_LINK_WITH_RS, EventScript_Return" in indigo
    assert "goto_if_set FLAG_SYS_CAN_LINK_WITH_RS, IndigoPlateau_PokemonCenter_1F_EventScript_SeviiIslandComplete" in indigo

    # Curated bridge stays below the strengthened League opener (Lorelei 74-79).
    maxima = [max(levels) for _, levels in FINAL_TIERS.values()]
    assert min(maxima) >= 64
    assert max(maxima) <= 70

    print(
        "B3 postgame progression PASS: six high-value Network VS Seeker finals "
        "bridge levels 64-70, while strengthened League remains Network-gated."
    )

if __name__ == "__main__":
    main()
