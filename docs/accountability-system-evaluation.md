# Accountability System Evaluation

The trial week evaluates the accountability system as a reusable product, not only the
configured application it grades. Preserve raw daily evidence and record failures; do
not rewrite history to make the pilot look cleaner.

## Daily data to retain

- Trigger time, completion time, retry count, and controller version.
- Frozen plan hash, product remote/branch/SHA, and Gauntlet evidence commit SHA.
- Deterministic test and E2E commands, exit codes, durations, and artifact locations.
- Deployed URL and browser-review artifacts.
- Configured model adapter and model identifier, without secrets.
- Delivery score, Mastery score, overall grade, confidence, and cited evidence.
- Rubric and prompt versions plus any cross-model score disagreement.
- Planner inputs, next-plan output, estimated difficulty, and learner-reported effort.
- Infrastructure errors distinguished from learner evidence failures.
- Appeals, decisions, judge identity, disposition, and time required to appeal.

## Reuse criteria

### 1. Autonomous enforcement

The controller runs at the cutoff without a learner request. Avoidance, a sleeping
laptop, or forgetting a command cannot suppress the review.

### 2. Evidence integrity

Every verdict points to the frozen plan, a remote-reachable commit, reproducible command
results, and durable artifacts. Later work cannot change an earlier grade.

### 3. Reproducibility and model portability

The same evidence bundle can be regraded. Switching providers requires configuration,
not changes to scheduling, evidence collection, schemas, or rubric semantics.

### 4. Grading fairness

Delivery and Mastery remain distinct. Mechanical facts come from deterministic checks;
subjective claims cite evidence and include confidence. Infrastructure failures never
masquerade as learner failures.

### 5. Calibration quality

The planner responds differently to incomplete delivery, weak mastery, quick high-
quality completion, and genuine blockers. Tomorrow's boundary changes without moving
today's frozen line.

### 6. Actionability

The report makes the next corrective action obvious. Feedback is concise enough to use
the following morning and specific enough to verify.

### 7. Portability and setup burden

A new project supplies configuration, commands, rubric, and backlog without forking the
controller. Installation and recovery are documented and can be rehearsed from zero.

### 8. Safety and authority

The grader remains read-only toward the product repository. Publishing, deployment,
and other external mutations require separately configured authority and audit trails.

### 9. Appeal resistance and correction quality

Measure whether legitimate factual errors can be corrected from frozen evidence without
making broad grade shopping easy. Record denied, accepted, and abandoned appeals plus
the learner effort required to file them.

## End-of-pilot evaluation

At the end of the configured run, assess each criterion with evidence, list every manual
intervention, compare at least one frozen bundle across two model configurations when
feasible, and produce a prioritized change list before the full Gauntlet begins.
