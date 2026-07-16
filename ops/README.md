# Local controller preflight and installation

The controller runs on this workstation. DigitalOcean credentials and application
deployment are not part of this run.

## What the local launch gate means

The launch gate is a one-time rehearsal before the Gauntlet becomes active. It proves:

1. Both private repository branches can be pinned over SSH.
2. The local dependency caches can verify a clean frozen clone without package-network access.
3. The grader and planner can call OpenRouter and return valid structured JSON.
4. `$gauntlet-grade` can create a pre-cutoff receipt and write ledger results.
5. Day 1's plan and mastery note are already pushed.

Only after all five facts are true does `run.json` change from `draft` to `active`.

## Local requirements

- Keep this workstation online while `$gauntlet-grade` runs.
- SSH read access to `ChrisSannar/tutoring-platform` and write access to
  `ChrisSannar/gauntlet`.
- `OPENROUTER_API_KEY` exported by the interactive shell, with a $5 key limit.
- Dependency caches at `$HOME/.cache/gauntlet/{uv,bun,playwright}` populated during
  preflight. Midnight installation is offline.
- Persistent controller state at `$HOME/.local/state/gauntlet`; do not delete it during
  the run because it contains immutable submission receipts and freezes.

## Launch commands

```bash
cd /home/chrissannar/Practice/gauntlet
python -m controller.gauntlet_controller validate runs/2026-07-15-tutoring-platform/run.json
python -m controller.gauntlet_controller pin git@github.com:ChrisSannar/gauntlet.git master
python -m controller.gauntlet_controller pin git@github.com:ChrisSannar/tutoring-platform.git main
python -m controller.gauntlet_controller invoke runs/2026-07-15-tutoring-platform/run.json grader fixtures/grade-request.json
python -m controller.gauntlet_controller invoke runs/2026-07-15-tutoring-platform/run.json planner fixtures/plan-request.json
```

The interactive shell is important because that is currently where the OpenRouter key
is exported. `ops/run-local-controller.sh` provides the same environment to systemd.

## Manual pre-cutoff submission

After both repositories are pushed, invoke `$gauntlet-grade` before the displayed
cutoff. Invocation immediately freezes the eligible SHAs. If infrastructure fails after
the freeze, invoke it again; the retry reuses the receipt even after midnight.

The former local timer is not used for `learner-before-cutoff` runs. Disable it once:

```bash
systemctl --user disable --now gauntlet-controller.timer
```
