#!/usr/bin/env python3
"""Prove the RC reconciliation ledger covers exactly the 154 frozen requirements."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "docs/spec/Pokemon_Rojo_Fuego_Full_Matrices_v1.0.md"
LEDGER = ROOT / "docs/production/RC_REQUIREMENTS_RECONCILIATION.md"

EXPECTED_SUPERSEDED = {"QOL-008", "SAVE-002", "COMP-006"}
VALID_CLASSES = {
    "implemented + automated evidence",
    "implemented + runtime evidence required",
    "superseded by amendment",
    "A-005 redesign pending",
    "implemented core + A-005 UX pending",
    "encounter implemented; A-005 access redesign pending",
    "functional core runtime-proven; A-005 presentation pending",
    "destination core implemented; A-005 access split pending",
}


def main():
    matrix = MATRIX.read_text(encoding="utf-8")
    ledger = LEDGER.read_text(encoding="utf-8")

    impl_start = matrix.index("TAB NAME: Implementacion>")
    impl_end = matrix.index("<PARSED TEXT FOR SHEET: 3", impl_start)
    frozen_rows = matrix[impl_start:impl_end]
    frozen_ids = re.findall(r"^\d+,([A-Z]+-\d+),", frozen_rows, re.MULTILINE)

    ledger_rows = re.findall(
        r"^\|\s*([A-Z]+-\d+)\s*\|.*?\|\s*\*\*([^*]+)\*\*\s*\|",
        ledger,
        re.MULTILINE,
    )
    ledger_ids = [row[0] for row in ledger_rows]
    classifications = {req_id: classification.strip() for req_id, classification in ledger_rows}

    assert len(frozen_ids) == 154, f"frozen matrix has {len(frozen_ids)} implementation rows, expected 154"
    assert len(set(frozen_ids)) == 154, "duplicate requirement IDs in frozen matrix"
    assert len(ledger_ids) == 154, f"reconciliation has {len(ledger_ids)} rows, expected 154"
    assert len(set(ledger_ids)) == 154, "duplicate requirement IDs in reconciliation"

    missing = sorted(set(frozen_ids) - set(ledger_ids))
    extra = sorted(set(ledger_ids) - set(frozen_ids))
    assert not missing, "requirements missing from reconciliation: " + ", ".join(missing)
    assert not extra, "unknown requirements in reconciliation: " + ", ".join(extra)

    invalid = {
        req_id: classification
        for req_id, classification in classifications.items()
        if classification not in VALID_CLASSES
    }
    assert not invalid, f"invalid reconciliation classifications: {invalid}"

    superseded = {
        req_id for req_id, classification in classifications.items()
        if classification == "superseded by amendment"
    }
    assert superseded == EXPECTED_SUPERSEDED, (
        f"superseded rows changed: got {sorted(superseded)}, "
        f"expected {sorted(EXPECTED_SUPERSEDED)}"
    )

    automated = sum(c == "implemented + automated evidence" for c in classifications.values())
    runtime = sum(c == "implemented + runtime evidence required" for c in classifications.values())
    pending = sum("pending" in c for c in classifications.values())
    print(
        "Gate 1 reconciliation PASS: exact frozen 154/154 ID set; "
        f"{automated} automated, {runtime} runtime-required, "
        f"{pending} amendment-pending, "
        f"{len(superseded)} superseded by approved amendments."
    )


if __name__ == "__main__":
    main()
