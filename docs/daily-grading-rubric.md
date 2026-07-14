# Daily Grading Rubric — Pilot v0.1

This is the public grading contract for the accountability pilot. The controller records
the rubric version with every grade. Revise the rubric only for future evidence windows;
never retroactively change the contract for a frozen day.

## Preconditions

- Grade only the day's frozen plan and frozen evidence bundle.
- Award no credit for time spent, code volume, or work pushed after midnight.
- Do not require stretch work or invent acceptance criteria.
- Return `INFRA_ERROR` without a grade when controller, network, model, or browser
  infrastructure prevents a fair review.
- Cite evidence for every nonzero score and state confidence as low, medium, or high.

## Delivery — 0 to 4

### 4 — Excellent

Every required outcome works and has reproducible evidence. The deployed critical path,
tests, and E2E checks agree. The implementation handles material failure cases within
the frozen scope without a known high-impact defect.

### 3 — Complete

Every required outcome is satisfied with credible committed and deployed evidence.
Required verification passes. Remaining issues are minor and do not break the promised
behavior.

### 2 — Partial

Meaningful required outcomes work, but at least one required outcome or important proof
is incomplete. The day produced usable progress but did not fully cross its boundary.

### 1 — Weak

Some relevant work exists, but most of the required boundary is missing, broken,
unverifiable, or off the critical path.

### 0 — No eligible delivery evidence

No remote-reachable product commit was frozen by the cutoff, or the evidence does not
demonstrate meaningful progress toward the required boundary.

## Mastery — 0 to 4

### 4 — Transferable

The mastery note and product evidence show accurate system understanding, explicit
tradeoffs, evidence-led debugging, and personal verification of AI contributions. The
learner connects the work to failure modes or principles that transfer beyond today's
exact implementation.

### 3 — Demonstrated

The learner accurately explains an important behavior, justifies a consequential
decision, investigates a real uncertainty, and names concrete checks used to verify AI
output. No core explanation materially conflicts with the implementation.

### 2 — Developing

The note contains specific, partly correct understanding, but an important explanation,
tradeoff, root-cause model, or verification claim is shallow, unsupported, or mistaken.
Tomorrow's plan should include focused mastery proof.

### 1 — Weak

The note is mostly generic summary, unsupported assertion, or activity reporting. It
does not show reliable ownership of the implemented behavior.

### 0 — No eligible mastery evidence

The required mastery note was not committed and pushed by the cutoff, or its content
provides no credible evidence of understanding.

## Overall grade

Score each dimension independently in increments of 0.5. The overall numeric score is
the lower of Delivery and Mastery.

| Lower score | Overall grade |
|---:|:---|
| 3.5–4.0 | A |
| 3.0 | B |
| 2.0–2.5 | C |
| 1.0–1.5 | D |
| 0.0–0.5 | F |

The report must show both dimension scores even when they yield the same letter. The
adaptive planner uses the separate scores, cited gaps, effort telemetry, and stretch
completion; it does not plan from the letter alone.

## Fairness and calibration

- Keep deterministic facts separate from LLM judgment.
- Quote or link the exact evidence supporting each anchor selection.
- Record model adapter, model identifier, rubric version, and prompt version.
- Preserve the original report. A correction or regrade appends a new report.
- Compare selected frozen bundles across models during the pilot and record disagreement
  without changing the original grade merely to force consensus.
- Evaluate rubric behavior using `docs/accountability-system-evaluation.md` after the
  configured run ends.

## Appeal contract

- Permit at most one learner-initiated appeal per finalized daily report.
- Require `templates/daily-grade-appeal.md`, committed and pushed in that day's
  `appeals/` folder.
- Accept only a specific factual error, evidence omission, rubric misapplication, or
  arithmetic error. Reject general regrade requests.
- Use only the original frozen evidence. New commits, explanations, deployments, and
  post-cutoff artifacts are inadmissible.
- Have a separate configured judge review the disputed claim and requested correction.
- Preserve the original report and append the appeal decision. Do not overwrite history.
- Allow no second learner appeal for that report during the pilot.
- Automatically send low-confidence grades to a second model pass without requiring an
  appeal. If dimension scores disagree by more than 0.5, mark `REVIEW_NEEDED`; do not
  silently average the results.
- Apply no grade penalty for a denied good-faith appeal. The required specificity,
  frozen-evidence constraint, committed artifact, and one-appeal limit provide friction
  without discouraging legitimate corrections.
