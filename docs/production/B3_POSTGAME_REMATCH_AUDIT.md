# B3 Postgame / Rematch Audit

**Date:** 2026-09-26
**Branch:** `feature/b3-postgame-rematch-identity`

## B3.1 — Unlock and identity

- All eight Gym Leader rematches unlock from `FLAG_SYS_GAME_CLEAR` (first Hall of Fame), not National Dex.
- Giovanni's postgame Gym reappearance follows the same rule.
- Rematches remain repeatable through the existing dedicated trainer-flag reset.
- Each leader now has a unique offer / intro / defeat / post-battle dialogue set.
- `validate_b3_rematch_identity.py` gates these requirements.

## Rematch progression snapshot

Gym rematch ace progression:
- Brock 66
- Misty 67
- Lt. Surge 69
- Erika 69
- Koga 71
- Sabrina 72
- Blaine 73
- Giovanni 74

This forms an optional bridge from the first Champion (ace 69) into the Network-Machine-gated strengthened League (Lorelei ace 79 through Champion ace 85), without forcing global EXP inflation.

Previously approved rematch roster identity adjustments are already present: Brock/Vulpix, Misty/Luvdisc+Togetic, single Electrode for Surge, second Vileplume for Erika, Sabrina/Gengar, and Giovanni's approved roster.

## B3.2 — League rematch refinement

Applied the previously approved Lorelei rematch amendment:
- Lapras 79: Ice Beam / Surf / Thunderbolt / **Confuse Ray**
- Body Slam is removed from the rematch set.

This restores Lapras's control identity while retaining the stronger rematch coverage package.


## B3.3 — Postgame training bridge

To avoid global EXP inflation or mandatory grinding, six existing high-value final VS Seeker tiers gated by the completed Network Machine were strengthened into a curated training bridge:

- Crush Kin Mik & Kia: 64 / 64
- Cooltrainer Leroy: 64 / 65 / 64 / 65 / 67
- Pokémon Ranger Jackson: 65 / 66 / 67
- Cooltrainer Michelle: 65 / 65 / 66 / 67 / 69
- Pokémon Ranger Katelyn: 68
- Cool Couple Lex & Nya: 70 / 70

These remain optional rematches and preserve normal VS Seeker progression logic. Their final tiers sit below the strengthened League opener (Lorelei 74–79) and complement the Gym rematch ace progression (66–74).

The strengthened League remains gated by `FLAG_SYS_CAN_LINK_WITH_RS`, i.e. completed Ruby/Sapphire Network Machine progression.

`tools/validate_b3_postgame_progression.py` now checks:
- Hall-of-Fame vs Network VS Seeker tier gating;
- exact selected final-tier placement and levels;
- strengthened League Network-Machine gating;
- bridge ceiling below the strengthened League.


## B3 closure gate

All B3 scope items are implemented and statically validated:

- Gym rematches unlock after first Hall of Fame / game clear.
- No National Dex or capture quota gates Gym rematches.
- All eight Gym Leader rematches remain repeatable.
- All eight leaders have unique rematch dialogue sets.
- Approved rematch roster identity changes are preserved.
- Lorelei rematch Lapras uses Confuse Ray as approved.
- Six optional high-value VS Seeker final tiers provide a level 64-70 training bridge.
- Strengthened League remains gated by completed Network Machine progression.
- No global EXP formula change was introduced.

Validation checkpoint before documentation-only closure:
- exact gameplay HEAD: `8a73aedb0f36d8b26a8956fd04e280139275cfa9`
- Full Gameplay Core run: `36282030839`
- result: **SUCCESS**


## B3.4 — Manual rematch review pending

The prior closure candidate was premature. Static/progression validation does not replace the manual design pass used for the first-cycle boss battles.

Before B3 can close, review the postgame boss rematches one by one with the user, covering:
- roster identity;
- levels and progression;
- IV tier;
- held items and trainer healing;
- moveset coherence and legality;
- challenge level versus adjacent bosses;
- anime/canon/game identity.

Required sequence:
1. Brock rematch
2. Misty rematch
3. Lt. Surge rematch
4. Erika rematch
5. Koga rematch
6. Sabrina rematch
7. Blaine rematch
8. Giovanni rematch
9. Lorelei rematch
10. Bruno rematch
11. Agatha rematch
12. Lance rematch
13. Gary/Blue Champion rematch

B3 must not merge until this manual pass and a final transversal rematch-progression audit are complete.


### Manual review 1/13 — Brock

**Status: APPROVED AS-IS.**

Reviewed roster, levels, effective IV tier, held items, trainer healing, AI and all six movesets.

User explicitly chose to retain **Rapid Spin on Forretress** for Pokémon identity rather than replace it with Earthquake. No gameplay data changes are required.

Approved Brock rematch remains:
Vulpix 60 / Crobat 61 / Forretress 62 / Ludicolo 63 / Marshtomp 64 / Steelix 66.


### Manual review 2/13 — Misty (in progress)

Approved identity correction:
- **Starmie is Misty's rematch ace at level 67.**
- Gyarados moves from level 67 to level 65.
- Overall level curve is unchanged; only the symbolic ace ordering changes.

Togetic moveset remains under manual review before Misty is closed.


Misty manual review closure:
- Starmie 67 is the symbolic ace; Gyarados is 65.
- Togetic: Psychic / Magical Leaf / Wish / Yawn.
- Psychic replaces Ancient Power by user approval.
- Roster, IV tier, held items, trainer healing and all other movesets approved.

**Status: APPROVED.**


### Manual review 3/13 — Lt. Surge

Approved adjustment:
- Electrode: Thunderbolt / **Taunt** / Mirror Coat / Explosion.
- Taunt replaces Light Screen to remove anti-synergy with Mirror Coat and reduce overlap with Electabuzz's Light Screen.
- Magneton, Electabuzz and Raichu remain unchanged.
- Raichu 69 remains the symbolic ace.

**Status: APPROVED.**


### Manual review 4/13 — Erika

Approved adjustment:
- Bellossom 64: **Synthesis** / Petal Dance / Sunny Day / Solar Beam.
- Synthesis replaces Giga Drain to reduce Grass-attack redundancy and strengthen Bellossom's sun-sustain identity.
- Both Vileplume remain; Vileplume 69 remains the symbolic ace.

All other Erika rematch roster, levels, IV tier, held items, trainer healing and movesets approved.

**Status: APPROVED.**
