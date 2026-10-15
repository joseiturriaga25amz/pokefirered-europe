# Pokemon Rojo Fuego Full — Final MyBoy RC Checklist

**Purpose:** final runtime acceptance only after the candidate build is frozen and consolidated CI is green.  
**Required emulator:** MyBoy, per amendment A-001.  
**Bag rule:** vanilla 42-slot Items pocket, per amendment A-002. QA-005 and QA-006 from the historical workbook are superseded and must not be executed.

## Evidence rule

For each block record **PASS / FAIL / BLOCKED**, the exact commit SHA, save used, and only the screenshot/video needed to prove the branch being tested. A compile/static pass never substitutes a MyBoy pass.

## B10 MyBoy first-play runtime checkpoint — 2026-10-15 (diagnostic prototype only)

**Tester evidence:** user successfully built local `rojo-fuego-full-diagnostico.gba` from `prototype/follower-runtime` source HEAD `0774ebfdabbc28ed0796394a5451a06464e2e694` on Ubuntu/WSL; local build log SHA-1 `c8fc905eaaf290347646c784e2bf5dae4b6fe1dd`, pinned-source 386 normal/shiny build COMPLETE. User opened that ROM in My Boy on Android from a new game. My Boy version/device model not supplied. Ten screenshots supplied in conversation; findings below are verbal/visual runtime evidence, **not** independent automated runtime certification or final RC.

- **A01 PASS (observed):** boots, normal player naming/starter selection, Charmander chosen in Oak's lab, first Gary battle playable/completable.
- **A02 PASS (observed):** exactly one Charmander visibly appeared immediately after starter confirmation on clear tile.
- **A03 PARTIAL/POSITIVE:** still screenshots show recognizable Charmander front/back/side views, readable normal tail-flame colors; user reports following in all four directions in lab and Pallet. Still images alone cannot verify frame cadence or every directional animation.
- **A04 PARTIAL / VISUAL DEFECT:** walking/corners and circling Pallet houses followed naturally. On ledge jumps the user reports follower jumps after player but can appear on the same tile as player at landing until player moves; audit transient overlap and safe trail/reposition, do not call ledges fully passed. Running stress remains untested.
- **A05 PARTIAL / SCRIPTED-INTERIOR UX FAIL:** ordinary Pallet house entry/exit works. On Viridian Mart Oak Parcel scripted clerk interaction follower disappears and returns only after dialog; on return to Oak, follower hides throughout Gary arrival/Pokédex scene, returning afterward. User dislikes abrupt disappearance. Distinguish safe dialog vs forced-movement cinematic staging; further warp/door cases pending.
- **A06 NOT EXECUTED:** narrow path / moving NPC pressure scenario not yet explicitly tested.
- **A07 PARTIAL / UX FAIL for trainer and wild battle (2026-10-15 My Boy):** starter Gary battle completes and follower returns, but vanishes abruptly upon Gary's prebattle dialog. Wild encounter in Route 1 also begins with abrupt follower disappearance during battle-transition animation; follower returns after finishing battle. Wild battle execution is positive; presentation acceptance FAIL in both cases. Need stage/hold or controlled transition without unsafe script/collision leaks.
- **A08 FAIL (repro):** after normal in-game save and loading saved game in My Boy, no follower appears even after walking on open tiles; entering a Pallet Town house causes it to reappear, and it persists on leaving. No claim of missing party data or corrupted save.
- **A09 VISUAL FAIL (repro):** opening Start menu/Save hides follower; reading a Pallet Town sign also hides it, though the player remains visible and no follower removal is narratively needed. User requests follower visible and stationary for menus, signs and ordinary NPC text. Menus, reading and saving themselves appear functional; closing-menu behavior remains to check.

**Source investigation — not yet corrected:** `src/full_follower.c::ShouldSuppressFollower` suppresses whenever `ArePlayerFieldControlsLocked()`; `src/start_menu.c::ShowStartMenu` explicitly locks controls. Distinguish field Start/Save menu from unsafe cutscene/control locks; do not bypass all locks globally. `FullFollower_OnLocalMapReady` returns without creating the follower task during `QL_IS_PLAYBACK_STATE`; normal saved-game resume can traverse FireRed Quest Log playback; `src/quest_log.c::Task_EndQuestLog` restores control without reinitializing the follower task. This is a strong source-level explanation for A08, **pending a narrowly scoped fix and exact-ROM My Boy retest**.

**A07 prebattle follower presentation — user-requested UX acceptance criterion (2026-10-15, NOT IMPLEMENTED):** For Gary and other trainer encounters, favor moving the existing visual follower to a safe adjacent position beside the player, facing the challenging trainer while dialogue runs; retain it on-screen through dialogue until the actual battle-screen transition. After the battle it should resume normal trailing behavior automatically. For wild encounters or cramped/scripted scenes where safe positioning is impossible, prefer remaining visible until the battle transition; if necessary use a deliberate brief fade/white dissolve/recollection cue rather than instantaneous pop-out. A literal Poké Ball animation is not required. Do **not** blindly exempt all script locks from follower suppression or move the object across obstacles/NPCs; review trainer sight, map event scripts, palette/OAM, sprite lifetime, battlefield transition and save/link safety before implementing. In future runtime QA inspect opening Gary dialogue, trainer-sight NPC, narrow scripted battle and a wild encounter, including safe reappearance after. The follower remains a projection of the actual eligible party Pokémon, not a new saved entity. UX preference recorded, **implementation/CI/My Boy retest pending**.

**New user proposal (not automatically implemented):** show only Gary/Blue with his Squirtle → Wartortle → Blastoise lineage in story scenes; unlike the player's dynamic party follower, this must be designed as Gary-specific staged event presentation / controlled motion, with safe NPC collision and cutscene handling. Existing A-007 approves Gary signature companion staging, but this new moving-through-story behavior needs scoping. Do not mix it into A08/A09 lifecycle fixes.

**Oak Charmander guaranteed shiny — approved user-specific requirement (2026-10-15, NOT IMPLEMENTED):** At Professor Oak's normal laboratory starter choice, ONLY the player's Charmander gift (National #004, level 5) must be genetically shiny at creation, not merely have a shiny-looking follower sprite. Preserve legitimate player OT and personality/shiny semantics so the overworld follower, battle, party summary, subsequent Charmeleon and Charizard evolutions, and save/trade continue to report shiny consistently. Leave Bulbasaur/Squirtle choices, other encountered/gifted Charmander, Gary's Squirtle line, global shiny rates, starters' moves/level and standard starter-dialogue/variable progression unchanged. The existing starter map calls generic `givemon PLAYER_STARTER_SPECIES, 5` and `ScriptGiveMon` uses `CreateMon` without guaranteed shiny; implementation must scope the exceptional personality selection to Oak's player-Charmander creation (never globally alter `ScriptGiveMon`). Tests: start new game choose Charmander and verify shiny in battle/summary/follower; level to evolutions and check persistence; start new game choose Bulbasaur/Squirtle unaffected; save-reload/trade ABI safety. Existing private user ROM at technical SHA `0774ebf` is UNMODIFIED and has normal Charmander. Do not claim this is implemented or validated until new source, exact HEAD CI and My Boy retest. Do not combine gameplay mutation with ongoing first-build QA.

**Second My Boy field pass — Route 1, Viridian, Pallet (2026-10-15, same diagnostic SHA-1 `c8fc905eaaf290347646c784e2bf5dae4b6fe1dd`):** User reports catching Mankey and Rattata and successful follower identity/graphics for these additional species under the same current prototype limitations; this is a **three-species runtime sample, not proof of all 386**. Corners and ordinary footsteps look natural. During ledge jumps, follower can temporarily land on/overlap the player tile until the player takes another step (A04 geometry defect). During tall-grass wild battle entry the follower instantly vanishes during transition and returns afterward (A07 presentation defect). During the forced Viridian Mart parcel script, Oak Parcel/Pokédex cutscenes, and simple Pallet sign interaction, the follower instantly disappears and later reappears (A05/A09 contextual recall defect). User also observed sudden disappearance during Nurse Joy healing. In a healing context, the chosen design direction is an intentional gentle recall/fade **when actual healing begins**, followed by natural reappearance, because the same party companion is being healed. No Poké Ball effect is mandated, no implementation has occurred; ensure any future effect works with six-party healing, battle, save, quest log and cutscene states.

**Technical rationale to investigate:** `src/full_follower.c::ShouldSuppressFollower` globally returns TRUE for script enable/field control lock and ledge-jump copyable movement; `RefreshFollower` immediately removes the object when suppressed, while `FollowRecordedPlayerSteps` may recall on unexpected steps. Generic script lock from signs and the Viridian Mart's `lockall` scene can therefore remove the follower abruptly. Do not solve by globally disabling script protection: classify dialog, trainer battle, in-field menus, scripted movement, warp, heal and ledges separately and make removal state-dependent. Maintain live party identity, collision, palette/OAM safety, link/quest-log isolation, and no persistent object-save changes. Verify after isolated technical fixes on exact new ROM in My Boy.

**State:** B10 OPEN; diagnostic runtime QA found menu/save-load, dialog, wild/trainer battle, healing and ledge presentation defects. Follow-up technical corrections and fresh exact-ROM My Boy retest required; no final RC acceptance, no master integration. **Next:** finish low-risk remaining A04–A07/A09 observations on same ROM and separately fix/revalidate Quest Log return and safe Start-menu persistence. Rebuild ROM at exact technical fix HEAD; preserve user's original save and avoid making claims from CI alone.

---

## RC-01 — Boot, save compatibility and persistence
**Covers:** QA-002, QA-004, QA-007, QA-008 plus regression around A-002.

1. Boot the exact RC ROM in MyBoy and start a new game.
2. Save, close/reopen MyBoy, reload, change map, save again and reload.
3. Open a known-good vanilla Spanish save in the Full ROM; save/reload it.
4. Acquire ordinary items until the normal 42-slot behavior is exercised; do not attempt the superseded 142-slot test.
5. Visit maps/events that consume Full flags/vars, save/reload, and revisit them.

**PASS:** no black screen/crash, Spanish data remains intact, saves reopen, vanilla progress survives migration, Full event state persists, normal Items pocket behaves like vanilla.

## RC-02 — Physical/special split and battle interactions
**Covers:** QA-009..QA-020.

Use controlled Pokémon with deliberately different Atk/SpA and Def/SpD. Exercise Shadow Ball, Crunch, Waterfall, Fire Punch, Sludge Bomb, Leaf Blade and Hidden Power, then test contact effects, burn, Reflect/Light Screen, Counter/Mirror Coat and a boss AI battle.

**PASS:** damage follows the frozen per-move category, Hidden Power is always special, contact is independent of category, burn/screens/counter mechanics use the new category correctly, and AI does not display category-blind choices.

## RC-03 — Evolution matrix and pre-National Pokédex
**Covers:** QA-023..QA-037.

1. Level Kadabra, Machoke, Graveler and Haunter through 36.
2. Use Metal Coat on Scyther and Onix, Dragon Scale on Seadra, Up-Grade on Porygon, King's Rock on Poliwhirl and Slowpoke.
3. Use Sun Stone/Moon Stone on Eevee.
4. Evolve a sufficiently friendly Golbat before National Dex.
5. Inspect Pokédex before/after National Dex and attempt the vanilla-forbidden pre-National non-Kanto/egg trade.

**PASS:** every evolution reaches the frozen target with no trade requirement; Crobat can exist pre-National without corrupting the Kanto Pokédex UI; vanilla trade restriction remains.

## RC-04 — TMs/HMs, Move Reminder, tutors and field QoL
**Covers:** QA-038..QA-049.

1. Teach the same TM to two compatible Pokémon; confirm the TM remains.
2. Attempt to obtain/buy a duplicate unique TM and attempt to sell/discard one.
3. Verify an HM field move still requires the Pokémon to know the HM.
4. Use Move Reminder and confirm exactly $2,000 is charged.
5. Use a tutor once for free, then repeat and confirm the approved price.
6. Run inside a normal interior after Running Shoes; verify explicitly forbidden tiles still block running.
7. Exhaust Repel with another in stock: test Yes, No, last-item/no-stock, and fallback behavior.
8. Toggle the EV summary view and compare all six values/total with a known EV test Pokémon.
9. With a living non-Egg Synchronize lead, perform a controlled encounter sample.

**PASS:** reusable/unique TM rules hold, HMs remain vanilla, pricing is exact, no Repel loop/softlock occurs, EV values are exact, and Synchronize behaves near the intended 50% over a sufficiently large sample.

## RC-05 — Safari
**Covers:** QA-050, QA-051.

1. Enter with 30 Safari Balls and walk beyond 650 steps without exhausting the balls.
2. In a second run, consume all 30 balls.

**PASS:** walking does not end the Safari session; reaching zero balls does.

## RC-06 — Wild encounters and Altering Cave spot-check
**Covers runtime spot-check for:** QA-052..QA-070. Exact slot rates are CI-validated.

1. Spot-check representative FireRed exclusives and Full additions in their frozen areas.
2. In Altering Cave, use the researcher selector for each of the nine states and trigger at least one encounter per state.

**PASS:** no LeafGreen exclusives replace FireRed exclusives; all nine Altering Cave states produce the intended species and the selector never strands the player.

## RC-07 — Fossils and Fighting Dojo
**Covers:** QA-071..QA-078.

1. Take one Mt. Moon fossil; confirm the other remains unavailable before revival.
2. Revive the first in Cinnabar, return, obtain the second, and revive it; also revive Old Amber.
3. Confirm Dojo rematch/reward is blocked before Sabrina.
4. After Sabrina, complete the second trial once from each possible first Hitmon choice.
5. Repeat the reward attempt with party/storage constrained so the first give attempt cannot complete.

**PASS:** both fossils plus Aerodactyl are obtainable in one save, the opposite Hitmon is awarded exactly once, and a full destination never destroys the reward.

## RC-08 — Static legendaries and mythicals
**Covers:** QA-079..QA-105.

For Articuno, Zapdos, Moltres, Mewtwo, Lugia, Ho-Oh, Deoxys, Mew and Celebi test the applicable branches on disposable saves: flee, KO, capture, Hall of Fame/respawn transition.

**PASS:** flee does not permanently consume the encounter; KO follows the frozen pending/respawn rule; capture permanently closes only that encounter; species, level, moveset and fateful state match the frozen specification.

## RC-09 — Ticket quests, Mew/Celebi gating and roaming beasts
**Covers:** QA-106..QA-118.

1. Confirm Hall of Fame alone does not auto-grant tickets.
2. Exercise incomplete and complete MysticTicket prerequisites.
3. Execute Aurora quest in the frozen order and verify Birth Island access/Deoxys.
4. Attempt Mew before its prerequisites, then complete the mansion sequence.
5. Attempt Celebi before its prerequisites, then after National Dex + Network Machine + all three beasts.
6. Run the sequential beasts through flee, Roar, KO, route change, capture and Pokédex area display.

**PASS:** quest order cannot be bypassed, no ticket appears early, each beast identity/state persists correctly, KO/Roar cannot erase the sequence, and Pokédex area tracks only the active seen beast.

## RC-10 — Economy and renewable resources
**Covers:** QA-119..QA-124.

1. Buy Porygon twice at exactly 5,000 coins each.
2. Before/after National Dex compare renewable evolution items.
3. Verify postgame Lucky Egg purchase at $30,000 while Chansey's original method still exists.
4. Trigger the Resort Gorgeous Jacki/Gillian/Celina VS Seeker circuit and inspect payouts.
5. Re-test one paid tutor against the approved table.
6. On Two Island, compare berry inventory before National Dex and after National Dex; verify exact prices.
7. Use each EV-reducing berry on a Pokémon with the corresponding EV >0 and friendship below max, then again with that EV at 0 but friendship below max.

**PASS:** prices/inventory match the freeze; EV berry lowers its target EV by 10 to a floor of 0 and can still raise friendship at 0 EV; it has no effect only when target EV is 0 and friendship is already max.

## RC-11 — Bosses, League and Gary
**Covers runtime behavior for:** QA-126..QA-131. Frozen party legality/rosters are CI-validated by MOV-006.

1. Fight representative early/mid/late Gym leaders, first League and rematches.
2. Observe maximum healing-item use where frozen.
3. Verify held items activate on representative rematch Pokémon.
4. Play all Gary encounters on the Full path and the postgame rematch.

**PASS:** levels/rosters seen in-game match the frozen data, healing caps are respected, held items work, and Gary always follows the approved Squirtle route/progression.

## RC-12 — Link compatibility in MyBoy
**Covers:** QA-132, QA-133 plus QA-037 regression.

Using MyBoy link emulation, perform Full → vanilla and vanilla → Full legal Kanto trades; separately attempt the pre-National blocked cases.

**PASS:** legal Gen III-compatible Pokémon trade both directions without structural corruption; forbidden pre-National cases remain blocked; save/reload works on both sides afterward.

## RC-13 — Frozen bug regressions
**Covers:** QA-134..QA-139.

Run focused repros for roamer IV persistence, fishing-area bounds, L=A held repeat, Move Reminder scroll indicators, two-slot party animation memory path, and Berry Crush sparkle behavior.

**PASS:** none of the original reproduction cases reappears and no adjacent UI/input regression is introduced.

## Final acceptance

The RC may be called **v1.0 final** only when:
- consolidated CI for the exact tested SHA is green;
- this checklist has no FAIL/BLOCKED item that affects acceptance;
- any discovered regression is fixed and the affected block plus its adjacent regression checks are re-run;
- the tested ROM checksum is recorded together with the MyBoy results.
