#!/usr/bin/env python3
"""Print the frozen daily view for the active Gauntlet run."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from controller.gauntlet_controller import today_view  # noqa: E402


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
        raise SystemExit(
            "Multiple active Gauntlet runs found; pass one run.json explicitly:\n"
            f"{choices}"
        )
    return matches[0]


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit(f"Usage: {Path(sys.argv[0]).name} [path/to/run.json]")

    config = Path(sys.argv[1]).expanduser() if len(sys.argv) == 2 else active_run()
    if not config.is_absolute():
        config = ROOT / config
    print(today_view(config.resolve()))


if __name__ == "__main__":
    main()
