# Next Session — Pokémon Rojo Fuego Full v1.0

Resume the project from the repository, not from chat memory.

## Required first reads

Read, in this order:

1. `docs/production/PROJECT_CONTINUITY.md`
2. `docs/production/DECISION_AMENDMENTS.md`
3. `docs/production/RC_AUDIT_LOG.md`
4. `docs/production/FINAL_AUDIT_PLAN.md`
5. `docs/production/RC_MYBOY_CHECKLIST.md`
6. `docs/production/SECOND_PASS_AUDIT.md`

Only consult `docs/spec/` when a frozen design detail is needed.

## Active branch handoff — follower runtime (2026-10-19)

If resuming the approved follower prototype, use branch `prototype/follower-runtime` and read `docs/production/RC_MYBOY_CHECKLIST.md`, section **Follower prototype — current corrective roadmap**. Verify branch/HEAD first; the last technical commit is `0dc16af7de44fcc5479576599858455ec8e20904` (guard against dynamic follower ID 254 NPC-script lookup), and the roadmap was recorded by docs-only commit `5e4ca95`. Technical guard `0dc16af` is IMPLEMENTED but not MyBoy-confirmed. The 2026-10-19 follower CI runs on `0dc16af`, `5e4ca95`, `50f37e2` failed at compile because `field_control_avatar.c` omitted `full_follower.h` (`OBJ_EVENT_ID_FULL_FOLLOWER` undeclared). Corrected by technical commit `6a6b4afc587352a536810f4f05963c269f7d46c8`. Follower Prototype run `39325607382` for that exact technical SHA was **IN PROGRESS when recorded**, not yet a PASS; recheck its final result before advancing. Current action: verify successful build and audit full script lookup coverage, then implement A-button friendship-tier dialogue in an isolated microblock. `GetLeadMonFriendship` is NOT suitable without changing lead selection: it includes fainted first-slot Pokémon while the follower uses the first alive, non-egg species. The user has stopped manual exploratory play: five of six checks done, Surf deferred to test fixture; do not request further story progression or repeat the known crashing A-interaction on the old ROM. Proceed through save/load restoration, contextual visibility, movement/presentation polish, exact technical CI, bundled new ROM/MyBoy regression, integration gates. Do not mistake the general RC audit section below for the next action on this follower branch.

## Current phase

The project is in **Release Candidate final audit**, not broad implementation.

The branch has received additional code-affecting audit fixes after the last historically validated payload. Do **not** inherit an older CI PASS or ROM checksum. Confirm the exact current HEAD and its consolidated workflow result before any RC freeze.

## What to do next

Continue the **exhaustive final audit** in `FINAL_AUDIT_PLAN.md`.

Priority:

1. finish the remaining first-pass static sweep;
2. continue the independent second-pass audit in `SECOND_PASS_AUDIT.md`;
3. verify target-language/compiled-path correctness and semantic baseline diff coverage;
4. correct any real implementation or validator defects found;
5. keep `RC_AUDIT_LOG.md` and `PROJECT_CONTINUITY.md` synchronized;
6. require exact current HEAD consolidated CI green;
7. freeze one reproducible RC ROM + SHA-1 only after that green result;
8. execute the final MyBoy runtime checklist on that exact ROM.

Do **not** ask the user to repeat earlier decisions or reconstruct deleted chats.

## Approved workflow

- Advance autonomously and meticulously.
- Do not return to repeated user-run tests after every small fix.
- Use CI/static inspection during audit.
- Reserve manual MyBoy testing for final RC acceptance or a runtime-only defect that cannot otherwise be resolved.
- Do not declare v1.0 final from compilation alone.
- Do not merge/tag final until the exact tested RC passes the final acceptance gates.

## Critical amendments

- MyBoy, not mGBA, is the required runtime QA environment.
- Normal Items pocket remains vanilla 42 slots; never restore the abandoned 142-slot bag.
- Chats are disposable; GitHub is the continuity authority.
