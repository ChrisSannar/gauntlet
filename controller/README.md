# Gauntlet Controller

The controller is the provider-neutral, externally scheduled half of `$gauntlet`.
It treats the product repository as read-only and writes finalized evidence, grades,
and next-day plans only to the configured Gauntlet ledger.

## Commands

```bash
python -m controller.gauntlet_controller validate <run.json>
python -m controller.gauntlet_controller validate <run.json> --operational
python -m controller.gauntlet_controller cron-lines <run.json> --state-dir <dir>
python -m controller.gauntlet_controller close-day <run.json> YYYY-MM-DD --state-dir <dir>
python -m controller.gauntlet_controller close-auto <run.json> --state-dir <dir>
```

`cron-lines` prints, but does not install, the crontab entry. Installation is a separate
explicit server action. `close-auto` grades the previous local date, allowing a midnight
trigger to close the day that just ended.

Adapters receive one JSON object on stdin and must return one JSON object on stdout.
See `docs/run-contract.md`. Adapter failures exit with code 2 and an `INFRA_ERROR`
diagnostic. The controller never converts them into a learner grade.

## Current minimum

The close-day path atomically persists the first observed ledger and product SHAs before
checks or model calls. Retries reuse that freeze, read evidence from detached frozen
commits, and append output on top of the current ledger head. An incomplete original
freeze is permanently `INFRA_ERROR`; a later push can never replace it.

Repository-only runs require `deployed_url: null` and disable browser review. Configured
checks may still launch a repository-local Playwright application. Checks marked
`infrastructure: true` convert provisioning/cache failures to `INFRA_ERROR` instead of
learner failure.

The controller host still needs Git credentials for the ledger, read access to the product, the
configured LLM adapter executables/secrets, offline dependency caches, and cron. A run remains draft until its
`PENDING` values are replaced and `status` becomes `active`.
