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
- **QOL-HM-002 — HMs as field licenses:** field actions require possession of the corresponding HM plus the original badge/narrative gate; no party Pokémon needs to know the move. HMs remain reusable teachable moves for battle, and an HM move learned by a Pokémon may be replaced/forgotten normally without the Move Deleter.
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
