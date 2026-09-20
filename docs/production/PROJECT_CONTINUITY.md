# Pokémon Rojo Fuego Full v1.0 — Project Continuity

**Purpose:** make the repository sufficient to resume the project without relying on any previous chat.

## 1. Start here in every new session

Before modifying code:

1. Read this file.
2. Read `docs/production/DECISION_AMENDMENTS.md`.
3. Read `docs/production/RC_AUDIT_LOG.md`.
4. Read `docs/production/FINAL_AUDIT_PLAN.md`.
5. Read `docs/production/RC_MYBOY_CHECKLIST.md`.
6. Inspect the current branch HEAD and latest GitHub Actions result.
7. Only if a design detail is still needed, consult the frozen sources under `docs/spec/`.

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
- Baseline commit: `e184c5cf898cd29efbd33bc1bfe5994277e21ab`.
- Production target: `firered_es_modern`.
- Baseline Spanish SHA-1: `ab8f6bfe0ccdaf41188cd015c8c74c314d02296a`.

## 5. Current technical state at continuity freeze

The latest code-affecting RC audit commit currently recorded is:

- `48ca26236b1f55c495a57fc4ece54481f9eccc1a` — makes Gary's Oak's Lab starter identity explicitly Squirtle for every player-starter choice. Earlier recovery commits also fix doubles-AI history aliasing/OOB behavior, direct-use trade-item evolutions, unique reusable TM transactions and vanilla-save migration.

Later commits through the current continuity update are documentation-only unless explicitly noted otherwise.

The consolidated workflow for the code-equivalent RC state completed **SUCCESS**. It covered:

- Spanish modern ROM build;
- physical/special split and split-aware AI;
- modern category/contact data;
- direct trade-item evolutions;
- field QoL;
- Move Reminder and tutor pricing;
- legendary/mythical event levels;
- reusable unique TMs;
- approved encounter rates;
- frozen Gary/boss rosters;
- RC freeze validator;
- full trainer legality validator;
- ROM checksum.

Last recorded ROM SHA-1 for that code payload:

`a47a1e8cfa4683789ea9383a5c2438316e09d759`

## 6. RC audit findings repaired so far

See `RC_AUDIT_LOG.md` for full details. Key repaired findings include:

- sequential-roamer Pokédex mapping;
- Celebi trigger placement;
- missing MOV-006 full trainer-set legality validator;
- missing QOL-009 EV summary view;
- Resort Gorgeous payout identity;
- Move Reminder scroll-indicator bug;
- L=A held-repeat bug;
- two-slot party animation buffer leak;
- direct trade-item evolution UI route;
- missing ECO-004 berry economy and Emerald-style EV-reducing berry behavior;
- missing consolidated freeze validator;
- stale historical QA references to mGBA/142-slot bag;
- explicit save layout/migration RC gates;
- explicit vanilla Gen III ID-space gates;
- explicit frozen economy/postgame-stock gates;
- hardened Gate 6 persistent event-state coverage;
- hardened Gate 7 one-save obtainability coverage;
- exact audited-blob locks for five high-risk gameplay data files.

## 7. Important automatic validators

### `tools/validate_full_trainer_sets.py`
Last known PASS:
- 34 Full parties;
- 163 Pokémon;
- 632 custom moves;
- validates species, level, IV, held item and move legality including level-up, TM/HM, tutor, egg and pre-evolution learnability.

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

After app-side forced closures on 2026-09-20, the repository was re-read from GitHub before further changes. The branch history was intact. The audit documentation had lagged behind the code, so the state was reconciled. RC-F022 and RC-F023 are now statically hardened and awaiting CI confirmation; RC-F024 records and fixes an additional Gate 7 validator blind spot discovered during recovery. Subsequent audit blocks found and fixed RC-F025 (vanilla-save migration invocation), RC-F026 (unique reusable TM transaction consistency), RC-F027 (missing direct-use trade-evolution item effects), and RC-F028 (doubles-AI history aliasing/OOB behavior identified during Gate 2A external-reference review), and RC-F029 (Gary's Oak's Lab starter identity still varying despite fixed Squirtle battle parties).

The exact current branch HEAD must still be checked by CI before any RC freeze. No MyBoy final acceptance result should be inferred from static validation.

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
