---
name: gauntlet-grade
description: Submit and grade the active Gauntlet day from committed-and-pushed evidence. Use when the learner invokes $gauntlet-grade, asks to submit today's Gauntlet work, requests the daily grade, or needs to retry a grading attempt whose pre-cutoff receipt already exists.
---

# Gauntlet Grade

Warn once that invocation immediately freezes the pushed product and ledger SHAs. Then
run the deterministic bundled script from the Gauntlet repository root:

```bash
python .agents/skills/gauntlet-grade/scripts/gauntlet_grade.py
```

Do not edit, commit, push, or repair learner work before submission. The script must be
invoked before the configured cutoff for a new submission. Once its immutable receipt
and freeze exist, allow the same command to finish or retry after the cutoff.

Return the script output. Treat exit code 2 as `INFRA_ERROR`, never as a learner grade.
If the user supplies a specific `run.json`, pass it as the sole argument.
