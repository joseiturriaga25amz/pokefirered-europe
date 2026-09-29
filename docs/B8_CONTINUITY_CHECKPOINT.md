# B8 Continuity Checkpoint — 2026-09-29

## Repository state

- Repository: `joseiturriaga25amz/pokefirered-europe`
- Branch: `feature/b8-signature-pokemon-staging`
- Verified HEAD: `80da1a520b6a1f704e67c5795bf266da10e39ef2`
- Verified CI run: `36590266216`
- CI result: **success**
- Workflow: **Full Gameplay Core**
- Compatibility target remains **MyBoy**.

## Working method — mandatory

The user explicitly prefers **microblocks** to avoid long tool loops or chats appearing stuck.

Rules:
1. Work in small isolated blocks.
2. Usually make 1–2 meaningful GitHub actions, then report a checkpoint.
3. Do not poll GitHub Actions repeatedly.
4. For each staged signature Pokémon:
   - inspect map and constraints first;
   - implement one atomic change;
   - trigger/observe one CI;
   - only move to the next block when the prior HEAD is validated.
5. Do not ask the user to test interim builds in MyBoy unless specifically requested. Internal CI/validation is preferred until a meaningful milestone.

## B8 objective

Stage signature Pokémon beside important trainers/leaders using overworld objects while preserving:
- scripts,
- warps,
- collision and access,
- rematch logic,
- MyBoy compatibility,
- existing frozen gameplay invariants.

Current staging uses static 32x32 Pokémon icon-derived overworld graphics. The separate future follower mechanic (first Pokémon walking behind the player, fully animated) is **not part of B8** and must remain separate.

## New visual composition rule — approved by user

From this point onward, and during a later polish pass over already-added signatures:

1. Prefer the signature Pokémon **beside the trainer**, left or right.
2. Avoid putting it directly behind the trainer when a clean lateral composition is possible.
3. When the room permits, compose trainer + Pokémon as a visually balanced, more centered pair within the scene.
4. Choose left/right based on:
   - collision,
   - warps,
   - approach lanes,
   - sightlines,
   - scripts,
   - visual balance.
5. If neither side is safe/clean, use the best nonblocking fallback.
6. Never sacrifice gameplay correctness for visual symmetry.

Important: several already-added signatures currently use "behind" positions. They are valid technically, but should be revisited in a later **visual composition polish pass** under this new rule.

## B8 signature staging already implemented

### Elite Four / League
- Lorelei → **Lapras**
  - Already staged and validated.
- Remaining League signatures to implement next:
  - Bruno → **Machamp**
  - Agatha → **Gengar**
  - Lance → **Dragonite**
- Champion Gary/Blue signature staging remains pending.
  - Earlier concept discussed: stage his Squirtle evolutionary line appropriately (Squirtle / Wartortle / Blastoise) depending on progression/context.
  - Before implementing, inspect existing Gary/Blue scripts and frozen rival decisions so staging does not alter battle roster logic.

### Gym Leaders

- Brock → **Onix → Steelix**
  - Dynamic stage-aware signature.
  - Onix before postgame/rematch condition.
  - Steelix after game clear + relevant Brock TM/rematch condition.
  - Existing validated location: signature object at `(4,5)`.
- Misty → **Starmie**
  - Implemented.
  - Existing validated location: `(8,5)`.
  - `OBJ_EVENT_GFX_STARMIE = 158`.
- Lt. Surge → **Raichu**
  - Implemented.
  - Existing validated location: `(4,2)`.
  - `OBJ_EVENT_GFX_RAICHU = 159`.
- Erika → **Gloom**
  - Implemented.
  - Existing validated location: `(6,3)`.
  - `OBJ_EVENT_GFX_GLOOM = 156`.
- Koga → **Golbat → Crobat**
  - Dynamic stage-aware signature.
  - Existing validated location: `(5,13)`.
  - Golbat pre-postgame; Crobat postgame/rematch condition.
  - `OBJ_EVENT_GFX_GOLBAT = 154`.
  - `OBJ_EVENT_GFX_CROBAT = 155`.
- Sabrina → **Kadabra**
  - Implemented.
  - Existing validated location: `(14,10)`.
  - `OBJ_EVENT_GFX_KADABRA = 157`.
- Blaine → **Magmar**
  - Implemented.
  - Existing validated location: `(4,4)`.
  - `OBJ_EVENT_GFX_MAGMAR = 160`.
- Giovanni → **Persian**
  - Final correction is **Persian**, not Rhydon.
  - HEAD commit: `80da1a520b6a1f704e67c5795bf266da10e39ef2` — "B8: correct Giovanni signature to Persian".
  - Existing validated location: `(1,2)`.
  - Uses `FLAG_TEMP_2` and scripts clear/set it plus remove the signature object appropriately.
  - `OBJ_EVENT_GFX_PERSIAN = 161`.

Current graphics count at verified HEAD:
- `NUM_OBJ_EVENT_GFX = 162`.

## Important corrected decisions

- Erika signature is **Gloom**, not Vileplume.
- Sabrina signature is **Kadabra**, not Alakazam.
- Koga uses **Golbat → Crobat** across progression.
- Brock uses **Onix → Steelix** across progression.
- Giovanni signature is **Persian**. A prior Rhydon staging commit existed but was corrected by the verified HEAD.
- Lorelei signature is **Lapras**.

## Relevant recent commit chain

Newest first:
- `80da1a520b6a1f704e67c5795bf266da10e39ef2` — B8: correct Giovanni signature to Persian — **CI green**
- `bf85a46c17cae115b4fac90c9ef5a406ce3c943b` — B8: stage Giovanni signature Rhydon — superseded by Persian correction
- `a9b366ae625e369158730b3f7122dc94def86216` — B8: stage Blaine signature Magmar — CI green
- `3e24f5aa0588962b6366c28a5b4afa54c2637785` — B8: stage Lt Surge signature Raichu — CI green
- `d268d2f46467611b82f4205e5f279d539264d269` — B8: stage Misty signature Starmie — CI green
- `26afbc3738c52784eebc8d3f7973de4f4bde1786` — B8: stage Sabrina signature Kadabra
- `4cda5a26a23b676f7d379d7420bf22eb83793025` — B8: declare Erika Gloom graphics info
- `560bde0d0e0ed0b563e20916e430b32d36f26ad6` — B8: stage Erika signature Gloom
- `b9405ffedb658e6abcdae2146b74b2ca15a7d7bb` — B8: align graphics-count validator after Koga assets

## Validator

Primary B8 validator:
- `tools/validate_b8_signature_staging.py`

At verified HEAD it checks:
- Lorelei/Lapras
- Brock Onix→Steelix
- Misty/Starmie
- Surge/Raichu
- Erika/Gloom
- Koga Golbat→Crobat
- Sabrina/Kadabra
- Blaine/Magmar
- Giovanni/Persian

It currently expects `NUM_OBJ_EVENT_GFX = 162`.

## Next work — recommended order

Continue B8 in microblocks:

1. **Bruno → Machamp**
   - First inspect `PokemonLeague_BrunosRoom` map + scripts.
   - Apply the new lateral/centered composition rule.
   - Verify Machamp icon palette index before defining graphics info.
   - Add validator coverage.
   - One atomic commit + one CI checkpoint.

2. **Agatha → Gengar**
   - Same process.
   - Prefer left/right staging and balanced room composition.

3. **Lance → Dragonite**
   - Same process.
   - Check approach/exit lane carefully in League room.

4. **Gary/Blue champion signature**
   - Inspect champion room scripts and rival progression first.
   - Preserve the frozen decision that Gary/Blue's battle identity is already defined elsewhere.
   - Staging is visual only; do not silently change battle rosters.
   - Resolve exact evolution/state presentation from existing project decisions before coding if repository evidence is insufficient.

5. **Visual composition polish pass**
   - Revisit all B8 signatures.
   - Move "behind" placements laterally where safe and aesthetically better.
   - Keep validated gameplay constraints intact.
   - Update validator coordinates atomically.

6. Only after B8 is fully green and visually polished, revisit the separate **fully animated follower Pokémon mechanic** as its own block/branch.

## Existing larger project constraints to preserve

- Pokémon FireRed GBA base, Spanish/European project.
- Final emulator target: **MyBoy**.
- Physical/Special split modernized.
- No Fairy type.
- TMs reusable.
- HM system remains original.
- Trade evolutions converted to level/other accessible methods.
- Safari: no time limit; 30 Balls.
- Wild encounter and legendary/event decisions already have frozen validators.
- Gym rematches, Gary/Blue rosters, League rematches and other prior gameplay work are guarded by CI validators. Do not alter them casually.
- User values fidelity to anime + game canon, with challenge adjusted mainly through sensible roster/level design rather than arbitrary gimmicks.

## Handoff instruction for next ChatGPT chat

Start by:
1. Reading this file.
2. Verifying branch HEAD and latest CI once.
3. Do not reconstruct old decisions from memory if this checkpoint and repository disagree; repository + this checkpoint control.
4. Continue with Bruno → Machamp as the next isolated B8 block.
5. Maintain frequent visible checkpoints and avoid long repeated GitHub loops.
