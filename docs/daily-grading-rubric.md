# Daily Grading Rubric — v0.2

This is the public grading contract for the accountability pilot. The controller records
the rubric version with every grade. Revise the rubric only for future evidence windows;
never retroactively change the contract for a frozen day.

## Preconditions

- Grade only the day's frozen plan and frozen evidence bundle.
- Award no credit for time spent, code volume, or work pushed after the learner invokes
  `$gauntlet-grade`. Invocation must begin before the displayed cutoff and immediately
  freezes both remote heads. A recorded freeze may finish or retry after the cutoff.
- Do not require stretch work or invent acceptance criteria.
- Return `INFRA_ERROR` without a grade when controller, dependency cache, model, or local test
  infrastructure prevents a fair review.
- Cite evidence for every nonzero score and state confidence as low, medium, or high.

## Delivery — 0 to 4

Judge four observable dimensions: required outcomes, reproducible proof, material
failure handling, and scope integrity. A passing test supports only the behavior it
actually exercises. Unchecked claims, unpushed files, and unrelated feature volume do
not compensate for a missing required outcome.

### 4 — Excellent

Every required outcome works and has reproducible repository evidence. Deterministic
tests and local E2E checks agree. The implementation handles material failure cases within
the frozen scope without a known high-impact defect. Evidence is easy to rerun from the
frozen checkout and clearly maps each plan item to a check.

### 3 — Complete

Every required outcome is satisfied with credible committed repository evidence.
Required verification passes. Remaining issues are minor and do not break the promised
behavior. Failure-path evidence may be narrower than excellent work, but no required
boundary item depends on assertion alone.

### 2 — Partial

Meaningful required outcomes work, but at least one required outcome or important proof
is incomplete. The day produced usable progress but did not fully cross its boundary.
Use 2.5 when most required behavior is proven and the remaining gap is narrow; use 2.0
when the gap is material.

### 1 — Weak

Some relevant work exists, but most of the required boundary is missing, broken,
unverifiable, or off the critical path. Use 1.5 for a coherent partial vertical slice;
use 1.0 when evidence is fragmented or mostly scaffolding.

### 0 — No eligible delivery evidence

No remote-reachable product commit was frozen by the cutoff, or the evidence does not
demonstrate meaningful progress toward the required boundary.

### How to raise Delivery

1. Convert each required bullet into one observable behavior and one exact check.
2. Add the smallest negative-path test that would disprove the happy-path claim.
3. Run the repository commands from a clean checkout, not only a long-lived workspace.
4. Remove or defer unrelated work until every required check maps to the frozen plan.

## Mastery — 0 to 4

Judge five observable dimensions: system model, consequential reasoning, evidence-led
debugging, personal verification of AI work, and transfer. Prefer explanations that
name inputs, state changes, boundaries, failure modes, and observable outputs. Fluent
prose without concrete evidence is not mastery.

### 4 — Transferable

The mastery note and product evidence show accurate system understanding, explicit
tradeoffs, evidence-led debugging, and personal verification of AI contributions. The
learner connects the work to failure modes or principles that transfer beyond today's
exact implementation. The learner can predict a novel failure, design a check for it,
and explain what evidence would change the model.

### 3 — Demonstrated

The learner accurately explains an important behavior, justifies a consequential
decision, investigates a real uncertainty, and names concrete checks used to verify AI
output. No core explanation materially conflicts with the implementation. At least one
claim links an exact code path to a test, trace, query, or state transition.

### 2 — Developing

The note contains specific, partly correct understanding, but an important explanation,
tradeoff, root-cause model, or verification claim is shallow, unsupported, or mistaken.
Tomorrow's plan should include focused mastery proof. Use 2.5 when the model is largely
accurate but one dimension is thin; use 2.0 when multiple dimensions lack evidence.

### 1 — Weak

The note is mostly generic summary, unsupported assertion, or activity reporting. It
does not show reliable ownership of the implemented behavior. Use 1.5 when one concrete
explanation exists amid generic material; use 1.0 when concrete ownership is absent.

### 0 — No eligible mastery evidence

The required mastery note was not committed and pushed by the cutoff, or its content
provides no credible evidence of understanding.

### How to raise Mastery

1. Trace one real request from input through state changes to output and name the files.
2. Predict a failure before running a test; compare the prediction with the result.
3. Rebuild or explain one small AI-generated path without consulting the AI response.
4. Record what evidence changed your mind, not merely what tool you ran.
5. Transfer the principle by proposing a different system where it applies and one case
   where it does not.

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

Half-point scores mean the evidence sits meaningfully between adjacent anchors; they
are not a substitute for choosing an anchor. The report must name the higher anchor's
missing evidence.

## Required feedback

Every grade must include:

- evidence-backed strengths worth repeating;
- two to five ordered improvement actions tied to the weaker dimension;
- one to three learning directions, each describing deliberate practice and observable
  proof of improvement;
- evidence citations for the score and confidence level.

Advice must be actionable inside the repository. Prefer “write an invalid-token test,
predict the status code, then explain the authorization branch it exercises” over
“learn more about security.” Do not expand the already-frozen daily obligation when
giving improvement advice; the planner decides what becomes required tomorrow.

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
