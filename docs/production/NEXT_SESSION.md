# Next Session — Pokémon Rojo Fuego Full v1.0

Resume from the repository, never from chat memory.

## Read first

1. `docs/production/PROJECT_CONTINUITY.md` — section 0 is the live resume point.
2. `docs/production/REPOSITORY_GUARDRAILS.md`.
3. `docs/production/DECISION_AMENDMENTS.md` — especially A-013.
4. `docs/production/POLISH_IMPLEMENTATION_MATRIX.md`.
5. Inspect live refs, exact HEADs and Full Gameplay Core evidence for the SHA being advanced.

Use `docs/spec/` only for frozen historical design details.

## Current state

- Canonical repository: `joseiturriaga25amz/pokefirered-europe`.
- **Active microblock: Prima Spanish-localization (APPROVED, NOT CLOSED)**. Branch `feature/prima-spanish-localization`. Two trainer display fields plus Spanish player-visible dialogue, Fame Checker and related texts changed from `LORELEI` to `PRIMA`; technical IDs, other languages, `ISLA PRIMA`, save/link structures and rosters unchanged. Existing legality validator and audited JSON blob lock updated. Verify branch HEAD, obtain Full Gameplay Core SUCCESS exact feature HEAD, audit, merge via controlled PR, and verify exact merged master SHA CI before CLOSED. Lance review is next after closure. Record evidence here and in PROJECT_CONTINUITY.md.

- **Active resume checkpoint (2026-10-08): Agatha CLOSED.** Exact feature HEAD `c8c4c2ab33bfdf085c65a1ea400aefee40c82674`: Full Gameplay Core **#678 SUCCESS**. PR #33 merged as `8197d040b7dcc0c5e3bf5a08ed3f6968ba477e16`; Full Gameplay Core **#679 SUCCESS** on that exact integrated master SHA, evidenced by GitHub Actions screenshot (push event and green job). Only continuity documentation commits followed; they did not change ROM/build/validators. Next block: **Lance research and proposal review**, with user approval before gameplay. AI-polish idea remains **PROPOSED** in `POLISH_IMPLEMENTATION_MATRIX.md` and is not part of Lance.
- **Current checkpoint — Bruno CLOSED:** feature HEAD `4af261c4ad9d407cb22adff40188ac1dd6ca81bd` passed Full Gameplay Core **#675 SUCCESS**; PR #32 merged as `478e56c4f40f4ca4c12d36be13e8c5bee2728cd7`; exact integrated master SHA passed Full Gameplay Core **#676 SUCCESS** (verified from GitHub Actions UI). Only documentary continuity changes followed. **Historical checkpoint:** Agatha subsequently approved, implemented, integrated and CLOSED.


- **Agatha CI checkpoint:** exact feature HEAD `c8c4c2ab33bfdf085c65a1ea400aefee40c82674` passed Full Gameplay Core **#678 SUCCESS**; #677 identified an outdated frozen Agatha party order assertion and workflow expectation was corrected. PR **#33 MERGED** as `8197d040b7dcc0c5e3bf5a08ed3f6968ba477e16`. Master verified identical before documentary followups. **Final status: CLOSED:** GitHub Actions push-run Full Gameplay Core #679 SUCCESS on `8197d04`, verified by user-provided screenshot. Continue with Lance review; no Lance implementation without approved design.

- Integration branch: `master`.
- **Agatha integrated microblock:** `feature/agatha-roster-identity`; exact approved moves, order and ace-only held items implemented. Haunter Lv60 has Protect instead of Curse; Misdreavus Lv77 keeps Mean Look; ace Gengar Lv81 holds Spell Tag. Existing IVs and 2 Full Restores stay unchanged. Approved target documented in `DECISION_AMENDMENTS.md`. **Final state: CLOSED after feature CI #678, merged PR #33 and exact integrated CI #679.** Begin Lance design review; no feature implementation yet.

- Last production block **CLOSED on master**: **B8 — Signature Pokémon staging**.
- B8 master checkpoint: `28f42346916bf9d19c558ce4ce19fb849f5b6e33`.
- B8 post-integration Full Gameplay Core **#617: SUCCESS**.
- Brock feature/documentation HEAD: `3d357df82120b779213b4fc5e8b9c56eb86ae1f1`.
- Brock feature Full Gameplay Core **#619: SUCCESS**.
- Brock merged master checkpoint: `269d75b501a99c92fd8296189760899a6a5d4571`.
- Brock post-integration Full Gameplay Core **#620: SUCCESS**.
- Brock original roster microblock: **CLOSED**.
- Brock second-pass feature HEAD: `12b244fd3b1f87b8b653fd6aaaa3d21b53c967f2`.
- Brock second-pass Full Gameplay Core **#631: SUCCESS**.
- Brock second-pass merged master checkpoint: `193b14aa3e5426dbf6049efa32a6d7c2c4d0d050`.
- Brock second-pass post-integration Full Gameplay Core **#632: SUCCESS**.
- Brock second-pass tuning microblock: **CLOSED**.
- A-013 defines the reusable Gym Leader review/implementation procedure.
- Misty feature HEAD: `4c8d16bcf7878960b6dd5f7ffb5ee44c5ff2adf7`.
- Misty feature Full Gameplay Core **#624: SUCCESS**.
- Misty merged master checkpoint: `323ff3daef5e8019690cda83c4527b5ec07ff3c1`.
- Misty post-integration Full Gameplay Core **#625: SUCCESS**.
- Misty roster/identity microblock: **CLOSED**.
- Misty second-pass feature HEAD: `a06ac70b39e3d4736de86a3680ffb0ffda1d079b`.
- Misty second-pass Full Gameplay Core **#635: SUCCESS**.
- Misty second-pass merged master checkpoint: `08bbd40374850595bc8261b1ab44ebae2012aa35`.
- Misty second-pass post-integration Full Gameplay Core **#636: SUCCESS**.
- Misty second-pass tuning microblock: **CLOSED**.
- Lt. Surge feature HEAD: `2bb74e404511e3e4b04a29d283c99b6d23a72e9d`.
- Lt. Surge Full Gameplay Core **#639: SUCCESS**.
- Lt. Surge merged master checkpoint: `27dc2ff8a99fb5d9c5135ef39e02670b2ca08196`.
- Lt. Surge post-integration Full Gameplay Core **#640: SUCCESS**.
- Lt. Surge prior roster/tuning closure remains historical evidence.
- Lt. Surge third-pass feature HEAD `32163f2677e4012032cce1070165b103f64a2ca5`: Full Gameplay Core **#642 SUCCESS**.
- Merged to `master` as `fb9bf7caec094b451cd6bb61b1752a142adb4d78`; post-integration Full Gameplay Core **#643 SUCCESS**.
- Lt. Surge third-pass curve microblock: **CLOSED**.
- Erika feature HEAD `9e0e105c36fa1e964bd21a879b6c892c9ff6cd7f`: Full Gameplay Core **#649 SUCCESS**.
- PR #24 merged Erika to `master` as `541a49b56b84bc71f5e00ba9dcf976759968bbaf`.
- Erika post-integration Full Gameplay Core **#650 SUCCESS** on that exact SHA.
- Erika roster/curve microblock: **CLOSED**.
- CI infrastructure microblock A-014: **CLOSED**. Feature HEAD `cfebaa25b6c02153f7c2a694b245854d679670b3` passed Full Gameplay Core **#652**; PR #25 merged as `f1e5da264e4791d8c023e596f64dfcb583a95a28`; post-integration Full Gameplay Core **#653 SUCCESS** on that exact master SHA.
- Koga feature HEAD `73788013338fc394c6ba125f9d3f966f1f21e948`: Full Gameplay Core **#655 SUCCESS**.
- PR #26 merged Koga to `master` as `b00c95c7bcceaed2ad8a1538eb7659c5e421c881`.
- Koga post-integration Full Gameplay Core **#656 SUCCESS** on that exact master SHA.
- Koga roster/identity microblock: **CLOSED**.
- #654 is historical only: it failed on a stale frozen-roster expectation and did not expose a gameplay defect.
- A-015 Gym healing baseline: **CLOSED**. Feature HEAD `463cba885435f05d99a5147ca525b749a15d7a5b` passed Full Gameplay Core **#657**; PR #27 merged as `899f421e176988ac211da4ede91dbefe707d15da`; post-integration Full Gameplay Core **#658 SUCCESS** on that exact master SHA.
- Closed story-healing floor: Brock 1 Potion; Misty 1 Super Potion; Lt. Surge 1 Super Potion + 1 Full Heal; Erika 1 Hyper Potion + 1 Full Heal; Koga 2 Hyper Potions + 1 Full Heal. Existing rematches remain unchanged.
- Sabrina final feature HEAD `714d552e31ab9c861c83da62c8836644f134c5b1`: Full Gameplay Core **#661 SUCCESS**; technical HEAD `86e5366566134b94428bdea49228a8f68fd27ca5` passed **#660**.
- PR #28 merged Sabrina to `master` as `d63fe7839f9e7a3f21ddfb135660496c7069de89`; post-integration Full Gameplay Core **#662 SUCCESS** on that exact SHA.
- Sabrina roster/identity/staging microblock: **CLOSED**. Story: Mr. Mime 42 / Venomoth 43 / Haunter 45 / Kadabra 47. Rematch: Mr. Mime 65 / Venomoth 66 / Wobbuffet 67 / Espeon 68 / Gengar 70 / Alakazam 72. Rematch Venomoth uses Giga Drain. Kadabra -> Alakazam staging is active.
- Blaine technical feature HEAD `80b2d6b5576b82bf305e04a9af430d7a2e387cb2`: Full Gameplay Core **#663 SUCCESS**.
- PR #29 merged Blaine to `master` as `d2b8922e932fdfc6a983c7783049e89b2013952f`; post-integration Full Gameplay Core **#665 SUCCESS** on that exact SHA.
- Blaine roster/identity microblock: **CLOSED**. Story: Rapidash 47 / Rhydon 48 / Ninetales 49 / Arcanine 50 / Magmar 52. Rematch: Rapidash 66 / Rhydon 67 / Magcargo 68 / Ninetales 68 / Arcanine 70 / Magmar 73. Only Magmar holds Charcoal; Magcargo Curse is an explicit trainer-only exception.
- Giovanni technical feature HEAD `cf687ae709c366275f88861b69e282f425612374`: Full Gameplay Core **#667 SUCCESS**.
- PR #30 merged Giovanni to `master` as `02636a3b785c9d3a21c2efeeee6a7fe2d770dc02`; post-integration Full Gameplay Core **#669 SUCCESS** on that exact SHA.
- Giovanni four-encounter progression/identity/staging microblock: **CLOSED**. Hideout: Onix 29 / Rhyhorn 30 / Kangaskhan 33. Silph: Nidorino 45 / Kangaskhan 46 / Rhyhorn 47 / Nidoqueen 49. Gym: Kingler 51 / Golem 52 / Nidoking 53 / Nidoqueen 54 / Rhydon 56 / Mewtwo 56. Rematch: Cloyster 67 / Camerupt 68 / Machamp 69 / Nidoking 70 / Nidoqueen 71 / Rhydon 74. Persian stages beside Giovanni in Hideout, Silph and Viridian.

- Lorelei technical feature HEAD `ba5af8fabfd4a62a78e15a4c664d39cb04838ac8`: Full Gameplay Core **#671 SUCCESS**.
- PR #31 merged Lorelei to `master` as `d2cf0df0cd797bacbc88266be6e0f2ea0c4a0377`.
- Lorelei post-integration Full Gameplay Core **#673 SUCCESS** on that exact master SHA.
- Lorelei roster/identity microblock: **CLOSED**. First League: Dewgong 57 / Cloyster 58 / Slowpoke 56 / Slowbro 59 / Jynx 60 / Lapras 61. Strengthened League: Dewgong 75 / Cloyster 77 / Piloswine 74 / Slowking 76 / Jynx 75 / Lapras 79. Only Lapras is equipped.

- Bruno target is **APPROVED / IMPLEMENTED / VALIDATED / CI-GREEN / CLOSED**.
- First League target: Onix 58 / Hitmonchan 59 / Hitmonlee 60 / Onix 60 / Machamp 62 @ Sitrus Berry.
- Strengthened League target: Hitmontop 75 / Hitmonchan 76 / Hitmonlee 76 / Hariyama 77 / Steelix 78 / Machamp 80 @ Black Belt.
- Only Machamp is equipped; existing IV tiers and 2 Full Restores remain.
- Rematch Hitmonlee Lv76 Detect is an explicitly approved narrow trainer-only exception. Steelix Dig is legal and deliberately retained.
- Difficulty audit found no additional move-strength changes necessary for Elite Four #2.

## Exact next action

1. Bruno and Agatha are CLOSED. Agatha proof: feature Full Gameplay Core #678 SUCCESS, PR #33 merged as `8197d04`, integrated Full Gameplay Core #679 SUCCESS.
2. Review Lance's actual first League and strengthened League teams in the current repository, comparing vanilla FireRed, difficulty progression, A-016 move/item/IV policies and signature identity.
3. Present options for the user's approval before modifying Lance gameplay. Record decisions in existing `DECISION_AMENDMENTS.md` only after approval.
4. Implement approved Lance decisions in one isolated feature microblock with validators, exact-head CI, controlled integration and post-integration CI.
5. Keep the trainer AI improvement proposal separate and unapproved.

## Continuity rule

No new generic continuity/backlog/handoff file is needed. Project continuity lives here and in `PROJECT_CONTINUITY.md`; approved decisions live in `DECISION_AMENDMENTS.md`; the production work order lives in `POLISH_IMPLEMENTATION_MATRIX.md`.

MyBoy remains the required final runtime acceptance environment.
