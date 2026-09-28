# B3 Global Canon / Ace Audit — Checkpoint

Date: 2026-09-28
Branch at checkpoint: `feature/b3-global-canon-audit-v3`

## Purpose
Persistent resume point for the B3 global trainer canon/ace audit. This file is the authoritative checkpoint if chat history is unavailable.

## Completed and user-approved

### Gary / Blue rematch — 6/6
- Nidoqueen 80: Earthquake / Hyper Beam / Ice Beam / Thunderbolt.
  - Superpower -> Hyper Beam approved.
- Magmar 80: Flamethrower / Fire Blast / Brick Break / Psychic.
  - Confuse Ray -> Psychic approved.
- Golem 81: unchanged.
- Scizor 82: unchanged.
- Arcanine 83: unchanged; Bite explicitly retained over Aerial Ace.
- Blastoise 85 ★: unchanged.

### Intermediate-stage ace exceptions
- Erika Gloom:
  - First: Petal Dance / Sleep Powder / Moonlight / Acid.
  - Rematch: Solar Beam / Sludge Bomb / Sleep Powder / Sunny Day.
  - .iv = 255 in both ace appearances.
- Koga Golbat / Crobat:
  - Golbat 46 ★: Wing Attack / Bite / Confuse Ray / Screech.
  - Toxic -> Screech approved.
  - Golbat keeps .iv = 255 + Sharp Beak.
  - Crobat 71 ★: Aerial Ace / Poison Fang / Bite / Confuse Ray, unchanged.
- Sabrina Kadabra:
  - First and rematch: Psychic / Calm Mind / Recover / Reflect.
  - .iv = 255 + Twisted Spoon in both ace appearances.

### Remaining ace progressions
- Brock: Onix 17 ★ -> Steelix 66 ★, unchanged.
- Misty: Starmie 26 ★ -> Starmie 67 ★, unchanged.
- Lt. Surge: Raichu 30 ★ -> Raichu 69 ★, unchanged.
- Blaine:
  - First Magmar 52 ★ unchanged.
  - Rematch Magmar 73 ★ finalized as Flamethrower / Fire Blast / Brick Break / Confuse Ray.
  - Fire Punch -> Flamethrower approved.
- Giovanni: Rhydon 56 ★ -> Rhydon 74 ★, unchanged.
  - Mewtwo remains a separate narrative superweapon and does not displace Rhydon as combat ace.
- Lorelei: Lapras 61 ★ -> Lapras 79 ★, unchanged.
- Bruno: Machamp 62 ★ -> Machamp 80 ★, unchanged.
- Agatha: Gengar 63 ★ -> Gengar 81 ★, unchanged.
- Lance: Dragonite 65 ★ -> Dragonite 82 ★, unchanged.
  - Red Gyarados retained as a separate canonical signature piece.
  - Salamence retained in rematch without displacing Dragonite as ace.

## Critical implementation state
- Lance trainer Gyarados is forced shiny only in Lance's first League and rematch trainer battles through the scoped runtime override.
- Lance rematch includes Salamence.
- Bruno rematch uses Hariyama instead of Hitmontop while retaining Onix + Steelix + Hitmonchan + Hitmonlee + Machamp.
- Agatha rematch includes Sableye as an explicit Full thematic addition, not falsely canonical.
- Global ace identity validation and audited-data blob locking remain part of the B3 validation system.

## Resume point
The manual ace/moveset transversal pass through Lance is complete.

Next steps:
1. Run a final repository consistency / transversal audit.
2. Run current-head validators and CI.
3. Reconcile any stale documentation or blob locks.
4. Create/merge the next production checkpoint.
5. Continue with the next B3 block only after that checkpoint is verified.

This file exists specifically so the project can resume without depending on chat history.
