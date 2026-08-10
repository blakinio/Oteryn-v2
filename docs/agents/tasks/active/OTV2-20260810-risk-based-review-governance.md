# OTV2-20260810-risk-based-review-governance

```yaml
task_id: OTV2-20260810-risk-based-review-governance
title: Make independent review risk-based and Codex optional
mode: GOVERNANCE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260810-risk-based-review-governance
pr: null
base_sha: 9794e9a6307b6f9db193ca2ce08607eb065b7d7e
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT governance coordinator
created_at: 2026-08-10T22:10:00+02:00
updated_at: 2026-08-10T22:10:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - AGENTS.md
  - docs/agents/TASK_CLOSEOUT_AUDIT_E2E.md
  - docs/agents/DELIVERY_COMPLETENESS_AND_CLOSEOUT.md
  - docs/agents/tasks/active/OTV2-20260810-risk-based-review-governance.md
public_contracts:
  - AGENTS.md
  - docs/agents/TASK_CLOSEOUT_AUDIT_E2E.md
depends_on:
  - owner instruction on 2026-08-10 to use Codex only when necessary
blocks:
  - unnecessary Codex dependency for low-risk Oteryn-v2 work
cross_repository_coordination_id: null
external_repositories: []
```

## Outcome

Replace the universal independent-audit requirement with a risk-based review policy without weakening self-review, exact-head CI/E2E, ownership, branch protection or high-risk review. Every task gets mandatory full-diff self-review. Independent review is required when a governing contract/owner explicitly requires it, for high-risk security/authority/data/production changes, for safety/governance reductions or authority expansion, or when unresolved uncertainty/material complexity makes a second perspective necessary. Codex is one optional independent-review mechanism, never a named mandatory dependency.

## Architecture and source of truth

- `PROVEN`: current root governance requires an independent audit in the default delivery workflow and before terminal closeout.
- `PROVEN`: Codex is not a runtime/build dependency and is not named as the sole permitted auditor.
- `OWNER_ACCEPTED`: the repository owner explicitly instructed on 2026-08-10 to use Codex only when necessary.
- `OWNER_ACCEPTED`: the implementing agent may and should perform its own review/audit, but must not label that self-review independent.
- `DERIVED`: a universal independent-review requirement adds unnecessary latency to low-risk documentation/coordination changes while giving little incremental safety when exact-head CI plus full-diff self-review already proves the relevant scope.
- `DERIVED`: high-risk auth/session/protocol/persistence/economy/security/production/governance-authority changes continue to justify an independent second perspective.

## Acceptance criteria

- [ ] Require full-diff self-review for every task before readiness.
- [ ] Define explicit conditions that require independent review.
- [ ] Keep independent review mandatory for high-risk authority/security/durable-data/production and safety-reducing governance changes.
- [ ] State that Codex is optional and should be used only when an independent reviewer is required and no sufficient already-available reviewer/mechanism exists, or when risk materially benefits from it.
- [ ] Permit human reviewer, separate agent/session, Codex or dedicated independent audit workflow when independence and evidence are real.
- [ ] Forbid claiming self-review as independent review.
- [ ] Preserve exact-head CI/E2E, no-bypass, ownership and merge protection.
- [ ] Run governance validation and independent review of this governance-safety change before merge.

## Excluded scope

- no weakening of exact-head required checks;
- no bypass of branch protection/review threads/E2E;
- no production authority expansion;
- no change to runtime code or architecture contracts;
- no claim that Codex is unavailable or prohibited.

## Implementation / findings

This governance change is itself safety-sensitive because it narrows when independent review is mandatory. The owner explicitly authorized the policy change, but the current trusted-base governance still requires independent review for this PR. Therefore Codex (or another genuinely independent reviewer) is necessary for this one governance delivery even though the new steady-state policy makes it optional by name.

## Validation

### Focused

- command/run: pending governance diff review
- result: pending

### Component/integration

- result: `NOT_APPLICABLE` — governance documentation only

### E2E

- result: `NOT_APPLICABLE` — no executable product behavior

### Exact-head CI

- final head: pending
- trigger source: pull_request
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: required under trusted-base governance because this change reduces a universal safety gate
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: PR #145 is independent architecture work and does not overlap these governance paths
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Dedicated governance branch and task created from trusted main after explicit owner instruction.
status: implementing
branch: docs/OTV2-20260810-risk-based-review-governance
head_sha: null
pr: null
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: null
ci_check_generation: null
ci_checks_for_current_head: 0
ci_run_ids: []
ci_job_ids: []
runner_assignment_state: unknown
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 0
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: null
blocker: null
next_action: Update the three governance documents with the owner-approved risk-based review policy.
```
