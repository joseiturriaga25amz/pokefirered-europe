# B8 Continuity Checkpoint — canonical handoff

## Source of truth

This file is the canonical handoff for B8. A new chat should be able to continue by reading this file and the repository only.

- Repository: `joseiturriaga25amz/pokefirered-europe`
- Branch: `feature/b8-signature-pokemon-staging`
- Code HEAD verified before this checkpoint commit: `84dff0dfca394aad72bc7c1584ca8de1eb7fbebe`
- Code HEAD message: `B8: require talking to Gary before Champion battle`
- Compatibility target: **MyBoy**
- Primary validator: `tools/validate_b8_signature_staging.py`
- Current `NUM_OBJ_EVENT_GFX`: **166**
- No GitHub Actions workflow run/status was returned for HEAD `84dff0d...` when checked on 2026-09-29. Do **not** describe this HEAD as CI-green until a run is actually verified.

After this document commit, branch HEAD will naturally be one documentation commit newer than the code HEAD above.

## Mandatory working method

The user wants **microblocks**.

1. Make one small, isolated change at a time.
2. Report after each microblock.
3. Avoid long repeated GitHub loops.
4. Do not ask for MyBoy testing during interim work unless the user requests it.
5. Prefer repository validators / CI until a meaningful milestone.
6. Battle-team research is frozen until B8 is fully closed.

## B8 objective

B8 stages each important trainer's signature Pokémon as an overworld object, with direct visual pairing where safe, while preserving scripts, warps, collision/access, rematches, save flow, Hall of Fame flow and MyBoy compatibility.

The future fully animated follower mechanic is **not B8**.

## Locked visual rule

- Prefer the signature Pokémon directly **left or right** of the trainer.
- No empty tile between trainer and Pokémon when a safe direct placement exists.
- Adjust nearby NPC placement or scripted movement when needed, rather than weakening the composition.
- Do not sacrifice gameplay correctness for appearance.

## Current implemented state

### League / Champion

- Lorelei: **Lapras left of Lorelei**
  - Lorelei `(6,5)`
  - Lapras `(5,5)`

- Bruno: **Machamp left of Bruno**
  - Bruno `(6,5)`
  - Machamp `(5,5)`
  - Commit: `c812be742d7a679fca8b075cc6b09650078be6c3`

- Agatha: **Gengar right of Agatha**
  - Agatha `(6,5)`
  - Gengar `(7,5)`
  - Main composition commit: `1fed0b91e2a05ca24af8f1127deafd7aa453258a`
  - Validator fix: `20c2e5e526a89f41288993bccd0cab78cf3047c1`

- Lance: **Dragonite right of Lance**
  - Lance `(6,8)`
  - Dragonite `(7,8)`
  - Lance's right-side scripted movement was rerouted around Dragonite.
  - Validator explicitly checks the detour.
  - Commit: `851fce81936bb255b24413f66e776db410a5094b`

- Champion Gary/Blue: **Blastoise right of Gary**
  - Gary `(6,8)`
  - Blastoise `(7,8)`
  - Commit: `d1b67b4253646ee2371f95df7ad7283cb98c1e45`

- Champion battle interaction:
  - entering the room no longer launches Gary's battle automatically;
  - the player regains control;
  - Gary has script `PokemonLeague_ChampionsRoom_EventScript_Rival`;
  - talking to Gary starts intro/rematch intro and battle;
  - post-battle Oak + Hall of Fame flow remains in the same talk script;
  - validator checks that battle is absent from the entry script and present in Gary's talk script.
  - Commit: `84dff0dfca394aad72bc7c1584ca8de1eb7fbebe`

### Gym Leaders

- Brock: **Onix / Steelix left of Brock**
  - Brock `(6,5)`
  - signature `(5,5)`
  - dynamic `OBJ_EVENT_GFX_VAR_0`
  - Onix before postgame/rematch condition; Steelix after the existing progression condition.
  - Composition commit: `956488638d4fe3936f417114b5abea39d1ca71ff`

- Misty: **Starmie left of Misty**
  - Misty `(8,6)`
  - Starmie `(7,6)`
  - Commit: `5af8d64dd2837335163fe7ee5379f5d1dd2f8f03`

- Lt. Surge: **Raichu** remains staged and validated at `(4,2)`.

- Erika: **Gloom right of Erika**
  - Erika `(6,4)`
  - Gloom `(7,4)`
  - trainer Lisa moved to `(8,4)`, with original facing/sight distance preserved.
  - Commit: `c6e01af32fbace78c53ff98d5ce7304185d77a24`

- Koga: **Golbat / Crobat left of Koga**
  - Koga `(7,13)`
  - signature `(6,13)`
  - dynamic `OBJ_EVENT_GFX_VAR_1`
  - Golbat pre-postgame; Crobat postgame/rematch condition.
  - Composition commit: `f6abd0f12504c564413135b61a059b137de71c2b`

- Sabrina: **Kadabra left of Sabrina**
  - Sabrina `(14,11)`
  - Kadabra `(13,11)`
  - Commit: `465d45cf26ca8df83ca61db4d62fbb93a251e838`

- Blaine: **Magmar** remains staged and validated at `(4,4)`.

- Giovanni: **Persian** remains staged and validated at `(1,2)`.
  - Uses `FLAG_TEMP_2`.
  - Giovanni scripts clear/set the flag and remove the signature object as required.
  - Persian is the final corrected signature; the earlier Rhydon attempt is superseded.

## Critical correction: Misty pool ambience is NOT currently in the branch

A previous chat response reported the Misty pool ambience as completed, but the repository was re-checked and that change is **not present** at the current branch HEAD.

Current facts:

- `CeruleanCity_Gym/map.json` contains Misty + Starmie but **no Seel and no Staryu/Goldeen pool objects**.
- `tools/validate_b8_signature_staging.py` has **no pool ambience checks**.
- `NUM_OBJ_EVENT_GFX` is still **166**, not 168.
- Therefore **Misty pool ambience remains pending** and must be implemented again as its own microblock if it is kept in B8.

Technical research already established for the retry:

- Seel icon palette index: **2**
- Staryu icon palette index: **2**
- Starmie icon palette index: **2**
- Goldeen/Seaking icon palette index: **0**
- Current custom icon-derived overworld Pokémon use the single swappable `PALSLOT_NPC_SPECIAL`.
- Two competing special icon palettes in the same room can overwrite each other's colors.
- Therefore the safe ambience pair is **Seel + Staryu**, not Seel + Goldeen/Seaking, unless the palette system itself is deliberately expanded.
- Suggested water positions previously analyzed:
  - Seel `(5,12)`
  - Staryu `(12,14)`
- Those positions are pond-water tiles and do not overlap existing object/warp events.
- Keep this decorative implementation static/non-interactive; do not expand the engine just for this detail.

## Battle roster decision gate

Commit: `9998500f699383abcce7f1cca8c30e58edd2670c`

Do not redesign or re-open battle teams during B8.

The user will later perform a new dedicated research pass for:
- Gym Leader initial teams;
- Gym Leader rematches;
- Elite Four initial teams;
- Elite Four rematches.

That research begins **only after B8 is fully completed, validated and closed**.

Until then, existing battle rosters are frozen. B8 is presentation/staging only.

## Relevant recent commit chain

Newest code work first:

- `84dff0dfca394aad72bc7c1584ca8de1eb7fbebe` — require talking to Gary before Champion battle
- `d1b67b4253646ee2371f95df7ad7283cb98c1e45` — place Blastoise beside Gary
- `851fce81936bb255b24413f66e776db410a5094b` — place Dragonite beside Lance
- `465d45cf26ca8df83ca61db4d62fbb93a251e838` — place Kadabra beside Sabrina
- `c6e01af32fbace78c53ff98d5ce7304185d77a24` — place Gloom beside Erika
- `5af8d64dd2837335163fe7ee5379f5d1dd2f8f03` — tighten Misty/Starmie composition
- `9998500f699383abcce7f1cca8c30e58edd2670c` — defer roster research until B8 closes
- `f6abd0f12504c564413135b61a059b137de71c2b` — tighten Koga composition
- `956488638d4fe3936f417114b5abea39d1ca71ff` — tighten Brock composition
- `20c2e5e526a89f41288993bccd0cab78cf3047c1` — fix Agatha validator
- `1fed0b91e2a05ca24af8f1127deafd7aa453258a` — tighten Agatha/Gengar composition
- `c812be742d7a679fca8b075cc6b09650078be6c3` — tighten Bruno/Machamp composition

## Remaining B8 work from this checkpoint

Continue in this exact order, one microblock at a time:

1. **Misty pool ambience**
   - implement Seel + Staryu safely;
   - add their two object graphics;
   - update `NUM_OBJ_EVENT_GFX`;
   - add validator coverage;
   - commit atomically;
   - verify branch HEAD after commit.

2. **Full B8 audit**
   - inspect every staged map and all B8-related scripts;
   - check object positions, warps, collision/access, dynamic Brock/Koga state, Erika trainer relocation, Lance detour and Gary talk-to-battle flow;
   - do not add new features during audit.

3. **Run / verify validation and CI**
   - run the B8 validator through the project's normal CI path;
   - verify a real workflow result for the exact code HEAD;
   - do not claim CI-green from an old commit.

4. **Closure checkpoint**
   - update this document with final code HEAD, verified CI run/result and any final corrections;
   - mark B8 closed.

Only after that should the user begin the separate roster-research block.

## Handoff instruction for another chat

A new chat should:

1. Read **this file first**.
2. Verify current branch HEAD.
3. Treat repository state as authoritative over previous chat messages.
4. Notice that Misty pool ambience is still pending despite a prior chat claim.
5. Continue with the Misty pool ambience microblock only.
6. Keep battle rosters frozen.
7. Continue reporting one microblock at a time.
