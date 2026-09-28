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

Previously approved rematch roster identity adjustments are already present: Brock/Vulpix, Misty/Luvdisc+Togetic, single Electrode for Surge, Erika's Gloom as anime-signature ace, Sabrina/Haunter, and Giovanni's approved roster.

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


## B3.4 — Manual rematch review history

> Historical review log. Any provisional statements below are superseded by the later
> global canon-depth corrections and the final transversal ace-audit result in this file.

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

Historical gate satisfied for checkpoint integration; final B3 release closure still requires current exact-head CI and runtime acceptance.


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

Togetic's review was subsequently closed; the approved rematch set is Psychic / Magical Leaf / Wish / Yawn.


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
- Vileplume remains at level 66.
- **Gloom becomes Erika's symbolic ace at level 69**, prioritizing anime identity over final-stage evolution.
- Only Gloom receives the exceptional IV boost (**.iv = 255**) to compensate for remaining unevolved; the rest of Erika's rematch keeps the existing IV tier.
- Gloom keeps the existing ace package: Solar Beam / Sludge Bomb / Sleep Powder / Sunny Day with Miracle Seed.

All other Erika rematch roster, levels, held items, trainer healing and movesets remain unchanged.

**Status: APPROVED — ace/IV criterion corrected.**


### Manual review 5/13 — Koga (in progress)

Approved:
- Venomoth 65: **Psychic / Silver Wind / Giga Drain / Sleep Powder**.
- Psychic replaces Psybeam.
- Giga Drain replaces Gust.
- Weezing becomes the symbolic ace at **level 71**.
- Crobat moves from level 71 to **level 68**.
- Overall level curve remains unchanged.

Weezing's fourth-move ambiguity was subsequently resolved: Sludge Bomb / Flamethrower / Toxic / Explosion.


Koga follow-up approved:
- Weezing 71: Sludge Bomb / Flamethrower / **Toxic** / Explosion.
- Toxic replaces Thunderbolt.
- Koga's Toxic distribution was subsequently resolved: Ariados also receives Toxic; no broader team-wide Toxic duplication was added.


Koga final follow-up approved:
- Ariados 64: Sludge Bomb / Psychic / Spider Web / **Toxic**.
- Toxic replaces Agility, giving Ariados a trap + poison role.
- No additional Toxic users added; Venomoth, Muk, Forretress and Crobat keep distinct roles.

**Status: APPROVED.**


### Manual review 6/13 — Sabrina

Approved adjustment:
- Mr. Mime 65: **Psychic** / Baton Pass / Barrier / Calm Mind.
- Psychic replaces Psybeam to bring its lone attack up to postgame strength.
- Historical note superseded: Kadabra 72 is now Sabrina's symbolic ace; Alakazam is retained at Lv66.
- All other Sabrina rematch roster, levels, IV tier, held items, trainer healing and movesets approved.

**Status: APPROVED.**


### Manual review 7/13 — Blaine

Reviewed roster, levels, effective IV tier, held items, trainer healing, AI and all six movesets.

No changes required. Magmar 73 remains the symbolic ace.

**Status: APPROVED AS-IS.**


### Manual review 8/13 — Giovanni

Approved final adjustment:
- Nidoking 71: Earthquake / Megahorn / **Flamethrower** / Ice Beam.
- Flamethrower replaces Thunderbolt by user approval.
- Rhydon 74 remains the combat ace; Persian remains Giovanni's visual/narrative signature.
- All other roster, levels, IV tier, held items, trainer healing and movesets approved.

**Status: APPROVED.**


### Manual review 9/13 — Lorelei

Approved adjustment:
- Piloswine 76: Earthquake / Rock Slide / Blizzard / **Double-Edge**.
- Double-Edge replaces Hail, removing weather redundancy with Dewgong and restoring the canonical FRLG rematch offensive identity.
- Lapras 79 remains the symbolic ace with Ice Beam / Surf / Thunderbolt / Confuse Ray.
- All other Lorelei rematch roster, levels, IV tier, held items, trainer healing and movesets approved.

**Status: APPROVED.**


### Manual review 10/13 — Bruno

Approved adjustment:
- Onix 75: Earthquake / Rock Slide / Iron Tail / **Screech**.
- Screech replaces Sandstorm to avoid damaging Bruno's Fighting core and better support his physical-pressure identity.
- Machamp 80 remains the symbolic ace.
- All other Bruno rematch roster, levels, IV tier, held items, trainer healing and movesets approved.

**Status: APPROVED.**


### Manual review 11/13 — Agatha

Approved adjustment:
- Arbok 79: **Sludge Bomb** / Earthquake / Rock Slide / Glare.
- Sludge Bomb replaces Poison Fang to restore postgame STAB power while retaining Glare-based control.
- Gengar 81 remains the symbolic ace.
- All other Agatha rematch roster, levels, IV tier, held items, trainer healing and movesets approved.

**Status: APPROVED.**


## B3.5 — Canon-depth re-audit

The user requested a finer canon pass before B3 closure, explicitly combining:
- original FRLG rematch identity;
- later core-game teams where they reveal trainer progression;
- Pokémon the Series ownership/signature details;
- regional progression across Kanto / Johto / Hoenn;
- Gen III legality and this hack's modern physical/special split;
- visual identity details such as canonical Shiny Pokémon.

This reopens the Elite Four review even where a previous manual pass had already approved the battle.

Current canon-depth findings:
- Lorelei: current team already fuses FRLG with her animated-series roster well; no Hoenn addition has a sufficiently direct canon basis.
- Bruno: Hariyama is canonically used in the HGSS rematch, but the previously proposed Onix -> Hariyama replacement is under reconsideration because Bruno's giant Onix is a specific animated-series capture and strong character identity. A better six-mon fusion may retain Onix and replace Steelix with Hariyama.
- Agatha: current Gengar / Crobat / Misdreavus / Arbok core already combines FRLG rematch, anime and later official identity well; no Hoenn addition currently has a strong direct basis.
- Lance: add Salamence from the later HGSS rematch as a sixth Pokémon. Lance's Gyarados should be treated as the canonical red/Shiny Gyarados from the Lake of Rage anime storyline if a narrowly scoped trainer-Shiny implementation is validated.

Do not close or merge B3 until this canon-depth re-audit is resolved and the final exact-head CI passes.


## B3.6 — Global canon-depth scope

User correction: the canon-depth audit is **global**, not limited to Elite Four rematches.

Required coverage before B3 closure:
- all eight Kanto Gym Leaders: first battle + rematch;
- Giovanni: Rocket Hideout + Silph + Viridian Gym + postgame rematch;
- Gary/Blue: all major story battles relevant to the approved progression, first Champion and Champion rematch;
- Elite Four: first League + strengthened rematch;
- cross-battle continuity (same owned Pokémon, evolutions, shiny identity, signature identity, regional progression, moves and visual staging).

Evidence hierarchy:
1. FireRed/LeafGreen canon for the base encounter;
2. later core-series teams when they demonstrate documented progression;
3. Pokémon the Series ownership/captures/evolutions/signature details;
4. other official continuities only when clearly labeled and when they improve identity without displacing stronger core/anime evidence;
5. Full-original additions only when explicitly identified as thematic rather than falsely described as canon.

Resolved design directions:
- **Bruno rematch:** Onix + Steelix retained; Hariyama replaces Hitmontop; Hitmonchan and Hitmonlee remain; Machamp remains ace.
- **Agatha rematch:** Sableye added as a sixth Pokémon and explicitly documented as a Full thematic Hoenn addition rather than canonical ownership.
- **Lance first League + rematch:** Gyarados is implemented as the same canonical Red/Shiny Gyarados in both encounters.
- **Lance rematch:** Salamence added as the later-game/Hoenn progression member; Dragonite remains ace.
- Trainer shiny implementation is narrowly scoped to Lance's Gyarados and does not modify save structures, link serialization, global shiny odds, wild encounters or unrelated trainer parties.

Important correction discovered by the global pass:
- Sabrina's animated-series Ghost partner is **Haunter** and is documented as not having evolved; the rematch has therefore been corrected from Gengar to Haunter.

B3 design work has been checkpoint-merged incrementally. Final B3 release closure still requires consolidated exact-head CI and final MyBoy acceptance.


### Global canon-depth correction — Sabrina

User-approved correction:
- Sabrina rematch changes **Gengar 69 -> Haunter 69**.
- Moves remain Shadow Ball / Thunderbolt / Hypnosis / Dream Eater with Spell Tag.
- Rationale: Pokémon the Series associates Sabrina specifically with Haunter, and the character does not need a forced final-stage evolution merely because this is a rematch. This mirrors other fidelity-first choices such as Brock retaining Marshtomp.
- Historical note superseded: Kadabra 72 is Sabrina's combat/symbolic ace; Alakazam is retained at Lv66.

**Status: APPLIED.**


### Global canon-depth correction — Erika ace criterion

User clarification:
- Ace selection and IV compensation are separate rules.
- Erika's ace must be **Gloom 69** because Gloom is her anime-symbolic Pokémon.
- Gloom alone is strengthened to **.iv = 255** because it remains an intermediate evolutionary stage.
- This IV exception must **not** be generalized to other aces.
- No other trainer IVs were changed by this correction.

**Status: APPLIED.**


### Global ace audit — Sabrina and Koga correction

User-approved ace rule:
- The ace is the trainer's strongest symbolic/character Pokémon, not merely the statistically strongest species.
- If the canonical/symbolic ace is intentionally kept at an intermediate evolutionary stage, it may receive targeted compensation through level, held item and maximum trainer IVs.
- This compensation is exceptional and must not be generalized to every ace.

Applied:
- **Sabrina first battle:** Alakazam moves to Lv45; **Kadabra becomes Lv47 ace**, .iv=255, Twisted Spoon.
- **Sabrina rematch:** Alakazam moves to Lv66; **Kadabra becomes Lv72 ace**, .iv=255, Twisted Spoon. Haunter remains Lv69 with Spell Tag.
- **Koga first battle:** Weezing moves to Lv41; **Golbat becomes Lv46 ace**, .iv=255, Sharp Beak.
- **Koga rematch:** Weezing moves to Lv68; **Crobat becomes Lv71 ace**, preserving normal rematch IV tier and Sharp Beak.
- Giovanni's Persian remains a visual/narrative signature rather than combat ace; no ace reassignment is made on that basis.

A dedicated validator now locks the approved symbolic-ace progression across:
- all eight Gym Leaders, first battle + rematch;
- Giovanni's story battles, Gym battle and rematch;
- Elite Four first League + strengthened League;
- Gary/Blue's Squirtle -> Wartortle -> Blastoise progression through Champion rematch.

**Status: APPLIED; global ace audit validator added.**


### Canon-depth implementation checkpoint — Lance / Bruno / Agatha

Applied after global canon re-audit:

**Lance**
- The Gyarados in both first League and strengthened League is now forced shiny at runtime.
- Scope is deliberately narrow: only TRAINER_ELITE_FOUR_LANCE and TRAINER_ELITE_FOUR_LANCE_2 when the generated species is Gyarados.
- The implementation changes only the generated enemy mon's OT ID to match its fixed personality, yielding shiny value 0. It does not change global shiny odds, saves, link serialization, wild encounters or unrelated trainers.
- Salamence Lv80 is added to the strengthened rematch with Lum Berry and Dragon Claw / Flamethrower / Rock Slide / Rest.
- Dragonite remains the ace.

**Bruno**
- Hitmontop leaves the strengthened rematch.
- Hariyama Lv78 enters with Sitrus Berry and Brick Break / Bulk Up / Earthquake / Rock Slide.
- Onix and Steelix are both retained.
- Hitmonchan and Hitmonlee are retained because they are stronger long-term character identifiers than Hitmontop.
- Machamp remains the ace.

**Agatha**
- Sableye Lv78 is added as the sixth member with Focus Band and Shadow Ball / Faint Attack / Fake Out / Confuse Ray.
- Sableye is explicitly a Full thematic Hoenn addition, not claimed as canonical ownership.
- Gengar remains the ace.

Validators updated:
- exact League roster validator;
- global ace/canon identity validator;
- audited trainer-party blob lock.

**Status: APPLIED.**


### Global symbolic-ace audit — transversal result

The ace audit is now applied consistently across story progression and rematches.

Approved interpretation:
- ace means the trainer's principal combat identity, not automatically the highest-BST species or most visually famous companion;
- anime identity is prioritized when it gives a clearer character-specific signature;
- core-series progression is used to evolve that identity where appropriate;
- an intermediate-stage ace may receive targeted IV/item compensation;
- Giovanni is a special case: Persian is a narrative/visual signature but not automatically the combat ace.

Current accepted ace continuity:
- Brock: Onix -> Steelix.
- Misty: Starmie -> Starmie.
- Lt. Surge: Raichu -> Raichu.
- Erika: Gloom -> Gloom (max-IV intermediate-stage exception).
- Koga: Golbat -> Crobat (Golbat receives the intermediate-stage exception).
- Sabrina: Kadabra -> Kadabra (max-IV + Twisted Spoon intermediate-stage exception).
- Blaine: Magmar -> Magmar.
- Giovanni: Rocket Hideout Kangaskhan; Silph Nidoqueen; Viridian Gym Rhydon as trainer ace alongside narrative Mewtwo; postgame Rhydon. Persian remains signature/motif, not forced into ace status.
- Lorelei: Lapras -> Lapras.
- Bruno: Machamp -> Machamp.
- Agatha: Gengar -> Gengar.
- Lance: Dragonite -> Dragonite; Gyarados is the same canonical Red/Shiny Gyarados in both League encounters.
- Gary/Blue: Squirtle -> Wartortle -> Blastoise throughout the rival progression, first Champion and Champion rematch.

No additional ace reassignment is currently justified by the global evidence hierarchy.

**Status: ACE AUDIT CLOSED pending CI/runtime validation, not design changes.**


### Manual review 13/13 — Gary/Blue Champion rematch (REOPENED FOR STEPWISE MOVE REVIEW)

Reviewed exact roster, level curve, IV tier, held items, movesets, ace identity, anime ownership and FRLG continuity.

Approved roster:
- Nidoqueen 80 — Soft Sand — Earthquake / Superpower / Ice Beam / Thunderbolt.
- Magmar 80 — Charcoal — Flamethrower / Fire Blast / Brick Break / Confuse Ray.
- Golem 81 — Hard Stone — Earthquake / Rock Slide / Double-Edge / Explosion.
- Scizor 82 — Metal Coat — Swords Dance / Steel Wing / Aerial Ace / Quick Attack.
- Arcanine 83 — no held item — Flamethrower / ExtremeSpeed / Iron Tail / Bite.
- **Blastoise 85 ★** — Leftovers — Hydro Pump / Ice Beam / Earthquake / Rain Dance.

Canon-depth rationale:
- The six-species roster is an exceptionally close reconstruction of Gary's Silver Conference full-battle selection: Nidoqueen / Magmar / Golem / Scizor / Arcanine / Blastoise.
- Blastoise remains the unquestioned ace: it is Gary's first partner and is explicitly treated as his strongest/main battle Pokémon in the animated series.
- Blastoise's Full moveset exactly matches Blue's FRLG strengthened Champion-rematch moveset, while Hydro Pump is also a repeatedly documented move of Gary's Blastoise in animation. This is therefore the strongest game/anime hybrid point in the entire rival design.
- Magmar preserves both of its documented animated-series attacks (Flamethrower and Fire Blast) while retaining two gameplay-support moves.
- Scizor preserves Steel Wing and Quick Attack from its animated-series set while Swords Dance and Aerial Ace preserve rematch pressure and coverage.
- Golem's documented anime attacks (Magnitude / Rollout) were not forced over Earthquake / Rock Slide because the existing set is the stronger postgame realization of the same Ground/Rock combat identity and avoids lowering trainer AI quality.
- Nidoqueen's anime moves are deliberately not copied wholesale because doing so would materially reduce postgame coverage; ownership/roster identity is prioritized while its Full set remains a high-end mixed attacker.
- Arcanine keeps Flamethrower from animation plus strong Blue/FRLG-style coverage and priority identity.
- Fully evolved ace rule applies: Blastoise does not receive the intermediate-stage .iv=255 exception. Its .iv=247 tier remains intentional.

**Status: REOPENED.**

The roster/ace identity remains approved, but the moveset/item pass must be repeated
Pokémon-by-Pokémon with the user, explicitly comparing:
1. original FRLG Champion rematch design;
2. Gary's animated-series demonstrated moves where applicable;
3. the current Full moveset;
4. Gen III legality + modern physical/special split;
5. whether a concrete adjustment improves identity or challenge.

Do not treat Gary as moveset-closed until all six slots are reviewed in that format.

Note on numbering: 13/13 is only the historical manual rematch sequence. It is followed
by the transversal progression/canon audit and therefore is not the end of B3 review work.


### Gary/Blue rematch stepwise move review — 1/6 Nidoqueen

User-approved adjustment:
- **Nidoqueen 80:** Earthquake / **Hyper Beam** / Ice Beam / Thunderbolt.
- Hyper Beam replaces Superpower.
- Soft Sand remains.
- Rationale: Hyper Beam is directly demonstrated by Gary's Nidoqueen in the animated series, while Earthquake preserves the primary physical Ground role and Ice Beam + Thunderbolt preserve the high-end mixed coverage expected of the Champion rematch.
- This intentionally sacrifices some raw competitive efficiency from Superpower in exchange for stronger character identity without materially weakening the overall set.

**Status: APPROVED AND APPLIED.**


### Gary/Blue rematch stepwise move review — 2/6 Magmar

User-approved adjustment:
- **Magmar 80:** Flamethrower / Fire Blast / Brick Break / **Psychic**.
- Psychic replaces Confuse Ray.
- Charcoal remains.
- Flamethrower + Fire Blast preserve Gary's directly demonstrated anime identity.
- Psychic improves Champion-rematch offensive coverage and makes better use of Magmar's special attacking role than the removed passive confusion slot.

**Status: APPROVED AND APPLIED.**


### Gary/Blue rematch stepwise move review — 3/6 Golem

User approved Golem 81 unchanged:
- Earthquake / Rock Slide / Double-Edge / Explosion.
- Hard Stone remains.
- Anime Magnitude / Rollout were reviewed but rejected because they would materially reduce Champion-rematch consistency and power versus the current Ground/Rock realization.

**Status: APPROVED AS-IS.**

### Gary/Blue rematch stepwise move review — 4/6 Scizor

User approved Scizor 82 unchanged:
- Swords Dance / Steel Wing / Aerial Ace / Quick Attack.
- Metal Coat remains.
- Steel Wing + Quick Attack preserve direct Gary anime identity; Swords Dance + Aerial Ace provide stronger Gen III postgame function without redundant Metal Claw/Swift.

**Status: APPROVED AS-IS.**


### Gary/Blue rematch stepwise move review — 5/6 Arcanine

User explicitly preferred the current set over the proposed Aerial Ace substitution.

Approved unchanged:
- **Arcanine 83:** Flamethrower / ExtremeSpeed / Iron Tail / Bite.
- No held item.
- Bite is retained for Dark coverage and team role differentiation, despite Aerial Ace matching the original FRLG rematch more closely.

**Status: APPROVED AS-IS.**


### Gary/Blue rematch stepwise move review — 6/6 Blastoise

User approved Blastoise 85 ace unchanged:
- Hydro Pump / Ice Beam / Earthquake / Rain Dance.
- Leftovers remains.
- The set is retained because it exactly matches Blue's strengthened FRLG rematch moveset while Hydro Pump also preserves direct Gary-anime identity.
- As a fully evolved ace, Blastoise keeps the normal high Champion IV tier rather than receiving the intermediate-stage .iv=255 exception.

**Status: APPROVED AS-IS.**

### Gary/Blue rematch stepwise move review — FINAL

Approved final rematch:
- Nidoqueen 80: Earthquake / Hyper Beam / Ice Beam / Thunderbolt.
- Magmar 80: Flamethrower / Fire Blast / Brick Break / Psychic.
- Golem 81: Earthquake / Rock Slide / Double-Edge / Explosion.
- Scizor 82: Swords Dance / Steel Wing / Aerial Ace / Quick Attack.
- Arcanine 83: Flamethrower / ExtremeSpeed / Iron Tail / Bite.
- Blastoise 85 ★: Hydro Pump / Ice Beam / Earthquake / Rain Dance.

Gary/Blue rematch move review is now complete.

**Status: 6/6 CLOSED.**


### Global ace transversal review — Gloom

User approved Erika's ace progression unchanged after dedicated moveset review.

First battle — Gloom 35 ★:
- Petal Dance / Sleep Powder / Moonlight / Acid.
- Sitrus Berry.
- .iv = 255.

Rematch — Gloom 69 ★:
- Solar Beam / Sludge Bomb / Sleep Powder / Sunny Day.
- Miracle Seed.
- .iv = 255.

Rationale:
- first battle preserves Yellow-era Gloom identity while replacing redundant secondary status with Moonlight sustain;
- rematch uses a distinct sun-enabled ace pattern with dual STAB and Sleep Powder control;
- no further move changes are required.

**Status: APPROVED AS-IS.**


### Global ace transversal review — Golbat 46 ★

User-approved adjustment:
- **Golbat 46:** Wing Attack / Bite / Confuse Ray / **Screech**.
- Screech replaces Toxic.
- Sharp Beak remains.
- .iv = 255 remains.
- Rationale: Wing Attack + Screech are directly demonstrated by Koga's Golbat in the animated series; Confuse Ray preserves established Koga/Golbat control identity; removing Toxic avoids four-way Toxic redundancy in the first Koga battle while keeping poison pressure elsewhere on the team.

**Status: APPROVED AND APPLIED.**


### Global ace transversal review — Sabrina Kadabra

User approved both Kadabra ace sets unchanged.

First battle — Kadabra 47 ★:
- Psychic / Calm Mind / Recover / Reflect.
- Twisted Spoon.
- .iv = 255.

Rematch — Kadabra 72 ★:
- Psychic / Calm Mind / Recover / Reflect.
- Twisted Spoon.
- .iv = 255.

Rationale:
- Psychic + Recover preserve direct Sabrina/Kadabra animated-series identity;
- Calm Mind preserves FRLG Sabrina identity and her signature TM;
- Reflect is retained over Future Sight because it materially improves Kadabra's physical survivability and produces a stronger ace without sacrificing the core canon identity;
- repeating the set is intentional: the rematch represents the same symbolic partner at a much higher level rather than a different tactical identity.

**Status: APPROVED AS-IS.**

### Intermediate-stage ace audit — closure

Special intermediate-stage ace compensation is now closed:
- Erika: Gloom 35 / 69 — .iv=255.
- Koga: Golbat 46 — .iv=255 + Sharp Beak; evolves to Crobat 71 with normal rematch IV tier.
- Sabrina: Kadabra 47 / 72 — .iv=255 + Twisted Spoon.

Ace status does not globally imply max IV; these are targeted fidelity/balance exceptions.

**Status: CLOSED.**


### Global ace transversal review — Brock

User approved Brock's ace progression unchanged.

First battle — Onix 17 ★:
- Rock Tomb / Rock Smash / Bind / Screech.
- Oran Berry.
- .iv = 50.

Rematch — Steelix 66 ★:
- Earthquake / Rock Slide / Iron Tail / Crunch.
- Leftovers.
- .iv = 214.

Rationale:
- Bind preserves direct anime identity for Brock's Onix;
- Steelix is the evolved continuation of Brock's signature Onix;
- Iron Tail preserves evolved anime identity while the remaining postgame moves provide appropriate physical pressure and coverage.

**Status: APPROVED AS-IS.**


### Global ace transversal review — Misty

User approved Misty's ace progression unchanged.

First battle — Starmie 26 ★:
- Water Pulse / Swift / Rapid Spin / Recover.
- Sitrus Berry.
- .iv = 83.

Rematch — Starmie 67 ★:
- Surf / Psychic / Thunderbolt / Recover.
- Twisted Spoon.
- .iv = 214.

Rationale:
- first battle preserves the original FRLG Starmie set;
- rematch upgrades Water Pulse -> Surf, adds Psychic as second STAB and Thunderbolt as advanced coverage, while Recover remains the continuity anchor.

**Status: APPROVED AS-IS.**


### Global ace transversal review — Lt. Surge

User approved Lt. Surge's ace progression unchanged.

First battle — Raichu 30 ★:
- Shock Wave / Mega Punch / Thunder Wave / Quick Attack.
- Sitrus Berry.
- .iv = 99.

Rematch — Raichu 69 ★:
- Thunderbolt / Brick Break / Iron Tail / Thunder Wave.
- Leftovers.
- .iv = 214.

Rationale:
- Shock Wave -> Thunderbolt is the natural STAB progression;
- Thunder Wave remains the continuity/control anchor;
- early physical pressure from Mega Punch/Quick Attack evolves into stronger Brick Break/Iron Tail coverage for postgame.

**Status: APPROVED AS-IS.**
