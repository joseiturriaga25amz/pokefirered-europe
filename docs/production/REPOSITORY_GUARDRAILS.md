# Repository Guardrails — Pokémon Rojo Fuego Full

This file exists to prevent accidental work against the upstream repository or any non-canonical remote.

## Canonical repository

- **WRITE TARGET / project source of truth:** `joseiturriaga25amz/pokefirered-europe`
- **Upstream reference only:** `CompuMaxx/pokefirered-europe`
- Upstream may be read for comparison, but production commits, branches, blobs, files, pull requests and release work must never target upstream.

## Mandatory preflight before any repository mutation

Before creating or updating a branch, file, blob, tree, commit or pull request:

1. Resolve the target repository explicitly.
2. Confirm the exact full name is `joseiturriaga25amz/pokefirered-europe`.
3. Confirm repository permissions report `push: true`.
4. Confirm the active production branch and its HEAD.
5. Only then perform writes.

If any of those checks fail, **stop writes**. Read-only investigation may continue, but no production state may be claimed as implemented.

## Current production branch

At the time this guardrail was added:

- Branch: `feature/b2-boss-rival-balance`
- Protected checkpoint before this documentation change: `eed2d780be04f1b6dcc396ef9d01b5808dd8aea4`
- That checkpoint contains the hardened Giovanni/Mewtwo escape cutscene.
- Its parent implementation commit is `b48fab525fd10a11e5552d5b6ef22ada5fb712d8`.

## Session rule

Every new coding session must treat `docs/production/PROJECT_CONTINUITY.md` and this file as mandatory startup context.

A repository name inferred from a parent/fork relationship, search result, previous tool call or old chat is not sufficient. The full repository name must be checked directly before the first write.

## Incident note — 2026-09-25

During B2 review, read operations were accidentally pointed at the upstream repository `CompuMaxx/pokefirered-europe`. The upstream correctly exposed `pull: true, push: false`, which caused write attempts to fail with HTTP 403. No project data was lost: the authoritative fork already contained the B2 branch and both Mewtwo commits.

Corrective action: canonical-repository and push-permission preflight is now mandatory before all future writes.


## Single-line production rule

The project must never be advanced in parallel across multiple repositories or multiple production branches.

- There is exactly one canonical write repository: `joseiturriaga25amz/pokefirered-europe`.
- There is exactly one active production branch at a time.
- While a production block is open, all code and documentation writes for that block must land on that one branch.
- Do not begin the next production block on another branch while the current block is still unmerged.
- Before opening the next block: validate the current block, merge it into the fork's `master`, verify the new `master` HEAD, and create the next branch from that exact merged HEAD.
- Detached or unreferenced production commits are not an accepted project state.
- The upstream `CompuMaxx/pokefirered-europe` is never a production write target.

Current state when this rule was added:
- Active block: B2
- Active branch: `feature/b2-boss-rival-balance`
- Fork B2 HEAD before this guardrail update: `388cfde07504e4843f3414dc88206150618d8d0b`
- Fork `master`: `b64676b3177f162acfc04214027e0e2ae3e35c3b`
- Upstream has no B2 branch.
