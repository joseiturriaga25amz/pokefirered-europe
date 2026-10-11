# Pokémon Rojo Fuego Full v1.0 — Project Continuity

**Purpose:** make the repository sufficient to resume the project without relying on any previous chat.

## 0. Current operational state — 2026-10-08

- **B9 / P-05 seen-species encounter guidance (2026-10-11; ACTIVE / CI PENDING):** On `feature/b9-pokedex-encounter-guidance`, technical commit `c143f8515cf856a3af62fe7c01a8259d843852cc`, PR #41. Adds a read-only method/level summary to the unused Pokédex area-page header, derived from the live wild-encounter tables for already seen species; restricts scans to existing Kanto/unlocked Sevii map areas, preserves the active Altering Cave rotation, and excludes roaming beasts' special live locations from generic wild metadata. Existing map markers, encounters, save layout, link protocol and runtime flags are unchanged. **Not yet validated or closed.** Full Gameplay Core run `38106955066` (#705) started for the exact technical SHA and must complete and be audited before merge. Next: inspect #705, repair failures without unrelated gameplay, verify feature CI, merge PR #41, check integrated master CI, then document closure. National 100%-reward decision remains NOT APPROVED and is a later B9 microblock. MyBoy runtime QA separately pending.


This section is the current resume point. Later dated sections preserve history and may name branches that are no longer active.

- Canonical repository: `joseiturriaga25amz/pokefirered-europe`.
- **B9 / A-010 Kanto completion reward (2026-10-10; ACTIVE):** First scoped B9 microblock on branch `feature/b9-kanto-diploma-master-ball`, PR #40, implementation `5c2f46c`, validator refinement `4ba45ae`. Preserves GAME FREAK designer's original `HasAllKantoMons()` (150 Kanto, Mew excluded) and `ShowDiploma`; afterwards grants `ITEM_MASTER_BALL` only once with `FLAG_FULL_KANTO_DEX_MASTER_BALL_CLAIMED = 0x8CF` within audited Full save flag namespace. Checks bag space AND actual `additem` result before setting claimed flag; failure retains eligibility and produces an explicit retry message. Adds equivalent text labels to all five existing languages. Extends existing save namespace validator and persistent-event-state audit. **CLOSED (2026-10-10):** B9 / A-010 Kanto diploma one-time Master Ball. Feature technical HEAD `4ba45aebe07336502bfe906bee4b5381aa6051ac` Full Gameplay Core #38067186285 SUCCESS; feature documentation-only follow-up `fe5c797d80061dc0f9f4224b8806c1e7c3179d9d` changed only PROJECT_CONTINUITY and NEXT_SESSION. PR #40 merged as master `38e082e665f1dba2b65beb9c608dfb2fa47a4944` and exact integrated Full Gameplay Core #38076525554 SUCCESS. Diploma unchanged; `HasAllKantoMons()` gate; one-time `ITEM_MASTER_BALL` award with audited Full flag `0x8CF`; bag-full/additem-failure retry never sets claim flag; supported languages and existing save/event validators updated. No Dex save layout/SaveBlock/link change. MyBoy hands-on runtime still pending. B9 overall remains OPEN: next read-only seen-species encounter guidance, then National 100%-reward design decision before full B9 closure. B9 read-only seen-species encounter guidance is a later separate microblock. A-010 National 100% extra reward is deliberately NOT YET APPROVED; preserve original National diploma until separately decided. Do not change Dex save layout/SaveBlock size, global Pokedex flags, moves or gameplay outside A-010.
- **Brock MT39 reused-TM dialogue correction (2026-10-09; CLOSED):** User identified inaccurate one-use MT teaching claim in Brock's Spanish text. Verified actual reusable TM teaching in `src/party_menu.c`; updated only `data/maps/PewterCity_Gym/text_es.inc` to state TMs may be used repeatedly (no script/gameplay changes). Feature `fix/brock-reusable-tm-dialogue` HEAD `8126fa68c65f854528e58f3b6dead10d4891732e` Full Gameplay Core #37976809032 SUCCESS, PR #39 merged into master at `745f719ef09c7a8aa8cea75310f79ab71f2fa840`, exact integrated Full Gameplay Core #37977351796 SUCCESS. Future: consider separate narrative consistency inspection for other vanilla one-use-TM descriptions if evidence warrants; not implicitly approved. Next operational block remains B9 Pokédex usefulness. MyBoy runtime QA separately pending.
- **A-016 full leader direct-dialogue polish (2026-10-09; ACTIVE):** User extended approved P-03 rematch-only dialogue work to **all available player-facing direct dialogues with the eight Gym Leaders**, including first battle intro/defeat, post-battle advice, MT explanation and bag-full responses where present, rematch offer/introduction/defeat/after and a new leader-specific decline response while preserving opt-in. Two direct Giovanni encounters outside Gym (Rocket Hideout B4F, Silph Co 11F) are also polished. Branch `feature/a016-full-leader-dialogue-polish` from master `34f5e3a`, PR #38. Microcommits `8e2013b` Brock/Misty, `935f444` remaining six, `4399204` eight refusal responses, `827ebf8` stricter existing rematch-identity validator, `316060d` out-of-Gym Giovanni narrative. Original story/flag/MT/medal/battle/quest logic unchanged; Brock's special badge event and Giovanni/Mewtwo escape script are preserved. **Status: IMPLEMENTED / VALIDATED / FEATURE CI-GREEN / INTEGRATED / INTEGRATED CI-GREEN / CLOSED.** Exact feature Full Gameplay Core **#37929921451 SUCCESS** on `5e7e056b973a671f8fb2ca0c0795895c57a2c0fc`; earlier runs caught an improperly escaped validator assertion and it was corrected without altering gameplay or dialogue. PR **#38** merged to master as `7af6c6ccfe7d50bebe48e2c31b16e7d8d48854fc`; exact integrated push Full Gameplay Core **#37930672948 SUCCESS**. Eight Gym Leaders' initial dialogue, postbattle/MT-specific interactions and all rematch responses (including refusal), plus Giovanni's Rocket Hideout and Silph Co direct story dialogue, closed. All eight gyms' event script logic was independently normalized/audited: original branches, battle triggers, reward/medal sequencing unchanged except unique refusal message. MyBoy runtime QA remains separate. Next approved production work: B9 Pokédex usefulness; P-06 NPC +1/+2 level proposal and battle AI remain PROPOSED. Closure verified as above. Continue B9 after reviewing matrix. MyBoy runtime acceptance remains separate. P-06 NPC level proposal remains PROPOSED.
- **A-016 transversal party-order polish (2026-10-09; IN PROGRESS):** Feature `feature/a016-transversal-party-order`, technical commit `d4be97bfc87e695eda004c3df113c1387c135cc2` from master `3147f15`. Audited major trainers after Gary closure. Four order-only changes: Lt. Surge opens with Voltorb (Magnemite moves to 3rd); Erika opens Victreebel (Oddish moves 2nd); Misty rematch opens Staryu then Togetic; Giovanni rematch opens Nidoking and Cloyster moves to fourth. All species, levels, moves, held items, IVs, ace last, healing and AI remain unchanged. Frozen inline workflow trainer-order expectations and audited trainer-party blob lock updated. Other leads retained because identity/tactics already justified. **CLOSED 2026-10-09:** A-016 transversal party-order-only changes feature HEAD `cb923dd8b8ddafea06189130a52473e1d40a2114` passed Full Gameplay Core #37922920204 SUCCESS. Initial #37922475005 failed an obsolete strict reorder expectation; `cb923dd` corrected exactly three frozen expectations without weakening any legality gate. PR #37 merged as `36913f2cb62d421c76636cf95fec831e74ce2135`; exact integrated master push Full Gameplay Core #37923377038 SUCCESS. Four reorders only: Surge Voltorb lead, Erika Victreebel lead, Misty rematch Staryu lead, Giovanni rematch Nidoking lead. Member arrays unchanged as unordered sets (same species, levels, moves, IVs, items and ace), no AI/healing/save/link change. P-06 NPC +1/+2 level/farming idea remains PROPOSED in existing matrix; no levels changed. Next: standalone Gym Leader rematch-dialogue polish, then resume B9 in approved sequence. MyBoy runtime QA is independent. Separate user NPC +1/+2 levels/farming suggestion registered as PROPOSED in existing `POLISH_IMPLEMENTATION_MATRIX.md` P-06 follow-up; do not apply now.
- **Gary roster/progression implementation (2026-10-09):** User approved conservative refinement of the supplied nine-encounter rosters with ordered leads, legal moves, ace-only items and unchanged Full level/IV tiers. Feature branch `feature/gary-roster-progression`, technical commit `26d621c6a8aa40a6cc9765125545b6d08eaee156`, PR #36. Teams: Oak 1; Route22 early 2; Cerulean 4 (Wartortle Lv22); S.S. Anne 4; Pokemon Tower 6; Silph 6; Route22 late 6; Champion first 6; rematch 6. All 3 legacy starter-party definitions remain identical; gameplay still selects fixed Squirtle progression. Initial levels 5/12/22/28/34/49/61/69/85 unchanged, with no blanket IV increases; only Blastoise carries items from Silph onward, and Champion retains two Full Restores. Four legality fixes: Nidorino early Fury Attack -> Double Kick/Horn Attack; Arcanine Earthquake -> Dig. Defensive Umbreon Toxic/Confuse Ray/Moonlight, Blastoise rematch retains Earthquake and Rain Dance for coverage. Validator locks, ace identity and audited trainer-party blob updated; obsolete Abra Confusion exception removed because early Gary uses Kadabra. **Status: APPROVED / IMPLEMENTED / VALIDATED / FEATURE CI-GREEN / INTEGRATED / INTEGRATED CI-GREEN / CLOSED.** **Gary CLOSED evidence (2026-10-09):** approved nine-encounter roster feature HEAD `3ba3811fc62f2dd4d2d7151b0a6933171038fd3b` passed exact feature Full Gameplay Core **#37909837264 SUCCESS**. Initial feature run `#37909349310` failed an obsolete inline Gary-roster freeze in workflow, corrected at `3ba3811` without weakening the rule. PR **#36** merged to `master` as `076cffb80967d4b7c220aa5f14627e4217b20813`; exact integrated push Full Gameplay Core **#37910445569 SUCCESS**. Gary gameplay/validator block **CLOSED**; MyBoy hands-on RC runtime QA is separate. Next: A-016 transversal party-order-only audit of Gym Leaders, Giovanni, Elite Four and Gary; thereafter separate dialogue polish and B9 according to approved matrix. Closure recorded; next A-016 transversal order-only audit per authorized production plan. MyBoy runtime QA separately pending. No unrelated AI changes.
- **Lance closure checkpoint (2026-10-09):** **CLOSED (2026-10-09)**. Feature HEAD `473c00f2f0c9ff5a43453dbc085fc96ed6bd2f8d`: Full Gameplay Core **#682 SUCCESS**. PR **#35** merged to `master` at `657f69e3f4bc445e10ec762b2e5ab9005cd8ea92`. Post-integration Full Gameplay Core **#683 SUCCESS** (run ID `37881229687`, `push`, exact integrated SHA; 46 successful steps). Subsequent master commits `f0bc860` and `e21b634` changed only `docs/production/PROJECT_CONTINUITY.md` and `docs/production/NEXT_SESSION.md`, respectively; validated ROM/gameplay unchanged. MyBoy runtime QA remains a distinct release-stage gate. Next: Gary/Blue roster/progression/identity design review, without gameplay edits until user approval.

- **Lance implementation record (2026-10-08): Lance roster identity.** Explicitly APPROVED after the leader-to-Liga transversal design audit; the design is recorded in `DECISION_AMENDMENTS.md` under the Lance A-016 amendment. Feature branch: `feature/lance-roster-identity` from master `88c7b20d1d32194c7606f18a06c18ec9cb14d162`. First League: shiny Gyarados64, Dragonair61, Aerodactyl63, Dragonair62, Dragonite65 @ Sitrus Berry. Strengthened League: shiny Gyarados81, Kingdra79, Charizard80, Salamence80, Aerodactyl80, Dragonite82 @ Leftovers. Ace-only items, unchanged Full IVs and healing. Edits scoped to Lance parties, roster/ace/frozen-order validator expectations, audited party blob and continuity. **Final state: IMPLEMENTED / VALIDATED / FEATURE CI-GREEN #682 / INTEGRATED PR #35 / INTEGRATED CI-GREEN #683 / CLOSED.** Next: Gary/Blue design review; no Gary gameplay changes before explicit approval. Future AI idea remains separate.

- **Prima localization integrated checkpoint (2026-10-08):** user-approved Spanish-only `LORELEI` → `PRIMA` completed on feature HEAD `ddd049c8bb712032207523dcc6fa3be4f219ff4e`; Full Gameplay Core **#680 SUCCESS** on that exact SHA. PR #34 merged into `master` as `7c0031b312534cc44119216ea37bc9a9df076d87`, master verified identical to that SHA after merge. **Post-merge Full Gameplay Core #681 SUCCESS** (GitHub Actions run ID `37749207866`, `push` on `master`, exact merged HEAD `7c0031b312534cc44119216ea37bc9a9df076d87`) verified through GitHub API and user screenshot. **State: IMPLEMENTED / VALIDATED / FEATURE CI-GREEN / INTEGRATED / INTEGRATED CI-GREEN / CLOSED.** Documentation-only commits after merge cannot change the tested ROM; MyBoy runtime QA remains a separate release acceptance stage. No changes to non-Spanish display names, internal IDs, battle, save/link. The next block after closure remains Lance design review; MyBoy runtime QA remains separate.

- **Prima localization implementation record (2026-10-08; subsequently CLOSED):** user APPROVED display-name change `LORELEI` → `PRIMA` in Spanish only, after Agatha CLOSED and before Lance review. Feature branch `feature/prima-spanish-localization` updates only two Spanish trainer display names, five Spanish text files (League, Lorelei house, Icefall Cave, Four Island Mart, Fame Checker), existing full trainer validator and audited trainer JSON blob lock. Spanish `ISLA PRIMA` remains unchanged; internal trainer IDs, event/flag/map labels, non-Spanish names/text, Pokémon rosters, battle AI, save/link protocol remain unchanged. **Final state: CLOSED** after feature CI #680, PR #34 merge `7c0031b`, and exact integrated CI #681. The next design block is Lance; the original pending validation instructions are superseded by this evidence.

- **Current major-trainer handoff: Agatha CLOSED (2026-10-08).** Approved roster/identity branch HEAD `c8c4c2ab33bfdf085c65a1ea400aefee40c82674` passed exact-head Full Gameplay Core **#678 SUCCESS**. PR **#33** merged into `master` as `8197d040b7dcc0c5e3bf5a08ed3f6968ba477e16`; **post-integration Full Gameplay Core #679 SUCCESS on that exact merge SHA**, verified from the GitHub Actions run screenshot supplied in the project conversation (push to master, 5m51s, ROM artifact produced). **Status: IMPLEMENTED / VALIDATED / CI-GREEN / INTEGRATED / CLOSED.** Documentation-only follow-up commits after the merge do not modify build/runtime, validators, or ROM. No MyBoy runtime QA is implied. **Next:** Lance first-League/rematch research, audit and user approval before any gameplay change. The trainer-battle AI proposal remains PROPOSED in `POLISH_IMPLEMENTATION_MATRIX.md` and is outside Lance scope.
- **Bruno roster/identity microblock CLOSED (2026-10-08):** approved A-016 first League and strengthened League parties implemented on feature HEAD `4af261c4ad9d407cb22adff40188ac1dd6ca81bd`; Full Gameplay Core **#675 SUCCESS** on that exact feature HEAD. Earlier #674 failed only in the newly introduced ace validator and was corrected without gameplay changes. PR **#32** merged to `master` as `478e56c4f40f4ca4c12d36be13e8c5bee2728cd7`. Post-integration Full Gameplay Core **#676 SUCCESS** on exact merged master SHA (GitHub Actions UI evidence, 2026-10-08). This block is **CLOSED**. The subsequent continuity-only commits change documentation, not gameplay or CI. **Historical next step at Bruno closure:** Agatha review, subsequently completed and CLOSED.


- **Agatha integration evidence:** exact feature HEAD `c8c4c2ab33bfdf085c65a1ea400aefee40c82674` passed Full Gameplay Core **#678 SUCCESS** (earlier #677 found obsolete Agatha order expectation in frozen boss roster workflow; corrected without gameplay change). PR **#33** merged to `master` as `8197d040b7dcc0c5e3bf5a08ed3f6968ba477e16`; master HEAD verified identical to this SHA before documentary commits. **Status (updated): CLOSED after Full Gameplay Core #679 SUCCESS on the exact integrated SHA `8197d04`, verified through the GitHub Actions push-run screenshot.** The connector PR-only workflow lookup does not include push-run evidence; earlier pending status is historical. Later documentation-only commits did not change the ROM. Lance review is next.

- Integration branch: `master`.
- **Agatha integrated checkpoint (2026-10-08):** Approved under the new Agatha amendment in `DECISION_AMENDMENTS.md`. Feature branch `feature/agatha-roster-identity` changes only Agatha's two parties, the exact League roster/ace/item validators and the audited trainer-party blob; no trainer AI, global learnsets, save/link or other trainers changed. First League: Gengar59 / Golbat60 / Haunter60 (Protect, not Curse) / Arbok61 / Gengar63 @ Sitrus Berry. Rematch: Gengar76 / Misdreavus77 (Mean Look) / Arbok77 / Sableye78 / Crobat79 / Gengar81 @ Spell Tag. Existing IVs and 2 Full Restores preserved. **State (final): VALIDATED / FEATURE CI-GREEN #678 / MERGED PR #33 / INTEGRATED CI-GREEN #679 / CLOSED.** Next: research and review Lance; do not assume new Lance decisions approved.

- Last production block fully **CLOSED on master**: **B8 — Signature Pokémon staging**.
- B8 reconciled feature HEAD: `8794674c33e0ff9ecf899f557da76ea07a57e27b`.
- B8 exact-head Full Gameplay Core: run **#616** — **SUCCESS**.
- B8 merged master checkpoint: `28f42346916bf9d19c558ce4ce19fb849f5b6e33`.
- B8 post-integration Full Gameplay Core: run **#617** — **SUCCESS**. B8 is therefore **CLOSED**.
- Approved amendment A-013 interposes the Gym Leader roster-research pass before resuming B9. This is an approved scope-order amendment, not a reopening of B8.
- Active roster branch: `design/leader-roster-research`.
- Brock roster feature/documentation HEAD `3d357df82120b779213b4fc5e8b9c56eb86ae1f1` passed Full Gameplay Core run **#619**.
- Brock merged to `master` as `269d75b501a99c92fd8296189760899a6a5d4571`.
- Brock post-integration Full Gameplay Core run **#620** on that exact master SHA: **SUCCESS**.
- Brock roster microblock is therefore **CLOSED**.
- Brock was later reopened only for an approved **second-pass tuning microblock**; the earlier closure remains historical evidence.
- Brock second-pass feature HEAD `12b244fd3b1f87b8b653fd6aaaa3d21b53c967f2` passed Full Gameplay Core **#631**.
- Brock second-pass merged to `master` as `193b14aa3e5426dbf6049efa32a6d7c2c4d0d050`.
- Brock second-pass post-integration Full Gameplay Core **#632** on that exact master SHA: **SUCCESS**.
- Brock second-pass tuning microblock is therefore **CLOSED**.
- Final first battle: Zubat 13 / Vulpix 14 / Geodude 15 / Onix 17; only Onix holds an Oran Berry; Onix remains ace/signature.
- Final rematch: Marshtomp 60 / Ludicolo 61 / Forretress 62 / Golem 63 / Crobat 64 / Steelix 68; only Steelix holds Metal Coat; Steelix remains ace/signature.
- Trainer-only Brock move exceptions are limited to Zubat Lv.13 Wing Attack, Vulpix Lv.14 Fire Spin + Agility, and Geodude Lv.15 Revenge.
- Brock approved identity is Onix as first-battle ace/signature and Steelix as rematch ace/signature. Exact roster/moves/levels are recorded in A-013.
- The leader-change procedure learned from Brock is frozen in A-013: update intentional frozen roster expectations, preserve legality/audit locks, exact-head CI, integration, then exact integrated-head CI.
- Misty roster feature HEAD `4c8d16bcf7878960b6dd5f7ffb5ee44c5ff2adf7` passed Full Gameplay Core run **#624**.
- Misty merged to `master` as `323ff3daef5e8019690cda83c4527b5ec07ff3c1`.
- Misty post-integration Full Gameplay Core run **#625** on that exact master SHA: **SUCCESS**.
- Misty roster/identity microblock is therefore **CLOSED**.
- Misty first battle: Psyduck 20 / Poliwag 21 / Staryu 23 / Starmie 26; Starmie remains first-battle ace/signature.
- Misty rematch: Staryu 61 / Corsola 62 / Politoed 63 / Togetic 64 / Starmie 66 / Gyarados 68; Gyarados is ace while Starmie remains signature companion.
- Misty gym staging now includes Starmie left of Misty, Togepi right of Misty, Seel + Horsea pool ambience and existing Staryu ambience.
- Psyduck's Water Gun is an explicitly approved trainer-only legality exception; no global learnset/save/link/species data changed.
- During validation, two stale expectations were corrected without gameplay rollback: the old Staryu Swift exception and the old Starmie-rematch-ace rule.
- Misty was later reopened only for an approved **second-pass tuning microblock**; the earlier closure remains historical evidence.
- Misty second-pass feature HEAD `a06ac70b39e3d4736de86a3680ffb0ffda1d079b` passed Full Gameplay Core **#635**.
- Misty second-pass merged to `master` as `08bbd40374850595bc8261b1ab44ebae2012aa35`.
- Misty second-pass post-integration Full Gameplay Core **#636** on that exact master SHA: **SUCCESS**.
- Misty second-pass tuning microblock is therefore **CLOSED**.
- Final first battle: Psyduck 20 / Poliwag 21 / Staryu 23 / Starmie 26; only Starmie holds Mystic Water; Starmie remains ace/signature.
- Final rematch: Togetic 61 / Staryu 62 / Politoed 63 / Corsola 64 / Starmie 66 / Gyarados 68; only Gyarados holds Mystic Water; Gyarados remains ace and Starmie remains signature companion.
- Trainer-only Misty move exceptions are limited to Psyduck Lv.20 Water Gun, Staryu Lv.23 Swift and Politoed Lv.63 Bounce.
- Full Gameplay Core #634 failed only because the audited `trainer_parties.h` blob lock still encoded the previous party data; the lock was intentionally relocked after reviewing the approved diff, with no gameplay rollback.
- Lt. Surge feature HEAD `2bb74e404511e3e4b04a29d283c99b6d23a72e9d` passed Full Gameplay Core **#639**.
- Lt. Surge merged to `master` as `27dc2ff8a99fb5d9c5135ef39e02670b2ca08196`.
- Lt. Surge post-integration Full Gameplay Core **#640** on that exact master SHA: **SUCCESS**.
- Lt. Surge roster/tuning microblock is therefore **CLOSED**.
- Final first battle: Pikachu 25 / Voltorb 26 / Raichu 30; only Raichu holds Sitrus Berry; Raichu remains ace/signature.
- Final rematch: Pikachu 62 / Electrode 64 / Magneton 65 / Manectric 66 / Electabuzz 67 / Raichu 69; only Raichu holds Magnet; Raichu remains ace/signature.
- No trainer-only move exception was required for Lt. Surge.
- Lt. Surge third-pass feature HEAD `32163f2677e4012032cce1070165b103f64a2ca5` passed Full Gameplay Core **#642**, merged to `master` as `fb9bf7caec094b451cd6bb61b1752a142adb4d78`, and post-integration Full Gameplay Core **#643** passed on that exact SHA. Third-pass status: **CLOSED**. Final first battle is Magnemite 24 / Pikachu 25 / Voltorb 26 / Raichu 30; rematch unchanged.
- Erika roster/curve microblock is **CLOSED**. Final first battle: Oddish 29 / Victreebel 31 / Tangela 33 / Gloom 35; only Gloom holds Sitrus Berry and remains ace/signature with intermediate-stage max-IV compensation. Final rematch: Tangela 62 / Jumpluff 63 / Bellossom 64 / Cradily 65 / Victreebel 66 / Vileplume 69; only Vileplume holds Miracle Seed, uses the normal rematch IV tier (`.iv = 214`) and is the evolved ace/signature. Celadon staging changes Gloom -> Vileplume for postgame/rematch eligibility.
- B9 Pokédex usefulness remains the next production B-block after the explicitly interposed roster-research pass is complete.

**Erika closure evidence:** feature HEAD `9e0e105c36fa1e964bd21a879b6c892c9ff6cd7f` passed Full Gameplay Core **#649**; PR #24 merged to `master` as `541a49b56b84bc71f5e00ba9dcf976759968bbaf`; post-integration Full Gameplay Core **#650** passed on that exact master SHA. Runs #647/#648 exposed only stale Erika expectations in `validate_b3_global_ace_identity.py`; validator-only corrections `dda4848` and `9e0e105` aligned the gate with the approved design without changing gameplay.

**CI infrastructure closure evidence:** A-014 feature HEAD `cfebaa25b6c02153f7c2a694b245854d679670b3` passed Full Gameplay Core **#652**; PR #25 merged to `master` as `f1e5da264e4791d8c023e596f64dfcb583a95a28`; post-integration Full Gameplay Core **#653** passed on that exact master SHA. This microblock changed CI/workflow policy only; no gameplay was modified. A-014 is therefore **CLOSED**.

**A-015 healing-baseline closure evidence:** feature HEAD `463cba885435f05d99a5147ca525b749a15d7a5b` passed Full Gameplay Core **#657**; PR #27 merged to `master` as `899f421e176988ac211da4ede91dbefe707d15da`; post-integration Full Gameplay Core **#658** passed on that exact master SHA. A-015 healing-baseline microblock is **CLOSED**. Story healing floor now preserves vanilla-or-better resources for Brock through Koga; rematches remain unchanged.

**Sabrina closure evidence:** final feature HEAD `714d552e31ab9c861c83da62c8836644f134c5b1` passed Full Gameplay Core **#661**; technical feature HEAD `86e5366566134b94428bdea49228a8f68fd27ca5` had already passed **#660**. PR #28 merged to `master` as `d63fe7839f9e7a3f21ddfb135660496c7069de89`; post-integration Full Gameplay Core **#662** passed on that exact master SHA. Sabrina roster/identity/staging microblock is **CLOSED**. Final story team is Mr. Mime 42 / Venomoth 43 / Haunter 45 / Kadabra 47; final rematch is Mr. Mime 65 / Venomoth 66 / Wobbuffet 67 / Espeon 68 / Gengar 70 / Alakazam 72. Kadabra is the max-IV story ace with Twisted Spoon; Alakazam uses the normal rematch IV tier and Twisted Spoon. Saffron staging progresses Kadabra -> Alakazam. Story healing is 2 Hyper Potions + 1 Full Heal; rematch remains 2 Full Restores.

**Blaine closure evidence:** technical feature HEAD `80b2d6b5576b82bf305e04a9af430d7a2e387cb2` passed Full Gameplay Core **#663**. Final PR HEAD `2acb5a046e6d1362ccce4f82aefb85ad897544e8` differs only by documentation. PR #29 merged to `master` as `d2b8922e932fdfc6a983c7783049e89b2013952f`; post-integration Full Gameplay Core **#665** passed on that exact master SHA. Blaine roster/identity microblock is **CLOSED**. Final story team: Rapidash 47 / Rhydon 48 / Ninetales 49 / Arcanine 50 / Magmar 52. Final rematch: Rapidash 66 / Rhydon 67 / Magcargo 68 / Ninetales 68 / Arcanine 70 / Magmar 73. Only Magmar holds Charcoal. Story healing is 2 Hyper Potions + 1 Full Heal; rematch remains 2 Full Restores. Magcargo Curse is a narrowly scoped trainer-only exception; global learnsets remain unchanged.

**Giovanni closure evidence:** technical feature HEAD `cf687ae709c366275f88861b69e282f425612374` passed Full Gameplay Core **#667**. Initial run **#666** failed only because Magnitude was unnecessarily declared as an exception even though the legality validator proved it legal; gameplay was unchanged by the validator-only correction. Final PR HEAD `2d247eb7ff4b7e218173ca374caa75a7bfb0356f` differs from the green technical HEAD only by documentation. PR #30 merged to `master` as `02636a3b785c9d3a21c2efeeee6a7fe2d770dc02`; post-integration Full Gameplay Core **#669** passed on that exact SHA. Giovanni four-encounter progression/identity/staging microblock is **CLOSED**. Persian is staged beside Giovanni in Rocket Hideout, Silph and Viridian; Rhydon remains the Gym/rematch combat ace with Soft Sand; Mewtwo remains the Lv56 max-IV narrative superweapon and breakout cutscene. Only Rhyhorn Lv30 Sand Attack requires a new trainer-only exception; Rhyhorn Lv47 Magnitude is legal through existing project rules.

**Lorelei closure evidence:** technical feature HEAD `ba5af8fabfd4a62a78e15a4c664d39cb04838ac8` passed Full Gameplay Core **#671**. Final feature HEAD `63c56d3bfb119de396418ca493c6a4f3a2d89069` adds only the approved-target documentation on top of the green technical payload. PR #31 merged to `master` as `d2cf0df0cd797bacbc88266be6e0f2ea0c4a0377`; post-integration Full Gameplay Core **#673** passed on that exact master SHA. Lorelei roster/identity microblock is **CLOSED**. Final first League: Dewgong 57 / Cloyster 58 / Slowpoke 56 / Slowbro 59 / Jynx 60 / Lapras 61. Final strengthened League: Dewgong 75 / Cloyster 77 / Piloswine 74 / Slowking 76 / Jynx 75 / Lapras 79. Only Lapras holds an item; existing IV tiers, healing and Lapras staging are preserved.

**Bruno approved target:** design review and difficulty audit are complete. First League is Onix 58 / Hitmonchan 59 / Hitmonlee 60 / Onix 60 / Machamp 62 @ Sitrus Berry with vanilla-oriented tactical moves. Strengthened League is Hitmontop 75 / Hitmonchan 76 / Hitmonlee 76 / Hariyama 77 / Steelix 78 / Machamp 80 @ Black Belt. Only Machamp holds an item. Existing IV tiers and 2 Full Restores remain. Rematch Hitmonlee Lv76 Detect is an explicitly approved narrow trainer-only legality exception; Steelix Dig is legal and deliberately retained. Audit found no further move-strength adjustment necessary for Bruno's position as Elite Four #2.

**Next production action (current):** B9/A-010 Kanto Master Ball reward CLOSED after feature Full Gameplay Core #38067186285, merged PR #40 `38e082e`, and integrated Full Gameplay Core #38076525554 SUCCESS. Next: separately investigate and implement read-only Pokédex encounter-method/level guidance for seen species; preserve protected-event mystery, area-marker compatibility and save layout. Do not design National completion reward without user decision. NPC +1/+2 level/farming and trainer battle AI proposals remain PROPOSED.

### Existing continuity roles — do not duplicate

- Project-wide continuity and handoff protocol: this file.
- Short next-session pointer: `docs/production/NEXT_SESSION.md`.
- Approved post-freeze decisions: `docs/production/DECISION_AMENDMENTS.md`.
- Approved work order and future blocks: `docs/production/POLISH_IMPLEMENTATION_MATRIX.md`.
- Defects / acceptance evidence: `docs/production/RC_AUDIT_LOG.md`.
- Final static/release method: `FINAL_AUDIT_PLAN.md` and `SECOND_PASS_AUDIT.md`.
- Final runtime acceptance: `RC_MYBOY_CHECKLIST.md`.
- Frozen historical design: `docs/spec/`.

No new generic continuity, backlog, decision-log or handoff file is needed. Out-of-scope ideas belong in the relevant existing block/checkpoint as **PROPOSED / pending decision**, or in `POLISH_IMPLEMENTATION_MATRIX.md` when they belong to an already approved future block. Only explicitly approved decisions belong in `DECISION_AMENDMENTS.md`.

## 1. Start here in every new session

Before modifying code:

1. Read this file.
2. Read `docs/production/REPOSITORY_GUARDRAILS.md` and verify the canonical repository is `joseiturriaga25amz/pokefirered-europe` with `push: true` before any write.
3. Read `docs/production/DECISION_AMENDMENTS.md`.
4. Read `docs/production/POLISH_IMPLEMENTATION_MATRIX.md`.
5. Read `docs/production/NEXT_SESSION.md`.
6. Inspect the current branch/HEAD and the latest **Full Gameplay Core** result for that exact SHA.
7. Read `RC_AUDIT_LOG.md`, `FINAL_AUDIT_PLAN.md`, `SECOND_PASS_AUDIT.md` or `RC_MYBOY_CHECKLIST.md` when the active block/release gate requires them.
8. Only if a frozen design detail is still needed, consult `docs/spec/`.

Previous chats are **not required** and must not override the repository.

## 2. Source-of-truth precedence

From highest to lowest authority:

1. Explicit approved post-freeze amendments in `docs/production/DECISION_AMENDMENTS.md`.
2. Frozen preproduction specification under `docs/spec/Pokemon_Rojo_Fuego_Full_Preproduccion_v1.0.md`.
3. Frozen matrices under `docs/spec/Pokemon_Rojo_Fuego_Full_Matrices_v1.0.md`.
4. Frozen decision log under `docs/spec/Pokemon_Rojo_Fuego_Full_Decision_Log_v1.0.md`.
5. Frozen production prompt under `docs/spec/Pokemon_Rojo_Fuego_Full_Prompt_Maestro_Produccion_v1.0.md`.
6. Current implementation and automated tests as evidence of what is actually implemented.

A historical frozen requirement superseded by an approved amendment must **not** be silently restored.

## 3. Approved amendments that materially change the freeze

- **A-001:** MyBoy is the required runtime QA emulator. mGBA is optional diagnostic only.
- **A-002:** abandon the 142-slot normal Items pocket; keep vanilla 42-slot behavior. The 400 bytes at `0x348C` remain reserved/unused.
- **A-003:** finish implementation/static verification first; concentrate user-run runtime QA in the final RC phase instead of stopping after every block.
- **A-004:** GitHub is the continuity authority. Chats are disposable.

## 4. Repository / branch / baseline — historical snapshot

- Repository: `joseiturriaga25amz/pokefirered-europe`.
- Upstream reference only: `CompuMaxx/pokefirered-europe` (never a production write target).
- Historical active branch at this snapshot: `feature/b3-postgame-rematch-identity`. Current branch authority is section 0 plus live Git refs.
- Repository write preflight is mandatory: exact full name + `push: true` before any mutation.
- Frozen vanilla tag: `baseline-spanish-vanilla`.
- Baseline commit: `e184c5cf898cd29efebd33bc1bfe5994277e21ab`.
- Production target: `firered_es_modern`.
- Baseline Spanish SHA-1: `ab8f6bfe0ccdaf41188cd015c8c74c314d02296a`.

## 5. Technical state at the earlier continuity freeze — historical

The first exhaustive static audit is nearly complete and an explicit **second-pass adversarial audit** is active.

Latest code-affecting second-pass commits include:

- `25fb95adfaab7c734d86f9e83241c4ae148d914b` — corrected wireless-status UBFIX applied from a clean pre-change file;
- `2f21644529ba1146f70adc8b7f26a7e3135a60e9` — applies Full Hall-of-Fame KO recovery to the Spanish script actually compiled;
- `74bf56b4ac6799682d2ccef60c274b0f80582a36` — restores the non-target generic Hall-of-Fame script to vanilla;
- `444b1f27e4bfda87f3f326937af238d7e28c0845` — extends exact audited blob locks to trainer payloads and target-language high-risk scripts;
- `7fe7204c8d125180dee1faa18df5309b599e8732` — adds the second-pass release-integrity validator to consolidated CI.

The exact current HEAD still requires a fresh consolidated CI result before any RC freeze. Older CI success and older ROM hashes are historical evidence only and must **not** be treated as validation of the current code payload.

The workflow still builds `firered_es_modern`, performs two clean builds and requires byte-for-byte reproducibility before recording a checksum.

## 6. RC audit findings repaired so far

See `RC_AUDIT_LOG.md` for the authoritative finding-by-finding record. The recovery/final audit now includes RC-F001..RC-F035, with RC-F031 explicitly corrected as a false positive rather than retained as a fictional bug fix.

Important late findings include:

- vanilla-save migration existed but was not called on Continue;
- reusable-TM capacity/add/shop paths were inconsistent;
- direct trade-evolution items reached the UI without a core evolution effect;
- doubles AI had per-side history aliasing and out-of-bounds move-history reads;
- Gary routing/identity still depended on vanilla starter branches;
- recorded AI hold effects were briefly reinterpreted as item IDs and corrected;
- tested link synchronization fixes were excluded from Full's MODERN revision-0 build;
- UBFIX mon-data accessors still relied on incompatible function aliases;
- wireless status group accounting could index outside its counter array;
- Hall-of-Fame state validation was checking a generic script while the Spanish target lacked the Full KO-recovery hooks;
- Repel RC-F031 was a recovery-audit false positive: the Spanish target already implemented QOL-007, and the generic accidental edit was reverted.

Exact blob locks now cover the original high-risk gameplay data plus trade, trainer metadata/parties and selected Spanish high-risk scripts.

## 7. Important automatic validators

### `tools/validate_full_trainer_sets.py`
Last known PASS:
- 34 Full parties;
- 163 Pokémon;
- 632 custom moves;
- validates species, level, IV, held item and move legality including level-up, TM/HM, tutor, egg and pre-evolution learnability.

### `tools/validate_release_integrity.py`
Second-pass meta-gate that verifies:
- consolidated CI targets `firered_es_modern`;
- all production validators are actually invoked;
- Gate 6/7/QoL checks point at Spanish scripts that feed the target;
- generic non-target Hall-of-Fame/Repel scripts remain vanilla;
- second-pass high-risk blob locks are present;
- audit-log traceability includes the corrected false positive and late recovery findings.

### `tools/validate_rc_freeze.py`
Protects, among other things:
- Gen III species/move/item ID-space compatibility;
- SaveBlock1 size and Full header offset;
- non-destructive Full save migration;
- vanilla bag reservation after A-002;
- frozen item and berry prices;
- EV-reducing berry definitions;
- Two Island berry progression;
- fossils and Cinnabar revival;
- second Fighting Dojo state/reward;
- approved evolution invariants;
- all nine Altering Cave tables and automatic-rotation invariants;
- Porygon prize remains repeatable; A-008 changes final price/presentation to 5,500 coins / localized 5.500 FICHAS.

## 8. Save / compatibility facts

Direct comparison with `baseline-spanish-vanilla` established:

- vanilla had `unused_3D24[16]`;
- Full replaces exactly those 16 bytes with `struct FullSaveHeader`;
- `towerChallengeId` and `trainerTower` keep their offsets;
- `SaveBlock1` remains `0x3D68`;
- `fullHeader` remains at `0x3D24`;
- `unused_348C[400]` remains intact after A-002;
- Pokémon / BoxPokemon layouts remain compile-locked Gen III compatible;
- species/move/item ID spaces remain vanilla-sized;
- pre-National non-Kanto/egg link restrictions remain;
- Gen III Pokémon trading compatibility is an explicit acceptance goal;
- round-tripping the same modified save through vanilla is **not** a supported goal.

## Current RC audit recovery note

After the 2026-09-20 app-side forced closures, repository history was confirmed intact and the audit resumed from GitHub. The first audit found multiple real defects and also exposed one false positive caused by inspecting a generic language script instead of the Spanish file actually compiled. That false positive is recorded and corrected.

The audit is now using a second independent layer defined in `docs/production/SECOND_PASS_AUDIT.md`: compiled-target verification, semantic baseline diff, validator skepticism, negative-path review, cross-layer contradiction checks and exact blob locks after semantic review.

A reproducible MyBoy RC was frozen at `a1c7fa573ac784ef089bfdf966aa38fc84861212` (ROM SHA-1 `6ebb0ce7cc736d7fd6c9c5bce09a21aaaf7d0443`) and entered runtime QA. Runtime invalidated it with two confirmed blockers: RC-F040 (pre-National cross-generation evolutions reached the animation but were canceled by a leftover vanilla National-Dex guard) and RC-F041 (Koichi's Fighting Dojo sight-trigger script no longer began with `trainerbattle`, causing deterministic MyBoy freeze when he approached the player). Both defects are fixed in source and statically gated. A replacement reproducible MyBoy artifact/checksum is required after the accumulated runtime-polish pass before final acceptance continues on the new candidate.

## 9. Historical RC-era remaining-work note

This section predates the later approved B0–B12 polish work order and is retained as release-history context. The current work order is `POLISH_IMPLEMENTATION_MATRIX.md`, and the live resume point is section 0. The final RC requirements below still apply when B11/B12 are reached:

1. finish exhaustive static/specification audit described in `FINAL_AUDIT_PLAN.md`;
2. ensure exact final HEAD CI is green;
3. build/freeze one RC ROM and record checksum;
4. execute `RC_MYBOY_CHECKLIST.md` on that exact build;
5. repair any runtime defects;
6. rerun affected tests plus adjacent regressions;
7. perform final release-diff and documentation consistency pass;
8. only then promote/merge/tag v1.0.

Do **not** call the project 100% final merely because CI is green.

## 10. Working-style instruction

The user explicitly prefers:

- rapid forward progress;
- autonomous, meticulous internal review;
- no repeated manual testing interruptions during implementation;
- runtime tests concentrated at meaningful final milestones;
- no need to request approval for ordinary bug fixes required to satisfy already-approved requirements.

Do not reintroduce a slow block-by-block approval workflow.

## 11. If a new chat starts

Read section 0, inspect live refs/HEAD and the exact-SHA Full Gameplay Core result, then continue the current B-block. Do not reconstruct state from an old chat and do not treat a historical branch/checkpoint elsewhere in this file as current merely because it appears later in the document.


## 12. 2026-09-24 handoff — runtime QA closeout and approved polish scope

The old MyBoy RC is a1c7fa573ac784ef089bfdf966aa38fc84861212 (ROM SHA-1 6ebb0ce7cc736d7fd6c9c5bce09a21aaaf7d0443) and is NOT the final acceptance candidate. It remains useful only as runtime evidence.

### Old-RC evidence now closed

- Mew quest in Pokémon Mansion was completed and Mew captured. Functional chain passes, but narrative/visual presentation needs polish: preserve canonical diary history, add current-day NPC atmosphere, visible overworld Mew appearances and an interactable final Mew instead of immediate battle from the last diary.
- Gym rematches: Brock was battled repeatedly, proving repeatability in runtime. Misty, Lt. Surge and Erika were also reached/battled and felt appropriately challenging; the user's party was intentionally underleveled from speedrun-style progression, so do not treat difficulty as a balance defect.
- All eight gym-rematch scripts currently reuse the same generic offer/opening/defeat/post-battle strings. Replace with leader-specific dialogue while preserving teams/mechanics.
- Strengthened League was entered; Lorelei battle started and Dewgong/Lapras were observed before the underleveled team lost. This is a smoke PASS for rematch-League activation only, not full League acceptance.
- Do not force the user to grind this old RC to complete the strengthened League or Ho-Oh respawn. Validate Ho-Oh KO/HOF recovery on a disposable/new RC save.
- Roaming beasts and Celebi are intentionally withdrawn from old-RC manual QA because both will be redesigned.

### Approved legendary narrative V2

See DECISION_AMENDMENTS.md A-005. Key points:
- Celio returns to network/Ruby/Sapphire connectivity role and no longer distributes legendary tickets.
- Maritime/birds -> MysticTicket -> Lugia; Deoxys -> Pewter Museum investigation -> AuroraTicket; Mewtwo -> Mansion/Mew; beasts -> Ho-Oh capstone; Celebi -> separate Berry Forest nature quest.
- First beast contact is a no-battle cinematic with Suicune focus plus Raikou/Entei, all marked seen; only one roamer active sequentially.
- Roamer search/catch UX must be much less tedious.
- Preserve Gen III IDs, structures, ticket destinations, Pokédex flags, vanilla roamer storage and advanced-save migration.

### Approved immersion/QoL scope

See DECISION_AMENDMENTS.md A-006.

- Sell all existing Gen III specialty Balls progressively and naturally: Malla/Net, Nido/Nest, Acopio/Repeat, Turno/Timer, Lujo/Luxury, Buceo/Dive, Honor/Premier. Master/Safari stay non-commercial.
- Dive Ball keeps original Gen III behavior unchanged; in FireRed it may be mostly aesthetic because there is no normal underwater map use. Do not invent Surf/fishing behavior.
- Approved experience targets: party-leader follower Pokémon, contextual follower dialogue, more useful Pokédex for seen species, natural postgame training bridge, legendary environmental signals, and stronger identity for important NPC dialogue.
- Follower remains a technical-gate module, not permission to destabilize v1.0.

### Follower research result to resume from

A strong public technical/reference candidate is monhacks/arrantemerald branch followers-expanded-id:
- README explicitly claims HGSS-style followers for all 386 Pokémon, forms and shinies;
- follower interactions/messages, dynamic overworld palettes, large OW support and a backwards-compatible 16-bit overworld graphics-ID scheme;
- repository contains 440 Pokémon overworld PNG files under graphics/object_events/pics/pokemon, including forms/legacy variants;
- README says it does not increase save-data structures or the object-event structure.

This is Emerald code, not drop-in FireRed code. Port only the minimal concepts/assets after source audit. The repository did NOT expose a clear top-level license during inspection, so asset/code provenance and redistribution permission must be resolved before importing. Do not assume public GitHub equals licensed for redistribution.

Compatibility design for follower:
- follower is derived from the existing party leader and is not separately persisted;
- do not alter struct Pokemon, BoxPokemon, SaveBlock sizes, species/item IDs or Link serialization;
- on/off control may use an audited existing Full flag/setting;
- auto-hide/reappear around bike/Surf/Fly/link/cutscenes/unsafe scripts as needed;
- isolated prototype plus rollback; MyBoy QA for warps/ledges/doors/trainer sight/palettes/OAM/party reorder/egg/fainted lead/shiny/save-load/link.

### Next session order

1. Re-read PROJECT_CONTINUITY.md, DECISION_AMENDMENTS.md, RC_AUDIT_LOG.md, FINAL_AUDIT_PLAN.md, RC_MYBOY_CHECKLIST.md.
2. Continue follower-source/license/provenance research before importing anything.
3. Convert approved old-RC runtime findings into the grouped polish implementation:
   - RC-F040/RC-F041 already fixed in source;
   - legendary V2 narrative and roamer UX;
   - Mew visual/narrative polish;
   - unique leader-rematch dialogue;
   - specialty Ball shops;
   - Pokédex/postgame-training/NPC/ambient polish.
4. Prototype follower separately and merge only if it passes structural/runtime gates.
5. Update validators/checklist to the approved V2 behavior.
6. Build and freeze a new exact MyBoy RC/checksum only after current HEAD CI/static audit is green.
7. Final runtime acceptance belongs to the new RC, not the old test ROM.


## 2026-09-24 — follower/provenance and polish checkpoint

Repository-only continuation was performed from the production documents, not from chat memory.

### New production documentation

- `docs/production/FOLLOWER_TECHNICAL_RESEARCH.md`
  - upstream inspected: `monhacks/arrantemerald` branch `followers-expanded-id`;
  - bulk HGSS follower asset provenance traced to veekun/HGSS extraction;
  - no repository-wide license grant found for upstream follower code/assets;
  - external 386/440-sprite set is not treated as redistribution-cleared;
  - conservative FireRed architecture defined without 16-bit graphics IDs or save/link structure growth.
- `docs/production/POLISH_IMPLEMENTATION_MATRIX.md`
  - maps A-005/A-006 into production work packages P-01 through P-08;
  - explicitly records that current Celio Mystic/Aurora distribution is pre-A-005 behavior and must be replaced.

### Isolated follower prototype

Branch: `prototype/follower-runtime`

Green compile checkpoint:
`6b7fd84ecdc02eb188721dd4526c2e853a43859f`

Actions run:
`36013304188` — PASS.

The prototype:
- uses only existing Full-native Pokémon overworld assets;
- keeps generic object graphics IDs 8-bit;
- does not modify Pokémon/BoxPokemon/SaveBlock/link serialization;
- is excluded from link-map initialization;
- remains blocked from production pending MyBoy runtime + Save/Link QA.

### RC policy

The ROM SHA-1 `a1c7fa573ac784ef089bfdf966aa38fc84861212` remains historical runtime evidence only. It is not a final candidate.

Do not generate or label a replacement final RC until:
1. approved A-005/A-006 production polish is implemented;
2. validators and MyBoy checklist reflect the new truth;
3. follower is either MyBoy-approved for integration or explicitly excluded from v1.0;
4. exact-HEAD CI is green;
5. the replacement RC is frozen by Git SHA + ROM SHA-1 and receives the required runtime suite.


## 2026-09-24 — production order locked after Drive/runtime reconciliation

Drive evidence document reviewed:
`Pokemon Rojo Fuego Full v1.0 — Evidencia Runtime RC`.

The remaining work is now intentionally split into small production blocks B0–B12 in `POLISH_IMPLEMENTATION_MATRIX.md`. This supersedes any vague “implement all polish at once” interpretation.

New approved decision:
- A-007 adds fixed signature Pokémon beside the 8 Gym Leaders, Elite Four and Gary/Blue.
- This is not the player follower system; it is controlled map/event presentation.
- Required signature mapping and QA constraints are recorded in `DECISION_AMENDMENTS.md`.
- Missing trainer-signature sprites are a bounded asset problem (~13 identities) and should be used as a safe sprite/OAM pilot before universal follower coverage.

Operational rule:
- complete one B-block at a time;
- end each block with build/static validation and documentation;
- do not generate replacement RC until B11;
- Drive remains the manual MyBoy/runtime evidence record;
- GitHub remains the implementation/continuity authority.


## 13. Chat/resource management and handoff protocol

This is a **project rule**, not a chat-memory preference.

### Workload sizing

To reduce forced chat/tool interruptions:

- do not run repository research, compilation review, audit, mutation and long-form reporting as one monolithic operation;
- split technical work into bounded units: **locate → inspect → change → validate → record**;
- prefer targeted file/range inspection over oversized repository dumps;
- keep modifications small enough to be reviewable and reversible;
- finish each coherent unit with a Git checkpoint and concise state note before starting the next;
- split large textual audits/specifications into prudent sections instead of producing or ingesting them in one oversized pass;
- avoid repeating already-recorded repository context in chat when GitHub documents are authoritative.

### Chat rotation

The assistant must actively watch for signs that the current conversation is becoming unsafe to continue efficiently, including:

- repeated long tool traces or large repository outputs;
- several major implementation/audit blocks accumulated in one chat;
- signs of context pressure, truncated tool output or prior forced-stop risk;
- a natural project checkpoint where continuing in a fresh chat would reduce risk without losing momentum.

When that point is reached, **tell the user proactively before a forced closure occurs**.

Before recommending a new chat:

1. finish or safely checkpoint the current atomic subtask;
2. commit/document the exact repository state;
3. update this continuity file or the relevant production handoff document if project truth changed;
4. provide the user with a ready-to-paste continuation prompt containing:
   - repository name;
   - active branch;
   - exact HEAD;
   - current B-block/subblock;
   - completed work;
   - open gate/failure, if any;
   - exact next action;
   - instruction to read PROJECT_CONTINUITY.md and authoritative production docs first;
   - reminder not to reconstruct state from old chat text when repository truth exists.

Do not rotate chats merely because a response is long. Rotate when continuity risk becomes materially higher than the cost of starting fresh.

### Continuation-prompt template

Use this structure and fill it with the current exact state:

> Continuamos el proyecto Pokémon Rojo Fuego Full v1.0.
> 
> Repositorio: `joseiturriaga25amz/pokefirered-europe`
> Rama activa: `<branch>`
> HEAD exacto: `<sha>`
> Bloque actual: `<B-block/subblock>`
> 
> Antes de modificar nada, lee `docs/production/PROJECT_CONTINUITY.md` y los documentos de producción que allí se indican. GitHub es la autoridad de continuidad; no reconstruyas el estado desde el chat anterior.
> 
> Estado cerrado: <summary>
> Gate/fallo abierto: <summary or none>
> Siguiente acción exacta: <next action>
> 
> Mantén el protocolo de trabajo en bloques acotados: localizar → inspeccionar → cambiar → validar → registrar. Evita operaciones monolíticas y textos/auditorías excesivamente grandes en una sola pasada.


## 14. 2026-09-24 B0 runtime-evidence reconciliation

The external Drive runtime evidence was re-read specifically for post-freeze approvals that had not yet been promoted into repository authority. A-008 now makes the following B1 rules repository-authoritative: UI-001 EV layout repair, UI-002 visible move category, Porygon 5,500/aligned presentation, vending quantity selector, badge-gated Oak aides, National Dex without the 60-capture quota, HM item+badge field licenses with forgettable learned HMs, and vanilla held-item Exp. Share behavior.

These are no longer Drive-only decisions. B1 must implement against A-008 and update validators/runtime checks accordingly.


## 15. B0 closed / B1 opened

B0 is CLOSED at exact validated HEAD `f93996b28eb5d5f1824a24c89bf6ee1e4be0944d`.

GitHub Actions run `36023307145` completed SUCCESS on that exact HEAD. The repository now contains the current A-005/A-006/A-007/A-008/A-009 acceptance truth, bounded-work/chat-handoff protocol, updated reconciliation classifications, and no stale Celio/old-Celebi acceptance assertions in the principal validators.

B1 branch: `feature/b1-low-risk-qol`.

B1.1 starts with the lowest-risk local corrections: Porygon 5,500/localized presentation, National Dex removal of the 60-capture gate while retaining the One Island story gate, and Move Reminder money-based localization cleanup. Later B1 subblocks handle Oak aide badge gates, UI-001/UI-002, vending quantity, and final HM field-license behavior.


## 16. 2026-09-25 — B1 closed / B2 next

B1 — Low-risk UX/QoL cleanup is CLOSED at exact validated HEAD `ede84f8837346ffe22d697c9ed6a6677ad7fb3f4`.

GitHub Actions:
- run `36135969057` — **Full Gameplay Core**
- result: **SUCCESS**

The final B1 correction was L10N-002: the active Spanish Move Reminder dialogue now matches the real repeatable 2.000-money system and no longer instructs the player to bring mushrooms.

New approved deferred polish:
- A-010 records the GAME FREAK Pokédex completion improvement;
- Kanto completion keeps the diploma and adds one one-time Master Ball with retry-safe full-bag handling;
- implementation belongs to B9, not B1;
- the National completion bonus remains intentionally undecided until B9.

Next production block: **B2 — Boss/rival balance reconciliation**.

B2 must begin from a fresh branch/checkpoint derived from the validated B1 HEAD and follow the bounded protocol: locate → inspect → change → validate → record.


## 17. 2026-09-25 — repository-target incident / guardrail

A B2 write attempt was accidentally directed at the upstream repository `CompuMaxx/pokefirered-europe`, which correctly exposed read-only permissions to the connector (`pull: true, push: false`). No project data was lost. The canonical fork `joseiturriaga25amz/pokefirered-europe` retained branch `feature/b2-boss-rival-balance` at hardened Mewtwo checkpoint `eed2d780be04f1b6dcc396ef9d01b5808dd8aea4`, with parent implementation commit `b48fab525fd10a11e5552d5b6ef22ada5fb712d8`.

Permanent rule: read `docs/production/REPOSITORY_GUARDRAILS.md` at session start and verify the exact canonical repo plus `push: true` before every first write of a session. Upstream is comparison/reference only.


## 18. 2026-09-26 — B2 closed / B3 started

B2 — Boss/rival balance reconciliation was merged to `master` through PR #3 after exact-head Full Gameplay Core run `36253119207` completed SUCCESS on `479b1c04924e7ccbd3c0c079dc42a21bdee9ae48`.

Merged master checkpoint: `0a081948847de63022d65237868a5d46dc368c6c`.

B3 active branch: `feature/b3-postgame-rematch-identity`, created from that exact merged master checkpoint.

B3.1 changes:
- Gym Leader rematches now unlock from `FLAG_SYS_GAME_CLEAR`, not National Dex;
- Giovanni's postgame reappearance follows the same game-clear rule;
- all eight Gym Leaders have unique rematch offer / intro / defeat / post-battle dialogue;
- repeatability remains intact via `cleartrainerflag`;
- `tools/validate_b3_rematch_identity.py` is wired into Full Gameplay Core.


B3.3 postgame training bridge:
- six existing Network-Machine-gated VS Seeker final tiers were raised into an optional level 64–70 bridge;
- no global EXP formula or mandatory-grind rule changed;
- strengthened League remains gated by `FLAG_SYS_CAN_LINK_WITH_RS`;
- `tools/validate_b3_postgame_progression.py` is wired into Full Gameplay Core.


## 19. 2026-09-26 — B3 closure candidate

B3 — Postgame progression and rematch identity has reached closure scope.

Validated gameplay checkpoint:
- branch: `feature/b3-postgame-rematch-identity`
- HEAD: `8a73aedb0f36d8b26a8956fd04e280139275cfa9`
- Full Gameplay Core run `36282030839`: **SUCCESS**

Implemented B3 scope:
- first-Hall-of-Fame Gym rematch unlocks;
- no National Dex/capture dependency for Gym rematches;
- eight unique leader rematch dialogue sets;
- repeatability preserved;
- Lorelei rematch Lapras refinement applied;
- optional level 64-70 Network-era VS Seeker training bridge;
- strengthened League remains Network-Machine gated;
- B3-specific identity/progression validators added.

This documentation-only closure commit must also pass Full Gameplay Core before merge. After that, merge B3 to `master` and start B4 from the exact merged master checkpoint.


### Historical — B3 closure candidate was ON HOLD (superseded)

User clarified the intended review methodology: postgame rematches must receive the same one-by-one manual design review used for the first-cycle Gym Leaders, Gary, Giovanni and League.

At that historical point, B3 was **not closed** and was not to be merged yet.

> **Superseded historical note:** the manual sequence below was completed later on 2026-09-28 and the resulting checkpoint was merged to `master` via PR #6 (merge commit `5c481fb4165c4b5e9a2fb25730d6821865c29814`). Do not treat this earlier pending-state note as current.


## 2026-09-28 — Erika ace / IV clarification

User clarified two independent rules for the global canon-depth audit:
- symbolic ace selection must follow the trainer's strongest character identity, especially anime signature where applicable;
- IV compensation is a separate balance tool and is not automatically attached to every ace.

Applied to Erika rematch:
- Vileplume remains Lv66 at the existing rematch IV tier;
- Gloom is now Lv69 and is Erika's symbolic ace;
- only Gloom receives .iv = 255 because it deliberately remains an intermediate evolutionary stage;
- no global ace-IV rewrite is authorized.

The ace audit must continue across all reviewed bosses using identity/fidelity criteria without altering IVs unless separately approved.


## 2026-09-28 — Global ace audit rule

Ace identity is now audited globally for Gym Leaders, Giovanni, Gary/Blue and the Elite Four across first encounters and rematches.

Approved exception rule:
- symbolic/canonical identity determines the ace;
- intermediate-stage aces may receive max trainer IVs and an appropriate held item to justify remaining unevolved;
- IV enhancement is not implied by ace status.

Corrections applied:
- Sabrina: Kadabra ace in first battle and rematch; max IV + Twisted Spoon. Alakazam remains on both teams at a lower level.
- Koga: Golbat ace in first battle with max IV + Sharp Beak; Crobat ace in rematch. Weezing moves below the ace slot.
- Erika's already-applied Gloom rule remains the model for intermediate-stage ace compensation.
- Giovanni's Persian remains signature/motif rather than battle ace.

Validator: tools/validate_b3_global_ace_identity.py.


## 2026-09-28 — Canon-depth checkpoint: Lance / Bruno / Agatha

Implemented on feature/b3-global-canon-audit-v2:
- Lance's Gyarados is forced shiny in both first League and rematch, narrowly scoped at trainer-party generation time.
- Lance rematch gains Salamence Lv80; Dragonite remains ace.
- Bruno rematch replaces Hitmontop with Hariyama Lv78 while retaining Onix, Steelix, Hitmonchan, Hitmonlee and Machamp.
- Agatha rematch gains Sableye Lv78 as a Full thematic Hoenn sixth; ownership is not represented as canonical.
- Exact League and global identity validators updated.

Historical next step at that point: continue the global transversal audit of Gary/Blue, Giovanni, all Gym Leaders and Elite Four. This was subsequently completed and merged in PR #6.


## 2026-09-28 — Global ace audit design closure

Global symbolic-ace review completed across Gary/Blue, Giovanni, all Kanto Gym Leaders and the Elite Four, including first encounters and strengthened/rematch states.

Design corrections required by the audit were limited to:
- Erika -> Gloom;
- Koga -> Golbat/Crobat;
- Sabrina -> Kadabra;
- Lance Gyarados -> Red/Shiny identity continuity.

Other current ace assignments remain accepted:
Brock Onix/Steelix; Misty Starmie; Surge Raichu; Blaine Magmar; Lorelei Lapras; Bruno Machamp; Agatha Gengar; Lance Dragonite; Gary Squirtle/Wartortle/Blastoise. Giovanni uses encounter-specific combat aces and Persian is not treated as the ace solely because it is his visual companion.

Design audit is closed; technical closure still requires current exact-head CI and later runtime acceptance.


## 2026-09-28 — Current B3 checkpoint after PR #6

PR #6 merged the completed global canon/ace audit to `master` at:
- merge commit `5c481fb4165c4b5e9a2fb25730d6821865c29814`.

The manual transversal ace/moveset review through Lance is complete and user-approved.

Approved gameplay changes in that pass:
- Gary Nidoqueen: Superpower -> Hyper Beam.
- Gary Magmar: Confuse Ray -> Psychic.
- Koga first-battle Golbat: Toxic -> Screech.
- Blaine rematch Magmar: Fire Punch -> Flamethrower, yielding Flamethrower / Fire Blast / Brick Break / Confuse Ray.

Approved unchanged ace progressions:
- Brock Onix -> Steelix.
- Misty Starmie -> Starmie.
- Lt. Surge Raichu -> Raichu.
- Erika Gloom -> Gloom.
- Koga Golbat -> Crobat after the Screech adjustment.
- Sabrina Kadabra -> Kadabra.
- Giovanni Rhydon -> Rhydon.
- Lorelei Lapras -> Lapras.
- Bruno Machamp -> Machamp.
- Agatha Gengar -> Gengar.
- Lance Dragonite -> Dragonite.
- Gary/Blue Squirtle -> Wartortle -> Blastoise.

Authoritative resume file:
- `docs/production/B3_GLOBAL_AUDIT_CHECKPOINT.md`.

Current work after PR #6:
- final repository consistency audit;
- exact-head validators / CI;
- correct any stale documentation or validation gaps;
- create the next safe checkpoint only after CI passes.


## 2026-09-28 — B3 final technical closure / B4 specialty Ball candidate

B3 final consistency audit was merged through PR #7:
- merge commit: `715649b259fb95eaaa24ea09f8dc6b2b0b510093`;
- exact tested head before merge: `ed080dd78d05b52de10aa20dad06e0e043b1835f`;
- Full Gameplay Core run `36432599241`: **SUCCESS**.

B4 branch:
- `feature/b4-specialty-ball-economy`.

Implemented B4 scope:
- Vermilion Mart: Net Ball;
- Fuchsia Mart: Nest Ball;
- Saffron Mart: Timer Ball;
- Cinnabar Mart: Repeat Ball;
- Celadon Department Store 2F: Luxury Ball + Premier Ball;
- Four Island Mart: Dive Ball;
- Seven Island Mart: complete legitimate late/postgame stock of Net/Nest/Repeat/Timer/Luxury/Dive/Premier Balls.

Economy / compatibility:
- existing item prices retained: specialty Balls 1,000; Premier Ball 200;
- Master Ball and Safari Ball remain excluded from these shops;
- `src/data/items.json` was not modified;
- original Gen III Dive Ball behavior remains unchanged: 3.5x only on underwater map type, 1x otherwise;
- caught-ball metadata / item IDs remain untouched.

Validator:
- `tools/validate_b4_specialty_balls.py`;
- wired into Full Gameplay Core.

Functional B4 checkpoint:
- HEAD `354cc1ede9ebe7ea5c3675176a3c3a5b51b3ead3`;
- Full Gameplay Core run `36433908751`: **SUCCESS**;
- B4 specialty Ball validator: **PASS**;
- reproducible ROM build, release integrity and MyBoy RC packaging: **PASS**.

A final documentation-only exact-HEAD CI is required after this continuity update. If green, merge B4 and begin B5 — Altering Cave and encounter polish from the exact merged master checkpoint.


## 2026-09-28 — B4 closed / B5 Altering Cave candidate

B4 — Specialty Balls and economy distribution is CLOSED:
- PR #8;
- merge commit `189447c2fbb238d328e3c6f86146025fa52a8851`;
- exact documentation HEAD `17271c0c175b26c8faf0b006cb4da385c9855acf`;
- Full Gameplay Core run `36434865537`: **SUCCESS**.

B5 branch:
- `feature/b5-altering-cave-encounter-polish`.

Implemented B5 scope:
- Altering Cave no longer uses the manual species selector;
- `VAR_ALTERING_CAVE_WILD_SET` rotates automatically on each cave entry through all nine original tables:
  Zubat → Mareep → Pineco → Houndour → Teddiursa → Aipom → Shuckle → Stantler → Smeargle → Zubat;
- the scientist/researcher is informational only and reports the active table without mutating it;
- FireRed/LeafGreen table ordering and the existing runtime table-index mechanism are preserved;
- original version-specific Altering Cave encounter rates are preserved (FireRed 5, LeafGreen 7).

A-009 rarity reconciliation applied:
- Safari Scyther / Pinsir / Kangaskhan / Chansey / Tauros: 10%;
- Dratini: 10% Surf in Safari Center, 4% fishing in each Safari area;
- Dragonair: 1% fishing in each Safari area;
- Kanto starters: base 10%, middle 4%, final 1% in approved thematic locations;
- Magmar: 4% Mt. Ember;
- Electabuzz: 4% Power Plant.

Validation:
- new `tools/validate_b5_encounter_polish.py`;
- `validate_full_obtainability.py`, `validate_full_event_states.py` and `validate_release_integrity.py` updated to the automatic-rotation truth;
- audited encounter/blob locks refreshed.

Functional B5 checkpoint:
- HEAD `3d748663bf40e59aabba21b0a85790b7e478e6b0`;
- Full Gameplay Core run `36457796839`: **SUCCESS**;
- reproducible ROM build: **PASS**;
- B5 encounter polish validator: **PASS**;
- one-save obtainability: **PASS**;
- persistent event-state audit: **PASS**;
- second-pass release integrity: **PASS**;
- MyBoy RC patch packaging: **PASS**.

Next gate:
- run exact-head CI after this documentation update;
- if green, merge B5 to `master`;
- then begin B6 — Legendary narrative V2 core from the exact merged master checkpoint.


## 20. 2026-09-30 — continuity architecture audit

The repository continuity architecture was audited before new gameplay work.

- Existing files already cover continuity, decisions, approved work order, block checkpoints, release audit and MyBoy acceptance; no additional generic documentation file is needed.
- Early “current” wording and `NEXT_SESSION.md` were stale; historical records are preserved but labeled as historical.
- B6/B7 acceptance evidence is now recorded in `RC_AUDIT_LOG.md`.
- The 154-row reconciliation ledger is advanced from pre-B6/B7 A-005 pending states to current implementation/runtime-evidence-required states.
- Altering Cave MyBoy instructions now match B5 automatic rotation.
- `Full Gameplay Core` is the production CI authority; legacy compatibility and Block 1/2 workflows remain manual diagnostics instead of automatic red gates.
- Exact-SHA validation remains mandatory: a green result never transfers automatically to a changed HEAD.
