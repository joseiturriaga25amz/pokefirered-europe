# Follower System Technical / Provenance Research

**Project:** Pokémon Rojo Fuego Full v1.0  
**Status:** research gate; follower is **not approved for integration** yet.  
**Primary reference inspected:** `monhacks/arrantemerald`, branch `followers-expanded-id`, commit `48ba7614fedeb5bc88ca5a0db57ea7a64bdac392`.  
**Full source baseline inspected:** `feature/full-gameplay-core` at `643ea9c0550b7aeb495919c1c1988af2677d237e`.

## 1. Decision authority

This document implements the research requirement in A-006 of `DECISION_AMENDMENTS.md`.

The accepted product target remains:

- party leader is the visual follower;
- follower is derived runtime state, never a second stored Pokémon;
- on/off support;
- automatic hide/reappear around incompatible transitions and scripted states;
- contextual interaction is cosmetic only;
- no new Pokémon/item IDs;
- no expansion of Pokémon, BoxPokemon, SaveBlock or link-serialized Pokémon data;
- MyBoy QA is mandatory before integration;
- follower must be removable if it destabilizes v1.0.

## 2. Upstream technical findings

### 2.1 The reference branch is not a small patch

`followers-expanded-id` is a long-lived Emerald branch and is hundreds of commits ahead of its original base. Its follower implementation reaches across:

- object-event movement;
- field/player control;
- overworld lifecycle;
- trainer sight;
- field effects;
- scripts;
- palettes/OAM;
- object-event graphics tables;
- follower text/interaction;
- map/script transition handling.

Therefore it must not be merged wholesale into FireRed Full.

### 2.2 “No object-event size growth” does not mean “no layout change”

In the inspected Emerald branch:

- `ObjectEventTemplate.graphicsId` is widened from 8 to 16 bits;
- `ObjectEvent.graphicsId` is widened from 8 to 16 bits;
- the `ObjectEvent` fields are repacked/reordered and the total structure remains `0x24`;
- the 16-bit graphics ID carries species/form metadata;
- follower shininess uses an existing bitfield area.

FireRed Full currently retains the vanilla-style 8-bit `graphicsId` layout.

**Conclusion:** copying the expanded-ID data layout into FireRed Full would introduce a broad runtime ABI/layout change even though the structure's total byte size could remain unchanged. That is unnecessary risk for Gen III/Link/Save goals.

### 2.3 Useful upstream concepts

The following ideas are technically useful as references, but their code is not to be copied verbatim unless licensing is later resolved:

- dynamically spawning one follower object;
- deriving the follower from the first eligible live, non-Egg party member;
- hiding/removing it when no eligible party member exists;
- re-evaluating follower identity after party changes;
- player-shadow movement state;
- temporary invisibility across incompatible avatar states;
- dynamic graphics/palette replacement;
- contextual interaction selected from species/type/status/map/weather/tile conditions;
- explicit handling of doors, ledges, warps, scripts and trainer-sight edge cases.

## 3. Provenance and redistribution findings

### 3.1 No repository-wide license grant found

At the inspected upstream commit, no root `LICENSE`, `COPYING` or equivalent repository-wide license was present. License files found under `tools/` apply to those tools, not automatically to the follower implementation or graphics.

**Policy for Full:** public availability on GitHub is not treated as permission to copy or redistribute upstream follower code.

### 3.2 Bulk follower sprites

The historical commit that added the original 386 follower sprites is:

`6692cd992f82e747ff308f7417b910df2d3c743c`

Its included extraction script states that it extracts HGSS follower spritesheets and identifies veekun as the sprite-pack source.

This establishes that the bulk graphics are derived from official HeartGold/SoulSilver artwork rather than original artwork authored and openly licensed by the repository maintainer.

Veekun's download page allows reuse of its collected/ripped files but also explicitly states that Nintendo made them and that veekun does not claim ownership.

**Conclusion:** this is useful provenance, but it is not a clear copyright license from the Pokémon rights holders. The 386-image bulk set is therefore **not cleared for import into Full** under a strict redistribution-rights test.

### 3.3 Later sprite replacements

Repository history contains later sprite replacements with individual credits (for example Jaizu, LarryTurbo, SonikkuA-DatH, andrian_timeswift, shikashipx and others).

Credit is not, by itself, a license grant. Each such asset would require its own provenance and permission/license verification before it could be called legally cleared.

### 3.4 Current Full-native Pokémon overworld assets

The FireRed Full repository already contains 42 Pokémon overworld PNGs in `graphics/object_events/pics/pokemon/`, including representative assets such as:

- Pikachu;
- Mew;
- Mewtwo;
- Articuno / Zapdos / Moltres;
- Suicune / Raikou / Entei;
- Lugia / Ho-Oh;
- Celebi;
- Snorlax;
- several ordinary Kanto species.

These are sufficient to validate follower mechanics without importing any external follower graphics.

This does **not** assert that Pokémon game assets are generally open-licensed; it only means the prototype can avoid adding a new third-party asset/provenance dependency.

## 4. FireRed-safe prototype architecture

The first prototype must deliberately avoid the upstream 16-bit graphics-ID architecture.

### P0 invariants

Do not change:

- `sizeof(struct ObjectEvent)`;
- field offsets inside `struct ObjectEvent`;
- `sizeof(struct ObjectEventTemplate)`;
- `ObjectEvent.graphicsId` width;
- `ObjectEventTemplate.graphicsId` width;
- `struct Pokemon`;
- `struct BoxPokemon`;
- SaveBlock sizes/offsets;
- link/trade Pokémon serialization;
- species, item, move or Poké Ball IDs.

### P1 follower identity

Use one runtime-only follower object with a reserved special local ID that does not collide with map NPC IDs, player, camera or RFU-reserved IDs.

The follower's species/appearance state should live in follower-specific **runtime state**, not in the persisted Pokémon structure and not encoded into the generic object-event `graphicsId`.

### P2 graphics indirection

For the prototype, expose only a small allow-list of existing Full-native overworld Pokémon assets.

Recommended approach:

1. reserve one normal 8-bit follower graphics ID;
2. when that graphics ID is resolved for the follower object, select the appropriate existing `ObjectEventGraphicsInfo` via a follower-specific runtime species selector;
3. leave the global generic object graphics ID namespace and struct layouts unchanged;
4. expand the table/asset layer only after mechanics pass.

This separates movement correctness from the future 386-asset problem.

### P3 initial species set

Use a deliberately small mechanically diverse set from existing assets:

- Pikachu — ordinary 32x32 walking case;
- Snorlax — large/heavy-looking boundary case if existing object graphics dimensions permit;
- Mew — floating/mythical case and also directly relevant to A-005;
- Suicune — legendary case;
- one ordinary bird Pokémon — movement/animation contrast.

Do not block the first technical prototype on complete species coverage.

### P4 party rule

Initial rule should match A-006 product intent while remaining deterministic:

- first conscious, non-Egg party Pokémon;
- if party slot 0 is an Egg/fainted, advance to the first eligible party member;
- if none is eligible, no follower is spawned;
- boxing/reordering/healing/fainting causes re-evaluation without persisting a duplicate Pokémon.

### P5 lifecycle

At minimum, prototype hooks must cover:

- map load;
- warp/door transition;
- party re-evaluation;
- bike;
- Surf;
- Fly/teleport-like transition;
- scripted player movement;
- trainer sight;
- battle enter/return;
- save/load;
- link-room / trade entry and exit.

Follower should be hidden or removed before a risky mode and recreated from party data afterward, rather than trying to persist follower object state through those systems.

## 5. Compatibility rationale

### Save

A runtime-derived follower with no new stored Pokémon and no SaveBlock expansion preserves the existing Full save architecture. A future optional on/off preference, if persisted, must use only an audited Full-owned flag/var/byte already reserved by the Full schema.

### Link / trade

Follower presentation must remain outside link-serialized Pokémon data. Link rooms should explicitly suppress the follower unless a later MyBoy test proves the presentation object harmless.

Full ↔ vanilla legal Pokémon trade remains governed by the existing Gen III structures and restrictions.

### Future Emerald Full

Keep follower **behavioral API** separate from FireRed's object-event implementation:

- get eligible follower Pokémon;
- should follower be visible;
- spawn/remove/refresh;
- select follower graphics;
- contextual interaction.

That permits a future Emerald Full implementation to use an Emerald-native graphics layer without forcing FireRed to adopt Emerald's expanded graphics-ID ABI.

## 6. Prototype QA gate

Follower remains outside production until a separate MyBoy prototype passes all of these:

1. clean boot/new game;
2. repeated outdoor map transitions;
3. doors and stairs;
4. ledges;
5. bike on/off;
6. Surf enter/exit;
7. Fly/warp;
8. trainer sight;
9. scripted movement/cutscene;
10. battle enter/return;
11. party reorder;
12. slot-0 fainted;
13. slot-0 Egg;
14. all party Pokémon fainted/ineligible;
15. deposit/withdraw leader;
16. evolution/form/appearance refresh where applicable;
17. save, close MyBoy, reload;
18. vanilla Spanish save import;
19. link-room entry/exit;
20. Full ↔ vanilla legal trade, then save/reload both sides;
21. palette/OAM stress and repeated transitions;
22. follower toggle on/off if persistence is implemented.

Any save corruption, link regression, softlock, black screen, persistent ghost object, object-event collision corruption or unrecoverable visual state is a release blocker and removes follower from v1.0 until repaired.

## 7. Current disposition

- **Research:** sufficient to begin an isolated prototype.
- **Upstream code:** reference only; no repository-wide license grant found.
- **HGSS/veekun bulk follower sprites:** provenance identified; redistribution rights not clearly granted by the rights holder; do not import as “legally cleared”.
- **Full-native overworld assets:** sufficient for first mechanics prototype.
- **16-bit expanded graphics IDs:** reject for the first FireRed prototype.
- **Production integration:** blocked pending isolated implementation + MyBoy QA.
