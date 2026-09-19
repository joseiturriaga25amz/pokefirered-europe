# Production Log — Block 1: Baseline / Toolchain / Upstream fixes

Date: 2026-09-19
Branch: `feature/baseline-toolchain`
Frozen base: `e184c5cf898cd29efebd33bc1bfe5994277e21ab`

## Scope

Implements the first production block defined by the frozen preproduction specification:

- BASE-001 / BASE-002 / BASE-003: Spanish product base, pret as selective upstream, `firered_es_modern`.
- BASE-004: reproducible Spanish vanilla baseline.
- BASE-005: production branch governance and immutable baseline tag.
- BASE-006: selective ports of the post-freeze upstream fixes explicitly required by the specification.
- BUG-012: corrected `LOCALID_RUBY` placement in Mt. Ember.

## Baseline

- `compare_firered_es`: PASS on the frozen base.
- Expected SHA-1: `ab8f6bfe0ccdaf41188cd015c8c74c314d02296a`.
- Verified SHA-1: PASS.
- Immutable tag `baseline-spanish-vanilla` exists and points to `e184c5cf898cd29efebd33bc1bfe5994277e21ab`.

## Upstream ports

### Missing return / undefined behavior
Source reference: pret/pokefirered `70b76a15df8c6a6dd03d7a09e8f9eddd2e4dc29d`.

Applied to `src/battle_message.c` so `BattleStringExpandPlaceholdersToDisplayedString` returns the result of `BattleStringExpandPlaceholders`.

### latin_small / gbagfx
Source reference: pret/pokefirered `39c22794e688d813962f40645cf975a730ee89da`.

The upstream change could not be copied blindly because the European base contains separate EN/ES/IT/FR/DE Latin font assets. The port therefore preserves the European 16-column PNG source layout while generating true 8x16 half-width glyph data through the new `.hwlatfont` path.

Updated:
- `tools/gbagfx/font.c`
- `tools/gbagfx/font.h`
- `tools/gbagfx/main.c`
- `graphics_file_rules.mk`
- `src/text.c`
- `.gitignore`

All five small Latin variants use `.hwlatfont`; normal/male/female Latin fonts remain on the existing full-width `.latfont` path to minimize unrelated churn.

### Mt. Ember LOCALID_RUBY
Source reference: pret/pokefirered `537c71dfd36b83c9cdac8e4ed4a6721a6132d645`.

- Removed `LOCALID_RUBY` from the pushable boulder in `MtEmber_RubyPath_B3F`.
- Assigned `LOCALID_RUBY` to the actual Ruby object in `MtEmber_RubyPath_B5F`.

## CI / validation

Dedicated workflow: `.github/workflows/full-production-block1.yml`.

Results on the production branch:
- Spanish modern head build (`firered_es_modern`): PASS.
- Frozen Spanish vanilla baseline build/compare: PASS.
- Documented SHA-1 check: PASS.
- Static source audit: no old `latin_small*.latfont` references remain in the converted rule/data paths; five `.hwlatfont` rules and five runtime references are present.
- Mt. Ember source audit: B3F has no `LOCALID_RUBY`; B5F has exactly one.
- Missing-return source audit: corrected return is present.

Inherited upstream CI was adapted for the Full fork so feature changes compile rather than being rejected for no longer matching vanilla ROM hashes. The compatibility job builds FireRed/LeafGreen revision variants plus modern without byte-identity comparison.

## Open acceptance gate

QA-001 is satisfied by CI.

QA-002 is only partially satisfied by CI: the Spanish modern ROM compiles successfully, but the runtime smoke still requires booting the produced ROM, starting a game, and verifying in-game save/load.

Per production amendment A-001, **MyBoy is the primary emulator for this ordinary Android functional smoke**. mGBA is retained for QA cases that explicitly depend on it, especially later link/trade regression.

No merge to `master` is authorized until the MyBoy runtime smoke is completed.


## Runtime QA incident — MyBoy

The first MyBoy runtime smoke exposed a real rendering regression before merge: normal gameplay booted, but multiple UI strings and labels rendered with missing/corrupted glyphs in the bag, battle UI, move list, and party screen.

**Result:** FAIL. The user correctly stopped the test; no merge was performed.

Root cause: the initial multilingual `.hwlatfont` adaptation packed only 16 half-width glyphs per 256-pixel row and emitted an 8192-byte Spanish small-font asset. The actual small-font layout is 32 glyphs per row (8x16 each), requiring a 16384-byte asset. This truncated/misaligned the glyph table used by `DecompressGlyph_Small`.

Correction: restore 32-column half-width packing, correct the reverse conversion row count, and add a CI size guard for `latin_small_es.hwlatfont` before producing the MyBoy test artifact.

The runtime gate remains OPEN until the corrected build is retested successfully in MyBoy.


## Block 1 — exact MyBoy retest checklist

**Purpose:** verify the corrected Spanish small-font path and basic runtime integrity of the baseline/toolchain fixes before merge.

**Starting state:** use the freshly generated Block 1 ROM in MyBoy. Do not reuse the failed ROM build. A new game is preferred for this smoke.

| Check | Action | Expected result | Fail / stop condition |
|---|---|---|---|
| 1. Boot | Launch the ROM from a cold start | Nintendo/Game Freak/title flow displays normally | Freeze, black screen, corrupted title/UI |
| 2. New game text | Start a new game and advance through the opening dialogue/name flow | Spanish text is complete, legible, correctly spaced and accented | Missing letters, wrong glyphs, blank labels, garbled text |
| 3. Overworld | Gain control of the player and move/interact normally | Movement and dialogue work without visual corruption | Lockup, input failure, broken dialogue |
| 4. Party UI | Open Pokémon/party screen after obtaining the starter | Names, HP, level, menu labels and text render correctly | Missing/corrupt text or UI labels |
| 5. Battle UI | Trigger the first rival battle | Pokémon names, HP boxes, battle messages and command text render correctly | Blank/corrupt text, broken battle flow |
| 6. Move list | Open the move-selection screen during battle | Move names, PP and type labels render correctly | Missing glyphs/labels or corrupted move text |
| 7. Bag UI | Open the Bag once available | Pocket title, item name, description and commands render correctly | Missing/corrupt text, broken navigation |
| 8. Save | Save through the in-game menu | Save completes normally with no error | Save fails, hangs, corrupt message |
| 9. Cold reload | Fully close MyBoy, reopen the ROM and choose Continue | Save is detected and loads to the correct state | No Continue option, load failure, corruption |
| 10. Short regression | Move, open party and bag again after loading | Same UI remains correct after reload | Any post-load text/UI regression |

**Evidence requested:** screenshots of (a) opening dialogue, (b) party screen, (c) battle move-selection screen, (d) bag, and (e) Continue after cold reload.

**Stop point:** once check 10 passes. Do not progress further for Block 1.

**PASS rule:** all 10 checks pass on the corrected build. Any one failure keeps Block 1 open.


## Handoff hardening after second MyBoy failure

The second MyBoy smoke again failed on compact UI text while boot/save/load and normal dialogue remained functional. Before issuing another user build, the CI gate was strengthened so that all four Spanish Latin font assets used at runtime (small, normal, male, female) must match the frozen vanilla baseline byte-for-byte, and Spanish runtime references must remain on the legacy European `.latfont` format. This is a pre-handoff invariant for Block 1, not merely a post-failure note.


## MyBoy Revision 3 visual retest

**Build:** SHA-1 `9904e96ac13c78b3a295d923f8325d2904334554`

User-provided screenshots confirm that the previously corrupted compact Spanish text now renders correctly in:
- Bag item/action UI.
- Party screen.
- Battle HUD.
- Battle command menu.
- Move-selection screen including move names, PP and type.

**Visual regression status:** PASS.

The Block 1 runtime gate remains pending only until save -> fully close MyBoy -> reopen -> Continue is explicitly confirmed on this exact Revision 3 build.


## Final MyBoy runtime result — PASS

**Build tested:** Revision 3, SHA-1 `9904e96ac13c78b3a295d923f8325d2904334554`

The user explicitly confirmed on MyBoy that:
- the game boots normally;
- compact Spanish UI text renders correctly in Bag, Party, battle HUD, battle command menu and move-selection UI;
- in-game saving succeeds;
- MyBoy can be fully closed and the same save can be reopened with Continue;
- gameplay resumes successfully from the saved state.

**Block 1 runtime smoke:** PASS.

Together with the clean Spanish modern build, frozen vanilla SHA verification, upstream compatibility build, localized font byte-for-byte baseline gates and static source audits, the Block 1 acceptance gate is satisfied.
