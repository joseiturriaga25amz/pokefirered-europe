# Pokemon Rojo Fuego Full — RC Audit Log

**Audit start:** 2026-09-20  
**Branch:** `feature/full-gameplay-core`  
**Frozen base:** `baseline-spanish-vanilla` -> `e184c5cf898cd29efebd33bc1bfe5994277e21ab`

## Source precedence used by the audit

1. Frozen preproduction v1.0 and matrices.
2. Explicit production amendments in `docs/production/DECISION_AMENDMENTS.md`.
3. Current implementation and CI as evidence of implementation.
4. Runtime MyBoy QA as final evidence for behavior that cannot be proven statically.

The audit does not silently restore requirements superseded by an approved amendment.

## Approved post-freeze amendments

- **A-001:** MyBoy is the required runtime emulator. mGBA is optional only.
- **A-002:** normal Items pocket remains vanilla at 42 slots. The abandoned 142-slot bag is not a production requirement.

## Current automated gates

The Full gameplay workflow builds `firered_es_modern` and protects:
- physical/special split and move categories;
- approved evolution changes;
- minimum learnset corrections;
- Synchronize wild-nature behavior hook;
- Full save namespaces;
- approved shops and encounter rates;
- Gary/story boss/rematch rosters;
- legendary KO/Hall of Fame respawn invariants;
- sequential roaming beasts and Pokedex tracking;
- Mystic/Aurora ticket quest progression;
- Mew/Celebi event state and movesets;
- Gen III Pokemon/BoxPokemon structure sizes;
- vanilla pre-National trade restrictions.

## Findings repaired during RC audit

### RC-F001 — Sequential-roamer Pokedex still used vanilla starter mapping
**Status:** FIXED  
The Pokedex location code still associated Entei/Suicune/Raikou with the player's starter. Full now checks the actually active beast and requires it to have been seen before revealing its current route.

### RC-F002 — Celebi trigger was attached provisionally to the Berry Forest welcome sign
**Status:** FIXED  
The event is now attached to a real Berry Forest tree. When Celebi requirements are not satisfied the object keeps normal Cut-tree behavior.

### RC-F003 — MOV-006 trainer-set legality validator missing
**Status:** FIXED / PASS  
Added `tools/validate_full_trainer_sets.py` and wired it into CI. The validator passed across 34 Full parties, 163 Pokémon and 632 custom moves, checking repository species/move/item IDs plus level/TM-HM/tutor/egg/evolution-line learnability.

### RC-F004 — QOL-009 EV summary view missing
**Status:** FIXED / IN VALIDATION  
The frozen specification requires an EV view in the Pokémon summary. Added a SELECT toggle on the Skills page, exact six-stat EV values, proportional per-stat bars, and total/510 information. The toggle is disabled for battle/enemy/link summaries and works from the normal party/box summary path.

### RC-F005 — ECO-008 Resort Gorgeous circuit payout incomplete
**Status:** FIXED / IN VALIDATION  
Celina remained a Painter in the implementation, so the intended Jacki/Gillian/Celina high-payout VS Seeker circuit was not satisfied. Celina now uses the Lady trainer class/presentation while keeping her localized name and frozen party. CI now asserts Lady class for all three circuit trainers.

## Structural compatibility evidence

- No new Pokemon, move or item IDs are introduced by Full.
- `sizeof(struct BoxPokemon) == 0x50` is compile-locked.
- `sizeof(struct Pokemon) == 0x64` is compile-locked.
- SaveBlock1 remains `0x3D68`.
- The Full header occupies the approved 16-byte region at `0x3D24`.
- Pre-National egg/non-Kanto trade restrictions remain in the original trade path.
- Mew/Deoxys fateful-encounter trade check remains active.

## Runtime-only acceptance still required

These classes cannot be truthfully closed by static inspection/build alone:
- new game / continue / save-load smoke;
- battle damage and AI behavioral smoke tests;
- menu/UI interactions;
- Safari step/ball behavior;
- event sequencing from a real save;
- flee/KO/capture branches for legendary and mythical encounters;
- roamer movement, Roar and identity persistence;
- VS Seeker/rematch repeatability;
- link/trade behavior with MyBoy;
- end-to-end progression and softlock/regression playthrough.

## Release rule

Do **not** merge to `main` or label v1.0 final until:
1. consolidated CI is green;
2. static audit has no open critical implementation findings;
3. required MyBoy runtime checklist has been executed;
4. regressions discovered by that checklist are corrected and retested.


### RC-F006 — BUG-007 Move Reminder stored both scroll indicators in one slot
**Status:** FIXED / IN VALIDATION  
The second scroll indicator overwrote `spriteIds[0]`, exactly matching the frozen bug description. It now uses `spriteIds[1]`, and visibility updates reference the stored sprite IDs rather than assuming sprite numbers 0/1.

### RC-F007 — BUG-008 L=A key repeat still used mismatched raw/remapped state
**Status:** FIXED / IN VALIDATION  
Key repeat now compares the current raw input with the previous raw held input, then maps repeated L presses to A in `newAndRepeatedKeys`. This preserves the normal L=A synthetic A behavior while allowing held-key repetition.

### RC-F008 — BUG-009 party two-slot animation leak was language-dependent
**Status:** FIXED / IN VALIDATION  
The two temporary tilemap buffers are now unconditionally freed after the two-mon slide animation. The previous source only freed them in non-English builds; Full now carries one safe path for every build.

### RC-F009 — EVO-005..010 trade-item evolution UI route incomplete
**Status:** FIXED / IN VALIDATION  
`GetEvolutionTargetSpecies` already accepted `EVO_TRADE_ITEM` in item-use mode, but Metal Coat, Dragon Scale, Up-Grade and King's Rock still used `ITEM_TYPE_BAG_MENU`. Because `FieldUseFunc_EvoItem` obtains its next callback from the item type, those items lacked the party-selection callback. They now use `ITEM_TYPE_PARTY_MENU`, matching evolution stones while retaining their existing hold effects and evolution table semantics.
