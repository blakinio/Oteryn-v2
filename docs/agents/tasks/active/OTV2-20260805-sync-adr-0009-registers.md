# OTV2-20260805-sync-adr-0009-registers

```yaml
task_id: OTV2-20260805-sync-adr-0009-registers
title: Synchronize ADR-0009 across canonical architecture registers
mode: REPAIR
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/sync-adr-0009-registers
pr: null
base_sha: 96c605c9fabc3266eca9dd7f0010c97e88fd057c
head_sha: null
owner: GPT-5.6-Thinking-architecture-coordinator
created_at: 2026-08-05T20:42:00+02:00
updated_at: 2026-08-05T20:42:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
  - docs/architecture/MULTICHANNEL_SYSTEM_SCOPE_MATRIX.md
  - docs/agents/tasks/active/OTV2-20260805-sync-adr-0009-registers.md
  - .github/workflows/temporary-sync-adr-0009.yml
public_contracts:
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
  - docs/architecture/MULTICHANNEL_SYSTEM_SCOPE_MATRIX.md
depends_on:
  - ADR-0009
  - PR #37 merged as 96c605c9fabc3266eca9dd7f0010c97e88fd057c
blocks: []
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Make the canonical architecture indexes and multichannel terminology accurately reflect the already accepted ADR-0009 GameNode execution, capacity, deployment and recovery baseline, without changing runtime code or accepting new numerical capacity claims.

## Architecture and source of truth

### PROVEN

- ADR-0009 is accepted on `main` through PR #37 and defines `PERF-01` and `OPS-CHANNEL-01` as follow-up gates.
- `GLOBAL_ARCHITECTURE_DECISION_REGISTER.md` lists ADR-0008 but omits ADR-0009 and the two follow-up gates.
- `FOUNDATION_DECISION_BACKLOG.md` still identifies ADR-0001 through ADR-0007 as the canonical accepted range and omits ADR-0008, ADR-0009, `PERF-01` and `OPS-CHANNEL-01`.
- `MULTICHANNEL_SYSTEM_SCOPE_MATRIX.md` describes `Node` as physical placement, while ADR-0009 clarifies that `GameNode` is the logical runtime identity of one game-server process identified by `NodeId`, distinct from host and container placement.
- PR #38 separately owns archival of the completed ADR-0008 and ADR-0009 task records; this task does not modify those paths.

## Acceptance criteria

- [ ] The foundation backlog lists ADR-0001 through ADR-0009 as accepted and registers `PERF-01` and `OPS-CHANNEL-01` without changing the immediate `FND-01` next action.
- [ ] The global register lists ADR-0009 as accepted and places `PERF-01` and `OPS-CHANNEL-01` at the correct later operational/performance gates.
- [ ] The scope matrix distinguishes GameNode process identity from host/container placement and references the exact recovery follow-up owners.
- [ ] No fixed player count, tick rate, worker count, orchestrator product, RPO, RTO or reconnect timing is invented.
- [ ] No runtime code, external repository or production system changes.
- [ ] Full diff audit and exact-head governance checks pass.

## Excluded scope

- Do not implement FND-01, FND-03, persistence, orchestration, benchmarks or recovery.
- Do not modify ADR-0009 substance.
- Do not modify task archive paths owned by PR #38.
- Do not select exact capacity values or deployment products.

## Implementation / findings

A bounded self-removing workflow is used only as a GitHub-hosted text-patching mechanism because the local sandbox cannot resolve GitHub and the connector contents API requires complete-file replacement. It has same-branch-only write permission, fixed assertions and no secret, external input or production access. Final validation will run on a later connector-authored exact head after the workflow has removed itself.

## Validation

### Focused

- command/run: pending
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture-index repair only
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no executable product behavior changes
- result: `NOT_APPLICABLE`

### Exact-head CI

- head: pending
- workflow/run: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: adversarial cross-check against ADR-0009, ADR-0001, backlog, global register and scope matrix
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: PR #38 owns task archival only and has no architecture-path overlap
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Scope claimed from main commit 96c605c9fabc3266eca9dd7f0010c97e88fd057c with no overlap with PR #38.
status: implementing
branch: docs/sync-adr-0009-registers
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
next_action: Apply the bounded architecture-index synchronization and remove the temporary patch workflow in the same automated commit.
```
