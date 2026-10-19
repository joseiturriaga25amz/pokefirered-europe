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
- **A05 PARTIAL / SCRIPTED-INTERIOR UX FAIL:** ordinary entrances/exits work repeatedly: 5 cycles each at Viridian trainer school house, Pokémon Center and Mart (15 total), with no permanent follower loss or duplication observed. Sometimes the follower appears visually at/with the player tile on map arrival and becomes distinct only after the player moves; a safe nearby-tile spawn could improve this. Forced Viridian Mart Oak Parcel clerk script, Oak/Gary/Pokédex scene and upstairs Pokémon Center tutorial abruptly hide follower. Pokémon Center escalator ascent does not show companion accompanying player. Distinguish safe dialogue, escalator/warp and forced-movement scene.
- **A06 PARTIAL / VISUAL DEFECT:** user stood near a wandering NPC and moved Mankey into its route. NPC continued normally but visibly overlaid Mankey in the same tile; no deadlock. Collision/occlusion should be judged independently of nonblocking follower design, without making follower a gameplay obstacle. Additional high-density NPC stress deferred.
- **A07 PARTIAL / UX FAIL for trainer and wild battle (2026-10-15 My Boy):** Oak's-lab Gary battle works but follower vanishes abruptly upon prebattle dialog; Route 1 wild encounter likewise removes follower during transition, returning afterward. In Viridian Forest a trainer detects the player from distance; companion disappears when trainer approaches for battle. At Brock, companion disappears as soon as initial conversation begins (user has not reported victory). Need distinguish trainer sight, scripted and wild battle states while avoiding unsafe NPC/collision persistence.
- **A08 FAIL (repro):** after normal in-game save and loading saved game in My Boy, no follower appears even after walking on open tiles; entering a Pallet Town house causes it to reappear, and it persists on leaving. No claim of missing party data or corrupted save.
- **A09 VISUAL FAIL (repro):** opening Start menu/Save hides follower; reading a Pallet Town sign also hides it, though the player remains visible and no follower removal is narratively needed. User requests follower visible and stationary for menus, signs and ordinary NPC text. Menus, reading and saving themselves appear functional; closing-menu behavior remains to check.

**Source investigation — not yet corrected:** `src/full_follower.c::ShouldSuppressFollower` suppresses whenever `ArePlayerFieldControlsLocked()`; `src/start_menu.c::ShowStartMenu` explicitly locks controls. Distinguish field Start/Save menu from unsafe cutscene/control locks; do not bypass all locks globally. `FullFollower_OnLocalMapReady` returns without creating the follower task during `QL_IS_PLAYBACK_STATE`; normal saved-game resume can traverse FireRed Quest Log playback; `src/quest_log.c::Task_EndQuestLog` restores control without reinitializing the follower task. This is a strong source-level explanation for A08, **pending a narrowly scoped fix and exact-ROM My Boy retest**.

**A07 prebattle follower presentation — user-requested UX acceptance criterion (2026-10-15, NOT IMPLEMENTED):** For Gary and other trainer encounters, favor moving the existing visual follower to a safe adjacent position beside the player, facing the challenging trainer while dialogue runs; retain it on-screen through dialogue until the actual battle-screen transition. After the battle it should resume normal trailing behavior automatically. For wild encounters or cramped/scripted scenes where safe positioning is impossible, prefer remaining visible until the battle transition; if necessary use a deliberate brief fade/white dissolve/recollection cue rather than instantaneous pop-out. A literal Poké Ball animation is not required. Do **not** blindly exempt all script locks from follower suppression or move the object across obstacles/NPCs; review trainer sight, map event scripts, palette/OAM, sprite lifetime, battlefield transition and save/link safety before implementing. In future runtime QA inspect opening Gary dialogue, trainer-sight NPC, narrow scripted battle and a wild encounter, including safe reappearance after. The follower remains a projection of the actual eligible party Pokémon, not a new saved entity. UX preference recorded, **implementation/CI/My Boy retest pending**.

**New user proposal (not automatically implemented):** show only Gary/Blue with his Squirtle → Wartortle → Blastoise lineage in story scenes; unlike the player's dynamic party follower, this must be designed as Gary-specific staged event presentation / controlled motion, with safe NPC collision and cutscene handling. Existing A-007 approves Gary signature companion staging, but this new moving-through-story behavior needs scoping. Do not mix it into A08/A09 lifecycle fixes.

**Oak Charmander guaranteed shiny — HISTORICAL APPROVAL WITHDRAWN by user on 2026-10-19; NOT IMPLEMENTED:** The user expressly rescinds the October 15 request to force shiny on the player's Charmander starter at Professor Oak's laboratory. **Current requirement: all three Oak starters, including Charmander, use ordinary Gen III/Full personality and shiny generation; no guaranteed shiny, special encounter odds, forced personality, cosmetic shiny-only follower or starter-specific bias.** Legitimately shiny Pokémon must still use their real shiny overworld palette and preserve normal species/evolution/save/trade data. The starter is currently received through generic `givemon PLAYER_STARTER_SPECIES, 5` and `ScriptGiveMon` calls `CreateMon`; no gameplay rollback is required. Treat the former request as superseded history, not a pending feature; remove it from future implementation/QA to-do lists while leaving dated history visible.

**Follower ambient idle animation — 2026-10-19, USER REQUEST / PROPOSED / NOT IMPLEMENTED:** User likes the sense of continuous life in Pokémon Quetzal follower animations and asks whether our single follower can animate naturally **when standing still**. Current follower graphics have four direction-aware walk frames and standing/facing animation commands hold the first frame (`sFollowerPilotFace*[]`). Evaluate selective idle loops/poses: slight breathing/blinking/tail movements for ground Pokémon, flame flicker for Charizard, gentle persistent hovering for levitating species, optional low flight while walking with landing when idle for suitable species. **Do not indiscriminately loop walking-in-place or make every species bob:** respect biology, sprite cadence, palette/OAM, tile geometry and transitions. Quetzal is behavioral inspiration only; do not copy unavailable/unlicensed source/assets. Feasibility/implementation are separate from B10 critical fixes, and must be validated on exact ROM in My Boy.

**Naturalness/authenticity review — 2026-10-19, NO OTHER GAMEPLAY CHANGE APPROVED:** User wants a conservative review of older personal design choices that may weaken authentic Kanto immersion. Discuss, without changing: (1) Lance's deliberately shiny red Gyarados, (2) Gary/Blue's fixed Squirtle→Blastoise rival line regardless of chosen player starter, (3) signature overworld Pokémon beside many major trainers, (4) legendary/mythical and high-value reward distribution, and (5) modern QoL such as HM licenses, reusable TMs and trade-free evolution. Distinguish authored narrative rewards from automatic forced rarity and natural species roles. Do not undo integrated production gameplay based on this request; specific design decisions require deliberate user approval and isolated validation/integration/CI/My Boy QA.

**Second My Boy field pass — Route 1, Viridian, Pallet (2026-10-15, same diagnostic SHA-1 `c8fc905eaaf290347646c784e2bf5dae4b6fe1dd`):** User reports catching Mankey and Rattata and successful follower identity/graphics for these additional species under the same current prototype limitations; this is a **three-species runtime sample, not proof of all 386**. Corners and ordinary footsteps look natural. During ledge jumps, follower can temporarily land on/overlap the player tile until the player takes another step (A04 geometry defect). During tall-grass wild battle entry the follower instantly vanishes during transition and returns afterward (A07 presentation defect). During the forced Viridian Mart parcel script, Oak Parcel/Pokédex cutscenes, and simple Pallet sign interaction, the follower instantly disappears and later reappears (A05/A09 contextual recall defect). User also observed sudden disappearance during Nurse Joy healing. In a healing context, the chosen design direction is an intentional gentle recall/fade **when actual healing begins**, followed by natural reappearance, because the same party companion is being healed. No Poké Ball effect is mandated, no implementation has occurred; ensure any future effect works with six-party healing, battle, save, quest log and cutscene states.

**Technical rationale to investigate:** `src/full_follower.c::ShouldSuppressFollower` globally returns TRUE for script enable/field control lock and ledge-jump copyable movement; `RefreshFollower` immediately removes the object when suppressed, while `FollowRecordedPlayerSteps` may recall on unexpected steps. Generic script lock from signs and the Viridian Mart's `lockall` scene can therefore remove the follower abruptly. Do not solve by globally disabling script protection: classify dialog, trainer battle, in-field menus, scripted movement, warp, heal and ledges separately and make removal state-dependent. Maintain live party identity, collision, palette/OAM safety, link/quest-log isolation, and no persistent object-save changes. Verify after isolated technical fixes on exact new ROM in My Boy.

**Third My Boy runtime report — attempted follower interaction / hard freeze (2026-10-15, local diagnostic ROM from technical `0774ebf`; NOT REPRODUCED BY ENGINEER):** While grinding in grass, user turned to face their follower and pressed an interaction button (A or B uncertain); game completely froze, with no further controls. Priority **CRITICAL / BLOCKER for B10**. Do not repeatedly reproduce on the only save. Engine evidence: player A-interaction in `src/field_control_avatar.c::GetInteractedObjectEventScript` may select the special follower object by position, then call `GetObjectEventScriptPointerByObjectEventId`. Follower uses transient local ID `OBJ_EVENT_ID_FULL_FOLLOWER = 254` and has no permanent map event template. `src/event_object_movement.c::GetObjectEventScriptPointerByLocalIdAndMap` dereferences `GetObjectEventTemplateByLocalIdAndMap(...)->script` without a NULL guard, while `FindObjectEventTemplateByLocalId` returns NULL when no template exists. Therefore **A-press follower → NULL dereference is a strong source-supported root cause**; user subsequently confirmed the exact button is **A** and reproduced the same freeze when facing **Charmander** and **Mankey**. This supports a species-independent interaction defect; actual CPU/runtime crash mechanism still awaits instrumentation/validated fix. Fix safely by routing/guarding follower interaction before NPC template lookup; then add controlled cosmetic follower interaction as approved in A-006. Do not patch by fabricating a persistent map NPC/template or mutating save/link structures. Audit counter interactions/other object-event script callers, collision-free runtime object lookup and link/quest-log isolation. Validate through isolated technical commit, exact SHA CI and My Boy runtime QA.

**Remaining diagnostic plan — exhaust current private ROM before rebuilding (2026-10-15, no new gameplay changes yet):** User explicitly prefers one consolidated exploratory QA pass instead of a new ROM after every defect. Continue with the original exact ROM only after normal reload of known-good in-game save. *Do not intentionally face follower and press A/B again*, do not test known-crashing paths, keep private backup of `.sav` if convenient; avoid cheat codes and risky save-state-only evidence. Low-risk accessible coverage: (1) party lead order changes Charmander→Mankey→Rattata→Charmander, compare sprite identity and duplicates; (2) use Pokémon Center PC to deposit/retrieve a nonessential party Pokémon and confirm follower chooses actual first healthy party species, respecting eggs/fainted rules only if naturally available; (3) NPC-rich/narrow-path movement with ordinary walking and safe turns, check overlap/flicker/occlusion; (4) ordinary doorway/warp repetitions, interiors and return field, screen scroll; (5) ordinary NPC/sign interactions (report sudden hides, don't require numerous repetitions); (6) optional trainer line-of-sight encounter only if naturally accessible; (7) save-load issue already FAIL, no need repeated reproduction. Stop on any new freeze/softlock, backup and report exact place, last key/action and current party lead. Never force 386 species, shiny hunt, later Rayquaza/Treecko, bike, Surf, Fly, evolution, link/trade or a full playthrough for this early diagnostic; these remain DEFERRED until appropriate test fixtures / new validated RC. Bundle fixes by subsystem then compile/CI and return once for a bounded regression suite; exact number of future ROMs cannot be guaranteed.

**Follower A-interaction friendship dialogue — user-approved target (2026-10-15, NOT IMPLEMENTED):** Pressing A while facing the transient follower should safely trigger a contextual cosmetic response sourced from the **actual party Pokémon's Gen III friendship value (0–255)**, not merely static flavor. Prefer natural qualitative dialogue bands such as wary / curious / comfortable / affectionate / very close; if desired their ranges can be mapped transparently to approximate 0–100% equivalents, but do not misrepresent that converted percentage as a distinct stored game mechanic. User wants a narrative sense of the friendship tier, not necessarily an intrusive percentage overlay. Allow species-appropriate text variation as a later polish, but first guard the 254 dynamic object from invalid map-template lookup / lockup; use existing text/dialogue controls safely and preserve saved Pokémon identity, party order, link ABI, and state. Validate with at least Charmander/Mankey, multiple friendship tiers, dialogue close/control recovery, wild battle aftermath, menu/save/reload.

**Ledge-hop sequencing — user-approved UX target (2026-10-15, NOT IMPLEMENTED):** When the player jumps a ledge, delay the follower's analogous hop until the player has completed landing **and** the landing tile is clear. Avoid jumping on top of the player; resume path following on safe free tiles without losing the follower, teleports, or being stuck if the player pauses after landing. Suspected trail sequencing, movement interpolation and landing-space/timing mismatch: **not yet proven to be only a speed/timer bug**. Must test stopping immediately after hop, multiple ledges, edges/corners, camera scroll, and occupied landing tile.

**Fourth My Boy field pass — Viridian, Forest and Brock (2026-10-15; same private diagnostic ROM from technical `0774ebf`):** User explicitly verified first-party identity reorders: Charmander/Mankey/Rattata display correctly when moved to slot 1; depositing active-lead Mankey in PC promoted Rattata to slot 1 and follower switched to Rattata; retrieving Mankey into slot 3 did not wrongly switch companion; moving Mankey back to first properly did. Positive proof of party-order/PC lifecycle for this small sample. Wandering NPC steps into Mankey's tile with visible sprite overlap but no freeze; the runtime follower is intentionally nonblocking and must not become a movement obstruction during any presentation fix. User repeated entrance/exit 5 times each at Viridian City school house, Pokémon Center and Mart, without stuck/despawn bug; companion may not become visible until player moves one square after map entry. Companion absent in Pokémon Center escalator animation, plus abrupt hide in second-floor introductory scene. Forest trainer's line-of-sight approach hides follower before battle; Brock introduction dialog hides follower, demonstrating both encounter categories. In trainer battle Mankey (first party slot) fainted; afterward Charmander (second healthy party member) became visible follower as intended. Charmander later evolved into Charmeleon and the follower graphic changed correspondingly, another major positive lifecycle checkpoint. Newly captured Pikachu also appears correctly when selected first. **Positive coverage:** Charmander, Charmeleon, Mankey, Rattata and Pikachu sampled (5 species/forms), not 386-species QA; simple sprite substitution/party-state acceptance only. **Remaining:** ongoing A/B diagnostic suites still need shiny variant, frame-by-frame motion, large Pokémon, dense OAM/VRAM, link/trade, bike/Surf/Fly and final save-load regression on corrected ROM; do not require manual full playthrough or test multiple incremental ROMs to cover them.

**Presentation design follow-up (not implemented):** On safe map arrival, prefer an adjacent unoccupied tile and avoid an initial visually shared player tile; do not forcibly spawn into walls, warps or NPC. On Pokémon Center escalator, assess whether to display a safe staged follower ascent or an explicit smooth recall/reappearance if map-engine choreography cannot support it; no accidental teleport/ghost sprite. NPC collision visual overlap must be prevented where feasible without allowing the follower to block NPC travel or scripts. For ledges, delay pursuit until player landing space clears. For NPC trainer sight and Brock/Oak/Center scripts, use contextual staging/visibility, not global script-lock removal.

**Expanded single-ROM exploratory route — user opted to progress through story (2026-10-15; CURRENT diagnostic ROM ONLY, NOT acceptance on future fixes):** The tester explicitly prefers advancing the existing My Boy game through more story content, in order to discover *additional classes of follower runtime defects before any new ROM build*, rather than switching to a newly compiled ROM after every incremental fix. This replaces the prior premature recommendation to end manual exploratory testing now. Keep original diagnostic source/ROM identifiers `0774ebf` / SHA-1 `c8fc905eaaf290347646c784e2bf5dae4b6fe1dd`. Retain confirmed defects as FAILs; no requirement to reproduce them again. Save regularly in-game, maintain a private backup of original .sav before riskier milestones, avoid cheats, and **do not press A facing the follower** (critical freeze across Charmander/Mankey). Report new freeze/crash/softlock immediately and stop the affected path, not necessarily all safe exploration. Do not presume an older diagnostic save will load a future modified ROM without explicit compatibility verification.

**Stage I — currently at Brock → Mt. Moon → Cerulean (first report checkpoint):** safely complete Brock (no need to re-prove known dialogue hide); observe post-battle follower recovery after evolution/fainted lead; test cave entrance/exit, ladders/floors, ordinary wild encounters, terrain/occlusion and stair/ledge geometry; trainer sight and scripted rival confrontation when naturally reached; ordinary sign/NPC scripts already show bug, record only *new* behavior. Check sprite clipping, NPC overlapping, sprite freeze, duplicates, map-return initial placement, and crash. No need to manipulate specific long-term progression just for test.

**Stage II — Cerulean → Vermilion / S.S. Anne → bike when naturally available (second checkpoint):** naturally occurring scripted rival/trainer and multi-floor interiors, ship stairs/doorways, special warps/cutscenes, optional Escape Rope/Dig/Teleport only if legitimately available; retrieve bicycle voucher from Vermilion Fan Club and bike from Cerulean shop if convenient; test bicycle mount, riding, dismount and restoring companion on safe tile. Distinguish intentional suppression from awkward abrupt pop-out. Test different party layouts and six-member roster only if naturally attained. Report novel defect categories, not every repeated script hide.

**Stage III — Celadon → Route 16 → Fuchsia/Safari as voluntarily reached (third checkpoint):** bicycle speed/roads, taller/different graphics Pokémon when encountered, many NPCs and indoor transitions; Fly availability (Route 16 house via Cut) and Surf acquired via Fuchsia Safari when story access permits; verify recall/reappearance for Fly/Surf and water/reflections, shore and post-Surf map-return. Safari and cycling return issues where naturally encountered. A large 64px legendary, shiny variant, eggs, fainted all party, link/trade, 386 graphics coverage and heavy OAM/VRAM need controlled later fixtures: **do not force an unnecessary shiny hunt, exhaustive Pokédex, full League or complete playthrough now**. This optional natural-play milestone does not replace future exact-fix-ROM My Boy QA.

**Reporting/decision gate:** One concise report per stage: location/action, companion species, what unexpectedly happened, whether repeated, and screenshot/video only if useful. "No new problems" is valid. At end of Stage III (or earlier if a new freeze/softlock repeatedly prevents safe progress), consolidate findings into separate minimal technical microblocks: (1) A-interaction crash, (2) save/reload and follower lifecycle, (3) normal dialogue/cutscene/trainer/wild/Center visibility transitions, (4) map/warp/ledge/NPC/bike/Surf/Fly visual behavior, (5) friendship dialogue and approved Oak-only shiny starter as distinct additions with compatibility checks. Batch controlled engineering work before requesting an **updated** private ROM, but do not promise that one rebuild can certify all fixes: exact HEAD technical CI and affected My Boy regressions are mandatory.

**My Boy checkpoint — Mt. Moon (2026-10-15):** The player entered/exited Mt. Moon five times; the follower remained available. On both ascending and descending stairs, the companion appeared immediately at the player's side, unlike previously observed delayed appearance at some doors. A circular-patrol NPC overlapped the nonblocking follower; no lock-up was reported. The already-known instantaneous prebattle follower disappearance was unchanged. The player has exited Mt. Moon and is heading toward Cerulean City. Do not request repeated reports of the known prebattle issue; request only changed behavior or newly observed defects. These observations apply to the existing diagnostic ROM, not to any corrected build.

**Cerulean/Bill visual checkpoint — 2026-10-15, user My Boy diagnostic ROM from technical `0774ebf`, screenshots supplied (NOT a new build):** The rival encounter near Cerulean, Nugget Bridge and Bill's house/interiors introduced **no new distinct problems**: prebattle and scripted interaction visibility failures are already documented, so tester should not repeat identical reports. During story advancement **Charmeloeon evolved into Charizard** and **Mankey into Primeape**; follower visuals followed both evolutions successfully. User supplied 8 screenshots covering Charizard and Primeape in multiple directions in the Cerulean exterior. Charizard and Primeape look coherent in still captures, with no obvious tile corruption. The tester subsequently reviewed Charizard again and **withdrew the suspicion of deformation**, stating that its HGSS-style appearance is good. **No Charizard correction is indicated by the current screenshots.** Optional walking video may help assess moving frames without presuming a defect. This is **positive runtime sample for 7?** actual observed distinct forms: Charmander, Charmeleon, Charizard, Mankey, Primeape, Rattata and Pikachu = **7 species/forms**, not 386-species certification. User has passed Cerulean/Gary/Nugget Bridge/Bill milestone and may continue towards Vermilion and S.S. Anne on same save.

**Optional natural follower locomotion — USER PREFERENCE / PROPOSED / FEASIBILITY PENDING (2026-10-15):** For naturally flying species such as Charizard, the user's preference is a low flying/flapping animation **while walking** and a land-and-stand pose **while stationary** when species-appropriate assets allow it. For naturally levitating species such as Gastly or Magnemite, **continuous levitation while moving and stationary**. Do not assume every Flying-type or Fly HM learner physically flies (Dodrio). Separate from the Fly field move. Audit direction-aware movement/idle/landing sprite frames, wings, shadow, OAM/palette, collision, indoors and provenance before implementation. This is an optional enhancement, not a B10 blocker.

**Optional rideable Fly and Surf mounts — USER PREFERENCE / PROPOSED / ARCHITECTURAL FEASIBILITY PENDING (2026-10-15):** The user would like, if technically achievable without harming the game, to visibly ride a believable party Pokémon using Fly (e.g. Charizard), rather than a generic shadow, and to ride a suitable aquatic Pokémon during Surf (e.g. Lapras), rather than the default water blob. Do **not** treat type or move compatibility alone as proof that the species can physically carry the player; use an ordinary effect fallback. Keep approved HM rules unchanged: Fly is taught to a compatible party Pokémon, while Surf is a field license based on item/badge, not a required Surf learner in the party. Never impose a new Surf party restriction, fabricate ownership, or modify save/link formats. Assess player alignment, directional assets, boarding/unboarding, water bobbing/reflections, shore transitions, graphics provenance, palette/OAM/VRAM, Quest Log and link. No approval to implement now; nonmandatory ideas belong to later, separately scoped feasibility work. User plans to continue with Vermilion/S.S. Anne and may optionally submit a short Charizard/Primeape walking clip. No new ROM required now.

**My Boy video evidence — Primeape/Charizard and menu/NPC (2026-10-15, existing diagnostic ROM from technical `0774ebf`):** User supplied one 38-second private MP4 (~2712x1220, 24 fps) showing continuous Cerulean overworld movement. Frame-by-frame visual review: Primeape follows, turns and animates around 0–17 seconds; no obvious frame tile corruption or severe sprite deformation observed. In the area of a moving NPC around 5–8 seconds, visual proximity/occlusion and sprites sharing apparent footprint reinforce the previously reported overlap issue, without visible player-lock/crash. At ~17.5 s Primeape is visible beside the player; at ~18.0 s the Start menu appears, the player remains on screen and Primeape has vanished entirely (**A09 visual FAIL confirmed on video, not mere UI occlusion**). Party menu transition follows around 20–25 s; Charizard is visible and animates in multiple directions from ~25 s onward, with recognizable body/wings/flame and no clear conversion corruption. At ~37 s the Start menu is again displayed without Charizard: same contextual recall defect across species. This recording supplies stronger *dynamic visual evidence* than earlier still screenshots, but does not independently establish flawless cadence or 386-species coverage, prove tile coordinate equality, show the A-interaction crash, or validate fixes. No new technical commit or ROM was made; preserve user video outside public repo and log only observations. **Result:** Charizard art correction NOT indicated; prioritize safe menu visibility and NPC/object sprite overlap while retaining nonblocking field movement. Tester may continue to Vermilion/S.S. Anne; no need to rerecord these already-established failures.

**Optional portable party storage menu — 2026-10-19, USER PREFERENCE / DESIGN DISCUSSION CLOSED / TECHNICAL REVIEW PENDING:** User explicitly likes Pokémon Quetzal's ability to access existing Pokémon storage boxes from the Start menu **during normal exploration**, deposit party members, withdraw replacements and reorganize the team without returning to a physical PC. This is the central utility, not merely read-only box browsing. The user considers the design discussion settled and delegates scheduling of feasibility review; **NOT implemented or authorized to merge without compatibility audit**. Investigate reusing FireRed's existing storage and party screens without altering Pokémon/box/save structures, and carefully handle follower refresh, the last usable party Pokémon, eggs, fainted party, full party/box, unsafe scripts, maps, trainer battles, Quest Log, multiplayer/link and field control. Future Emerald Full link/trade compatibility is a hard design constraint; a shared Gen III Pokémon data format is necessary but not sufficient proof. Prefer isolated technical microblock after current B10 follower blockers and a focused My Boy regression; no need to recompile current diagnostic ROM to evaluate this proposal.

**Follower stationary looping animation — 2026-10-19, USER PREFERENCE REFINED / DESIGN DISCUSSION CLOSED / REVIEW PENDING:** User specifically wants the **existing walk animation frames to continue cycling in place when the player and follower stop**, like the Quetzal example: apparent footsteps or lively movement on the same tile, not necessarily new custom breathing/blinking frames. Do not change map coordinates or follow-path state, and avoid animation task conflicts during turns, interactions, battle/cutscene suppression and warps. Assess cadence, orientation and all 386 species with existing directional frames; no new sprites needed to trial the effect. This is optional polish to schedule **after B10 critical stability corrections** and preferably bundle into a later bounded diagnostic build, not a reason to halt the current field pass.

**Gary canon preference — 2026-10-19, USER RECONFIRMED:** User explicitly retains Gary/Blue's fixed Squirtle→Wartortle→Blastoise progression for canon reasons; do not reopen this during naturalness review without a new request. No change to gameplay.

**State:** B10 OPEN / CRITICAL reproducible follower A-interaction freeze plus contextual visibility, field geometry and save-load defects. Current diagnostic ROM cannot pass acceptance. No gameplay fix, new ROM, CI for fixes or master integration yet. **Next:** finish safe manual diagnostic coverage on this ROM *without re-triggering the freeze*; then fix the interaction crash first, followed by safe lifecycle/presentation/ledge changes and a consolidated exact-ROM My Boy regression. Preserve user's original save; later species, shiny, bike/Surf/Fly, link and final RC remain separate acceptance stages.

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
