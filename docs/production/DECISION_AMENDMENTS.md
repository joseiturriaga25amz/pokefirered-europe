# Production Decision Amendments

This file records explicit user-approved changes made after the 2026-09-19 preproduction freeze. It supplements the frozen v1.0 documents without silently rewriting their historical state.

## A-001 — Emulator policy

**Date:** 2026-09-19  
**Status:** APPROVED  
**Supersedes:** the v1.0 wording that designated mGBA as the general primary emulator.

### Decision

- **MyBoy is the required runtime emulator for all user-run functional QA and Android playtesting, including link/trade tests.**
- MyBoy may satisfy ordinary smoke tests, save/load tests, gameplay regression, event checks, battle checks, and link/trade validation.
- **mGBA is no longer a required emulator for project acceptance.** It may be used only as an optional secondary diagnostic/reference tool if a defect needs cross-emulator comparison.
- MyBoy results must be recorded explicitly as MyBoy results.
- If a future test exposes a MyBoy-specific limitation that prevents the test from being executed at all, that limitation must be documented and brought back to the user before substituting another emulator; no automatic fallback is assumed.

### Rationale

The original preproduction freeze selected mGBA without first confirming the user's emulator preference or device constraints. The user explicitly corrected this during production and stated that MyBoy is the emulator they use and prefer, and then clarified that they want MyBoy used for all runtime testing. MyBoy supports GBA link-cable emulation, including same-device and Bluetooth/Wi-Fi modes, so link/trade QA does not inherently require mGBA. This amendment preserves test rigor while making the user's actual target environment authoritative for runtime acceptance.


## A-002 — Restore vanilla bag capacity

**Date:** 2026-09-19  
**Status:** APPROVED  
**Supersedes:** the v1.0 decision to expand the normal-items pocket from 42 to 142 slots.

### Decision

- The normal-items pocket keeps the original FireRed capacity and behavior: **42 slots**.
- The proposed 100 extra `ItemSlot` entries at `0x348C..0x361B` are **not used for the bag**.
- `unused_348C[400]` remains unused/reserved as in the base game.
- No contiguous 142-slot RAM mirror, no extended-bag save/load path, and no 50-item stress QA remain part of production.
- The Full save header at `0x3D24..0x3D33` and the reserved Full flag/var namespaces remain in scope because later Full events require persistent state.
- This amendment follows a failed MyBoy runtime test of the 142-slot implementation, where the game reached a black screen. The user explicitly chose to remove the bag expansion rather than continue investing in that feature.

### Rationale

The expanded bag is not important enough to the intended experience to justify additional implementation risk. Preserving vanilla bag behavior reduces save/runtime complexity while keeping the persistent-state infrastructure needed by later Full systems.


## A-003 — Production cadence: implement first, runtime QA at the end

**Date:** 2026-09-19  
**Status:** APPROVED  
**Supersedes:** the original per-block process that required repeated user-run smoke/functional tests after every implementation block.

### Decision

- During the remaining production phase, implementation and static/automated verification are performed continuously without stopping the user for repeated manual MyBoy tests.
- The assistant/developer is expected to be internally meticulous: compile, inspect, audit, add automated gates, and repair discovered defects while continuing toward the Release Candidate.
- User-run MyBoy functional testing is concentrated in the final RC audit and in genuinely necessary milestone/reproduction cases, not after every small change.
- A compilation or static PASS never substitutes for the final MyBoy runtime acceptance.
- If a runtime-only uncertainty blocks safe implementation, it is documented rather than silently declared PASS.

### Rationale

The user explicitly prioritized rapid progress and enjoyment over a strict software-engineering cadence with many visible intermediate tests. The project still requires rigorous final validation, but repeated manual checkpoints during implementation were judged unnecessarily slow for this project.


## A-004 — Repository is the continuity authority; chats are disposable

**Date:** 2026-09-20  
**Status:** APPROVED  
**Supersedes:** any workflow that relies on previous ChatGPT conversations as necessary project state.

### Decision

- The GitHub repository must contain the complete operational state required to resume Pokémon Rojo Fuego Full from a new chat or a different session.
- Frozen specification sources are archived under `docs/spec/`.
- Post-freeze decisions live in this amendment log.
- Current implementation/audit state lives in `docs/production/PROJECT_CONTINUITY.md` and `docs/production/RC_AUDIT_LOG.md`.
- Final audit method lives in `docs/production/FINAL_AUDIT_PLAN.md`.
- Runtime acceptance lives in `docs/production/RC_MYBOY_CHECKLIST.md`.
- Prior chats are context only; they are not a source of truth and may be deleted.
- When a new chat starts, the assistant must reconstruct state from the repository before modifying code.

### Rationale

The project has spanned multiple long chats and conversation continuity is brittle. Persisting decisions and state in Git makes the project reproducible, auditable, and independent of chat history.


## A-005 — Runtime polish: legendary narrative, Mew presentation and leader identity

**Date:** 2026-09-24  
**Status:** APPROVED  
**Supersedes:** the earlier Full postgame narrative in which Celio distributed both legendary tickets and the Sapphire/Network handoff effectively opened most legendary content at once.

### Decision

- **Legendary narrative V2 is approved.** Legendary content is split into independent thematic arcs rather than a single Celio/Sapphire hub:
  - Articuno/Zapdos/Moltres remain exploration discoveries in their original Kanto locations.
  - A short maritime investigation inspired explicitly by the Pokémon 2000 anime/movie connection between the birds and Lugia leads to the original ITEM_MYSTIC_TICKET; the gate is the three birds **seen**, not necessarily captured.
  - Lugia remains on Navel Rock. Ho-Oh uses the same original MysticTicket/Navel Rock destination but becomes the capstone of the Suicune/Raikou/Entei arc instead of being immediately available with Lugia.
  - Mewtwo remains the Cerulean Cave post-Network encounter; Mew remains its Kanto genetic-story epilogue in Pokémon Mansion.
  - Deoxys becomes an autonomous Pewter Museum / space-anomaly investigation whose scientist grants the original ITEM_AURORA_TICKET; Celio is removed from the ticket handoff.
  - Celebi keeps Berry Forest identity but gains its own forest/nature mini-investigation; capturing all three beasts is no longer presented as a canonical causal requirement.
- **Celio is restricted to his canonical/credible network role:** Ruby/Sapphire, Network Machine and regional connectivity. He does not distribute legendary tickets or present the legendary beasts.
- **Roaming beasts V2:** one cinematic/overworld first contact shows Suicune as the focus with Raikou and Entei present; all three flee with **no battle and no capture opportunity**. All three are marked seen with standard Pokédex flags. Only Suicune is active/trackable first, then Raikou, then Entei, preserving one vanilla roamer at a time and VAR_FULL_ROAMER_SEQUENCE.
- Roamer UX is approved for substantial simplification: immediate Pokédex tracking after the cinematic, less erratic route movement, higher encounter reliability when reaching the tracked route, a short combat window before fleeing, and easier catch balance. Exact route cadence/probabilities/catch rates remain polish/QA values, not immutable contract numbers.
- **Mew presentation polish is approved in principle:** preserve the canonical mansion diary history, but add present-day atmosphere, visible Mew overworld appearances while the player follows the diary trail, and a final visible/interactable Mew before battle rather than launching the battle immediately when the last diary closes. Existing OBJ_EVENT_GFX_MEW is to be reused; do not change Pokémon/save/link structures.
- **Gym leader rematch dialogue identity is approved:** the eight leaders must not share the same four generic rematch strings. Keep the approved teams and repeatable mechanics, but write leader-specific offer/opening/defeat/post-battle dialogue consistent with each character.
- Old RC runtime established: Mew quest/capture works; Brock rematch is repeatable; Misty/Surge/Erika rematches start and are challenging; strengthened League starts and Lorelei was seen using Dewgong/Lapras. The user was deliberately underleveled from speedrun-style progression, so no forced grind is required.
- Old-RC roaming-beast capture and Celebi are **withdrawn from the current manual QA pass**. Ho-Oh respawn-after-KO is not to be forced through another League solely for QA; validate on a disposable/new RC save.

### Compatibility constraints

- Preserve original species/item IDs, Gen III Pokémon/BoxPokemon structures, TrainerCard/link packet formats, MysticTicket/AuroraTicket IDs and ferry destinations, standard Pokédex flags and vanilla roamer storage.
- New narrative state may use audited Full flags/vars only; no save-structure growth.
- Advanced-save migration must preserve already-earned tickets/captures and the old RC's Ho-Oh KO-pending state without duplication or softlock.
- Structural compatibility is a design requirement, not proof of Full↔future-Emerald interoperability; final MyBoy link QA remains mandatory.


## A-006 — Immersion/QoL expansion: special Balls, follower Pokémon and postgame guidance

**Date:** 2026-09-24  
**Status:** APPROVED WITH FOLLOWER TECHNICAL GATE

### Decision

- **All existing Gen III specialty Poké Balls become naturally purchasable** with progression/context-appropriate shops and prices: Net/Malla, Nest/Nido, Repeat/Acopio, Timer/Turno, Luxury/Lujo, Dive/Buceo and Premier/Honor. Do not sell Master Ball or Safari Ball.
- Keep **Dive Ball mechanics unchanged** in FireRed Full. In the current Gen III code its bonus applies only on MAP_TYPE_UNDERWATER; FireRed has no normal underwater gameplay, so it is primarily aesthetic/collection value there. Do not invent Surf/fishing bonuses. It becomes naturally useful again in future Emerald Full.
- Distribution should feel progressive rather than dumping every Ball in the first shop. Midgame stores may introduce Malla/Nido; late-game/Sevii stores add Acopio/Turno/Lujo/Honor/Buceo; at least one postgame/Sevii shop should provide a complete legitimate specialty-Ball stock. Exact store and price table must be balanced against the existing economy and Ultra Ball price before implementation.
- **Follower Pokémon is an approved experience target:** the party leader should be able to appear as an overworld companion following the player, with an on/off option and robust automatic hiding/reappearance around unsafe transitions (bike/Surf/Fly/link/cutscenes/etc.) as required by the implementation.
- **Follower contextual interaction is approved:** talking to the companion may use species/type/friendship/status/map/weather context to produce HGSS-style reactions. This must remain cosmetic and may not mutate Pokémon structures or create a second stored copy of the follower.
- **Pokédex usefulness improvements are approved:** improve information for already-seen species (for example clearer encounter method/area/level context) while preserving discovery and not revealing unknown legendary locations.
- **Postgame training progression is approved:** provide a natural level bridge from speedrun/end-story teams into gym rematches and the strengthened League using existing rematches/VS Seeker/high-value trainers rather than global EXP inflation or mandatory grind.
- **Legendary environmental signals are approved:** use cries, overworld sprites, NPC reactions, scenery and staged clues to make legendary quests feel discovered rather than menu-unlocked.
- **Important NPC identity polish is approved:** major NPCs, especially leaders/scientists/sailors/quest characters, should have context-specific dialogue rather than interchangeable Full boilerplate.

### Follower feasibility / source research

- Full's current FireRed tree contains only a limited set of Pokémon overworld event sprites, so native assets alone are insufficient for all 386 species.
- A concrete Gen III reference exists: monhacks/arrantemerald, branch followers-expanded-id, documents HGSS-style followers for **all 386 Pokémon including forms and shinies**, follower interactions, dynamic overworld palettes, 64x64 support and a backwards-compatible 16-bit overworld graphics-ID expansion. Its repository contains hundreds of Pokémon overworld PNG assets (440 files in the follower Pokémon graphics directory, including forms/legacy variants).
- The same project states that it does **not increase save-data structures or the object-event structure**, and recommends the expanded-ID follower branch. This makes it a strong technical/reference candidate for solving the sprite-work problem without drawing 386 sets manually.
- It is an **Emerald** implementation, not a drop-in FireRed patch. Port only the minimum follower/graphics/palette concepts after a source-level audit against our FireRed engine. Do not adopt a full expansion base that changes species/items/save/link contracts.
- The repository does not expose a clear top-level license for these follower assets. Before redistributing imported sprites/code, verify provenance, permission/credits and any third-party asset terms. Technical availability is not automatic redistribution permission.
- Follower implementation remains gated behind an isolated prototype because it is highly transversal. Acceptance requires MyBoy tests for warps, ledges, doors, trainer sight, scripts, palette/OAM pressure, party reorder/boxing/eggs/fainted lead/shiny, save/load and Full↔vanilla link. If the module threatens stability or compatibility, it can be removed without blocking the rest of v1.0.

### Compatibility constraints

- Do not add new Pokémon or Ball IDs for these features.
- The follower is a visual projection of an existing party Pokémon, never new persistent Pokémon data.
- Preserve struct Pokemon, BoxPokemon, SaveBlock layouts and Link serialization.
- Preserve original specialty-Ball IDs and caught-ball metadata so Pokémon traded to future Emerald Full remain normal Gen III Pokémon.


## A-007 — Signature Pokémon staging for major trainers

**Date:** 2026-09-24  
**Status:** APPROVED

### Decision

- Major trainer characters should visibly have one signature/ace Pokémon beside them in the overworld to strengthen the anime-like presentation before battle.
- v1.0 required scope is deliberately bounded to:
  - the eight Kanto Gym Leaders;
  - Lorelei, Bruno, Agatha and Lance;
  - Gary/Blue as rival and Champion, with the Squirtle line evolving visually with his progression where practical.
- This is **not** implemented through the player's dynamic follower system. Boss companions are ordinary controlled map/event presentation objects with fixed species/graphics for each scene.
- The displayed Pokémon should prioritize character identity and the approved battle roster, not merely the numerically highest level. Initial target identities for implementation/audit are:
  - Brock — Onix;
  - Misty — Starmie;
  - Lt. Surge — Raichu;
  - Erika — Vileplume;
  - Koga — Weezing;
  - Sabrina — Alakazam;
  - Blaine — Magmar;
  - Giovanni — Persian;
  - Lorelei — Lapras;
  - Bruno — Machamp;
  - Agatha — Gengar;
  - Lance — Dragonite;
  - Gary/Blue — Squirtle → Wartortle → Blastoise according to story stage.
- Exact positioning must preserve NPC movement, trainer sight, scripted cutscenes, warps and player collision. The companion should be non-blocking or placed outside required walking paths.
- The companion remains visual presentation only. It does not represent a second stored Pokémon, does not alter the trainer party, and requires no new save state.
- Other NPC companions are **not part of the mandatory v1.0 scope**. They may be added only when an NPC has strong narrative value, a suitable asset is already available/provenance-cleared, and the addition does not expand QA materially.

### Asset / compatibility constraints

- Reuse existing FireRed Full overworld assets where suitable.
- Missing signature sprites must use a project-created or otherwise provenance-cleared asset path; do not import the unresolved HGSS/veekun follower pack merely to satisfy this feature.
- Prefer normal static 8-bit object-event graphics IDs. Do not introduce the Emerald follower branch's 16-bit graphics-ID ABI for boss staging.
- Audit available object-event graphics-ID space and per-map object counts before adding assets.
- This block should serve as a small-scale sprite/OAM/map-integration pilot before any attempt at 386-species follower coverage.

### QA

- Compile/static map validation for every touched room.
- Confirm each signature Pokémon is visible beside the intended trainer at the correct story stage.
- Confirm player pathing, interaction with the trainer, battle start, post-battle state and rematch interaction remain functional.
- Explicit MyBoy spot-checks: at least one early Gym, one late Gym, one Elite Four room and one Gary/Champion scene.
- No change to SaveBlock, Pokémon/BoxPokemon structures or Link serialization.


## A-008 — Runtime-approved B1 QoL and presentation rules

**Date:** 2026-09-24  
**Status:** APPROVED  
**Supersedes/extends:** frozen QOL-002 HM behavior, frozen ECO-006 Porygon price, and post-freeze runtime polish decisions that were previously recorded only in the external runtime evidence log.

### Decision

The following runtime-approved rules are authoritative for B1 and v1.0 closure:

- **UI-001 — EV layout:** keep the existing EV view/toggle and exact EV data, but repair the cramped/overlapping lower-page layout before final RC.
- **UI-002 — move category visibility:** Physical / Special / Status must be clearly visible when inspecting moves. This is a v1.0 closure requirement even though the original freeze specified the split primarily as engine behavior.
- **ECO-CASINO-001 — Porygon:** change the repeatable Celadon Game Corner Porygon prize from **5,000 to 5,500 coins**, keep it last in the list, and format/alignment must match the localized prize list (5.500 FICHAS in Spanish presentation).
- **QOL-VEND-001 — vending machines:** Fresh Water / Soda Pop / Lemonade vending purchases must support a quantity selector with atomic money/space validation and delivery. Prices and the thirsty-girl drink-for-TM interaction remain unchanged.
- **QOL-AIDE-001 — Oak aides:** replace species-count gates with story-appropriate badge gates while retaining NPC location, one-time reward flags and bag-space checks:
  - Route 2 / HM05 Flash — Cascade Badge;
  - Route 11 / Itemfinder — Thunder Badge;
  - Route 10 / Everstone — Thunder Badge;
  - Route 16 / Amulet Coin — Rainbow Badge;
  - Route 15 / Exp. Share — Rainbow Badge.
- **QOL-NATDEX-001 — National Dex:** remove the vanilla 60-captured-species quota. Keep first Hall of Fame / game clear and the One Island narrative visit gate; preserve Oak's National Dex scene itself.
- **QOL-HM-002 — HMs as field licenses:** field actions require possession of the corresponding HM plus the original badge/narrative gate; no party Pokémon needs to know the move for Cut trees/Dotted Hole, Surf, Strength, Flash, Rock Smash or Waterfall. **Approved exceptions:** Fly remains vanilla and requires a compatible party Pokémon that knows Fly; optional grass-cutting remains on the vanilla learned-Cut route rather than expanding the party-menu action system. HMs remain reusable teachable moves for battle, and an HM move learned by a Pokémon may be replaced/forgotten normally without the Move Deleter.
- **QOL-EXP-001 — Exp. Share:** keep vanilla FireRed held-item behavior. Do not implement automatic modern party-wide EXP distribution.

### Compatibility constraints

- No SaveBlock, Pokémon/BoxPokemon, species/item ID or Link serialization changes.
- HM field-action changes must reuse existing item/badge/progression state rather than create a new persistent HM-license structure.
- Aide/vending/Porygon changes must preserve one-time reward flags, inventory safety and existing item IDs.
- Final validators and MyBoy checks must test the amended behavior, not the superseded frozen QOL-002/ECO-006 wording.


## A-009 — Runtime-approved later-block balance, progression and localization rules

**Date:** 2026-09-24  
**Status:** APPROVED  
**Purpose:** promote approved runtime findings that were already reflected in the production work order but were not yet repository-authoritative decisions.

### Decision

- **BOSS-GIO-001:** all Giovanni battles, including Rocket Hideout and Silph Co., must receive the same Full boss-design standard used for Gym Leaders, League and Gary: real challenge, character identity, anime/canon + game grounding, and moves coherent with the point of the story. Exact rosters/moves/levels are B2 implementation details subject to legality/progression validation.
- **BOSS-REMATCH-001:** Gym Leader rematches unlock directly after the first Hall of Fame / game clear and do not depend on National Dex or capture counts. The strengthened League/Gary rematch remains a later postgame tier gated by the completed Ruby/Sapphire Network Machine progression.
- **ENC-ALTERING-001:** Altering Cave must keep the nine existing tables/IDs 0–8 but rotate the active table automatically through player activity/progress rather than a manual species selector. One table is active at a time and remains stable during a visit. The researcher becomes informational. Avoid RTC dependence.
- **Special encounter rarity:** final polish targets are Safari headline rares 10% in their best zone, Dratini 10% in its best Safari zone, wild starters 10% / 4% / 1% for base / middle / final stages, and Magmar/Electabuzz 4%. Do not make them feel rare by lowering catch rates; Dragonair direct availability, if retained, must remain clearly rarer than Dratini.
- **Legendary capture UX:** legendary capture must be materially less tedious than the old RC while remaining clearly harder than ordinary Pokémon. Apply the principle across Full legendaries; exact numerical catch-rate values remain a B6 polish/QA decision and are not frozen by this amendment. Mew/Celebi do not need to be made harder.
- **L10N-001:** all Full-added Spanish monetary/coin text must use localized thousands separators consistently (for example 1.000, 1.500, 2.000, 5.500, 10.000) without silently changing underlying values unless another approved balance decision does so.
- **L10N-002:** the active Move Reminder dialogue must match the Full money-based repeat system and must not tell the player to bring mushrooms when the actual path charges money.

### Compatibility constraints

- Preserve Altering Cave variable semantics/IDs and encounter table format.
- Do not alter species/item IDs, Pokémon/BoxPokemon structures, SaveBlock sizes or Link serialization for these rules.
- Boss/encounter/capture tuning must be validated against story-stage progression and existing respawn/state-machine guarantees.


## A-010 — GAME FREAK Pokédex completion rewards

**Date:** 2026-09-25  
**Status:** APPROVED  
**Implementation block:** B9 — Pokédex usefulness

### Decision

- Preserve the original GAME FREAK diploma presentation in `CeladonCity_Condominiums_3F`.
- Completing the Kanto Pokédex under the existing `HasAllKantoMons()` rule (150 Kanto species, Mew excluded) awards:
  - the original Kanto diploma; and
  - **one additional Master Ball** as a tangible completion reward.
- The Master Ball reward is strictly one-time. Use an audited persistent flag; do not add item IDs or grow save structures.
- Full-bag handling must be safe: if the player cannot receive the Master Ball, do **not** mark the reward as claimed. The player may return later and receive it once space is available.
- The dialogue should acknowledge the diploma and then explicitly recognize that the achievement merits an additional prize.
- `HasAllMons()` / National Pokédex completion retains the National diploma, but its additional 100%-completion reward is intentionally **not frozen yet**. It will be designed separately before B9 closes rather than defaulting to a second Master Ball.

### Compatibility constraints

- Reuse `ITEM_MASTER_BALL`.
- No species/item ID changes.
- No Pokémon/BoxPokemon or link-serialization changes.
- No SaveBlock growth; allocate only an audited existing Full flag namespace.
- Preserve the original diploma behavior and National/Kanto distinction.


## A-011 — Signature staging identity correction

**Date:** 2026-09-28  
**Status:** APPROVED  
**Supersedes:** only the affected signature-species mapping lines in A-007; all A-007 technical constraints remain in force.

### Decision

- Brock: **Onix** in the main-story Gym battle; **Steelix** for the postgame rematch.
- Erika: **Gloom**, not Vileplume.
- Koga: **Golbat** in the main-story Gym battle; **Crobat** for the postgame rematch.
- Sabrina: **Kadabra**, not Alakazam.
- The visible companion must be story-stage aware whenever the approved rematch identity changes.
- Misty remains Starmie, Lt. Surge remains Raichu, Blaine remains Magmar, Giovanni remains Persian, Lorelei remains Lapras, Bruno remains Machamp, Agatha remains Gengar, Lance remains Dragonite, and Gary/Blue remains stage-aware Squirtle → Wartortle → Blastoise.
- These visual changes reuse the same story/rematch gates already used by the trainer scripts and add no new save state.


## A-012 — Full animated follower presentation

**Date:** 2026-09-28  
**Status:** APPROVED  
**Applies to:** B10 player-follower integration.

### Decision

- The player follower must use a **fully animated overworld walking presentation**, not a static Pokémon icon sliding behind the player.
- The visible follower must have direction-aware movement and actual walking frames appropriate to the FireRed object-event engine.
- The static icon-to-object bridge developed in B8 may be reused for trainer staging, but it is **not acceptable as the final player-follower rendering path**.
- B10 must therefore use provenance-cleared/project-created animated overworld assets for supported species, with palette/OAM integration designed for follower runtime.
- The follower remains a cosmetic projection of the party-slot-1 Pokémon and must not add a second stored Pokémon or change Pokémon/BoxPokemon, SaveBlock, or link serialization.
- If complete animated coverage cannot be provided safely for all intended species, the feature must remain gated rather than silently degrading unsupported species to floating/static icons.

### Acceptance intent

The target presentation is HGSS-like in behavior: the Pokémon should visibly walk behind the player, turn with movement, and transition naturally through ordinary field movement. Final MyBoy QA remains required for animation, warps, ledges, doors, scripts, palette/OAM pressure, save/load, and link isolation.

## A-013 — Major-trainer roster research method and Brock roster identity

**Date:** 2026-09-30  
**Status:** APPROVED  
**Scope:** Gym Leader roster research pass; Brock completed. This records design decisions only. Gameplay implementation, levels and movesets remain a separate validated microblock.

### Review method

For each Gym Leader, review the complete canon-associated Pokémon pool one species/line at a time, with special weight given to anime-owned/used Pokémon as identity candidates. Anime chronology is not a hard restriction: canon is used to establish trainer identity, not to reproduce the exact episode timeline.

For each leader:
1. review the complete candidate list with a brief potential assessment;
2. define first battle and rematch rosters;
3. explicitly confirm signature/overworld companion and ace for both stages;
4. only after roster approval, rebalance levels, order, held items and movesets against the real production progression;
5. validate trainer-set legality and adjacent progression before implementation is considered complete.

Elite Four and Gary/Blue research remains a later phase after the Gym Leader pass. Giovanni additionally requires review of non-Gym story appearances.

### Brock — approved roster

**First battle**
- Geodude
- Zubat
- Vulpix
- Onix — ace and signature companion

**Rematch**
- Golem
- Crobat
- Forretress
- Ludicolo
- Marshtomp
- Steelix — ace and signature companion

### Brock design intent

- Zubat is intentionally present in the first battle despite not being a classic Brock Gym species because it strongly represents Brock's anime identity.
- Vulpix receives a first-battle slot for the same identity reason and is intentionally dropped from the rematch.
- The rematch preserves three visible progression lines from the first battle: Geodude→Golem, Zubat→Crobat and Onix→Steelix.
- Steelix remains the rematch ace; Onix remains the first-battle ace.
- The B8 staging decision already matches this identity: Brock displays Onix pre-rematch and Steelix in the later state.
- Brock implementation is now defined as follows:
  - first battle levels: Geodude 13, Zubat 14, Vulpix 15, Onix 17;
  - first-battle moves: Geodude — Rock Throw/Tackle/Defense Curl/Mud Sport; Zubat — Leech Life/Astonish/Supersonic; Vulpix — Ember/Quick Attack/Roar/Tail Whip; Onix — Rock Tomb/Bind/Screech/Tackle;
  - rematch levels remain 60/61/62/63/64/66 with Golem/Crobat/Forretress/Ludicolo/Marshtomp/Steelix;
  - Golem uses Earthquake/Rock Slide/Brick Break/Double-Edge and **must not use Explosion**;
  - Steelix retains Leftovers and remains the rematch ace;
  - exact roster assertions are enforced in `tools/validate_full_trainer_sets.py`.
- English move identifiers above are repository constants; user-facing review should always present the Spanish in-game names.

### Brock closure evidence

- Final feature/documentation HEAD: `3d357df82120b779213b4fc5e8b9c56eb86ae1f1`.
- Full Gameplay Core run **#619**: **SUCCESS**.
- Merged to `master` as `269d75b501a99c92fd8296189760899a6a5d4571`.
- Post-integration Full Gameplay Core run **#620**: **SUCCESS**.
- Brock roster microblock status: **CLOSED**.
- Next leader under this amendment: **Misty**.

### Implementation/validation procedure for later Leader changes

When an approved Leader roster changes a previously frozen trainer set:
1. modify only the approved party/level/move/item scope;
2. update every exact-roster/frozen expectation that intentionally describes that same set;
3. preserve semantic legality validation and relock audited data blobs only after reviewing the intentional diff;
4. run Full Gameplay Core on the exact feature HEAD;
5. if infrastructure fails because it still encodes the superseded approved roster, update that expectation rather than reverting valid gameplay;
6. integrate onto the current master only after the exact feature HEAD is green;
7. rerun the production gate on the exact integrated master HEAD before marking the microblock CLOSED.

This procedure is part of the Gym Leader roster pass and should be reused for Misty and later Leaders when their approved rosters differ from the currently frozen production sets.

### Misty — approved roster identity

**First battle**
- Staryu
- Starmie
- Psyduck
- Poliwag

Rationale:
- Togepi and Horsea are strongly associated with Misty, but are excluded from the battle roster because the intended characterization distinguishes Pokémon she notably carried/cared for from Pokémon she regularly used to battle.
- Psyduck and Poliwag therefore take the anime-identity battle slots alongside the Staryu/Starmie core.

**Rematch**
- Starmie
- Gyarados
- Corsola
- Politoed
- Togetic
- Staryu

**Ace/signature split**
- First battle ace: Starmie.
- First battle signature companion: Starmie.
- Rematch ace: Gyarados.
- Rematch signature companion: Starmie.
- This intentionally separates combat strength from visual identity: Gyarados is the stronger rematch ace, while Starmie remains Misty's most iconic companion for staging.

**Visual staging — approved**
- Misty remains at (8,6).
- Starmie remains immediately to Misty's left at (7,6) in both story/rematch states.
- Togepi is placed immediately to Misty's right at (9,6) as a non-battle identity/presentation object.
- Existing Seel remains in the pool at (5,12).
- Horsea is placed in the pool at (6,12), directly beside Seel.
- Existing Staryu pool ambience remains at (12,14).
- The selected Togepi tile is the symmetric free platform tile beside Misty; the Horsea tile is a free water tile matching the existing pool ambience and conflicts with no object or warp.
- Togepi and Horsea require new static icon-object registrations following the existing Seel/Staryu B8 icon pattern; no new Pokémon/save/link structure is required.

**Balance status**
- Species/identity are approved.
- Levels/order/held items remain under review.
- Approved rematch move adjustments:
  - Corsola uses Spike Cannon / Cañón Pincho instead of Ancient Power.
  - Togetic uses Safeguard / Velo Sagrado, Metronome / Metrónomo, Psychic / Psíquico and Fly / Vuelo.
- First-battle Psyduck uses Water Gun / Pistola Agua instead of Water Sport / Hidrochorro.
  - This is an **explicit approved trainer-only move exception**.
  - It does not modify Psyduck's global learnset, save structures, link/trade data, species data or move data.
  - The legality validator must whitelist only `sParty_LeaderMisty / SPECIES_PSYDUCK / level 20 / MOVE_WATER_GUN`; no broader exception is approved.



### Misty implementation specification

**First battle**
- Psyduck Lv.20 — Confusion / Disable / Scratch / Water Gun; no held item.
- Poliwag Lv.21 — Water Gun / Hypnosis / DoubleSlap / Bubble; no held item.
- Staryu Lv.23 — Water Pulse / Recover / Rapid Spin / Camouflage; no held item.
- Starmie Lv.26 — Water Pulse / Swift / Rapid Spin / Recover; Sitrus Berry; ace and signature companion.

**Rematch**
- Staryu Lv.61 — Surf / Ice Beam / Cosmic Power / Recover; no held item.
- Corsola Lv.62 — Surf / Spike Cannon / Recover / Mirror Coat; no held item.
- Politoed Lv.63 — Surf / Ice Beam / Hypnosis / Perish Song; Sitrus Berry.
- Togetic Lv.64 — Safeguard / Metronome / Psychic / Fly; Leftovers.
- Starmie Lv.66 — Surf / Psychic / Thunderbolt / Recover; Twisted Spoon; signature companion.
- Gyarados Lv.68 — Waterfall / Earthquake / Dragon Dance / Hyper Beam; Mystic Water; ace.

**Gym staging**
- Starmie at (7,6), Misty at (8,6), Togepi icon at (9,6).
- Seel icon at (5,12), Horsea icon at (6,12), existing Staryu icon at (12,14).
- Togepi/Horsea use static icon objects and remain non-interactive/nonblocking.


### Misty closure evidence

- Final feature HEAD: `4c8d16bcf7878960b6dd5f7ffb5ee44c5ff2adf7`.
- Full Gameplay Core run **#624**: **SUCCESS**.
- Merged to `master` as `323ff3daef5e8019690cda83c4527b5ec07ff3c1`.
- Post-integration Full Gameplay Core run **#625**: **SUCCESS**.
- Misty roster/identity microblock status: **CLOSED**.
- Validation incidents resolved during the cycle:
  - removed obsolete Staryu Lv.23 Swift/Rapidez legality exception after the approved moveset changed;
  - updated B3 ace validator from Starmie Lv.67 to Gyarados Lv.68 to match the approved ace/signature split.
- Next leader under A-013: **Lt. Surge**.


### Brock tuning amendment — second pass

**Status:** APPROVED / IMPLEMENTED on branch `fix/brock-roster-adjustments-2`.

This reopens Brock only as a new tuning microblock. The prior Brock closure remains valid historical evidence for the earlier approved version.

**First battle**
- Zubat Lv.13 — Wing Attack / Leech Life / Whirlwind / Supersonic.
- Vulpix Lv.14 — Ember / Quick Attack / Fire Spin / Agility.
- Geodude Lv.15 — Rock Throw / Tackle / Revenge / Defense Curl.
- Onix Lv.17 — Rock Tomb / Tackle / Bind / Screech; retains Oran Berry; remains ace/signature.

**Rematch**
- Marshtomp Lv.60 — Earthquake / Muddy Water / Mud Shot / Protect; no held item.
- Ludicolo Lv.61 — Surf / Giga Drain / Ice Beam / Bullet Seed; no held item.
- Forretress Lv.62 — Rapid Spin / Spikes / Protect / Explosion.
- Golem Lv.63 — Earthquake / Rock Slide / Rollout / Defense Curl; no held item.
- Crobat Lv.64 — Sludge Bomb / Aerial Ace / Bite / Confuse Ray; no held item.
- Steelix Lv.68 — Earthquake / Iron Tail / Crunch / Dragon Breath; Metal Coat; remains ace/signature.

**Held-item policy**
- First battle: only Onix carries an Oran Berry.
- Rematch: only Steelix carries a held item, Metal Coat, to reinforce its Steel-type ace identity.
- Marshtomp, Ludicolo, Forretress, Golem and Crobat carry no held items.

**Trainer-only legality exceptions**
- Zubat Lv.13 Wing Attack.
- Vulpix Lv.14 Fire Spin.
- Vulpix Lv.14 Agility.
- Geodude Lv.15 Revenge.

These exceptions apply only to Brock's trainer party. They do not modify global learnsets, species data, move data, save compatibility or link/trade structures.


### Brock second-pass closure evidence

- Final second-pass feature HEAD: `12b244fd3b1f87b8b653fd6aaaa3d21b53c967f2`.
- Full Gameplay Core **#631**: **SUCCESS**.
- Merged to `master` as `193b14aa3e5426dbf6049efa32a6d7c2c4d0d050`.
- Post-integration Full Gameplay Core **#632**: **SUCCESS**.
- Second-pass tuning status: **CLOSED**.
- Final held-item policy:
  - first battle: only Onix holds Oran Berry;
  - rematch: only Steelix holds Metal Coat;
  - all other Brock rematch Pokémon hold no item.
- Validation incident #628 was caused by a duplicate stale Brock rematch expectation in `validate_full_trainer_sets.py`; removed without gameplay rollback.
- Runs #629/#630 were infrastructure-stalled before project validation and are not closure evidence.
- Do not begin Lt. Surge until explicitly requested by the user.

### Misty tuning amendment — second pass

**Status:** **CLOSED**.

This reopens Misty only as a new tuning microblock. The prior Misty closure remains valid historical evidence for the earlier approved version.

**First battle**
- Psyduck Lv.20 — Water Gun / Confusion / Disable / Scratch; no held item.
- Poliwag Lv.21 — Water Gun / Bubble / DoubleSlap / Hypnosis; no held item.
- Staryu Lv.23 — Water Pulse / Swift / Rapid Spin / Protect; no held item.
- Starmie Lv.26 — Water Pulse / Swift / Rapid Spin / Recover; Mystic Water; remains ace/signature.

**Rematch**
- Togetic Lv.61 — Hidden Power / Metronome / Safeguard / Protect; no held item.
- Staryu Lv.62 — Surf / Ice Beam / Double-Edge / Recover; no held item.
- Politoed Lv.63 — Surf / Brick Break / Mega Punch / Bounce; no held item.
- Corsola Lv.64 — Surf / Spike Cannon / Mirror Coat / Recover; no held item.
- Starmie Lv.66 — Surf / Psychic / Protect / Recover; no held item; remains signature companion.
- Gyarados Lv.68 — Waterfall / Earthquake / Rain Dance / Protect; Mystic Water; remains rematch ace.

**Held-item policy**
- First battle: only Starmie carries Mystic Water.
- Rematch: only Gyarados carries Mystic Water.

**Trainer-only legality exceptions**
- Psyduck Lv.20 Water Gun (existing approved exception).
- Staryu Lv.23 Swift.
- Politoed Lv.63 Bounce.

The Staryu and Politoed exceptions are identity-specific trainer-party exceptions only. They do not modify global learnsets, species data, move data, save compatibility or link/trade structures.

**Mirror Coat compatibility check**
- Corsola's Mirror Coat remains valid with Full's physical/special split.
- Damage bookkeeping records physical/special damage from each move's explicit modern category via `IS_MOVE_PHYSICAL` / `IS_MOVE_SPECIAL`, and Mirror Coat reads the special-damage record.



### Misty second-pass closure evidence

- Final second-pass feature HEAD: `a06ac70b39e3d4736de86a3680ffb0ffda1d079b`.
- Full Gameplay Core **#635**: **SUCCESS**.
- Merged to `master` as `08bbd40374850595bc8261b1ab44ebae2012aa35`.
- Post-integration Full Gameplay Core **#636** on that exact master SHA: **SUCCESS**.
- Second-pass tuning status: **CLOSED**.
- Final first-battle Starmie remains Lv.26 and carries Mystic Water.
- Final rematch held-item policy: only Gyarados carries Mystic Water.
- Trainer-only exceptions are limited to Psyduck Lv.20 Water Gun, Staryu Lv.23 Swift and Politoed Lv.63 Bounce.
- Run #634 failed only because the audited `trainer_parties.h` blob lock still referenced the previous intentional trainer data; the lock was relocked after diff review and #635/#636 passed.
- Do not begin Lt. Surge until explicitly requested by the user.


### A-013 research pool — user-supplied canon associations

**Status:** APPROVED RESEARCH INPUT / NOT A ROSTER DECISION.

This list is preserved from the user's research and is the candidate pool to use for the remaining Gym Leader / Giovanni identity analysis. It must not be expanded, reduced, or silently corrected from chat memory. Inclusion here means "consider during analysis", not "approved for a battle roster".

#### Brock

**Kanto**
- Onix (ace)
- Geodude (icónico)
- Zubat (no lo usaba tanto en principio)
- Vulpix (se lo da Suzy)

**Johto**
- Zubat evolucionó a Golbat
- Golbat evolucionó a Crobat (fuerte)
- Pineco
- Onix evolucionó a Steelix (fuerte y ace)

**Bien**
- Pineco evolucionó a Forretress
- Lotad-Lombre-Ludicolo
- Mudkip-Marshtomp

#### Misty

**Kanto**
- Staryu (icónico y querido)
- Starmie (ace)
- Seel que luego es Dewgong (es del gimnasio)
- Goldeen (poco uso)
- Horsea (rescatado y tierno)
- Psyduck (se auto atrapó)
- Togepi (muy querido)
- Poliwag (se encariñó con él)

**Johto**
- Su Poliwag evolucionó a Poliwhirl
- Corsola (de sus Pokémon más fuertes)
- Su Poliwhirl evolucionó a Politoed

**Hoenn**
- Gyarados (insignia y fuertísimo)
- Togepi evolucionó a Togetic
- Azurill
- Luvdisc es caso especial: solo aparece en un capítulo especial; no se cuenta.

#### Lt. Surge

**Kanto**
- Raichu (anime)
- Voltorb (canon videojuegos)
- Pikachu (canon videojuegos)

**Johto**
- Voltorb evolucionó a Electrode
- Magneton

**Oro HeartGold y Plata SoulSilver**
- Electrike-Manectric
- Electabuzz

#### Erika

**Kanto**
- Weepinbell (Rojo, Azul, Amarillo) (anime)
- Victreebel (Rojo Fuego y Verde Hoja)
- Tangela (anime)
- Gloom (Amarillo) (Pokémon insignia anime) (anime)
- Vileplume (insignia juegos)

**Johto**
- Bellossom
- Jumpluff (HeartGold y SoulSilver)

**Hoenn**
- Cradily (videojuegos)
- Shiftry (videojuegos)
- Exeggutor (videojuegos)

#### Koga

Visual identity note: en el gimnasio mantiene Voltorb camuflados como Poké Balls trampa para detener a los intrusos. El usuario quiere considerar implementarlo visualmente, sin combate, solo estético.

**Kanto**
- Koffing (Rojo, Azul, Rojo Fuego y Verde Hoja)
- Weezing (Rojo, Azul, Rojo Fuego y Verde Hoja) (insignia en Rojo Fuego)
- Muk
- Venonat (anime) (Amarillo)
- Venomoth (anime) (Amarillo)
- Golbat (anime)

**Johto — Oro, Plata, Cristal, HeartGold, SoulSilver**
- Ariados
- Forretress
- Crobat

**Hoenn**
- Swalot (HeartGold y SoulSilver)

#### Sabrina

**Kanto**
- Abra (icono anime, evoluciona a Kadabra)
- Kadabra (icono del anime)
- Mr. Mime (videojuegos)
- Venomoth (Rojo, Azul, Rojo Fuego y Verde Hoja)
- Alakazam (insignia videojuegos)

**Johto — Oro, Plata, Cristal, HeartGold, SoulSilver**
- Espeon

**Hoenn**
- Wobbuffet (HeartGold y SoulSilver)
- Jynx (HeartGold y SoulSilver)

#### Blaine

**Kanto**
- Growlithe (todos los videojuegos)
- Arcanine (insignia videojuego) (todos los videojuegos)
- Ponyta
- Rapidash
- Magmar (principal en Amarillo) (insignia anime)
- Ninetales (Rojo, Azul, Rojo Fuego y Verde Hoja) (anime)
- Rhydon (anime)

**Johto**
- Magcargo

**Hoenn — HeartGold y SoulSilver**
- Torkoal
- Camerupt

#### Giovanni

**Kanto**
- Rhyhorn
- Onix
- Nidorino
- Nidorina
- Nidoking (evolucionado de Nidorino)
- Nidoqueen (evolucionado de Nidorina)
- Dugtrio
- Persian (Amarillo)
- Kangaskhan
- Mewtwo (anime)
- Golem (se lo deja al Team Rocket para defender el gimnasio)
- Machamp (se lo deja al Team Rocket para defender el gimnasio)
- Kingler (se lo deja al Team Rocket para defender el gimnasio)
- Rhydon (se ve en el anime como parte del arsenal de Pokémon) (insignia en Pokémon Origins)
- Cloyster (se ve en el anime como parte del arsenal de Pokémon)

**Hoenn — HeartGold y SoulSilver**
- Camerupt
- Golem
- Sandslash


### Lt. Surge — approved roster and tuning

**Status:** **CLOSED**.

This decision uses only the persisted A-013 user-supplied canon research pool. Raichu remains Lt. Surge's ace and signature companion in both stages; no B8 staging change is required.

**First battle**
- Pikachu Lv.25 — ThunderShock / Quick Attack / Double Team / Thunder Wave; no held item.
- Voltorb Lv.26 — Shock Wave / Tackle / SonicBoom / Screech; no held item.
- Raichu Lv.30 — Shock Wave / Mega Punch / Slam / Thunder Wave; Sitrus Berry; ace/signature.

**Rematch**
- Pikachu Lv.62 — Thunderbolt / Iron Tail / Quick Attack / Double Team; no held item.
- Electrode Lv.64 — Thunderbolt / Rollout / Light Screen / Explosion; no held item.
- Magneton Lv.65 — Thunderbolt / Tri Attack / Thunder Wave / Metal Sound; no held item.
- Manectric Lv.66 — Thunderbolt / Bite / Thunder Wave / Roar; no held item.
- Electabuzz Lv.67 — Thunderbolt / ThunderPunch / Brick Break / Light Screen; no held item.
- Raichu Lv.69 — Thunder / Thunderbolt / Mega Punch / Body Slam; Magnet; ace/signature.

**Held-item policy**
- First battle: only Raichu holds Sitrus Berry.
- Rematch: only Raichu holds Magnet.

**Legality**
- All approved moves are legal through the existing project level-up / TM-HM / tutor / pre-evolution lineage rules.
- No trainer-only move exception is required.
- No global learnset, species, move, save, staging, or link/trade structure change is approved by this microblock.


### Lt. Surge closure evidence

- Final feature HEAD: `2bb74e404511e3e4b04a29d283c99b6d23a72e9d`.
- Full Gameplay Core **#639**: **SUCCESS**.
- Merged to `master` as `27dc2ff8a99fb5d9c5135ef39e02670b2ca08196`.
- Post-integration Full Gameplay Core **#640** on that exact master SHA: **SUCCESS**.
- Lt. Surge roster/tuning status: **CLOSED**.
- Final first battle: Pikachu Lv.25 / Voltorb Lv.26 / Raichu Lv.30; only Raichu holds Sitrus Berry.
- Final rematch: Pikachu Lv.62 / Electrode Lv.64 / Magneton Lv.65 / Manectric Lv.66 / Electabuzz Lv.67 / Raichu Lv.69; only Raichu holds Magnet.
- Raichu remains ace/signature in both stages.
- No trainer-only move exception was required.
- Do not begin Erika until explicitly requested by the user.


### A-013 curve-audit baseline and Lt. Surge third-pass amendment

**Status:** **CLOSED**.

The Gym Leader pass now carries a transversal progression audit in addition to canon/identity review. For each remaining first encounter, compare against the already approved leaders using:
- first-battle Kanto-only species restriction;
- roster size and evolutionary stages;
- levels and actual trainer IVs (`.iv * 31 / 255`);
- held items and trainer bag healing;
- move power/category, status pressure, recovery and speed;
- practical counters available to the player before the Gym;
- comparison to vanilla FireRed/LeafGreen and to adjacent Full leaders;
- continuity from first encounter into rematch;
- runtime feel remains a later acceptance layer and is not replaced by static analysis.

This baseline is intentionally reusable for Koga, Sabrina, Blaine and Giovanni. Their current roster sizes are not frozen by this note: later approved changes must be re-evaluated against the whole curve rather than assuming the current 4/4/5/6 pattern remains final.

**Lt. Surge third-pass change**
- The previous Lt. Surge closure remains historical evidence for the prior approved version.
- First battle gains a deliberately modest Kanto Magnemite at Lv.24: ThunderShock / Tackle / Supersonic / Metal Sound; no held item.
- Final first-battle order becomes Magnemite 24 / Pikachu 25 / Voltorb 26 / Raichu 30.
- Pikachu, Voltorb and Raichu retain their already approved sets/items.
- Raichu remains the unique ace/signature and the only first-battle held-item user (Sitrus Berry).
- Rematch remains unchanged: Pikachu 62 / Electrode 64 / Magneton 65 / Manectric 66 / Electabuzz 67 / Raichu 69.
- Magnemite -> Magneton is an approved evolutionary-continuity inference for Full; it is not represented as a direct Kanto ownership claim from the research pool.
- No trainer-only legality exception, global learnset change, save/link change or staging change is required.


### Lt. Surge third-pass closure evidence

- Feature HEAD: `32163f2677e4012032cce1070165b103f64a2ca5`.
- Full Gameplay Core **#642**: **SUCCESS**.
- Merged to `master` as `fb9bf7caec094b451cd6bb61b1752a142adb4d78`.
- Post-integration Full Gameplay Core **#643** on that exact master SHA: **SUCCESS**.
- Third-pass curve status: **CLOSED**.
- Final first encounter: Magnemite Lv.24 / Pikachu Lv.25 / Voltorb Lv.26 / Raichu Lv.30.
- Rematch is unchanged from the prior approved Surge closure.
- Raichu remains ace/signature and the only held-item user in the first encounter.

### Erika curve/identity amendment — approved target

**Status:** APPROVED / IMPLEMENTED / VALIDATED / CI-GREEN / CLOSED.

The transversal curve audit approves the following target while preserving the rule that first Gym encounters use Kanto species only.

**First battle**
- Oddish Lv.29 — Absorb / Acid / PoisonPowder / Stun Spore; no held item.
- Victreebel Lv.31 — Giga Drain / Acid / PoisonPowder / Sleep Powder; no held item.
- Tangela Lv.33 — Giga Drain / Bind / Stun Spore / Growth; no held item.
- Gloom Lv.35 — Petal Dance / Acid / PoisonPowder / Sleep Powder; Sitrus Berry; ace/signature.

**Rematch**
- Tangela Lv.62 — Giga Drain / Tickle / PoisonPowder / Sleep Powder; no held item.
- Jumpluff Lv.63 — Giga Drain / Leech Seed / Sleep Powder / Sunny Day; no held item.
- Bellossom Lv.64 — SolarBeam / Petal Dance / Synthesis / Sunny Day; no held item.
- Cradily Lv.65 — Rock Slide / Giga Drain / Confuse Ray / Recover; no held item.
- Victreebel Lv.66 — Giga Drain / Sludge Bomb / Razor Leaf / PoisonPowder; no held item.
- Vileplume Lv.69 — SolarBeam / Sludge Bomb / Synthesis / Sunny Day; Miracle Seed; ace/signature.

**Identity / continuity**
- Oddish -> Bellossom is an approved implied progression for one line.
- First-battle Gloom -> rematch Vileplume is the approved ace/signature progression.
- Because Vileplume is a final evolutionary stage, it must use the normal rematch trainer-IV tier rather than the prior max-IV compensation that existed solely to justify an unevolved Gloom ace.
- The prior Gloom-rematch max-IV rule is superseded for Erika only; this is not a global ace-IV policy change.
- Rematch visual staging must show Vileplume beside Erika instead of Gloom.
- Held-item policy: only first-battle Gloom holds Sitrus Berry; only rematch Vileplume holds Miracle Seed.
- Roster-size progression for later Koga/Sabrina/Blaine/Giovanni remains open to future review; each change must be rechecked against the transversal curve baseline rather than assuming current roster sizes are permanent.


### Erika implementation notes

- First encounter keeps Gloom as the symbolic anime-priority ace with max trainer-IV compensation because it remains an intermediate stage.
- Tangela Lv.33 Stun Spore is the only newly required trainer-only legality exception in this Erika microblock; it is scoped to Erika/Tangela/Lv.33 and does not change global learnsets.
- Rematch Vileplume Lv.69 uses `.iv = 214`, the normal Erika rematch tier (about 26/31 actual IVs), replacing the prior `.iv = 255` compensation that existed only for unevolved Gloom.
- The rematch contains one Vileplume, at Lv.69; the previous Lv.66 Vileplume slot is replaced by Cradily Lv.65 and Victreebel advances to Lv.66.
- Celadon Gym staging remains Gloom through the story state and changes to Vileplume for postgame/rematch eligibility through `VAR_OBJ_GFX_ID_2`.
- Vileplume reuses its existing 32x32 Pokémon icon and icon palette 0 through the established B8 inanimate-object architecture; no new art asset, species ID, save data or link structure is introduced.
- Erika keeps her existing two Super Potions; reducing trainer-bag healing was analyzed but was not part of the approved change.


### Erika closure evidence

- Feature HEAD: `9e0e105c36fa1e964bd21a879b6c892c9ff6cd7f`.
- Full Gameplay Core **#649: SUCCESS** on that exact feature HEAD.
- PR #24 merged the exact green feature to `master` as `541a49b56b84bc71f5e00ba9dcf976759968bbaf`.
- Full Gameplay Core **#650: SUCCESS** on that exact integrated master SHA.
- Full Gameplay Core #647 and #648 failed only because `tools/validate_b3_global_ace_identity.py` still encoded superseded Erika Gloom-rematch/max-IV and old ace-moveset expectations. Validator-only commits `dda4848` and `9e0e105` corrected those stale expectations; no gameplay rollback or unrelated change was required.
- Erika roster/curve/staging microblock is therefore **CLOSED**.


## A-014 — CI workflow resilience and documentation-only policy

**Date:** 2026-10-01
**Status:** APPROVED / IMPLEMENTED / VALIDATED / CI-GREEN / CLOSED

### Decision

- Full Gameplay Core uses the explicit GitHub-hosted runner `ubuntu-24.04` instead of `ubuntu-latest`.
- ARM/libpng dependencies remain installed by the workflow; transient APT/mirror failures use conservative retry support.
- No arbitrary dependency-install timeout is added.
- Full Gameplay Core is not triggered when a push or pull request changes only `docs/**` and/or Markdown files.
- If a change mixes documentation with any technical file, the normal Full Gameplay Core gate still applies.
- Workflow/build/validator changes themselves remain technical changes and require the full gate.
- A documentation-only continuity commit does not invalidate the exact-head CI evidence of the immediately preceding gameplay commit when the diff is verified as documentation-only.
- Pull requests remain an integration-control mechanism; they are not a substitute for the Actions runner and must not be created solely to evade runner failures.

### Rationale

Full Gameplay Core #651 on documentation-only HEAD `5e39aec` stalled in dependency installation before compilation or project validation, while the integrated Erika gameplay HEAD `541a49b` had already passed #650. The change reduces unnecessary heavy CI work without weakening technical gates and makes transient runner/mirror handling more robust.

### Closure evidence

- Feature HEAD: `cfebaa25b6c02153f7c2a694b245854d679670b3`.
- Full Gameplay Core **#652: SUCCESS** on that exact feature HEAD.
- PR #25 merged to `master` as `f1e5da264e4791d8c023e596f64dfcb583a95a28`.
- Full Gameplay Core **#653: SUCCESS** on that exact integrated master SHA.
- No gameplay, ROM data, validators, save/link structures or assets changed in this microblock.
- A-014 is therefore **CLOSED**.


### Koga curve/identity amendment — approved target

**Status:** APPROVED / IMPLEMENTED ON FEATURE BRANCH / VALIDATION PENDING.

The transversal leader pass approves Koga with anime-priority Golbat identity in the first encounter and Crobat as its evolved rematch ace.

**First battle**
- Koffing Lv.38 — Self-Destruct / Sludge / Smokescreen / Toxic; no held item.
- Venomoth Lv.39 — Silver Wind / Sleep Powder / Stun Spore / Toxic; no held item.
- Muk Lv.40 — Sludge / Minimize / Acid Armor / Toxic; no held item.
- Weezing Lv.42 — Sludge / Haze / Smokescreen / Toxic; no held item.
- Golbat Lv.44 — Sludge Bomb / Wing Attack / Bite / Toxic; Sharp Beak; ace/signature.

**Rematch**
- Ariados Lv.64 — Sludge Bomb / Psychic / Spider Web / Toxic; no held item.
- Forretress Lv.65 — Rapid Spin / Spikes / Toxic / Explosion; no held item.
- Venomoth Lv.66 — Psychic / Silver Wind / Giga Drain / Sleep Powder; no held item.
- Muk Lv.67 — Sludge Bomb / Body Slam / Acid Armor / Toxic; no held item.
- Weezing Lv.69 — Sludge Bomb / Flamethrower / Toxic / Haze; no held item.
- Crobat Lv.71 — Sludge Bomb / Aerial Ace / Double Team / Toxic; Sharp Beak; ace/signature.

**Identity / progression**
- First-battle Golbat remains the anime-priority symbolic ace and keeps max trainer-IV compensation (`.iv = 255`) because it is an intermediate evolutionary stage.
- Golbat -> Crobat is the approved ace/signature progression into the rematch.
- Weezing remains the second-strongest thematic pillar rather than replacing Golbat/Crobat as ace.
- Only Golbat/Crobat hold an item; Forretress Focus Band and Muk Leftovers are removed from the rematch.
- Koga keeps two Hyper Potions in the first battle and two Full Restores in the rematch.
- Crobat's approved rematch set explicitly retains Double Team.
- Fuchsia Gym adds two non-interactive Item Ball decoys as visual stand-ins for Koga's Voltorb-disguised-as-Poke-Ball trap identity. They do not trigger battle, rewards, flags or scripts.
- The separate retrospective review of leader trainer-bag items is out of scope for this Koga microblock.
