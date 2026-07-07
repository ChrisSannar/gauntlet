# The Gauntlet — AI × EdTech

Start with [`CURRICULUM.md`](CURRICULUM.md). Decisions: [`docs/adr/`](docs/adr/).
Vocabulary: [`docs/GLOSSARY.md`](docs/GLOSSARY.md).

## Layout

- `specs/` — what to build, per project, with weekly milestones. **Read these.**
- `.grading/` — hidden rubrics + grader protocol. **Chris: never open this folder.**
- `submissions/` — Chris writes `week-NN.md` here to request grading (format below).
- `grades/` — the grader writes its reports here. Chris may read his reports.

## Requesting a grade

Create `submissions/week-NN.md` containing:

```markdown
# Week NN Submission — attempt M
- Project repo: <path or URL>
- Commit SHA: <sha being graded>
- Deployed URL: <public URL>
- Run locally: <exact commands>
- Run evals/tests: <exact commands>
- Artifact index: <paths to brief, ADRs, eval reports, critique, etc.>
- Notes: <anything the grader needs (test credentials, etc.)>
```

Then invoke the grader (opencode + GLM or any capable model) with:

> You are the Gauntlet grader. Read `.grading/README.md` and follow it exactly to
> grade the submission in `submissions/week-NN.md`.

Unlimited attempts until midnight of day 7. Pass = C or better. Below C at the
deadline = reset (ADR 0003).
