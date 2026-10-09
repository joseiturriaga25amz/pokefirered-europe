# Full v1.0 — Approved Polish Implementation Matrix

**Authority:** A-005 and A-006 in `DECISION_AMENDMENTS.md`  
**Baseline:** `feature/full-gameplay-core` after follower research documentation  
**Rule:** this matrix prepares the production polish independently from `prototype/follower-runtime`.

## P-01 Legendary narrative V2

### Birds
Keep Articuno, Zapdos and Moltres in their original Kanto exploration locations. Preserve the existing respawn-after-KO safety logic.

### Mystic Ticket / Navel Rock
Replace the current Celio-owned Full postgame ticket distribution.

Required behavior:
- eligibility uses all three Kanto birds **seen**, not captured;
- the narrative hook is maritime/investigative, not Celio handing out unrelated event tickets;
- Mystic Ticket remains the original Gen III item ID;
- Navel Rock shipping flag/destination remain canonical;
- Lugia is the first Navel Rock legendary available;
- Ho-Oh is a later capstone of the roaming-beast sequence, not simply co-available with Lugia.

Primary audit targets:
- `data/maps/OneIsland_PokemonCenter_1F/scripts.inc` — remove Full ticket ownership from Celio;
- ferry/harbor scripts — move maritime clue/reward path here;
- `src/roamer.c` and beast progression flags/vars — Ho-Oh capstone eligibility;
- Navel Rock scripts — gate Ho-Oh independently from Lugia;
- Spanish text files for every touched map.

### Deoxys / Aurora Ticket
Move Aurora progression out of Celio:
- autonomous Pewter Museum / space-anomaly investigation;
- scientist gives Aurora Ticket after the approved investigation;
- preserve original Aurora Ticket ID and Birth Island ship destination.

Primary targets:
- Pewter Museum map scripts/text;
- ferry/harbor unlock;
- Birth Island battle script remains canonical destination.

### Celebi
Keep Berry Forest / nature investigation self-contained.
Do not gate Celebi on capturing the three roaming beasts.

### Mewtwo
Keep Cerulean Cave post-Network and current respawn safety.

## P-02 Mew visual presentation

Current scripts already implement the Mew quest state and final battle, but presentation is largely cry/text-driven.

Required V2:
- preserve original Mansion diary history;
- add visible Mew overworld appearances during the quest;
- use existing `OBJ_EVENT_GFX_MEW`;
- final Mew must be visibly present/interactable immediately before battle;
- no new species ID, no SaveBlock growth, no change to battle identity.

Primary targets:
- `data/maps/PokemonMansion_1F/map.json`, scripts/text;
- Mansion 2F/3F/B1F maps/scripts/text;
- existing `VAR_FULL_MEW_QUEST`, `FLAG_FULL_MEW_CAUGHT`, `FLAG_FULL_MEW_KO_PENDING`.

## P-03 Gym leader rematch dialogue identity

Keep already-approved rematch teams, levels, repeatability and battle mechanics.

Add unique per-leader:
1. rematch offer;
2. battle opening;
3. defeat line;
4. post-battle line.

Targets:
- all eight `data/maps/*City_Gym/scripts.inc`;
- corresponding Spanish text files;
- trainer data only if a leader-specific battle text pointer requires it.

No generic shared Full-rematch dialogue should remain visible for the eight leaders.

## P-04 Specialty Poké Ball distribution

Make these obtainable through natural shops:
- Net Ball;
- Nest Ball;
- Repeat Ball;
- Timer Ball;
- Luxury Ball;
- Dive Ball;
- Premier Ball.

Constraints:
- do not sell Master Ball or Safari Ball;
- no new item IDs;
- Dive Ball mechanics remain unchanged in FireRed;
- progression should stage availability rather than expose every Ball immediately;
- at least one late/postgame Sevii shop provides a complete legitimate specialty-Ball stock;
- prices must remain coherent relative to Great/Ultra Ball and Full's economy.

Implementation strategy:
- use existing mart inventory script structures;
- prefer Kanto thematic placement plus a Sevii consolidated postgame stock;
- Premier Ball may be sold directly if bonus-on-10-Poké-Balls is intentionally not implemented; A-006 requires availability, not a new purchasing subsystem.

Validator targets:
- assert all seven item constants occur in at least one reachable mart inventory;
- assert Master/Safari are absent from new shop inventories.

## P-05 More useful Pokédex

Goal: for a **seen** species, expose useful encounter guidance while not revealing undiscovered legendary/event locations.

Phase-1 implementation:
- reuse existing area-marker machinery for map location;
- add method metadata when encounter data exists: grass/cave, surf, fishing, special/event;
- add level range when it can be derived from wild encounter tables;
- hide or redact location/method for protected legendary/event species until their discovery condition is met.

Primary targets:
- `src/pokedex.c`;
- `src/pokedex_screen.c`;
- `src/pokedex_area_markers.c`;
- encounter-table helpers / wild encounter data;
- Spanish UI text.

Compatibility:
- read-only derivation from existing encounter/Dex flags;
- no new Pokédex save structure.

## P-06 Postgame training bridge

Do not add global EXP inflation and do not impose mandatory grinding.

Use existing systems:
- strengthen the natural postgame value of leader rematches;
- ensure a useful set of high-value VS Seeker/rematch trainers exists after Network/postgame progression;
- preserve player freedom to challenge while underleveled.

Primary targets:
- `src/vs_seeker.c` rematch progression table;
- trainer parties/rewards;
- selected postgame NPC hints.

Validator:
- static inventory of intended high-value rematch trainers and their final tiers;
- no change to global EXP formula.

### P-06 follow-up proposal (2026-10-09) — NPC battle levels / farming economy

**Status: PROPOSED — NOT APPROVED OR IMPLEMENTED.** User suggests potentially raising selected non-boss NPC trainer parties by +1 or +2 levels, partly because NPC/rematch battles are used for training and EXP farming. Do not apply globally. During a separate P-06 balancing study, audit trainer location, story timing, VS Seeker repeatability, encounter and boss level curve, EXP rewards and level-grinding opportunities; compare original vs Full NPC tiers. Evaluate selective +1/+2 only if it improves pacing without producing excessive EXP or making optional farming mandatory. Preserve global EXP mechanics, existing trainer progression decisions, and economy. Present recommendation and affected scope to user for approval before any trainer-data changes. Excludes the current A-016 party-order-only microblock.

## P-07 Environmental signals

Add restrained hints before major optional content:
- maritime/Navel Rock clues;
- Pewter/space anomaly clues;
- Mansion/Mew atmosphere;
- Berry Forest/Celebi nature clues;
- beast tracking cues.

Requirements:
- hints should guide without map-marker overexposure;
- no legendary location spoiler before the associated discovery flag/state.

Targets are map scripts/text only unless a tiny field special is required.

## P-08 Important NPC identity

Improve names/role cues for significant Full-added quest NPCs so they do not read as generic dispensers.

Priority NPC classes:
- maritime investigator/captain/harbor staff;
- Pewter scientist/museum staff;
- nature/Berry Forest investigator;
- postgame training/rematch guidance NPC.

No new save state solely for naming/presentation.

## Validation order

1. implement P-01/P-02 narrative state changes;
2. semantic migration audit against existing Full saves;
3. implement P-03/P-04;
4. implement P-05/P-06;
5. implement P-07/P-08;
6. run static validators;
7. update `RC_MYBOY_CHECKLIST.md` to A-005/A-006 truth;
8. freeze replacement RC commit;
9. require green exact-HEAD CI;
10. run MyBoy runtime suite;
11. only after runtime PASS, update `RC_AUDIT_LOG.md` and final acceptance evidence.

## Follower separation

`prototype/follower-runtime` is not part of this polish branch.

Follower can enter production only after:
- isolated compile/reproducibility checks;
- MyBoy runtime QA;
- Save/Link checks;
- provenance decision for full asset coverage.

If follower fails the gate, P-01 through P-08 must remain releasable without it.


## P-09 Signature Pokémon beside major trainers

Authority: A-007.

Required v1.0 scope:
- 8 Gym Leaders;
- Lorelei, Bruno, Agatha, Lance;
- Gary/Blue rival/Champion scenes.

Initial signature mapping:
- Brock — Onix (story) → Steelix (rematch);
- Misty — Starmie;
- Lt. Surge — Raichu;
- Erika — Gloom;
- Koga — Golbat (story) → Crobat (rematch);
- Sabrina — Kadabra (story) → Alakazam (rematch);
- Blaine — Magmar;
- Giovanni — Persian;
- Lorelei — Lapras;
- Bruno — Machamp;
- Agatha — Gengar;
- Lance — Dragonite;
- Gary/Blue — Squirtle/Wartortle/Blastoise by stage.

Implementation constraints:
- fixed map/event presentation objects, not the dynamic player-follower system;
- normal FireRed 8-bit object-event graphics IDs;
- no Pokémon/save/link structure changes;
- non-blocking placement and no trainer-sight/cutscene interference;
- provenance-cleared/project-created sprite path for missing assets;
- this block doubles as a small sprite/OAM integration pilot.

## Production work order — small, reversible blocks

A-013 temporarily interposes the approved Gym Leader roster-research pass after B8 closure and before B9. This does not remove or redefine B9–B12; it only changes the immediate execution order until the leader pass is complete.

The following order is authoritative for the remaining v1.0 production pass. Each block must be independently reviewable and must end with compile/static validation plus documentation before the next begins.

### B0 — Baseline and validator truth
Scope:
- reconcile repository docs with all approved runtime findings from the Drive evidence;
- update stale checklist language that still reflects pre-A-005/A-006 behavior;
- lock current save/link structural invariants;
- keep RC-F040 and RC-F041 regression validators.

No gameplay expansion in this block.

Exit gate:
- exact HEAD CI green;
- docs/validators describe current approved behavior;
- no stale Celio/old legendary requirements represented as acceptance truth.

### B1 — Low-risk UX/QoL cleanup
Authority: A-008 plus the referenced runtime findings.
Scope:
- UI-001 EV layout;
- UI-002 visible Physical/Special/Status category;
- Porygon 5,500-coin presentation/alignment;
- vending-machine quantity selector;
- Oak aide medal gates;
- National Dex no 60-capture quota;
- final HM rule QOL-HM-002: HM possession + badge enables field action; learned HM moves are forgettable;
- L10N-001 localized thousands separators for Full-added money/coin text;
- L10N-002 Move Reminder active dialogue aligned with the money-based system.

Reason for position:
small/localized changes with high runtime value; establishes a clean base before narrative/map work.

Exit gate:
- build green;
- targeted static validators;
- no SaveBlock/link schema changes.

### B2 — Boss/rival balance reconciliation
Authority: A-009 for Giovanni/progression-aware boss polish.
Scope:
- BOSS-001 premature-move audit, especially early Gary and first gyms;
- Giovanni Rocket Hideout and Silph battles brought to approved Full boss standard;
- preserve approved rosters/identity where frozen, changing only approved gaps/incoherent moves;
- add/extend trainer legality validators.

Exit gate:
- all boss party validators green;
- no accidental roster regression;
- staged progression/move availability audit documented.

### B3 — Postgame progression and rematch identity
Authority: A-009/BOSS-REMATCH-001 plus A-005 leader-identity polish.
Scope:
- gym rematches available after first Hall of Fame;
- strengthened League remains after Network Machine;
- eight leader-specific rematch dialogue sets;
- postgame training bridge through leaders/VS Seeker/high-value trainers.

Exit gate:
- repeatability retained;
- no National-Dex/capture dependency for Gym rematches;
- dialogue uniqueness validator;
- postgame progression validator.

### B4 — Specialty Balls and economy distribution
Scope:
- Net/Nest/Repeat/Timer/Luxury/Dive/Premier availability;
- staged Kanto/Sevii shop distribution;
- complete legitimate late/postgame shop;
- preserve original Dive Ball mechanics;
- Master/Safari excluded.

Exit gate:
- all seven specialty Balls reachable;
- shop/price validators green;
- caught-ball metadata untouched.

### B5 — Altering Cave and encounter polish
Authority: A-009/ENC-ALTERING-001 and approved special-encounter rarity targets.
Scope:
- automatic 9-table Altering Cave rotation;
- researcher becomes informational;
- approved special-encounter rates (Safari rares, Dratini, starters, Magmar/Electabuzz);
- preserve FireRed/LeafGreen integration intent.

Exit gate:
- all nine tables reachable;
- no manual species selector;
- encounter blob validators updated.

### B6 — Legendary narrative V2 core
Authority: A-005 plus A-009 legendary-capture UX principle.
Scope:
- remove legendary ticket ownership from Celio;
- maritime birds → Mystic Ticket → Lugia;
- Pewter Museum anomaly → Aurora Ticket → Deoxys;
- separate Berry Forest/Celebi investigation;
- roaming-beast first-contact cinematic and sequential activation;
- Ho-Oh as beast-arc capstone;
- advanced-save semantic migration.

Reason for later position:
highest state-machine/migration risk among non-follower features.

Exit gate:
- old saves cannot duplicate/softlock tickets or legendary captures;
- Celio canonical network role restored;
- all quest-state validators green.

### B7 — Legendary presentation / environmental signals
Scope:
- Mew visible appearances and final interactable Mew;
- cries/scenery/NPC clues for legendary arcs;
- important quest-NPC identity polish.

Exit gate:
- presentation does not alter battle identity/state;
- no hidden legendary spoilers before discovery flags;
- script/map compile validation.

### B8 — Signature Pokémon staging
**Status: CLOSED on master `28f4234`; post-integration Full Gameplay Core #617 SUCCESS.**

Scope:
- A-007 major-trainer companion objects;
- implement only missing signature assets needed for the 13 trainer identities;
- validate object counts, placement, trainer sight and scripted movement.

Reason before universal follower:
small controlled map-object pilot exercises the same sprite/OAM constraints with far less runtime risk.

Exit gate:
- all required major trainers have correct signature presentation;
- MyBoy milestone spot-check on early Gym / late Gym / Elite Four / Gary;
- no collision, trainer-sight or transition regression.

### B9 — Pokédex usefulness
Scope:
- encounter method and level context for seen species;
- preserve mystery for undiscovered legendary/event encounters;
- reuse existing area-marker system where possible;
- A-010 Kanto completion reward in GAME FREAK: preserve diploma + one-time Master Ball with retry-safe full-bag behavior;
- retain the National diploma and design its separate 100%-completion reward before B9 closure.

Exit gate:
- encounter guidance remains read-only derivation;
- no Pokédex save-layout change or SaveBlock growth;
- protected-event species do not leak locations;
- Kanto Master Ball cannot duplicate and cannot be lost when the bag is full;
- original Kanto/National diploma distinction remains intact.

### B10 — Player follower prototype QA and integration decision
Scope:
- continue only from `prototype/follower-runtime`;
- expand mechanics testing first, not asset coverage;
- MyBoy warps/doors/ledges/bike/Surf/Fly/scripts/battle/save/link tests;
- verify party reorder/egg/fainted lead behavior;
- resolve asset provenance before any broad sprite import.

Decision gate:
- PASS → integrate conservatively and then expand coverage;
- FAIL or unresolved provenance → exclude follower from v1.0 without blocking B0–B9.

### B11 — Consolidated validators and replacement RC
Scope:
- update FINAL_AUDIT_PLAN / RC_MYBOY_CHECKLIST to final V2 truth;
- run exhaustive static/spec audit;
- exact-HEAD CI;
- freeze Git SHA + ROM SHA-1;
- produce replacement RC only here.

### B12 — Final MyBoy acceptance
Scope:
- execute only the affected/required runtime matrix on the new exact RC;
- use Drive runtime evidence document for manual observations and PASS/FAIL;
- repair any blocker, regenerate exact RC if code changes;
- final audit log and release decision.

## FUTURE PROPOSAL — Conservative trainer battle AI improvements (NOT APPROVED)

**State:** PROPOSED / EVALUATION PENDING. Recorded on 2026-10-08 at the start of the Agatha roster review. This is an out-of-scope idea, not an approved design or implementation block; it must not interrupt Agatha.

Investigate improving decision quality for important trainer battles (Gym Leaders, Elite Four, Giovanni and Gary/Blue) without unfair foreknowledge of the player's hidden moves/actions. Candidate research: move utility/type and KO selection, status/setup timing, and—only after risk assessment—switching and team-level decisions.

Current engine is FireRed-derived with existing Full physical/special-category AI adaptations. Before approving a design, inspect AI flags and scripts, engine move selection, switch/item logic, double battles and battle RNG, and determine whether changes can be scoped without SaveBlock, link/trade protocol or battle-state ABI changes. Do not promise zero compatibility risk.

If eventually approved, isolate it in an independently reviewable technical microblock with explicit regression/legality validators, deterministic battle scenarios, exact-head Full Gameplay Core, controlled integration, integrated-head CI and targeted MyBoy runtime acceptance. No gameplay/AI changes are authorized by this entry.

## FEASIBILITY REVIEW — Spanish character name Lorelei → Prima (2026-10-08)

**Status:** USER APPROVED / IMPLEMENTED / VALIDATED / CI-GREEN / INTEGRATED / CLOSED (2026-10-08). This is a user-approved self-contained localization microblock, assessed after Agatha closure and before Lance. The approval is strictly limited to Spanish player-visible character name; trainer IDs and other-language names remain unchanged. Do not broaden the scope.

**Finding:** the approved Spanish-only localization was implemented without changing technical trainer identities or other languages. Baseline analysis confirmed low predicted compatibility risk **when strictly limited to Spanish-facing display strings**. Before implementation, the existing trainer JSON has distinct `trainerName_english`, `trainerName_spanish`, `trainerName_italian`, `trainerName_french` and `trainerName_german` fields for each of the two Lorelei battles. Spanish originally used `LORELEI` for both and now uses `PRIMA`, while French retains `OLGA`, confirming that localized character display names are supported. `PRIMA` is shorter than `LORELEI`, so the substitution does not introduce a longer trainer name. The unrelated location string `ISLA PRIMA` already exists in Spanish; it must **not** be altered.

**Confirmed Spanish-facing references to review if approved:**
1. `src/data/trainers.json` — `trainerName_spanish` for `TRAINER_ELITE_FOUR_LORELEI` and `TRAINER_ELITE_FOUR_LORELEI_2` (only these two name fields).
2. `data/maps/PokemonLeague_LoreleisRoom/text_es.inc` — first battle and rematch self-introductions (2 visible name occurrences).
3. `data/maps/FourIsland_LoreleisHouse/text_es.inc` — home dialogue name prefixes (2 occurrences).
4. `data/maps/FourIsland_IcefallCave_Back/text_es.inc` — Team Rocket scene name prefixes (4 occurrences).
5. `data/maps/FourIsland_Mart/text_es.inc` — NPC reference to her name (1 occurrence).
6. `data/text/spanish/fame_checker.inc` — Fame Checker, related quotations and Pokémon Journal text (11 visible `LORELEI` lines, excluding symbols/identifiers).

**Identity-preservation rules:** leave `TRAINER_ELITE_FOUR_LORELEI*`, `FAMECHECKER_LORELEI`, map paths/labels, trainer picture graphics, flags/vars, event scripts, pointers, all English/Italian/French/German names and texts, roster, battle AI, link/trade protocol and SaveBlock data unchanged. Do not broadly replace `Lorelei` in code; preserve internal symbols. Review any additional user-visible Spanish occurrences before implementation.

**Validation and acceptance if separately approved:** make a dedicated small feature branch; adjust only the needed strings and Spanish trainer names, check in-game character encoding and Fame Checker/Pokémon Journal line layout, add a targeted Spanish-name/reference validator if justified, and refresh the audited `src/data/trainers.json` blob lock in `tools/validate_audited_data_blobs.py`. Run Full Gameplay Core on the exact feature HEAD and after integration, and test the battle introduction, rematch, Four Island home/cave/mart and Fame Checker in MyBoy, including existing save compatibility. This is a ROM-content change, **not** a docs-only exemption. No claim of absolute zero risk or of runtime validation is made here.

**Decision and closure:** the user explicitly approved Spanish display name **`PRIMA`** with other languages and technical identities unchanged. Feature HEAD `ddd049c8bb712032207523dcc6fa3be4f219ff4e` passed Full Gameplay Core **#680 SUCCESS**; PR **#34** merged as `7c0031b312534cc44119216ea37bc9a9df076d87`; exact integrated master SHA passed Full Gameplay Core **#681 SUCCESS** (push-run `37749207866`). **Microblock CLOSED.** Validation was technical/build CI; MyBoy runtime acceptance remains a separate release-QA layer. Next: Lance design review.

## Documentation cadence

After every B-block:
1. update `PROJECT_CONTINUITY.md` with completed scope, commit SHA, CI result and next block;
2. update `RC_AUDIT_LOG.md` when the block changes acceptance evidence or discovers/fixes a defect;
3. update the relevant validator/checklist immediately when behavior changes;
4. use the Google Drive runtime document for manual MyBoy evidence, observations and final runtime acceptance—not as the source of implementation truth.

This keeps disposable chats out of the critical path: a new chat resumes from the last completed B-block in GitHub, then consults Drive only for runtime evidence.
