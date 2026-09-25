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

**B2-F003 — RETRACTED / FALSE POSITIVE.**

Initial inspection treated Thunderbolt as a later-TM leak. Repository learnset verification shows Pikachu learns Thunderbolt naturally at level 26, exactly the level used by Surge, and Raichu may legitimately retain it after evolution. Surge therefore needs no BOSS-001 correction for Thunderbolt. This correction is kept in the audit trail rather than silently deleting the false positive.

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


## B2.2 implementation decision

Applied the minimum correction needed to remove the two clear direct-damage progression spikes while preserving frozen rosters, levels and boss identity:

- Gary / Cerulean Abra 18: **Psychic → Thief**. Reflect, Light Screen and Teleport remain as utility. Thief is species-legal and its TM is obtainable in Mt. Moon before Cerulean.
- Misty / Starmie 26: **Psychic → Rapid Spin**. Water Pulse remains the signature STAB; Recover and Swift remain. This removes the later Psychic spike without weakening Misty's roster or ace level.
- Lt. Surge: **no change** after B2-F003 was retracted through level-up-learnset verification.
- Brock: no change.

B2.2 intentionally does not rewrite support moves solely because their TM source occurs later. The BOSS-001 correction is aimed at unexplained early power leakage; signature-leader moves and bounded utility are allowed when they preserve encounter identity without introducing a late-game direct-damage spike.


## User-approved leader decisions

### Brock — APPROVED AS CURRENT

No roster, level, move or item changes.

### Misty — APPROVED 2026-09-25

Keep current roster/levels:
- Goldeen 21
- Staryu 23
- Starmie 26 + Sitrus Berry

Approved moves:
- Goldeen — Water Pulse / Horn Attack / Supersonic / Peck
- Staryu — Water Pulse / Swift / Rapid Spin / Light Screen
- Starmie — Water Pulse / Swift / Rapid Spin / Recover

Design intent:
- Goldeen opens with a weaker overall stat profile but already introduces Misty's Water Pulse identity.
- Staryu adds utility and Swift even though Swift is normally learned at level 24; exact level-up timing is not being used as a hard restriction for boss custom sets.
- Starmie remains the ace through stats, level, Sitrus Berry and recovery rather than premature Psychic coverage.
- All selected moves are legal for the species in FRLG/Full; custom boss sets may use a species-legal move slightly before its natural level-up point when explicitly approved.


### Brock — revision approved 2026-09-25

Onix 17 changes **Rock Throw → Rock Smash**.

Final approved Brock first-battle set:
- Geodude 14 — Rock Throw / Tackle / Defense Curl / Mud Sport
- Onix 17 — Rock Tomb / Rock Smash / Bind / Screech + Oran Berry

Rationale:
- Rock Smash is legal for Onix through HM06.
- The change gives Brock's ace a more anime-like physical identity and differentiates Onix from Geodude's basic Rock offense.
- No roster, level, item, IV or other move changes.


### Lt. Surge — partial approval 2026-09-25

Approved:
- Voltorb 25 — Shock Wave / Tackle / SonicBoom / Screech
- Pikachu 26 — Shock Wave / Thunder Wave / Quick Attack / Double Team

Design rule:
- first-battle Electric ceiling is Shock Wave, matching the signature-TM progression used with Brock/Rock Tomb and Misty/Water Pulse;
- Voltorb is intentionally the simple first escalation step;
- Raichu remains pending user approval and must feel like the ace without using Thunderbolt in the first battle.


### Koga — partial approval 2026-09-25

Approved:
- Muk 43 changes Sludge Bomb -> Sludge (Spanish ROM name: Residuos).
- Muk final pending no other changes: Sludge / Minimize / Acid Armor / Toxic.

Design rule:
- Koga first-battle Poison STAB ceiling uses Sludge (65 BP; 97.5 STAB reference), not Sludge Bomb (90 BP; 135 STAB reference).
- Weezing ace set remains under review; Explosion and Self-Destruct are explicitly rejected for the first battle.
