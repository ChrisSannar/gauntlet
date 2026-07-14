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

The close-day path pins and clones the ledger and product branches, runs configured
checks, optionally invokes the browser adapter, invokes the grader, enforces the
lower-of-two result, invokes the planner, commits the append-only artifacts to the
ledger, and pushes the ledger branch.

The server still needs Git credentials for the ledger, read access to the product, the
configured LLM adapter executables/secrets, and cron. A run remains draft until its
`PENDING` values are replaced and `status` becomes `active`.
