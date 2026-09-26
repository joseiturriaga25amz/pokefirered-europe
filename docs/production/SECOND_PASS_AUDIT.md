# Second-Pass RC Audit — Pokémon Rojo Fuego Full v1.0

**Purpose:** independent adversarial review after the first exhaustive static audit, before freezing a ROM for MyBoy acceptance.

This pass assumes that a first-pass validator can itself be wrong. It therefore audits not only implementation, but also the evidence chain used to declare implementation correct.

## Principles

1. **Compiled-target truth:** inspect the files that actually feed `firered_es_modern`, especially language-specific scripts.
2. **Semantic diff, not line-count confidence:** compare modified gameplay data against `baseline-spanish-vanilla` and separate formatting churn from functional changes.
3. **Validator skepticism:** a PASS is accepted only if the validator checks the correct file/path/state and does not merely search for convenient tokens.
4. **Cross-layer consistency:** UI/script entry point, generic engine behavior, persistent state, economy/resource consumption and recovery path must agree.
5. **Negative paths matter:** cancel, no room, no money, KO, flee, no stock, link cancellation and reload paths are audited explicitly.
6. **Exact-lock after semantic review:** once a high-risk payload is reviewed, lock its Git blob so later collateral edits cannot invalidate the audit silently.
7. **Runtime boundary honesty:** behavior that cannot be proven statically remains open for MyBoy; static evidence is never promoted to runtime PASS.

## Second-pass layers

### S2-1 — Target/path audit
- Spanish Hall-of-Fame script versus generic sibling.
- Spanish Repel script versus generic sibling.
- Spanish item-ball and move-tutor scripts.
- Workflow references point to target-language files.
- Non-target generic scripts restored to vanilla where recovery accidentally touched them.

### S2-2 — High-risk semantic diff
- Battle move metadata.
- Evolution table and direct-use evolution item effects.
- Wild encounter tables.
- Trainer metadata and party payload.
- Gary routing.
- Save namespace/layout and migration.
- Link/trade callbacks and UBFIX paths.

### S2-3 — Evidence-chain audit
- Every production validator is invoked by the consolidated workflow.
- Gate 6/7/QoL validators inspect compiled Spanish paths.
- High-risk payloads receive exact blob locks after semantic review.
- False-positive findings are corrected in the audit log instead of preserved as fictional fixes.

### S2-4 — Cross-system contradiction sweep
Look specifically for:
- script says success but engine rejects action;
- validator inspects generic file while target compiles localized file;
- capacity/check path disagrees with mutation path;
- state advances before reward/resource is actually delivered;
- UI exposes an operation the core engine cannot complete;
- fallback/negative branch consumes money/item/state;
- recovery state exists but is never invoked by the actual lifecycle callback.

### S2-5 — Pre-freeze acceptance
Before freezing:
1. second-pass static sweep has no open release blocker;
2. exact HEAD consolidated CI is green;
3. ROM build is byte-for-byte reproducible;
4. exact ROM SHA-1 is recorded;
5. only then execute `RC_MYBOY_CHECKLIST.md`.

## Findings discovered by the second-pass mindset

The recovery/final audit has already exposed examples of the failure classes this pass is designed to catch:

- validator targeting the wrong language script;
- UI route present while generic item-effect engine still rejected the operation;
- save migration function present but not called by Continue;
- trade/link fixes gated by revision instead of Full's forced BUGFIX path;
- wireless status array indexing unsafe under MODERN/UBFIX;
- a recovery audit false positive (Repel) corrected rather than hidden.

## Current status

Second-pass audit is active. Static completion is not equivalent to release acceptance. MyBoy remains mandatory for the final runtime gates, especially save migration/persistence, battle behavior, link/trade, event terminal branches, UI re-entry/cancellation and progression smoke.
