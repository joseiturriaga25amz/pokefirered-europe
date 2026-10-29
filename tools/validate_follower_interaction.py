#!/usr/bin/env python3
"""Source-only B10 A-button/friendship contract: no ROM, compiler or asset access."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def body(src, signature):
    start = src.index(signature + "\n{")
    opening = src.index("{", start)
    depth = 0
    for pos in range(opening, len(src)):
        if src[pos] == "{":
            depth += 1
        elif src[pos] == "}":
            depth -= 1
            if depth == 0:
                return src[start:pos + 1]
    raise AssertionError("Unterminated function: " + signature)

def errors(follower, avatar, events, script):
    issues = []
    def require(predicate, message):
        if not predicate:
            issues.append(message)

    eligible = body(follower, "static u16 GetEligiblePrototypeFollowerSpecies(bool8 *isShiny)")
    interaction = body(follower, "const u8 *FullFollower_GetFriendshipInteractionScript(void)")
    route = body(avatar, "static const u8 *GetInteractedObjectEventScript(struct MapPosition *position, u8 metatileBehavior, u8 direction)")
    setup = body(avatar, "static bool8 TryStartInteractionScript(struct MapPosition *position, u16 metatileBehavior, u8 direction)")
    begin = body(follower, "void FullFollower_BeginSafeDialogue(const u8 *script)")
    clear = body(follower, "void FullFollower_ClearSafeDialogue(void)")
    safe = body(follower, "static bool8 IsSafeFollowerDialogueScript(const u8 *script)")
    refresh = body(follower, "static void RefreshFollower(void)")
    run = body(script, "bool8 ScriptContext_RunScript(void)")
    init = body(script, "void ScriptContext_Init(void)")
    set_script = body(script, "void ScriptContext_SetupScript(const u8 *ptr)")

    require("for (i = 0; i < PARTY_SIZE; i++)" in eligible
            and "species != SPECIES_NONE && hp != 0 && !isEgg" in eligible
            and "GetPrototypeFollowerGraphicsId(species) == 0xFF" in eligible
            and "IsMonShiny(&gPlayerParty[i])" in eligible,
            "eligible lead must be first healthy, non-Egg, supported party mon")
    require("GetEligiblePrototypeFollowerSpecies(&isShiny)" in interaction
            and "if (monSpecies != species)" in interaction
            and "GetMonData(mon, MON_DATA_NICKNAME, gStringVar1)" in interaction
            and "GetMonData(mon, MON_DATA_FRIENDSHIP)" in interaction
            and interaction.index("MON_DATA_NICKNAME") < interaction.index("MON_DATA_FRIENDSHIP"),
            "nickname and friendship must come from the same eligible mon")
    require("!sFollowerEnabled || species == SPECIES_NONE" in interaction
            and "species != sFollowerSpecies || isShiny != sFollowerIsShiny" in interaction,
            "stale, missing or disabled follower must not receive dialogue")
    require("SetMonData(" not in interaction and "AdjustFriendship(" not in interaction,
            "interaction must not mutate Pokemon data")

    refs = [int(x) for x in re.findall(r"EventScript_FullFollowerFriendship(\d+)", interaction)]
    require(refs == list(range(7)), "friendship pointer table order must be 0..6")
    conditions = [(op, int(n), int(tier)) for op, n, tier in re.findall(
        r"(?:else\s+)?if\s*\(\s*friendship\s*(==|>=|>|<=|<)\s*(\d+)\s*\)\s*tier\s*=\s*(\d+)\s*;",
        interaction)]
    require(len(conditions) == 6 and re.search(r"\belse\s+tier\s*=\s*0\s*;", interaction),
            "unrecognized friendship conditional chain")
    def actual(value):
        for op, threshold, tier in conditions:
            if {"==": value == threshold, ">=": value >= threshold,
                ">": value > threshold, "<": value < threshold,
                "<=": value <= threshold}[op]:
                return tier
        return 0
    def expected(value):
        return (6 if value == 255 else 5 if value >= 200 else
                4 if value >= 150 else 3 if value >= 100 else
                2 if value >= 50 else 1 if value > 0 else 0)
    require(all(actual(value) == expected(value) for value in range(256)),
            "friendship mapping differs from seven approved 0..255 ranges")

    for index in range(7):
        block = re.search(rf"(?m)^EventScript_FullFollowerFriendship{index}::\s*\n((?:[ \t]+[^\n]*\n)+)", events)
        expected_lines = ["lockall", f"msgbox Text_FullFollowerFriendship{index}",
                          "releaseall", "end"]
        require(block is not None and [line.strip() for line in block.group(1).splitlines()] == expected_lines,
                f"unsafe or missing friendship script {index}")
        texts = re.findall(
            rf'(?m)^Text_FullFollowerFriendship{index}::\s*\n[ \t]+\.string "([^"]+)"',
            events)
        require(len(texts) == 2 and all("{STR_VAR_1}" in msg and msg.endswith("$") for msg in texts),
                f"missing ES/EN nickname text for tier {index}")

    require(route.index("return FullFollower_GetFriendshipInteractionScript();")
            < route.index("GetObjectEventScriptPointerByObjectEventId(objectEventId)"),
            "follower A route must precede ordinary NPC script lookup")
    for guard in ("OBJ_EVENT_ID_FULL_FOLLOWER", "!MetatileBehavior_IsCounter(metatileBehavior)",
                  "!QL_IS_PLAYBACK_STATE", "!InUnionRoom()"):
        require(guard in route, "A route missing guard: " + guard)
    require("ScriptContext_SetupScript(script);\n    FullFollower_BeginSafeDialogue(script);" in setup,
            "safe dialogue must be offered after script setup")
    require("FindFollowerObject() != NULL" in begin
            and "!QL_IS_PLAYBACK_STATE" in begin
            and "!gPaletteFade.active" in begin
            and "IsSafeFollowerDialogueScript(script)" in begin,
            "script hold must only apply to safe, existing follower")
    require("FOLLOWER_MAX_SAFE_MESSAGES" in safe
            and "FOLLOWER_CMD_LOADWORD" in safe
            and "FOLLOWER_CMD_CALLSTD" in safe
            and "FOLLOWER_CMD_END" in safe
            and "address > 0x09FFFFC0" in safe,
            "safe script bounded grammar not recognized")
    require("sFollowerSafeDialogue = FALSE;" in clear
            and "FullFollower_ClearSafeDialogue();" in init
            and "FullFollower_ClearSafeDialogue();" in run
            and "FullFollower_ClearSafeDialogue();" in set_script
            and "sFollowerSafeDialogue = FALSE;" in refresh,
            "script exit/replacement or field-unlock cleanup missing")
    return issues

def main():
    paths = ["src/full_follower.c", "src/field_control_avatar.c",
             "data/event_scripts.s", "src/script.c"]
    original = [(ROOT / path).read_text(encoding="utf-8") for path in paths]
    failures = errors(*original)
    for failure in failures:
        print("FAIL:", failure)
    if failures:
        return 1
    # Mutation tests prove that source regressions actually fail this validator.
    mutations = [
        (0, "friendship >= 200", "friendship >= 201"),
        (0, "MON_DATA_FRIENDSHIP", "MON_DATA_LEVEL"),
        (1, "!InUnionRoom()", "InUnionRoom()"),
        (2, "msgbox Text_FullFollowerFriendship3", "giveitem ITEM_POTION"),
        (3, "FullFollower_ClearSafeDialogue();", "/* reset removed */"),
    ]
    for path_index, before, after in mutations:
        mutated = list(original)
        assert before in mutated[path_index], (path_index, before)
        mutated[path_index] = mutated[path_index].replace(before, after, 1)
        assert errors(*mutated), "validator did not reject mutation: " + before
    print("B10 friendship/A-button semantic source contract PASS (256 values, 7 scripts, 5 mutations)")
    print("Source-only validation; ROM compilation and MyBoy runtime NOT EXECUTED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
