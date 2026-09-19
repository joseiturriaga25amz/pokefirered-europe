# Production Block 2 — Full save infrastructure, bag extension and namespaces

## Frozen scope

This block implements the frozen save architecture without changing `sizeof(struct SaveBlock1)`:

- SaveBlock1 remains exactly `0x3D68`.
- `0x348C..0x361B` becomes 100 extra `ItemSlot` entries for the normal-items pocket.
- Logical normal-items capacity is 42 + 100 = 142 slots.
- `0x3D24..0x3D33` becomes the 16-byte Full header: magic `RFFL`, `schemaVersion = 1`, remaining bytes reserved.
- Persistent Full flags are reserved at `0x8C3..0x8E2`.
- Persistent Full vars are reserved at `0x408C..0x409B`.
- A save without the Full magic is treated as schema 0: extra item slots must be initialized empty and the Full header written without altering standard save fields.

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

## Implementation sequence

1. Map the reserved bytes and namespaces while proving SaveBlock1 remains 0x3D68.
2. Implement Full header initialization/import path.
3. Implement 142-slot logical normal-items pocket without shifting vanilla SaveBlock1 fields.
4. Validate encryption/re-key, add/remove/sort, save/reload and vanilla-save import.
5. Build Spanish modern target and run MyBoy QA.

## User runtime QA handoff

The final MyBoy checklist for this block will explicitly cover:
- importing/continuing a pre-Full Spanish save;
- new-game save creation;
- ordinary item acquisition/use/toss/sort;
- filling beyond the original 42-slot normal-items limit;
- save -> fully close MyBoy -> reopen -> Continue;
- verifying items beyond slot 42 persist;
- checking that key items, Poké Balls, TMs/HMs and berries remain unaffected.

Block 2 is not complete until those checks pass.
