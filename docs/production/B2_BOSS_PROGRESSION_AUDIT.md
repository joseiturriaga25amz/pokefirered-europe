# B2 Boss / Rival Progression Audit

**Date:** 2026-09-25  
**Branch:** `feature/b2-boss-rival-balance`  
**Starting code checkpoint:** `ede84f8837346ffe22d697c9ed6a6677ad7fb3f4` (B1 gameplay, Full Gameplay Core run 36135969057 SUCCESS)  
**B2 documentation base:** `dc807ad7d8a7b93c5a91ba5ea5dec71583196284`

## Scope

B2.1 is a read-only reconciliation pass for BOSS-001 / A-009. It checks whether early boss moves are merely species-legal or also coherent with the player's story-stage move power/access. Frozen rosters and levels remain authoritative unless a later approved amendment explicitly changes them.

## Findings

### Gary — Cerulean

Frozen roster remains:
- Abra 18
- Rattata 19
- Pidgeotto 20
- Squirtle 22

Current Abra set:
- Psychic
- Reflect
- Light Screen
- Teleport

**Finding B2-F001 — progression mismatch.**

The frozen matrix describes this encounter as “legal and progressive” and says Abra should use legal TMs so it is not a dead turn. Species legality is satisfied, but the current set front-loads late-game-strength/support TMs into the Cerulean encounter. Psychic is the principal power spike. The roster/level must remain unchanged; B2 should replace only the incoherent move payload while keeping Abra an active threat.

### Brock

Current key set:
- Geodude 14 — Rock Throw / Tackle / Defense Curl / Mud Sport
- Onix 17 — Rock Tomb / Rock Throw / Bind / Screech

**Result:** no BOSS-001 correction identified. Rock Tomb is Brock's own signature TM/reward and is appropriate boss presentation for this stage.

### Misty

Current notable moves:
- Goldeen 21 — Water Pulse / Horn Attack / Peck / Supersonic
- Staryu 23 — Water Pulse / Light Screen / Recover / Rapid Spin
- Starmie 26 — Water Pulse / Psychic / Recover / Swift

**Finding B2-F002 — progression mismatch.**

Water Pulse is appropriate as Misty's signature TM. Psychic on Starmie is a much later player-access move and creates an avoidable early power spike. Light Screen is species-legal but also arrives later in normal player progression. B2 should retain Misty's identity/difficulty while replacing premature move sources rather than weakening roster/levels.

### Lt. Surge

Current notable moves:
- Voltorb 25 — Shock Wave / Spark / SonicBoom / Screech
- Pikachu 26 — Thunderbolt / Thunder Wave / Quick Attack / Double Team
- Raichu 30 — Thunderbolt / Body Slam / Mega Kick / Quick Attack

**Finding B2-F003 — progression mismatch.**

Shock Wave is appropriate as Surge's signature TM. Thunderbolt appears before the player's normal Celadon access to that move. B2 should remove the premature Thunderbolt dependency while preserving Surge as a meaningful difficulty spike.

### Giovanni — Rocket Hideout / Silph

Current parties are still `TrainerMonNoItemDefaultMoves`:
- Rocket Hideout: Onix 25 / Rhyhorn 24 / Kangaskhan 29
- Silph: Nidorino 37 / Kangaskhan 35 / Rhyhorn 37 / Nidoqueen 41

**Finding B2-F004 — approved boss-standard gap.**

A-009 explicitly requires these Giovanni encounters to receive the Full boss-design standard. They currently rely on default level-up moves rather than deliberate custom boss sets. This is not a frozen-roster conflict: B2 should keep the approved species/levels unless a concrete incoherence is found, but convert these encounters to intentional legal/progression-aware movesets and validate them.

## Non-findings / constraints

- Gary's fixed Squirtle line and exact frozen encounter rosters/levels remain unchanged.
- Do not alter first-gym rosters merely to solve move progression.
- Do not use “the species can learn the TM” as sufficient proof of stage appropriateness.
- Do not require every boss move to be obtainable by the player at that exact moment; signature-boss moves are valid when narratively justified. The audit targets unexplained power leakage from substantially later progression.
- Trainer legality validation remains mandatory after every set change.

## Next microblocks

1. **B2.2:** reconcile Gary Cerulean + Misty + Surge move payloads only; no roster/level changes.
2. Run trainer-set legality validator / consolidated targeted CI.
3. **B2.3:** convert Rocket Hideout Giovanni to a deliberate custom-move boss set and validate.
4. **B2.4:** convert Silph Giovanni similarly.
5. Re-audit adjacent Gary/boss encounters for accidental regression, then close B2 with staged-progression documentation.
