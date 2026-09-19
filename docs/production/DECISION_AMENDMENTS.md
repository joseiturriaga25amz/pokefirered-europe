# Production Decision Amendments

This file records explicit user-approved changes made after the 2026-09-19 preproduction freeze. It supplements the frozen v1.0 documents without silently rewriting their historical state.

## A-001 — Emulator policy

**Date:** 2026-09-19  
**Status:** APPROVED  
**Supersedes:** the v1.0 wording that designated mGBA as the general primary emulator.

### Decision

- **MyBoy is the primary emulator for user-run functional smoke tests and normal Android playtesting.**
- A production block may satisfy its ordinary runtime smoke requirement on MyBoy when the QA case does not explicitly depend on a feature unique to another emulator.
- **mGBA remains a technical regression tool where specifically required**, especially for link/trade validation or other cases whose existing QA definition explicitly names mGBA.
- MyBoy results must be recorded as MyBoy results; they must not be relabeled as mGBA results.
- If a later QA case requires behavior that MyBoy cannot exercise reliably, that case may use mGBA without changing MyBoy's role as the user's primary emulator.

### Rationale

The original preproduction freeze selected mGBA without first confirming the user's emulator preference or device constraints. The user explicitly corrected this during production and stated that MyBoy is the emulator they use and prefer. This amendment preserves the project's test rigor while aligning routine functional testing with the actual target play environment.
