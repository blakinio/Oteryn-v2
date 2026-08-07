# OTV2-20260808-fnd02-protocol-contract

```yaml
task_id: OTV2-20260808-fnd02-protocol-contract
title: Freeze the protocol-oteryn v1 foundation contract
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260808-fnd02-protocol-contract
pr: 94
base_sha: b9c5764711c4206832209f6ca89b9dc56492c3c1
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-08T00:25:00+02:00
updated_at: 2026-08-08T00:48:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260808-fnd02-protocol-contract.md
  - docs/architecture/FND-02_PROTOCOL_OTERYN_V1_CONTRACT.md
  - docs/contracts/protocol-oteryn/v1/foundation.proto
  - docs/contracts/PROTOCOL_OTERYN_V1_REGISTRY.json
  - docs/contracts/RESOURCE_LIMITS_REGISTRY.json
  - docs/contracts/CROSS_REPOSITORY_CONTRACT_LOCK.json
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
  - docs/agents/tasks/active/OTV2-20260805-foundation-preimplementation-contracts.md
public_contracts:
  - docs/architecture/FND-02_PROTOCOL_OTERYN_V1_CONTRACT.md
  - docs/contracts/protocol-oteryn/v1/foundation.proto
  - docs/contracts/PROTOCOL_OTERYN_V1_REGISTRY.json
  - docs/contracts/RESOURCE_LIMITS_REGISTRY.json
depends_on:
  - docs/architecture/FND-ID-01_FOUNDATION_IDENTIFIER_CONTRACT.md
  - docs/architecture/FND-02_PLATFORM_PROTOCOL_RECONCILIATION_OWNER_BASELINE.md
  - docs/architecture/ARCHITECTURE_REVIEW_REFINEMENTS_2026-08-07.md
  - docs/contracts/FOUNDATION_ERROR_VOCABULARY.md
  - docs/contracts/FOUNDATION_FAILURE_SCENARIOS.md
  - docs/architecture/FND-ID-01_GAME_SESSION_RECONNECT_GENERATION_OWNER_BASELINE.md
  - docs/architecture/DISCONNECT_LIVENESS_AND_CRASH_EVIDENCE_OWNER_BASELINE.md
  - docs/architecture/LAG_DISCONNECT_PROTECTION_OWNER_BASELINE.md
blocks:
  - FND-03
  - canonical protocol-oteryn implementation
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/Oteryn-Platform
```

## Outcome

Freeze one implementable, secure and evolvable `protocol-oteryn` v1 foundation contract for the native Rust client/server stack without implementing runtime code.

## Architecture and source of truth

- `PROVEN`: task base is `b9c5764711c4206832209f6ca89b9dc56492c3c1`; no open Oteryn-v2 PR existed when the task started.
- `PROVEN`: current-status authority identified FND-02 as the next ordered gate.
- `PROVEN`: `blakinio/Oteryn-Platform@c0b8703d326a04b43ae8e06f6192b0cb91c859b7` is reconciliation input only.
- `PROVEN`: FND-ID keeps canonical `GameSessionId` game-issued after admission and leaves `CommandId`/wire ordering to FND-02.
- `PROVEN`: accepted reconnect semantics preserve an eligible `GameSessionId` while advancing transport generation.
- `PROVEN`: accepted liveness semantics use server-observed control progress, not gameplay-command silence or socket-open state.
- `PROVEN`: the resource-limit registry had no concrete entries before this task.
- `PROVEN`: current TLS 1.3 is RFC 9846; service identity verification is covered by RFC 9525.
- `PROVEN`: protobuf supports compatible additive evolution but serialized protobuf bytes are not canonical semantic identity.
- `OWNER_AUTHORIZED`: the owner instructed continued architecture execution on 2026-08-08.

## Frozen candidate contract

The PR currently freezes:

- family `oteryn`, protocol major `1`;
- transport profile `TCP + TLS 1.3`, ALPN `oteryn-game/1`, verified server identity, no TLS 0-RTT/plaintext/Canary fallback;
- BE32 length framing with one bounded protobuf envelope;
- protobuf binary, `proto3` source IDL, no concrete Rust protobuf library yet;
- schema revision/hash as evidence rather than lockstep runtime compatibility identity;
- no speculative optional capabilities in initial v1; future additive numeric capabilities only;
- exposed foundation UUID IDs as 16-byte UUID network-order values;
- monotonic `uint64 connection_generation` fencing both directions;
- `(GameSessionId, uint64 CommandId)` as the one client command identity/order, with no UUIDv4+second-sequence pair;
- monotonic per-GameSession server sequence;
- typed domain revisions, bounded replay/resync and atomic chunked snapshot replacement;
- liveness probe/ack primitives separated from gameplay-command activity;
- stable protocol error registry;
- concrete externally controlled protocol limits;
- independent byte/golden, malformed, property, fuzz and cross-version evidence requirements.

## Acceptance criteria

- [x] One native production family remains `oteryn`; Canary fallback/translation is absent.
- [x] Transport/TLS/framing are explicit and downgrade-resistant.
- [x] IDL/serialization and evolution rules are explicit without pinning a Rust implementation library.
- [x] Foundation IDL avoids freezing downstream gameplay payload schemas.
- [x] Core protocol semantics are separate from optional capabilities/content/rulesets.
- [x] Command identity/order prevents duplicate re-execution without an unbounded UUID cache.
- [x] Server sequence and transport generation survive eligible reconnect correctly.
- [x] Snapshot/delta/resync never guesses through revision/sequence gaps.
- [x] Partial snapshots cannot cross connection generations.
- [x] Liveness does not depend on gameplay-command traffic.
- [x] Exact externally controlled hard limits are registered.
- [x] Error codes map to the shared foundation vocabulary.
- [x] Applicable foundation failure scenarios have explicit FND-02 assertions.
- [x] Independent codec/framing evidence is mandatory for later implementation acceptance.
- [x] Historical Platform contract remains reconciliation-only evidence.
- [x] No Rust runtime, listener, codec crate, database schema, Platform write or production activation is introduced.
- [ ] Complete final-head changed-file review passes.
- [ ] Independent exact-head architecture/security audit reports zero open material findings.
- [ ] Exact-head required GitHub checks pass.
- [ ] Delivery PR is squash-merged.
- [ ] Follow-up closeout records immutable merged FND-02 evidence, reconciles programme status/lock and releases ownership.

## Excluded scope

- Runtime implementation of protocol/listener/client adapter/codecs.
- Concrete Rust protobuf/TLS dependency selection.
- FND-03 scheduler/runtime queues/recovery implementation.
- FND-04 credential/admission/lease/reconnect state machine and heartbeat cadence.
- Gameplay-specific movement/combat/inventory/chat/quest/content payloads.
- Platform contract mutation or rollout.
- QUIC, application compression, live channel migration or Canary compatibility in v1.

## Audit findings and repairs

The first adversarial pass found five contract-hygiene issues and all were repaired before final validation:

1. `ProtocolError` was unnecessarily bidirectional -> registry now makes it server-to-client.
2. bootstrap message phases were named too narrowly -> registry uses `BOOTSTRAP`.
3. server sequence class naming was inconsistent -> standardized on `SERVER_SEQUENCED`.
4. stale-generation fencing was explicit mainly for client->server -> contract now requires current generation in both directions and client rejection of stale server frames.
5. capability/snapshot/liveness edge cases were underspecified -> unknown supported capabilities may be ignored during intersection while unknown selected/required capabilities fail; partial snapshots are discarded on generation change; liveness probe IDs never wrap/reuse.

The contract also states that mTLS/client certificates are not a v1 requirement; FND-04 application admission proof remains separate.

## Validation

### Focused

- JSON/protobuf/hash/static contract consistency: final exact-head review pending.
- foundation schema SHA-256 recorded in registry: `6e1c614661e72daac529be9d0ec06317201b916cd47ae17ff1590da5c7205ebe`.

### Component/integration

`NOT_APPLICABLE` — this delivery changes architecture/contract/schema-definition files only.

### E2E

`NOT_APPLICABLE` — the contract defines mandatory later wire/E2E evidence but does not implement gameplay transport.

### Exact-head CI

- trigger source: pull_request
- PR: `#94`
- final head: pending last task-checkpoint commit
- Agent governance: pending current generation
- Dependency review: pending current generation
- CodeQL: pending current generation

## Independent audit

- exact head: pending final checkpoint head
- method: adversarial protocol/security/compatibility review against accepted ADRs, FND-ID, reconnect/liveness baselines, Platform reconciliation input, TLS/protobuf primary evidence and complete diff
- first-pass findings: five, all repaired before final-head review
- open material findings: pending final re-audit

## PR and closeout

- PR: `#94` draft
- changed-file review: pending final head
- unresolved review threads: pending
- merge: pending
- cross-repository lock exact merged evidence: intentionally deferred until immutable squash merge exists
- programme transition to FND-03: intentionally finalized in closeout after accepted merge
- ownership release: pending

## Context checkpoint

```yaml
last_progress: FND-02 candidate contract and machine-readable IDL/registries are complete; first adversarial findings were repaired and PR #94 is validating.
status: validating
branch: docs/OTV2-20260808-fnd02-protocol-contract
head_sha: null
pr: 94
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: pull_request
ci_check_generation: pending-final-task-checkpoint
ci_checks_for_current_head: 0
ci_run_ids: []
ci_job_ids: []
runner_assignment_state: unknown
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 1
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: null
blocker: null
next_action: Re-audit the exact PR head, verify required CI, then merge FND-02 and perform immutable closeout/status/lock reconciliation.
```
