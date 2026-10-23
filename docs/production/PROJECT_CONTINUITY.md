# Pokémon Rojo Fuego Full v1.0 — Project Continuity


## CURRENT ACTIVE ROADMAP (2026-10-22)

This is the operative source-of-truth snapshot. Historical dated entries below remain evidence, but do not define competing active task queues. Recheck GitHub branch, HEAD, CI and amendments at each session. NO GAMEPLAY MODIFIED BY THIS AUDIT.

**Repository state:** prototype/follower-runtime HEAD 617367ea3457969ccde70e1b748e45a8e0b3881c at audit; master 8d89f2b444a6e25ef47716861a53f2e4f6920d07 separate/diverged. Last technical SHA fdf710c116d4bb6a347f7a81caf3cb62b2b22996: exact Full Gameplay Core run 39851490790 SUCCESS and Follower Prototype run 39851490652 SUCCESS. Last docs-only 617367e: Full Core run 39851709696 IN PROGRESS, Follower run 39851709892 SUCCESS when inspected. B10 follower OPEN; no merge, no MyBoy final QA. Do not treat a passing older SHA as CI proof for a new technical HEAD.

### Rarity policy and cross-map evidence

Current branch compared directly with tag baseline-spanish-vanilla, using FireRed land/water/rock encounter tables: 24 changed maps, 91 species/map/method percentage differences (including newly changed Route1/Route22/Route3/MtMoon). Fishing and all reward/gift methods still require separate contextual review; changed means changed from baseline, not necessarily broken.

- **Starter families (actual wild odds):** Charmander/Charmeleon/Charizard at Mt Ember 15%/5%/4%; Squirtle/Wartortle/Blastoise at Seafoam B1F 15%/5%/4%; Bulbasaur/Ivysaur/Venusaur at Berry Forest 15%/5%/4%. The user wants directly caught final evolutions to feel **exceptionally rare** because their basic forms can be evolved. Candidate: final Charizard/Blastoise/Venusaur 1% each, preserving basics at 15% and middle stages at 5%. This exact numeric candidate is NOT YET APPROVED NOR IMPLEMENTED.
- Eevee on Route7 is 15%; Vaporeon/Jolteon/Flareon each 4% in their special habitats. Review stone-evolution availability and whether final forms merit rarer direct encounters. Do not automatically apply the 1% rule to every species or final.
- LeafGreen-type inclusions checked: Bellsprout Route5 25%, Sandshrew and Vulpix Route8 20% each, Slowpoke Route6 surfing 100%; Safari Pinsir/Scyther, Chansey, Kangaskhan and Tauros in designated sites 15%. Basic/unique species should remain reasonably obtainable. All were consciously incorporated by earlier approved encounter constraints; modifications require own justification and semantic validator updates.
- Rare encounters examined across FireRed land/surf/rock/fishing methods: 49 individual map+method+species results at exactly 1%, representing only 14 species; most have an easier alternative via another map, evolution or gift. Do not globally raise them. Route3 Nidoran female 14% and male 11%, and MtMoon 1F/B2F Clefairy 10%, were separately IMPLEMENTED in fdf710c with exact CI success. Route1 Speed-only 35% Pidgey / 35% Rattata / 30% Spearow and Route22 Attack-only 55% Mankey / 45% Nidoran male also implemented and validated on preceding 0a3d026.
- Viridian Forest southeast clearing near **non-trainer boy at (45,58)** is user-selected for Oddish-only (+1 SpAttack). NOT IMPLEMENTED. Bellsprout gives +1 Attack and must not be included. Wild headers are per map, so a safe bounded encounter patch needs grass metatile/collision/item/warp/follower audit or a separately connected micro-map. Preserve remainder of Forest unchanged and check early Oddish effect on Brock.

**Working rarity principle (proposed):** early basic species obtainable; evolved alternatives uncommon; final stages directly catchable at genuinely special odds only when their basic evolution path is already accessible. Balance species-wide encounter access, route ecology, version identity, percent arithmetic, capture chance, gifts and trades. Actual numeric changes remain separate technical microblocks; preserve audited data blob hashes and frozen 21-map invariants.

### Nine NPC trades: player-value audit / design direction

Actual FireRed source trade roster in src/data/ingame_trades.h:
1. Abra to Mr. Mime — candidate retain.
2. Poliwhirl to Jynx — user wants Jynx **earlier**; audit NPC location, acquisition timing and whether a less burdensome species request is better. No selected substitute yet.
3. Nidoran male to Nidoran female — USER WANTS REPLACEMENT (female now 14% Route3); new request/reward pair not decided.
4. Spearow to Farfetch'd (held Stick) — candidate retain, Spearow now normally found Route1.
5. Nidorino to Nidorina — USER WANTS REPLACEMENT; new request/reward not decided.
6. Golduck to Lickitung — assess late acquisition and trade value.
7. Raichu to Electrode — user finds Electrode reward poor; evaluate an improved trade, not yet selected.
8. Venonat to Tangela (held Stardust) — user finds Tangela reward poor; evaluate an improved trade, not yet selected.
9. Ponyta to Seel — user finds this plausible; check actual site and stage.

All nine preserve a source-defined fixed personality/OT/nickname/IV/item. Before editing verify script placement, NPC timing and dialogue, reward rarity and usefulness, party/box and link safety, species availability and required trade evolution. NPC trades are distinct from link exchange. No replacements are approved by exact pair and none has been changed.

### Phase 0 source follow-up — 2026-10-23 (DOCUMENTATION ONLY; gameplay unchanged)

Audit reference: branch `prototype/follower-runtime` pre-note HEAD `9cb858afc2bd179a1b89ce96080d667f6f30086a` (master remained `8d89f2b4`, NOT merged). Both exact-head workflows finished SUCCESS: Full Gameplay Core [39854853814](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/39854853814), Follower Prototype [39854853769](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/39854853769). This does **not** mean MyBoy acceptance, ROM delivery, integration, or B10 closure.

**Encounter table verified in source**, `src/data/wild_encounters.json` against `baseline-spanish-vanilla`:
- Mt Ember Exterior: Charmander 15% (level 30/32), Charmeleon 5% (36), Charizard 4% (40); Seafoam B1F: Squirtle 15% (26/28), Wartortle 5% (28), Blastoise 4% (36); Berry Forest: Bulbasaur 15% (30/35), Ivysaur 5% (31), Venusaur 4% (37). User's exceptional-direct-final concept supports *proposing* 1% for the three final evolutions only, not changing source now. Land table slots are 20/20/10/10/10/10/5/5/4/4/1/1: moving any final 4%-slot to 1% necessarily reassigns an existing slot (Mt Ember Rapidash/Magmar, Seafoam Golduck/Golbat, Berry Forest Venomoth/Hypno). Require an explicit ecology-neutral slot redistribution and semantic validator before approval/implementation; do not silently increase another rare's probability.
- Eevee Route7 15%; Vaporeon Seafoam B1F 4%; Jolteon Power Plant 4%; Flareon Mansion 1F 4%. Default preliminary advice: keep 4% pending review of stone evolution and natural availability, no blanket final-stage rule.
- FireRed Safari comparison, same specific land areas: Chansey North 4% -> Full 15%, Kangaskhan East 4% -> 15%, Tauros West 4% -> 15%, Scyther Center 4% -> 15%; Pinsir Center absent in original FireRed -> Full 15%. These deserve a Safari catch/flee/steps/economy study before selecting 5/10/15%, not an automatic nerf. Dratini Super Rod Safari 15% and Dragonair 1% remain unchanged in those fishing slots. Clefairy Mt Moon 1F 1% -> 10%; Mt Moon B2F 6% -> 10%. These increases were part of earlier encounter work; reopening is review, not revocation.
- Other verified additions: Bellsprout Route5 25%, Sandshrew and Vulpix Route8 20% each, Magmar Mt Ember 5%, Electabuzz Power Plant 5%, Wild Eevee Route7 15%. The rarity policy should preserve basic-form usability and validate total player access via evolution/gift/trades, not simply count an isolated 1% slot.

**Nine source NPC trade sites verified** against `src/data/ingame_trades.h` and the actual `data/maps/*/scripts.inc`:
1. `Route2_House`: Abra -> Mr Mime (retain candidate; arrival through Route2 access still contextual).
2. `CeruleanCity_House3`: Poliwhirl -> Jynx. NPC is early, but Poliwhirl acquisition is fishing/evolution-gated; Old Rod fish in relevant Route25/6 slots is Magikarp only, so NPC location alone does not make Jynx early.
3. `UndergroundPath_NorthEntrance`: Nidoran M -> Nidoran F (must replace according to user).
4. `VermilionCity_House2`: Spearow -> Farfetch'd with Stick (retain candidate).
5. `Route11_EastEntrance_2F`: Nidorino -> Nidorina (must replace).
6. `Route18_EastEntrance_2F`: Golduck -> Lickitung (Golduck acquisition is unnecessarily late for unique Lickitung; review request).
7. `CinnabarIsland_PokemonLab_Lounge`: Raichu -> Electrode (user rejects reward).
8. `CinnabarIsland_PokemonLab_Lounge`: Venonat -> Tangela (user rejects reward); note this NPC script invokes lower-level `CreateInGameTradePokemon` and `DoInGameTradeScene`, unlike most other trades, requiring dedicated script-equivalence audit.
9. `CinnabarIsland_PokemonLab_ExperimentRoom`: Ponyta -> Seel. Ponyta wild at Mt Ember/Kindle Road, ordinarily accessible during the Sevii detour after Blaine; Seel is wild already in Seafoam. Candidate is to keep Seel but request a species reachable before/around Cinnabar instead.

**Concrete candidate pairs for design discussion ONLY — NONE APPROVED OR IMPLEMENTED:**
- Cerulean: Clefairy -> Jynx (10% Mt Moon Clefairy, available before Cerulean) instead of Poliwhirl; alternate easier Meowth/another early species, but weigh Jynx's early Ice/Psychic power and boosted traded EXP.
- Underground North: Meowth -> Shellder instead of the Nidoran swap (Meowth Route5; Shellder otherwise later fishing).
- Route11 gate: Drowzee -> Staryu instead of Nidorino/Nidorina (Drowzee Route11; Staryu Vermilion by later rod). Check if Staryu/Starmie pre-Celadon progression is too advantageous.
- Route18 gate: Doduo -> Lickitung instead of Golduck (Doduo on Routes16–18; Lickitung not wild in current source).
- Cinnabar lounge: Raichu -> Magmar instead of Electrode (trade cost/high-value rare; consider whether devalues Mt Ember 5% Magmar); Venonat -> Electabuzz instead of Tangela (Power Plant 5%; consider whether trade reward is too generous). These pair choices are not committed design.
- Cinnabar lab: Koffing -> Seel instead of Ponyta (Koffing abundant in Mansion, avoids post-Blaine Ponyta prerequisite). Alternative retain existing pair after progression study.
- Keep Abra -> Mr Mime and Spearow -> Farfetch'd candidates unchanged.

**Pre-implementation trade safety gate:** no new species IDs or save/BoxPokemon/link layout; preserve each trade's existing one-time completion flag/slot for old save compatibility; review dynamic generic dialogue *and* hard-coded NPC text, Spanish names/nicknames/OT/item/mail, requested-species accessibility, traded-mon level and learnset, pre-National Kanto eligibility, trade cancellation/full party, player value, and scripts/warps before editing. Do not rename old flags merely for aesthetics. Separate encounter odds from trade changes and from Viridian Forest Oddish map work.

**Cross-block idea feasibility status:** the current matrix below is an inventory, not proof of completion. Prior proposals requiring independent source-level assessment include (LOW-MED) EV summary bars removal/nature colors, leader rematch dialogue; (MED) 252-useful-EV battle milestone and displayed enemy EV yield; (MED-HIGH) battle move-type/STAB/category/contact information, repeated medicine, Dex route completion, six-EV training hub, journals/registry; (HIGH) Hold-R ball selector, START PC access, postcapture inspection and universal scene-aware follower/386 normal-shiny runtime. Audit data flow, battle callbacks, field-task controls, UI screen geometry, flags, player accessibility, save/link safety and tests before allocating microblocks. Existing user preferences are not universal implementation approval. Final MyBoy and private ROM delivery remain separate release blockers.

### Remaining feature feasibility inventory and gates

| Feature | Real status | Main risk and next evidence |
| --- | --- | --- |
| Follower 386 sprites normal/shiny, interactions, Gary scenes, all Gym/League/story contexts, save/bike/Surf/link | B10 PARTIAL; diagnostic builder compiles privately, removes ROM afterward; MyBoy incomplete, no master merge | HIGH graphics/OAM/script runtime. Gary's own separate visible follower unverified; A-007 citation contradicts current formal A-001..A-006. |
| Eight leader-specific rematch conversations | A-005 APPROVED, all eight still share four generic scripts | LOW-MED script/Spanish/QA. Keep all already-approved boss parties unchanged. |
| Koichi Dojo fix | source implemented and validated statically | MyBoy regression still pending. |
| EV summary numbers, no bars; blue boosted / red reduced nature | six numeric EV values and total exist, bars persist; nature colors not built, 252 useful vs actual 255/stat cap label wrong | LOW-MED summary/palette/screen QA; no EV game rule change. |
| 252-useful-EV-only notice after battle | preferred, not implemented, never 100/200 | MED gain recipient/threshold aggregation and battle callback. |
| Live enemy EV yield; move contact, category, STAB, type/resistance; healthbox type icons | data exist, display not implemented | MED-HIGH battle UI layout, dual types, special type changes and move immunity/abilities. |
| Hold-R wild-only ball quick select with left/right/release | NOT IMPLEMENTED | HIGH battle input/catch/cancel; MyBoy touch and Safari/link safe. |
| PC from START, postcatch nature/ability/moves inspection | requested, NOT IMPLEMENTED | HIGH storage/capture/save/script state restrictions. |
| Dex route completion, postgame journal, boss registry | user-preferred, NOT IMPLEMENTED | MED-HIGH discovery/spoiler/flags and storage budget. |
| Repeated medicine use; postgame six-EV-specialist trainer row | user-preferred, not verified implemented | MED-HIGH inventory or map/XP/money/economy/battle data. |
| Legendary narrative, special Balls, EV/Dex polish, follower friendships, early game/Gary/Liga/Dojo, MyBoy | A-005/A-006 and historical freeze, MIXED partial and tests | Must reconcile source against approved decisions and complete all critical regressions before candidate. Guaranteed shiny Charmander is explicitly REVOKED. |

### Controlled project work order (one active stream, no monolithic changes)

**PHASE 0 (ACTIVE):** finish full rarity + acquire-by-evolution/trade/gift audit (not blanket odds); map all nine NPC trade scripts and availability, propose exact replacement pairs; technical feasibility/priority of all user-endorsed QoL above. No additional feature source edits in this phase. Treat previous chronology as historical, not instructions to resume outdated early-NPC trainers or 100/200 EV alerts.

**PHASE 1:** after any material design approvals, separate controlled microblocks for (a) optional final-stage encounter odds, (b) NPC trade rewards/request/dialogue, (c) Oddish-only southeast Forest patch. Distinct commits and exact validator + hash-lock + full game CI, audit after implementation. Do not mix them.

**PHASE 2:** highest-value approved UI and quality improvements first: EV numbers-only and nature colors, leader-specific rematch dialogs, EV yield battle info, 252 milestone, then risky control/storage/capture/PC work only after reviewed callback/state design; schedule postgame EV hub, journals, history and medicines independently. Features proposed but not prioritized for this release must stay visible rather than silently becoming blockers or silently removed.

**PHASE 3:** finish B10 follower, Gary's own companion design traceability, story-script/Gym/League/Dojo and legendary/roster integration audit, preserve original saves and link ABI. MyBoy QA is a separate layer.

**PHASE 4:** deliberate integration of diverged branch with master, exact technical + integrated HEAD CI, safe asset/license provenance and verified MyBoy patch/ROM delivery followed by full acceptance. Never declare release only on workflow green.

Continuity ownership: THIS file is global current state + decision/feasibility evidence; NEXT_SESSION.md contains **only** next action and checkpoint; DECISION_AMENDMENTS.md has approved postfreeze architectural/design overrides; RC_MYBOY_CHECKLIST.md is runtime testing; frozen docs/spec/ never overrule amendments. Referenced REPOSITORY_GUARDRAILS.md and POLISH_IMPLEMENTATION_MATRIX.md do not exist in this branch; do NOT recreate duplicate documents without need.

---

**Purpose:** make the repository sufficient to resume the project without relying on any previous chat.

## 1. Start here in every new session

Before modifying code:

1. Read this file.
2. Read `docs/production/DECISION_AMENDMENTS.md`.
3. Read `docs/production/RC_AUDIT_LOG.md`.
4. Read `docs/production/FINAL_AUDIT_PLAN.md`.
5. Read `docs/production/RC_MYBOY_CHECKLIST.md`.
6. Read `docs/production/SECOND_PASS_AUDIT.md`.
7. Inspect the current branch HEAD and latest GitHub Actions result.
8. Only if a design detail is still needed, consult the frozen sources under `docs/spec/`.

Previous chats are **not required** and must not override the repository.

## 2. Source-of-truth precedence

From highest to lowest authority:

1. Explicit approved post-freeze amendments in `docs/production/DECISION_AMENDMENTS.md`.
2. Frozen preproduction specification under `docs/spec/Pokemon_Rojo_Fuego_Full_Preproduccion_v1.0.md`.
3. Frozen matrices under `docs/spec/Pokemon_Rojo_Fuego_Full_Matrices_v1.0.md`.
4. Frozen decision log under `docs/spec/Pokemon_Rojo_Fuego_Full_Decision_Log_v1.0.md`.
5. Frozen production prompt under `docs/spec/Pokemon_Rojo_Fuego_Full_Prompt_Maestro_Produccion_v1.0.md`.
6. Current implementation and automated tests as evidence of what is actually implemented.

A historical frozen requirement superseded by an approved amendment must **not** be silently restored.

## 3. Approved amendments that materially change the freeze

- **A-001:** MyBoy is the required runtime QA emulator. mGBA is optional diagnostic only.
- **A-002:** abandon the 142-slot normal Items pocket; keep vanilla 42-slot behavior. The 400 bytes at `0x348C` remain reserved/unused.
- **A-003:** finish implementation/static verification first; concentrate user-run runtime QA in the final RC phase instead of stopping after every block.
- **A-004:** GitHub is the continuity authority. Chats are disposable.

## 4. Repository / branch / baseline

- Repository: `joseiturriaga25amz/pokefirered-europe`.
- Active production branch: `feature/full-gameplay-core`.
- Frozen vanilla tag: `baseline-spanish-vanilla`.
- Baseline commit: `e184c5cf898cd29efebd33bc1bfe5994277e21ab`.
- Production target: `firered_es_modern`.
- Baseline Spanish SHA-1: `ab8f6bfe0ccdaf41188cd015c8c74c314d02296a`.

## 5. Current technical state at continuity freeze

The first exhaustive static audit is nearly complete and an explicit **second-pass adversarial audit** is active.

Latest code-affecting second-pass commits include:

- `25fb95adfaab7c734d86f9e83241c4ae148d914b` — corrected wireless-status UBFIX applied from a clean pre-change file;
- `2f21644529ba1146f70adc8b7f26a7e3135a60e9` — applies Full Hall-of-Fame KO recovery to the Spanish script actually compiled;
- `74bf56b4ac6799682d2ccef60c274b0f80582a36` — restores the non-target generic Hall-of-Fame script to vanilla;
- `444b1f27e4bfda87f3f326937af238d7e28c0845` — extends exact audited blob locks to trainer payloads and target-language high-risk scripts;
- `7fe7204c8d125180dee1faa18df5309b599e8732` — adds the second-pass release-integrity validator to consolidated CI.

The exact current HEAD still requires a fresh consolidated CI result before any RC freeze. Older CI success and older ROM hashes are historical evidence only and must **not** be treated as validation of the current code payload.

The workflow still builds `firered_es_modern`, performs two clean builds and requires byte-for-byte reproducibility before recording a checksum.

## 6. RC audit findings repaired so far

See `RC_AUDIT_LOG.md` for the authoritative finding-by-finding record. The recovery/final audit now includes RC-F001..RC-F035, with RC-F031 explicitly corrected as a false positive rather than retained as a fictional bug fix.

Important late findings include:

- vanilla-save migration existed but was not called on Continue;
- reusable-TM capacity/add/shop paths were inconsistent;
- direct trade-evolution items reached the UI without a core evolution effect;
- doubles AI had per-side history aliasing and out-of-bounds move-history reads;
- Gary routing/identity still depended on vanilla starter branches;
- recorded AI hold effects were briefly reinterpreted as item IDs and corrected;
- tested link synchronization fixes were excluded from Full's MODERN revision-0 build;
- UBFIX mon-data accessors still relied on incompatible function aliases;
- wireless status group accounting could index outside its counter array;
- Hall-of-Fame state validation was checking a generic script while the Spanish target lacked the Full KO-recovery hooks;
- Repel RC-F031 was a recovery-audit false positive: the Spanish target already implemented QOL-007, and the generic accidental edit was reverted.

Exact blob locks now cover the original high-risk gameplay data plus trade, trainer metadata/parties and selected Spanish high-risk scripts.

## 7. Important automatic validators

### `tools/validate_full_trainer_sets.py`
Last known PASS:
- 34 Full parties;
- 163 Pokémon;
- 632 custom moves;
- validates species, level, IV, held item and move legality including level-up, TM/HM, tutor, egg and pre-evolution learnability.

### `tools/validate_release_integrity.py`
Second-pass meta-gate that verifies:
- consolidated CI targets `firered_es_modern`;
- all production validators are actually invoked;
- Gate 6/7/QoL checks point at Spanish scripts that feed the target;
- generic non-target Hall-of-Fame/Repel scripts remain vanilla;
- second-pass high-risk blob locks are present;
- audit-log traceability includes the corrected false positive and late recovery findings.

### `tools/validate_rc_freeze.py`
Protects, among other things:
- Gen III species/move/item ID-space compatibility;
- SaveBlock1 size and Full header offset;
- non-destructive Full save migration;
- vanilla bag reservation after A-002;
- frozen item and berry prices;
- EV-reducing berry definitions;
- Two Island berry progression;
- fossils and Cinnabar revival;
- second Fighting Dojo state/reward;
- approved evolution invariants;
- all nine Altering Cave tables/selector values;
- Porygon 5,000-coin price.

## 8. Save / compatibility facts

Direct comparison with `baseline-spanish-vanilla` established:

- vanilla had `unused_3D24[16]`;
- Full replaces exactly those 16 bytes with `struct FullSaveHeader`;
- `towerChallengeId` and `trainerTower` keep their offsets;
- `SaveBlock1` remains `0x3D68`;
- `fullHeader` remains at `0x3D24`;
- `unused_348C[400]` remains intact after A-002;
- Pokémon / BoxPokemon layouts remain compile-locked Gen III compatible;
- species/move/item ID spaces remain vanilla-sized;
- pre-National non-Kanto/egg link restrictions remain;
- Gen III Pokémon trading compatibility is an explicit acceptance goal;
- round-tripping the same modified save through vanilla is **not** a supported goal.

## Current RC audit recovery note

After the 2026-09-20 app-side forced closures, repository history was confirmed intact and the audit resumed from GitHub. The first audit found multiple real defects and also exposed one false positive caused by inspecting a generic language script instead of the Spanish file actually compiled. That false positive is recorded and corrected.

The audit is now using a second independent layer defined in `docs/production/SECOND_PASS_AUDIT.md`: compiled-target verification, semantic baseline diff, validator skepticism, negative-path review, cross-layer contradiction checks and exact blob locks after semantic review.

A reproducible MyBoy RC was frozen at `a1c7fa573ac784ef089bfdf966aa38fc84861212` (ROM SHA-1 `6ebb0ce7cc736d7fd6c9c5bce09a21aaaf7d0443`) and entered runtime QA. Runtime invalidated it with two confirmed blockers: RC-F040 (pre-National cross-generation evolutions reached the animation but were canceled by a leftover vanilla National-Dex guard) and RC-F041 (Koichi's Fighting Dojo sight-trigger script no longer began with `trainerbattle`, causing deterministic MyBoy freeze when he approached the player). Both defects are fixed in source and statically gated. A replacement reproducible MyBoy artifact/checksum is required after the accumulated runtime-polish pass before final acceptance continues on the new candidate.

## 9. What remains before v1.0 final

The project is no longer in a broad implementation phase. Remaining work is primarily **Release Candidate audit and runtime acceptance**:

1. finish exhaustive static/specification audit described in `FINAL_AUDIT_PLAN.md`;
2. ensure exact final HEAD CI is green;
3. build/freeze one RC ROM and record checksum;
4. execute `RC_MYBOY_CHECKLIST.md` on that exact build;
5. repair any runtime defects;
6. rerun affected tests plus adjacent regressions;
7. perform final release-diff and documentation consistency pass;
8. only then promote/merge/tag v1.0.

Do **not** call the project 100% final merely because CI is green.

## 10. Working-style instruction

The user explicitly prefers:

- rapid forward progress;
- autonomous, meticulous internal review;
- no repeated manual testing interruptions during implementation;
- runtime tests concentrated at meaningful final milestones;
- no need to request approval for ordinary bug fixes required to satisfy already-approved requirements.

Do not reintroduce a slow block-by-block approval workflow.

## 11. If a new chat starts

The correct first action is to inspect this repository and continue from the RC audit. Do not ask the user to reconstruct old chat history and do not assume a stale commit from a previous conversation is still HEAD.


## 12. 2026-09-24 handoff — runtime QA closeout and approved polish scope

The old MyBoy RC is a1c7fa573ac784ef089bfdf966aa38fc84861212 (ROM SHA-1 6ebb0ce7cc736d7fd6c9c5bce09a21aaaf7d0443) and is NOT the final acceptance candidate. It remains useful only as runtime evidence.

### Old-RC evidence now closed

- Mew quest in Pokémon Mansion was completed and Mew captured. Functional chain passes, but narrative/visual presentation needs polish: preserve canonical diary history, add current-day NPC atmosphere, visible overworld Mew appearances and an interactable final Mew instead of immediate battle from the last diary.
- Gym rematches: Brock was battled repeatedly, proving repeatability in runtime. Misty, Lt. Surge and Erika were also reached/battled and felt appropriately challenging; the user's party was intentionally underleveled from speedrun-style progression, so do not treat difficulty as a balance defect.
- All eight gym-rematch scripts currently reuse the same generic offer/opening/defeat/post-battle strings. Replace with leader-specific dialogue while preserving teams/mechanics.
- Strengthened League was entered; Lorelei battle started and Dewgong/Lapras were observed before the underleveled team lost. This is a smoke PASS for rematch-League activation only, not full League acceptance.
- Do not force the user to grind this old RC to complete the strengthened League or Ho-Oh respawn. Validate Ho-Oh KO/HOF recovery on a disposable/new RC save.
- Roaming beasts and Celebi are intentionally withdrawn from old-RC manual QA because both will be redesigned.

### Approved legendary narrative V2

See DECISION_AMENDMENTS.md A-005. Key points:
- Celio returns to network/Ruby/Sapphire connectivity role and no longer distributes legendary tickets.
- Maritime/birds -> MysticTicket -> Lugia; Deoxys -> Pewter Museum investigation -> AuroraTicket; Mewtwo -> Mansion/Mew; beasts -> Ho-Oh capstone; Celebi -> separate Berry Forest nature quest.
- First beast contact is a no-battle cinematic with Suicune focus plus Raikou/Entei, all marked seen; only one roamer active sequentially.
- Roamer search/catch UX must be much less tedious.
- Preserve Gen III IDs, structures, ticket destinations, Pokédex flags, vanilla roamer storage and advanced-save migration.

### Approved immersion/QoL scope

See DECISION_AMENDMENTS.md A-006.

- Sell all existing Gen III specialty Balls progressively and naturally: Malla/Net, Nido/Nest, Acopio/Repeat, Turno/Timer, Lujo/Luxury, Buceo/Dive, Honor/Premier. Master/Safari stay non-commercial.
- Dive Ball keeps original Gen III behavior unchanged; in FireRed it may be mostly aesthetic because there is no normal underwater map use. Do not invent Surf/fishing behavior.
- Approved experience targets: party-leader follower Pokémon, contextual follower dialogue, more useful Pokédex for seen species, natural postgame training bridge, legendary environmental signals, and stronger identity for important NPC dialogue.
- Follower remains a technical-gate module, not permission to destabilize v1.0.

### Follower research result to resume from

A strong public technical/reference candidate is monhacks/arrantemerald branch followers-expanded-id:
- README explicitly claims HGSS-style followers for all 386 Pokémon, forms and shinies;
- follower interactions/messages, dynamic overworld palettes, large OW support and a backwards-compatible 16-bit overworld graphics-ID scheme;
- repository contains 440 Pokémon overworld PNG files under graphics/object_events/pics/pokemon, including forms/legacy variants;
- README says it does not increase save-data structures or the object-event structure.

This is Emerald code, not drop-in FireRed code. Port only the minimal concepts/assets after source audit. The repository did NOT expose a clear top-level license during inspection, so asset/code provenance and redistribution permission must be resolved before importing. Do not assume public GitHub equals licensed for redistribution.

Compatibility design for follower:
- follower is derived from the existing party leader and is not separately persisted;
- do not alter struct Pokemon, BoxPokemon, SaveBlock sizes, species/item IDs or Link serialization;
- on/off control may use an audited existing Full flag/setting;
- auto-hide/reappear around bike/Surf/Fly/link/cutscenes/unsafe scripts as needed;
- isolated prototype plus rollback; MyBoy QA for warps/ledges/doors/trainer sight/palettes/OAM/party reorder/egg/fainted lead/shiny/save-load/link.

### Next session order

1. Re-read PROJECT_CONTINUITY.md, DECISION_AMENDMENTS.md, RC_AUDIT_LOG.md, FINAL_AUDIT_PLAN.md, RC_MYBOY_CHECKLIST.md.
2. Continue follower-source/license/provenance research before importing anything.
3. Convert approved old-RC runtime findings into the grouped polish implementation:
   - RC-F040/RC-F041 already fixed in source;
   - legendary V2 narrative and roamer UX;
   - Mew visual/narrative polish;
   - unique leader-rematch dialogue;
   - specialty Ball shops;
   - Pokédex/postgame-training/NPC/ambient polish.
4. Prototype follower separately and merge only if it passes structural/runtime gates.
5. Update validators/checklist to the approved V2 behavior.
6. Build and freeze a new exact MyBoy RC/checksum only after current HEAD CI/static audit is green.
7. Final runtime acceptance belongs to the new RC, not the old test ROM.


### B10 checkpoint after Route 22 early MID (2026-10-22)

The follower prototype remains on `prototype/follower-runtime`, **not on `master`**. The exact previous head `e728c4f` passed Full Gameplay Core run `39822343019` and Follower Prototype run `39822343251`. New technical commit `6df73cb` extends Route 22 early scripted Gary visibility to the MID trigger using a tested seven-tile path restriction; its exact CI must be verified before claiming CI-GREEN. Read the latest dated entry in `NEXT_SESSION.md` and the MyBoy checklist before any further work. The 386-species private ROM builder passes automated checks but deletes the ROM and is not a public downloadable MyBoy artifact. MyBoy visual QA, remaining scripted Gary encounters, integrated master CI and a legitimate deliverable format still require work.



## 2026-10-22 — Cross-block pre-candidate audit (requested before another near-final test ROM)

**Scope:** repository-wide release-readiness triage, not a gameplay change or final audit PASS. At inspection HEAD `313940a4def7cb171bd358d43203de84821cdb82` on `prototype/follower-runtime`, master `8d89f2b444a6e25ef47716861a53f2e4f6920d07`, separate production branch `feature/full-gameplay-core` at `5205ad95b98c4815b7ddcfff4f8ad533b5a04183`. GitHub comparison `master...prototype/follower-runtime`: DIVERGED (150 ahead, 736 behind), with 29 differing files in the comparison; assess merge base and master advances before integration, do not assume a clean fast-forward.

**Do not equate completion of B10 with completion of Full.** Distinguish a disposable private 386-normal/shiny follower diagnostic from a near-final integrated MyBoy candidate. Preserve approved systems, avoid unnecessary gameplay rewrites, and require evidence for each gate.

| Area | Evidence on repository | Assessment for near-final candidate |
| --- | --- | --- |
| Bosses, all 8 Gym leaders, Elite Four, League and Gary team progression | `src/data/trainer_parties.h`, `tools/validate_full_league_rosters.py`, `tools/validate_full_trainer_sets.py` and consolidated Full Gameplay Core CI; current compiled examples include Brock and Champion | IMPLEMENTED and automatically checked, but fresh integrated-head runtime balance/items/AI and full MyBoy acceptance still required; do not reopen approved rosters without evidence of mismatch |
| Second Fighting Dojo and Koichi freeze | Spanish `data/maps/SaffronCity_Dojo/scripts.inc` has `trainerbattle_single` first for sight trigger, post-Sabrina second trial, opposite Hitmon reward and no-room retry; `RC_AUDIT_LOG.md` RC-F041 and event validators | Source fix exists; **MyBoy regression retest still pending** on new candidate |
| Follower for player (general systems) | `src/full_follower.c`, existing run gates, MyBoy exploratory findings in `RC_MYBOY_CHECKLIST.md`; follows player in normal field, but scripted/Gym/League/menu/battle transitions need category-by-category QA | B10 is open. Gary is a special script subset, not exclusive scope; test all leader, Elite Four, NPC, boss, wild, healing, bike/Fly/Surf, save/load, link, OAM/graphics contexts |
| Gary's **own** Squirtle/Wartortle/Blastoise overworld companion | Historical checklist calls it a proposed staged visual and mentions `A-007`, but `DECISION_AMENDMENTS.md` contains only A-001..A-006. `full_follower.c` provides the PLAYER follower and cutscene allowance, not demonstrated independent Gary-NPC companion implementation | **DECISION TRACEABILITY CONFLICT / NOT VERIFIED IMPLEMENTED.** Reconcile actual approval, stage/lifecycle/graphics and dynamic scenes before adding it; do not confuse it with Gary's fixed battle roster |
| Remote Pokémon PC on START menu | `src/start_menu.c` has Pokédex/Pokémon/Bag/Player/Save/Option/Exit etc; no PC entry. No explicit approved PC-from-Start requirement found in current amendments or historical specification inspected | **USER PROPOSAL / NOT IMPLEMENTED.** Define availability (field only, no battle/Safari/link), storage vs item PC scope and safeguards, then seek design decision rather than silently committing a new global feature |
| Legends V2, Mew presentation, rematch leader-specific dialogue, specialty Balls, Pokédex usefulness, postgame training, EV/menu polish and other QoL | A-005/A-006 approved scope and old RC findings in `PROJECT_CONTINUITY.md`; frozen reconciliation pre-dates some polish | **MIXED / NOT FULLY RECONCILED.** Concrete confirmed gap: all eight Gym rematches still share literally identical offer/intro/defeat/after lines in compiled Spanish `data/maps/{PewterCity,CeruleanCity,VermilionCity,CeladonCity,FuchsiaCity,SaffronCity,CinnabarIsland,ViridianCity}_Gym/scripts.inc`, contrary to approved A-005; implement leader-specific text in a scoped later microblock without modifying teams. Continue auditing shops, legendary quests, UI and postgame features; no blanket PASS or blanket NOT IMPLEMENTED without code proof |
| Final integration and packaging | Follower and master are distinct; Full Gameplay Core and Follower Prototype CI on exact predecessor `e728c4f` passed; later Route 22 MID `6df73cb` exact workflows pending during review. Private 386 sprite diagnostic builds and deletes ROM; redistribution and MyBoy delivery constraints remain | Require exact technical CI, adversarial audit, controlled branch integration, integrated HEAD validation, reproducible checksum/private authorized distribution and MyBoy scenario-based acceptance; no final-release claim from build alone |

**Order before a near-final test ROM:** (1) finish current Route 22 MID CI, then reconcile cross-block requirements and approved/unapproved design proposals; (2) group remaining B10 cutscene variants and generic Gym/Elite Four/trainer interaction QA (not just Gary), including 386 sprites/shiny and companion life cycle; (3) audit A-005/A-006 polish, Dojo regression, frozen rosters and other QoL/UI against actual target/master; (4) isolate any required gameplay fixes into small commits with exact Full Gameplay Core/Follower Prototype CI; (5) integrate deliberately and validate the integrated HEAD; (6) produce a legally distributable/authorized MyBoy candidate and test it, with focused Surf fixture and event/save/link checkpoints. PC remote and Gary's own overworld companion are separately tracked design/traceability questions; do not declare them approved simply because discussed.

No fresh MyBoy QA and no source implementation were performed in this audit. No new planning files are needed; this record plus `NEXT_SESSION.md`, `RC_MYBOY_CHECKLIST.md` and existing approved amendments are sufficient for continuity.


## 2026-10-22 — User-intent review: EV UI, natures, conservative inspirations (NO GAMEPLAY EDIT)

This is a cross-block PROPOSAL / DESIGN-AUDIT checkpoint, **not new approved game functionality**. The existing A-005/A-006 decisions and explicit supersessions remain authoritative. Do not infer blanket implementation from CI-GREEN or reintroduce revoked features.

- **Explicitly rescinded:** the proposal to force Oak's Charmander shiny was withdrawn on 2026-10-19; keep ordinary Gen III personality/shiny generation for all three starters. Do not add any forced shiny, shiny-only palette override or special guaranteed odds. `RC_MYBOY_CHECKLIST.md` already preserves the dated withdrawal.
- **Confirmed EV summary gap / user preference:** `src/pokemon_summary_screen.c` already toggles the Skills page with SELECT to display the six actual EV values and total (calculated from party Pokémon, no saved UI copy). However `PrintFullEvValue` still draws a 28-pixel bar per stat via `FillWindowPixelRect`, contrary to the explicitly requested numbers-only, uncluttered presentation. Track a separate UI cleanup to remove bar rendering while retaining values, 6 entries, total and a legible presentation. Do not touch EV gain/party or save data casually.
- **EV cap discrepancy to audit:** the summary prints `MAX. STAT 252 / TOTAL 510`, but `include/constants/pokemon.h` sets `MAX_PER_STAT_EVS 255` and `MAX_TOTAL_EVS 510`, and `src/pokemon.c::MonGainEVs` uses that actual 255 cap. 252 is the final multiple of four relevant for stat gain, not the true Gen III storage/acquisition ceiling. The UI must not mislabel mechanics. Decide whether to display '252 útiles / 255 máximo Gen III', or explicitly approve a behavioral cap change; default is preserve 255/510 and compatibility.
- **New idea / proposed optional feature:** unobtrusive EV milestones at crossing 100, 200 and 252 **effective** EVs in any stat, ideally queued/aggregated after battle or another safe field context, not mid-battle; per-Pokémon/per-stat one-time threshold crossings without new persistent save fields, and no spam after repeated save/load, vitamin/berry/retraining. Must audit actual old/new EV accumulation, party-wide awards, thresholds, trainer/wild battles and space/text before implementing. Not approved; no code change.
- **New idea / proposed visual:** on the Pokémon summary/stats page, subtle upward colored indicator (red) for nature-boosted stat and downward colored indicator (blue) for nature-reduced stat; neutral natures show no markers. Consistent with HGSS style; display only, use existing nature APIs and preserve personality and Gen III calculations. The user described this for a freshly captured Pokémon; opening summary after capture is an appropriate low-friction place, without inserting mandatory capture-dialog popups. No current nature-stat coloring found in `src/pokemon_summary_screen.c` during this audit. Needs text palette/layout/accessibility review and MyBoy.
- **Curated external design inspirations (NOT code-import authorization):** Quetzal's lively overworld presentation and follower idles; HGSS colored nature stats; pokeemerald-expansion configurable summary EV/IV views; careful comparison with high-QoL hacks for concise menus/Pokédex/search/feedback. Prefer Gen III compatibility, single dynamic protagonist companion, no forced newer-gen mechanics, no creep in creature roster or balance. Evaluate asset/source licenses and FireRed architecture before borrowing any implementation. Do not automatically add co-op, Megas, Terastalization, randomizers, cheat menus or mass modern mechanics.
- **Scope safeguards:** cross-check unimplemented A-005 leader identity texts, proposed remote PC-from-START, Gary's own staged companion, 386 followers, boss dialogue/League, visual presentation, classic Kanto immersion and the Dojo MyBoy regression. Continue the cross-block inventory before assembling near-final MyBoy candidate. The recorded A-007 reference for Gary is inconsistent with the amendments file ending at A-006; reconcile approval separately. Do not turn suggestions into decisions solely because they appeared in a conversation.

Next action: verify exact post-doc CI status, then run focused UI/data audit for EV display/nature and compare other approved polish items by source; only implement a reviewed microblock under an explicit approved decision.


## 2026-10-22 — Updated EV milestone and nature-color user direction (SUPERSEDES EARLIER PROPOSALS)

**Current expressed user direction (do not reinstate old 100/200 proposals):**
- **EV summary:** numbers for all six actual EV values and total, without the small per-stat bars/graph. The existing SELECT toggle and the actual EV counts remain. Rendering cleanup is still NOT IMPLEMENTED.
- **EV milestone notification:** ONLY the **252 useful EV** milestone per stat, after a battle awards EVs crossing that effective threshold; **no messages at 100 or 200 EV**. Keep this lightweight and nonblocking. Compare pre-/post-award actual stat EV for each awarded party member, and emit a single grouped postbattle notice only when pre < 252 and post >= 252; do not fire on every later battle, unrelated stat, mere menu open, or loading a save. Multiple recipients/stat milestones in one fight need aggregation and display policy before implementation. If an award jumps from 251 to 254 (Gen III allows 255/stat, 510 total), do not claim the raw counter equals exactly 252: message should state 'alcanzó 252 EV útiles' or equivalent while summary still shows the accurate raw value. **Preserve actual Gen III caps 255/510 and normal Pokémon compatibility; 252 is useful/effective milestone, not storage cap.** This is a now-expressed user UI requirement, subject to technical flow/safety review; it is NOT IMPLEMENTED.
- **Nature boost/reduction indicator:** exact USER direction is **BLUE for stat increased** by nature, **RED for stat decreased**, neutral stats unmarked. Earlier red-up/blue-down description is REVOKED. No arrows, +/-10% annotations or large overlays necessary. Prefer recoloring the existing stat name/value text (or a small colored dot if engine layout makes that safer), on the usual summary/stats screen even after catching a Pokémon; no required capture pop-up or modified nature mechanics. Nature table is already stored internally in `src/pokemon.c` as `sNatureStatTable`; it is static to that module. Exposing effect safely via a narrow read-only accessor or equivalent display-only logic would require separate code audit. **NOT IMPLEMENTED**; needs MyBoy UI/palette checks.
- **External-hack brainstorming:** User found the prior suggestions (Quetzal/HGSS/expansion generic comparisons) underwhelming and did not select any as a change. Do **not** treat those items as approved work or repeatedly promote the same ideas. Only surface thoroughly evaluated, material improvements relevant to classic Kanto/FireRed Full if the user later asks. No external code/art import authorized.

This current dated direction supersedes the earlier 100/200/252 and red-up/blue-down discussion in the preceding audit note. It does not alter independent approved decisions (A-001..A-006), nor reinstate the withdrawn forced-shiny Charmander. Existing B10 and near-final ROM gates remain. **This checkpoint changes documentation only.**


## 2026-10-22 — User-endorsed training / battle UX proposals after six Quetzal screenshots

**Status: USER-PREFERRED / DESIGN AND FEASIBILITY GATE PENDING.** User selected or positively endorsed functionality during UX planning; this is not proof of implementation, CI, or a universal instruction to ship every idea in the imminent near-final RC. No gameplay or UI source was changed. A separate, scoped technical plan is needed for battle input, battle UI, EV trainer map objects, save state and test fixtures. Do not treat source photos as distributable art.

**Player-preferred scope, preserving what was actually said:**

1. **View native EV yield for the current opposing Pokémon while in battle**, not only in its Pokédex entry. Base species EV yield, accurately expressed per stat (e.g. `At. Esp. +1`); distinguish from the actual gain when Pokérus, Macho Brace, Exp Share, recipient roster and total EV caps apply. The Pokédex must also expose yield when appropriately discovered. Avoid extra intrusive screens and do not expose unseen species before discovery.
2. **Optional inspection immediately after capture** of that Pokémon's nature, ability and moves (with the new BLUE boosts/RED drops nature styling), without forced PC travel. Must preserve capture, nickname, party full → storage destination, egg and storage/transfer callbacks; offer skip/cancel.
3. **Pokédex route-by-route completeness**: counts known/captured species by accessible area, do not leak never-seen rare/legendary/plot species; distinguish multiple encounter methods, day/rod/Safari/Altering Cave states when relevant.
4. **Repeatable training trainers in the story and a six-category postgame hub**. Early: Attack and Sp. Attack trainer options around Viridian City / Route 22 for starter training; Route 1 already provides Speed, no need to supplant it. Postgame: six visible NPCs in a row, one per HP, Attack, Defense, Sp. Attack, Sp. Defense, Speed, each providing easy rematches against up to six Pokémon that **all yield EVs only in that assigned stat**, preferably 2–3 yield when canon evolved species are appropriate; no item-based instant grant, no global EV-yield rewrite. Source examples `NIDORAN_M` +1 Attack, `ODDISH` +1 Sp. Attack, `MACHAMP` +3 Attack, `ALAKAZAM` +3 Sp. Attack (checked in compiled species-info). Requires levels/money/XP/replay balance so first-gym challenge isn't trivialized, adequate battle variety, consistent economy and story gate. Specify exact teams, amounts, rematch access and location before implementation.
5. **Postgame objective journal**, tracking real optional goals/quest states without enforcing a linear checklist, revealing future legendary unlocks or changing save structures without audit.
6. **Batch/repeated medicine use** in Bag/party screens, faster healing without skipping actual per-use inventory/HP/PP/status checks.
7. **Major battle registry**, e.g. defeated Gym/Elite Four / Gary encounters and unlocked rematches, reusing existing defeated trainer/flag data when possible rather than duplicating persistent records.
8. **R Poké Ball shortcut in WILD battles** as demonstrated in Quetzal screenshots: a quick-use ball popup at battle action menu; while R is held, left/right cycles through owned ball types, releasing R attempts to throw selected ball, with visible ball type and count; permit safe cancel (e.g. B) before release. Evaluate tap R vs hold separation and reliable held/released transition in MyBoy touch controls; do not consume a ball on accidental input/no item. **Never** enable trainer-battle capture, link battles or incompatible Safari/double/forced/scripted modes. Use normal bag/catch checks and callbacks, with no duplicated bag logic.
9. **Battle healthbox type icon(s)** for both currently visible Pokémon (dual types should not be suppressed or misrepresented; enough GBA VRAM/OAM/layout budget must be measured).
10. **Battle move selection information**: physical/special/status glyph; contact/non-contact information; small '+' if using the move's actual type gains STAB; text color **GREEN for type-super-effective, RED for resisted**, neutral regular, immunity clearly distinct. The user screenshots show these in-context, not an info encyclopedia popup. Read move `gBattleMoves[]` `.type`, `.category`, `.flags & FLAG_MAKES_CONTACT`, Pokémon types and native `gTypeEffectiveness`, not a custom contradictory chart. Handle dual typing / true zero multipliers, status moves, variable types (Hidden Power, Weather Ball etc), target-switch/doubles and potential ability immunities in design; avoid claiming guaranteed damage/effectiveness when abilities/weather/status alter outcome. Prefer eligibility based on actual visible opponent and current move context. The physical/special **split is already in Full**; this proposal is a UI affordance, not request to change mechanics.

**Priority direction:** battle EV yield + readable move info / healthbox type + R shortcut and postcapture details are moment-to-moment QoL; early Attack/Sp. Attack mentors and six-stat postgame training hub plus catch-per-route summary / objectives / major-battle registry are scoped progression content. This expands the cross-block candidate inventory, but is NOT a reason to abandon current critical follower stability/Dojo/combat-difficulty and fixed-story gates.

**Known implementation facts at checkpoint:** `src/battle_controller_player.c::HandleInputChooseAction` uses A/B/D-pad and has no R shortcut; `src/data/battle_moves.h` stores `type`, `category` and `flags`, incl. `FLAG_MAKES_CONTACT`; `include/battle.h` defines `IS_MOVE_PHYSICAL/SPECIAL/STATUS`; `src/battle_main.c` contains `gTypeEffectiveness`; `src/data/pokemon/species_info.h` stores EV yield. These establish feasibility inputs **not completed UX**. Source of screenshot inspiration is user-uploaded images; do not add their images or external code/assets to the repo. Preserve one protagonist follower, normal Gen III saves/links, Spanish ROM target, existing movesets and user-approved teams.

**Still active existing decisions:** 252-useful-EV **only** postbattle milestone (never 100/200); EV numeric UI without bars, nature BLUE increase/RED decrease; rescinded shiny-guaranteed Charmander. Existing remote PC from START is a recorded user preference in the MyBoy checklist, currently not implemented. Do not overwrite the superseded states.

**Next before any implementation:** (1) prioritize user-valued additions versus near-final ROM timing; (2) separate simple display-only pilots from battle-control/save/map systems; (3) independently audit controller command state and field-script/capture lifecycle, possible OAM/VRAM/text layout conflicts, EV recipient rules and save space; (4) propose narrow design where alternatives materially affect gameplay; (5) implement only authorized microblocks with adversarial review, exact gameplay CI and focused MyBoy QA. Continue broad audit; B10 remains open.


### 2026-10-22 — Early EV training correction: no repeatable NPCs before Brock (DESIGN PENDING)

- This supersedes the earlier tentative plan for repeatable Attack / Sp. Attack trainer NPCs around Viridian/Route22 **before Brock**: there is no usual rebattle mechanism at that stage, and user wants wild training instead. Do not implement early repeatable EV trainer NPCs on the basis of previous discussions. The separate six-stat repeatable trainer hub **postgame** remains a distinct favorable idea.
- Source facts checked on the active follower prototype: `src/data/pokemon/species_info.h` grants `MANKEY` +1 Attack, `SPEAROW` +1 Speed (NOT Attack), `RATTATA` +1 Speed, `PIDGEY` +1 Speed, `NIDORAN_M` +1 Attack and `ODDISH` +1 Sp. Attack. A previous user's assumption that Spearow grants Attack was corrected. Preserve normal Gen III EV logic.
- `src/data/wild_encounters.json` FireRed `MAP_ROUTE1` land encounters are only Pidgey/Rattata (all +1 Speed), **so Route 1 should stay unchanged**. FireRed `MAP_ROUTE22` has 12 encounter slots: 45% Rattata + 45% Mankey + 10% Spearow (using declared slot rates of 20/20/10/10/10/10/5/5/4/4/1/1 percent). No Nidoran♂ currently appears in that Route22 table. The least disruptive high-purity candidate is replacing only the five Rattata slots with Mankey, yielding **90% Mankey (+1 Attack) / 10% Spearow (+1 Speed)** and retaining early Spearow obtainability; **not fully pure** Attack. 100% Attack would require removal/replacement of Spearow with Mankey or another Attack-yielder and has greater Pokédex/biome consequences. These are OPTIONS, not approved modifications.
- User wants a pre-Brock **localized Sp. Attack encounter area**, likely Oddish (native +1 Sp. Attack), without replacing Viridian Forest's original forest species. `src/wild_encounter.c::GetCurrentMapWildMonHeaderId` selects grass encounters by map group/number, not by the exact grass patch; merely placing a patch of grass on Route2 or Viridian Forest does not grant its own species table. Options: a small independently mapped forest clearing (new map/connector/event assets with dedicated 100%-Oddish table), or a tightly bounded position/tile-aware special encounter override with stronger engine audit. A blanket change to all of Viridian Forest or all Route2 is NOT recommended just to get a small Oddish training patch. Adding catchable pre-Brock Oddish also advances availability of a Grass Pokémon and may affect Brock's challenge; evaluate that before approving.
- No gameplay/map/encounter data changed in this checkpoint. **Design decision pending:** preserve early species by favoring Route22 90/10, and compare the safest localized Oddish-area implementation plus its progression impact; obtain user preference for meaningful tradeoffs before technical edit. Maintain exact Full Gameplay Core and Follower Prototype validation for any later data/maps/runtime change.


### 2026-10-22 — Pre-Brock encounter distribution revised by user (decision on female Nidoran pending)

- User's updated concept **SUPERSEDES** prior 90% Mankey / 10% Spearow candidate and previous pre-Brock repeatable trainer proposal: move Spearow from Route22 to Route1, retaining Pidgey and Rattata; Route22 should show Mankey plus male/female Nidoran, with female rare, and post-Brock original Nidoran area should favor females; at a discrete grassy area near the non-battling boy on the **right of the SOUTH entrance** to Viridian Forest, make a dedicated Sp. Attack encounter spot with Oddish; user asks whether Bellsprout can share it.
- **Confirmed actual EV yields in `src/data/pokemon/species_info.h`:** Mankey +1 Attack; Nidoran♂ +1 Attack; Nidoran♀ **+1 HP, not Attack**; Oddish +1 Sp. Attack; Bellsprout **+1 Attack, not Sp. Attack**; Spearow, Pidgey, Rattata +1 Speed. Cannot honestly deliver 'Route22 only Attack' when including Nidoran♀, nor 'Oddish+Bellsprout only Sp. Attack' without modifying canonical yields (NOT recommended). Do not silently change EV yields.
- Current FireRed encounter percentages (source `src/data/wild_encounters.json`, 12 land slots): Route1 Pidgey 50%, Rattata 50%; Route22 Mankey 45%, Rattata 45%, Spearow 10%; Route3 Nidoran♂ 14%, Nidoran♀ 1%. LeafGreen Route3 already reverses those to ♀14% / ♂1%. A feasible, low-impact candidate Route1 45% Pidgey, 45% Rattata, 10% Spearow (reassign two 5%-rate slots); Route22 **OPTION A** 70% Mankey / 25% Nidoran♂ / 5% Nidoran♀ (95% Attack EV encounters and 5% HP), or **OPTION B** ~70% Mankey / 30% Nidoran♂ (100% Attack but no Nidoran♀ before Brock in this map; retain/buff female Route3). User choice between A and B **not yet resolved**. If choosing Route3 female-dominant distribution, retain access to male Nidoran via Route22 and audit FireRed vs LeafGreen identity / catchability.
- Viridian Forest source map has a NON-TRAINER `ViridianForest_EventScript_Boy` at (45,58), near the south-east clearing, while `ViridianForest_EventScript_Youngster` at (29,58) is also non-trainer; item at (49,60). This grounds the user-described right-side space. Existing standard land encounter table is per map, so a localized only-Oddish patch requires either an independently mapped clearing or a safely bounded coordinate/tile-based exception. Preserve other native Forest encounter slots, trainers, paths, warp/QuestLog, save/capture, follower and Pokédex route counts; survey collision/tile geometry before deciding architecture.
- **Proposed forest composition:** Oddish only (100% +1 Sp. Attack). Bellsprout would spoil the pure Sp. Attack zone and can remain in its original later locations; any special early appearance/encounter method requires a separate explicit design choice. This proposal intentionally makes catchable Oddish available before Brock, impacting challenge/obtainability and requiring team/progression audit.
- This is a **recorded user proposal, not a finalized implementation design**. User must resolve genuine Attack-purity vs female-Nidoran-availability tradeoff before modifying encounter tables, plus authorization of the small forest zone. No gameplay, map, encounter data or workflow modified. Technical implementation if approved requires Full Gameplay Core and Follower Prototype exact CI, independent encounter probability/area regression tests, optional targeted MyBoy smoke. Keep postgame six-NPC EV hub distinct.


### 2026-10-22 — Pre-Brock encounter commit and cross-map rarity / NPC trade audit

**Technical implementation:** `0a3d02613a241c0265c2b16b4f57cb5fe136f806` on `prototype/follower-runtime` changes exactly `sRoute1_FireRed` to Pidgey 35% / Rattata 35% / Spearow 30% (+1 Speed all), and `sRoute22_FireRed` to Mankey 55% / Nidoran♂ 45% (+1 Attack all), preserving their low levels, the existing native wild encounter system and all LeafGreen table variants. Technical scope: `src/data/wild_encounters.json`, an explicit semantic check in `.github/workflows/full-gameplay-core.yml`, and the exact audited blob SHA in `tools/validate_audited_data_blobs.py`. No maps, save/link structures, baseline historical 21-map gate or encounter logic changed. This supersedes earlier 90/10 or Nidoran♀ Route22 proposals. Exact technical Full Gameplay Core `39849932055` SUCCESS; Follower Prototype `39849932247` was still IN_PROGRESS during checkpoint. No MyBoy QA; no master integration.

**Audit scope across map encounter methods:** the current FireRed encounter data include land, surfing water, rock smash and Old/Good/Super Rod fishing tables. Computed per-species probabilities using each method's slot weights and each map; **49 distinct map/method/species occurrences at exactly 1% representing 14 species** (10 land, 35 Super Rod, 4 surfing water). This is not 49 globally rare species. Many have more accessible alternate floors, routes or methods and should not all be raised blindly (e.g. Psyduck multiple 1%-rod entries but common elsewhere; Haunter 1% Pokémon Tower 3F, much more common on other floors; Lapras 1% optional Icefall Cave water and a story gift; Dragonair 1% Safari Super Rod but obtainable via Dratini evolution). Most 5% encounters are not automatically defects either. Protect version identity, legal 386 obtainability and original progression.

**Genuinely high-friction early-game candidates found:**
- `sRoute3_FireRed`: current Nidoran♂ 14%, Nidoran♀ 1%. User wants female distinctly discoverable rather than 1%, at least as likely as male after Brock. Candidate **Nidoran♀ 14%, Nidoran♂ 11%**, retaining all original Route3 species by reallocating existing slot #5 (10% Pidgey→♀), #8 (4% male→♀), #10 (1% female→♂): final Spearow 35%, Pidgey 20%, Mankey 10%, Jigglypuff 10%, Nidoran♀ 14%, Nidoran♂ 11%. Avoid changing LeafGreen until separately justified; Route22 now provides plentiful male Nidoran.
- `sMtMoon1F_FireRed`: Clefairy 1%, Paras 5%, Geodude 25%, Zubat 69%. Candidate Clefairy **9%** using two distinct 4%-weight Zubat slots, retaining Paras and Geodude and leaving Zubat 61%; rare but far less frustrating. `sMtMoonB2F_FireRed`: Clefairy 6%; optional modest bump to **10%** by changing a single 4% Zubat slot. Do not automatically modify other odd/evolved/optional 1% species without checking alternative access. Exact final rates and FireRed scope are suggestions grounded in slot arithmetic, not yet implemented or approved as a frozen specification.
- The Forest `MAP_VIRIDIAN_FOREST` non-battling boy at (45,58), near the southeast SOUTH entry, is the user's preferred Oddish-only Sp. Attack patch. Native encounter table is whole-map; the original forest must remain unchanged outside the selected area. Any scoped tile/coordinate patch requires examining the map binary and tile grass/collision behavior, full trainer/item/warp/field follower route. Alternatively tiny own-map clearing has extra map/warps. **Not implemented yet**; Oddish +1 Sp. Attack, Bellsprout +1 Attack and unsuitable. Natural pre-Brock Oddish availability must be deliberately reviewed versus Brock challenge.
  
**NPC trade audit of current FireRed `src/data/ingame_trades.h` (9 entries, no modifications):** Abra→Mr. Mime, Poliwhirl→Jynx, Nidoran♂→Nidoran♀, Spearow→Farfetch'd (Stick held), Nidorino→Nidorina, Golduck→Lickitung, Raichu→Electrode, Venonat→Tangela (Stardust held), Ponyta→Seel. Other rewards retain fixed personality, imperfect IV spreads, OTs, nicknames and item/mail metadata. Stage-by-stage assess how readily each requested Pokémon can be obtained, whether reward gives meaningful Pokédex/evolution/battle utility rather than asking for a harder-to-get or evolved mon, whether dialogue accurately previews the exchange, and the effect of our early Spearow and Nidoran♂ accessibility; e.g. Raichu→Electrode and Nidorino→Nidorina are candidates for scrutiny, not proven defects. Do NOT replace all trades or change trade code, personality/OT generation, national access or link ABI without explicit design reconciliation. Ingame NPC trades are distinct from live link trades.

**Next microblock:** verify exact Follower Prototype CI `39849932247`; then independently implement the narrow Route3/Mt Moon rarity correction if accepted after scope review, or audit Forest binary grass-area feasibility. Stage NPC-trade-by-NPC improvement proposal after validating where NPCs are located and when species become obtainable. Persist in existing docs; do not start a monolithic world encounter rewrite.


### 2026-10-22 — Corrected FireRed Route 3 and Mt Moon rare encounters (follow-up microblock)

- Completed separately from the earlier Route1/Route22 EV-pure microblock. Technical commit `fdf710c116d4bb6a347f7a81caf3cb62b2b22996` changes only the FireRed `sRoute3_FireRed`, `sMtMoon1F_FireRed` and `sMtMoonB2F_FireRed` entries in `src/data/wild_encounters.json`. Updates corresponding semantic rate checks in existing Full Gameplay Core gate and exact `src/data/wild_encounters.json` audited SHA in `tools/validate_audited_data_blobs.py`; the historical frozen-change manifest remains untouched. No other encounter maps, map scripts, Pokemon EV yields, save/link fields, trades or input changed.
- **New exact land-encounter probabilities**: Route3 FireRed Spearow 35%, Pidgey 20%, Mankey 10%, Jigglypuff 10%, Nidoran♀ 14%, Nidoran♂ 11% (before ♀1% / ♂14%). MtMoon 1F Zubat 60%, Geodude 25%, Paras 5%, Clefairy 10% (before 1%). MtMoon B2F Zubat 45%, Geodude 30%, Paras 15%, Clefairy 10% (before 6%). Clefairy new 1F slots remain levels 8–10. All baseline species remain catchable; LeafGreen encounter tables unchanged. Both 1% basic-species pain points addressed without systematically rewriting every rare encounter.
- **Exact predecessor CI** on `0a3d02613a241c0265c2b16b4f57cb5fe136f806`: Full Gameplay Core run `39849932055` SUCCESS and Follower Prototype run `39849932247` SUCCESS. New technical `fdf710c` Full Gameplay Core run `39851490790` and Follower Prototype run `39851490652` were IN PROGRESS at documentation checkpoint; **not yet validated / CI-GREEN** for the new code until the exact jobs are confirmed.
- **NPC trade triage** (nine FireRed offers; data in `src/data/ingame_trades.h`) remains proposal-only: Abra→Mr.Mime, Poliwhirl→Jynx, Nidoran♂→Nidoran♀, Spearow→Farfetch'd, Nidorino→Nidorina, Golduck→Lickitung, Raichu→Electrode, Venonat→Tangela, Ponyta→Seel. Early Spearow and male Nidoran now make Farfetch'd and female-Nidoran offers simpler, while Route3 female availability reduces the incentive to trade Nidoran. Potential low-value demands (Raichu→Electrode, Nidorino→Nidorina) need site-specific offer/availability audit, not automatic replacement. Consider enhancing fixed-IV competitive utility or item presentation only after checking species/flag economy, all nine NPC scripts, save/link and story progression.
- **Pending forest design**: protect user-chosen southeastern Viridian Forest non-trainer boy (45,58), south entrance, as 100% Oddish +1 Sp. Attack _inside a precisely delimited grass patch_, without altering standard forest encounters elsewhere. Examine 54×69 map.bin grass metatiles/collision and field encounter callbacks or separate tiny clearing before technical edit. Bellsprout +1 Attack stays excluded. Preserve NPC and nearby Potion event, warps and follower. If a new map is unavoidable, require intentional layout approval rather than silently constructing a new forest area.
- Other 1% encounter cases are triaged by **global attainability and alternative map/method**; 49 distinct 1%-probability map/method occurrences (14 species) are not 49 unavailable species. Leave optional evolved/alternative-sourced rarities at original rates unless individual playability audits justify changes. The near-final candidate, follower B10, MyBoy acceptance and integration to master remain incomplete.
