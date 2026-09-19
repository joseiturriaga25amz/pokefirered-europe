# User Runtime QA Handoff Standard

This document defines how every production block must be handed to the user for runtime validation in MyBoy.

## Required handoff format

Every user-run QA block must state:

1. **Purpose** — what the block changed and what the runtime test is meant to catch.
2. **Exact build** — commit/build identifier being tested.
3. **Starting state** — new game, existing save, location, required items/Pokémon, or other prerequisites.
4. **Exact steps** — numbered actions in the order the user should perform them.
5. **Expected result** — what should be visible or happen after each important step.
6. **Fail conditions** — concrete symptoms that mean the user should stop and report immediately.
7. **Evidence requested** — screenshots/video only for the screens or moments relevant to the block.
8. **Stop point** — where the user should stop so they do not spend time testing unrelated content.
9. **Result status** — PASS, FAIL, or BLOCKED. Never infer PASS from compilation alone.

## Scope rule

The user must not be asked to "play normally and see if anything looks wrong" when a narrower checklist can be provided. Runtime QA should be specific to the systems touched by the block, plus a small set of regression checks appropriate to the risk of those changes.

## Emulator

MyBoy is the required runtime QA environment per amendment A-001.
