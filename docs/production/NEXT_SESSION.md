# Next Session — Pokémon Rojo Fuego Full v1.0

Resume from the repository, never from chat memory.

## Read first

1. `docs/production/PROJECT_CONTINUITY.md` — section 0 is the live resume point.
2. `docs/production/REPOSITORY_GUARDRAILS.md`.
3. `docs/production/DECISION_AMENDMENTS.md` — especially A-013.
4. `docs/production/POLISH_IMPLEMENTATION_MATRIX.md`.
5. Inspect live refs, exact HEADs and Full Gameplay Core evidence for the SHA being advanced.

Use `docs/spec/` only for frozen historical design details.

## Current state

- Canonical repository: `joseiturriaga25amz/pokefirered-europe`.
- Integration branch: `master`.
- Last production block **CLOSED on master**: **B8 — Signature Pokémon staging**.
- B8 master checkpoint: `28f42346916bf9d19c558ce4ce19fb849f5b6e33`.
- B8 post-integration Full Gameplay Core **#617: SUCCESS**.
- Active branch: `design/leader-roster-research`.
- Brock reconciled HEAD: `ccc85275d5954d48673fb7694c7379f1cc54e186`.
- Brock Full Gameplay Core **#618: SUCCESS**.
- Brock is **IMPLEMENTED + VALIDATED + CI-GREEN, NOT YET CLOSED** until merged and the resulting master HEAD is green.
- A-013 defines the reusable Gym Leader review/implementation procedure.

## Exact next action

1. integrate the exact Brock branch into current `master`;
2. verify Full Gameplay Core on the exact resulting master HEAD;
3. record Brock **CLOSED**;
4. then begin **Misty** analysis using A-013;
5. keep Elite Four and Gary/Blue research deferred until the Gym Leader pass is complete;
6. resume B9 only after the explicitly interposed leader-roster pass.

## Continuity rule

No new generic continuity/backlog/handoff file is needed. Project continuity lives here and in `PROJECT_CONTINUITY.md`; approved decisions live in `DECISION_AMENDMENTS.md`; the production work order lives in `POLISH_IMPLEMENTATION_MATRIX.md`.

MyBoy remains the required final runtime acceptance environment.
