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
