# Next Session — Pokémon Rojo Fuego Full v1.0

Resume the project from the repository, not from chat memory.

## Required first reads

Read, in this order:

1. `docs/production/PROJECT_CONTINUITY.md`
2. `docs/production/DECISION_AMENDMENTS.md`
3. `docs/production/RC_AUDIT_LOG.md`
4. `docs/production/FINAL_AUDIT_PLAN.md`
5. `docs/production/RC_MYBOY_CHECKLIST.md`

Only consult `docs/spec/` when a frozen design detail is needed.

## Current phase

The project is in **Release Candidate final audit**, not broad implementation.

The code payload equivalent to the current candidate has already passed the consolidated CI and both major custom validators. The most recent commits after the validated code payload are documentation/continuity changes only. Confirm the current HEAD and its latest workflow result before doing anything else.

## What to do next

Continue the **exhaustive final audit** in `FINAL_AUDIT_PLAN.md`.

Priority:

1. finish the 154-requirement reconciliation;
2. audit the RC diff against `baseline-spanish-vanilla`;
3. identify static blind spots not yet represented by validators;
4. specifically verify obtainability/breeding/resource prerequisites and persistent event state machines;
5. correct any real implementation defects found;
6. keep `RC_AUDIT_LOG.md` updated;
7. once static audit has no open release-blocking finding, freeze one exact RC SHA + ROM SHA-1;
8. then execute the final MyBoy runtime checklist.

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
