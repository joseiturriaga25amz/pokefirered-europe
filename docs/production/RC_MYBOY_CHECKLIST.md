# Pokemon Rojo Fuego Full — Final MyBoy RC Checklist

**Purpose:** final runtime acceptance only after the candidate build is frozen and consolidated CI is green.  
**Required emulator:** MyBoy, per amendment A-001.  
**Bag rule:** vanilla 42-slot Items pocket, per amendment A-002. QA-005 and QA-006 from the historical workbook are superseded and must not be executed.

## Evidence rule

For each block record **PASS / FAIL / BLOCKED**, the exact commit SHA, save used, and only the screenshot/video needed to prove the branch being tested. A compile/static pass never substitutes a MyBoy pass.

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

## RC-09 — Legendary narrative V2, Mew/Celebi gating and roaming beasts
**Covers:** QA-106..QA-118, as superseded by A-005.

1. Confirm Hall of Fame alone does not auto-grant either legendary ticket and that Celio never distributes MysticTicket/AuroraTicket or introduces the roaming beasts.
2. Complete the maritime/birds investigation: Articuno, Zapdos and Moltres must only need to be **seen**; its completion grants MysticTicket and enables Lugia access at Navel Rock.
3. Confirm Ho-Oh is not opened merely by obtaining MysticTicket; its Navel Rock access is unlocked only by completing the Suicune → Raikou → Entei capstone.
4. Complete the Pewter Museum / space-anomaly investigation and verify its scientist grants AuroraTicket and enables Birth Island/Deoxys without a Celio handoff.
5. Complete the Mewtwo → Pokémon Mansion/Mew epilogue: preserve the historical diary material, observe the approved present-day/overworld Mew staging, and interact with the final visible Mew before battle.
6. Complete the independent Berry Forest Celebi nature investigation; capturing all three beasts must not be a causal prerequisite.
7. Trigger the first roaming-beast cinematic: Suicune focus with Raikou and Entei present, no battle, all three marked seen, then verify only Suicune is active first and the sequence advances Suicune → Raikou → Entei.
8. Exercise route tracking, encounter, flee, Roar, KO and capture branches for each active beast, including persistence across save/load.

**PASS:** A-005 quest ownership and order cannot be bypassed; Celio remains network-only; no ticket appears early; Ho-Oh stays gated behind the beast capstone; Mew/Celebi use their approved independent narratives; each beast identity/state persists correctly; and Pokédex tracking follows only the active roamer after the initial all-seen cinematic.

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
