#!/usr/bin/env python3
"""Freeze and grade the active Gauntlet day from pushed repository evidence."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from controller.gauntlet_controller import ControllerError, submit_current  # noqa: E402


def active_run() -> Path:
    matches: list[Path] = []
    for config in sorted((ROOT / "runs").glob("*/run.json")):
        try:
            data = json.loads(config.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if data.get("status") == "active":
            matches.append(config)
    if not matches:
        raise SystemExit("No active Gauntlet run found under runs/*/run.json.")
    if len(matches) > 1:
        choices = "\n".join(f"  - {path.relative_to(ROOT)}" for path in matches)
        raise SystemExit(f"Multiple active runs found; pass one run.json explicitly:\n{choices}")
    return matches[0]


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit(f"Usage: {Path(sys.argv[0]).name} [path/to/run.json]")
    config = Path(sys.argv[1]).expanduser() if len(sys.argv) == 2 else active_run()
    if not config.is_absolute():
        config = ROOT / config
    state_dir = Path(os.environ.get("GAUNTLET_STATE_DIR", "~/.local/state/gauntlet")).expanduser()
    try:
        result = submit_current(config.resolve(), state_dir)
    except ControllerError as exc:
        print(f"INFRA_ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc

    grade = result["grade"]
    evidence = result["evidence"]
    print(f"Finalized Gauntlet day {evidence['day']}.")
    print(f"Frozen product: {evidence['product_sha']}")
    print(f"Frozen ledger: {evidence['ledger_sha']}")
    print(
        f"Delivery {grade['delivery_score']}/4 | Mastery {grade['mastery_score']}/4 | "
        f"Overall {grade['overall_grade']} ({grade['overall_score']}/4)"
    )
    print("\nHighest-leverage improvements:")
    for item in grade["improvement_actions"]:
        print(f"- {item}")
    print("\nLearning directions:")
    for item in grade["learning_directions"]:
        print(f"- {item}")


if __name__ == "__main__":
    main()
