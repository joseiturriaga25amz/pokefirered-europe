# Production Decision Amendments

This file records explicit user-approved changes made after the 2026-09-19 preproduction freeze. It supplements the frozen v1.0 documents without silently rewriting their historical state.

## A-001 — Emulator policy

**Date:** 2026-09-19  
**Status:** APPROVED  
**Supersedes:** the v1.0 wording that designated mGBA as the general primary emulator.

### Decision

- **MyBoy is the required runtime emulator for all user-run functional QA and Android playtesting, including link/trade tests.**
- MyBoy may satisfy ordinary smoke tests, save/load tests, gameplay regression, event checks, battle checks, and link/trade validation.
- **mGBA is no longer a required emulator for project acceptance.** It may be used only as an optional secondary diagnostic/reference tool if a defect needs cross-emulator comparison.
- MyBoy results must be recorded explicitly as MyBoy results.
- If a future test exposes a MyBoy-specific limitation that prevents the test from being executed at all, that limitation must be documented and brought back to the user before substituting another emulator; no automatic fallback is assumed.

### Rationale

The original preproduction freeze selected mGBA without first confirming the user's emulator preference or device constraints. The user explicitly corrected this during production and stated that MyBoy is the emulator they use and prefer, and then clarified that they want MyBoy used for all runtime testing. MyBoy supports GBA link-cable emulation, including same-device and Bluetooth/Wi-Fi modes, so link/trade QA does not inherently require mGBA. This amendment preserves test rigor while making the user's actual target environment authoritative for runtime acceptance.


## A-002 — Restore vanilla bag capacity

**Date:** 2026-09-19  
**Status:** APPROVED  
**Supersedes:** the v1.0 decision to expand the normal-items pocket from 42 to 142 slots.

### Decision

- The normal-items pocket keeps the original FireRed capacity and behavior: **42 slots**.
- The proposed 100 extra `ItemSlot` entries at `0x348C..0x361B` are **not used for the bag**.
- `unused_348C[400]` remains unused/reserved as in the base game.
- No contiguous 142-slot RAM mirror, no extended-bag save/load path, and no 50-item stress QA remain part of production.
- The Full save header at `0x3D24..0x3D33` and the reserved Full flag/var namespaces remain in scope because later Full events require persistent state.
- This amendment follows a failed MyBoy runtime test of the 142-slot implementation, where the game reached a black screen. The user explicitly chose to remove the bag expansion rather than continue investing in that feature.

### Rationale

The expanded bag is not important enough to the intended experience to justify additional implementation risk. Preserving vanilla bag behavior reduces save/runtime complexity while keeping the persistent-state infrastructure needed by later Full systems.
