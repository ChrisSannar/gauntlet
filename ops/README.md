# Controller preflight and installation

The DigitalOcean host is a controller only; it never deploys the product.

## Required host state

- Ledger checkout at `/opt/gauntlet`, with write credentials only for
  `ChrisSannar/gauntlet`.
- Read-only deploy key for `ChrisSannar/tutoring-platform`.
- `OPENROUTER_API_KEY` supplied by the service environment, with a $5 key limit.
- Python, Git, `uv`, Bun, Playwright Chromium, and `flock` installed.
- Dependency caches populated at `/var/cache/gauntlet/{uv,bun,playwright}` during
  preflight; midnight verification uses offline installation.

## Launch gate

```bash
cd /opt/gauntlet
python -m controller.gauntlet_controller validate runs/2026-07-15-tutoring-platform/run.json
python -m controller.gauntlet_controller pin git@github.com:ChrisSannar/gauntlet.git master
python -m controller.gauntlet_controller pin git@github.com:ChrisSannar/tutoring-platform.git main
python -m controller.gauntlet_controller invoke runs/2026-07-15-tutoring-platform/run.json grader fixtures/grade-request.json
python -m controller.gauntlet_controller invoke runs/2026-07-15-tutoring-platform/run.json planner fixtures/plan-request.json
```

Only after these pass, change `status` from `draft` to `active`, commit, push, and run
`validate --operational` against that pushed commit.

## Cron

```bash
mkdir -p /var/lib/gauntlet
python -m controller.gauntlet_controller cron-lines \
  /opt/gauntlet/runs/2026-07-15-tutoring-platform/run.json \
  --state-dir /var/lib/gauntlet
```

Install the three printed entries in the controller user's crontab. They run at 00:00,
00:15, and 00:30 America/Chicago under one `flock`; retries reuse the local immutable
freeze record. Back up `/var/lib/gauntlet` because losing a freeze record makes a fair
retry impossible and must remain `INFRA_ERROR`.
