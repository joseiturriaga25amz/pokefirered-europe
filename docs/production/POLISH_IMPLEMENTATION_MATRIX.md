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
