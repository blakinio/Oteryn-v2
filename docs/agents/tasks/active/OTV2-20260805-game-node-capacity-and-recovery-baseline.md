# OTV2-20260805-game-node-capacity-and-recovery-baseline

```yaml
task_id: OTV2-20260805-game-node-capacity-and-recovery-baseline
title: Record GameNode execution, capacity, deployment and recovery baseline
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/adr-0008-protocol-canary-reference-only
pr: 37
base_sha: 52ef04882e13771829e0159b63410a7cd9e80150
head_sha: ac4affe5b3eab63a175ed3ac700e9d937e2f4f10
owner: GPT-5.6-Thinking-architecture-coordinator
created_at: 2026-08-05T19:45:00+02:00
updated_at: 2026-08-05T19:45:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/architecture/ADR-0009-game-node-execution-capacity-deployment-and-recovery-baseline.md
  - docs/agents/tasks/active/OTV2-20260805-game-node-capacity-and-recovery-baseline.md
public_contracts:
  - docs/architecture/ADR-0009-game-node-execution-capacity-deployment-and-recovery-baseline.md
depends_on:
  - ADR-0001
  - ADR-0003
  - ADR-0004
  - ADR-0007
  - FND-03
  - FND-04
  - DUR-02
  - DUR-03
blocks:
  - publication of production player-capacity claims until PERF-01 is accepted with measured evidence
  - automatic production channel scaling until OPS-CHANNEL-01 is accepted
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/Oteryn-Platform
```

## Outcome

Persist the owner-approved architecture direction for GameNode terminology, multithreaded single-writer execution, channel/GameNode/world capacity measurement, process/container deployment, dynamic channel creation and safe player recovery after GameNode failure.

The package deliberately records invariants and required evidence while leaving exact player limits, tick frequency, worker counts, orchestration product and recovery timings unresolved until representative implementation and benchmarks exist.

## Architecture and source of truth

### PROVEN

- ADR-0001 already requires one logical authoritative mutation owner per channel and allows several channels on one node.
- ADR-0001 distinguishes channel identity from physical placement and requires generation fencing for stale sessions/writers.
- ADR-0004 selects PostgreSQL and explicit game-data ownership.
- ADR-0007 requires deterministic multichannel failure, recovery and cleanup evidence.
- Repository governance prohibits claiming performance or recovery success without named exact evidence.
- The owner requested on 2026-08-05 that the architecture retain the discussed multithreading, capacity, deployment, dynamic-channel and container-failure decisions.

### ACCEPTED DIRECTION

- `GameNode` means one logical running instance of the game-server process with its own `GameNodeId`; it is not a physical host or Kubernetes Node.
- Production defaults to one GameNode process per container, while the same binary remains runnable as a native process.
- One GameNode may host several ChannelRuntimes; a dedicated one-channel GameNode remains a supported placement option.
- The server is multithreaded, but one logical writer commits authoritative mutations for each channel.
- I/O, authoritative simulation and bounded CPU-bound auxiliary work remain separated.
- Capacity is measured independently per channel, per GameNode and per logical world.
- Player limits are derived later from representative benchmarks, with an initial target of at least 30% production headroom below measured saturation.
- Existing GameNodes may create channels dynamically only when accepted capacity remains; new processes/containers are started by an external orchestrator.
- The game process never calls Docker/Kubernetes APIs to create itself or replacement nodes.
- Initial recovery uses fencing, replacement/restart, checkpoint plus bounded replay, fresh Game Sessions and full snapshots.
- Players are not silently transferred to another channel or teleported solely because a GameNode failed.
- Live migration and hot standby remain deferred.

## Acceptance criteria

- [x] Canonical terminology distinguishes host, container, GameNode process, GameNode and ChannelRuntime.
- [x] Production process/container topology and the external orchestrator boundary are recorded.
- [x] Multithreaded execution preserves one logical authoritative writer per channel.
- [x] Parallel result return requires generation/revision/task identity and stale-result rejection.
- [x] Capacity is defined separately for channel, GameNode and world.
- [x] Representative benchmark and saturation evidence requirements are recorded without inventing player numbers.
- [x] Dynamic channel lifecycle and placement escalation are recorded.
- [x] GameNode failure behavior, fencing, recovery and player reconnect are recorded.
- [x] Critical durable operations remain atomic/idempotent and protected against duplication during crash recovery.
- [x] Follow-up gates `PERF-01` and `OPS-CHANNEL-01` are registered with explicit ownership.
- [x] No runtime code, deployment configuration, external repository or production system is changed.
- [ ] Full changed-file and full-diff architecture audit passes.
- [ ] Exact-head required workflows pass.

## Excluded scope

- Do not implement the GameNode process or ChannelRuntime.
- Do not select exact player limits, tick frequency, worker counts or CPU affinity.
- Do not select or configure Docker, Kubernetes, systemd or another production orchestrator.
- Do not select exact checkpoint interval, RPO, RTO or reconnect grace period.
- Do not implement live migration, warm standby or multi-node partitioning of one channel.
- Do not modify Platform, Gateway, PostgreSQL, Otheryn, otclient or production systems.

## Implementation / findings

- Added ADR-0009 as the durable architecture baseline.
- Registered `PERF-01` for capacity/performance/scalability and `OPS-CHANNEL-01` for GameNode deployment, dynamic channel orchestration and recovery.
- Preserved existing ownership boundaries: `FND-03` owns execution, `FND-04` owns sessions/leases, `DUR-02` owns durable recovery, `DUR-03` owns item/currency conservation and `QA-E2E-01` owns physical failure evidence.
- Reused PR #37 because the owner extended the current architecture package while it remained open; this task owns only new non-overlapping paths.

## Validation

### Focused

- command/run: pending complete read-through and changed-file review of ADR-0009 and this task record
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture-only package
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no executable product change
- result: `NOT_APPLICABLE`; ADR-0009 defines mandatory future container/process termination scenarios

### Exact-head CI

- head: pending final documentation head
- workflow/run: pending
- result: pending

## Independent audit

- exact head: pending final documentation head
- method/auditor: adversarial architecture review against ADR-0001, ADR-0003, ADR-0004, ADR-0007, FND-03/FND-04/DUR-02/DUR-03 ownership and repository governance
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: PR #37 also contains ADR-0008; no path ownership overlap
- merge commit/result: pending
- ownership release: pending merge and archive

## Context checkpoint

```yaml
last_progress: ADR-0009 records the GameNode execution, capacity, deployment, dynamic-channel and failure-recovery baseline.
status: validating
branch: docs/adr-0008-protocol-canary-reference-only
head_sha: ac4affe5b3eab63a175ed3ac700e9d937e2f4f10
pr: 37
ci_check_generation: null
ci_checks_for_current_head: 0
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 0
stall_warnings: 0
blocker: null
next_action: Audit the complete PR diff and update PR metadata for the expanded architecture scope.
```
