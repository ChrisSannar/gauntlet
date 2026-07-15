---
name: gauntlet-today
description: Print the active Gauntlet run's frozen daily instructions, required proof, scope guard, cutoff, mastery-note path, and submission checklist. Use when the learner invokes $gauntlet-today or asks what to do today in the active Gauntlet.
---

# Gauntlet Today

Run the deterministic bundled script from the repository root:

```bash
python .agents/skills/gauntlet-today/scripts/gauntlet_today.py
```

Return its stdout verbatim. Do not load run documents, summarize the output, grade work,
change the frozen boundary, or invoke an LLM adapter.

If the user supplies a specific `run.json`, pass it as the sole argument. Otherwise let
the script discover the single active run.
