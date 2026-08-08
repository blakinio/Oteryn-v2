# OTV2-20260808-fnd03-runtime-execution-final

```yaml
task_id: OTV2-20260808-fnd03-runtime-execution-final
title: Finalize FND-03 authoritative runtime execution contract
mode: CONTRACT
status: investigating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260808-fnd03-runtime-execution-final
pr: null
base_sha: a931c54e7e32b2cea370317ce88896a18eed8ccb
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: GPT-5.6 Sol architecture continuation session
created_at: 2026-08-08T19:28:00+02:00
updated_at: 2026-08-08T19:28:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/architecture/FND-03_RUNTIME_EXECUTION_CONTRACT.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
  - docs/agents/tasks/active/OTV2-20260808-fnd03-runtime-execution-final.md
public_contracts:
  - docs/architecture/FND-03_RUNTIME_EXECUTION_CONTRACT.md
depends_on:
  - docs/architecture/FND-03_AUTHORITATIVE_RUNTIME_EXECUTION_ANALYSIS_BASELINE.md
  - docs/architecture/FND-03_RUNTIME_LIFECYCLE_FAILURE_AND_REPLAY_ANALYSIS_BASELINE.md
  - docs/architecture/ADR-0001-native-rust-multichannel-platform.md
  - docs/architecture/ADR-0009-game-node-execution-capacity-deployment-and-recovery-baseline.md
  - docs/architecture/FND-ID-01_FOUNDATION_IDENTIFIER_CONTRACT.md
  - docs/architecture/FND-02_PROTOCOL_OTERYN_V1_CONTRACT.md
  - docs/architecture/INSTANCE_SCOPE_AND_RUNTIME_OWNER_BASELINE.md
  - docs/architecture/DISCONNECT_LIVENESS_AND_CRASH_EVIDENCE_OWNER_BASELINE.md
  - docs/architecture/DISCONNECT_REENTRY_PVE_PROTECTION_OWNER_DECISION.md
  - docs/architecture/DISCONNECT_CLIENT_OS_FORENSICS_PRIVACY_TIMING_REFINEMENT.md
  - docs/contracts/RESOURCE_LIMITS_REGISTRY.json
  - docs/contracts/FOUNDATION_ERROR_VOCABULARY.md
  - docs/contracts/FOUNDATION_FAILURE_SCENARIOS.md
blocks:
  - authoritative Rust GameNode runtime implementation claims
  - runtime-dependent vertical-slice implementation packages
  - FND-04 final integration where session/reconnect semantics depend on runtime liveness and fencing interfaces
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Produce the complete architecture-only `FND-03 Runtime Execution Contract` from the two accepted analysis baselines now canonical on `main`.

The contract must freeze only the runtime semantics required before implementation: ownership and lifecycle boundaries, authoritative input linearization, ordering/evidence semantics, clocks and timers, auxiliary-work revalidation, queue/backpressure classes, recovery/fencing/checkpoint cuts, deterministic randomness/replay, failure/error disposition, FND-04 liveness interface and downstream gate ownership.

It must not choose benchmark-sensitive runtime technology or numeric capacity values without evidence, and it must not authorize Rust runtime implementation merely by accepting the architecture contract.

## Architecture and source of truth

- **PROVEN:** `main@a931c54e7e32b2cea370317ce88896a18eed8ccb` contains the merged FND-03 analysis baselines and their completed lifecycle closeout.
- **PROVEN:** no open pull requests existed when this final package began.
- **PROVEN:** later duplicate lifecycle PR #101 was closed unmerged as superseded by canonical closeout #100.
- **PROVEN:** closed PR #99 is a non-authoritative premature draft and must not be treated as accepted FND-03 contract text.
- **PROVEN:** FND-02 owns per-GameSession `(GameSessionId, CommandId)`, connection generation, server sequence and snapshot/delta/resync semantics; FND-03 consumes rather than redefines them.
- **PROVEN:** one logical mutation owner per ChannelRuntime/InstanceRuntime is already accepted; process/thread placement is not semantic authority.
- **DERIVED from merged analysis:** one owner-scoped runtime execution ordinal is sufficient as the mandatory linearization/evidence value if each normalized authoritative input is resolved without interleaving; resulting domain mutations advance their own state revisions. A second public/runtime-wide commit counter is not automatically required.
- **DERIVED from merged analysis:** scope ownership generation must be distinct from NodeId and cannot be self-granted by a newly started GameNode.
- **UNKNOWN / intentionally deferred:** concrete async runtime, worker topology/counts, CPU affinity, global tick/quantum, benchmark-sensitive queue/timer/worker limits, checkpoint storage/RPO/RTO and orchestrator product.

## Acceptance criteria

### Final ownership and ordering semantics

- [ ] Freeze final responsibilities for NodeRuntime, WorldServices, ChannelRuntime and InstanceRuntime.
- [ ] Freeze canonical identity versus scope-ownership generation versus NodeId placement separation.
- [ ] Define who may establish a newer ownership generation semantically, without selecting an orchestrator product.
- [ ] Freeze one authoritative owner execution linearization value and explicitly decide the disposition of analysis-only `RuntimeInputOrdinal` / `RuntimeCommitOrdinal` terminology.
- [ ] Define ordering and non-interleaving semantics for commands, timers, control/fencing events, service completions and auxiliary results.
- [ ] Define exhaustion/non-reuse behavior for runtime ordering/fencing values without requiring a public wire encoding where none is needed.

### Time, timers and liveness

- [ ] Freeze wall-clock versus process-local monotonic time versus authoritative execution order semantics.
- [ ] Prohibit persistence/comparison of opaque process-local monotonic instants across NodeId replacement.
- [ ] Define durable/recoverable timer boundary as domain semantic state owned by gameplay/DUR contracts.
- [ ] Freeze timer scheduling, equal-deadline ordering, cancellation/stale-generation behavior and bounded catch-up policy requirement.
- [ ] Freeze the FND-03/FND-04 liveness interface: what FND-04 decides and what FND-03 measures/executes for 2 s, 5 s, 15 s and 4 s policies.

### Queues, dependencies and recovery

- [ ] Freeze required bounded queue/work classes and post-reservation no-silent-drop rule.
- [ ] Require concrete numeric runtime limits in `RESOURCE_LIMITS_REGISTRY.json` before implementation acceptance, backed by safety/benchmark/spike evidence rather than guessed in this contract.
- [ ] Freeze slow-client bounded resync/close direction and control-lane non-starvation.
- [ ] Freeze asynchronous dependency pending/revalidation behavior.
- [ ] Freeze lifecycle activation/drain/checkpoint/fence/recovery cuts while leaving persistence encoding/RPO/RTO to later owners.
- [ ] Preserve same semantic ChannelId/InstanceId across eligible recovery while NodeId and ownership generation change.

### Determinism, failure and downstream boundaries

- [ ] Freeze deterministic authoritative gameplay RNG requirements and separation from security randomness.
- [ ] Freeze deterministic simulation replay evidence boundary and prohibit analytics replay from replaying gameplay mutation.
- [ ] Produce complete FND-03 disposition for the foundation failure catalogue without falsely claiming executable proof.
- [ ] Map runtime-facing failures to the foundation error vocabulary without exposing implementation strings as public contract.
- [ ] Freeze the exact downstream ownership split with FND-04, DUR-*, ANL-*, PERF-01, OPS-CHANNEL-01 and gameplay contracts.
- [ ] Synchronize `FOUNDATION_PROGRAMME_CURRENT_STATUS.md` with transition-safe wording that remains correct before and after merge.

### Governance

- [ ] No runtime code/workspace/production implementation is introduced.
- [ ] Full changed-path architecture review finds zero unresolved material conflicts.
- [ ] Exact-head Agent governance and applicable repository checks pass.
- [ ] Independent exact-head architecture/security audit passes with zero open material findings.
- [ ] Squash merge only after all final-head gates pass; archive/release ownership in a separate closeout PR.

## Excluded scope

This task must not:

- implement GameNode/ChannelRuntime/InstanceRuntime Rust code;
- create speculative runtime crates or select Tokio/another runtime as binding architecture;
- select worker/thread counts, CPU affinity, fixed global tick frequency or scheduler quantum;
- guess numeric queue/timer/worker capacities;
- define PostgreSQL schema, transaction isolation, checkpoint encoding, journal technology, RPO/RTO or backup policy;
- define FND-04 credentials/tokens/lease storage or duplicate-login state machine;
- define ANL-01 event schema/outbox implementation;
- select Kubernetes/Docker/systemd or another orchestrator product;
- define gameplay-specific combat/movement/AI tie-break formulas beyond the generic owner execution framework;
- authorize client diagnostics, Launcher/Guardian implementation, production traffic/deployment or external-repository writes.

## Implementation / findings

The final contract will resolve the remaining analysis ambiguity conservatively:

- keep **one mandatory owner-scoped `RuntimeExecutionOrdinal` semantic** for normalized authoritative input linearization/evidence;
- do not freeze two separate physical `RuntimeInputOrdinal` / `RuntimeCommitOrdinal` counters as architectural requirements;
- require one normalized input resolution to be non-interleaved at the logical owner boundary; zero or more resulting domain mutations use their existing domain/state revisions and deterministic internal sub-order;
- when an operation becomes asynchronous/pending, its later completion is a new normalized owner input correlated to the original CommandId/operation/task identity;
- ordinal/fencing values never wrap/reuse inside their scope; exhaustion fails closed and requires safe scope/session lifecycle transition rather than reuse.

This choice reduces redundant counters while preserving the analysis requirement that CommandId, runtime execution order, server_sequence and state revisions remain semantically distinct.

## Validation

### Focused

- accepted-analysis reconciliation: in progress
- final contract consistency review: pending

### Component/integration

- result: `NOT_APPLICABLE` — architecture-only contract delivery.

### E2E

- result: `NOT_APPLICABLE` — no executable capability introduced.

### Exact-head CI

- final head: pending
- trigger source: pending
- workflow/run/job: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: pending
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: #99 and #101 closed unmerged as superseded; neither is authority
- merge policy: squash after exact-head validation
- merge commit/result: pending
- ownership release: pending separate closeout

## Context checkpoint

```yaml
last_progress: Final FND-03 package started from clean main after analysis PR #98 and closeout #100; duplicate #101 is closed, and this task owns only the final runtime contract, current-status synchronization and its task record.
status: investigating
branch: docs/OTV2-20260808-fnd03-runtime-execution-final
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
next_action: Draft FND-03_RUNTIME_EXECUTION_CONTRACT.md from the two merged analysis baselines and accepted foundation contracts, then audit before any status synchronization or merge claim.
```
