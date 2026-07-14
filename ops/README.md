# Local controller preflight and installation

The controller runs on this workstation. DigitalOcean credentials and application
deployment are not part of this run.

## What the local launch gate means

The launch gate is a one-time rehearsal before the Gauntlet becomes active. It proves:

1. Both private repository branches can be pinned over SSH.
2. The local dependency caches can verify a clean frozen clone without package-network access.
3. The grader and planner can call OpenRouter and return valid structured JSON.
4. The midnight timer is installed and can write ledger results.
5. Day 1's plan and mastery note are already pushed.

Only after all five facts are true does `run.json` change from `draft` to `active`.

## Local requirements

- Keep this workstation awake and online from 23:55 through 00:35 America/Chicago.
- SSH read access to `ChrisSannar/tutoring-platform` and write access to
  `ChrisSannar/gauntlet`.
- `OPENROUTER_API_KEY` exported by the interactive shell, with a $5 key limit.
- Dependency caches at `$HOME/.cache/gauntlet/{uv,bun,playwright}` populated during
  preflight. Midnight installation is offline.
- Persistent controller state at `$HOME/.local/state/gauntlet`; do not delete it during
  the run because it contains immutable cutoff records.

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

## Midnight automation

The tracked user service and timer run at 00:00, 00:15, and 00:30 America/Chicago.
All attempts share a `flock`; retries must find and reuse the 00:00 freeze. The timer is
not persistent: if this workstation sleeps through midnight, it must remain an
infrastructure failure rather than admitting a late commit.

Install and inspect:

```bash
mkdir -p ~/.config/systemd/user ~/.local/state/gauntlet
cp ops/systemd/gauntlet-controller.service ops/systemd/gauntlet-controller.timer ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now gauntlet-controller.timer
systemctl --user list-timers gauntlet-controller.timer
journalctl --user -u gauntlet-controller.service
```
