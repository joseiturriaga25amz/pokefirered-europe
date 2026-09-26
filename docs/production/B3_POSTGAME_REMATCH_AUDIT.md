# B3 Postgame / Rematch Audit

**Date:** 2026-09-26
**Branch:** `feature/b3-postgame-rematch-identity`

## B3.1 — Unlock and identity

- All eight Gym Leader rematches unlock from `FLAG_SYS_GAME_CLEAR` (first Hall of Fame), not National Dex.
- Giovanni's postgame Gym reappearance follows the same rule.
- Rematches remain repeatable through the existing dedicated trainer-flag reset.
- Each leader now has a unique offer / intro / defeat / post-battle dialogue set.
- `validate_b3_rematch_identity.py` gates these requirements.

## Rematch progression snapshot

Gym rematch ace progression:
- Brock 66
- Misty 67
- Lt. Surge 69
- Erika 69
- Koga 71
- Sabrina 72
- Blaine 73
- Giovanni 74

This forms an optional bridge from the first Champion (ace 69) into the Network-Machine-gated strengthened League (Lorelei ace 79 through Champion ace 85), without forcing global EXP inflation.

Previously approved rematch roster identity adjustments are already present: Brock/Vulpix, Misty/Luvdisc+Togetic, single Electrode for Surge, second Vileplume for Erika, Sabrina/Gengar, and Giovanni's approved roster.

## B3.2 — League rematch refinement

Applied the previously approved Lorelei rematch amendment:
- Lapras 79: Ice Beam / Surf / Thunderbolt / **Confuse Ray**
- Body Slam is removed from the rematch set.

This restores Lapras's control identity while retaining the stronger rematch coverage package.
