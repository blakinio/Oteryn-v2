# OTV2-20260806-governance-ci-recovery

```yaml
task_id: OTV2-20260806-governance-ci-recovery
title: Harden exact-head governance CI recovery
mode: GOVERNANCE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: governance/ci-recovery-hardening-20260806
pr: null
base_sha: 26b5fa275fba19fdee0e26a6f65263489af3e500
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT governance coordinator
created_at: 2026-08-06T20:47:00+02:00
updated_at: 2026-08-06T20:47:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - .github/workflows/agent-governance.yml
  - docs/agents/ANTI_STALL_AND_EXECUTION_BUDGET.md
  - docs/agents/DELIVERY_COMPLETENESS_AND_CLOSEOUT.md
  - docs/agents/GITHUB_ONLY_EXECUTION.md
  - docs/agents/SESSION_RECOVERY_AND_ORPHANED_EXECUTION.md
  - docs/agents/tasks/TASK_TEMPLATE.md
  - docs/agents/tasks/active/OTV2-20260806-governance-ci-recovery.md
public_contracts: []
depends_on: []
blocks: []
cross_repository_coordination_id: null
external_repositories: []
```

## Outcome

Prevent exact-head closeout loops caused by connector-suppressed workflow events, runner starvation and CI-nudge commits while preserving the protected `Agent governance / validate` merge gate.

## Architecture and source of truth

- `PROVEN`: main requires `Agent governance / validate` and allows no routine bypass.
- `PROVEN`: the workflow already supports `workflow_dispatch`, but the dispatch path does not verify an open PR, same-repository head or expected SHA.
- `PROVEN`: a queued job may remain unassigned with `runner_id = 0` and no steps started.
- `DERIVED`: agents need an explicit classification and recovery order that does not mutate a frozen head merely to create another event.

## Acceptance criteria

- [ ] Define a final-head freeze that forbids CI-nudge commits and duplicate replacement PRs used only to regenerate checks.
- [ ] Distinguish event suppression, runner starvation and an executed workflow failure.
- [ ] Define one bounded recovery path and an exact owner-action blocker when the connector lacks dispatch/cancel operations.
- [ ] Harden manual governance dispatch with required PR number and expected 40-character head SHA.
- [ ] Verify the dispatched PR is open, targets `main`, comes from `blakinio/Oteryn-v2` and still has the expected head.
- [ ] Run governance and repository-policy validation on the exact final head.
- [ ] Preserve the required check name `Agent governance / validate` and all branch protections.

## Excluded scope

- no ruleset bypass or weakening;
- no automatic success status creation;
- no `pull_request_target` execution of untrusted PR code;
- no external repository changes;
- no modification of UUIDv7 architecture PR content.

## Implementation / findings

Task scope claimed. Implementation pending.

## Validation

### Focused

- command/run: pending
- result: pending

### Component/integration

- command/run: pending
- result: pending

### E2E

- scenario: manual-dispatch validation of an open same-repository PR at an exact SHA
- result: pending

### Exact-head CI

- head: pending
- workflow/run: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: pending
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: UUIDv7 PR #57 is related only as incident evidence and must not be modified
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Claimed the bounded governance and workflow recovery scope.
status: implementing
branch: governance/ci-recovery-hardening-20260806
head_sha: null
pr: null
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: null
ci_check_generation: null
ci_checks_for_current_head: 0
ci_run_ids: []
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
next_action: Create the PR, then apply the atomic governance hardening patch.
```
