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
- vanilla pre-National trade restrictions;
- frozen RC economy/event/evolution invariants via `tools/validate_rc_freeze.py`.

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
**Status:** FIXED / CI PASS  
The frozen specification requires an EV view in the Pokémon summary. Added a SELECT toggle on the Skills page, exact six-stat EV values, proportional per-stat bars, and total/510 information. The toggle is disabled for battle/enemy/link summaries and works from the normal party/box summary path.

### RC-F005 — ECO-008 Resort Gorgeous circuit payout incomplete
**Status:** FIXED / CI PASS  
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
**Status:** FIXED / CI PASS  
The second scroll indicator overwrote `spriteIds[0]`, exactly matching the frozen bug description. It now uses `spriteIds[1]`, and visibility updates reference the stored sprite IDs rather than assuming sprite numbers 0/1.

### RC-F007 — BUG-008 L=A key repeat still used mismatched raw/remapped state
**Status:** FIXED / CI PASS  
Key repeat now compares the current raw input with the previous raw held input, then maps repeated L presses to A in `newAndRepeatedKeys`. This preserves the normal L=A synthetic A behavior while allowing held-key repetition.

### RC-F008 — BUG-009 party two-slot animation leak was language-dependent
**Status:** FIXED / CI PASS  
The two temporary tilemap buffers are now unconditionally freed after the two-mon slide animation. The previous source only freed them in non-English builds; Full now carries one safe path for every build.

### RC-F009 — EVO-005..010 trade-item evolution UI route incomplete
**Status:** FIXED / CI PASS  
`GetEvolutionTargetSpecies` already accepted `EVO_TRADE_ITEM` in item-use mode, but Metal Coat, Dragon Scale, Up-Grade and King's Rock still used `ITEM_TYPE_BAG_MENU`. Because `FieldUseFunc_EvoItem` obtains its next callback from the item type, those items lacked the party-selection callback. They now use `ITEM_TYPE_PARTY_MENU`, matching evolution stones while retaining their existing hold effects and evolution table semantics.


### RC-F010 — ECO-004 berry shop and Emerald EV-berry behavior were absent
**Status:** FIXED / CI PASS  
The frozen matrix required adventure/post-National berry inventories with approved prices and Emerald-style EV-reducing berries. The implementation still had vanilla Two Island stock, every approved berry retained the placeholder price 20, and Pomeg/Kelpsy/Qualot/Hondew/Grepa/Tamato had no field-use effect. Full now adds the staged Two Island berry inventory, all 28 frozen prices, direct party use for the six EV berries, -10 EV reduction with floor 0, and the Emerald friendship increase path (including friendship-only use when the target EV is already 0).

### RC-F011 — Fossil/Dojo/Altering Cave/economy freeze lacked a consolidated static gate
**Status:** FIXED / CI PASS  
Added `tools/validate_rc_freeze.py` and wired it into CI. It protects the frozen berry economy/effects, both-fossil recovery path, Cinnabar revival support, second Dojo state/reward invariants, Eevee/level evolution invariants, all nine Altering Cave tables/selector states, and the 5,000-coin Porygon price.


### RC-F012 — Historical QA workbook still names superseded emulator/bag tests
**Status:** RESOLVED BY AMENDMENT TRACEABILITY  
The frozen specification still contains mGBA wording in COMP-006/QA-002 and the abandoned bag expansion in QOL-008, SAVE-002 and QA-005/QA-006. These historical rows remain preserved, but A-001/A-002 supersede them and they are not release criteria. Added `docs/production/RC_MYBOY_CHECKLIST.md` as the authoritative final runtime handoff: MyBoy is required, the Items pocket is vanilla 42 slots, and runtime acceptance is grouped without restoring the abandoned bag implementation.


### RC-F013 — High-risk save layout/migration invariants were compile-only, not RC-gated
**Status:** FIXED / IN VALIDATION  
The implementation already preserved `SaveBlock1 == 0x3D68`, the Full header at `0x3D24`, and `unused_348C[400]`, while `InitFullSaveData` initializes only the Full-owned header. The RC validator now asserts these A-002/SAVE-001/SAVE-004 invariants and rejects any migration path that touches the vanilla bag or reserved `0x348C` area.


### RC-F014 — COMP-001 vanilla ID-space compatibility lacked an explicit RC gate
**Status:** FIXED / IN VALIDATION  
Direct baseline comparison confirms the ID spaces are unchanged: `SPECIES_EGG = 412` / `NUM_SPECIES = SPECIES_EGG`, `MOVES_COUNT = 355`, and `ITEMS_COUNT = 375`. The RC validator now locks those values so Full cannot silently introduce incompatible Pokémon, move or item IDs.


### RC-F015 — Frozen item economy was correct but incompletely protected
**Status:** FIXED / IN VALIDATION  
The approved prices for all 16 type boosters, special held items, renewable evolution items, PP consumables, Lucky Egg and TM44 were present, and the post-National Celadon stock was correctly gated. The RC validator now locks those prices, requires post-National-only stock where specified, and rejects the explicitly excluded Exp. Share, Amulet Coin, Soothe Bell and Macho Brace from that shop.

### RC-F016 — SAVE-012 ticket quests did not set vanilla RECEIVED flags
**Status:** FIXED / IN VALIDATION  
The Full MysticTicket/AuroraTicket quests correctly granted the existing items and enabled the original ferry destinations, but they did not set `FLAG_RECEIVED_MYSTIC_TICKET` / `FLAG_RECEIVED_AURORA_TICKET` as required by SAVE-012. Both vanilla receipt flags are now set at successful delivery, and `tools/validate_rc_freeze.py` locks the paired RECEIVED + ENABLE_SHIP state. The redundant second `InitRoamer` call introduced in the Sapphire handoff was also removed; the original vanilla call remains.

### RC-F017 — ROM checksum changes across docs-only commits
**Status:** FIXED / IN VALIDATION — RC FREEZE REMAINS BLOCKED UNTIL CI PROVES IT  
The consolidated workflow produced different SHA-1 values for `pokefirered_modern_es.gba` across docs-only commits, and a rerun of the exact same SHA `032f2c4...` changed from `6cad6404...` to `31eff4b8...`. A dedicated two-clean-build gate reduced the mismatch to three ASCII digit bytes. Root cause: the MODERN branch in `src/main.c` embedded `__DATE__ " " __TIME__` in `BuildDateTime`. Full now uses a deterministic retail timestamp for the Spanish modern target, and CI rebuilds from clean twice and requires byte-for-byte equality before any RC checksum may be accepted.

### RC-F018 — Gate 1 had no explicit 154/154 disposition ledger
**Status:** FIXED / DOCUMENTED  
Added `docs/production/RC_REQUIREMENTS_RECONCILIATION.md` and classified all 154 implementation requirements against A-001..A-004 and the current implementation. The ledger currently has 52 implemented + automated-evidence rows, 99 implemented + runtime-evidence-required rows, and 3 superseded rows. Runtime-classified entries remain deliberately unclosed until MyBoy.

### RC-F019 — ENC-022 baby obtainability prerequisites were not statically proven
**Status:** FIXED / IN VALIDATION  
Added `tools/validate_full_obtainability.py`. It proves one-save prerequisite paths for Pichu, Cleffa, Igglybuff, Togepi, Tyrogue, Smoochum, Elekid, Magby, Azurill and Wynaut, including Ditto/parents, the Jynx in-game trade, both Hitmon sources, the Togepi egg, and Sea/Lax Incense.

### RC-F020 — Full flag/var namespace ownership had no collision scan
**Status:** FIXED / IN VALIDATION  
Added `tools/validate_full_save_namespace.py`. It locks the Full flag/var assignments, rejects live uses of vanilla numeric aliases inside the reserved Full ranges, and asserts migration initialization touches only the Full header rather than the vanilla bag/reserved area.


### RC-F021 — Frozen bugfix validator crashed on vanilla map objects without `local_id`
**Status:** FIXED / CI PENDING  
`tools/validate_frozen_bugfixes.py` indexed `obj["local_id"]` for every Mt. Ember B3F/B5F object event. Vanilla boulders and Rock Smash objects legitimately omit that optional field, so the validator raised `KeyError` even though the Ruby object itself was correctly moved to B5F. The BUG-012 check now filters to objects that actually define `local_id`, preserving the intended invariant without rejecting valid vanilla map objects.

### RC-F022 — Gate 7 obtainability validator overclaimed its coverage
**Status:** FIXED / CI PENDING  
The current `validate_full_obtainability.py` prints a broad Gate 7 PASS after checking the frozen ENC additions, baby prerequisites, fossils, selected event species and renewable evolution items, but it does not construct a complete reachability proof. The 154-requirement ledger confirms that Gen I–III #001–386 is the allowed species universe rather than a standalone requirement to add local sources for every Hoenn species; D-039/EVT-019 explicitly exclude the reserved Hoenn legendaries. Gate 7 now proves the complete self-contained Kanto Pokédex closure, the approved LeafGreen additions, Full starter/Eevee/Safari/Altering Cave sources, direct evolution routes/resources, baby breeding prerequisites, fossils/Dojo and the required legendary/mythical event sources. RC-F024 further hardened the proof to use FireRed encounter records only and conditional in-game trade closure. Runtime event behavior remains reserved for MyBoy.

### RC-F023 — Persistent event-state validator did not cover every Gate 6 machine
**Status:** FIXED / CI PENDING  
`validate_full_event_states.py` now additionally locks the sequential roamer transition machine, Aurora/Mystic quest transitions and full-bag non-advance behavior, Altering Cave selector persistence, repeatable Porygon purchase, tutor first-free/repeat-paid state paths, Two Island berry progression and repeatable Gym rematches. This closes the identified static coverage gaps; runtime terminal behavior still requires the final MyBoy checklist.

### RC-F024 — Gate 7 obtainability proof mixed FireRed/LeafGreen encounter tables and trusted trade outputs unconditionally
**Status:** FIXED / CI PENDING  
`validate_full_obtainability.py` originally walked the entire dual-version `wild_encounters.json`, so a species present only in a LeafGreen table could incorrectly satisfy the FireRed Full one-save proof. It also seeded every in-game trade output without first proving that the requested species was obtainable. The validator now restricts wild-source discovery to `_FireRed` encounter records and closes in-game trades only when each requested species is already reachable. This hardens Gate 7 without changing gameplay data.

### RC-F025 — Vanilla-save migration initializer was not invoked on Continue
**Status:** FIXED / CI PENDING  
`InitFullSaveData()` existed and correctly limited migration writes to the 16-byte Full header, but it was only called from new-game initialization. A valid vanilla Spanish save loaded through CONTINUE could therefore enter gameplay without receiving the required `RFFL` magic/schema header, contradicting SAVE-003/SAVE-004 and QA-004. The continue paths in `src/overworld.c` now call `InitFullSaveData()` before normal field restoration, including the Quest Log return path. This changes only the Full-owned header when the magic/version are absent.

### RC-F026 — Unique reusable TM rules were inconsistent across capacity/add/shop paths
**Status:** FIXED / CI PENDING  
Full treats TMs as permanent single-copy unlocks, but the transaction paths were not fully aligned. `AddBagItem` rejected an already-owned TM yet still accepted bulk counts when the TM was not owned, `CheckBagHasSpace` could report space for duplicate TMs, and marts could offer quantities greater than one. That created paths where a script/shop could treat a duplicate or bulk TM as receivable even though the permanent-unlock model requires exactly one logical copy. The bag-space check now rejects duplicate/bulk TMs, `AddBagItem` rejects TM counts other than one, and marts cap TM quantity at one. The RC freeze validator now locks these invariants and also verifies the TM Case sell path cannot remove a TM.

### RC-F027 — Direct-use trade-evolution items reached the party menu but had no evolution item effect
**Status:** FIXED / CI PENDING  
RC-F009 changed King's Rock, Metal Coat, Dragon Scale and Up-Grade to `ITEM_TYPE_PARTY_MENU` with `FieldUseFunc_EvoItem`, and `GetEvolutionTargetSpecies` already accepts `EVO_TRADE_ITEM` during item use. However, the generic item-effect engine still rejected those IDs because `IS_POKEMON_ITEM` ended at the berry range and `gItemEffectTable` had no `ITEM4_EVO_STONE` entries for the four trade-evolution items. The UI path therefore existed but the actual direct-use evolution could still report no effect. The four items are now explicitly recognized as Pokémon-usable and mapped to evolution-stone effects. The RC freeze validator locks both requirements.

### RC-F028 — Doubles AI history had per-side aliasing and out-of-bounds move-history reads
**Status:** FIXED / CI PENDING  
Gate 2A reviewed current `pret/pokefirered` upstream work on doubles AI and then confirmed the same failure mode directly in Full's active source: the vanilla history structure stores only two history slots, target move-history loops iterate eight entries, and `Cmd_if_has_move_with_effect` can index a four-move battler array with values 4..7. In doubles this can alias battlers on the same side and read outside the move array. Full already forces `BUGFIX`, so the repair is isolated to that path: battle history is now per battler, move history is bounded to `MAX_MON_MOVES`, recorded abilities/items are keyed by exact battler, and the initial doubles target is forced onto the opposite side. The frozen AI scripts remain unchanged; this is a safety/correctness repair rather than new competitive AI. `validate_frozen_bugfixes.py` now gates the repaired invariants.

### RC-F029 — Gary's battle parties were fixed to Squirtle, but the Oak's Lab starter state/dialogue still varied
**Status:** FIXED / CI PENDING  
Gate 11 found that the trainer-party data already cloned every Bulbasaur/Charmander rival branch to the frozen Squirtle/Blastoise roster, but Oak's Lab still assigned `RIVAL_STARTER_SPECIES` to Charmander or Bulbasaur for two player-starter choices. That meant the lab scene could explicitly announce that Gary received a non-Squirtle starter even though his battle party immediately used Squirtle, contradicting RIV-001's fixed-starter requirement. All three lab choices now assign `RIVAL_STARTER_SPECIES = SPECIES_SQUIRTLE`; the generic physical Poké Ball movement/IDs remain available for scene choreography. `validate_full_league_rosters.py` now gates the fixed Squirtle identity and the already-frozen identical rival party branches.

### RC-F030 — Doubles-AI repair reinterpreted a recorded hold effect as an item ID
**Status:** FIXED / CI PENDING  
During follow-up review of RC-F028, the new per-battler history path in `Cmd_get_hold_effect` called `ItemId_GetHoldEffect(BATTLE_HISTORY->itemEffects[battlerId])`. That history field is populated by `RecordItemEffectBattle` with the hold-effect value itself (for example `HOLD_EFFECT_FOCUS_BAND`), not an item ID. Passing that value back through the item-ID lookup could therefore return the hold effect of an unrelated low-numbered item and mislead AI decisions. The BUGFIX path now returns the recorded hold-effect value directly, matching the meaning of the stored field. `validate_frozen_bugfixes.py` now locks this invariant.

### RC-F031 — QOL-007 Repel audit initially inspected the wrong language script
**Status:** FALSE POSITIVE CORRECTED / STATIC PASS  
The first recovery pass inspected `data/scripts/repel.inc`, but `firered_es_modern` actually compiles `data/scripts/spanish/repel.inc`. The Spanish script already contained the chained-Repel implementation before recovery: stock check, Yes/No prompt, preference for `VAR_FULL_LAST_REPEL`, fallback to another available Repel, exact 100/200/250-step counters, and clean no-stock/No exits. The temporary edit to the generic non-target script was reverted to baseline, and `validate_rc_freeze.py` now points at the Spanish script that is actually compiled. Final interaction behavior remains a MyBoy requirement.

### RC-F032 — MODERN revision-0 build was not inheriting tested link synchronization fixes
**Status:** FIXED / CI PENDING  
Gate 12 pre-runtime review compared Full's link/trade paths with current tested revision-0xA bugfix work from upstream. Full builds `firered_es_modern` with `MODERN=1` but `GAME_REVISION=0`, so guards written only as `#if REVISION >= 0xA` were still excluded even though Full globally enables `BUGFIX`. Relevant link paths therefore missed fixes that wait for link-idle/fade completion and clear stale post-link callbacks. The BUGFIX path now covers `ClearFieldCallback`, link-battle teardown, multi-battle pre-init, wireless cable-club battle/trade startup, link full-save synchronization, canceled-trade exit and Union Room battle synchronization. `src/trade.c` differs from vanilla only by the canceled-trade BUGFIX guard and has been re-locked at its new audited blob. Final Full↔vanilla behavior still requires MyBoy Gate 12.

### RC-F033 — UBFIX still used incompatible two-argument/three-argument mon-data function aliases
**Status:** FIXED / CI PENDING  
Gate 2A reviewed current upstream UBFIX work and confirmed that Full still declared `GetMonData2` as a function alias of `GetMonData3` (and likewise for BoxMon) even though the signatures differ. Full forces `UBFIX` in MODERN builds, so keeping the incompatible alias defeats the intended undefined-behavior hardening at a very widely used data-access boundary. Under `UBFIX`, the two-argument accessors are now inline wrappers that call the three-argument functions with `NULL`; the original aliases remain only for non-UBFIX matching builds. `validate_frozen_bugfixes.py` now gates both wrappers.

### RC-F034 — Wireless communication status could index group-count arrays out of bounds in MODERN/UBFIX
**Status:** FIXED / CI PENDING  
Gate 12/2A review of current upstream UBFIX work found that Full's revision-0 wireless communication status screen still compiled the vanilla group-accounting path. Several activities use `NUM_GROUPTYPES` or `GROUPTYPE_NONE` as sentinel group IDs; the old path can feed those values directly into the four-element `groupCounts` array. Because Full forces `UBFIX`, the status screen now maps the revision-0xA activities to `GROUPTYPE_TOTAL`, bounds-checks the group type before indexing, and uses the corrected count-change logic under `UBFIX`. The first patch attempt accidentally replaced the forward declaration instead of the implementation; it was immediately discarded and the file was rebuilt from the pre-change commit before applying the corrected patch. The final source has one prototype and one implementation and is now gated by `validate_frozen_bugfixes.py`.

### RC-F035 — Hall-of-Fame event-state validator audited the generic script, not the Spanish script actually compiled
**Status:** FIXED / CI PENDING  
The Spanish target includes `data/scripts/spanish/hall_of_fame.inc`, while Gate 6 was validating `data/scripts/hall_of_fame.inc`. The generic file contained all Full KO-recovery hooks, but the Spanish file only cleared the vanilla Lugia/Ho-Oh/Deoxys flew-away flags. In the actual `firered_es_modern` ROM, Kanto static KO-pending flags plus Mew/Celebi recovery therefore would not have been reset after Hall of Fame. The audited Full reset logic has now been copied into the Spanish Hall-of-Fame script, and `validate_full_event_states.py` now checks that target-language file directly. The GitHub Actions workflow had the same generic-path blind spot in six Hall-of-Fame checks and now points to the Spanish script as well. A companion audit confirmed the generic and Spanish item-ball scripts are byte-identical; `validate_full_obtainability.py` now targets the Spanish file explicitly anyway to avoid future language-path drift.

### RC-F036 — Continuity documents still described an older code payload as current/validated
**Status:** FIXED / DOCUMENTED  
The second-pass audit found that `PROJECT_CONTINUITY.md` and `NEXT_SESSION.md` still described an older code-affecting commit and implied that later descendants were documentation-only / already covered by consolidated CI. Multiple functional audit repairs had been added after that state, so a crash or new session could incorrectly inherit an obsolete CI PASS or ROM checksum and freeze the wrong payload. Continuity has been rewritten to treat older CI/checksums as historical evidence only, require exact-current-HEAD CI before freeze, and include the new adversarial second-pass audit in the mandatory resume path.

