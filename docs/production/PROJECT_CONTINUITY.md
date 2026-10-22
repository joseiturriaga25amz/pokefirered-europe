# Pokémon Rojo Fuego Full v1.0 — Project Continuity

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
