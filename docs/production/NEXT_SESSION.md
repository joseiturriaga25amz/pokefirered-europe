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
- Brock feature/documentation HEAD: `3d357df82120b779213b4fc5e8b9c56eb86ae1f1`.
- Brock feature Full Gameplay Core **#619: SUCCESS**.
- Brock merged master checkpoint: `269d75b501a99c92fd8296189760899a6a5d4571`.
- Brock post-integration Full Gameplay Core **#620: SUCCESS**.
- Brock original roster microblock: **CLOSED**.
- Brock second-pass feature HEAD: `12b244fd3b1f87b8b653fd6aaaa3d21b53c967f2`.
- Brock second-pass Full Gameplay Core **#631: SUCCESS**.
- Brock second-pass merged master checkpoint: `193b14aa3e5426dbf6049efa32a6d7c2c4d0d050`.
- Brock second-pass post-integration Full Gameplay Core **#632: SUCCESS**.
- Brock second-pass tuning microblock: **CLOSED**.
- A-013 defines the reusable Gym Leader review/implementation procedure.
- Misty feature HEAD: `4c8d16bcf7878960b6dd5f7ffb5ee44c5ff2adf7`.
- Misty feature Full Gameplay Core **#624: SUCCESS**.
- Misty merged master checkpoint: `323ff3daef5e8019690cda83c4527b5ec07ff3c1`.
- Misty post-integration Full Gameplay Core **#625: SUCCESS**.
- Misty roster/identity microblock: **CLOSED**.
- Misty second-pass feature HEAD: `a06ac70b39e3d4736de86a3680ffb0ffda1d079b`.
- Misty second-pass Full Gameplay Core **#635: SUCCESS**.
- Misty second-pass merged master checkpoint: `08bbd40374850595bc8261b1ab44ebae2012aa35`.
- Misty second-pass post-integration Full Gameplay Core **#636: SUCCESS**.
- Misty second-pass tuning microblock: **CLOSED**.
- Lt. Surge feature HEAD: `2bb74e404511e3e4b04a29d283c99b6d23a72e9d`.
- Lt. Surge Full Gameplay Core **#639: SUCCESS**.
- Lt. Surge merged master checkpoint: `27dc2ff8a99fb5d9c5135ef39e02670b2ca08196`.
- Lt. Surge post-integration Full Gameplay Core **#640: SUCCESS**.
- Lt. Surge prior roster/tuning closure remains historical evidence.
- Lt. Surge third-pass feature HEAD `32163f2677e4012032cce1070165b103f64a2ca5`: Full Gameplay Core **#642 SUCCESS**.
- Merged to `master` as `fb9bf7caec094b451cd6bb61b1752a142adb4d78`; post-integration Full Gameplay Core **#643 SUCCESS**.
- Lt. Surge third-pass curve microblock: **CLOSED**.
- Erika roster/curve microblock is **IMPLEMENTED** on `fix/erika-curve-identity`, pending exact-head validation and integration.

## Exact next action

1. validate the exact Erika feature HEAD with Full Gameplay Core;
2. if green, integrate only that exact HEAD to `master`;
3. run Full Gameplay Core on the exact integrated master SHA;
4. persist Erika closure evidence and only then move to Koga analysis.

## Continuity rule

No new generic continuity/backlog/handoff file is needed. Project continuity lives here and in `PROJECT_CONTINUITY.md`; approved decisions live in `DECISION_AMENDMENTS.md`; the production work order lives in `POLISH_IMPLEMENTATION_MATRIX.md`.

MyBoy remains the required final runtime acceptance environment.
