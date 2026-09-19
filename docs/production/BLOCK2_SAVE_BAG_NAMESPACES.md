# Production Block 2 — Full save header and persistent namespaces

## Approved scope after amendment A-002

Block 2 now implements only the persistent infrastructure needed by later Full events while preserving vanilla bag behavior.

- SaveBlock1 remains exactly `0x3D68`.
- The normal-items pocket remains vanilla: **42 slots**.
- `0x348C..0x361B` remains `unused_348C[400]`; it is not used by the bag.
- `0x3D24..0x3D33` becomes the 16-byte Full header: magic `RFFL`, `schemaVersion = 1`, remaining bytes reserved.
- Persistent Full flags remain reserved at `0x8C3..0x8E2`.
- Persistent Full vars remain reserved at `0x408C..0x409B`.
- A valid save without the Full magic is treated as schema 0: only the 16-byte Full header is initialized. Standard FireRed fields, including all bag data, remain untouched.

## Namespace assignments

Flags:
- 0x8C3 FLAG_FULL_DOJO_CHOSE_HITMONLEE
- 0x8C4 FLAG_FULL_DOJO_SECOND_REWARD
- 0x8C5 FLAG_FULL_ZAPDOS_KO_PENDING
- 0x8C6 FLAG_FULL_ARTICUNO_KO_PENDING
- 0x8C7 FLAG_FULL_MOLTRES_KO_PENDING
- 0x8C8 FLAG_FULL_MEWTWO_KO_PENDING
- 0x8C9 FLAG_FULL_MEW_CAUGHT
- 0x8CA FLAG_FULL_MEW_KO_PENDING
- 0x8CB FLAG_FULL_CELEBI_CAUGHT
- 0x8CC FLAG_FULL_CELEBI_KO_PENDING

Vars:
- 0x408C VAR_FULL_MYSTIC_QUEST
- 0x408D VAR_FULL_AURORA_QUEST
- 0x408E VAR_FULL_MEW_QUEST
- 0x408F VAR_FULL_CELEBI_QUEST
- 0x4090 VAR_FULL_ROAMER_SEQUENCE

The rest of both namespaces remains reserved.

## Runtime acceptance

MyBoy QA for this reduced block checks:
1. normal boot/new game;
2. vanilla Bag behavior remains normal;
3. in-game save succeeds;
4. fully close MyBoy;
5. reopen and Continue;
6. resumed game and Bag remain normal.

The removed 142-slot implementation and its failed black-screen QA are historical evidence only and are not production requirements.
