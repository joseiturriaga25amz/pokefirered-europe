## CURRENT CHECKPOINT — 2026-10-24: Raichu for Magmar source; exact CI pending

- **Third approved trade gate complete on prototype:** `baea8a9234bc3c81cbe12eecd492c32ac87b14af`, FireRed `Doduo -> Lickitung`, original LeafGreen Slowbro request intact. Exact [Full Gameplay Core #40077567451](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/40077567451) **SUCCESS** and [Follower Prototype #40077567460](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/40077567460) **SUCCESS**; independent one-field source diff and unchanged NPC script PASS. This is source IMPLEMENTED + VALIDATED + CI-GREEN on prototype, **not integrated/CERRADO on master**, MyBoy exchange QA separate.
- **Fourth technical implementation SHA `bf397c4c8b44b4bca6b98cb35071d22ce8b68470`**, `INGAME_TRADE_ELECTRODE` in `src/data/ingame_trades.h`, Cinnabar Lab Lounge: FireRed **Raichu -> Magmar** and new nickname Spanish `BRASAS`, Italian `BRACE`, French `BRAISE`, German `GLUT`, English `EMBER`. LeafGreen remains original **Raichu -> Electrode**, with its exact previous nickname and species. Only FireRed nickname/reward fields split from the previously shared record using `#if defined(FIRERED)` / `#elif defined(LEAFGREEN)`; requested species remains shared Raichu. Preserved original OT `CANEL` (Spanish), IVs `{19,16,18,25,25,19}`, personality `0x06341016`, `ITEM_NONE`, offered-Pokémon level and existing `FLAG_DID_ESPHERE_TRADE`. No new flag/ID, no NPC script edit and no save/link ABI changes.
- **Independent source audit PASS:** replacing the two-field version split with original nickname and Electrode species, and removing five new nick macros, restores exact source header. NPC script blob unchanged; original LeafGreen data untouched. Scope exactly three technical files: trade header, dedicated new Full Gameplay Core semantic validator, audited trade blob SHA. No edits to previous 3 NPC trade slots.
- **CI still IN PROGRESS at writing**: exact [Full Gameplay Core #40077986613](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/40077986613), [Follower Prototype #40077986626](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/40077986626) on technical SHA `bf397c4c8b44b4bca6b98cb35071d22ce8b68470`. Validate both before CI-GREEN claims or next gameplay commit; diagnose exact failed step if needed. Docs-only commits afterward do not alter ROM.
- **NEXT after gate:** fifth distinct trade `Venonat -> Electabuzz` in `INGAME_TRADE_TANGELA` (same Lounge, Norma). Original shared `Venonat -> Tangela` must remain as-is for LeafGreen; FireRed gets Electabuzz and localized nickname (Spanish `CHISPA`). Preserve OT `DULCE`, Stardust, IV/personality, old `FLAG_DID_TANGENY_TRADE`, special-script handling, save compatibility. Then final sixth `Koffing -> Seel` in Experiment Room as separate technical microblock. No B10 merge, no MyBoy acceptance claim.

---

## CURRENT CHECKPOINT — 2026-10-24: third approved trade Doduo -> Lickitung technical CI pending

- **Last game-changing technical SHA** `baea8a9234bc3c81cbe12eecd492c32ac87b14af` on `prototype/follower-runtime`. **Staryu predecessor exact CI now confirmed GREEN**: `840e002d70d171de7b4e0d1ad09eac0d25f9c7ff` Full Gameplay Core [#40072383187](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/40072383187) **SUCCESS**, Follower Prototype [#40072383184](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/40072383184) **SUCCESS**; FireRed Drowzee->Staryu implementation, original LeafGreen and one-time flag unchanged. First Shellder trade `4f9faf6` also exact Full #40071937495 and Follower #40071937490 SUCCESS. Both prior trade source microblocks VALIDATED + CI-GREEN ON PROTOTYPE but NOT integrated/closed on master.
- **Third trade source IMPLEMENTED** `baea8a9234bc3c81cbe12eecd492c32ac87b14af`: `INGAME_TRADE_LICKITUNG` in `src/data/ingame_trades.h` now **FireRed `DODUO -> LICKITUNG`** in Route18 East Entrance 2F, replacing only the old requested `SPECIES_GOLDUCK` with `SPECIES_DODUO`. The original LeafGreen `SLOWBRO -> LICKITUNG`, Lickitung nickname (`LICKITITO` in Spanish), OT `DIOCHO`, `{24,19,21,15,23,21}` fixed IVs, personality `0x451308ab`, held `ITEM_NONE`, and `FLAG_DID_MARC_TRADE` remain unchanged. No map, script, party/save/link ABI modification. Independent exact source comparison: replacing this one FireRed request restores byte-for-byte previous trade header; NPC script blob unchanged; eight other trade entries and all localized names intact.
- New **Full Gameplay Core targeted semantic assertion** confirms pair, original LeafGreen requirement, metadata and persistent save flag, and updated exact `src/data/ingame_trades.h` blob lock; these are the only other two technical diff files. Exact Full Gameplay Core [#40077567451](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/40077567451) and Follower Prototype [#40077567460](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/40077567460) **IN PROGRESS at this checkpoint**, not yet CI-GREEN. Never claim CI success without exact run results.
- **Next microblock after exact CI success:** fourth approved trade **Raichu -> Magmar** in the `INGAME_TRADE_ELECTRODE` slot, Cinnabar Lab Lounge. Source currently shares original `RAICHU -> ELECTRODE` across FR/LG, so introduce a narrowly scoped `#if defined(FIRERED)` FireRed reward `MAGMAR` and original request `RAICHU`, leaving LeafGreen original reward `ELECTRODE`, request `RAICHU`, nickname, OT/IV/personality/held item and original `FLAG_DID_ESPHERE_TRADE`. Distinct localized FireRed-only Magmar nickname (Spanish `BRASAS`). Do not edit any other trade entries in this technical microblock. Then distinct fifth Venonat->Electabuzz and sixth Koffing->Seel technical CI gates.
- **Not complete:** entire six-trade plan is still in progress; branch B10 divergent from `master` `8d89f2b4` and MyBoy runtime acceptance not done. Subsequent documentation-only commits do not affect exact technical SHA.

---

## CURRENT CHECKPOINT — 2026-10-24: Route11 Staryu exchange IMPLEMENTED, CI pending

- User's six-pair trade plan approved by contextual `Perfecto continúa` and recorded as 2026-10-24 decision in `DECISION_AMENDMENTS.md`. First exchange **Meowth -> Shellder**, technical `4f9faf614cbf24371c9e1b4f625e5ce6e56a65de`, was independently audited and passed **exact Full Gameplay Core #40071937495 SUCCESS** and **Follower Prototype #40071937490 SUCCESS**. Spanish received nickname PERLITA. Its specific continuity and original LeafGreen preservation remain in previous checkpoint below.
- Second separate technical commit **`840e002d70d171de7b4e0d1ad09eac0d25f9c7ff`** implements **Drowzee -> Staryu** at Route11 East Entrance 2F, FireRed only. Changed original `INGAME_TRADE_NIDORINOA` FireRed's requested Nidorino and offered Nidorina to requested Drowzee and offered Staryu. Received nickname localizations Spanish `ESTRELLA`, Italian `STELLA`, French `ETOILE`, German `STERNCHEN`, English `STARLIGHT` (within 10-char Gen III name budget). Keeps original OT `ONZANO`, IVs `{22,25,18,19,22,15}`, personality `0x00eeca15`, `ITEM_NONE`, inherited level, original `FLAG_DID_NINA_TRADE`, NPC script and original LeafGreen Nidorina->Nidorino. Independent source comparison PASS: other eight trade entries unchanged, LeafGreen record byte-identical, original NPC script unchanged, no save/link structs modified.
- The source commit adds a dedicated **Full Gameplay Core semantic check** for requested/reward species, nicknames, old save flag, OT/IVs/item and preservation of LeafGreen, plus updated `src/data/ingame_trades.h` exact audited blob SHA. Its exact **Full Gameplay Core [#40072383187](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/40072383187)** and **Follower Prototype [#40072383184](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/40072383184)** had just started and were **IN PROGRESS** at this checkpoint; **DO NOT** mark second trade CI-GREEN or CERRADO until results are verified.
- **NEXT:** inspect exact CI for technical `840e002`, diagnose any actual failure; if both pass, register successful gate and move to the third **Doduo -> Lickitung** FireRed-only `INGAME_TRADE_LICKITUNG` (change original Golduck request only; LeafGreen Slowbro request untouched), with its own validator, audited blob SHA and exact Full Gameplay Core / Follower run. The master branch remains `8d89f2b4`, prototype follower B10/MyBoy runtime integration OPEN. No merge yet.

---

## CURRENT CHECKPOINT — 2026-10-24: Meowth for Shellder verified on prototype

- The user accepted the prior six-pair recommended plan by replying `Perfecto continúa` directly to the explicit approval question; recorded as a **dated production amendment**. Nine-slot matrix in that amendment; six trades to be implemented individually without side effects on LeafGreen or old-save flags.
- First technical commit **`4f9faf614cbf24371c9e1b4f625e5ce6e56a65de`** on `prototype/follower-runtime` modifies `INGAME_TRADE_NIDORAN` **FireRed only**: Route5-area NPC accepts `Meowth` and awards `Shellder`, keeping the old `FLAG_DID_MS_NIDO_TRADE`, OT `QUICA`, original IVs/personality, held Tiny Mushroom and offered-Pokémon level. Original LeafGreen NidoranF->NidoranM data was byte-compared and unchanged. Reward nicknames for Spanish/Italian/French/German/English `PERLITA/PERLINA/PERLETTE/PERLE/PEARL`; original Nidoran nicknames retained but no longer used in FireRed. No scripts/maps/save/link structs edited.
- Same commit adds **targeted Full Gameplay Core test** for FireRed pair/nickname/metadata, LeafGreen original pair and the preserved NPC one-use flag. Audited trade-data blob SHA updated. Adversarial diff: all other eight in-game trade blocks unchanged, LeafGreen original branch byte-identical, NPC script byte-identical, original trade OT/IV/personality/held data retained. Static source audit PASS.
- At checkpoint, exact technical Full Gameplay Core [#40071937495](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/40071937495) and Follower Prototype [#40071937490](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/40071937490) are both **SUCCESS** on exact SHA (Full Gameplay Core, including reproducible ROM and trade/static validators; Follower Prototype, including temporary 386 normal/shiny builder). **Source IMPLEMENTED + audited + CI-GREEN ON PROTOTYPE**; branch not master-integrated and MyBoy trade/runtime QA still pending. The following documentation-only checkpoint does not change ROM/validators. Later documentation-only commit(s) cannot invalidate this technical SHA's gameplay content if diff proves documentation-only.
- **NEXT:** begin **Drowzee -> Staryu** at Route11 2F in a separate narrowly scoped technical commit with FireRed-only data and all language nicknames; preserve LeafGreen Nidorina->Nidorino and original save flag. Existing Jynx technical `ecd3a73` CI-GREEN earlier; B10 follower master integration and MyBoy QA remain OPEN.

---

## SOURCE AUDIT — 2026-10-24: Cinnabar Lab exchanges and trade approval packet

**STATE: SOURCE-AUDITED / PROPOSED, NO GAMEPLAY IMPLEMENTATION.** Branch `prototype/follower-runtime`; last technical SHA `ecd3a73` (Jynx FireRed Clefairy, LeafGreen original Poliwhirl) passed Full Gameplay Core #39995711513 and Follower Prototype #39995711582, not merged into master. The Route18 trade audit is docs-only `aa3310a` and preceding Route5/Route11 audits docs-only. A subsequent doc commit never replaces exact-sha technical CI or MyBoy runtime acceptance.

### Cinnabar laboratory original scripts / safe scope

- Two shared in-game NPC trades in `data/maps/CinnabarIsland_PokemonLab_Lounge/scripts.inc`: `INGAME_TRADE_ELECTRODE`, `FLAG_DID_ESPHERE_TRADE` (Clifton), and `INGAME_TRADE_TANGELA`, `FLAG_DID_TANGENY_TRADE` (Norma). Their dialogue dynamically buffers offered/requested species; Norma's code uses the direct specials sequence rather than the shared wrapper, but checks selected species, completion and one-time flag. Source scripts are valid as-is for swapping species. Both NPC objects exist in Lounge `map.json`, reached through Lab Entrance (no story scene prerequisite in the trade scripts).
- `data/maps/CinnabarIsland_PokemonLab_ExperimentRoom/scripts.inc` has the `INGAME_TRADE_SEEL` NPC (Garett) with `FLAG_DID_SEELOR_TRADE` and dynamic species names; this experiment room also contains fossil revival but the trade itself has no fossil prerequisite. Keep all original flags and IDs, including their obsolete nicknames: saves that have traded must continue showing completion.
- All three legacy `INGAME_TRADE_ELECTRODE`, `INGAME_TRADE_TANGELA`, `INGAME_TRADE_SEEL` records currently **share their reward species, nickname and requested species across FireRed and LeafGreen**. Unlike Jynx/Nidoran, there is no pre-existing FR/LG split in these three entries. Any new FireRed request/reward must be explicitly `#if defined(FIRERED)` with original `#elif defined(LEAFGREEN)` in reward/nickname/request fields. Preserve original OT, IVs/personality and items unless a distinct approved reason arises. Never overwrite LeafGreen's original trade rewards.

### Economics and chronology, source-verified

1. **Raichu -> Magmar** (Lounge Clifton, replaces Raichu -> Electrode): Pikachu is 5% in Viridian Forest (4+1%), also **25%** in Power Plant (10+10+4+1%); Thunder Stone available Celadon Department Store before National Dex, so Raichu needs a deliberate item investment. FireRed wild Magmar **5%** (4+1%) at Mt Ember Exterior, typically reachable on Sevii after the Blaine ferry trigger. The Cinnabar Lab trade can bring Magmar earlier, before its natural wild site; this is the strongest chronology improvement among the three. Level of received Magmar equals offered Raichu from `src/trade_scene.c`; no fixed-level gift. Preserve original `FLAG_DID_ESPHERE_TRADE`, `ITEM_NONE`, OT `CANEL` (Spanish), fixed IVs `{19,16,18,25,25,19}` and fixed personality. Replace inherited Spanish Electrode nickname `BOLICHI` with a short Magmar-appropriate nickname, proposed **BRASAS** (localize for other EU languages; no user nickname approval yet).
2. **Venonat -> Electabuzz** (Lounge Norma, replaces Venonat -> Tangela): Venonat FireRed **30%** across Routes12–15 (20+10%), **19%** Safari Center/West (10+4+4+1%), and a late Berry Forest presence. Wild FireRed Electabuzz **5%** (4+1%) at Power Plant, obtainable with Surf before Cinnabar for a prepared player. Thus Cinnabar NPC **does not advance the earliest natural Electabuzz area**, but rewards a common species in exchange for avoiding a rare 5% hunt and can offer trained-OT bonus EXP. Recommended as a convenience/collection trade, not a unique new Pokémon source; do not change intrinsic catches/flee or Power Plant rates. Preserve original `FLAG_DID_TANGENY_TRADE`, held `ITEM_STARDUST`, OT `DULCE` (Spanish), IVs `{22,17,25,16,23,20}`, fixed personality; change old Spanish `TANGELITO` nickname to appropriate **CHISPA** or comparable short Electric nickname (all languages to be checked).
3. **Koffing -> Seel** (Experiment Room Garett, replaces Ponyta -> Seel): FireRed Koffing **30%** land (20+10%) in Pokémon Mansion 1F/2F/3F/B1F, same Cinnabar Island as the lab; input is directly farmable on arrival, levels28–30. FireRed Seel is obtainable naturally **20% Seafoam B2F, 40% B3F, 50% B4F** and 60% B3F/B4F Surf encounters; this NPC does **not** make Seel scarce, but helps a player who reached Cinnabar from Pallet without passing Seafoam. Seel evolves by level34 into Dewgong; traded reward inherits Koffing's level rather than free level34 evolution. Original reward nick `SEELÍN` is already fitting (keep all languages), OT `GOYO` (Spanish), `ITEM_NONE`, IVs `{24,15,22,16,23,22}`, original `FLAG_DID_SEELOR_TRADE`. **Only** request changes for FireRed `SPECIES_KOFFING`; keep LeafGreen `SPECIES_PONYTA` -> Seel without alteration.

### Decision package for review (9 total NPC exchanges)

| NPC slot | FireRed plan | Status |
| --- | --- | --- |
| MR_MIME | Abra -> Mr. Mime | keep original; unchanged |
| JYNX | Clefairy -> Jynx | already implemented, exact technical CI-GREEN on prototype |
| NIDORAN | Meowth -> Shellder | audited, recommended, needs explicit approval; rename new FR nickname e.g. PERLITA |
| FARFETCHD | Spearow -> Farfetch'd | keep original; unchanged |
| NIDORINOA | Drowzee -> Staryu | audited, recommended with earlier Starmie power trade-off, needs approval; e.g. ESTRELLA |
| LICKITUNG | Doduo -> Lickitung | audited, recommended, needs approval; keep original LICKITITO |
| ELECTRODE | Raichu -> Magmar | audited, recommended; costs Thunder Stone and advances pre-Sevii access; e.g. BRASAS |
| TANGELA | Venonat -> Electabuzz | audited, recommended; Power Plant naturally earlier; e.g. CHISPA |
| SEEL | Koffing -> Seel | audited, recommended; wild Seafoam already abundant; retain SEELÍN |

**Scope**: all six further conversions are *candidate designs*, not automatically approved. On explicit consolidated approval use **one coherent NPC trade at a time**, each with bounded source + localized nickname + validators/obtaining-route test + exact trade data blob SHA + Full Gameplay Core and Follower Prototype exact SHA; keep original LeafGreen outputs in each. No new saves, flags, IDs or maps. Audit changed scripts only if necessary, avoid incidental boss/EV/follower changes. Trade QA in MyBoy remains future RC. No change to original Mr Mime, Farfetch'd or already completed Jynx. Approved design may require separate subsequent discussion if user rejects cost/reward or nicknames.


---

## SOURCE AUDIT — 2026-10-24: Route18 Doduo for Lickitung

**Read-only candidate assessment; no gameplay change or final pair approval.** Verified `prototype/follower-runtime` HEAD `7ba2ced79fc63cf00bb8d3eff54f4a3605dcd467`; the last gameplay SHA `ecd3a73` passed both exact workflows. Subsequent trade-audit commits are docs-only, not evidence that a new trade was implemented.

- **NPC / current data:** `Route18_EastEntrance_2F_EventScript_Haden` calls `INGAME_TRADE_LICKITUNG`, uses dynamic request/reward text, validates party species and protects one-time trade with `FLAG_DID_MARC_TRADE`. `src/data/ingame_trades.h` offers `SPECIES_LICKITUNG` with original Spanish nickname `LICKITITO`, OT `DIOCHO`, IVs `{24,19,21,15,23,21}`, fixed personality `0x451308ab`, `ITEM_NONE`, and **FireRed `GOLDUCK` vs LeafGreen `SLOWBRO` requested species**. Neither reward nor nickname needs alteration.
- **Actual encounter balance:** in `src/data/wild_encounters.json`, **Doduo 35% land** in each of FireRed Routes **16/17/18**, via slots 20% at level18/24, 10% at 20/26 and 5% at 22/28 respectively; also Safari East/West (21%). Existing Golduck is wild only in later Seafoam Islands and Cape Brink land slots (Golduck also evolves from Psyduck). There are **no wild Lickitung entries in the inspected encounter JSON**, so the original NPC reward is a meaningful collector acquisition rather than a common swap. Do not claim Lickitung entirely unobtainable via other scripts without whole-project script audit.
- **Pathing / bike caveat:** Route18 2F is directly upstairs from Route18 East Entrance 1F (`map.json`), which has exits onto Route18; Route18 connects east to Fuchsia City and north to Route17 Cycling Road. The first-floor `scripts.inc` enforces the Bicycle for cycling-road traversal, not a direct trade-trigger gate; from the Fuchsia side the building is a reasonable destination when Fuchsia is reached, though do not advertise it as pre-Fuchsia or universally accessible without route prerequisites. A captured Doduo from Routes16–18 naturally precedes or coincides with the NPC.
- **Engineering design recommendation: APPROVE candidate subject to user sign-off**: for FireRed only change `.requestedSpecies = SPECIES_DODUO`, preserving `SPECIES_LICKITUNG`, nickname `LICKITITO`, OT, held item, IVs, original flag, script, link/save structs and exact LeafGreen request `SPECIES_SLOWBRO`. The exchange inherits offered Doduo level from `src/trade_scene.c`. It improves trade feasibility without injecting early high-level or evolved reward. Validate both version branches, one-time flag, remaining 8 trade entries, blob lock and exact Full Gameplay Core upon later implementation.
- **Next:** assess the **three Cinnabar Pokémon Lab trade slots** as one cohesive read-only source audit (Raichu->Magmar, Venonat->Electabuzz, Koffing->Seel), especially whether Magmar would advance Mount Ember chronology, whether Electabuzz is already accessible in Power Plant before Cinnabar, and whether Koffing's low encounter/capture effort justifies Seel's utility. No gameplay edits before the final request/reward/nickname packet is approved.


---

## SOURCE AUDIT — 2026-10-24: Route11 Drowzee for Staryu

**State: SOURCE-AUDITED PROPOSAL, not implemented or unambiguously user-approved.** Branch `prototype/follower-runtime`, last technical `ecd3a73` still CI-GREEN, master integration and MyBoy acceptance still pending. The immediate predecessor `b6eb140` is a docs-only Meowth -> Shellder assessment, NOT ROM/gameplay.

**Candidate:** replace **FireRed only** NPC exchange `Nidorino -> Nidorina` at `Route11_EastEntrance_2F` with **Drowzee -> Staryu**, preserving existing `INGAME_TRADE_NIDORINOA` index, the original `FLAG_DID_NINA_TRADE`, NPC `Route11_EastEntrance_2F_EventScript_Turner` and all save/party/link ABI. The NPC in map 2F is reached via stairs in `Route11_EastEntrance_1F` (Route11 warps), without a requirement to wake Route12's Snorlax; the separate lookout text referencing Snorlax does not gate the trader.

**Source-backed access:** `src/data/wild_encounters.json` FireRed Route11 land Drowzee is **25%** at levels 11 (10%), 13 (10%) and 15 (4%+1%). FireRed Vermilion City Staryu is **40% with Super Rod** (slot6, levels 15–25); the rod is a later gift in `Route12_FishingHouse/scripts.inc`, not an item needed to obtain Drowzee. A trade creates the offered Staryu at the player's delivered Drowzee level, so typical output 11–15, not an overlevelled fixed gift. Staryu starts with Tackle/Harden, Water Gun at 6, Rapid Spin 10, Recover 15 and later BubbleBeam 28; evolution `SPECIES_STARYU -> SPECIES_STARMIE` uses Water Stone from Celadon Department Store 4F even before National Dex. Hence this *advances* access to an effective Water/Psychic evolution in midgame (Starmie), **but does not grant Starmie at Route11 nor alter the NPC's level**. Its battlefield strength merits a deliberate balanced choice rather than describing the trade as value-neutral. Misty's existing Staryu/Starmie already showcase this species earlier in the adventure.

**Legacy/version/text:** FireRed existing trade nickname Spanish `NIDRINA` is species-inappropriate for a Staryu; proposed new short Spanish nickname `ESTRELLA` (eight letters), with proper counterparts for Italian/French/German/English at any subsequent approved implementation. Preserve OT `ONZANO`, IVs/personality and `ITEM_NONE` rather than gifting an extra held item. Existing `#elif defined(LEAFGREEN)` `Nidorina -> Nidorino` request/reward/nickname must remain byte-identical; all 8 other trade sections unaffected. Generic exchange dialogue dynamically inserts request/reward species; no local text scripts need changing. Retain `FLAG_DID_NINA_TRADE` even if the mnemonic becomes obsolete so old saves cannot repeat a completed trade. No new species IDs, map, NPC, flag or SaveBlock.

**Recommendation:** favorable, with a known early-Staryu / Celadon-Starmie power trade-off. Maintain simple Drowzee request and current trade metadata, change only FireRed species fields and nickname after final approval, and explicitly test Water Stone access and gym curve. Prefer no additional level gate, new item or NPC. A future targeted Full Gameplay Core validator should assert species/version branch, one-time flag, dynamic request and preservation of other 8 NPC trades plus trade blob lock; then exact CI and eventual MyBoy runtime. No edits to gameplay in this audit.

**NEXT:** bounded evaluation of `Route18_EastEntrance_2F` Doduo -> Lickitung, followed separately by Cinnabar Magmar/Electabuzz and Seel exchange tradeoffs. Consolidate user-facing decision roster after the remaining source checks, avoiding repeated votes for minor source-safe details.


---

## SOURCE AUDIT — 2026-10-24: Underground North Meowth for Shellder

**Status: PROPOSED / SOURCE-AUDITED ONLY; no trade source changes, no design approval inferred from a favorable reaction.** The 2026-10-23 Jynx technical commit `ecd3a73` remains source-validated and exact Full Gameplay Core #39995711513 + Follower Prototype #39995711582 SUCCESS, the following docs-only `cf32aab` was separately exact-head green on Full Gameplay Core #39996594294 + Follower Prototype #39996594163. Current `prototype/follower-runtime` is not master-integrated; B10/MyBoy still outstanding.

**Candidate:** Replace **FireRed only** existing UndergroundPath North Entrance trade `Nidoran male -> Nidoran female` with **Meowth -> Shellder**, using the existing `INGAME_TRADE_NIDORAN` index, NPC script `UndergroundPath_NorthEntrance_EventScript_Saige` and persistent `FLAG_DID_MS_NIDO_TRADE`. Preserve original `LeafGreen Nidoran female -> Nidoran male` and all other NPC trade slots. In old saves that already set the one-time flag, the new reward must remain claimed/unavailable; clearing/reassigning it would allow trade duplication.

**Measured access/economy:** `src/data/wild_encounters.json` FireRed Route5 Meowth has **15%** land odds at levels 12 (10%), 14 (4%) and 16 (1%); Route6 Meowth is 35%. Route5 `map.json` warps directly into the NPC's entrance; its script dynamically buffers requested/reward species and checks party species. No hard-coded `Nidoran` in map script, only legacy flag/constant names, which should remain unchanged for save compatibility. Shellder is available later by **Super Rod (slot6, 40%)** in S.S. Anne Exterior, Pallet Town, Cinnabar Island, One Island and other mapped waters; the Super Rod is obtained from the Route12 Fishing House script, not available to a player arriving at Route5 for the first time. The S.S. Anne fishing location is sensitive to ship departure and must not be represented as permanently reachable. This is an early optional Dex access route, not an exclusive species or reward requiring National Dex. Wild catch rates: Meowth 255 and Shellder 190, making this a meaningful but not punitive convenience trade.

**Power curve:** `src/trade_scene.c` preserves the player's offered Pokémon level; the Shellder reward would ordinarily be levels 12–16 rather than a fixed high-level gift. It learns Icicle Spear at 8, Supersonic 15, Aurora Beam 22; it is Water type before Water Stone evolution. `src/data/pokemon/evolution.h` evolves it with `ITEM_WATER_STONE`; Celadon Department Store 4F offers Water Stone even before National Dex, so Cloyster (Water/Ice) becomes obtainable after reaching Celadon, not immediately at Route5. The original traded Nidoran female carries nickname **NIDRANA** in Spanish, and version-specific nicknames in other four languages; reusing those strings for a Shellder is poor polish. Recommend new short, context-appropriate FR nickname (Spanish **PERLITA**, verify all EU languages' max name/encoding) and retain original OT `QUICA`, fixed IV/personality and held Tiny Mushroom unless separate design review justifies changing them. Retain `FLAG_DID_MS_NIDO_TRADE` despite obsolete mnemonic and unchanged current quest log/save semantics. No need for new NPC, map, data IDs, mail, OT or save structure.

**Safety review for a future approved implementation:** guard `#if defined(FIRERED)` fields for requested `SPECIES_MEOWTH`, reward `SPECIES_SHELLDER`, matching FR nickname. Preserve the `#elif defined(LEAFGREEN)` block byte-for-byte. Check nickname definitions in Spanish/Italian/French/German/English, trade scene's dynamic text and level inheritance, party full/egg/cancel paths, no one-time flag changes, and other eight trade slot hash/membership. Add focused Full Gameplay Core assertions on both versions + one-save obtainability as needed, update existing audited trade-blob SHA, exact Full Core/Follower CI, and retain MyBoy trade/old-save QA for the final RC. No broad NPC trade batch.

**Engineering recommendation:** **yes, favorable choice** at existing Route5 location, with original Tiny Mushroom and version scope retained; unlocks a later fishing species earlier without a free fully evolved Cloyster or new engine feature. **Do not mark IMPLEMENTED or APPROVED yet.** Next review `Route11_EastEntrance_2F` Drowzee -> Staryu: this candidate may need stronger power-curve restraint because Starmie can evolve by Water Stone and has significant midgame utility.


---

## CURRENT CHECKPOINT — 2026-10-23: Cerulean Jynx trade CI-GREEN (not integrated)

**Active source branch:** `prototype/follower-runtime`. Exact technical HEAD `ecd3a73eca1bc58a08157a42a83b140edf0dd078`; master `8d89f2b4` remains separate and B10 follower OPEN. The source is IMPLEMENTED + static/compile VALIDATED + **CI-GREEN on prototype**, but NOT integrated/CERRADO and not accepted on MyBoy.

- `5f64e11`: approved Cerulean `Clefairy -> Jynx` request; targeted Full Gameplay Core test and exact audited `src/data/ingame_trades.h` blob lock. `0b0177d` protects **LeafGreen's original Poliwhirl -> Jynx** request with existing preprocessor structure; FireRed only gets Clefairy. Original Jynx nickname ZYNX, OT, IVs, nature personality, mail, level inheritance, script and `FLAG_DID_ZYNX_TRADE` preserved. Source diff independently confirmed other eight NPC trades unchanged byte-for-byte; no SaveBlock/link layout changes or new ID. Clefairy wild in Mt Moon (10%) before Cerulean; generic text substitution needs no map/Spanish script edit.
- Intermediate `5f64e11` Full Gameplay Core [39995000989](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/39995000989) **failed only at an obsolete one-save baby-obtainability validator after successful ROM compile and targeted Jynx test**: it expected unconditional Poliwhirl. `ecd3a73` updates `tools/validate_full_obtainability.py` to assert FireRed Clefairy availability, Jynx NPC/one-time flag and unchanged LeafGreen Poliwhirl + Poliwag path; does not weaken the Smoochum obtainable-in-one-save invariant. All other validator obligations unchanged.
- **Exact technical CI success:** Full Gameplay Core [#39995711513](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/39995711513) SUCCESS (including reproducible Spanish ROM and complete static gameplay gates); Follower Prototype [#39995711582](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/39995711582) SUCCESS (including temporary 386 normal/shiny sprite ROM compilation). This does NOT establish MyBoy runtime acceptance, a distributable ROM or safe merging of the divergent follower branch into master.
- Previous current rarity checkpoint and design inventory remain below as historical evidence. **NEXT:** small read-only feasibility/economy audit of proposed Meowth -> Shellder in UndergroundPath North Entrance. Do not implement other proposed pairs without complete decision; continue Drowzee -> Staryu, Doduo -> Lickitung, Raichu -> Magmar, Venonat -> Electabuzz, Koffing -> Seel individually. EV numbers-only/nature coloring, leader rematch dialogue and separate B10 follower runtime/integration remain scheduled.


---

## CURRENT CHECKPOINT — 2026-10-23: approved rarity and Safari access

This current operational checkpoint supersedes any earlier **proposal-only** status of the 1% Kanto wild finals or 5% Safari Dragonair below; the earlier notes remain dated historical evidence. Do not claim MyBoy success, follower integration or master gameplay integration from source-only changes.

- On isolated, already-diverged `prototype/follower-runtime` branch, first dedicated technical microblock **`8ac55d1dcbaa2be1c0430e1962fc7dcf823661e3`** changed exactly `src/data/wild_encounters.json`, the approved encounter-rate checks in `.github/workflows/full-gameplay-core.yml`, and the audited wild JSON blob SHA in `tools/validate_audited_data_blobs.py`. Mt Ember Charizard **1%**, Seafoam B1F Blastoise **1%**, Berry Forest Venusaur **1%**; corresponding Charmander/Squirtle/Bulbasaur **15%**, Charmeleon/Wartortle/Ivysaur **5%**. Original evolved-mon levels retained. Land 4%/1% slot swaps necessarily raise local Rapidash/Golduck/Venomoth to **4%**, without increasing Magmar/Electabuzz or other encounter species. Static semantic checks and file diff reviewed. **Exact Full Gameplay Core run [39990435833](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/39990435833) SUCCESS**, including reproducible Spanish ROM and encounter/blob validators. Follower Prototype run [39990436325](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/39990436325) still IN PROGRESS when last checked; this encounter block's required gameplay CI is green on exact source commit, but do not claim B10 follower CI from that.
- Second single-intention encounter microblock **`28ce8af3f07e4692fb1204f77453b1f96f1498a3`** keeps Super Rod Safari Dratini **15%** and increases Dragonair **1% -> 5%** identically at Center/East/North/West, leaving 40% Goldeen and 40% Seaking. Converts only prior 4% Super Rod Psyduck entries to Dragonair with original Dragonair level interval 25–35; Psyduck remains obtainable elsewhere. Updated exact validator assertions for four areas and same wild blob SHA. Static checks and narrow diff reviewed. **Exact Full Gameplay Core [39991224754](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/39991224754) and Follower Prototype [39991224769](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/39991224769) IN PROGRESS at checkpoint**; determine final outcomes before declaring CI-GREEN for this second technical commit. An intervening docs-only decision entry `b2e3567` does not alter ROM or reset its technical validation.
- Safari runtime source `src/safari_zone.c` confirms **30 Safari Balls, no step expiry**, voluntary exit preserved. Source `src/data/pokemon/species_info.h` confirms base catch rate/flee score **Chansey 30 / 125**, **Kangaskhan/Tauros/Scyther/Pinsir/Dragonair 45 / 125**, **Dratini 45 / 100**. Initial no-bait/no-rock Safari Ball gives approximately **3% for Chansey and 5% for rate-45 species** at full HP; Safari Pokémon can flee, so a 15% appearance chance is not a 15% catch chance. Rarity audit recommendation accepted: keep special Safari land 15% rates, no blanket rate reduction. This does not constitute MyBoy runtime QA.
- Wild Magmar remains **5% at Mt Ember** (natural encounter normally follows Blaine/Sevii travel), Electabuzz **5% at Power Plant** (can generally be accessed with Surf before the Cinnabar lab). Optional Cinnabar Raichu -> Magmar might bring Magmar forward but requires a Thunder Stone evolution as trade cost; Venonat -> Electabuzz would usually be later than Electabuzz's natural habitat, with lower input cost. Both NPC pair choices remain DESIGN CANDIDATES and should be balanced in their separate trade microblock; no NPC trade code edited.
- User favored **Clefairy -> Jynx** at existing Cerulean NPC as the definitive direction, but source change is **not yet implemented** and requires an isolated `src/data/ingame_trades.h` + map-text/flag semantic audit. The other suggested trade pairs were received positively but are **not final exact approvals**. Explicit user decisions are recorded in `DECISION_AMENDMENTS.md` (date-keyed entry due prior A-007 reference ambiguity).
- No new persistent species/items, SaveBlock, BoxPokemon, trainer roster, NPC trade data, Safari mechanics, graphic asset or follower ABI was touched. B10 follower remains OPEN; prototype and `master` remain separate until deliberate integration and MyBoy QA.

**NEXT:** (1) verify final exact technical CI of `28ce8af`, investigate only concrete failures; (2) source-audit approved Cerulean Clefairy -> Jynx implementation using the existing NPC flag/OT/nickname/Spanish dynamic text and check acquisition stage plus gain from traded EXP; (3) audit remaining proposed NPC trade pairs in small bounded review, then seek only genuinely consequential decisions; (4) address EV numbers-only/nature colors and leader rematch dialogue in separate source-safe blocks; (5) resume B10 scene-aware follower and independent 386 MyBoy/release/provenance gates without confusing successful compilation with runtime acceptance. Avoid additional files; update this and NEXT_SESSION at every closed microblock.

---

# Pokémon Rojo Fuego Full v1.0 — Project Continuity




## CURRENT ACTIVE ROADMAP (2026-10-22)

This is the operative source-of-truth snapshot. Historical dated entries below remain evidence, but do not define competing active task queues. Recheck GitHub branch, HEAD, CI and amendments at each session. NO GAMEPLAY MODIFIED BY THIS AUDIT.

**Repository state:** prototype/follower-runtime HEAD 617367ea3457969ccde70e1b748e45a8e0b3881c at audit; master 8d89f2b444a6e25ef47716861a53f2e4f6920d07 separate/diverged. Last technical SHA fdf710c116d4bb6a347f7a81caf3cb62b2b22996: exact Full Gameplay Core run 39851490790 SUCCESS and Follower Prototype run 39851490652 SUCCESS. Last docs-only 617367e: Full Core run 39851709696 IN PROGRESS, Follower run 39851709892 SUCCESS when inspected. B10 follower OPEN; no merge, no MyBoy final QA. Do not treat a passing older SHA as CI proof for a new technical HEAD.

### Rarity policy and cross-map evidence

Current branch compared directly with tag baseline-spanish-vanilla, using FireRed land/water/rock encounter tables: 24 changed maps, 91 species/map/method percentage differences (including newly changed Route1/Route22/Route3/MtMoon). Fishing and all reward/gift methods still require separate contextual review; changed means changed from baseline, not necessarily broken.

- **Starter families (actual wild odds):** Charmander/Charmeleon/Charizard at Mt Ember 15%/5%/4%; Squirtle/Wartortle/Blastoise at Seafoam B1F 15%/5%/4%; Bulbasaur/Ivysaur/Venusaur at Berry Forest 15%/5%/4%. The user wants directly caught final evolutions to feel **exceptionally rare** because their basic forms can be evolved. Candidate: final Charizard/Blastoise/Venusaur 1% each, preserving basics at 15% and middle stages at 5%. This exact numeric candidate is NOT YET APPROVED NOR IMPLEMENTED.
- Eevee on Route7 is 15%; Vaporeon/Jolteon/Flareon each 4% in their special habitats. Review stone-evolution availability and whether final forms merit rarer direct encounters. Do not automatically apply the 1% rule to every species or final.
- LeafGreen-type inclusions checked: Bellsprout Route5 25%, Sandshrew and Vulpix Route8 20% each, Slowpoke Route6 surfing 100%; Safari Pinsir/Scyther, Chansey, Kangaskhan and Tauros in designated sites 15%. Basic/unique species should remain reasonably obtainable. All were consciously incorporated by earlier approved encounter constraints; modifications require own justification and semantic validator updates.
- Rare encounters examined across FireRed land/surf/rock/fishing methods: 49 individual map+method+species results at exactly 1%, representing only 14 species; most have an easier alternative via another map, evolution or gift. Do not globally raise them. Route3 Nidoran female 14% and male 11%, and MtMoon 1F/B2F Clefairy 10%, were separately IMPLEMENTED in fdf710c with exact CI success. Route1 Speed-only 35% Pidgey / 35% Rattata / 30% Spearow and Route22 Attack-only 55% Mankey / 45% Nidoran male also implemented and validated on preceding 0a3d026.
- Viridian Forest southeast clearing near **non-trainer boy at (45,58)** is user-selected for Oddish-only (+1 SpAttack). NOT IMPLEMENTED. Bellsprout gives +1 Attack and must not be included. Wild headers are per map, so a safe bounded encounter patch needs grass metatile/collision/item/warp/follower audit or a separately connected micro-map. Preserve remainder of Forest unchanged and check early Oddish effect on Brock.

**Working rarity principle (proposed):** early basic species obtainable; evolved alternatives uncommon; final stages directly catchable at genuinely special odds only when their basic evolution path is already accessible. Balance species-wide encounter access, route ecology, version identity, percent arithmetic, capture chance, gifts and trades. Actual numeric changes remain separate technical microblocks; preserve audited data blob hashes and frozen 21-map invariants.

### Nine NPC trades: player-value audit / design direction

Actual FireRed source trade roster in src/data/ingame_trades.h:
1. Abra to Mr. Mime — candidate retain.
2. Poliwhirl to Jynx — user wants Jynx **earlier**; audit NPC location, acquisition timing and whether a less burdensome species request is better. No selected substitute yet.
3. Nidoran male to Nidoran female — USER WANTS REPLACEMENT (female now 14% Route3); new request/reward pair not decided.
4. Spearow to Farfetch'd (held Stick) — candidate retain, Spearow now normally found Route1.
5. Nidorino to Nidorina — USER WANTS REPLACEMENT; new request/reward not decided.
6. Golduck to Lickitung — assess late acquisition and trade value.
7. Raichu to Electrode — user finds Electrode reward poor; evaluate an improved trade, not yet selected.
8. Venonat to Tangela (held Stardust) — user finds Tangela reward poor; evaluate an improved trade, not yet selected.
9. Ponyta to Seel — user finds this plausible; check actual site and stage.

All nine preserve a source-defined fixed personality/OT/nickname/IV/item. Before editing verify script placement, NPC timing and dialogue, reward rarity and usefulness, party/box and link safety, species availability and required trade evolution. NPC trades are distinct from link exchange. No replacements are approved by exact pair and none has been changed.

### Phase 0 source follow-up — 2026-10-23 (DOCUMENTATION ONLY; gameplay unchanged)

Audit reference: branch `prototype/follower-runtime` pre-note HEAD `9cb858afc2bd179a1b89ce96080d667f6f30086a` (master remained `8d89f2b4`, NOT merged). Both exact-head workflows finished SUCCESS: Full Gameplay Core [39854853814](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/39854853814), Follower Prototype [39854853769](https://github.com/joseiturriaga25amz/pokefirered-europe/actions/runs/39854853769). This does **not** mean MyBoy acceptance, ROM delivery, integration, or B10 closure.

**Encounter table verified in source**, `src/data/wild_encounters.json` against `baseline-spanish-vanilla`:
- Mt Ember Exterior: Charmander 15% (level 30/32), Charmeleon 5% (36), Charizard 4% (40); Seafoam B1F: Squirtle 15% (26/28), Wartortle 5% (28), Blastoise 4% (36); Berry Forest: Bulbasaur 15% (30/35), Ivysaur 5% (31), Venusaur 4% (37). User's exceptional-direct-final concept supports *proposing* 1% for the three final evolutions only, not changing source now. Land table slots are 20/20/10/10/10/10/5/5/4/4/1/1: moving any final 4%-slot to 1% necessarily reassigns an existing slot (Mt Ember Rapidash/Magmar, Seafoam Golduck/Golbat, Berry Forest Venomoth/Hypno). Require an explicit ecology-neutral slot redistribution and semantic validator before approval/implementation; do not silently increase another rare's probability.
- **Suggested 1%-final slot swaps (PROPOSED, unapproved):** Mt Ember exchange Charizard's 4%-slot with Rapidash's 1%-slot (Charizard 1%, Rapidash 4%); Seafoam B1F exchange Blastoise 4% with Golduck 1% (Blastoise 1%, Golduck 4%); Berry Forest exchange Venusaur 4% with Venomoth 1% (Venusaur 1%, Venomoth 4%). All three preserve exactly 100% table weight, the other species' odds and starter 15/5 basics/intermediates. Audit encounter ecology, resulting evolved-species visibility, script/roster validation and post-approval blob hashes before choosing this over another 1%-slot alternative. No data altered by this note.
- Eevee Route7 15%; Vaporeon Seafoam B1F 4%; Jolteon Power Plant 4%; Flareon Mansion 1F 4%. Default preliminary advice: keep 4% pending review of stone evolution and natural availability, no blanket final-stage rule.
- FireRed Safari comparison, same specific land areas: Chansey North 4% -> Full 15%, Kangaskhan East 4% -> 15%, Tauros West 4% -> 15%, Scyther Center 4% -> 15%; Pinsir Center absent in original FireRed -> Full 15%. These deserve a Safari catch/flee/steps/economy study before selecting 5/10/15%, not an automatic nerf. Dratini Super Rod Safari 15% and Dragonair 1% remain unchanged in those fishing slots. Clefairy Mt Moon 1F 1% -> 10%; Mt Moon B2F 6% -> 10%. These increases were part of earlier encounter work; reopening is review, not revocation.
- Other verified additions: Bellsprout Route5 25%, Sandshrew and Vulpix Route8 20% each, Magmar Mt Ember 5%, Electabuzz Power Plant 5%, Wild Eevee Route7 15%. The rarity policy should preserve basic-form usability and validate total player access via evolution/gift/trades, not simply count an isolated 1% slot.

**Nine source NPC trade sites verified** against `src/data/ingame_trades.h` and the actual `data/maps/*/scripts.inc`:
1. `Route2_House`: Abra -> Mr Mime (retain candidate; arrival through Route2 access still contextual).
2. `CeruleanCity_House3`: Poliwhirl -> Jynx. NPC is early, but Poliwhirl acquisition is fishing/evolution-gated; Old Rod fish in relevant Route25/6 slots is Magikarp only, so NPC location alone does not make Jynx early.
3. `UndergroundPath_NorthEntrance`: Nidoran M -> Nidoran F (must replace according to user).
4. `VermilionCity_House2`: Spearow -> Farfetch'd with Stick (retain candidate).
5. `Route11_EastEntrance_2F`: Nidorino -> Nidorina (must replace).
6. `Route18_EastEntrance_2F`: Golduck -> Lickitung (Golduck acquisition is unnecessarily late for unique Lickitung; review request).
7. `CinnabarIsland_PokemonLab_Lounge`: Raichu -> Electrode (user rejects reward).
8. `CinnabarIsland_PokemonLab_Lounge`: Venonat -> Tangela (user rejects reward); note this NPC script invokes lower-level `CreateInGameTradePokemon` and `DoInGameTradeScene`, unlike most other trades, requiring dedicated script-equivalence audit.
9. `CinnabarIsland_PokemonLab_ExperimentRoom`: Ponyta -> Seel. Ponyta wild at Mt Ember/Kindle Road, ordinarily accessible during the Sevii detour after Blaine; Seel is wild already in Seafoam. Candidate is to keep Seel but request a species reachable before/around Cinnabar instead.

**Concrete candidate pairs for design discussion ONLY — NONE APPROVED OR IMPLEMENTED:**
- Cerulean: Clefairy -> Jynx (10% Mt Moon Clefairy, available before Cerulean) instead of Poliwhirl; alternate easier Meowth/another early species, but weigh Jynx's early Ice/Psychic power and boosted traded EXP.
- Underground North: Meowth -> Shellder instead of the Nidoran swap (Meowth Route5; Shellder otherwise later fishing).
- Route11 gate: Drowzee -> Staryu instead of Nidorino/Nidorina (Drowzee Route11; Staryu Vermilion by later rod). Check if Staryu/Starmie pre-Celadon progression is too advantageous.
- Route18 gate: Doduo -> Lickitung instead of Golduck (Doduo on Routes16–18; Lickitung not wild in current source).
- Cinnabar lounge: Raichu -> Magmar instead of Electrode (trade cost/high-value rare; consider whether devalues Mt Ember 5% Magmar); Venonat -> Electabuzz instead of Tangela (Power Plant 5%; consider whether trade reward is too generous). These pair choices are not committed design.
- Cinnabar lab: Koffing -> Seel instead of Ponyta (Koffing abundant in Mansion, avoids post-Blaine Ponyta prerequisite). Alternative retain existing pair after progression study.
- Keep Abra -> Mr Mime and Spearow -> Farfetch'd candidates unchanged.

**Pre-implementation trade safety gate:** no new species IDs or save/BoxPokemon/link layout; preserve each trade's existing one-time completion flag/slot for old save compatibility; review dynamic generic dialogue *and* hard-coded NPC text, Spanish names/nicknames/OT/item/mail, requested-species accessibility, traded-mon level and learnset, pre-National Kanto eligibility, trade cancellation/full party, player value, and scripts/warps before editing. Do not rename old flags merely for aesthetics. Separate encounter odds from trade changes and from Viridian Forest Oddish map work.

**Cross-block idea feasibility status:** the current matrix below is an inventory, not proof of completion. Prior proposals requiring independent source-level assessment include (LOW-MED) EV summary bars removal/nature colors, leader rematch dialogue; (MED) 252-useful-EV battle milestone and displayed enemy EV yield; (MED-HIGH) battle move-type/STAB/category/contact information, repeated medicine, Dex route completion, six-EV training hub, journals/registry; (HIGH) Hold-R ball selector, START PC access, postcapture inspection and universal scene-aware follower/386 normal-shiny runtime. Audit data flow, battle callbacks, field-task controls, UI screen geometry, flags, player accessibility, save/link safety and tests before allocating microblocks. Existing user preferences are not universal implementation approval. Final MyBoy and private ROM delivery remain separate release blockers.

### Remaining feature feasibility inventory and gates

| Feature | Real status | Main risk and next evidence |
| --- | --- | --- |
| Follower 386 sprites normal/shiny, interactions, Gary scenes, all Gym/League/story contexts, save/bike/Surf/link | B10 PARTIAL; diagnostic builder compiles privately, removes ROM afterward; MyBoy incomplete, no master merge | HIGH graphics/OAM/script runtime. Gary's own separate visible follower unverified; A-007 citation contradicts current formal A-001..A-006. |
| Eight leader-specific rematch conversations | A-005 APPROVED, all eight still share four generic scripts | LOW-MED script/Spanish/QA. Keep all already-approved boss parties unchanged. |
| Koichi Dojo fix | source implemented and validated statically | MyBoy regression still pending. |
| EV summary numbers, no bars; blue boosted / red reduced nature | six numeric EV values and total exist, bars persist; nature colors not built, 252 useful vs actual 255/stat cap label wrong | LOW-MED summary/palette/screen QA; no EV game rule change. |
| 252-useful-EV-only notice after battle | preferred, not implemented, never 100/200 | MED gain recipient/threshold aggregation and battle callback. |
| Live enemy EV yield; move contact, category, STAB, type/resistance; healthbox type icons | data exist, display not implemented | MED-HIGH battle UI layout, dual types, special type changes and move immunity/abilities. |
| Hold-R wild-only ball quick select with left/right/release | NOT IMPLEMENTED | HIGH battle input/catch/cancel; MyBoy touch and Safari/link safe. |
| PC from START, postcatch nature/ability/moves inspection | requested, NOT IMPLEMENTED | HIGH storage/capture/save/script state restrictions. |
| Dex route completion, postgame journal, boss registry | user-preferred, NOT IMPLEMENTED | MED-HIGH discovery/spoiler/flags and storage budget. |
| Repeated medicine use; postgame six-EV-specialist trainer row | user-preferred, not verified implemented | MED-HIGH inventory or map/XP/money/economy/battle data. |
| Legendary narrative, special Balls, EV/Dex polish, follower friendships, early game/Gary/Liga/Dojo, MyBoy | A-005/A-006 and historical freeze, MIXED partial and tests | Must reconcile source against approved decisions and complete all critical regressions before candidate. Guaranteed shiny Charmander is explicitly REVOKED. |

### Controlled project work order (one active stream, no monolithic changes)

**PHASE 0 (ACTIVE):** finish full rarity + acquire-by-evolution/trade/gift audit (not blanket odds); map all nine NPC trade scripts and availability, propose exact replacement pairs; technical feasibility/priority of all user-endorsed QoL above. No additional feature source edits in this phase. Treat previous chronology as historical, not instructions to resume outdated early-NPC trainers or 100/200 EV alerts.

**PHASE 1:** after any material design approvals, separate controlled microblocks for (a) optional final-stage encounter odds, (b) NPC trade rewards/request/dialogue, (c) Oddish-only southeast Forest patch. Distinct commits and exact validator + hash-lock + full game CI, audit after implementation. Do not mix them.

**PHASE 2:** highest-value approved UI and quality improvements first: EV numbers-only and nature colors, leader-specific rematch dialogs, EV yield battle info, 252 milestone, then risky control/storage/capture/PC work only after reviewed callback/state design; schedule postgame EV hub, journals, history and medicines independently. Features proposed but not prioritized for this release must stay visible rather than silently becoming blockers or silently removed.

**PHASE 3:** finish B10 follower, Gary's own companion design traceability, story-script/Gym/League/Dojo and legendary/roster integration audit, preserve original saves and link ABI. MyBoy QA is a separate layer.

**PHASE 4:** deliberate integration of diverged branch with master, exact technical + integrated HEAD CI, safe asset/license provenance and verified MyBoy patch/ROM delivery followed by full acceptance. Never declare release only on workflow green.

Continuity ownership: THIS file is global current state + decision/feasibility evidence; NEXT_SESSION.md contains **only** next action and checkpoint; DECISION_AMENDMENTS.md has approved postfreeze architectural/design overrides; RC_MYBOY_CHECKLIST.md is runtime testing; frozen docs/spec/ never overrule amendments. Referenced REPOSITORY_GUARDRAILS.md and POLISH_IMPLEMENTATION_MATRIX.md do not exist in this branch; do NOT recreate duplicate documents without need.

---

**Purpose:** make the repository sufficient to resume the project without relying on any previous chat.

## 1. Start here in every new session

Before modifying code:

1. Read this file.
2. Read `docs/production/DECISION_AMENDMENTS.md`.
3. Read `docs/production/RC_AUDIT_LOG.md`.
4. Read `docs/production/FINAL_AUDIT_PLAN.md`.
5. Read `docs/production/RC_MYBOY_CHECKLIST.md`.
6. Read `docs/production/SECOND_PASS_AUDIT.md`.
7. Inspect the current branch HEAD and latest GitHub Actions result.
8. Only if a design detail is still needed, consult the frozen sources under `docs/spec/`.

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

## 4. Repository / branch / baseline

- Repository: `joseiturriaga25amz/pokefirered-europe`.
- Active production branch: `feature/full-gameplay-core`.
- Frozen vanilla tag: `baseline-spanish-vanilla`.
- Baseline commit: `e184c5cf898cd29efebd33bc1bfe5994277e21ab`.
- Production target: `firered_es_modern`.
- Baseline Spanish SHA-1: `ab8f6bfe0ccdaf41188cd015c8c74c314d02296a`.

## 5. Current technical state at continuity freeze

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
- all nine Altering Cave tables/selector values;
- Porygon 5,000-coin price.

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

## 9. What remains before v1.0 final

The project is no longer in a broad implementation phase. Remaining work is primarily **Release Candidate audit and runtime acceptance**:

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

The correct first action is to inspect this repository and continue from the RC audit. Do not ask the user to reconstruct old chat history and do not assume a stale commit from a previous conversation is still HEAD.


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


### B10 checkpoint after Route 22 early MID (2026-10-22)

The follower prototype remains on `prototype/follower-runtime`, **not on `master`**. The exact previous head `e728c4f` passed Full Gameplay Core run `39822343019` and Follower Prototype run `39822343251`. New technical commit `6df73cb` extends Route 22 early scripted Gary visibility to the MID trigger using a tested seven-tile path restriction; its exact CI must be verified before claiming CI-GREEN. Read the latest dated entry in `NEXT_SESSION.md` and the MyBoy checklist before any further work. The 386-species private ROM builder passes automated checks but deletes the ROM and is not a public downloadable MyBoy artifact. MyBoy visual QA, remaining scripted Gary encounters, integrated master CI and a legitimate deliverable format still require work.



## 2026-10-22 — Cross-block pre-candidate audit (requested before another near-final test ROM)

**Scope:** repository-wide release-readiness triage, not a gameplay change or final audit PASS. At inspection HEAD `313940a4def7cb171bd358d43203de84821cdb82` on `prototype/follower-runtime`, master `8d89f2b444a6e25ef47716861a53f2e4f6920d07`, separate production branch `feature/full-gameplay-core` at `5205ad95b98c4815b7ddcfff4f8ad533b5a04183`. GitHub comparison `master...prototype/follower-runtime`: DIVERGED (150 ahead, 736 behind), with 29 differing files in the comparison; assess merge base and master advances before integration, do not assume a clean fast-forward.

**Do not equate completion of B10 with completion of Full.** Distinguish a disposable private 386-normal/shiny follower diagnostic from a near-final integrated MyBoy candidate. Preserve approved systems, avoid unnecessary gameplay rewrites, and require evidence for each gate.

| Area | Evidence on repository | Assessment for near-final candidate |
| --- | --- | --- |
| Bosses, all 8 Gym leaders, Elite Four, League and Gary team progression | `src/data/trainer_parties.h`, `tools/validate_full_league_rosters.py`, `tools/validate_full_trainer_sets.py` and consolidated Full Gameplay Core CI; current compiled examples include Brock and Champion | IMPLEMENTED and automatically checked, but fresh integrated-head runtime balance/items/AI and full MyBoy acceptance still required; do not reopen approved rosters without evidence of mismatch |
| Second Fighting Dojo and Koichi freeze | Spanish `data/maps/SaffronCity_Dojo/scripts.inc` has `trainerbattle_single` first for sight trigger, post-Sabrina second trial, opposite Hitmon reward and no-room retry; `RC_AUDIT_LOG.md` RC-F041 and event validators | Source fix exists; **MyBoy regression retest still pending** on new candidate |
| Follower for player (general systems) | `src/full_follower.c`, existing run gates, MyBoy exploratory findings in `RC_MYBOY_CHECKLIST.md`; follows player in normal field, but scripted/Gym/League/menu/battle transitions need category-by-category QA | B10 is open. Gary is a special script subset, not exclusive scope; test all leader, Elite Four, NPC, boss, wild, healing, bike/Fly/Surf, save/load, link, OAM/graphics contexts |
| Gary's **own** Squirtle/Wartortle/Blastoise overworld companion | Historical checklist calls it a proposed staged visual and mentions `A-007`, but `DECISION_AMENDMENTS.md` contains only A-001..A-006. `full_follower.c` provides the PLAYER follower and cutscene allowance, not demonstrated independent Gary-NPC companion implementation | **DECISION TRACEABILITY CONFLICT / NOT VERIFIED IMPLEMENTED.** Reconcile actual approval, stage/lifecycle/graphics and dynamic scenes before adding it; do not confuse it with Gary's fixed battle roster |
| Remote Pokémon PC on START menu | `src/start_menu.c` has Pokédex/Pokémon/Bag/Player/Save/Option/Exit etc; no PC entry. No explicit approved PC-from-Start requirement found in current amendments or historical specification inspected | **USER PROPOSAL / NOT IMPLEMENTED.** Define availability (field only, no battle/Safari/link), storage vs item PC scope and safeguards, then seek design decision rather than silently committing a new global feature |
| Legends V2, Mew presentation, rematch leader-specific dialogue, specialty Balls, Pokédex usefulness, postgame training, EV/menu polish and other QoL | A-005/A-006 approved scope and old RC findings in `PROJECT_CONTINUITY.md`; frozen reconciliation pre-dates some polish | **MIXED / NOT FULLY RECONCILED.** Concrete confirmed gap: all eight Gym rematches still share literally identical offer/intro/defeat/after lines in compiled Spanish `data/maps/{PewterCity,CeruleanCity,VermilionCity,CeladonCity,FuchsiaCity,SaffronCity,CinnabarIsland,ViridianCity}_Gym/scripts.inc`, contrary to approved A-005; implement leader-specific text in a scoped later microblock without modifying teams. Continue auditing shops, legendary quests, UI and postgame features; no blanket PASS or blanket NOT IMPLEMENTED without code proof |
| Final integration and packaging | Follower and master are distinct; Full Gameplay Core and Follower Prototype CI on exact predecessor `e728c4f` passed; later Route 22 MID `6df73cb` exact workflows pending during review. Private 386 sprite diagnostic builds and deletes ROM; redistribution and MyBoy delivery constraints remain | Require exact technical CI, adversarial audit, controlled branch integration, integrated HEAD validation, reproducible checksum/private authorized distribution and MyBoy scenario-based acceptance; no final-release claim from build alone |

**Order before a near-final test ROM:** (1) finish current Route 22 MID CI, then reconcile cross-block requirements and approved/unapproved design proposals; (2) group remaining B10 cutscene variants and generic Gym/Elite Four/trainer interaction QA (not just Gary), including 386 sprites/shiny and companion life cycle; (3) audit A-005/A-006 polish, Dojo regression, frozen rosters and other QoL/UI against actual target/master; (4) isolate any required gameplay fixes into small commits with exact Full Gameplay Core/Follower Prototype CI; (5) integrate deliberately and validate the integrated HEAD; (6) produce a legally distributable/authorized MyBoy candidate and test it, with focused Surf fixture and event/save/link checkpoints. PC remote and Gary's own overworld companion are separately tracked design/traceability questions; do not declare them approved simply because discussed.

No fresh MyBoy QA and no source implementation were performed in this audit. No new planning files are needed; this record plus `NEXT_SESSION.md`, `RC_MYBOY_CHECKLIST.md` and existing approved amendments are sufficient for continuity.


## 2026-10-22 — User-intent review: EV UI, natures, conservative inspirations (NO GAMEPLAY EDIT)

This is a cross-block PROPOSAL / DESIGN-AUDIT checkpoint, **not new approved game functionality**. The existing A-005/A-006 decisions and explicit supersessions remain authoritative. Do not infer blanket implementation from CI-GREEN or reintroduce revoked features.

- **Explicitly rescinded:** the proposal to force Oak's Charmander shiny was withdrawn on 2026-10-19; keep ordinary Gen III personality/shiny generation for all three starters. Do not add any forced shiny, shiny-only palette override or special guaranteed odds. `RC_MYBOY_CHECKLIST.md` already preserves the dated withdrawal.
- **Confirmed EV summary gap / user preference:** `src/pokemon_summary_screen.c` already toggles the Skills page with SELECT to display the six actual EV values and total (calculated from party Pokémon, no saved UI copy). However `PrintFullEvValue` still draws a 28-pixel bar per stat via `FillWindowPixelRect`, contrary to the explicitly requested numbers-only, uncluttered presentation. Track a separate UI cleanup to remove bar rendering while retaining values, 6 entries, total and a legible presentation. Do not touch EV gain/party or save data casually.
- **EV cap discrepancy to audit:** the summary prints `MAX. STAT 252 / TOTAL 510`, but `include/constants/pokemon.h` sets `MAX_PER_STAT_EVS 255` and `MAX_TOTAL_EVS 510`, and `src/pokemon.c::MonGainEVs` uses that actual 255 cap. 252 is the final multiple of four relevant for stat gain, not the true Gen III storage/acquisition ceiling. The UI must not mislabel mechanics. Decide whether to display '252 útiles / 255 máximo Gen III', or explicitly approve a behavioral cap change; default is preserve 255/510 and compatibility.
- **New idea / proposed optional feature:** unobtrusive EV milestones at crossing 100, 200 and 252 **effective** EVs in any stat, ideally queued/aggregated after battle or another safe field context, not mid-battle; per-Pokémon/per-stat one-time threshold crossings without new persistent save fields, and no spam after repeated save/load, vitamin/berry/retraining. Must audit actual old/new EV accumulation, party-wide awards, thresholds, trainer/wild battles and space/text before implementing. Not approved; no code change.
- **New idea / proposed visual:** on the Pokémon summary/stats page, subtle upward colored indicator (red) for nature-boosted stat and downward colored indicator (blue) for nature-reduced stat; neutral natures show no markers. Consistent with HGSS style; display only, use existing nature APIs and preserve personality and Gen III calculations. The user described this for a freshly captured Pokémon; opening summary after capture is an appropriate low-friction place, without inserting mandatory capture-dialog popups. No current nature-stat coloring found in `src/pokemon_summary_screen.c` during this audit. Needs text palette/layout/accessibility review and MyBoy.
- **Curated external design inspirations (NOT code-import authorization):** Quetzal's lively overworld presentation and follower idles; HGSS colored nature stats; pokeemerald-expansion configurable summary EV/IV views; careful comparison with high-QoL hacks for concise menus/Pokédex/search/feedback. Prefer Gen III compatibility, single dynamic protagonist companion, no forced newer-gen mechanics, no creep in creature roster or balance. Evaluate asset/source licenses and FireRed architecture before borrowing any implementation. Do not automatically add co-op, Megas, Terastalization, randomizers, cheat menus or mass modern mechanics.
- **Scope safeguards:** cross-check unimplemented A-005 leader identity texts, proposed remote PC-from-START, Gary's own staged companion, 386 followers, boss dialogue/League, visual presentation, classic Kanto immersion and the Dojo MyBoy regression. Continue the cross-block inventory before assembling near-final MyBoy candidate. The recorded A-007 reference for Gary is inconsistent with the amendments file ending at A-006; reconcile approval separately. Do not turn suggestions into decisions solely because they appeared in a conversation.

Next action: verify exact post-doc CI status, then run focused UI/data audit for EV display/nature and compare other approved polish items by source; only implement a reviewed microblock under an explicit approved decision.


## 2026-10-22 — Updated EV milestone and nature-color user direction (SUPERSEDES EARLIER PROPOSALS)

**Current expressed user direction (do not reinstate old 100/200 proposals):**
- **EV summary:** numbers for all six actual EV values and total, without the small per-stat bars/graph. The existing SELECT toggle and the actual EV counts remain. Rendering cleanup is still NOT IMPLEMENTED.
- **EV milestone notification:** ONLY the **252 useful EV** milestone per stat, after a battle awards EVs crossing that effective threshold; **no messages at 100 or 200 EV**. Keep this lightweight and nonblocking. Compare pre-/post-award actual stat EV for each awarded party member, and emit a single grouped postbattle notice only when pre < 252 and post >= 252; do not fire on every later battle, unrelated stat, mere menu open, or loading a save. Multiple recipients/stat milestones in one fight need aggregation and display policy before implementation. If an award jumps from 251 to 254 (Gen III allows 255/stat, 510 total), do not claim the raw counter equals exactly 252: message should state 'alcanzó 252 EV útiles' or equivalent while summary still shows the accurate raw value. **Preserve actual Gen III caps 255/510 and normal Pokémon compatibility; 252 is useful/effective milestone, not storage cap.** This is a now-expressed user UI requirement, subject to technical flow/safety review; it is NOT IMPLEMENTED.
- **Nature boost/reduction indicator:** exact USER direction is **BLUE for stat increased** by nature, **RED for stat decreased**, neutral stats unmarked. Earlier red-up/blue-down description is REVOKED. No arrows, +/-10% annotations or large overlays necessary. Prefer recoloring the existing stat name/value text (or a small colored dot if engine layout makes that safer), on the usual summary/stats screen even after catching a Pokémon; no required capture pop-up or modified nature mechanics. Nature table is already stored internally in `src/pokemon.c` as `sNatureStatTable`; it is static to that module. Exposing effect safely via a narrow read-only accessor or equivalent display-only logic would require separate code audit. **NOT IMPLEMENTED**; needs MyBoy UI/palette checks.
- **External-hack brainstorming:** User found the prior suggestions (Quetzal/HGSS/expansion generic comparisons) underwhelming and did not select any as a change. Do **not** treat those items as approved work or repeatedly promote the same ideas. Only surface thoroughly evaluated, material improvements relevant to classic Kanto/FireRed Full if the user later asks. No external code/art import authorized.

This current dated direction supersedes the earlier 100/200/252 and red-up/blue-down discussion in the preceding audit note. It does not alter independent approved decisions (A-001..A-006), nor reinstate the withdrawn forced-shiny Charmander. Existing B10 and near-final ROM gates remain. **This checkpoint changes documentation only.**


## 2026-10-22 — User-endorsed training / battle UX proposals after six Quetzal screenshots

**Status: USER-PREFERRED / DESIGN AND FEASIBILITY GATE PENDING.** User selected or positively endorsed functionality during UX planning; this is not proof of implementation, CI, or a universal instruction to ship every idea in the imminent near-final RC. No gameplay or UI source was changed. A separate, scoped technical plan is needed for battle input, battle UI, EV trainer map objects, save state and test fixtures. Do not treat source photos as distributable art.

**Player-preferred scope, preserving what was actually said:**

1. **View native EV yield for the current opposing Pokémon while in battle**, not only in its Pokédex entry. Base species EV yield, accurately expressed per stat (e.g. `At. Esp. +1`); distinguish from the actual gain when Pokérus, Macho Brace, Exp Share, recipient roster and total EV caps apply. The Pokédex must also expose yield when appropriately discovered. Avoid extra intrusive screens and do not expose unseen species before discovery.
2. **Optional inspection immediately after capture** of that Pokémon's nature, ability and moves (with the new BLUE boosts/RED drops nature styling), without forced PC travel. Must preserve capture, nickname, party full → storage destination, egg and storage/transfer callbacks; offer skip/cancel.
3. **Pokédex route-by-route completeness**: counts known/captured species by accessible area, do not leak never-seen rare/legendary/plot species; distinguish multiple encounter methods, day/rod/Safari/Altering Cave states when relevant.
4. **Repeatable training trainers in the story and a six-category postgame hub**. Early: Attack and Sp. Attack trainer options around Viridian City / Route 22 for starter training; Route 1 already provides Speed, no need to supplant it. Postgame: six visible NPCs in a row, one per HP, Attack, Defense, Sp. Attack, Sp. Defense, Speed, each providing easy rematches against up to six Pokémon that **all yield EVs only in that assigned stat**, preferably 2–3 yield when canon evolved species are appropriate; no item-based instant grant, no global EV-yield rewrite. Source examples `NIDORAN_M` +1 Attack, `ODDISH` +1 Sp. Attack, `MACHAMP` +3 Attack, `ALAKAZAM` +3 Sp. Attack (checked in compiled species-info). Requires levels/money/XP/replay balance so first-gym challenge isn't trivialized, adequate battle variety, consistent economy and story gate. Specify exact teams, amounts, rematch access and location before implementation.
5. **Postgame objective journal**, tracking real optional goals/quest states without enforcing a linear checklist, revealing future legendary unlocks or changing save structures without audit.
6. **Batch/repeated medicine use** in Bag/party screens, faster healing without skipping actual per-use inventory/HP/PP/status checks.
7. **Major battle registry**, e.g. defeated Gym/Elite Four / Gary encounters and unlocked rematches, reusing existing defeated trainer/flag data when possible rather than duplicating persistent records.
8. **R Poké Ball shortcut in WILD battles** as demonstrated in Quetzal screenshots: a quick-use ball popup at battle action menu; while R is held, left/right cycles through owned ball types, releasing R attempts to throw selected ball, with visible ball type and count; permit safe cancel (e.g. B) before release. Evaluate tap R vs hold separation and reliable held/released transition in MyBoy touch controls; do not consume a ball on accidental input/no item. **Never** enable trainer-battle capture, link battles or incompatible Safari/double/forced/scripted modes. Use normal bag/catch checks and callbacks, with no duplicated bag logic.
9. **Battle healthbox type icon(s)** for both currently visible Pokémon (dual types should not be suppressed or misrepresented; enough GBA VRAM/OAM/layout budget must be measured).
10. **Battle move selection information**: physical/special/status glyph; contact/non-contact information; small '+' if using the move's actual type gains STAB; text color **GREEN for type-super-effective, RED for resisted**, neutral regular, immunity clearly distinct. The user screenshots show these in-context, not an info encyclopedia popup. Read move `gBattleMoves[]` `.type`, `.category`, `.flags & FLAG_MAKES_CONTACT`, Pokémon types and native `gTypeEffectiveness`, not a custom contradictory chart. Handle dual typing / true zero multipliers, status moves, variable types (Hidden Power, Weather Ball etc), target-switch/doubles and potential ability immunities in design; avoid claiming guaranteed damage/effectiveness when abilities/weather/status alter outcome. Prefer eligibility based on actual visible opponent and current move context. The physical/special **split is already in Full**; this proposal is a UI affordance, not request to change mechanics.

**Priority direction:** battle EV yield + readable move info / healthbox type + R shortcut and postcapture details are moment-to-moment QoL; early Attack/Sp. Attack mentors and six-stat postgame training hub plus catch-per-route summary / objectives / major-battle registry are scoped progression content. This expands the cross-block candidate inventory, but is NOT a reason to abandon current critical follower stability/Dojo/combat-difficulty and fixed-story gates.

**Known implementation facts at checkpoint:** `src/battle_controller_player.c::HandleInputChooseAction` uses A/B/D-pad and has no R shortcut; `src/data/battle_moves.h` stores `type`, `category` and `flags`, incl. `FLAG_MAKES_CONTACT`; `include/battle.h` defines `IS_MOVE_PHYSICAL/SPECIAL/STATUS`; `src/battle_main.c` contains `gTypeEffectiveness`; `src/data/pokemon/species_info.h` stores EV yield. These establish feasibility inputs **not completed UX**. Source of screenshot inspiration is user-uploaded images; do not add their images or external code/assets to the repo. Preserve one protagonist follower, normal Gen III saves/links, Spanish ROM target, existing movesets and user-approved teams.

**Still active existing decisions:** 252-useful-EV **only** postbattle milestone (never 100/200); EV numeric UI without bars, nature BLUE increase/RED decrease; rescinded shiny-guaranteed Charmander. Existing remote PC from START is a recorded user preference in the MyBoy checklist, currently not implemented. Do not overwrite the superseded states.

**Next before any implementation:** (1) prioritize user-valued additions versus near-final ROM timing; (2) separate simple display-only pilots from battle-control/save/map systems; (3) independently audit controller command state and field-script/capture lifecycle, possible OAM/VRAM/text layout conflicts, EV recipient rules and save space; (4) propose narrow design where alternatives materially affect gameplay; (5) implement only authorized microblocks with adversarial review, exact gameplay CI and focused MyBoy QA. Continue broad audit; B10 remains open.


### 2026-10-22 — Early EV training correction: no repeatable NPCs before Brock (DESIGN PENDING)

- This supersedes the earlier tentative plan for repeatable Attack / Sp. Attack trainer NPCs around Viridian/Route22 **before Brock**: there is no usual rebattle mechanism at that stage, and user wants wild training instead. Do not implement early repeatable EV trainer NPCs on the basis of previous discussions. The separate six-stat repeatable trainer hub **postgame** remains a distinct favorable idea.
- Source facts checked on the active follower prototype: `src/data/pokemon/species_info.h` grants `MANKEY` +1 Attack, `SPEAROW` +1 Speed (NOT Attack), `RATTATA` +1 Speed, `PIDGEY` +1 Speed, `NIDORAN_M` +1 Attack and `ODDISH` +1 Sp. Attack. A previous user's assumption that Spearow grants Attack was corrected. Preserve normal Gen III EV logic.
- `src/data/wild_encounters.json` FireRed `MAP_ROUTE1` land encounters are only Pidgey/Rattata (all +1 Speed), **so Route 1 should stay unchanged**. FireRed `MAP_ROUTE22` has 12 encounter slots: 45% Rattata + 45% Mankey + 10% Spearow (using declared slot rates of 20/20/10/10/10/10/5/5/4/4/1/1 percent). No Nidoran♂ currently appears in that Route22 table. The least disruptive high-purity candidate is replacing only the five Rattata slots with Mankey, yielding **90% Mankey (+1 Attack) / 10% Spearow (+1 Speed)** and retaining early Spearow obtainability; **not fully pure** Attack. 100% Attack would require removal/replacement of Spearow with Mankey or another Attack-yielder and has greater Pokédex/biome consequences. These are OPTIONS, not approved modifications.
- User wants a pre-Brock **localized Sp. Attack encounter area**, likely Oddish (native +1 Sp. Attack), without replacing Viridian Forest's original forest species. `src/wild_encounter.c::GetCurrentMapWildMonHeaderId` selects grass encounters by map group/number, not by the exact grass patch; merely placing a patch of grass on Route2 or Viridian Forest does not grant its own species table. Options: a small independently mapped forest clearing (new map/connector/event assets with dedicated 100%-Oddish table), or a tightly bounded position/tile-aware special encounter override with stronger engine audit. A blanket change to all of Viridian Forest or all Route2 is NOT recommended just to get a small Oddish training patch. Adding catchable pre-Brock Oddish also advances availability of a Grass Pokémon and may affect Brock's challenge; evaluate that before approving.
- No gameplay/map/encounter data changed in this checkpoint. **Design decision pending:** preserve early species by favoring Route22 90/10, and compare the safest localized Oddish-area implementation plus its progression impact; obtain user preference for meaningful tradeoffs before technical edit. Maintain exact Full Gameplay Core and Follower Prototype validation for any later data/maps/runtime change.


### 2026-10-22 — Pre-Brock encounter distribution revised by user (decision on female Nidoran pending)

- User's updated concept **SUPERSEDES** prior 90% Mankey / 10% Spearow candidate and previous pre-Brock repeatable trainer proposal: move Spearow from Route22 to Route1, retaining Pidgey and Rattata; Route22 should show Mankey plus male/female Nidoran, with female rare, and post-Brock original Nidoran area should favor females; at a discrete grassy area near the non-battling boy on the **right of the SOUTH entrance** to Viridian Forest, make a dedicated Sp. Attack encounter spot with Oddish; user asks whether Bellsprout can share it.
- **Confirmed actual EV yields in `src/data/pokemon/species_info.h`:** Mankey +1 Attack; Nidoran♂ +1 Attack; Nidoran♀ **+1 HP, not Attack**; Oddish +1 Sp. Attack; Bellsprout **+1 Attack, not Sp. Attack**; Spearow, Pidgey, Rattata +1 Speed. Cannot honestly deliver 'Route22 only Attack' when including Nidoran♀, nor 'Oddish+Bellsprout only Sp. Attack' without modifying canonical yields (NOT recommended). Do not silently change EV yields.
- Current FireRed encounter percentages (source `src/data/wild_encounters.json`, 12 land slots): Route1 Pidgey 50%, Rattata 50%; Route22 Mankey 45%, Rattata 45%, Spearow 10%; Route3 Nidoran♂ 14%, Nidoran♀ 1%. LeafGreen Route3 already reverses those to ♀14% / ♂1%. A feasible, low-impact candidate Route1 45% Pidgey, 45% Rattata, 10% Spearow (reassign two 5%-rate slots); Route22 **OPTION A** 70% Mankey / 25% Nidoran♂ / 5% Nidoran♀ (95% Attack EV encounters and 5% HP), or **OPTION B** ~70% Mankey / 30% Nidoran♂ (100% Attack but no Nidoran♀ before Brock in this map; retain/buff female Route3). User choice between A and B **not yet resolved**. If choosing Route3 female-dominant distribution, retain access to male Nidoran via Route22 and audit FireRed vs LeafGreen identity / catchability.
- Viridian Forest source map has a NON-TRAINER `ViridianForest_EventScript_Boy` at (45,58), near the south-east clearing, while `ViridianForest_EventScript_Youngster` at (29,58) is also non-trainer; item at (49,60). This grounds the user-described right-side space. Existing standard land encounter table is per map, so a localized only-Oddish patch requires either an independently mapped clearing or a safely bounded coordinate/tile-based exception. Preserve other native Forest encounter slots, trainers, paths, warp/QuestLog, save/capture, follower and Pokédex route counts; survey collision/tile geometry before deciding architecture.
- **Proposed forest composition:** Oddish only (100% +1 Sp. Attack). Bellsprout would spoil the pure Sp. Attack zone and can remain in its original later locations; any special early appearance/encounter method requires a separate explicit design choice. This proposal intentionally makes catchable Oddish available before Brock, impacting challenge/obtainability and requiring team/progression audit.
- This is a **recorded user proposal, not a finalized implementation design**. User must resolve genuine Attack-purity vs female-Nidoran-availability tradeoff before modifying encounter tables, plus authorization of the small forest zone. No gameplay, map, encounter data or workflow modified. Technical implementation if approved requires Full Gameplay Core and Follower Prototype exact CI, independent encounter probability/area regression tests, optional targeted MyBoy smoke. Keep postgame six-NPC EV hub distinct.


### 2026-10-22 — Pre-Brock encounter commit and cross-map rarity / NPC trade audit

**Technical implementation:** `0a3d02613a241c0265c2b16b4f57cb5fe136f806` on `prototype/follower-runtime` changes exactly `sRoute1_FireRed` to Pidgey 35% / Rattata 35% / Spearow 30% (+1 Speed all), and `sRoute22_FireRed` to Mankey 55% / Nidoran♂ 45% (+1 Attack all), preserving their low levels, the existing native wild encounter system and all LeafGreen table variants. Technical scope: `src/data/wild_encounters.json`, an explicit semantic check in `.github/workflows/full-gameplay-core.yml`, and the exact audited blob SHA in `tools/validate_audited_data_blobs.py`. No maps, save/link structures, baseline historical 21-map gate or encounter logic changed. This supersedes earlier 90/10 or Nidoran♀ Route22 proposals. Exact technical Full Gameplay Core `39849932055` SUCCESS; Follower Prototype `39849932247` was still IN_PROGRESS during checkpoint. No MyBoy QA; no master integration.

**Audit scope across map encounter methods:** the current FireRed encounter data include land, surfing water, rock smash and Old/Good/Super Rod fishing tables. Computed per-species probabilities using each method's slot weights and each map; **49 distinct map/method/species occurrences at exactly 1% representing 14 species** (10 land, 35 Super Rod, 4 surfing water). This is not 49 globally rare species. Many have more accessible alternate floors, routes or methods and should not all be raised blindly (e.g. Psyduck multiple 1%-rod entries but common elsewhere; Haunter 1% Pokémon Tower 3F, much more common on other floors; Lapras 1% optional Icefall Cave water and a story gift; Dragonair 1% Safari Super Rod but obtainable via Dratini evolution). Most 5% encounters are not automatically defects either. Protect version identity, legal 386 obtainability and original progression.

**Genuinely high-friction early-game candidates found:**
- `sRoute3_FireRed`: current Nidoran♂ 14%, Nidoran♀ 1%. User wants female distinctly discoverable rather than 1%, at least as likely as male after Brock. Candidate **Nidoran♀ 14%, Nidoran♂ 11%**, retaining all original Route3 species by reallocating existing slot #5 (10% Pidgey→♀), #8 (4% male→♀), #10 (1% female→♂): final Spearow 35%, Pidgey 20%, Mankey 10%, Jigglypuff 10%, Nidoran♀ 14%, Nidoran♂ 11%. Avoid changing LeafGreen until separately justified; Route22 now provides plentiful male Nidoran.
- `sMtMoon1F_FireRed`: Clefairy 1%, Paras 5%, Geodude 25%, Zubat 69%. Candidate Clefairy **9%** using two distinct 4%-weight Zubat slots, retaining Paras and Geodude and leaving Zubat 61%; rare but far less frustrating. `sMtMoonB2F_FireRed`: Clefairy 6%; optional modest bump to **10%** by changing a single 4% Zubat slot. Do not automatically modify other odd/evolved/optional 1% species without checking alternative access. Exact final rates and FireRed scope are suggestions grounded in slot arithmetic, not yet implemented or approved as a frozen specification.
- The Forest `MAP_VIRIDIAN_FOREST` non-battling boy at (45,58), near the southeast SOUTH entry, is the user's preferred Oddish-only Sp. Attack patch. Native encounter table is whole-map; the original forest must remain unchanged outside the selected area. Any scoped tile/coordinate patch requires examining the map binary and tile grass/collision behavior, full trainer/item/warp/field follower route. Alternatively tiny own-map clearing has extra map/warps. **Not implemented yet**; Oddish +1 Sp. Attack, Bellsprout +1 Attack and unsuitable. Natural pre-Brock Oddish availability must be deliberately reviewed versus Brock challenge.
  
**NPC trade audit of current FireRed `src/data/ingame_trades.h` (9 entries, no modifications):** Abra→Mr. Mime, Poliwhirl→Jynx, Nidoran♂→Nidoran♀, Spearow→Farfetch'd (Stick held), Nidorino→Nidorina, Golduck→Lickitung, Raichu→Electrode, Venonat→Tangela (Stardust held), Ponyta→Seel. Other rewards retain fixed personality, imperfect IV spreads, OTs, nicknames and item/mail metadata. Stage-by-stage assess how readily each requested Pokémon can be obtained, whether reward gives meaningful Pokédex/evolution/battle utility rather than asking for a harder-to-get or evolved mon, whether dialogue accurately previews the exchange, and the effect of our early Spearow and Nidoran♂ accessibility; e.g. Raichu→Electrode and Nidorino→Nidorina are candidates for scrutiny, not proven defects. Do NOT replace all trades or change trade code, personality/OT generation, national access or link ABI without explicit design reconciliation. Ingame NPC trades are distinct from live link trades.

**Next microblock:** verify exact Follower Prototype CI `39849932247`; then independently implement the narrow Route3/Mt Moon rarity correction if accepted after scope review, or audit Forest binary grass-area feasibility. Stage NPC-trade-by-NPC improvement proposal after validating where NPCs are located and when species become obtainable. Persist in existing docs; do not start a monolithic world encounter rewrite.


### 2026-10-22 — Corrected FireRed Route 3 and Mt Moon rare encounters (follow-up microblock)

- Completed separately from the earlier Route1/Route22 EV-pure microblock. Technical commit `fdf710c116d4bb6a347f7a81caf3cb62b2b22996` changes only the FireRed `sRoute3_FireRed`, `sMtMoon1F_FireRed` and `sMtMoonB2F_FireRed` entries in `src/data/wild_encounters.json`. Updates corresponding semantic rate checks in existing Full Gameplay Core gate and exact `src/data/wild_encounters.json` audited SHA in `tools/validate_audited_data_blobs.py`; the historical frozen-change manifest remains untouched. No other encounter maps, map scripts, Pokemon EV yields, save/link fields, trades or input changed.
- **New exact land-encounter probabilities**: Route3 FireRed Spearow 35%, Pidgey 20%, Mankey 10%, Jigglypuff 10%, Nidoran♀ 14%, Nidoran♂ 11% (before ♀1% / ♂14%). MtMoon 1F Zubat 60%, Geodude 25%, Paras 5%, Clefairy 10% (before 1%). MtMoon B2F Zubat 45%, Geodude 30%, Paras 15%, Clefairy 10% (before 6%). Clefairy new 1F slots remain levels 8–10. All baseline species remain catchable; LeafGreen encounter tables unchanged. Both 1% basic-species pain points addressed without systematically rewriting every rare encounter.
- **Exact predecessor CI** on `0a3d02613a241c0265c2b16b4f57cb5fe136f806`: Full Gameplay Core run `39849932055` SUCCESS and Follower Prototype run `39849932247` SUCCESS. New technical `fdf710c` Full Gameplay Core run `39851490790` and Follower Prototype run `39851490652` were IN PROGRESS at documentation checkpoint; **not yet validated / CI-GREEN** for the new code until the exact jobs are confirmed.
- **NPC trade triage** (nine FireRed offers; data in `src/data/ingame_trades.h`) remains proposal-only: Abra→Mr.Mime, Poliwhirl→Jynx, Nidoran♂→Nidoran♀, Spearow→Farfetch'd, Nidorino→Nidorina, Golduck→Lickitung, Raichu→Electrode, Venonat→Tangela, Ponyta→Seel. Early Spearow and male Nidoran now make Farfetch'd and female-Nidoran offers simpler, while Route3 female availability reduces the incentive to trade Nidoran. Potential low-value demands (Raichu→Electrode, Nidorino→Nidorina) need site-specific offer/availability audit, not automatic replacement. Consider enhancing fixed-IV competitive utility or item presentation only after checking species/flag economy, all nine NPC scripts, save/link and story progression.
- **Pending forest design**: protect user-chosen southeastern Viridian Forest non-trainer boy (45,58), south entrance, as 100% Oddish +1 Sp. Attack _inside a precisely delimited grass patch_, without altering standard forest encounters elsewhere. Examine 54×69 map.bin grass metatiles/collision and field encounter callbacks or separate tiny clearing before technical edit. Bellsprout +1 Attack stays excluded. Preserve NPC and nearby Potion event, warps and follower. If a new map is unavoidable, require intentional layout approval rather than silently constructing a new forest area.
- Other 1% encounter cases are triaged by **global attainability and alternative map/method**; 49 distinct 1%-probability map/method occurrences (14 species) are not 49 unavailable species. Leave optional evolved/alternative-sourced rarities at original rates unless individual playability audits justify changes. The near-final candidate, follower B10, MyBoy acceptance and integration to master remain incomplete.
