# Next Session — Pokémon Rojo Fuego Full v1.0

Resume from the repository, never from chat memory.

## Read first

1. `docs/production/PROJECT_CONTINUITY.md` — section 0 is the live resume point.
2. `docs/production/REPOSITORY_GUARDRAILS.md`.
3. `docs/production/DECISION_AMENDMENTS.md`.
4. `docs/production/POLISH_IMPLEMENTATION_MATRIX.md`.
5. Inspect live refs, exact HEADs and the Full Gameplay Core result for the SHA you intend to advance.

Use RC audit/checklist documents only when the active block or release gate requires them. Use `docs/spec/` only for frozen historical design details.

## Current state

- Canonical repository: `joseiturriaga25amz/pokefirered-europe`.
- Integration branch: `master`.
- Last block **CLOSED on master**: B7.
- B7 merge checkpoint: `8b6502e7233f51b9ca19529479a7055a21261391`.
- B8 branch: `feature/b8-signature-pokemon-staging`.
- B8 current HEAD: `52ed97e6f20cad11903bcce1deda46400ae37ee9`.
- B8 status: **IMPLEMENTED + VALIDATED + CI-GREEN, NOT YET CLOSED**.
- B8 exact-head Full Gameplay Core: run `36643089722` — **SUCCESS**.
- Detailed B8 checkpoint: `docs/B8_CONTINUITY_CHECKPOINT.md` on the B8 branch.
- `fix/b8-misty-pool-ambience` is historical/diverged and is not the resume branch.

## Exact next action

After the documentation/CI consolidation is merged to `master`:

1. reconcile B8 with the new exact master HEAD without expanding its approved gameplay scope;
2. rerun Full Gameplay Core on the resulting exact B8 HEAD;
3. if green, merge B8 into `master`;
4. verify the merged master HEAD and record B8 **CLOSED**;
5. only then open B9 — Pokédex usefulness.

Do not start B9 in parallel and do not reopen the separate battle-roster research during B8 closure.

## Continuity rule

No new generic continuity/backlog/handoff file is needed. Project continuity lives in `PROJECT_CONTINUITY.md`; approved decisions in `DECISION_AMENDMENTS.md`; approved work in `POLISH_IMPLEMENTATION_MATRIX.md`. Record block-local ideas as **PROPOSED / pending decision** in an existing relevant checkpoint/work-order section, not as approved decisions.

MyBoy remains the required runtime acceptance environment.
