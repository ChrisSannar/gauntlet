# Gauntlet Run Evidence

Each execution stores learner-authored evidence and controller results outside the
graded product repository:

```text
runs/<run-id>/
  run.yaml
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

The controller creates the day folder, freezes `plan.md` from
`templates/daily-plan.md`, and copies `templates/daily-mastery-note.md` to
`mastery.md`. The learner completes and pushes `mastery.md` before midnight. It is
never deployed with the product.

The evidence bundle pins both the remote product commit and the Gauntlet repository
commit containing the plan and mastery note. Controller-generated reports are
append-only once finalized; corrections produce a new report rather than rewriting the
original.

The learner may submit at most one appeal for a finalized daily report using
`templates/daily-grade-appeal.md`. The appeal must itself be committed and pushed to
the Gauntlet repository, identify one disputed claim, and cite only the frozen bundle.
