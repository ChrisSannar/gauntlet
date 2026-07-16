# Gauntlet Run Contract

`schemas/run.schema.json` defines the variable inputs for one Gauntlet execution.
`templates/run.json` is a safe, consequence-free starting point.

## Variable per run

- Gauntlet evidence-ledger remote and branch.
- Product name, repository, branch, evidence mode, optional deployed URL, and backlog.
- Start/end dates, timezone, cutoff, and target focused hours.
- Public rubric, mastery template, and overall-score rule.
- Failure consequence and whether any consequence may execute automatically.
- Publishing mode, channels, and approval requirement.
- Deterministic/unit/integration/local-E2E commands and optional live-browser adapter.
- Grader, planner, and appeal-judge adapter commands.

The reusable skill and controller must not infer authority from a previous run. A new
run defaults to no automatic consequence and no publishing.

`project.evidence_mode = "repository-only"` requires `deployed_url = null` and disables
browser review. Only the two frozen remote commits, their committed artifacts, and
checks executed from the frozen product clone are eligible. A check marked
`infrastructure: true` provisions the offline test environment; failure is
`INFRA_ERROR`, not a delivery result.

## Cutoff and retry contract

Before tests or adapters, the controller creates an exclusive local freeze record and
pins ledger and product branch heads. The 00:15 and 00:30 retries reuse it. If the first
attempt cannot complete both pins, the record remains incomplete and later heads are
inadmissible. Losing or corrupting controller state is `INFRA_ERROR`.

Evidence is read from detached frozen commits. Controller reports are committed on top
of the then-current ledger head, preserving post-cutoff work while excluding it from the
grade. A matching finalized report makes every retry a no-op.

If a frozen verification command is operationally wrong, manual recovery may replace
only `verification.commands`. The controller rejects every broader configuration
change, continues to test the original frozen product and ledger SHAs, and records the
original commands, replacement commands, and both configuration hashes in evidence.
Automatic retries never opt into this recovery path.

## Adapter protocol

Every adapter is an executable command represented as an argument array. The controller
sends one UTF-8 JSON object on standard input and expects exactly one UTF-8 JSON object
on standard output. Diagnostic text belongs on standard error. A nonzero exit, timeout,
invalid JSON, or schema-invalid response is `INFRA_ERROR`.

The command is model-neutral: it may call a local model, hosted API, agent CLI, or a
test fixture. Secrets, including `OPENROUTER_API_KEY`, come from the controller environment and never from `run.json`,
evidence bundles, prompts, or reports.

## Authority boundary

`consequence.automatic_execution` and `publishing.mode` describe configured authority;
they do not grant it by themselves. Installation must separately provision narrowly
scoped credentials. Destructive reset behavior and automatic public posting require an
explicit setup action for that run and must produce an audit record.

The pilot uses:

- `consequence.mode = "none"`
- `consequence.automatic_execution = false`
- `publishing.mode = "disabled"` or `"draft-only"`
- `publishing.approval_required = true`
