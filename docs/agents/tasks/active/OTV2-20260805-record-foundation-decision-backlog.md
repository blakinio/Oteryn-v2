# OTV2-20260805-record-foundation-decision-backlog

```yaml
task_id: OTV2-20260805-record-foundation-decision-backlog
title: Record current foundation decision backlog
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/foundation-decision-backlog-20260805
pr: null
base_sha: 083d68308549d7fa7e486a464f279e42b2f6a96e
head_sha: null
owner: chatgpt-github-agent
created_at: 2026-08-05T10:11:00+02:00
updated_at: 2026-08-05T10:11:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/agents/tasks/active/OTV2-20260805-foundation-preimplementation-contracts.md
  - docs/agents/tasks/active/OTV2-20260805-record-foundation-decision-backlog.md
  - docs/agents/evidence/OTV2-20260805-foundation-original-handoff.md
public_contracts:
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/agents/tasks/active/OTV2-20260805-foundation-preimplementation-contracts.md
depends_on:
  - ADR-0001 through ADR-0004
blocks: []
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/Oteryn-Platform
  - blakinio/Otheryn
  - blakinio/otclient
```

## Outcome

Persist the remaining decision list from the owner discussion and reconcile the active foundation checkpoint with ADR-0002 through ADR-0004.

The delivered repository state must:

- identify decisions already accepted;
- order the decisions that block the real Rust workspace;
- identify decisions required before durable gameplay;
- preserve explicitly deferred subjects;
- make Workspace and Dependency Contract the exact next action;
- preserve the original detailed handoff unchanged for traceability.

## Architecture and source of truth

### PROVEN

- ADR-0002 accepted migration of the native Rust client into `blakinio/Oteryn-v2`.
- ADR-0003 accepted the Platform Identity/Game Gateway boundary and retained the initial Go Gateway.
- ADR-0004 selected PostgreSQL with separate Platform/game database ownership.
- The active foundation task still contained a historical `UNKNOWN` list from before those ADRs were accepted.

### DERIVED

- A current ordered backlog is required to prevent agents from treating resolved decisions as open or beginning workspace implementation before protocol/runtime/admission gates are accepted.

## Acceptance criteria

- [ ] `FOUNDATION_DECISION_BACKLOG.md` records accepted, blocking, pre-durable, expansion and deferred decisions.
- [ ] The active foundation task no longer lists client repository ownership or database technology as unknown.
- [ ] The active foundation task points to Workspace and Dependency Contract as the next action.
- [ ] The complete original handoff is preserved unchanged under `docs/agents/evidence/`.
- [ ] No external repository is modified.
- [ ] Full changed-file audit has zero open material findings.
- [ ] Exact-head `Agent governance` passes.
- [ ] PR is squash-merged and this task is archived.

## Excluded scope

- no workspace or Rust code;
- no client migration;
- no protocol/runtime/session/persistence implementation;
- no external-repository write;
- no database migration or provisioning.

## Implementation / findings

- pending initial commit

## Validation

### Focused

- workflow: `Agent governance`
- result: pending

### Component/integration

- result: `NOT_APPLICABLE` — documentation-only contract reconciliation

### E2E

- result: `NOT_APPLICABLE` — no executable runtime change

### Exact-head CI

- head: pending
- run: pending
- result: pending

## Independent audit

- exact head: pending
- method: adversarial full-diff review against ADR-0001 through ADR-0004 and the original handoff
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: The recording task was created and owns the current backlog, reconciled foundation checkpoint and preserved original handoff.
status: implementing
branch: docs/foundation-decision-backlog-20260805
head_sha: null
pr: null
ci_check_generation: null
ci_checks_for_current_head: 0
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 0
stall_warnings: 0
blocker: null
next_action: Commit the backlog, reconciled checkpoint and preserved original handoff.
```
