#!/usr/bin/env python3
"""Freeze, verify, grade, and plan Gauntlet days without product write access."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


class ControllerError(RuntimeError):
    """An infrastructure or contract error that must not become learner failure."""


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_value(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode()).hexdigest()


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise ControllerError(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ControllerError(f"expected JSON object in {path}")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def require_mapping(value: Any, name: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ControllerError(f"{name} must be an object")
    return value


def validate_run(config: dict[str, Any], operational: bool = False) -> None:
    required = {
        "schema_version",
        "run_id",
        "status",
        "ledger",
        "project",
        "schedule",
        "accountability",
        "verification",
        "adapters",
    }
    missing = sorted(required - config.keys())
    if missing:
        raise ControllerError(f"run configuration missing: {', '.join(missing)}")
    if config["schema_version"] != 1:
        raise ControllerError("unsupported schema_version")

    ledger = require_mapping(config["ledger"], "ledger")
    project = require_mapping(config["project"], "project")
    schedule = require_mapping(config["schedule"], "schedule")
    accountability = require_mapping(config["accountability"], "accountability")
    verification = require_mapping(config["verification"], "verification")
    adapters = require_mapping(config["adapters"], "adapters")

    for owner, fields in (
        (ledger, ("remote", "branch")),
        (project, ("name", "remote", "branch", "deployed_url", "backlog_path")),
        (
            schedule,
            ("timezone", "start_date", "end_date", "cutoff_local_time", "target_focused_hours"),
        ),
        (
            accountability,
            ("rubric_path", "mastery_template_path", "overall_rule", "consequence", "publishing"),
        ),
        (verification, ("commands", "browser")),
        (adapters, ("grader", "planner", "appeal_judge")),
    ):
        absent = [field for field in fields if field not in owner]
        if absent:
            raise ControllerError(f"configuration section missing: {', '.join(absent)}")

    try:
        start = dt.date.fromisoformat(str(schedule["start_date"]))
        end = dt.date.fromisoformat(str(schedule["end_date"]))
    except ValueError as exc:
        raise ControllerError(f"invalid run date: {exc}") from exc
    if end < start:
        raise ControllerError("end_date precedes start_date")
    try:
        ZoneInfo(str(schedule["timezone"]))
    except ZoneInfoNotFoundError as exc:
        raise ControllerError(f"unknown timezone: {schedule['timezone']}") from exc

    if accountability["overall_rule"] != "lower-of-delivery-mastery":
        raise ControllerError("unsupported overall_rule")
    if not isinstance(verification["commands"], list):
        raise ControllerError("verification.commands must be an array")
    browser = require_mapping(verification["browser"], "verification.browser")
    if browser.get("required") and not browser.get("enabled"):
        raise ControllerError("required browser verification cannot be disabled")
    for role in ("grader", "planner", "appeal_judge"):
        validate_adapter(require_mapping(adapters[role], f"adapters.{role}"), role)

    if operational:
        if config["status"] != "active":
            raise ControllerError("operational command requires status=active")
        pending = find_pending(config)
        if pending:
            raise ControllerError(f"active run contains PENDING at {pending[0]}")


def find_pending(value: Any, path: str = "$") -> list[str]:
    matches: list[str] = []
    if value == "PENDING":
        matches.append(path)
    elif isinstance(value, dict):
        for key, nested in value.items():
            matches.extend(find_pending(nested, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, nested in enumerate(value):
            matches.extend(find_pending(nested, f"{path}[{index}]"))
    return matches


def validate_adapter(adapter: dict[str, Any], name: str) -> None:
    command = adapter.get("command")
    timeout = adapter.get("timeout_seconds")
    if not isinstance(command, list) or not command or not all(isinstance(x, str) for x in command):
        raise ControllerError(f"{name}.command must be a nonempty string array")
    if not isinstance(timeout, int) or not 1 <= timeout <= 3600:
        raise ControllerError(f"{name}.timeout_seconds must be between 1 and 3600")


def run_process(
    command: list[str],
    *,
    cwd: Path | None = None,
    timeout: int = 300,
    input_text: str | None = None,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            command,
            cwd=cwd,
            env=env,
            input=input_text,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ControllerError(f"command failed to execute {command[0]}: {exc}") from exc


def invoke_adapter(adapter: dict[str, Any], payload: dict[str, Any]) -> dict[str, Any]:
    validate_adapter(adapter, "adapter")
    result = run_process(
        adapter["command"],
        timeout=adapter["timeout_seconds"],
        input_text=json.dumps(payload),
        env=os.environ.copy(),
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or "no diagnostic output"
        raise ControllerError(f"adapter exited {result.returncode}: {detail}")
    try:
        response = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise ControllerError(f"adapter returned invalid JSON: {exc}") from exc
    if not isinstance(response, dict):
        raise ControllerError("adapter response must be a JSON object")
    return response


def git_output(args: list[str], *, cwd: Path | None = None, timeout: int = 300) -> str:
    result = run_process(["git", *args], cwd=cwd, timeout=timeout)
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        raise ControllerError(f"git {' '.join(args)} failed: {detail}")
    return result.stdout.strip()


def pin_remote(remote: str, branch: str) -> str:
    output = git_output(["ls-remote", "--exit-code", remote, f"refs/heads/{branch}"])
    rows = [line.split() for line in output.splitlines() if line.strip()]
    if len(rows) != 1 or len(rows[0]) < 2:
        raise ControllerError(f"could not uniquely pin {remote} branch {branch}")
    sha = rows[0][0]
    if len(sha) != 40 or any(char not in "0123456789abcdef" for char in sha.lower()):
        raise ControllerError(f"remote returned invalid commit SHA: {sha}")
    return sha


def clone_branch(remote: str, branch: str, destination: Path, expected_sha: str) -> None:
    result = run_process(
        ["git", "clone", "--quiet", "--single-branch", "--branch", branch, remote, str(destination)],
        timeout=600,
    )
    if result.returncode != 0:
        raise ControllerError(f"clone failed: {result.stderr.strip()}")
    actual = git_output(["rev-parse", "HEAD"], cwd=destination)
    if actual != expected_sha:
        raise ControllerError(f"remote moved while freezing evidence: expected {expected_sha}, got {actual}")


def run_checks(checks: list[dict[str, Any]], checkout: Path, deployed_url: str) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    environment = os.environ.copy()
    environment["GAUNTLET_DEPLOYED_URL"] = deployed_url
    for check in checks:
        command = check.get("command")
        if not isinstance(command, list) or not command or not all(isinstance(x, str) for x in command):
            raise ControllerError(f"invalid verification command for {check.get('id', '<unknown>')}")
        started = dt.datetime.now(dt.UTC)
        result = run_process(
            command,
            cwd=checkout,
            timeout=int(check.get("timeout_seconds", 300)),
            env=environment,
        )
        duration = (dt.datetime.now(dt.UTC) - started).total_seconds()
        results.append(
            {
                "id": check.get("id"),
                "command": command,
                "required": bool(check.get("required", True)),
                "exit_code": result.returncode,
                "duration_seconds": round(duration, 3),
                "stdout": result.stdout,
                "stderr": result.stderr,
                "passed": result.returncode == 0,
            }
        )
    return results


def read_required(path: Path, label: str) -> str:
    try:
        return path.read_text()
    except OSError as exc:
        raise ControllerError(f"missing {label}: {path}") from exc


def score_letter(score: float) -> str:
    if score >= 3.5:
        return "A"
    if score >= 3.0:
        return "B"
    if score >= 2.0:
        return "C"
    if score >= 1.0:
        return "D"
    return "F"


def normalize_grade(response: dict[str, Any]) -> dict[str, Any]:
    try:
        delivery = float(response["delivery_score"])
        mastery = float(response["mastery_score"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ControllerError("grader response requires numeric delivery_score and mastery_score") from exc
    for name, score in (("delivery_score", delivery), ("mastery_score", mastery)):
        if not 0 <= score <= 4 or score * 2 != int(score * 2):
            raise ControllerError(f"{name} must be 0..4 in 0.5 increments")
    overall = min(delivery, mastery)
    normalized = dict(response)
    normalized.update(
        {
            "delivery_score": delivery,
            "mastery_score": mastery,
            "overall_score": overall,
            "overall_grade": score_letter(overall),
        }
    )
    return normalized


def render_grade(grade: dict[str, Any], evidence: dict[str, Any]) -> str:
    confidence = grade.get("confidence", "unspecified")
    summary = grade.get("summary", "No summary supplied.")
    return (
        f"# Daily Grade — {evidence['day']}\n\n"
        f"- Delivery: {grade['delivery_score']}/4\n"
        f"- Mastery: {grade['mastery_score']}/4\n"
        f"- Overall: {grade['overall_grade']} ({grade['overall_score']}/4)\n"
        f"- Confidence: {confidence}\n"
        f"- Product SHA: `{evidence['product_sha']}`\n"
        f"- Ledger SHA: `{evidence['ledger_sha']}`\n\n"
        f"## Summary\n\n{summary}\n"
    )


def date_in_run(config: dict[str, Any], day: dt.date) -> bool:
    schedule = config["schedule"]
    return dt.date.fromisoformat(schedule["start_date"]) <= day <= dt.date.fromisoformat(
        schedule["end_date"]
    )


def close_day(config_path: Path, day: dt.date, state_dir: Path) -> dict[str, Any]:
    bootstrap = read_json(config_path)
    validate_run(bootstrap, operational=True)
    if not date_in_run(bootstrap, day):
        raise ControllerError(f"{day} is outside configured run dates")

    ledger_cfg = bootstrap["ledger"]
    product_cfg = bootstrap["project"]
    ledger_sha = pin_remote(ledger_cfg["remote"], ledger_cfg["branch"])
    product_sha = pin_remote(product_cfg["remote"], product_cfg["branch"])

    with tempfile.TemporaryDirectory(prefix="gauntlet-close-") as temporary:
        root = Path(temporary)
        ledger = root / "ledger"
        product = root / "product"
        clone_branch(ledger_cfg["remote"], ledger_cfg["branch"], ledger, ledger_sha)
        clone_branch(product_cfg["remote"], product_cfg["branch"], product, product_sha)

        ledger_config_path = ledger / "runs" / bootstrap["run_id"] / "run.json"
        config = read_json(ledger_config_path)
        validate_run(config, operational=True)
        if sha256_value(config) != sha256_value(bootstrap):
            raise ControllerError("bootstrap configuration differs from frozen ledger configuration")

        day_dir = ledger / "runs" / config["run_id"] / "days" / day.isoformat()
        existing_grade_path = day_dir / "grade.json"
        existing_evidence_path = day_dir / "evidence.json"
        if existing_grade_path.exists() and existing_evidence_path.exists():
            return {
                "status": "already-finalized",
                "evidence": read_json(existing_evidence_path),
                "grade": read_json(existing_grade_path),
            }
        if existing_grade_path.exists() or existing_evidence_path.exists():
            raise ControllerError("day contains a partial finalized report; manual recovery required")
        plan = read_required(day_dir / "plan.md", "frozen daily plan")
        mastery_path = day_dir / "mastery.md"
        mastery = mastery_path.read_text() if mastery_path.exists() else ""
        rubric = read_required(ledger / config["accountability"]["rubric_path"], "rubric")
        backlog = read_required(ledger / config["project"]["backlog_path"], "backlog")
        checks = run_checks(config["verification"]["commands"], product, config["project"]["deployed_url"])

        browser_result: dict[str, Any] | None = None
        browser_config = config["verification"]["browser"]
        if browser_config["enabled"]:
            if browser_config["adapter"] is None:
                raise ControllerError("browser enabled without adapter")
            browser_result = invoke_adapter(
                browser_config["adapter"],
                {
                    "operation": "live-product-check",
                    "run_id": config["run_id"],
                    "day": day.isoformat(),
                    "url": config["project"]["deployed_url"],
                    "plan": plan,
                },
            )

        frozen_at = dt.datetime.now(dt.UTC).isoformat()
        evidence = {
            "schema_version": 1,
            "run_id": config["run_id"],
            "day": day.isoformat(),
            "frozen_at": frozen_at,
            "run_config_sha256": sha256_value(config),
            "ledger_sha": ledger_sha,
            "product_sha": product_sha,
            "plan": plan,
            "mastery_note": mastery,
            "mastery_note_present": bool(mastery.strip()),
            "checks": checks,
            "browser": browser_result,
        }

        grade_response = invoke_adapter(
            config["adapters"]["grader"],
            {
                "operation": "grade-day",
                "rubric": rubric,
                "evidence": evidence,
            },
        )
        grade = normalize_grade(grade_response)
        grade.update(
            {
                "schema_version": 1,
                "run_id": config["run_id"],
                "day": day.isoformat(),
                "evidence_sha256": sha256_value(evidence),
            }
        )

        local_day = state_dir / config["run_id"] / "days" / day.isoformat()
        write_json(local_day / "evidence.json", evidence)
        write_json(local_day / "grade.json", grade)
        (local_day / "grade.md").write_text(render_grade(grade, evidence))

        write_json(day_dir / "evidence.json", evidence)
        write_json(day_dir / "grade.json", grade)
        (day_dir / "grade.md").write_text(render_grade(grade, evidence))

        next_day = day + dt.timedelta(days=1)
        if date_in_run(config, next_day):
            plan_response = invoke_adapter(
                config["adapters"]["planner"],
                {
                    "operation": "plan-day",
                    "run": config,
                    "day": next_day.isoformat(),
                    "previous_plan": plan,
                    "previous_grade": grade,
                    "backlog": backlog,
                },
            )
            plan_markdown = plan_response.get("plan_markdown")
            if not isinstance(plan_markdown, str) or not plan_markdown.strip():
                raise ControllerError("planner response requires nonempty plan_markdown")
            next_dir = ledger / "runs" / config["run_id"] / "days" / next_day.isoformat()
            next_dir.mkdir(parents=True, exist_ok=True)
            if (next_dir / "plan.md").exists():
                raise ControllerError("next daily boundary already exists; refusing to overwrite it")
            (next_dir / "plan.md").write_text(plan_markdown.rstrip() + "\n")
            mastery_template = read_required(
                ledger / config["accountability"]["mastery_template_path"], "mastery template"
            )
            (next_dir / "mastery.md").write_text(mastery_template)

        git_output(["config", "user.name", "Gauntlet Controller"], cwd=ledger)
        git_output(["config", "user.email", "controller@gauntlet.invalid"], cwd=ledger)
        git_output(["add", f"runs/{config['run_id']}/days"], cwd=ledger)
        status = git_output(["status", "--porcelain"], cwd=ledger)
        if not status:
            raise ControllerError("controller produced no ledger changes")
        git_output(["commit", "-m", f"gauntlet: finalize {config['run_id']} {day.isoformat()}"], cwd=ledger)
        git_output(["push", "origin", f"HEAD:refs/heads/{ledger_cfg['branch']}"], cwd=ledger, timeout=600)
        return {"status": "finalized", "evidence": evidence, "grade": grade}


def automatic_day(config: dict[str, Any], now: dt.datetime | None = None) -> dt.date:
    timezone = ZoneInfo(config["schedule"]["timezone"])
    current = now.astimezone(timezone) if now else dt.datetime.now(timezone)
    return current.date() - dt.timedelta(days=1)


def cron_lines(config_path: Path, state_dir: Path) -> str:
    config = read_json(config_path)
    validate_run(config)
    hour, minute = config["schedule"]["cutoff_local_time"].split(":")
    controller = Path(__file__).resolve()
    lock = state_dir / f"{config['run_id']}.lock"
    log = state_dir / f"{config['run_id']}.log"
    quoted = [
        shlex.quote(str(value))
        for value in (
            lock,
            sys.executable,
            controller,
            "close-auto",
            config_path.resolve(),
            "--state-dir",
            state_dir.resolve(),
        )
    ]
    command = f"flock -n {' '.join(quoted)} >> {shlex.quote(str(log))} 2>&1"
    return f"CRON_TZ={config['schedule']['timezone']}\n{int(minute)} {int(hour)} * * * {command}\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="operation", required=True)

    validate = subparsers.add_parser("validate")
    validate.add_argument("config", type=Path)
    validate.add_argument("--operational", action="store_true")

    invoke = subparsers.add_parser("invoke")
    invoke.add_argument("config", type=Path)
    invoke.add_argument("role", choices=("grader", "planner", "appeal_judge"))
    invoke.add_argument("request", type=Path)

    pin = subparsers.add_parser("pin")
    pin.add_argument("remote")
    pin.add_argument("branch")

    close = subparsers.add_parser("close-day")
    close.add_argument("config", type=Path)
    close.add_argument("day", type=dt.date.fromisoformat)
    close.add_argument("--state-dir", type=Path, required=True)

    close_auto = subparsers.add_parser("close-auto")
    close_auto.add_argument("config", type=Path)
    close_auto.add_argument("--state-dir", type=Path, required=True)

    cron = subparsers.add_parser("cron-lines")
    cron.add_argument("config", type=Path)
    cron.add_argument("--state-dir", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        if args.operation == "validate":
            config = read_json(args.config)
            validate_run(config, operational=args.operational)
            print("valid")
        elif args.operation == "invoke":
            config = read_json(args.config)
            validate_run(config)
            response = invoke_adapter(config["adapters"][args.role], read_json(args.request))
            print(json.dumps(response, indent=2, sort_keys=True))
        elif args.operation == "pin":
            print(pin_remote(args.remote, args.branch))
        elif args.operation == "close-day":
            print(json.dumps(close_day(args.config, args.day, args.state_dir), indent=2, sort_keys=True))
        elif args.operation == "close-auto":
            config = read_json(args.config)
            day = automatic_day(config)
            if date_in_run(config, day):
                print(json.dumps(close_day(args.config, day, args.state_dir), indent=2, sort_keys=True))
            else:
                print(f"no-op: {day} outside run")
        elif args.operation == "cron-lines":
            print(cron_lines(args.config, args.state_dir), end="")
        return 0
    except ControllerError as exc:
        print(f"INFRA_ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
