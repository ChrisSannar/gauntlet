# Gauntlet Run Evidence

Each execution stores learner-authored evidence and controller results outside the
graded product repository:

```text
runs/<run-id>/
  run.json
  days/<YYYY-MM-DD>/
    plan.md
    mastery.md
    evidence.json
    grade.json
    grade.md
    appeals/
      appeal-01.md
      decision-01.md
```

Day 1's plan and mastery note are committed before launch. At the end of each workday,
the learner invokes `$gauntlet-grade` before the cutoff. The controller records the
invocation, freezes both remote SHAs, grades the completed note, and creates the next
day's plan and mastery note. The note is never stored in or deployed with the product.

The evidence bundle pins both the remote product commit and the Gauntlet repository
commit containing the plan and mastery note. Controller-generated reports are
append-only once finalized; corrections produce a new report rather than rewriting the
original.

The learner may submit at most one appeal for a finalized daily report using
`templates/daily-grade-appeal.md`. The appeal must itself be committed and pushed to
the Gauntlet repository, identify one disputed claim, and cite only the frozen bundle.

For the daily learner ritual, see [`docs/participating-in-a-run.md`](../docs/participating-in-a-run.md)
and run `python -m controller.gauntlet_controller today <run.json>`.
