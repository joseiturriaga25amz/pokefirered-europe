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
- Porygon prize remains repeatable; A-008 changes final price/presentation to 5,500 coins / localized 5.500 FICHAS.

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


## 2026-09-24 — follower/provenance and polish checkpoint

Repository-only continuation was performed from the production documents, not from chat memory.

### New production documentation

- `docs/production/FOLLOWER_TECHNICAL_RESEARCH.md`
  - upstream inspected: `monhacks/arrantemerald` branch `followers-expanded-id`;
  - bulk HGSS follower asset provenance traced to veekun/HGSS extraction;
  - no repository-wide license grant found for upstream follower code/assets;
  - external 386/440-sprite set is not treated as redistribution-cleared;
  - conservative FireRed architecture defined without 16-bit graphics IDs or save/link structure growth.
- `docs/production/POLISH_IMPLEMENTATION_MATRIX.md`
  - maps A-005/A-006 into production work packages P-01 through P-08;
  - explicitly records that current Celio Mystic/Aurora distribution is pre-A-005 behavior and must be replaced.

### Isolated follower prototype

Branch: `prototype/follower-runtime`

Green compile checkpoint:
`6b7fd84ecdc02eb188721dd4526c2e853a43859f`

Actions run:
`36013304188` — PASS.

The prototype:
- uses only existing Full-native Pokémon overworld assets;
- keeps generic object graphics IDs 8-bit;
- does not modify Pokémon/BoxPokemon/SaveBlock/link serialization;
- is excluded from link-map initialization;
- remains blocked from production pending MyBoy runtime + Save/Link QA.

### RC policy

The ROM SHA-1 `a1c7fa573ac784ef089bfdf966aa38fc84861212` remains historical runtime evidence only. It is not a final candidate.

Do not generate or label a replacement final RC until:
1. approved A-005/A-006 production polish is implemented;
2. validators and MyBoy checklist reflect the new truth;
3. follower is either MyBoy-approved for integration or explicitly excluded from v1.0;
4. exact-HEAD CI is green;
5. the replacement RC is frozen by Git SHA + ROM SHA-1 and receives the required runtime suite.


## 2026-09-24 — production order locked after Drive/runtime reconciliation

Drive evidence document reviewed:
`Pokemon Rojo Fuego Full v1.0 — Evidencia Runtime RC`.

The remaining work is now intentionally split into small production blocks B0–B12 in `POLISH_IMPLEMENTATION_MATRIX.md`. This supersedes any vague “implement all polish at once” interpretation.

New approved decision:
- A-007 adds fixed signature Pokémon beside the 8 Gym Leaders, Elite Four and Gary/Blue.
- This is not the player follower system; it is controlled map/event presentation.
- Required signature mapping and QA constraints are recorded in `DECISION_AMENDMENTS.md`.
- Missing trainer-signature sprites are a bounded asset problem (~13 identities) and should be used as a safe sprite/OAM pilot before universal follower coverage.

Operational rule:
- complete one B-block at a time;
- end each block with build/static validation and documentation;
- do not generate replacement RC until B11;
- Drive remains the manual MyBoy/runtime evidence record;
- GitHub remains the implementation/continuity authority.


## 13. Chat/resource management and handoff protocol

This is a **project rule**, not a chat-memory preference.

### Workload sizing

To reduce forced chat/tool interruptions:

- do not run repository research, compilation review, audit, mutation and long-form reporting as one monolithic operation;
- split technical work into bounded units: **locate → inspect → change → validate → record**;
- prefer targeted file/range inspection over oversized repository dumps;
- keep modifications small enough to be reviewable and reversible;
- finish each coherent unit with a Git checkpoint and concise state note before starting the next;
- split large textual audits/specifications into prudent sections instead of producing or ingesting them in one oversized pass;
- avoid repeating already-recorded repository context in chat when GitHub documents are authoritative.

### Chat rotation

The assistant must actively watch for signs that the current conversation is becoming unsafe to continue efficiently, including:

- repeated long tool traces or large repository outputs;
- several major implementation/audit blocks accumulated in one chat;
- signs of context pressure, truncated tool output or prior forced-stop risk;
- a natural project checkpoint where continuing in a fresh chat would reduce risk without losing momentum.

When that point is reached, **tell the user proactively before a forced closure occurs**.

Before recommending a new chat:

1. finish or safely checkpoint the current atomic subtask;
2. commit/document the exact repository state;
3. update this continuity file or the relevant production handoff document if project truth changed;
4. provide the user with a ready-to-paste continuation prompt containing:
   - repository name;
   - active branch;
   - exact HEAD;
   - current B-block/subblock;
   - completed work;
   - open gate/failure, if any;
   - exact next action;
   - instruction to read PROJECT_CONTINUITY.md and authoritative production docs first;
   - reminder not to reconstruct state from old chat text when repository truth exists.

Do not rotate chats merely because a response is long. Rotate when continuity risk becomes materially higher than the cost of starting fresh.

### Continuation-prompt template

Use this structure and fill it with the current exact state:

> Continuamos el proyecto Pokémon Rojo Fuego Full v1.0.
> 
> Repositorio: `joseiturriaga25amz/pokefirered-europe`
> Rama activa: `<branch>`
> HEAD exacto: `<sha>`
> Bloque actual: `<B-block/subblock>`
> 
> Antes de modificar nada, lee `docs/production/PROJECT_CONTINUITY.md` y los documentos de producción que allí se indican. GitHub es la autoridad de continuidad; no reconstruyas el estado desde el chat anterior.
> 
> Estado cerrado: <summary>
> Gate/fallo abierto: <summary or none>
> Siguiente acción exacta: <next action>
> 
> Mantén el protocolo de trabajo en bloques acotados: localizar → inspeccionar → cambiar → validar → registrar. Evita operaciones monolíticas y textos/auditorías excesivamente grandes en una sola pasada.


## 14. 2026-09-24 B0 runtime-evidence reconciliation

The external Drive runtime evidence was re-read specifically for post-freeze approvals that had not yet been promoted into repository authority. A-008 now makes the following B1 rules repository-authoritative: UI-001 EV layout repair, UI-002 visible move category, Porygon 5,500/aligned presentation, vending quantity selector, badge-gated Oak aides, National Dex without the 60-capture quota, HM item+badge field licenses with forgettable learned HMs, and vanilla held-item Exp. Share behavior.

These are no longer Drive-only decisions. B1 must implement against A-008 and update validators/runtime checks accordingly.
