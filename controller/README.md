# Gauntlet Controller

The controller is the provider-neutral evidence and grading engine behind `$gauntlet-grade`.
It treats the product repository as read-only and writes finalized evidence, grades,
and next-day plans only to the configured Gauntlet ledger.

## Commands

```bash
python -m controller.gauntlet_controller validate <run.json>
python -m controller.gauntlet_controller validate <run.json> --operational
python -m controller.gauntlet_controller today <run.json>
python -m controller.gauntlet_controller submit-current <run.json> --state-dir <dir>
python -m controller.gauntlet_controller close-day <run.json> YYYY-MM-DD --state-dir <dir>
```

`submit-current` must first be called before the configured cutoff. It records a local
receipt and freezes pushed repository heads immediately. After that receipt exists, the
same command may finish or retry after the cutoff without admitting later commits.

`today` is the learner-facing entry point. Before the run it previews Day 1; during the
run it prints the frozen required boundary, proof requirements, mastery-note path,
cutoff, and pre-midnight submission checklist. `today --day YYYY-MM-DD` previews a
specific generated boundary.

Adapters receive one JSON object on stdin and must return one JSON object on stdout.
See `docs/run-contract.md`. Adapter failures exit with code 2 and an `INFRA_ERROR`
diagnostic. The controller never converts them into a learner grade.

## Current minimum

The submission path atomically persists the first observed ledger and product SHAs before
checks or model calls. Retries reuse that freeze, read evidence from detached frozen
commits, and append output on top of the current ledger head. An incomplete original
freeze is permanently `INFRA_ERROR`; a later push can never replace it.

Repository-only runs require `deployed_url: null` and disable browser review. Configured
checks may still launch a repository-local Playwright application. Checks marked
`infrastructure: true` convert provisioning/cache failures to `INFRA_ERROR` instead of
learner failure.

The controller host still needs Git credentials for the ledger, read access to the product, the
configured LLM adapter executables/secrets, and offline dependency caches. A run remains draft until its
`PENDING` values are replaced and `status` becomes `active`.
