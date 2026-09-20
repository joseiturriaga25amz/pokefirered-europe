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
