# OTV2-20260810-stale-fnd-id-task-closeout

```yaml
task_id: OTV2-20260810-stale-fnd-id-task-closeout
title: Archive stale merged FND-ID support task records
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260810-stale-fnd-id-task-closeout
pr: null
base_sha: 8f5f20274aa8c886695fb36dfe14025f38f1ee1b
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT coordination session
created_at: 2026-08-10T22:40:00+02:00
updated_at: 2026-08-10T22:40:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260810-stale-fnd-id-task-closeout.md
  - docs/agents/tasks/active/OTV2-20260807-world-channel-uuidv7.md
  - docs/agents/tasks/active/OTV2-20260807-nodeid-incarnation.md
  - docs/agents/tasks/active/OTV2-20260807-instanceid-issuer.md
  - docs/agents/tasks/active/OTV2-20260807-partyid-issuer.md
  - docs/agents/tasks/active/OTV2-20260807-characterid-account-link.md
  - docs/agents/tasks/active/OTV2-20260807-fnd-id01-conversation-checkpoint.md
  - docs/agents/tasks/active/OTV2-20260807-account-single-online-character.md
  - docs/agents/tasks/active/OTV2-20260807-duplicate-login-combat-takeover.md
  - docs/agents/tasks/active/OTV2-20260807-combat-takeover-incumbent-protection.md
  - docs/agents/tasks/active/OTV2-20260807-game-session-reconnect-generation.md
  - docs/agents/tasks/archive/OTV2-20260807-world-channel-uuidv7.md
  - docs/agents/tasks/archive/OTV2-20260807-nodeid-incarnation.md
  - docs/agents/tasks/archive/OTV2-20260807-instanceid-issuer.md
  - docs/agents/tasks/archive/OTV2-20260807-partyid-issuer.md
  - docs/agents/tasks/archive/OTV2-20260807-characterid-account-link.md
  - docs/agents/tasks/archive/OTV2-20260807-fnd-id01-conversation-checkpoint.md
  - docs/agents/tasks/archive/OTV2-20260807-account-single-online-character.md
  - docs/agents/tasks/archive/OTV2-20260807-duplicate-login-combat-takeover.md
  - docs/agents/tasks/archive/OTV2-20260807-combat-takeover-incumbent-protection.md
  - docs/agents/tasks/archive/OTV2-20260807-game-session-reconnect-generation.md
public_contracts: []
depends_on:
  - merged PRs 64 through 73
  - FND-ID-01 lifecycle closeout PR 87
blocks:
  - truthful FND-ID-01 lifecycle-closed status in PR 145
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Remove ten stale advisory ownership records from `tasks/active/` after proving their delivery PRs are already merged, while preserving each historical task as an archive record with immutable PR/head/merge evidence. This is lifecycle bookkeeping only and changes no architecture or runtime authority.

## Architecture and source of truth

- `PROVEN`: PRs #64 through #73 are merged and their feature/contract changes already live in `main` history.
- `PROVEN`: FND-ID-01 lifecycle closeout PR #87 is merged.
- `PROVEN`: the ten corresponding support task records still remain under `docs/agents/tasks/active/`, so they retain stale advisory ownership despite terminal delivery.
- `DERIVED`: archiving these records removes stale coordination locks and makes the current lifecycle-closed FND-ID status truthful without changing any accepted semantic contract.
- `PROVEN`: PR #145 independently owns the stale PR #63 protocol-reconciliation record, so this cleanup deliberately does not touch that path.

## Acceptance criteria

- [ ] Archive exactly the ten proven-merged stale task records listed in `owned_paths`.
- [ ] Preserve original task IDs plus associated PR, final head and merge commit evidence.
- [ ] Remove the ten matching active records.
- [ ] Do not edit architecture/runtime/contracts or the PR #63 reconciliation task owned by PR #145.
- [ ] Full-diff self-review reports zero material findings.
- [ ] Exact-head governance/document checks pass.

## Excluded scope

- no architecture or semantic contract changes;
- no runtime code;
- no production/live changes;
- no cleanup of owner-accepted lag/disconnect analysis checkpoints;
- no PR #63 task cleanup because PR #145 already owns it;
- no broad active-task purge without merged-delivery evidence.

## Implementation / findings

Pending archive/delete operation.

## Validation

### Focused

- merged-delivery evidence: PRs #64-#73 and PR #87 verified through GitHub connector
- result: PASS for task selection

### Component/integration

- result: `NOT_APPLICABLE` — lifecycle documentation only

### E2E

- result: `NOT_APPLICABLE` — no executable product behavior

### Exact-head CI

- final head: pending
- trigger source: pull_request
- result: pending

## Self-review

- exact head: pending
- method/reviewer: implementing/coordinating agent (mandatory; cannot be delegated away)
- material findings: pending
- verdict: pending

## Independent review

- required: `NO` — this is exactly low-risk stale-task bookkeeping, changes no semantic/security/authority/runtime contract, and no owner/contract explicitly requires independent review
- exact head: `NOT_APPLICABLE`
- method/auditor: `NOT_APPLICABLE`
- material findings: `NOT_APPLICABLE`
- verdict: `NOT_APPLICABLE`

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: PR #145 depends on this cleanup but owns no overlapping path except the intentionally excluded PR #63 task
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Created bounded stale-task lifecycle cleanup after risk-based governance became authoritative on main.
status: implementing
branch: docs/OTV2-20260810-stale-fnd-id-task-closeout
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
next_action: Archive and delete exactly the ten proven-merged stale support task records in one coherent cleanup.
```
