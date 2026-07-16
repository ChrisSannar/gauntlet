# Participating in an Active Gauntlet Run

The daily plan is the frozen instruction contract. Do not infer extra requirements from
the broader backlog, and do not wait for a person or agent to start the day.

## Keep the repositories separate

The Gauntlet ledger owns `projects/`, `runs/`, controller automation, daily plans,
mastery notes, and grades. The product repository owns only application code,
application documentation, and repository-local tests or development tooling.

Do not clone or initialize the product repository inside `projects/`. A folder such as
`projects/tutoring-platform/` is ordinary ledger content and must not contain `.git`
metadata. Product-specific Gauntlet requirements belong there or under the active run,
never on a branch of the product remote.

## Start the day

From the Gauntlet ledger:

```bash
python -m controller.gauntlet_controller today runs/2026-07-15-tutoring-platform/run.json
```

Read three sections: required boundary, proof required, and scope guard. The boundary is
what must work today. Proof says how the repository must demonstrate it. The scope guard
prevents later-day or optional work from silently becoming required.

## Work

Work in the product repository on `main`. Use the tests and local E2E as feedback, but
the pushed product commit—not local uncommitted work—is eligible at submission. Finishing
early does not expand today's required boundary.

Record mastery evidence throughout the day in the exact `mastery.md` path printed by
`today`. Explain system behavior, consequential decisions, investigated uncertainty,
personal verification of AI output, and one transferable principle.

## Submit before the cutoff

Before the displayed cutoff:

1. Commit and push product work to product `main`.
2. Complete, commit, and push the day's `mastery.md` to ledger `master`.
3. Confirm both working trees are clean and tracking their remote branch.
4. Invoke `$gauntlet-grade`.

Invocation immediately freezes both remote SHAs, so do it only after the day's eligible
work is pushed. The controller runs deterministic verification, grades Delivery and
Mastery separately, commits the report, and creates the next day's plan. Work pushed
after invocation is not eligible even if it is still before midnight.

If grading has an infrastructure failure, do not manufacture or edit a grade. Invoke
`$gauntlet-grade` again. A retry after midnight is allowed only when the original
pre-cutoff receipt and complete freeze exist, and it uses only those original SHAs.
