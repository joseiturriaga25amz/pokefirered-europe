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



### 2026-10-20 — Follower interaction friendship microblock

- Verified the earlier A-interaction compile fix `6a6b4af`: Follower Prototype Actions run [39325607382](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/39325607382) completed **SUCCESS** for that exact technical SHA (private diagnostic 386-species build plus configured checks). This is not a MyBoy runtime PASS and not Full Gameplay Core.
- Implemented actual A-button dialogue when facing the runtime follower, without NPC template persistence: `67696cc` (four files: field interaction, follower runtime, header and event scripts). Corrected native dialogue newline encoding in `870b9a6`. These are separate technical commits with Follower Prototype automatic build runs [39457425247](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/39457425247) and [39457517291](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/39457517291), **IN PROGRESS when recorded**; verify final exact-SHA result and job logs before claiming validation.
- Dialogue currently exposes seven tiers for actual 0..255 friendship (0, 1–49, 50–99, 100–149, 150–199, 200–254, 255), and selects the first healthy non-egg party member matching the active follower. Unlike `GetLeadMonFriendship`, it skips fainted first-slot Pokémon. Cosmetic only: no Pokémon/BoxPokemon/SaveBlock/link changes; avoids Quest Log and Union Room entry, preserves transient local-ID 254 guard and ordinary counter handling. Spanish messages are emitted for the Spanish build; fallback English only for non-Spanish build configurations.
- Status: **IMPLEMENTED, NOT YET VALIDATED for the newest technical HEAD**, MyBoy not run. Before next feature, confirm Actions for `870b9a6`, inspect failure if any, and perform targeted source/script behavior audit (dialogue close, wrong/absent lead, reorder, follower sprite lifetime, busy field control). Continue roadmap microblock 3 (save/load restore) only once microblock 2 is accepted, then context visibility and geometry; bundle future MyBoy QA on a corrected ROM. Surf remains deferred/nonblocking; no user story replay.


### 2026-10-20 — B10 A08 save/load restoration

- Friendship interaction code HEAD `870b9a62f29bd62d41a9d823c1feae6d695203a6` passed Follower Prototype workflow run `39457517291`; subsequent docs-only HEAD `da9cbc15e02e9b2080b9b688a853710ae0b9f3f2` passed run `39457603360`. These are CI build/static checks, not MyBoy proof.
- **A08 implementation:** technical commit `62fe6b448761b4f6ab05f2c81ff9ffa7ffc9e1fc` modifies only `src/quest_log.c`: at the final state of `Task_EndQuestLog`, after field controls are unlocked, call `FullFollower_OnLocalMapReady()` to re-arm the runtime-only companion task suppressed during Quest Log playback. The task itself handles eligible party, map controls, bike/Surf and safe spawning. No saved data or link serialization changes. This addresses the source-supported path where resume from Quest Log left no follower until the next map transition.
- Follower Prototype CI run `39458289730` for `62fe6b4` was **IN PROGRESS when recorded**. Check its exact outcome and investigate any failure before calling this microblock validated. No MyBoy check or integration performed. Next: exact technical CI and targeted source audit, then B10 contextual visibility microblock. Surf remains deferred to a new diagnostic fixture, not story progression.


### 2026-10-20 — B10 A09 Start/Save visibility (partial contextual presentation)

- Exact technical HEAD `62fe6b448761b4f6ab05f2c81ff9ffa7ffc9e1fc` (Quest Log end restores transient follower task after save/load) passed Follower Prototype Actions run `39458289730`; subsequent docs-only HEAD `b1d4094481777091670d34d71dfedc62a49f33be` passed run `39458360974`. Compilation/static checks only; MyBoy A08 regression remains pending.
- `2a9bbf264f729f0863b69e5535345864cfd33840` implements a narrow **Start/Save menu** presentation exception: `StartMenu_IsSafeForFollower()` recognizes live non-link, non-fading menu tasks and only the ordinary HandleInput/Save callbacks; `ShouldSuppressFollower()` retains strict Quest Log, warp, bike/Surf, jump and `ScriptContext_IsEnabled()` checks. Adds matching static assertions to the existing Follower Prototype workflow rather than weakening its previous field-lock validator.
- **Scope:** Start/Save visibility only, **not** general NPC/sign dialogues, trainer sight, healing, battle lead-in, escalators, ledges or Surf. During generic scripts, the follower remains deliberately suppressed. This is a conservative first part of roadmap item 4, and must not be called complete contextual visibility.
- New exact technical workflow run `39459203847` was IN PROGRESS when recorded. Inspect final result and logs and repair a real failure before advancing. No exact updated MyBoy test or master integration; final user QA on a bundled corrected ROM only. Next: audit any remaining menu lifecycle/fade risk and then separately classify ordinary sign/NPC dialogue without globally bypassing scripted field locks.


### 2026-10-20 — B10 A09 text-only dialogue visibility

- Verified Start/Save technical commit `2a9bbf264f729f0863b69e5535345864cfd33840`: Follower Prototype run `39459203847` SUCCESS for that exact SHA (and docs-only `530e0d2` run `39459279530` SUCCESS). MyBoy runtime is still NOT EXECUTED.
- Technical commit `975a268d5b3671681f41f92f4f6ada3c72fe8f16` implements a narrow **text-only script** exemption for an already-existing follower. Direct A-interaction scripts must match a bounded, branch-free, single-message `loadword` + `callstd` grammar (optional lock/face/release). Other map scripts, gifts, trainer battles, warps, script replacements, menu fades, Quest Log and link play do NOT receive exemption. Follower stays frozen while text is displayed; no saved data changes. The existing Follower Prototype workflow now checks this safety contract and conservative command classification.
- Run `39464979599` was **IN PROGRESS** when documented. Exact technical CI and independent runtime behavior review are required before VALIDATED; do not call B10 presentation complete. Important follow-up: audit message closure, bytecode parser bounds, state cancellation on competing non-script field activities and cross-target compilation before moving into trainer-specific battle staging. A08/Start fixes still require bundled new MyBoy ROM checks. Surf remains deferred to fixture.

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
