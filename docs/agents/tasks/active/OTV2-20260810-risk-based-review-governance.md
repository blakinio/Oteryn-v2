# OTV2-20260810-risk-based-review-governance

```yaml
task_id: OTV2-20260810-risk-based-review-governance
title: Make independent review risk-based and Codex optional
mode: GOVERNANCE
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260810-risk-based-review-governance
pr: 146
base_sha: 9794e9a6307b6f9db193ca2ce08607eb065b7d7e
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT governance coordinator
created_at: 2026-08-10T22:10:00+02:00
updated_at: 2026-08-10T22:27:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - AGENTS.md
  - docs/agents/TASK_CLOSEOUT_AUDIT_E2E.md
  - docs/agents/DELIVERY_COMPLETENESS_AND_CLOSEOUT.md
  - docs/agents/ANTI_STALL_AND_EXECUTION_BUDGET.md
  - docs/agents/EXECUTION_PROTOCOL.md
  - docs/agents/tasks/TASK_TEMPLATE.md
  - docs/agents/tasks/active/OTV2-20260810-risk-based-review-governance.md
public_contracts:
  - AGENTS.md
  - docs/agents/TASK_CLOSEOUT_AUDIT_E2E.md
  - docs/agents/DELIVERY_COMPLETENESS_AND_CLOSEOUT.md
  - docs/agents/ANTI_STALL_AND_EXECUTION_BUDGET.md
  - docs/agents/EXECUTION_PROTOCOL.md
  - docs/agents/tasks/TASK_TEMPLATE.md
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

- `PROVEN`: trusted-base root governance requires an independent audit in the default delivery workflow and before terminal closeout.
- `PROVEN`: additional trusted-base policies also repeated that universal independent-audit requirement in anti-stall, execution protocol and the task template.
- `PROVEN`: Codex is not a runtime/build dependency and is not named as the sole permitted auditor.
- `OWNER_ACCEPTED`: the repository owner explicitly instructed on 2026-08-10 to use Codex only when necessary.
- `OWNER_ACCEPTED`: the implementing agent may and should perform its own review/audit, but must not label that self-review independent.
- `DERIVED`: a universal independent-review requirement adds unnecessary latency to low-risk documentation/coordination changes while giving little incremental safety when exact-head validation plus full-diff self-review already proves the relevant scope.
- `DERIVED`: high-risk auth/session/protocol/persistence/economy/security/production/governance-authority changes continue to justify an independent second perspective.

## Acceptance criteria

- [x] Require full-diff self-review for every task before readiness.
- [x] Define explicit conditions that require independent review.
- [x] Keep independent review mandatory for high-risk authority/security/durable-data/production and safety-reducing governance changes.
- [x] State that Codex is optional and may be invoked only when independent review is actually required by policy/owner/contract and Codex is the necessary or appropriate available independent mechanism for that requirement.
- [x] Permit human reviewer, separate agent/session, Codex or dedicated independent audit workflow when independence and evidence are real.
- [x] Forbid claiming self-review as independent review.
- [x] Preserve exact-head CI/E2E, no-bypass, ownership and merge protection.
- [x] Reconcile anti-stall, execution-protocol and task-template wording so no more-restrictive universal independent-audit rule silently overrides this policy.
- [ ] Run final exact-head governance checks and independent review of this governance-safety change before merge.

## Excluded scope

- no weakening of exact-head required checks;
- no bypass of branch protection/review threads/E2E;
- no production authority expansion;
- no change to runtime code or architecture contracts;
- no claim that Codex is unavailable or prohibited.

## Implementation / findings

- Root `AGENTS.md` makes full-diff self-review mandatory for every task and defines high-risk/explicit conditions requiring a genuine independent second review.
- `TASK_CLOSEOUT_AUDIT_E2E.md` mirrors the self-review versus risk-based independent-review distinction.
- `DELIVERY_COMPLETENESS_AND_CLOSEOUT.md` applies the distinction to final-head evidence and merge readiness.
- `ANTI_STALL_AND_EXECUTION_BUDGET.md`, `EXECUTION_PROTOCOL.md` and `TASK_TEMPLATE.md` no longer contain a conflicting universal-audit requirement.
- Independent mechanisms may be human, separate non-authoring agent/session, Codex or a dedicated audit workflow; Codex is optional by name and cannot be used merely for extra assurance when independent review is not required.
- Initial exact-head Codex review on `910ee7ff53394748caba9a630f10cea8467d960d` found one P2: three additional policies/template still imposed/assumed a universal independent audit. Repair cycle 1 aligned those files.
- Owner-instruction reconciliation then tightened the wording so Codex itself may be invoked only to satisfy an actually required independent-review gate. This is repair cycle 2 and does not change which high-risk areas require independence.
- This governance change is itself safety-sensitive because it narrows when independent review is mandatory. The owner explicitly authorized it, but the trusted-base rules governing this task still require independent review. Therefore Codex is necessary for PR #146 even though the resulting steady-state policy avoids routine Codex use.

## Validation

### Focused

- final scope is seven declared governance/task/template paths.
- self-review: no runtime/architecture/production authority change; exact-head CI/E2E/no-bypass rules remain mandatory; high-risk and safety-reducing changes retain independent-review requirement; Codex use is stricter than the initial candidate and matches the explicit owner instruction.
- result: PASS pending final exact-head repository checks.

### Component/integration

- result: `NOT_APPLICABLE` — governance documentation only.

### E2E

- result: `NOT_APPLICABLE` — no executable product behavior.

### Exact-head CI

- pre-repair head `910ee7ff53394748caba9a630f10cea8467d960d`: Agent Governance `31428208991` PASS; Dependency Review `31428211275` PASS; CodeQL `31428208971` PASS; superseded.
- repair-cycle-1 head `245e07ce7d0095dedd4b0756de3bc792ef44a805`: checks started but are superseded by owner-instruction wording repair.
- final head: pending after this checkpoint commit; previous results do not substitute.

## Self-review

- exact head: pending final head
- method/reviewer: implementing governance coordinator full-diff adversarial review
- material findings: zero known after owner-instruction reconciliation; final recheck pending
- verdict: pending exact-head recheck

## Independent review

- required: `YES` — trusted-base governance plus safety-gate reduction
- exact head: initial review on `910ee7ff53394748caba9a630f10cea8467d960d` found one P2 and is superseded by repairs
- method/auditor: Codex independent PR review because an independent mechanism is required for this governance change
- material findings: one P2 repaired; final-head review pending
- verdict: pending

## PR and closeout

- changed-file review: final seven-path scope pending exact-head recheck
- unresolved review threads: initial P2 resolved after repair; final review pending
- related/superseded PRs: PR #145 is independent architecture work and does not overlap these governance paths
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Repair cycle 2 enforces the owner's stricter rule that Codex is used only to satisfy an actually required independent-review gate.
status: validating
branch: docs/OTV2-20260810-risk-based-review-governance
head_sha: null
pr: 146
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: pull_request
ci_check_generation: final-head-pending
ci_checks_for_current_head: 0
ci_run_ids: []
ci_job_ids: []
runner_assignment_state: unknown
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 2
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: null
blocker: null
next_action: Verify final exact-head CI and obtain one final independent review for PR #146; merge only if no material finding remains.
```
