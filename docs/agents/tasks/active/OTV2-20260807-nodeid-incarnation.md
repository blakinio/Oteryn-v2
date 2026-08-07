# OTV2-20260807-nodeid-incarnation

```yaml
task_id: OTV2-20260807-nodeid-incarnation
title: Record NodeId process-incarnation semantics
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260807-nodeid-incarnation
pr: null
base_sha: 6804f5d67b63f1374a9efa3710bcaad10805c801
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-07T10:56:00+02:00
updated_at: 2026-08-07T10:56:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260807-nodeid-incarnation.md
  - docs/architecture/FND-ID-01_NODE_ID_PROCESS_INCARNATION_OWNER_BASELINE.md
public_contracts:
  - docs/architecture/FND-ID-01_NODE_ID_PROCESS_INCARNATION_OWNER_BASELINE.md
depends_on:
  - ADR-0001 native Rust multichannel architecture
  - ADR-0009 GameNode execution/capacity/recovery baseline
  - UUIDV7_DURABLE_IDENTITY_OWNER_BASELINE.md
blocks:
  - complete FND-ID-01 identifier catalogue until NodeId lifecycle is consumed
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Record the owner-accepted decision that canonical `NodeId` identifies one concrete GameNode process incarnation, uses strongly typed UUIDv7, and changes on every process restart. Stable host, VM, container-orchestrator node, deployment target or logical placement-slot identity is separate and must never be overloaded into `NodeId`.

## Architecture and source of truth

- `PROVEN`: ADR-0001 already defines `NodeId` as the logical identity of one GameNode process runtime and explicitly separates it from physical host/container/orchestrator identity.
- `PROVEN`: ADR-0009 separates host, container, process, GameNode and ChannelRuntime and allows a channel to move between GameNodes without changing channel identity.
- `PROVEN`: the durable UUIDv7 baseline lists `GameNodeId` as a candidate durable cross-boundary identity but leaves exact catalogue ownership/lifecycle to `FND-ID-01`.
- `OWNER_ACCEPTED`: on 2026-08-07 the repository owner accepted that canonical `NodeId` is a UUIDv7 process-incarnation identity and every GameNode process restart receives a new `NodeId`; stable infrastructure/placement identity, when needed, is separate.

The canonical project term remains `NodeId` to match ADR-0001. `GameNodeId` may appear in historical/candidate wording but must not become a second semantic identifier for the same process-incarnation concept without an explicit rename/migration decision.

## Acceptance criteria

- [x] Define `NodeId` as one GameNode process incarnation.
- [x] Use strongly typed UUIDv7 as canonical representation.
- [x] Require a new `NodeId` for every process restart/new incarnation.
- [x] Keep `NodeId` separate from host, VM, pod/container, orchestrator-node and stable deployment-slot identity.
- [x] Keep `NodeId` out of semantic `WorldId + ChannelId` channel identity.
- [x] State that possession of `NodeId` grants no gameplay or mutation authority by itself.
- [x] Preserve recovery/fencing semantics: a replacement process is a new node incarnation while the channel may retain the same `WorldId + ChannelId` with newer ownership generation/fence.
- [x] Avoid prematurely freezing the exact NodeId generator/registration handshake or the final name/owner of stable placement identity.
- [x] Do not implement runtime, orchestrator, protocol, persistence or production behavior.
- [ ] Review the final diff and exact-head checks before merge readiness.

## Excluded scope

- no Rust runtime implementation;
- no orchestrator integration;
- no heartbeat/lease/registration API;
- no exact `NodeId` wire encoding beyond full UUIDv7 preservation requirements already owned by later contracts;
- no stable host/placement identifier final naming or ownership decision;
- no `ChannelId`/`WorldId` lifecycle changes;
- no production deployment or activation;
- no completion of the full `FND-ID-01` catalogue.

## Implementation / findings

The decision intentionally distinguishes process incarnation from durable topology identity. A replacement GameNode is a different `NodeId`; a recovered channel is not therefore a different `ChannelId`. This gives diagnostics, stale-registration rejection, recovery and fencing a precise process identity without coupling application identity to mutable infrastructure.

Exact UUID generation location and registration/attestation protocol are deliberately left open. `NodeId` must be newly established for every process incarnation, but `FND-ID-01`/`FND-03`/operations contracts will assign exact generator, registration authority and failure semantics.

## Validation

### Focused

- command/run: pending exact-head documentation/governance workflow
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture documentation only
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no executable runtime behavior changes
- result: `NOT_APPLICABLE`

### Exact-head CI

- final head: recorded in immutable PR/check evidence after final content commit
- trigger source: pull_request
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Independent audit

- exact head: pending immutable PR/check evidence
- method/auditor: pending
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: PR #63 and PR #64 are separate architecture decisions and own no paths in this task
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Owner accepted NodeId as a UUIDv7 GameNode process-incarnation identity that changes on every process restart.
status: implementing
branch: docs/OTV2-20260807-nodeid-incarnation
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
next_action: Add the owner-accepted NodeId process-incarnation architecture baseline and open a bounded documentation PR.
```
