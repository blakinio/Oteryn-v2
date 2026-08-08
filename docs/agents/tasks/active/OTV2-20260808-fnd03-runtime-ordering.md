# OTV2-20260808-fnd03-runtime-ordering

```yaml
task_id: OTV2-20260808-fnd03-runtime-ordering
title: FND-03 authoritative runtime ordering analysis
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260808-fnd03-runtime-ordering
pr: 98
base_sha: b85bdd3f278d9de12284eab7c6352219325b3751
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: GPT-5.6 Sol architecture continuation session
created_at: 2026-08-08T19:06:00+02:00
updated_at: 2026-08-08T19:17:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260808-fnd03-runtime-ordering.md
  - docs/architecture/FND-03_AUTHORITATIVE_RUNTIME_EXECUTION_ANALYSIS_BASELINE.md
public_contracts:
  - docs/architecture/FND-03_AUTHORITATIVE_RUNTIME_EXECUTION_ANALYSIS_BASELINE.md
depends_on:
  - FND-ID-01 accepted and merged
  - FND-02 accepted and merged
  - ADR-0009 accepted GameNode execution/capacity/recovery baseline
  - merged disconnect/re-entry clarification package from PR #96
blocks:
  - FND-03 Runtime Execution Contract completion
  - authoritative runtime implementation claims
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/Oteryn-Platform (read-only)
  - blakinio/Otheryn (read-only)
  - blakinio/otclient (read-only)
```

## Outcome

Persist the owner-directed FND-03 runtime-execution analysis as a bounded architecture package and resolve only the runtime invariants that genuinely block the later FND-03 contract. The package defines a safe authoritative execution model for ChannelRuntime and InstanceRuntime without implementing the runtime or prematurely choosing benchmark-sensitive libraries, worker counts, tick rates, orchestration products or persistence technology.

This task is analysis input to the later complete FND-03 contract; it does not itself claim that FND-03 is accepted or that runtime implementation is authorized.

## Architecture and source of truth

- **PROVEN:** `main` at task start is `b85bdd3f278d9de12284eab7c6352219325b3751`.
- **PROVEN:** no open pull requests existed in `blakinio/Oteryn-v2` at task start.
- **PROVEN:** FND-ID-01 and FND-02 are accepted and merged; FND-03 is the next ordered foundation gate according to `FOUNDATION_PROGRAMME_CURRENT_STATUS.md`.
- **PROVEN:** ADR-0009 requires a multithreaded GameNode with exactly one logical authoritative mutation owner per ChannelRuntime and generation/revision validation for auxiliary work.
- **PROVEN:** `INSTANCE_SCOPE_AND_RUNTIME_OWNER_BASELINE.md` requires one logical authoritative mutation owner for each concrete InstanceRuntime and explicitly defers the exact ChannelRuntime/InstanceRuntime/WorldServices/GameNode relationship to FND-03.
- **PROVEN:** FND-02 freezes per-GameSession CommandId ordering and bounded ingress but does not define a complete world-simulation time model.
- **PROVEN:** the reconnect/disconnect owner baselines require server-authoritative timing and forbid trusting client-supplied timestamps for reconnect/protection decisions.
- **PROVEN:** `RESOURCE_LIMITS_REGISTRY.json` requires bounded concrete limits before implementation acceptance but does not currently provide evidence-backed FND-03 internal queue/timer/worker capacities.
- **DERIVED:** ChannelRuntime and InstanceRuntime should share one authoritative execution abstraction and differ by owned state scope rather than by scheduler semantics.
- **DERIVED:** CommandId ordering, runtime input order, authoritative mutation/commit order, state revisions, protocol server sequence, monotonic deadlines and wall-clock time must remain distinct concepts unless a later contract proves exact semantic equivalence.
- **DERIVED:** cross-session and async-completion ordering should linearize at the current authoritative owner and retain enough normalized-order evidence for deterministic replay rather than pretending OS thread wake-up order is a gameplay contract.
- **UNKNOWN:** final runtime library, worker topology, simulation quantum, queue capacities, CPU affinity, checkpoint interval and RPO/RTO remain deliberately unresolved until their owning contract or benchmark evidence exists.

Canonical inputs:

- `docs/architecture/ADR-0001-native-rust-multichannel-platform.md`
- `docs/architecture/ADR-0009-game-node-execution-capacity-deployment-and-recovery-baseline.md`
- `docs/architecture/FND-ID-01_FOUNDATION_IDENTIFIER_CONTRACT.md`
- `docs/architecture/FND-02_PROTOCOL_OTERYN_V1_CONTRACT.md`
- `docs/architecture/INSTANCE_SCOPE_AND_RUNTIME_OWNER_BASELINE.md`
- `docs/architecture/FND-ID-01_NODE_ID_PROCESS_INCARNATION_OWNER_BASELINE.md`
- `docs/architecture/FND-ID-01_GAME_SESSION_RECONNECT_GENERATION_OWNER_BASELINE.md`
- `docs/architecture/LAG_DISCONNECT_PROTECTION_OWNER_BASELINE.md`
- `docs/architecture/DISCONNECT_LIVENESS_AND_CRASH_EVIDENCE_OWNER_BASELINE.md`
- `docs/architecture/DISCONNECT_REENTRY_PVE_PROTECTION_OWNER_DECISION.md`
- `docs/architecture/DISCONNECT_CLIENT_OS_FORENSICS_PRIVACY_TIMING_REFINEMENT.md`
- `docs/architecture/MULTICHANNEL_SYSTEM_SCOPE_MATRIX.md`
- `docs/contracts/RESOURCE_LIMITS_REGISTRY.json`
- `docs/contracts/FOUNDATION_ERROR_VOCABULARY.md`
- `docs/contracts/FOUNDATION_FAILURE_SCENARIOS.md`
- `docs/agents/ARCHITECTURE_DECISION_DISCIPLINE.md`

## Acceptance criteria

- [x] Persist the current owner-directed runtime-execution conclusions in one bounded architecture baseline.
- [x] Separate CommandId order, runtime input order, authoritative mutation/commit order, monotonic deadlines and wall-clock timestamps explicitly.
- [x] Define one logical authoritative execution model usable by ChannelRuntime and InstanceRuntime.
- [x] Define auxiliary-work proposal/stale-result rules without allowing worker threads to mutate authoritative state directly.
- [x] Define ownership-generation and NodeId separation for crash/replacement safety.
- [x] Define queue/backpressure classes and fail-open/fail-closed principles without guessing benchmark-sensitive numeric capacities.
- [x] Analyse deterministic ordering for concurrent commands, timers, worker completions and system/runtime events.
- [x] Apply the mandatory architecture decision timing test to material recommendations.
- [x] Keep runtime implementation, library selection and production activation explicitly unauthorized.
- [ ] Complete documentation/governance validation and an independent architecture audit on the final unchanged head before merge.

## Excluded scope

This task must not:

- implement Rust runtime code, protocol listeners/codecs, Game Session admission, leases, persistence or production diagnostics;
- select Tokio or another server async runtime as a binding FND-03 choice;
- freeze worker counts, CPU affinity, exact simulation tick/quantum, queue capacities, checkpoint interval, RPO/RTO or orchestrator product without evidence;
- redefine FND-02 wire semantics or CommandId ordering;
- redefine FND-04 admission/reconnect credential or lease semantics;
- write to external repositories;
- authorize a mandatory Launcher/Guardian process or heartbeat;
- claim runtime, multichannel or E2E implementation evidence from this documentation-only package.

## Implementation / findings

The persisted analysis now establishes the recommended contract direction:

```text
multithreaded GameNode
-> multiple independent scopes may execute concurrently
-> one logical ordered owner per ChannelRuntime/InstanceRuntime
-> logical writer is not a dedicated OS-thread contract
-> CommandId order stays FND-02-owned
-> normalized runtime inputs are linearized at the authoritative owner
-> monotonic deadlines are distinct from wall clock and protocol sequencing
-> mutation-capable timers re-enter through the owner
-> worker/service completions are proposals/results, not mutation callbacks
-> stale generation/revision/local-handle work fails closed
-> control/fence work cannot be starved by ordinary gameplay backlog
-> all queue classes are bounded with explicit overload behavior
-> benchmark-sensitive numeric capacities wait for measured implementation evidence
-> replacement process gets a fresh NodeId while semantic channel/instance identity may survive under a newer ownership generation
-> deterministic replay records normalized authoritative input/commit evidence rather than original CPU/thread interleaving
```

The analysis also preserves a modular-monolith initial placement: one GameNode may host multiple channels/instances and in-process WorldServices integration, while semantic ownership remains explicit and independently extractable later.

A parallel final-contract PR #99 was created after this earlier task was already authoritative. It was closed unmerged as `SUPERSEDED / PREMATURE` so the final FND-03 contract cannot outrun its own analysis gate. No #99 content is canonical.

## Validation

### Focused

- changed-path review: pending final exact-head audit
- accepted-input consistency review: in progress; no material contradiction identified so far

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture-only package; no runtime component changes are authorized.
- result: `NOT_APPLICABLE`.

### E2E

- scenario: `NOT_APPLICABLE` — this task changes architecture documentation only and cannot prove executable runtime behavior.
- result: `NOT_APPLICABLE`.

### Exact-head CI

- final head: pending
- trigger source: pull_request
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: pending
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending final head
- unresolved review threads: pending
- related/superseded PRs: PR #99 closed unmerged as a later duplicate/premature final-contract package
- protected auto-merge: not requested
- merge policy: squash after exact-head validation and zero open material findings
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: PR #98 now contains the bounded FND-03 authoritative runtime execution analysis baseline; ordering/time domains, shared ChannelRuntime/InstanceRuntime execution semantics, control lane, timers, stale auxiliary work, generational handles, bounded overload policy, liveness integration and recovery direction are persisted without freezing benchmark-sensitive implementation choices; later duplicate PR #99 was closed unmerged.
status: validating
branch: docs/OTV2-20260808-fnd03-runtime-ordering
head_sha: null
pr: 98
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: pull_request
ci_check_generation: pending-final-head
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
next_action: Freeze the PR #98 head, perform independent full-diff architecture audit against accepted FND-03 inputs, and require exact-head repository checks before squash merge.
```
