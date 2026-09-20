# Pokémon Rojo Fuego Full v1.0 — Final Audit Plan

**Goal:** detect specification drift, illegal data, state-machine defects, save/compatibility regressions, softlocks and runtime-only bugs before declaring v1.0 final.

This audit is intentionally broader than "does it compile?". It separates what can be proven statically from what must be demonstrated in MyBoy.

---

## Gate 0 — Freeze the exact Release Candidate

Before final runtime testing:

1. choose one exact branch HEAD;
2. require the full GitHub Actions workflow to pass on that exact SHA;
3. build `firered_es_modern`;
4. record the ROM SHA-1;
5. do not modify code while that RC is being tested;
6. if any code changes, invalidate the old runtime result and create a new RC SHA/checksum.

**Exit criterion:** one immutable code candidate identified by Git SHA + ROM SHA-1.

---

## Gate 1 — Specification reconciliation

Purpose: ensure production did not silently diverge from approved design.

Audit all 154 implementation requirements against:

1. A-001..A-004 amendments;
2. frozen preproduction specification;
3. frozen matrix;
4. frozen decision log;
5. current implementation.

For every requirement classify it as:

- **implemented + automated evidence**;
- **implemented + runtime evidence required**;
- **superseded by amendment**;
- **not applicable by frozen design**;
- **open defect**.

Special attention:
- historical 142-slot bag rows must resolve to A-002, never be restored;
- historical mGBA rows must resolve to A-001/MyBoy;
- no chat-only decision may remain necessary to understand expected behavior.

**Exit criterion:** no unexplained requirement and no contradictory active source of truth.

---

## Gate 2 — Baseline and diff audit

Compare RC against `baseline-spanish-vanilla`.

Audit:
- every modified source/data file;
- every new file;
- every changed struct/constant;
- maps/scripts touched by Full;
- trainers, encounters, items and evolution tables;
- bugfix ports.

Questions for each diff:
- Is this change required by a frozen requirement or approved technical repair?
- Did it alter adjacent vanilla behavior unnecessarily?
- Did it accidentally modernize Gen IV+ mechanics?
- Did it introduce a new ID or layout change?
- Is there dead/provisional/debug code left behind?

**Exit criterion:** all meaningful diffs have a reason and no unexplained collateral modifications remain.

---

## Gate 3 — Build, compiler and automated invariant audit

Require:
- clean `firered_es_modern` build;
- no new compile/link warnings attributable to Full;
- all CI gates PASS;
- `validate_full_trainer_sets.py` PASS;
- `validate_rc_freeze.py` PASS.

Also inspect the validators themselves for blind spots:
- false positives;
- false negatives;
- regexes that only prove token presence rather than behavior;
- requirements not represented by any static assertion.

**Exit criterion:** automated gates are green **and** their coverage limitations are documented.

---

## Gate 4 — Data integrity and legality

### Pokémon / moves / items
Verify:
- no new IDs;
- all references resolve;
- no out-of-range species/move/item;
- Pokémon and BoxPokemon sizes remain vanilla-compatible;
- every frozen trainer set is legal;
- every held item exists;
- all levels/IVs match frozen tables;
- no unintended enemy EV optimization;
- no competitive nature forcing.

### Move mechanics
Cross-check:
- category;
- contact;
- power;
- accuracy;
- PP;
- secondary effects;
- Hidden Power;
- Counter/Mirror Coat;
- burn/screens;
- Hustle;
- AI damage evaluation.

**Exit criterion:** zero unresolved data/legal incompatibilities.

---

## Gate 5 — Save architecture and migration audit

Static review:
- `SaveBlock1 == 0x3D68`;
- Full header exactly occupies vanilla `unused_3D24[16]`;
- no downstream offset moved;
- `unused_348C[400]` untouched after A-002;
- Full flag/var namespaces do not collide;
- schema initialization writes only Full-owned bytes;
- existing vanilla fields are not reset during migration;
- save encryption/checksum paths remain untouched unless explicitly required.

Runtime review in MyBoy:
- new game save/load;
- Full save save/load;
- vanilla Spanish save import;
- event flags/vars persistence;
- party/PC/bag integrity across multiple saves/reloads.

**Exit criterion:** no corruption, reset, black screen or migration loss.

---

## Gate 6 — Event/state-machine audit

For every custom or modified persistent event, draw/inspect its state machine and test every terminal branch.

Required systems:
- second fossil;
- second Fighting Dojo reward;
- static legendary KO/flee/capture/Hall of Fame;
- Lugia/Ho-Oh/Deoxys event flags;
- sequential Suicune → Raikou → Entei;
- Roar/KO/route movement/identity persistence;
- MysticTicket quest;
- AuroraTicket quest;
- Mew mansion sequence;
- Celebi Berry Forest sequence;
- Altering Cave selector;
- Porygon repeat purchase;
- tutor first/free and repeat/paid paths;
- berry-shop progression.

For each:
- prerequisites;
- skipped prerequisites;
- repeated interaction;
- full party/PC where relevant;
- save/reload mid-state;
- leave/re-enter map;
- KO;
- flee;
- capture;
- Hall of Fame reset where applicable.

**Exit criterion:** no unreachable state, double reward, permanent loss, repeat exploit or softlock.

---

## Gate 7 — Encounter and obtainability audit

Prove that every intended Gen I–III species in v1.0 is obtainable by an approved method and that no required method depends on LeafGreen/event distribution/another cart.

Audit:
- FireRed exclusives preserved;
- approved LeafGreen families inserted at exact rates;
- starters/evolutions;
- Eevee/evolutions;
- Safari optimized slots;
- Altering Cave nine states;
- fossils;
- Dojo Hitmons;
- trade-evolution replacements;
- baby breeding requirements;
- all legendary/mythical routes;
- renewable evolution items/resources.

This gate must explicitly look for hidden prerequisites such as held incense, breeding restrictions, one-time gifts, unavailable parents or unavailable items.

**Exit criterion:** no species required by the Full vision is accidentally unobtainable.

---

## Gate 8 — Economy and repeatability audit

Verify exact frozen prices and renewable paths.

Check:
- type boosters;
- held items;
- evolution items;
- PP Up / Ether family;
- Lucky Egg;
- TM44;
- Porygon;
- tutors;
- Move Reminder;
- Two Island berries;
- Resort Gorgeous payout circuit;
- VS Seeker repeatability.

Look for:
- price overflow;
- zero-price sell exploits;
- accidental availability too early;
- supposed renewable resource that is still one-time;
- stock gated by wrong flag;
- duplicated unique TM.

**Exit criterion:** economy matches frozen rules and no obvious duplication/infinite-money exploit was introduced by Full.

---

## Gate 9 — UI / input / QoL regression audit

Runtime MyBoy focus:
- EV summary toggle;
- normal summary navigation;
- Move Reminder scrolling;
- L=A held repeat;
- party two-slot transitions;
- TM Case;
- reusable TM behavior;
- Repel prompt Yes/No/no-stock;
- indoor running and forbidden tiles;
- Safari entry/exit;
- berry use and messages;
- evolution-item party-selection route.

Look for:
- sprite leaks;
- text overflow;
- stale window/tilemap;
- wrong callback;
- softlock on B/cancel;
- repeated input;
- wrong sound/message;
- behavior that works only in one language path.

**Exit criterion:** all modified interfaces can be entered, used, cancelled and re-entered safely.

---

## Gate 10 — Battle and AI runtime audit

Use controlled test Pokémon to prove:
- physical/special damage source stats;
- defensive stats;
- burn;
- Reflect/Light Screen;
- contact abilities;
- Counter/Mirror Coat;
- Hidden Power;
- representative moves whose category changed;
- boss held items;
- healing limits;
- AI decisions under changed categories.

Static data correctness is not enough: this gate validates actual battle behavior.

**Exit criterion:** no category/contact mismatch or obvious AI regression.

---

## Gate 11 — Boss / Gary / League audit

Cross-check runtime rosters against frozen data:
- eight first Gym fights;
- approved rematches;
- first Elite Four;
- rematch Elite Four;
- every Gary encounter;
- Champion;
- postgame Gary.

Verify:
- species;
- levels;
- legal moves;
- IV targets;
- held items;
- healing item limits;
- Gary's approved Squirtle/Blastoise route and rotation.

**Exit criterion:** runtime matches frozen roster data with no illegal or unintended variant.

---

## Gate 12 — Gen III link/trade compatibility

Required in MyBoy:
- Full → vanilla legal Kanto Pokémon;
- vanilla → Full legal Kanto Pokémon;
- save/reload both sides;
- held item/moves/IV/EV integrity;
- blocked pre-National egg/non-Kanto cases;
- fateful-event safeguards for Mew/Deoxys as applicable.

Trading compatibility concerns Pokémon data, not round-tripping the same Full save through vanilla.

**Exit criterion:** legal trade round-trip of Pokémon data works without structural corruption.

---

## Gate 13 — Historical bug regression sweep

Reproduce/falsify the original bug classes:
- roamer IV setter;
- roamer Roar persistence;
- roamer status size;
- fishing Pokédex OOB;
- pre-National trade egg check;
- HP recalc clamp;
- Move Reminder second scroll indicator;
- L=A repeat;
- party-menu buffer leak path;
- Berry Crush sparkle;
- other BUGFIX/UBFIX paths touched by production.

**Exit criterion:** no known historical reproduction remains.

---

## Gate 14 — Long-session / progression regression

Do one broad progression smoke on the exact RC, prioritizing transitions rather than grinding:

- new game;
- several badges;
- key HM progression;
- Pokémon Tower / Silph / Cinnabar / League;
- Sevii Network Machine;
- postgame/National Dex;
- representative Full event;
- save/reload at multiple points.

This is specifically for defects that isolated tests miss:
- state contamination;
- map transition errors;
- cumulative save corruption;
- event order assumptions;
- resource exhaustion;
- long-lived globals.

**Exit criterion:** no progression blocker or cumulative regression.

---

## Gate 15 — Final release consistency audit

Before final tag/merge:

- exact HEAD CI green;
- exact tested ROM checksum recorded;
- no runtime FAIL/BLOCKED acceptance item;
- all repaired defects re-tested;
- `RC_AUDIT_LOG.md` up to date;
- `PROJECT_CONTINUITY.md` reflects final state;
- no TODO/provisional wording for finished systems;
- no debug cheats or temporary test scripts enabled;
- release notes identify A-001/A-002 deviations from historical freeze;
- final version/tag points to the actually tested SHA.

**Only after Gate 15 may v1.0 be called final.**

---

# Defect triage during final audit

## Release blocker
Examples:
- crash/black screen;
- save corruption;
- softlock/progression blocker;
- unobtainable required Pokémon/content;
- wrong permanent event state;
- broken trade compatibility;
- major battle mechanic incorrect.

Fix immediately, create new RC, rerun affected + adjacent gates.

## Major
Examples:
- wrong reward/price/roster;
- repeatability broken;
- QoL feature materially wrong;
- encounter unavailable at approved location/rate.

Fix before release and rerun affected gates.

## Minor
Examples:
- text wording/layout;
- cosmetic animation issue;
- non-blocking UI inconsistency.

Normally fix before final if low-risk; otherwise document explicitly. Never silently ignore.

---

# Audit principle

The audit is adversarial: try to make the ROM fail.

Do not test only the happy path. Prefer:
- boundary values;
- repeated interactions;
- cancel/back paths;
- full inventory/party/storage;
- save/reload mid-sequence;
- entering a system too early;
- entering after completion;
- KO/flee/capture variants;
- link restrictions;
- post-National transitions.

A system is not accepted because its code "looks right"; it is accepted when the strongest applicable static and runtime evidence agree.
