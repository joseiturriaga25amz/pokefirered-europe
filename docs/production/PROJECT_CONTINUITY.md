# Pokémon Rojo Fuego Full v1.0 — Project Continuity

**Purpose:** make the repository sufficient to resume the project without relying on any previous chat.

## 0. Current operational state — 2026-10-08

- **B10 private diagnostic user-friendly environment preflight (2026-10-14):** On `prototype/follower-runtime`, technical HEAD `5065657e7d6f2c2c37e35d36c8bea57518bdfd4b` adds `--check-environment` and pre-download preflight to existing `tools/build_follower_diagnostic.py`: verifies Git branch/checkout cleanliness, Ubuntu/WSL environment, ARM assembler/compiler, make, C compiler, pkg-config and libpng. Missing dependencies are reported with installation guidance rather than failing mid-build. Commit `b9df1ea`; commit `5065657` reorders existing full private source-to-ROM CI stage **before** runner-only modifications of tracked graphics headers to preserve the clean-checkout contract. **Follower Prototype #65 run `38621010671` IN_PROGRESS at checkpoint**, not CI-GREEN. Previous exact #63 SUCCESS applies to older HEAD only. No emulator QA nor private ROM supplied to user; B10 OPEN. Next inspect #65 exact logs, correct concrete issues, then provide supported Ubuntu/WSL private local build steps and ask only necessary environment clarification.

- **B10 Charmander-first MyBoy diagnostic plan (2026-10-14, docs-only):** User will choose Charmander in Oak's lab for first playable follower check. Existing `docs/production/RC_MYBOY_CHECKLIST.md` now contains first-play cases **A01–A09** for Oak script/first open tile, four-direction walking, running/corners, ordinary interiors/doors, collision/NPC, battle-return, save/reload, NPC palette integrity; later **B01–B06** for Charmander→Charmeleon→Charizard evolution, party lead/fainted/egg, shiny, Treecko/Rayquaza 32/64px, bike/Surf/reflections, link/trade. Added in docs-only commit `a1043cb8`; no gameplay or asset change. Current prototype exact HEAD `6ceac1b541555bd9a3b551c0f57209af01bf5fd3` remains CI #63 SUCCESS, full private builder/manifest tested in ephemeral CI; no downloadable ROM or MyBoy PASS yet. Next produce/use a legally suitable private ROM on local environment and execute A01–A09 with screenshots/brief defect notes; do not confuse this plan with testing completed. B10 OPEN.

- **B10 exact CI #63 end-to-end private builder PASS (2026-10-14):** prototype `prototype/follower-runtime` HEAD `6ceac1b541555bd9a3b551c0f57209af01bf5fd3` passed Follower Prototype #63 run `38617773797`. Job log explicitly confirms full `tools/build_follower_diagnostic.py` invocation with 386 normal+shiny species from pinned source, private ROM produced, manifest SHA-1/SHA-256 and exact HEAD checks PASS (`PRIVATE_DIAGNOSTIC_E2E_PASS species=386 sha1=b2f3abc97aeb78cbd38f1c5db39c6ef93519aa0c`), and worktree list restored. Temporary ROM deleted; no sprite or ROM uploaded, distributed or committed. The SHA-1 is **diagnostic ephemeral CI evidence**, not a distributable artifact or MyBoy acceptance. Technical HEAD IMPLEMENTED+VALIDATED+CI-GREEN but B10 still OPEN, no master gameplay merge; original Nintendo art redistribution rights remain unresolved. Next: arrange safe private local reproduction and seven MyBoy runtime cases; do not claim runtime PASS without recorded evidence.

- **B10 private MyBoy ROM builder end-to-end CI gate (2026-10-14):** Isolated `prototype/follower-runtime` technical HEAD `6ceac1b541555bd9a3b551c0f57209af01bf5fd3` adds one workflow stage to execute `tools/build_follower_diagnostic.py --download-pinned --output` for all 386 National IDs in a private temporary runner directory, then verify generated ROM size ≤32 MiB, manifest source revision, exact GITHUB_SHA, SHA-1/SHA-256, 386×2 registration, no MyBoy QA claims, and restoration of Git worktree listing. The temporary ROM and its manifest are deleted by trap; no assets or ROMs uploaded, and none committed. **Follower Prototype #63 run `38617773797` IN_PROGRESS at checkpoint: NOT CI-GREEN until exact result/log verified.** Previous #62 SUCCESS validates synthetic diagnostics and separate 386 ephemeral compile, not this end-to-end builder. Next review #63 logs, resolve any proven technical error with small commit, and only afterward prepare MyBoy access/testing. Rights to third-party Nintendo art unresolved, no release or master gameplay merge; B10 OPEN.

- **B10 private diagnostic builder CI #62 exact PASS (2026-10-14):** On `prototype/follower-runtime`, HEAD `1b71a5f4413223c0d293c9d8d971190a35c3b973`, Follower Prototype **#62 SUCCESS** run `38616401850`. CI logs explicitly show `Private B10 builder source completeness, generated registry and output isolation PASS` (synthetic test), followed by full 386 species normal/shiny generated graphics registration and successful secondary FireRed ES ROM build. Base and expanded EWRAM/IWRAM remain unchanged (259,182 B EWRAM / 29,172 B IWRAM); expanded link ROM region 16,176,780 B. Exact technical HEAD IMPLEMENTED + VALIDATED + CI-GREEN **for automation/self-test and ephemeral source-to-ROM compilation only**. `tools/build_follower_diagnostic.py` complete PRIVATE local-worktree build has NOT been exercised end-to-end; NO downloadable diagnostic ROM, MyBoy evidence, rights clearance, or `master` gameplay integration. Next bounded step is verify private end-to-end local builder and its digest/cleanup on a supported local ARM environment, then run existing B10 MyBoy diagnostic matrix if an appropriate locally built ROM is available. No art/ROM commit or upload. B10 remains OPEN.

- **B10 local private MyBoy diagnostic build path (2026-10-14):** Read-only preflight verified canonical repo with push access; master technical content remains untouched. Added `tools/build_follower_diagnostic.py` to isolated `prototype/follower-runtime` at commit `0b6d884226ca0aeb74fc9461da73f3a915a17826`. Builder requires a local branch checkout, creates a temporary detached `git worktree` for exact SHA, retrieves pinned HGSS archive or accepts user-provided local ZIP, checks 386 normal/shiny four-direction source completeness, injects graphics only into temporary checkout, builds `firered_es_modern`, checks ≤32 MiB, copies a **private local-only** `.gba` outside git with SHA-1/SHA-256 manifest, and removes temporary worktree. It does not upload ROM/sprites, grant redistribution permission or perform MyBoy QA. Added `python3 tools/build_follower_diagnostic.py --self-test` to existing Follower Prototype workflow in technical HEAD `1b71a5f4413223c0d293c9d8d971190a35c3b973`. **Follower Prototype #62 run `38616401850` IN_PROGRESS at checkpoint; NOT CI-GREEN until exact result verified**. Important: CI tests synthetic installer and existing 386 source→ROM path; actual local private-builder end-to-end invocation remains untested. Provenance of Nintendo art and user MyBoy visual QA remain pending; B10 OPEN. Next check #62 logs; repair bounded failures; then document secure local usage, validate exact ROM fingerprint in MyBoy, no master gameplay merge.

- **B10 runtime-resource/provenance audit checkpoint (2026-10-14):** No additional engine defect proven by source review, so no speculative gameplay changes. `RC_AUDIT_LOG.md` updated with source evidence (commit `05f1935`), and existing `RC_MYBOY_CHECKLIST.md` extended with seven B10-specific pre-integration test cases (commit `edb65ac`). Confirmed prior exact technical prototype `242b73897b7709a7341a17f79556244b9f52a028` passed Follower Prototype #60; 386 normal/shiny pairs compile **only in temporary runner checkout**. Linker base/full 386 EWRAM identical at 259,182 B (2,962 B remaining on linked EWRAM region), IWRAM identical at 29,172 B; does not prove available dynamic OBJ-VRAM/OAM or MyBoy runtime. Upstream pinned teobz README credits original Nintendo artwork from Veekun; redistribution clearance is unconfirmed, so no art or ROM publication. **Next:** establish an appropriate locally reproducible diagnostic build and run seven targeted MyBoy cases, then address only observed defects. B10 OPEN / no merge. This checkpoint is documentation-only; prior technical CI #60 remains applicable.

- **B10 full 386 graphical binding integrity gate passed exact HEAD (2026-10-14):** `prototype/follower-runtime` HEAD `242b73897b7709a7341a17f79556244b9f52a028` passed **Follower Prototype #60 SUCCESS** (run `38613213252`). CI logs explicitly confirm `Generated registry/frame/OAM/palette bindings verified: 386 normal+shiny species`, `Installed 386 National Dex normal/shiny sprite pairs into temporary checkout`, followed by successful second `pokefirered_modern_es.gba` rebuild with ≤32 MiB check. Negative truncated-shiny-palette test passed. Base and all-386 ROM link map measurements **both** report EWRAM 259,182 B / 256 KiB (98.87%) and IWRAM 29,172 B / 32 KiB (89.03%); adding the temporary 386 ROM sprite resources did not alter these link-time RAM totals. Full ROM link region after import 16,176,780 B (48.21% of 32 MiB), vs base 9,357,180 B. No MyBoy, sprite-runtime pressure, save/link or reflection acceptance established; no rights clearance, graphics or ROM permanently committed, no merge to master. **B10 OPEN** despite exact prototype CI-GREEN. Next bounded step: runtime/OAM-VRAM/64px palette and reflection adversarial audit plus provenance and MyBoy test approach, avoiding claiming runtime coverage from static builds.

- **B10 independent generated graphics integrity gate (2026-10-14):** Audited native follower 8-bit graphics dispatch, generated normal/shiny palette resolver, 16-frame four-direction animation tables, dedicated dynamic palette and one-frame OBJ tile allocation. Source build #59 already proved full 386×2 temporary ROM compilation but not in-game runtime. A validation gap was found: source-to-ROM gate did not independently assert all generated registry entries, frame offsets, dimension-specific OAM/subsprite definitions, palette byte lengths or duplicate/missing graphics files. Added `verify_installation()` and negative truncated-shiny-palette fixture to existing `tools/generate_follower_graphics.py` on isolated prototype technical HEAD `242b73897b7709a7341a17f79556244b9f52a028` (no engine/gameplay/ABI edits); generator now verifies every installed National-ID normal/shiny pair before reporting install success. **Follower Prototype #60 run `38613213252` in progress at checkpoint**, NOT yet validated/CI-GREEN for this HEAD. Previous #59 exact `9b100d9` remains successful for full ROM compile only. Next inspect exact #60 and its failure step (if any), correct bounded issues, compare EWRAM/IWRAM with baseline and investigate 64px OAM/VRAM behavior and palette/reflection lifecycle. Provenance and MyBoy remain unvalidated; B10 OPEN.

- **B10 386 normal/shiny real HGSS temporary ROM build: exact CI-GREEN (2026-10-14):** `prototype/follower-runtime` exact technical HEAD `9b100d9a3cd813decc67d61b1e08067ce50d1ffc` passed **Follower Prototype #59 SUCCESS** (run `38562952888`). Logs confirm full pinned-source 386/386 conversion audit PASS, compiler generator self-test PASS, `Installed 386 National Dex normal/shiny sprite pairs into temporary checkout`, secondary `pokefirered_modern_es.gba` compilation and link PASS, `<=32 MiB` file check PASS. Linked ROM section reports **16,176,780 bytes (48.21% of 32 MiB)**; EWRAM **259,182 B / 256 KiB (98.87%)** and IWRAM **29,172 B / 32 KiB (89.03%)**. These RAM figures must be compared against baseline and runtime stress-tested; compilation alone cannot prove VRAM/OAM, animations, maps/reflections, fades, saves/link, nor ROM-asset provenance. No external sprite images or resulting ROM were committed/distributed: this is **runner-only** graphics installation. #58 (`38562018888`) FAILED before second ROM build from source folder matching; the pinned hyphenated-Nidoran/Mr-Mime/Ho-Oh fix `9b100d9` was confirmed on #59. Technical milestone IMPLEMENTED + VALIDATED + exact CI-GREEN, **NOT INTEGRATED OR CLOSED**, B10 remains OPEN. **Next bounded microblock:** adversarial audit of 386 generated frame/animation/palette binding and VRAM/EWRAM/OAM budget with runtime lifecycle edge cases; assess provenance before any permanent asset import, then MyBoy acceptance and conservative integration. Production `master` only receives documentary evidence at this checkpoint.

- **B10 full 386 scale build #58 failure / folder naming fix (2026-10-14):** #58 run `38562018888` completed FAILURE in full source→ROM stage at `ValueError: 029: expected exactly one species folder, got 0`, before second ROM compilation. Source audit still PASS 386/386. Root cause audited against pinned teobz tree `f9ee9f83d0f53b196b64d65f7bb70369b196f33b`: converter `locate_species` pattern wrongly excluded four genuine hyphenated species directories (`029_nidoran-f`, `032_nidoran-m`, `122_mr-mime`, `250_ho-oh`), while source auditor accepted them. Isolated converter regex + self-test fixtures committed on `prototype/follower-runtime`: `9b100d9a3cd813decc67d61b1e08067ce50d1ffc`. **Follower Prototype #59 `38562952888` was IN_PROGRESS at checkpoint, not CI-GREEN.** Check exact #59 and follow-on compiler/ROM-size result, fix only proven additional errors. No 386 ROM-success or MyBoy/rights/integration claim; B10 OPEN.

- **B10 386-species source→ROM scale build launched (2026-10-14):** `prototype/follower-runtime` technical HEAD `c9c17bd4abb451a9364cd0c9e8feb45693991016`, one-file change to `.github/workflows/follower-prototype.yml`: expand the successful three-species temporary HGSS import/ROM compilation test to National Dex 1..386 normal+shiny, require all 3088 source APNG files (386 × 2 × 4 directions), generate both variants and all 16 frame slots per variant, assert ROM exists and is ≤32 MiB. No art or ROM committed; scope remains runner-only, no gameplay/SaveBlock/link edits. **Follower Prototype #58 run `38562018888` IN_PROGRESS at checkpoint; NOT validated/CI-GREEN until exact result and logs checked.** Earlier #57 exact `9541e5a` SUCCESS proved three pairs compile; it does not prove full-scale build. Next: check #58, classify failures without expanding scope prematurely, inspect C/compiler memory/ROM cost, only then assess subsequent runtime/provenance milestones. B10 remains OPEN and unmerged.

- **B10 confirmed 3-species HGSS source→ROM pilot CI-GREEN (2026-10-14):** Exact technical HEAD `9541e5a57c3b01eaabe3796abd9a13778c8e3e1c` on `prototype/follower-runtime` passed **Follower Prototype #57 SUCCESS** (run `38531690275`), including standard `firered_es_modern`, all predecessor follower checks, full read-only 386/386 normal/shiny source-conversion audit, synthetic installer self-test and experimental real-source generation/second ROM build. Job logs explicitly show `Installed 3 National Dex normal/shiny sprite pairs into temporary checkout`, rebuilt `pokefirered_modern_es.gba` successfully, and `Real-source follower graphics compiled into test ROM; no ROM or sprites uploaded.` Pilot species: Bulbasaur #1 32px, Treecko #252 32px (Gen III internal #277), Rayquaza #384 64px; two variants each. Earlier #55/#56 failures were caused by the installer empty-registry guard comparing trimmed registry body against untrimmed sentinel; narrow fix `9541e5a` normalized both sides; #56 `38498992376` failed pre-self-test. **Milestone achieved: proven reproducible three-species source-to-ROM compilation, not live sprite render/playtest.** All 386 source-convertible does NOT mean 386 installed in ROM; project source registry stays NULL outside runner; no source artwork/ROM distributed; no MyBoy acceptance or master gameplay integration; B10 remains OPEN. Next independently review 3-species generated graphics/OAM/palette/animation integration and scale checks for all 386 normal/shiny, establish provenance, run required runtime QA under release policy, integrate only after audit/CI gate.

- **B10 CI #55 / runner Python import correction (2026-10-13):** User-provided GitHub Actions screenshots establish Follower Prototype **#55 FAILED** at `Compile temporary ROM with real 32px and 64px HGSS follower normal-shiny bindings`; earlier source audits PASSED, step shown 0s. Full error log for #55 was not available; inspection independently established that the workflow's inline `python3 - <<'PY'` imports `audit_follower_source_samples` and `generate_follower_graphics` from `tools/` but does not add `tools` to Python's module path, so the real-source stage could fail before art generation. Isolated one-line workflow correction committed to `prototype/follower-runtime` at `3ee9b7bfb2a20a25ea215ba238177a039a26795f`: `PYTHONPATH=tools python3 - <<'PY'` for that exact block. Prototype HEAD verified. **Exact CI for 3ee9b7b NOT confirmed; no clean 3-species ROM build claim.** Next verify workflow run/step logs for exact SHA, correct only demonstrated further issues, then MyBoy/provenance/386 scale. `master` documentary only; B10 remains unmerged.

- **B10 correction after exact Follower Prototype #54 (2026-10-13):** #54 run `38452060147` completed FAILURE: baseline `firered_es_modern` and prior follower gates SUCCESS, but the new real-source build step stopped at `tools/generate_follower_graphics.py --self-test` with `AssertionError: unexpected overwrite`, BEFORE downloading/installing real art and rebuilding the experimental ROM. Root cause: checking two permanent species-0 sentinels did not prove both registry bodies empty. Isolated technical fix `a4a8cb19b69cd3e21b28075210637c6ed0b9eded` checks actual body content for both registry arrays before writes. Verified remote prototype HEAD exactly `a4a8cb1`; exact CI for this new SHA has NOT been observed passing (workflow-run query empty at checkpoint). Next: obtain exact Follower Prototype run for `a4a8cb1`, inspect 3-species real ROM compile; address only independently proven failures, then QA and 386 scaling. No MyBoy, no permanent HGSS artwork and no B10 master merge. 

- **B10 source→ROM compiler pipeline milestone (2026-10-13):** Exact Follower Prototype #50 FAILED after successfully compiling FireRed (run `38450370206`) due to a **bad source-validator expectation**: National Dex Treecko is an enum position, not a `#define`. Narrow workflow correction `2e5c1cd02260fda8eaed172b92b1b18d7111dee2` subsequently passed exact Follower Prototype #51 SUCCESS (run `38451524517`). Prototype `71d5946b3fe17304ba7764d183d6162cc54b2f0b` adds generated species-specific normal/shiny palette routing into dedicated follower dynamic OBJ palette slot, using registry entries, preserving existing NPC colors. Prototype `ee3b5917bdd861833696bc1ec682e59f996be51d` introduces `tools/generate_follower_graphics.py`: reads locally supplied audited APNGs, packs 16 frames/variant to indexed 4bpp and 32-byte normal/shiny palette, emits generated C `SpriteFrameImage`/object graphics pointers into **existing** registry in source checkout, not API-committed assets. Prototype `f7a99a3cd764844074a3faa1e848e6bef0a7c329` adds GitHub Action **read-only runner-only real source → local GBA compiler pilot** for Bulbasaur National 1, Treecko National 252 (internal 277), Rayquaza National 384 (64px), both visual variants. Real external APNGs are fetched temporarily, no sprite files or ROM artifacts committed/distributed. Exact Follower Prototype #54 run `38452060147` was `in_progress` when this checkpoint was written: **not CI-GREEN yet** and no successful end-to-end ROM claim. Next: inspect #54 exact failing step/build result; fix generator or test contract if genuinely defective; ensure clean no-art default CI, prove 3-species real ROM compile, then MyBoy runtime animations/reflections/VRAM/transition QA. 386/386 source-convertible is separate from 386 installed/art rights. B10 still isolated, unmerged; B9 National reward decision pending independently.


- **B10 Gen III internal→National Dex correction (2026-10-13):** Exact Follower Prototype #49 SUCCESS on previous technical HEAD `fb532e1d88e0d07b3b7c5484f8d056d9e10f3d70` run `38449232252`, confirms empty 386×2 registry compiles. Read-only review uncovered a **real future misidentification hazard:** Gen III `SPECIES_TREECKO=277` but `NATIONAL_DEX_TREECKO=252`; registry is indexed by National ID. In isolated technical commit `85742cdc41b226c95a1a730e30928a13c796626d`, `FullFollower_GetSpecies()` now returns `SpeciesToNationalPokedexNum(sFollowerSpecies)` (or 0 if NONE), and native follower eligibility accepts a registered pair of normal+shiny through existing 8-bit proxy. No Pokemon/SaveBlock/link layouts changed. Added source gate for Hoenn lookup and both-variant requirement. Follower Prototype CI #50 run `38450370206` was `in_progress` at checkpoint; current HEAD not yet CI-GREEN. **No generated artwork registry entries or real sprites yet**: registry is still all NULL, runtime proof with actual imported art, source rights, tests in MyBoy and integrated Full Gameplay Core outstanding. Next: verify exact #50, then build reproducible generator for species-specific SpriteFrameImage/OAM/normal-shiny palette C bindings from *rights-cleared* 4bpp assets; run real-asset end-to-end build in isolated CI without claiming art distribution; audit mismatch and all 386, perform MyBoy.


- **B10 386-index registry bridge / engineering quality gate (2026-10-13):** Confirmed exact Follower Prototype #48 SUCCESS on `9fe7ed0be77d41cfcd18ac7c4a8ccdda941a695f`, run `38446871759`: source-only HGSS conversion feasibility **386/386**, seven 64px and 379 32px, with Metapod down native 3-frame hold expanded to 4 GBA slots. No actual external art imported into ROM. Technical commit `fb532e1d88e0d07b3b7c5484f8d056d9e10f3d70` in `prototype/follower-runtime`: adds unsaved 16-bit National species getter plus bounded 386×(normal,shiny) optional graphics pointer registry in existing diagnostic graphics header, consulted by the existing 8-bit `OBJ_EVENT_GFX_FULL_FOLLOWER` resolver with native fallback; source/ABI assertion added to isolated workflow. **Registry entries are all NULL**, and six native prototype options remain; this is an architecture seam, not real 386 graphics runtime coverage. Exact CI #49 `38449232252` was `in_progress` at docs checkpoint, no current CI-GREEN claim until success. Needed for higher engineering quality: create reproducible legally cleared sprite-to-C/ROM generation with tested input contract (do not handwrite 772 definitions), then MyBoy runtime animation/VRAM/reflection/save/link QA, exact integrated master CI and provenance review. B9 National reward decision remains separate; B10 unmerged.


- **B10 Metapod (#011) real HGSS exception (2026-10-13):** Full pinned source CI #47 SUCCESS on exact `bdba657909e41bdb7a7101008f8c408b2be17803`, run `38444562698`: 385/386 normal+shiny source convertible, single blocker #011. Audited all eight Metapod APNGs at pinned HGSS SHA `f9ee9f83d0f53b196b64d65f7bb70369b196f33b`: down normal and shiny **three** source frames with timings **150/300/150 ms**; up/left/right have four frames. Committed isolated fix `9fe7ed0be77d41cfcd18ac7c4a8ccdda941a695f`: converter/auditor allow three frames ONLY species 11/down with exact 1:2:1 source delays, preserving native poses as four GBA slots `0,1,1,2`. Others still require four; synthetic unit/ZIP coverage tests added in existing files. **CI #48** `38446871759` was `in_progress` at documentation checkpoint; DO NOT claim 386/386 or CI-GREEN until exact #48 succeeds and report is checked. No sprite assets committed or rendered in a ROM; MyBoy, provenance and 386 sprite integration remain outstanding. Next: inspect exact #48 logs/results, fix only proven issues, then real assets runtime wiring and per-species visual QA.


- **B10 full 386 pinned HGSS source audit (2026-10-13):** Confirmed Follower Prototype #45 SUCCESS on exact technical `f6b7e45a8ec0f05e4f5f4ef9277e4c8b1a9bbc8d`, run `38440557027`; 16/32/64px synthetic sprite diagnostic code compiles, not MyBoy verified. Audited native per-frame 4bpp allocation, object reflection main tile reuse, transient palette lifecycle on failed sprite creation/cleanup; no additional proven engine defect selected in this microblock. Shifted to mandatory full Gen I–III normal/shiny feasibility: isolated technical commits `797be93965dd4a29a89faf1eb1d01976545f3088` and `bdba657909e41bdb7a7101008f8c408b2be17803` extend existing `tools/audit_follower_source_samples.py` to fetch **one pinned upstream source ZIP** into runner-only memory, inventory 386 species × regular/shiny × 4 directions, decode all frames, check <=15 colors/BGR555, alpha, animation uniqueness and distinct normal/shiny output, report species and blockers. Synthetic archive preflight and full audit run as new Follower Prototype #47 job `38444562698`, `in_progress` at checkpoint. **NO full 386 outcome or CI-GREEN claim yet; no Pokémon artwork committed, generated into Full ROM or legal rights established.** Network/archive failure must be distinguished from conversion defect. Next: inspect exact #47 result/log and per-species blockers, fix only proven audit/format issues, then scoped runtime data-loader/palette/geometry plus MyBoy QA. B10 still isolated and unmerged.


- **B10 size-aware follower synthetic graphics pilot (2026-10-13):** Follower Prototype #44 SUCCESS exact technical HEAD `c72f22092c82ca11b1a9a8cb9ad2ebdd98ecf85a`, run `38439549516`, verifies 16px dynamic pilot palette isolation/build. Audited native `CreateSpriteAt` uses `AllocSpriteTiles(images->size / 32)` per *current* frame, and object-event spawn sets `spriteFrameImage.size = graphicsInfo->size` before restoring full animation images. Isolated technical commit `f6b7e45a8ec0f05e4f5f4ef9277e4c8b1a9bbc8d` adds synthetic 32px (Snorlax prototype ID) and 64px (Mew prototype ID) 16-frame/four-direction walking diagnostic graphics and normal/shiny variants, using existing runtime palette routing and native 32/64 OAM/subsprite tables, without importing Pokémon art, changing saved state/link structures or global NPC palette slots. Raw 16-frame ROM image sizes: 8192 bytes (32px), 32768 bytes (64px) per variant, but runtime allocates one 512/2048-byte frame respectively; 64px still requires VRAM/OAM pressure and MyBoy visual QA. Follower Prototype #45 run `38440557027` was `in_progress` at checkpoint; no CI-GREEN claim for new HEAD yet. **Next:** verify #45 exact build/source gate, fix only proven errors, then audit per-frame animation indices and sprite palette lifecycle/weather/fades, plan migration to actual 386 indexed 4bpp normal/shiny assets, preserve FireRed ABI. B10 remains experimental and unmerged.


- **B10 real 20-species HGSS audit and isolated palette pilot (2026-10-13):** Exact Follower Prototype #43 SUCCESS (run `38438450305`, HEAD `07cd8db161f10426803a0cf4c0964dcbff177e65`); logs confirm **20/20 real sample normal+shiny pairs convertible without color loss, 20/20 normal/shiny BGR555 render hashes distinct**, 0 semi-transparent pixels; five 64x64 species Lugia/Wailord/Kyogre/Groudon/Rayquaza. This is read-only feasibility, not committed Pokémon artwork or runtime acceptance. `prototype/follower-runtime` technical commit `c72f22092c82ca11b1a9a8cb9ad2ebdd98ecf85a` changes **only diagnostic Pikachu follower graphics** to allocate a dynamic OBJ palette (nonreserved slots >=12 via `LoadSpritePalette`), apply field tint, release it on failed spawn and teardown, and share it with diagnostic reflections instead of clobbering native NPC palettes. Existing NPC reflection behavior unchanged; diagnostic mirror lacks native reflection tint, pending MyBoy QA. Follower Prototype #44 run `38439549516` was `in_progress` at checkpoint, **CI-GREEN not yet verified for this HEAD**. Source-only validation cannot prove all transition paths, sprites or palette behavior. Next: verify exact #44 compilation/validator; adversarially audit palette lifetime on failed allocation, follower swaps, reflection weather fades, map transitions and saturated 12–15 slots. Then evaluate 32/64px dynamic frame streaming, palette/VRAM, real source/provenance, MyBoy before mass 386 integration. B10 isolated/unmerged, 386 normal+shiny still required.


- **B10 real HGSS sample #42 and 20-species expansion (2026-10-13):** Confirmed exact prototype `3a77b3b615c174e9cd22024329896658826ade7e` passed Follower Prototype #42 SUCCESS, run `38429105044`; this is **real upstream APNG read-only feasibility**, not ROM incorporation. GitHub job logs showed Bulbasaur 32px 11/11 BGR555 normal/shiny colors, Pikachu 32px 9/9, Snorlax 32px 13/13, Wailord 64px 9/9, Deoxys 32px 13/13. All five pairs have 4 distinct rendered BGR555 frames per direction, 0 semitransparent pixels, all within 15 visible colors; 32px sheets each 8192 raw 4bpp bytes per variant, Wailord 32768 bytes per variant in ROM. **Runtime OBJ VRAM must contain only current frame** (2048 bytes per 64px frame, 4096 with reflection); never allocate whole 16-frame sheet concurrently. Expanded isolated real sample audit to 20 species incl. Venusaur, Charizard, Alakazam, Gengar, Gyarados, Mewtwo, Mew, Unown, Tyranitar, Lugia, Castform, Metagross, Kyogre, Groudon, Rayquaza via commit `07cd8db161f10426803a0cf4c0964dcbff177e65`. Adds palette/render-identity SHA256 and per-frame VRAM budget, but #43 run `38438450305` status `in_progress` at checkpoint; no 20-species outcome claimed. No graphics committed, no MyBoy or merge. **Next:** confirm exact #43 results, investigate failures/color outliers and palette allocation plus streaming architecture; continue toward mandatory 386 normal/shiny animations.


- **B10 pinned real HGSS asset feasibility audit (2026-10-13):** Follower Prototype #41 SUCCESS run `38425305781` for exact `cb02d48ea6e019efa29c61cbd58521b757c7abab`. New isolated technical commit `3a77b3b615c174e9cd22024329896658826ade7e` adds `tools/audit_follower_source_samples.py` plus a workflow step: a **read-only** pinned-source sample from `teobz/pkmn-hgss-animated-overworld-sprites` SHA `f9ee9f83d0f53b196b64d65f7bb70369b196f33b`, species Bulbasaur, Pikachu, Snorlax, Wailord and Deoxys, each normal and shiny four directions, measures 8-bit RGBA compositing, unique opaque BGR555 colors, semi-transparent pixels, distinct animation frames, exact lossless 4bpp packing eligibility and SHA-256 of inputs. Remote APNGs are downloaded into CI runner temporary directories **only**, never included in GitHub commits, ROM or artifacts. CI #42 run `38429105044` was `in_progress` at checkpoint: no successful real-sample metrics claimed yet. This CI step depends on upstream network availability; if it fails, separate network outage from actual conversion defect before deciding whether to isolate optional source audit from mandatory build. B10 still NOT 386 integrated, not MyBoy-accepted, branch isolated. **Next:** inspect exact CI #42 and evidence, then address genuinely incompatible color/alpha frames and dedicated follower palette/VRAM safely.


- **B10 packed 386 graphics verification (2026-10-13):** Verified exact Follower Prototype #40 SUCCESS (run `38414609819`, SHA `8d4649a5177b14b006bab59117ffdaf1382e7424`). No actual HGSS images were fetched for local conversion in this cycle because public art was not available as container-backed assets; do **not** claim real sample conversion. Additional technical microblock commit `cb02d48ea6e019efa29c61cbd58521b757c7abab` on `prototype/follower-runtime` extends existing `tools/validate_follower_graphics.py` with `--packed-manifest` contract for all 386 Dex entries, 16 tiled 4bpp frames per normal/shiny, directional variation, palette index bounds/16 BGR555 entries, byte budgets (16/32/64px), source path safety, and distinguishability between variants. Synthetic fixture exercises valid and invalid output; no external Pokémon graphics imported or distributed. Follower Prototype #41 run `38425305781` started; **not CI-GREEN until exact SHA success verified**. **Next:** inspect #41 exact results, fix test/code defects if real, then perform bounded sample conversion with access to candidate APNG assets, chart palette/color/size failures, and design dedicated follower palette slot without trampling NPC/reflection palettes. 386 normal/shiny real animated sprites mandatory; MyBoy and master integration outstanding.


- **B10 HGSS APNG → GBA 4bpp conversion pilot (2026-10-13):** Verified Follower Prototype #39 SUCCESS on exact `929125b661d5429d8e5e685ddc5729803fbef4e0`, run `38409285014`. Palette review confirmed FireRed NPC_1 and NPC_2 slots are shared with ordinary map NPCs; diagnostic blue/pink distinction is not a safe final dedicated follower palette solution, so did not mutate native palette registry speculatively. Isolated prototype commit `8d4649a5177b14b006bab59117ffdaf1382e7424` introduces `tools/convert_follower_apng.py`: reads four-frame RGBA APNG per cardinal direction and normal/shiny, reconstructs partial animation rectangles with blend/dispose, validates PNG CRC/deflate/frames/dimensions, converts 8-bit RGBA to BGR555 with explicit failure on semitransparency or more than 15 opaque colors per variant, packs Gen III tiled 4bpp 16-frame sheets and 32-byte palettes, and outputs local conversion manifest. CI synthetic test only; **no Nintendo/HGSS artwork committed and no real 386 asset pack generated in GitHub**. Follower Prototype #40 run `38414609819` status `in_progress` at documentation checkpoint; do NOT claim CI-GREEN pending successful exact SHA conclusion. **Next:** verify #40 build/self-test; inspect actual convertibility and fidelity of candidate APNGs separately, implement dedicated per-follower palette and 16/32/64 OAM/VRAM-safe runtime ingestion, then gate full 386 normal/shiny and MyBoy. B10 experimental, unmerged.


- **B10 diagnostic runtime graphics pilot (2026-10-13):** Follower Prototype #38 SUCCESS on exact `c91b199e4daac6404af751c5fc89790164075ba2`, run `38407893537`; validates shiny identity but not shiny visual graphics. Prototype technical commit `929125b661d5429d8e5e685ddc5729803fbef4e0` adds an isolated *synthetic diagnostic* 16×16 4bpp graphics table (16 frames = 4 per direction), native 8-bit follower graphics-id dispatch for Pikachu only, and palette-slot split regular blue (NPC_1)/shiny pink (NPC_2); no Pokémon artwork imported or new SaveBlock/BoxPokemon/link fields. Diagnostic pilot is not acceptable final follower graphics. **Important limitation**: two shared native NPC palette slots are for testing only, NOT species-accurate independent shiny palette allocation, and directional frames/animation only become runtime-proven by MyBoy visual QA. This commit also adds a CI source gate. Follower Prototype #39 run `38409285014` at checkpoint: `in_progress`; **not declared CI-GREEN until exact successful conclusion**. **Next:** verify exact #39 and diagnose build/validation failures; then investigate per-follower dedicated palette allocation and realistic 32/64px graphics budgets before importing actual animated normal/shiny assets. Required end state remains 386 regular/shiny animated species; provenance clearance and MyBoy acceptance are separate gates. B10 isolated, not integrated.


- **B10 mandatory 386 normal/shiny animated follower target; identity microblock (2026-10-13):** User reaffirmed that **all 386 species in normal and shiny animated presentation are mandatory target requirements**; do not demote them to optional or declare B10 complete with six placeholder/native OWs. Asset reuse/redistribution provenance still must be assessed; technical work must proceed independently. Confirmed Follower Prototype #37 SUCCESS (run `38406562439` on exact `99b1753861cccd1c2e3ee03a6ef5d741af487a58`). On isolated prototype committed `c91b199e4daac6404af751c5fc89790164075ba2`: adds transient shiny identity for **first eligible Pokémon** via native `IsMonShiny`, keeps graphics variant state through sprite lifecycle, forces replacement on shiny swap, and clears on suppression/warp/local reload. New source CI audit; **Follower Prototype #38 run `38407893537` was in progress at checkpoint.** This is NOT actual shiny rendering: still only six native sprites with no regular/shiny OW source assets committed. Existing strict 386 indexed 4bpp directional sheet manifest validator does not convert or visually verify animation. **Next:** verify exact #38 and fix any validation failures; then implement a FireRed-native controlled proof-of-rendering (normal/shiny palette and animation) with synthetic or clearly usable assets, followed by conversion/provenance and 386-by-386 import work. Preserve 8-bit object GFX ID, save/link ABI, isolate branch. B10 not integrated or MyBoy-approved.


- **B10 386 graphic import gate, synthetic proof (2026-10-13):** Exact prototype `8d5eb13b11dac69843a669863db24ee3bb2101ef` passed Follower Prototype #36 SUCCESS (`38405274080`). Bounded field effect/object/sprite allocator inspection found no additional proven urgent engine defect, so no further speculative movement changes. Added `tools/validate_follower_graphics.py` and corresponding isolated workflow self-test on prototype commit `99b1753861cccd1c2e3ee03a6ef5d741af487a58`: pre-import manifest must contain Dex 1–386, both normal/shiny, four named directions, indexed 4bpp PNG sheets of 4 horizontal 16/32/64-pixel frames, CRC/chunk sanity, no duplicate/unsafe paths; self-test uses synthetic graphics only. **CI #37 pending at documentation checkpoint**; the manifest tool validates structure, NOT frame uniqueness, provenance, actual species artwork, palettes across all frames, animated in-game display or MyBoy. No HGSS sprites were imported. **Next:** check exact #37 CI, fix defects if proven; expand preflight incrementally with per-species dimensions/memory and animation quality contract, then isolated actual graphics runtime pilot only with rights-cleared assets, and MyBoy QA when ready. B10 experimental/unmerged; do not claim 386 sprites integrated.


- **B10 #35 CI failure and focused validator repair (2026-10-13):** Follower Prototype #35 run `38400264028` on exact technical HEAD `cd0b67e2111e3b62a7bc018b98f771721aa8a090` **FAILED after successful ROM compilation**. Job step 23 `Audit follower field-effect low-byte identity and reflection capacity` failed a stale `re.search` that required immediate `return;` after `if (reflectionSpriteId == MAX_SPRITES)`; the valid new follower-specific flag reset is inside this guard. No compiler/gameplay failure was established. Validator-only correction `8d5eb13b11dac69843a669863db24ee3bb2101ef` recognizes a braced guard containing safe `return;`, keeps assertions that allocation guard precedes dereference and validates follower-only reflection retry. Follower Prototype **#36** run `38405274080` on exact `8d5eb13` was `in_progress` at this checkpoint, **CI-GREEN NOT YET VERIFIED**. `master` remains documentation-only changed; B10 unmerged, no MyBoy acceptance or 386 animated/shiny coverage. **Next:** verify exact #36 result and failing step if any; only after CI success audit remaining object/sprite pressure (especially reflection liveness and repeated spawn/remove); if no additional defect, move to focused MyBoy QA preparations and graphics feasibility rather than indefinite repetition.


- **B10 rapid follower spawn/despawn and reflection saturation audit (2026-10-13):** Verified Follower Prototype #34 **SUCCESS** (run `38397709014`, exact HEAD `05295757b90ba99728ba861fbe13a9faf6e8f563`), including build, compatibility and low-byte owner/reflection allocation validator. Additional adversarial source inspection confirmed the follower-owned terrain effect cleanup precedes main object teardown, shared resources use native `FieldEffectStop`, and shadow/grass/reflection ownership is detached before object-slot reuse. Found one further bounded visual-recovery defect: native `GetGroundEffectFlags_Reflection` pre-sets `hasReflection=TRUE`, but if all 64 sprite slots are occupied the guarded `CreateCopySpriteAt` returns without creating reflection, so a persistent reflective tile may not retry. Isolated technical commit `cd0b67e2111e3b62a7bc018b98f771721aa8a090` resets `hasReflection` **only for the transient follower** on failed reflection allocation; NPC semantics remain unchanged. Adds a focused gate for native allocation sentinel, flag ordering, follower-only retry, and capacity boundary model (source/model checks; **not** runtime stress proof). **Follower Prototype #35** run `38400264028` was `IN_PROGRESS` at checkpoint, exact HEAD `cd0b67e`; do **not** call it CI-GREEN until verified completed/success for that SHA. `master` gameplay unchanged, no MyBoy runtime, no 386 normal/shiny licensed animated import. **Next:** inspect exact #35 job and failures; if green, audit special reflection persistence and bounded object/OAM pressure independently, then prepare focused MyBoy prototype test scenarios. B10 NOT integrated/CERRADO.


- **B10 follower terrain identity + reflection sprite capacity fix (2026-10-13; technical CI awaiting verification):** Verified prototype previously at `7b27543`, Follower Prototype #32 SUCCESS. Native `StartFieldEffectForObjectEvent` writes only one byte to each 32-bit field-effect argument; attached sprites store those values as 16-bit data, so upper stale bits can defeat full-width field identity comparisons in the new cleanup routine. Separately `SetUpReflection` immediately indexed `gSprites[CreateCopySpriteAt(...)]` without handling `MAX_SPRITES` (64) on sprite-slot exhaustion. Implemented isolated prototype fix `3cb6d6bf49f396d0ef9cf4a9842fa94e21ae6aad`: low-byte comparisons for follower-linked terrain owner IDs and early return on failed reflection copy allocation; adds CI source/edge regression assertions. The new workflow assertion needed an escape-sequence-only repair commit `05295757b90ba99728ba861fbe13a9faf6e8f563`. **Current prototype technical HEAD `05295757`: IMPLEMENTED, NOT YET VERIFIED CI-GREEN, NOT CERRADO, not integrated**. No MyBoy executed and no 386 normal/shiny graphics added. **Next:** inspect exact Follower Prototype workflow run for `05295757`, verify build and regression gate; if red, identify exact failing step before modification. Then adversarially examine repeated spawn/remove and inherited fields under sprite/OAM pressure, and focused MyBoy scenarios. Preserve `master` gameplay and existing save/link ABI; document only proven findings.


- **B10 external graphics/source audit (2026-10-13 — graphics source audit; DOCS-ONLY):** Verified isolated technical HEAD `7b27543d96040604850d2293a20869a5b5d74746` passed exact Follower Prototype #32 SUCCESS (run `38331766149`; ROM build, compatibility, field-effect ownership and follower lifecycle validators). `master` was `7a2b74124cf4dd7c494de1ea97575cca777c7394` before this docs-only checkpoint; no follower feature has merged. Source audit: `aarant/pokeemerald` `followers-expanded-id` provides species-indexed GBA indexed 16-color 192x32 examples (Bulbasaur, Snorlax, Charizard, Wailord), dynamic palette/shiny handling and 440 OW PNGs, but expanding 8-bit object graphic fields to 16-bit is unsafe for Full. `teobz/pkmn-hgss-animated-overworld-sprites` APNG examples have four real animation frames/direction, RGBA rather than GBA indexed (Bulbasaur, Charizard and Snorlax 32x32; Wailord 64x64); previous 386/386 regular and shiny *filename* count remains unproven visually. `WiserVisor/FollowingPokeemerald` has real transition code, but known full-map/palette issues and SaveBlock-based follower state, so review only. `jsunaldo/Pokemon-Fire-Red-Legacy` advertises following sprites but its master `src/` exposes no identifiable follower module; do not regard claim as verified implementation. CompuMax's DS Style forum describes Gen I–III 4bpp indexed normal/shiny GBA OW art but download contents/rights were not audited. Upstream artwork derives from HGSS/Nintendo; all third-party asset import/redistribution rights remain unresolved. **Next bounded microblock:** independent rapid remove/recreate plus terrain field-effect ownership/slot-pressure audit, then focused MyBoy smoke testing; separately prototype a FireRed-native, runtime species-indexed 8-bit graphics slot and normal/shiny 16-color frame conversion with **provenance-cleared or synthetic test assets**, then per-species 386 coverage/size/palette manifests. Do not transplant Emerald ABI, import unlicensed assets, merge B10, or claim MyBoy QA/386 completion. `prototype/follower-runtime` has older copies of production docs; use current `master` production docs for continuation, while verifying prototype branch/HEAD before technical work. This entry supersedes earlier 'CI #32 pending' checkpoint without altering historical records.


- **B10 follower-associated field effect lifetime audit (2026-10-12; CI #32 pending):** Exact experimental `11544894c7e206ea47575fa5c4843e30cd810dc6` passed Follower Prototype #31 (`38328701482`). Native engine audit found field-effect callbacks for reflection, shadow, tall/long/short grass, sand pile, hot springs, feet-in-water and splash retain owner IDs and can reattach to a newly spawned follower when the same runtime local/object slot is reused before effects update. Implemented isolated prototype commit `7b27543d96040604850d2293a20869a5b5d74746`: remove follower-associated field-effect sprites before `RemoveObjectEventInternal` frees main sprite; no change for NPCs or saved flags; native field-effect cleanup for the effect sprites, original reflection invalidation pattern for copies; dedicated CI audit added. **Follower Prototype #32** (`38331766149`) IN PROGRESS at checkpoint; technical HEAD IMPLEMENTED, **NOT YET VALIDATED/CI-GREEN**. **Next:** check exact #32 and failures; verify effect ownership and rapid despawn/re-spawn, sprite exhaustion, terrain visual edge cases; follow with required focused MyBoy runtime scenarios. `master` remains gameplay-unchanged; B10 experimental, no 386 regular/shiny asset coverage or provenance acceptance. Whole-ROM playthrough remains at final integrated release.



- **B10 independent graphics/palette/VRAM lifecycle audit (2026-10-12; documentary checkpoint):** Verified `prototype/follower-runtime` HEAD `11544894c7e206ea47575fa5c4843e30cd810dc6` passed exact Follower Prototype **#31 SUCCESS** (`38328701482`). Read native object-event sprite init/teardown, dynamic follower graphics resolution, `ResumeMap` and return-to-field reconstruction, palette reservation and all six prototype picture tables. Allocation uses ordinary object-event sprite/OAM slots; follower graphics resolve through the native 8-bit table, with teardown using the old image size before graphic switch. Local/link/Quest Log returns discard transient object state before `ResetSpriteData`; regular field palette slots are already reserved and patched by `InitObjectEventPalettes`. Six sheets use **128 bytes (16×16) each except Snorlax 512 bytes (32×32)**; nine frame-table entries per sheet. Distinct source frames: Pikachu/Pidgey/Spearow **3 each**; Snorlax/Mew/Suicune **1 each**. All use shared NPC palette slots/tags: Pikachu/Pidgey/Snorlax BLUE slot 1, Suicune PINK slot 2, Mew GREEN slot 3, Spearow WHITE slot 4. These are inventory/structural checks, **not proof of genuine direction-aware movement, shiny variants, field-effect memory safety under load, or runtime visual acceptance**. No new actionable memory-allocation defect was established from inspected paths, so **NO technical modification, feature commit or new CI** was warranted. `master` gameplay unchanged. **Next bounded B10 microblock:** audit transient field-effect sprites (shadow/reflection/grass) after follower despawn and rapid repeated spawn/reload; identify real allocator/visibility defects before any graphics expansion. Then separately evaluate provenance-cleared 386 regular/shiny directional sheets, palette/OAM/VRAM and size feasibility. B10 remains isolated, unmerged and not MyBoy accepted. The user performs whole integrated-ROM playthrough at end of all blocks.



- **B10 sprite reconstruction audit (2026-10-12; exact Follower Prototype #31 pending):** Verified experimental #30 SUCCESS (`38328196727`) for `0fe0383b0f4d2613040f3cd64361d75e92ab07d3`. Found native `ResumeMap(FALSE)` resets sprite data and calls `SpawnObjectEventsOnReturnToField`, which reconstructs **all active** object events before follower task suppression. Existing transient follower thus could be reconstructed from stale object state during local returns from menus/battles. Isolated technical commit `11544894c7e206ea47575fa5c4843e30cd810dc6` adds `FullFollower_DiscardForLocalReload` before `ResetSpriteData` on ordinary local returns, marking only the transient follower inactive without altering flags/saves or the pending warp gate; link/Quest Log path keeps existing stronger discard and clears warp gate. Strengthened current prototype validator to check both return paths, object-active reconstruction, and proper sprite-reset ordering. **Follower Prototype #31** (`38328701482`) IN PROGRESS at checkpoint: IMPLEMENTED, NOT YET CI-GREEN. **Next:** inspect exact #31, repair only verified failures, continue sprite palette/slot lifecycle and special transitions. B10 remains experimental, not integrated or MyBoy runtime tested; six supported native species only, 386 normal/shiny animated provenance-cleared coverage remains open. The user's integrated whole-game MyBoy playthrough remains scheduled for the end of all blocks.



- **B10 independent local-return entry lifecycle audit (2026-10-12; Follower Prototype #30 pending):** Previous exact experimental HEAD `a07d08b2e29dea076b262d60fbeb6f669c228c2f` passed Follower Prototype #29 (`38327673460`, SUCCESS). Native map-loader review found `InitObjectEventsLocal` and `ReturnToFieldLocal` call `FullFollower_OnLocalMapReady` before `RunFieldCallback`, when entrance animation has not acquired the player-control lock; the unconditional early `RefreshFollower` on non-warp loads can allocate a follower sprite prematurely. Experimental commit `0fe0383b0f4d2613040f3cd64361d75e92ab07d3` removes eager RefreshFollower from map-ready, leaving the existing follower task to process field locks and safely spawn after callbacks. Updated existing CI gate to inspect actual map-load ordering and ensure only task refreshes. **Follower Prototype #30**, run `38328196727`, QUEUED at checkpoint; IMPLEMENTED, **NOT YET CI-GREEN**. **Next:** verify exact #30 status; independently audit special callbacks that never release field lock and sprite object ownership on return from link/Quest Log; adjust narrowly if evidenced. No master gameplay merge, no MyBoy runtime acceptance and no 386 genuine normal/shiny directional coverage/provenance clearance. Final integrated full-playthrough remains at end of project.



- **B10 independent transition audit (2026-10-12; CI #29 pending):** Verified prior exact prototype #28 SUCCESS on `d8d92f2439615f46316440a45f98bf5501208963`. Found short-circuit hazard in `RefreshFollower`: if disabled or party lead is ineligible, `ShouldSuppressFollower` was never called, so the warp lock-observation gate could remain stale and suppress a later eligible lead indefinitely. Isolated technical commit `a07d08b2e29dea076b262d60fbeb6f669c228c2f` on `prototype/follower-runtime` evaluates `ShouldSuppressFollower()` first, keeps object/sprite teardown, and aligns existing validator checks with a transition-gate model for ineligible/eligible leads. Follower Prototype #29 run `38327673460` IN PROGRESS at checkpoint; **IMPLEMENTED, NOT YET CI-GREEN** on this HEAD. `master` gameplay unchanged; B10 remains unmerged and not MyBoy accepted. **Next:** verify exact #29 CI and inspect any failed step; continue adversarial audit of return-from-link-room/Quest Log/ordinary field reload, graphics lifetime and atypical exits. Do not claim 386 normal/shiny animated coverage or asset clearance; final integrated whole-ROM MyBoy playthrough remains user-run at project end.


- **B10 transition handoff / final playthrough policy (2026-10-12):** Verified Follower Prototype **#28 SUCCESS**, run `38324367056`, exact technical HEAD `d8d92f2439615f46316440a45f98bf5501208963`. Door/stair/warp entrance recall is **IMPLEMENTED + CI-GREEN on isolated prototype**, **NOT CERRADO**, not merged to `master`, and not MyBoy-runtime validated. The approved B10 feature still lacks 386 genuine direction-aware regular/shiny overworld animations and asset license/provenance clearance; prototype supports only six native species. **Next bounded microblock:** independently audit the #28 code's field-control-lock release timing, normal versus special map return paths (door/stairs/escapes/teleports, link/Quest Log), graphics and sprite lifetime; repair only demonstrated defects, validate exact HEAD, then plan focused MyBoy scenario evidence. User clarified they will personally perform **a complete playthrough of the whole integrated game at the end of all project blocks**, not a full-game playthrough separately after B10. Preserve necessary targeted technical/visual MyBoy safety gates when applicable; do not mark any unobserved runtime scenario PASS, waive provenance, or merge B10 on static CI alone. Previous B0–B9 technically integrated work remains separate and is not to be retested wholesale as part of this B10 microblock. This docs-only handoff is not a new gameplay HEAD.


- **B10 door/stair/warp entrance transition work (2026-10-12):** Exact Follower Prototype #27 run `38323668000` **SUCCESS** on `7359840ad790db995ac23104f2371ac77b83c0a8`. Native audit found `LockPlayerFieldControls()` is independent of `ScriptContext_IsEnabled()`, so the follower could persist through door/stairs animation or respawn before the destination entrance callback acquired its field-control lock. Isolated **prototype technical** commit `d8d92f2439615f46316440a45f98bf5501208963` adds `FullFollower_RecallForWarp` at 11 field fade transition entrypoints (door, stair, generic, dive, teleport, escalator, special gym, link room), drops transient follower object on departure, and defers destination reappearance until the entrance lock has been observed and released; link cleanup resets the transition gate. Adds dedicated workflow assertion/model for source transition and destination callback ordering. **Exact Follower Prototype #28 run `38324367056` IN PROGRESS at documentation checkpoint: IMPLEMENTED, NOT yet CI-GREEN.** Do not claim MyBoy door/stairs runtime acceptance: must audit source and native entry timing and run real MyBoy checks before B10 integration. Main gameplay branch unchanged; 386 genuine animated normal/shiny coverage and asset provenance still pending. **Next:** check exact #28 run; if failure inspect failing step and repair narrowly; if green independently audit transition lifetime and tests, then MyBoy/manual QA prerequisites.


- **B10 #26 camera-validator repair (2026-10-12):** Follower Prototype #26 run `38320999182` **FAILED** for exact `13c4d33d9839644176942013ee45e278e44c082f`, despite successful ROM compilation and preceding validators. The new source gate `f.index("\nstatic bool8 FollowRecordedPlayerSteps(")` resolved to the earlier function **declaration**, not its later definition, leaving an empty slice of `FullFollower_OnCameraCoordsShift` and raising `AssertionError`. Verified the actual implementation preserves all expected invariants and FIFO wraparound example. Isolated **workflow-only** commit `7359840ad790db995ac23104f2371ac77b83c0a8` anchors its end to the full function definition and searches from the start of the camera hook; invariant checks remain intact. **Follower Prototype #27 run `38323668000` IN PROGRESS at this checkpoint: IMPLEMENTED, NOT YET CI-GREEN.** Next: verify exact #27 result, then independently audit doors/stairs/warps, object lifetime and presentation; no MyBoy runtime proof, 386 animated normal/shiny coverage or production follower integration.


- **B10 camera-scrolling follower tile-trail audit (2026-10-12):** Follower Prototype #25 run `38317181052` **SUCCESS** on exact `2a4bdc92383d5b31db04fb6547d575bdff429a91` (16/8-step count validator repaired). Adversarial audit found native `UpdateObjectEventCoordsForCameraUpdate` shifts every active object event's current/previous/initial map coordinates, but the transient follower's `sLastPlayerX/Y` and queued `sTrailX/Y` remained unshifted, risking false discontinuities and disoriented trail following during ordinary camera scroll. Isolated prototype commit `13c4d33d9839644176942013ee45e278e44c082f` introduces `FullFollower_OnCameraCoordsShift(dx,dy)` and calls it after native event-coordinate shifts, adjusting last player coordinates and only occupied slots of the bounded circular trail; static FIFO-wrap and camera gate added. **Follower Prototype #26 run `38320999182` IN PROGRESS at checkpoint: IMPLEMENTED, not yet CI-GREEN**. Next: confirm exact #26 and independently audit map transitions/doors/stairs and sprite lifetime; no MyBoy validation, 386 genuinely animated normal/shiny sprite assets, provenance clearance or production integration.


- **B10 #24 runner gate correction (2026-10-12):** Verified exact Follower Prototype #24 run `38316400816` FAILURE on `5aa06920d6c53a30071575942a7d0b2a07a5bd67`; ROM compile and prior collision validators succeeded, but new animation pace gate failed with `AssertionError` at `nframes("sSpeedNormalStepFuncs") == 16`. The regex required a trailing comma, yet the engine's final `Step1`/`Step2` table entries have none: it counted 15/7, not 16/8. Confirmed native source tables contain 16 normal and 8 fast entries with optional terminal comma. Isolated prototype **workflow-only** commit `2a4bdc92383d5b31db04fb6547d575bdff429a91` uses line-anchored `Step[1-8]` with optional comma, retaining both strict frame counts. Gameplay unchanged; Follower Prototype #25 run `38317181052` **IN PROGRESS at checkpoint**, not yet CI-GREEN. **Next:** verify exact #25 outcome, investigate any gate failure without weakening checks. B10 remains experimental; no MyBoy runtime, 386 genuinely animated normal/shiny sprites, asset clearance or production merge.


- **B10 #23 validator failure and narrow repair (2026-10-12):** Exact prototype `f14fc6397b80ccea193308d62c2c81ecb5a5a402` Follower Prototype #23 run `38315778673` **FAILURE**, although ROM compiled and earlier checks passed: old collision-recovery static gate still searched for `ObjectEventSetHeldMovement(follower, GetWalkNormalMovementAction(direction))` after run-pace change switched to `movementAction` selected between fast and normal. Source audit confirmed validator stale, no observed C compile error. Isolated **workflow-only** prototype commit `5aa06920d6c53a30071575942a7d0b2a07a5bd67` replaces the obsolete string check with ordered checks of collision gating, both fast/normal selectors and final selected held movement; gameplay unchanged. Exact Follower Prototype #24 run `38316400816` **QUEUED at checkpoint, not yet CI-GREEN**. Next check #24 exact outcome, inspect any new failing step and correct narrowly. No follower integration, MyBoy proof or 386 genuine normal/shiny assets.


- **B10 running pace and ledge jump safety (2026-10-12):** Confirmed exact prior prototype `b62fa950760737c85ec2c615eac5c70e0861c1e2` Follower Prototype #22 `38314580552` SUCCESS. Independent movement review showed player native running steps last 8 frames (`StartRunningAnim` / `MOVE_SPEED_FAST_1`), while follower normal held walks lasted 16 and could accumulate/overflow its eight-step trail during continuous running. Jumping ledges is a special two-tile action (`PlayerJumpLedge`, copyable movement 8), not an ordinary cardinal step, risking incorrect interim trail snapshots. Isolated prototype commit `f14fc6397b80ccea193308d62c2c81ecb5a5a402` uses native `GetWalkFastMovementAction` while player performs ordinary run, normal walking otherwise, and temporarily suppresses follower during active two-tile jump actions. Added static validator of animation timing and jump state. **Follower Prototype #23 run `38315778673` IN PROGRESS at this checkpoint: IMPLEMENTED, not yet CI-GREEN or MyBoy accepted.** Remaining: exact #23 outcome, adversarial inspection of state transitions/scheduler/corner history, stairs/doors, palette/OAM, 386 genuine regular/shiny animations and asset provenance; no production gameplay integration.


- **B10 follower trail recovery from impassable tile (2026-10-12):** Confirmed exact Follower Prototype #21 `38312792550` SUCCESS on `c315ebe09b5409164bbe26808e9cc4e329bb9946`. Audit of `FollowRecordedPlayerSteps` found every nonzero result from the native collision check was treated as temporary occupancy; impassable terrain, border or elevation could indefinitely queue steps until overflowing and recalling. Isolated prototype technical commit `b62fa950760737c85ec2c615eac5c70e0861c1e2` now **waits** only for `COLLISION_OBJECT_EVENT`, **recalls and resets** for other nonzero collisions, and walks only for `COLLISION_NONE`; static/test-model workflow gate added. **Follower Prototype #22 run `38314580552` IN PROGRESS at checkpoint: IMPLEMENTED, NOT yet CI-GREEN or MyBoy-validated.** No changes to production gameplay or persistent save/link layouts. Next: verify #22 exact HEAD; adversarial follow-up on movement queue ordering/timing, player jump mechanics, stairs/warps, graphical memory/OAM; 386 normal/shiny animated coverage still missing and provenance uncleared.


- **B10 adversarial follower collision audit (2026-10-12):** Verified predecessor Follower Prototype #20 SUCCESS for exact `5b1778b8c69a14f0f70b6b833e1c65e4aadee726` (run `38307990688`). Independent source audit found `DoesObjectCollideWithObjectAt` unconditionally ignored every collision when the moving object was the follower, permitting cosmetic walking through NPCs and the current player position. Isolated prototype commit `c315ebe09b5409164bbe26808e9cc4e329bb9946` corrects asymmetry: all world objects ignore the follower as an obstacle; the follower respects current+previous NPC occupancy and the player's CURRENT tile, but can enter the player's vacated previous tile. Added a static gate plus deterministic collision-contract examples. **Exact Follower Prototype #21 run `38312792550` IN PROGRESS at checkpoint: IMPLEMENTED, not yet CI-GREEN or MyBoy accepted.** Further adversarial QA must inspect step scheduling/queue overflow, avatar coordinate transitions, ledges, special doors, height/occlusion and palette/OAM lifetimes. No production gameplay integration; 386 normal/shiny animated sprites still unimplemented and provenance pending. **Next:** verify #21 exact HEAD and audit trail updates before extending feature.


- **B10 first bounded tile-trail prototype (2026-10-12; exact CI pending):** Confirmed previous prototype `3a4ff89aca2a303efe98a416961d379595b53fa9` Follower Prototype #19 run `38303922315` SUCCESS. `MOVEMENT_TYPE_COPY_PLAYER` copies simultaneous actions, not the player's prior route, which can cut corners. New isolated commit `5b1778b8c69a14f0f70b6b833e1c65e4aadee726` switches the follower to `MOVEMENT_TYPE_NONE` with native held walking actions, an unsaved bounded FIFO of player-vacated tiles (8 slots), cardinal adjacency and collision checks, and recall/reset when a warp/jump/discontinuity or queue overflow cannot be represented safely; validator updated to inspect native step lifecycle and a deterministic corner route model. Follower Prototype #20 run `38307990688` was IN PROGRESS at checkpoint: **IMPLEMENTED, NOT YET CI-GREEN**. This is preliminary: runtime scheduling, corner fidelity, jumps, doors, stairs, OAM/palette pressure and MyBoy QA need separate adversarial audit; do not claim HGSS parity. No 386 genuinely animated normal/shiny assets, ownership clearance or production merge. **Next:** check exact CI #20; audit movement and correct any compiler/validator/runtime risk before further features.


- **B10 directional-copy audit (2026-10-12; isolated):** Verified previous Follower Prototype #18 run `38303182183` SUCCESS on exact `7fd4b50722c7751a091a055e36bf020e2079028b`. Native `MOVEMENT_TYPE_COPY_PLAYER` transforms movement using the player initial-facing and follower `directionSequenceIndex`, not trailing-path history. Prototype spawned behind the player with inherited initial orientation, so cardinal steps could rotate (e.g. starting east and walking east moves follower north). Isolated commit `3a4ff89aca2a303efe98a416961d379595b53fa9` sets follower `directionSequenceIndex = DIR_NORTH` after spawn, with a new automated gate that checks all four directions against engine rotation tables. **Follower Prototype #19 run `38303922315` IN PROGRESS at checkpoint; IMPLEMENTED, not yet CI-GREEN.** This is only an absolute-direction copy fix, **not** HGSS-like path following or validated ledge/door/stairs handling. All 386 normal/shiny genuinely animated sprites, provenance review, palette/OAM QA and MyBoy testing remain outstanding; no follower integration into production. **Next:** verify exact #19, then audit/correct actual trailing path in isolated microblocks.


- **B10 Quest Log replay sprite lifecycle (2026-10-12; exact CI pending):** Previous isolated prototype `8a6787ae7e1d8a10b67f4c1215950c5454841b93` passed Follower Prototype #15 run `38302058283` SUCCESS after correcting safe-spawn function declaration (#14 failed compile). Independent audit found `ResumeMap(FALSE)` in Quest Log playback could reconstruct an already active runtime follower sprite before it was suppressed, and local map-load entry could schedule the follower during replay. In `prototype/follower-runtime`, `07d21f0` discards transient follower state before sprite reset when `QL_IS_PLAYBACK_STATE`; `44ebb7b` prevents `FullFollower_OnLocalMapReady` from scheduling a follower during replay; validator commit `7fd4b50722c7751a091a055e36bf020e2079028b` checks both invariants. **Follower Prototype #18** run `38303182183` PENDING at documentation checkpoint. Changes are experimental only, not production-integrated or MyBoy-tested. **Next:** verify exact #18 outcome, independently audit movement (COPY_PLAYER is not a true trailing path), ledges, stairs, door transitions, palette/OAM and save/link. Do not claim 386 animated normal/shiny species or released follower assets.


- **B10 safe interior respawn microblock (2026-10-12):** Independently verified previous isolated prototype `a3a182a90f3995aa5737178ed320f955eea667b0` **CI #13 SUCCESS** (run `38299958371`), including Quest Log exclusion. Audit found the follower's initial placement behind the player did not check map/NPC collision, potentially appearing inside walls or NPCs on indoor transitions. Isolated technical commit `e31d2f94ec87d09efdff42a80addb81135beb4d2` uses the existing player collision engine to check the behind-player tile before spawning; if blocked, retries in subsequent refreshes instead of creating the sprite in an invalid place. No global indoor suppression, save/link layout changes or sprite import. **Follower Prototype #14 run `38300778543` was QUEUED at this checkpoint: IMPLEMENTED, not yet CI-GREEN or MyBoy-validated.** Next: verify exact #14 and independently audit motion on cramped corridors, ledges, special warps, OAM/palette lifetime, object slot pressure and realistic HGSS-follow behavior. Target of 386 animated regular/shiny species remains unimplemented and asset provenance uncleared. No production gameplay change.


- **B10 isolated Quest Log safety microblock (2026-10-12; CI pending):** Investigated movement recording and verified `ObjectEventSetSingleMovement()` records NPC steps while `quest_log.c` replays them through `sMovementScripts[OBJECT_EVENT_TEMPLATES_COUNT][2]`. Runtime follower local ID `254` is outside that fixed table. Prototype technical commit `d62cdae0c9b44fdc634be10bbfee0d1036762bc4` excludes follower movements from Quest Log recording and suppresses its presentation in playback; validator-only follow-up `a3a182a90f3995aa5737178ed320f955eea667b0` fixes the exact function-signature test. **Only the latest prototype HEAD `a3a182a` may be CI-GREEN once exact #13 run `38299958371` succeeds; this is pending at documentation time.** Master remains gameplay-unchanged. Note: full Quest Log state lifecycle, repeated map entry, palette/OAM pressure, geometry, indoor behavior and MyBoy QA are still unaudited/open; no 386 normal/shiny animation coverage or bulk sprite clearance. **Next:** verify exact CI #13, audit replay/memory behavior, then continue isolated mechanics. No production follower merge.


- **B10 follower indoor-presence policy APPROVED (2026-10-12, documentation only):** User approved HGSS-like contextual follower visibility **both outdoors and in safe indoor spaces**; no universal indoor suppression. Bicycle/Surf and incompatible Fly/warp/link/cutscenes temporarily recall the follower, with safe no-duplicate return on foot; overly large species may be restricted in small interiors after geometry/asset/runtime audit. This updates A-012 in `DECISION_AMENDMENTS.md` and B10 in `POLISH_IMPLEMENTATION_MATRIX.md`. Proposed per-species natural flight/hover (Charizard etc.; Dodrio not automatically airborne because it learns Fly) is **NOT yet implemented or fully approved as a 386-category table**. Isolated HEAD `9a4075636bd788fe5f3bdaa77db81b4daa7df37c` remains Prototype CI #11 SUCCESS (run `38297297543`); no MyBoy visual/runtime QA, 386 genuine animations, shiny variant assets or public redistribution clearance. **Next:** isolated memory/palette/size/transition audit; document flight-taxonomy feasibility separately before gameplay implementation. Production gameplay unchanged.\n\n
- **B10.4 verified checkpoint + locomotion concept (2026-10-12):** Follower Prototype **#11 SUCCESS**, exact experimental HEAD `9a4075636bd788fe5f3bdaa77db81b4daa7df37c`, run `38297297543`. Runtime follower spawn/despawn on bicycle, Surf and script suppression is implemented and statically checked; **not MyBoy-accepted**, nor production integrated. FireRed Full `master` still B9 gameplay, with only subsequent documentary commits. User suggested HGSS-style contextual behavior (bike/Surf recall, safe reappearance) and **species-natural locomotion**: Charizard low flight instead of walking, winged species flap, ghosts/Magnemite hover; Dodrio remains ground-running despite knowing Fly. This is **PROPOSED ONLY**, not approved for implementation. Catalogue species into ground / winged flyer / levitator / special and audit actual frame/graphics requirements, OAM, palette and shadow before proposing an implementation. Keep HGSS bike/Surf suppression as baseline unless independently approved. Next technical microblock remains palette/OAM/memory/warp and MyBoy QA, plus provenance-cleared genuine 386 animated normal/shiny sprites; no mass import or final ROM claim.


- **B10.4 sprite/OAM suppression (2026-10-12, isolated):** Prototype #10 succeeded at exact `195b2fa50705e408b16385921e9642de52ccbde6` (run `38296590287`); #9 at `b52fc4f` failed only the new return-path validator matching a declaration instead of implementation, corrected by `195b2fa`. Subsequent review found follower objects were kept allocated while invisible during bike/Surf/script control, and code forced sprite visibility independently of engine off-screen culling. Prototype commit `9a4075636bd788fe5f3bdaa77db81b4daa7df37c` now removes transient follower object/sprite during suppression, recreates when eligible, and leaves sprite visibility to the existing object-event engine; native six-species sprite dimensions/palette slots checked in dedicated workflow gate. **Follower Prototype #11 run `38297297543` was IN PROGRESS when recorded: IMPLEMENTED, NOT YET VALIDATED/CI-GREEN.** Continue by verifying #11 exact SHA, auditing actual memory/palette ownership and transitions, then MyBoy QA. Do not merge into master; six static native species are not 386 animated regular/shiny followers, external asset rights remain unresolved. Last production gameplay B9 remains unchanged.


- **B10.4 isolated follower return-path guard (2026-10-12; exact CI #9 pending):** Read-only review identified a real link-return hazard in `src/overworld.c`: `ReloadObjectsAndRunReturnToFieldMapScript()` was shared by local, link and Quest Log returns yet unconditionally called `FullFollower_OnLocalMapReady()`. Isolated fix on `prototype/follower-runtime` commit `b52fc4fec2516be44a92d7e0213966e849824475` gates the hook for local returns only, excludes link and Quest Log return paths, and clears the transient follower object before `ResumeMap(TRUE)` resets sprites (no persistent flag edits). Follower Prototype #9 run `38296019696` is IN PROGRESS at documentation checkpoint; this SHA is IMPLEMENTED, **not yet CI-GREEN**. Previous #8 run `38294340968` SUCCESS on exact `aee17d1`. Remaining B10.4: investigate object-graphics palette ownership, OAM/tile allocation, map warps and full MyBoy QA. 386 regular/shiny follower coverage and sprite redistribution clearance remain BLOCKED. No follower code integrated into production. **Next: check CI #9 and audit outcomes before another microblock.**


- **B10 isolated prototype update (2026-10-12; CI #8 pending):** `prototype/follower-runtime` #6 passed exact SHA `a60b11b6bc5601f087520dc0c9c914430ce7c52b` (8-bit species-selected graphics slot, CI run `38292418362` SUCCESS). #7 passed exact SHA `3628a486e933dc09dbeb843d2f79bea20cd9bb1f` (despawn ineligible follower without persistent save flag, run `38293461836` SUCCESS). Further independent audit detected that swapping graphic metadata in place could mismatch sprite tile cleanup sizes between species. The follow-up `aee17d119d44a3134a600ebc68c5633df200e16a` now removes the old follower before updating runtime species/graphics and respawns it afterwards; isolated Follower Prototype **#8**, run `38294340968`, was in progress at recording, so this new SHA is **IMPLEMENTED, NOT YET CI-GREEN**. Remaining blockers: MyBoy runtime tests for animation, palettes, OAM and changing party; map/warp/task lifecycle and save/link; licensed/source-cleared assets and all 386 species (regular/shiny). No follower merge, no production gameplay changes, no 386-ready ROM. **Next:** check exact #8 result and independently audit sprite allocation/palette and field transitions before further changes.


- **B10 asset verification update (2026-10-12; RESEARCH):** External `teobz/pkmn-hgss-animated-overworld-sprites` tree `f9ee9f83...` contains regular and shiny APNG filenames in all four directions for every species 001–386 (1,544 per variant). This is filename coverage, **not** a licensed, adapted or QA-validated animated ROM. Local FireRed Full still has 42 native sheets; 5 reuse two frames across all directions and 0 show verified direction-distinct animated walking groups. Isolated follower audit `1da448b7` passed Prototype CI **#5** run `38280331311`. **No production merge or external sprite import.** See `FOLLOWER_TECHNICAL_RESEARCH.md` section 8 for scope, source SHA and gates.


- **B10 complete-species animated follower audit (2026-10-12; RESEARCH / BLOCKED FOR INTEGRATION):** The user requests all 386 animated follower species in an integrated test ROM; this is the target, not a current implementation claim. Inspected isolated branch `prototype/follower-runtime`: CI #3 SUCCESS at `ee9fbc3` only for six-map prototype and basic compatibility; audit workflow commit `da1c64a` added frame inventory (CI #4 SUCCESS), refined by `1da448b` to reject reused generic two-frame poses as full directional walking (exact #5 pending). Production source has 42 native Pokémon sheets (32 with multiple directional/pose frame IDs, 10 one-frame), with 5 sheets reusing two-frame alternation across directions, but 0 verified direction-distinct walking animations; direction poses are not walking animations. Reference Emerald (`monhacks/arrantemerald`) 386 system needs 16-bit graphics-ID architecture incompatible with Full's unchanged object ABI. Another 493-species 4-frame GIF/APNG derivative HGSS source (`teobz/pkmn-hgss-animated-overworld-sprites`) was identified as a research source; veekun-derived Nintendo sprites are **not provenance-cleared for public Full bulk import**. No 386-species integrated ROM, no MyBoy QA, no merge. Next: provenance-cleared 386 walking assets + FireRed runtime species-selected graphic slot design, isolated CI and MyBoy compatibility gates. Technical evidence and full gate documented in `docs/production/FOLLOWER_TECHNICAL_RESEARCH.md` section 8.



- **B9 / National Dex Lucky Egg reward (2026-10-12; CLOSED TECHNICALLY):** Approved Lucky Egg reward for National `HasAllMons()` completion, offered by GAME FREAK designer after original diploma; separate one-time audited flag `0x8D0`, claimed only on successful additem, retry on bag-full. Celadon 4F post-National shop no longer sells Lucky Egg; original rare Chansey held-item source preserved; Kanto Master Ball and diplomas unchanged. Feature implementation `f8a6f438204372ec3ee850932ee32e9531269c76` + read-only continuity `d049f50` + corrected frozen shop validator `0f569f34daa906a4525e3cfc88238e8d5c8ef493`, PR #43. Exact feature Full Gameplay Core #717 run `38276084421` SUCCESS (46 steps); earlier #715 failed obsolete shop availability assertion and #716 predates correction. PR #43 merged to `master` as `f91b8e0b4aa0b10d37838783788e972ee8fcbcd3`; exact integrated Full Gameplay Core #718 run `38276844517` SUCCESS (46 steps). No save-layout/Pokémon struct/link changes. **B9 technical scope CLOSED; MyBoy runtime/visual acceptance remains PENDING**, including bag-full/retry, one-time prize, both rewards owed in the same interaction, and Pokédex UI fit. Next: B10 follower prototype QA/integration decision subject to independent asset provenance/runtime gates; do not begin until inspecting current B10 prerequisites.


- **UI-001 numeric-only EV layout (2026-10-11; CLOSED TECHNICALLY):** User-approved count-only EV presentation without mini-bars, keeping all six native-font EV numbers and one total, native Summary palette and SELECT toggle. Feature branch `feature/ui001-ev-numeric-layout`, technical implementation `0c7d34143695c6d0b7cfa1871187e4f98cd52e0e`, documentation `7c4794b`, workflow expectation update `326d52cdb0600c5911496a4b55ab995bf26f605f`. Earlier feature runs #711 and #712 failed the now-obsolete frozen EV footer-text assertion; the rule was updated to check the current total/summary without dropping all EV checks. Feature Full Gameplay Core **#713 SUCCESS** run `38186222280` exact feature SHA `326d52c`; PR **#42** merged as `55914aa1f9bc3e93761a2aab4c5aa6ca03304196`, exact integrated Full Gameplay Core **#714 SUCCESS**, run `38186603630`, 46 steps. No EV training/math, Pokémon data, saves, link, combat or other UI changed. **MyBoy visual QA pending:** inspect six rows and total at actual resolution, switch SELECT both ways, review edge EV cases (0/252/510). NEXT: resume B9 National 100%-completion additional-reward design decision (not approved), or separately approved next production block; no new gameplay without requisite approval.


- **B9 / P-05 seen-species encounter guidance (2026-10-11; CLOSED TECHNICALLY):** Feature PR #41 (technical commits `c143f85`, compiler include repair `1634d13`, UI width fallback `7ad629f`, and honest on-foot terminology `5e43420`) merged as `cfa0ce4ad9ff9bf40f58ccdc6c012268a44ee867`; exact feature Full Gameplay Core #709 run `38107859214` SUCCESS (46 steps), exact integrated `master` Full Gameplay Core #710 run `38185544115` SUCCESS (46 steps). Read-only seen-species encounter method and level ranges in existing Pokédex area screen; only unlocked Sevii/active Altering Cave tables considered; roaming beasts excluded; existing map markers and save/link untouched. MyBoy visual and runtime QA remains pending. B9 overall OPEN pending separate user decision for National 100% reward. **Next approved separate visual microblock:** UI-001 EV count-only cleanup: remove 28-pixel per-stat mini-bars, keep six aligned EV numbers and total, and preserve summary page, font/palette, save/link and SELECT toggle. No change to EV mechanics.


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
