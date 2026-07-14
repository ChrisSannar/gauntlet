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

Day 1's plan and mastery note are committed before launch. At midnight the controller
freezes both remote SHAs, grades the completed note, and creates the next day's plan and
mastery note. The learner completes and pushes `mastery.md` before midnight. It is never
stored in or deployed with the product.

The evidence bundle pins both the remote product commit and the Gauntlet repository
commit containing the plan and mastery note. Controller-generated reports are
append-only once finalized; corrections produce a new report rather than rewriting the
original.

The learner may submit at most one appeal for a finalized daily report using
`templates/daily-grade-appeal.md`. The appeal must itself be committed and pushed to
the Gauntlet repository, identify one disputed claim, and cite only the frozen bundle.
