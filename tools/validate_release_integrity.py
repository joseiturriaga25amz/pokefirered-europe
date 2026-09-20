#!/usr/bin/env python3
"""Second-pass release-integrity meta-audit for the Spanish Full RC.

This validator does not prove gameplay behavior. It verifies that the CI and
static validators are checking the files that actually feed firered_es_modern
and that high-risk second-pass coverage cannot silently drift back to generic
or stale paths.
"""

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def git_blob_sha(path):
    data = (ROOT / path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(text, token, label):
    assert token in text, f"{label}: missing {token}"


def main():
    workflow = read(".github/workflows/full-gameplay-core.yml")
    require(workflow, "make -j2 firered_es_modern", "target")
    require(workflow, "branches:\n      - feature/full-gameplay-core", "branch")

    # RC-F039: the RC handoff must rebuild against the exact frozen Spanish
    # baseline commit, and continuity must name the same immutable commit.
    baseline_sha = "e184c5cf898cd29efebd33bc1bfe5994277e21ab"
    require(workflow, f"ref: {baseline_sha}", "RC frozen baseline")
    continuity = read("docs/production/PROJECT_CONTINUITY.md")
    require(continuity, baseline_sha, "continuity frozen baseline")
    assert "e184c5cf898cd29efbd33bc1bfe5994277e21ab" not in workflow
    assert "e184c5cf898cd29efbd33bc1bfe5994277e21ab" not in continuity

    validators = (
        "tools/validate_audited_data_blobs.py",
        "tools/validate_full_move_metadata.py",
        "tools/validate_full_league_rosters.py",
        "tools/validate_requirement_reconciliation.py",
        "tools/validate_rc_freeze.py",
        "tools/validate_full_trainer_sets.py",
        "tools/validate_full_obtainability.py",
        "tools/validate_full_save_namespace.py",
        "tools/validate_full_event_states.py",
        "tools/validate_frozen_bugfixes.py",
        "tools/validate_release_integrity.py",
    )
    for path in validators:
        require(workflow, path, "workflow coverage")

    # Spanish target: validators and CI must inspect the actual language-specific
    # scripts instead of generic siblings that can diverge.
    assert "data/scripts/hall_of_fame.inc" not in workflow
    require(workflow, "data/scripts/spanish/hall_of_fame.inc", "workflow Hall of Fame")

    event_states = read("tools/validate_full_event_states.py")
    require(event_states, 'read("data/scripts/spanish/hall_of_fame.inc")', "Gate 6 language path")
    assert 'read("data/scripts/hall_of_fame.inc")' not in event_states

    obtainability = read("tools/validate_full_obtainability.py")
    require(obtainability, 'read("data/scripts/spanish/item_ball_scripts.inc")', "Gate 7 language path")

    freeze = read("tools/validate_rc_freeze.py")
    require(freeze, 'read("data/scripts/spanish/repel.inc")', "QOL-007 language path")

    # Non-target generic scripts touched accidentally during recovery must remain
    # exactly vanilla; they are not allowed to masquerade as Spanish evidence.
    expected_generic = {
        "data/scripts/repel.inc": "97bf963b9be5f40ceed9c450cc614b9ce5a0ce3f",
        "data/scripts/hall_of_fame.inc": "7fede6987415696ca223e2c9efe3a5d7dd57e182",
    }
    for path, expected in expected_generic.items():
        actual = git_blob_sha(path)
        assert actual == expected, f"{path}: non-target generic drift {actual} != {expected}"

    # The second-pass audit locks these high-risk payloads after semantic review.
    audited = read("tools/validate_audited_data_blobs.py")
    for path in (
        "src/data/trainers.json",
        "src/data/trainer_parties.h",
        "data/scripts/spanish/hall_of_fame.inc",
        "data/scripts/spanish/repel.inc",
        "data/scripts/spanish/move_tutors.inc",
    ):
        require(audited, f'"{path}"', "second-pass blob lock")

    # Cross-layer Altering Cave audit: map object -> menu -> selector value ->
    # runtime table index -> actual FireRed table species must all agree.
    cave_map = __import__("json").loads(read("data/maps/SixIsland_AlteringCave/map.json"))
    researcher = [
        obj for obj in cave_map["object_events"]
        if obj.get("script") == "SixIsland_AlteringCave_EventScript_Researcher"
    ]
    assert len(researcher) == 1, researcher

    menu_h = read("include/constants/menu.h")
    require(menu_h, "#define MULTICHOICE_FULL_ALTERING_CAVE_PAGE1", "Altering Cave menu id")
    require(menu_h, "#define MULTICHOICE_FULL_ALTERING_CAVE_PAGE2", "Altering Cave menu id")

    menu_c = read("src/script_menu.c")
    for token in (
        "sMultichoiceList_FullAlteringCavePage1",
        "sMultichoiceList_FullAlteringCavePage2",
        "[MULTICHOICE_FULL_ALTERING_CAVE_PAGE1]",
        "[MULTICHOICE_FULL_ALTERING_CAVE_PAGE2]",
    ):
        require(menu_c, token, "Altering Cave menu registry")

    cave = read("data/maps/SixIsland_AlteringCave/scripts.inc")
    species = (
        ("Zubat", "SPECIES_ZUBAT"),
        ("Mareep", "SPECIES_MAREEP"),
        ("Pineco", "SPECIES_PINECO"),
        ("Houndour", "SPECIES_HOUNDOUR"),
        ("Teddiursa", "SPECIES_TEDDIURSA"),
        ("Aipom", "SPECIES_AIPOM"),
        ("Shuckle", "SPECIES_SHUCKLE"),
        ("Stantler", "SPECIES_STANTLER"),
        ("Smeargle", "SPECIES_SMEARGLE"),
    )
    for value, (label, _) in enumerate(species):
        require(cave, f"SixIsland_AlteringCave_EventScript_Set{label}::", "Altering Cave selector")
        require(cave, f"setvar VAR_ALTERING_CAVE_WILD_SET, {value}", "Altering Cave selector")
    require(cave, "case 127, SixIsland_AlteringCave_EventScript_ResearcherEnd", "Altering Cave cancel")

    wild_c = read("src/wild_encounter.c")
    require(wild_c, "if (alteringCaveId >= NUM_ALTERING_CAVE_TABLES)", "Altering Cave bounds")
    require(wild_c, "i += alteringCaveId;", "Altering Cave table selection")
    wild_h = read("include/wild_encounter.h")
    require(wild_h, "#define NUM_ALTERING_CAVE_TABLES 9", "Altering Cave table count")

    encounters = __import__("json").loads(read("src/data/wild_encounters.json"))
    fire_tables = []
    for group in encounters["wild_encounter_groups"]:
        for encounter in group.get("encounters", []):
            if (
                encounter.get("map") == "MAP_SIX_ISLAND_ALTERING_CAVE"
                and "FireRed" in encounter.get("base_label", "")
            ):
                fire_tables.append(encounter)
    assert len(fire_tables) == 9, len(fire_tables)
    for i, (_, expected_species) in enumerate(species):
        mons = fire_tables[i]["land_mons"]["mons"]
        assert mons, i
        assert all(mon["species"] == expected_species for mon in mons), (i, expected_species)

    # Recovery findings must be recorded, including the corrected false positive.
    audit_log = read("docs/production/RC_AUDIT_LOG.md")
    require(audit_log, "RC-F031", "audit traceability")
    require(audit_log, "FALSE POSITIVE CORRECTED / STATIC PASS", "audit honesty")
    for finding in ("RC-F032", "RC-F033", "RC-F034", "RC-F035"):
        require(audit_log, finding, "audit traceability")

    print(
        "Second-pass release-integrity PASS: Spanish target paths, validator "
        "coverage, generic-script isolation and high-risk blob locks are coherent."
    )


if __name__ == "__main__":
    main()
