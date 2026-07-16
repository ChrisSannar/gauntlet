from __future__ import annotations

import datetime as dt
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from controller.gauntlet_controller import (
    ControllerError,
    automatic_day,
    automatic_freeze_window,
    close_day,
    cron_lines,
    establish_freeze,
    ensure_cutoff_reached,
    invoke_adapter,
    normalize_grade,
    pin_remote,
    today_view,
    validate_run,
    validate_plan_markdown,
    verification_repair,
)


ROOT = Path(__file__).resolve().parents[1]


class ControllerTests(unittest.TestCase):
    def make_repo(self, root: Path, name: str) -> tuple[Path, Path]:
        source = root / name
        bare = root / f"{name}.git"
        source.mkdir()
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=source, check=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=source, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=source, check=True)
        subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True)
        subprocess.run(["git", "remote", "add", "origin", str(bare)], cwd=source, check=True)
        return source, bare

    def commit_and_push(self, source: Path, message: str) -> str:
        subprocess.run(["git", "add", "."], cwd=source, check=True)
        subprocess.run(["git", "commit", "-qm", message], cwd=source, check=True)
        subprocess.run(["git", "push", "-q", "origin", "HEAD:refs/heads/main"], cwd=source, check=True)
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source, text=True).strip()

    def test_draft_template_validates(self) -> None:
        config = json.loads((ROOT / "templates" / "run.json").read_text())
        validate_run(config)

    def test_pending_config_cannot_operate(self) -> None:
        config = json.loads((ROOT / "templates" / "run.json").read_text())
        config["status"] = "active"
        with self.assertRaisesRegex(ControllerError, "PENDING"):
            validate_run(config, operational=True)

    def test_required_browser_cannot_be_disabled(self) -> None:
        config = json.loads((ROOT / "templates" / "run.json").read_text())
        config["project"]["evidence_mode"] = "deployed"
        config["project"]["deployed_url"] = "https://example.test"
        config["verification"]["browser"]["required"] = True
        with self.assertRaisesRegex(ControllerError, "cannot be disabled"):
            validate_run(config)

    def test_adapter_uses_json_stdin_stdout(self) -> None:
        adapter = {
            "command": [
                sys.executable,
                "-c",
                "import json,sys; value=json.load(sys.stdin); json.dump({'seen': value['x']}, sys.stdout)",
            ],
            "timeout_seconds": 5,
        }
        self.assertEqual(invoke_adapter(adapter, {"x": 7}), {"seen": 7})

    def test_invalid_adapter_output_is_infrastructure_error(self) -> None:
        adapter = {
            "command": [sys.executable, "-c", "print('not-json')"],
            "timeout_seconds": 5,
        }
        with self.assertRaisesRegex(ControllerError, "invalid JSON"):
            invoke_adapter(adapter, {})

    def test_lower_of_two_is_controller_enforced(self) -> None:
        grade = normalize_grade(
            {
                "delivery_score": 4,
                "mastery_score": 2.5,
                "overall_score": 4,
                "overall_grade": "A",
            }
        )
        self.assertEqual(grade["overall_score"], 2.5)
        self.assertEqual(grade["overall_grade"], "C")

    def test_scores_use_half_point_increments(self) -> None:
        with self.assertRaisesRegex(ControllerError, "0.5 increments"):
            normalize_grade({"delivery_score": 3.2, "mastery_score": 3})

    def test_pin_remote_reads_branch_head(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            bare = root / "remote.git"
            source.mkdir()
            subprocess.run(["git", "init", "-q", "-b", "main"], cwd=source, check=True)
            subprocess.run(["git", "config", "user.name", "Test"], cwd=source, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=source, check=True)
            (source / "README.md").write_text("test\n")
            subprocess.run(["git", "add", "README.md"], cwd=source, check=True)
            subprocess.run(["git", "commit", "-qm", "test"], cwd=source, check=True)
            expected = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source, text=True).strip()
            subprocess.run(["git", "clone", "-q", "--bare", str(source), str(bare)], check=True)
            self.assertEqual(pin_remote(str(bare), "main"), expected)

    def test_close_day_runs_full_transaction_and_pushes_ledger(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            product, product_remote = self.make_repo(root, "product")
            (product / "app.txt").write_text("deployed product\n")
            product_sha = self.commit_and_push(product, "product")

            adapter = root / "adapter.py"
            adapter.write_text(
                "import json,sys\n"
                "request=json.load(sys.stdin)\n"
                "if request['operation']=='grade-day':\n"
                " json.dump({'delivery_score':4,'mastery_score':3,'confidence':'high','summary':'good'},sys.stdout)\n"
                "elif request['operation']=='plan-day':\n"
                " json.dump({'plan_markdown':'# Daily Plan — 2026-07-14\\n\\n## Required boundary\\n- Build it.\\n\\n## Proof required\\n- Test it.\\n\\n## Scope guard\\n- Stop here.\\n'},sys.stdout)\n"
                "else:\n"
                " raise SystemExit(2)\n"
            )

            ledger, ledger_remote = self.make_repo(root, "ledger")
            run_id = "integration-run"
            run = {
                "schema_version": 1,
                "run_id": run_id,
                "status": "active",
                "ledger": {"remote": str(ledger_remote), "branch": "main"},
                "project": {
                    "name": "Test",
                    "remote": str(product_remote),
                    "branch": "main",
                    "evidence_mode": "repository-only",
                    "deployed_url": None,
                    "backlog_path": "projects/test/BACKLOG.md",
                },
                "schedule": {
                    "timezone": "America/Chicago",
                    "start_date": "2026-07-13",
                    "end_date": "2026-07-14",
                    "cutoff_local_time": "00:00",
                    "target_focused_hours": 16,
                },
                "accountability": {
                    "rubric_path": "docs/rubric.md",
                    "mastery_template_path": "templates/mastery.md",
                    "overall_rule": "lower-of-delivery-mastery",
                    "consequence": {
                        "mode": "none",
                        "description": "test",
                        "automatic_execution": False,
                    },
                    "publishing": {
                        "mode": "disabled",
                        "channels": [],
                        "approval_required": True,
                    },
                },
                "verification": {
                    "commands": [
                        {
                            "id": "smoke",
                            "command": [sys.executable, "-c", "from pathlib import Path; assert Path('app.txt').exists()"],
                            "timeout_seconds": 10,
                            "required": True,
                        }
                    ],
                    "browser": {"enabled": False, "adapter": None, "required": False},
                },
                "adapters": {
                    role: {"command": [sys.executable, str(adapter)], "timeout_seconds": 10}
                    for role in ("grader", "planner", "appeal_judge")
                },
            }
            (ledger / "runs" / run_id / "days" / "2026-07-13").mkdir(parents=True)
            (ledger / "runs" / run_id / "run.json").write_text(json.dumps(run))
            (ledger / "runs" / run_id / "days" / "2026-07-13" / "plan.md").write_text("# Plan\n")
            (ledger / "runs" / run_id / "days" / "2026-07-13" / "mastery.md").write_text("# Mastery\n")
            (ledger / "docs").mkdir()
            (ledger / "docs" / "rubric.md").write_text("# Rubric\n")
            (ledger / "templates").mkdir()
            (ledger / "templates" / "mastery.md").write_text("# Mastery Template\n")
            (ledger / "projects" / "test").mkdir(parents=True)
            (ledger / "projects" / "test" / "BACKLOG.md").write_text("# Backlog\n")
            self.commit_and_push(ledger, "ledger")

            result = close_day(ledger / "runs" / run_id / "run.json", dt.date(2026, 7, 13), root / "state")
            self.assertEqual(result["grade"]["overall_grade"], "B")
            self.assertEqual(result["evidence"]["product_sha"], product_sha)

            checkout = root / "ledger-check"
            subprocess.run(
                ["git", "clone", "-q", "--branch", "main", str(ledger_remote), str(checkout)], check=True
            )
            finalized = checkout / "runs" / run_id / "days" / "2026-07-13"
            self.assertTrue((finalized / "evidence.json").exists())
            self.assertTrue((finalized / "grade.json").exists())
            self.assertTrue((checkout / "runs" / run_id / "days" / "2026-07-14" / "plan.md").exists())
            self.assertEqual(pin_remote(str(product_remote), "main"), product_sha)
            repeated = close_day(
                ledger / "runs" / run_id / "run.json", dt.date(2026, 7, 13), root / "state"
            )
            self.assertEqual(repeated["status"], "already-finalized")

    def test_repository_only_rejects_deployment_and_browser(self) -> None:
        config = json.loads((ROOT / "templates" / "run.json").read_text())
        config["project"]["deployed_url"] = "https://example.test"
        with self.assertRaisesRegex(ControllerError, "deployed_url=null"):
            validate_run(config)

    def test_incomplete_freeze_never_admits_later_heads(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            state = Path(temporary)
            config = json.loads((ROOT / "templates" / "run.json").read_text())
            config["run_id"] = "freeze-test"
            path = state / "freeze-test" / "freezes" / "2026-07-15.json"
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps({"status": "freezing"}))
            with self.assertRaisesRegex(ControllerError, "original cutoff freeze is incomplete"):
                establish_freeze(config, dt.date(2026, 7, 15), state)

    def test_verification_repair_allows_only_command_changes(self) -> None:
        frozen = json.loads((ROOT / "templates" / "run.json").read_text())
        operational = json.loads(json.dumps(frozen))
        operational["verification"]["commands"] = [
            {"id": "tests", "command": ["python", "-m", "pytest"]}
        ]

        repair = verification_repair(frozen, operational)

        self.assertEqual(repair["kind"], "verification-commands-only")
        self.assertNotEqual(repair["frozen_config_sha256"], repair["operational_config_sha256"])

    def test_verification_repair_rejects_broader_changes(self) -> None:
        frozen = json.loads((ROOT / "templates" / "run.json").read_text())
        operational = json.loads(json.dumps(frozen))
        operational["verification"]["commands"] = [
            {"id": "tests", "command": ["python", "-m", "pytest"]}
        ]
        operational["schedule"]["end_date"] = "2026-08-01"

        with self.assertRaisesRegex(ControllerError, "differs from frozen"):
            verification_repair(frozen, operational)

    def test_daily_plan_requires_concrete_ordered_sections(self) -> None:
        valid = """# Daily Plan — 2026-07-16

## Required boundary
- Build it.

## Proof required
- Run tests.

## Scope guard
- Stop here.
"""
        validate_plan_markdown(valid, dt.date(2026, 7, 16))
        with self.assertRaisesRegex(ControllerError, "missing ordered required sections"):
            validate_plan_markdown(
                "# Daily Plan — 2026-07-16\n\n## Required boundary\n- Build it.\n",
                dt.date(2026, 7, 16),
            )

    def test_cron_has_midnight_and_two_retries(self) -> None:
        config_path = ROOT / "runs" / "2026-07-15-tutoring-platform" / "run.json"
        lines = cron_lines(config_path, Path("/tmp/gauntlet-state")).splitlines()
        self.assertEqual(lines[0], "CRON_TZ=America/Chicago")
        self.assertEqual([line.split()[:2] for line in lines[1:]], [["0", "0"], ["15", "0"], ["30", "0"]])

    def test_day_cannot_freeze_before_its_cutoff(self) -> None:
        config = json.loads((ROOT / "templates" / "run.json").read_text())
        now = dt.datetime(2026, 1, 1, 23, 59, tzinfo=dt.UTC)
        with self.assertRaisesRegex(ControllerError, "cutoff has not been reached"):
            ensure_cutoff_reached(config, dt.date(2026, 1, 1), now)

    def test_automatic_day_is_previous_local_date(self) -> None:
        config = json.loads((ROOT / "templates" / "run.json").read_text())
        now = dt.datetime(2026, 7, 14, 5, 1, tzinfo=dt.UTC)
        self.assertEqual(automatic_day(config, now), dt.date(2026, 7, 13))

    def test_only_cutoff_attempt_can_create_automatic_freeze(self) -> None:
        config = json.loads((ROOT / "templates" / "run.json").read_text())
        self.assertTrue(automatic_freeze_window(config, dt.datetime(2026, 1, 2, 6, 2, tzinfo=dt.UTC)))
        self.assertFalse(automatic_freeze_window(config, dt.datetime(2026, 1, 2, 6, 15, tzinfo=dt.UTC)))

    def test_today_previews_first_day_before_run(self) -> None:
        config_path = ROOT / "runs" / "2026-07-15-tutoring-platform" / "run.json"
        now = dt.datetime(2026, 7, 14, 18, tzinfo=dt.UTC)
        rendered = today_view(config_path, now=now)
        self.assertIn("Preview: Gauntlet Day 1", rendered)
        self.assertIn("Required boundary: Foundation", rendered)
        self.assertIn("Before midnight", rendered)
        self.assertIn("2026-07-16 00:00 CDT", rendered)


if __name__ == "__main__":
    unittest.main()
