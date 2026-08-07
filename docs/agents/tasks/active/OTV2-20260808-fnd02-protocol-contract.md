# OTV2-20260808-fnd02-protocol-contract

```yaml
task_id: OTV2-20260808-fnd02-protocol-contract
title: Freeze the protocol-oteryn v1 foundation contract
mode: CONTRACT
status: investigating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260808-fnd02-protocol-contract
pr: null
base_sha: b9c5764711c4206832209f6ca89b9dc56492c3c1
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-08T00:25:00+02:00
updated_at: 2026-08-08T00:25:00+02:00
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

Freeze one implementable, secure and evolvable `protocol-oteryn` v1 foundation contract for the native Rust client/server stack without implementing runtime code. The package must independently decide transport, TLS integration, framing, serialization, versioning, capability extension, wire identifier representation, command identity/order/idempotency, authoritative server sequencing, snapshot/delta/resync semantics, reconnect continuity fields, error behavior, hard wire limits and independent compatibility evidence.

## Architecture and source of truth

- `PROVEN`: current trusted base is `b9c5764711c4206832209f6ca89b9dc56492c3c1` after Character Authority closeout PR #91.
- `PROVEN`: no open Oteryn-v2 PR exists at task start.
- `PROVEN`: `FOUNDATION_PROGRAMME_CURRENT_STATUS.md` marks FND-02 as the next ordered foundation gate.
- `PROVEN`: the Platform contract at `blakinio/Oteryn-Platform@c0b8703d326a04b43ae8e06f6192b0cb91c859b7` is `RECONCILIATION_INPUT_ONLY`, not final FND-02 authority.
- `PROVEN`: `RESOURCE_LIMITS_REGISTRY.json` contains no concrete entries before this task.
- `PROVEN`: canonical Rust workspace has 19 members and no production server or protocol-oteryn crate yet; this task is architecture-only.
- `PROVEN`: current TLS 1.3 specification is RFC 9846; application protocols must define TLS integration and server identity verification.
- `PROVEN`: Protocol Buffers binary supports compatible schema evolution, while serialized protobuf bytes are not a canonical semantic representation.
- `OWNER_AUTHORIZED`: the project owner instructed continued architecture execution on 2026-08-08.

## Acceptance criteria

- [ ] One production protocol family `oteryn` remains the only native gameplay protocol.
- [ ] Transport/TLS/framing are frozen with no Canary fallback, sniffing or plaintext downgrade.
- [ ] IDL/serialization is independently selected and its evolution rules are explicit.
- [ ] The foundation `.proto` schema is implementable without freezing downstream movement/combat/content message payloads.
- [ ] Core protocol semantics are versioned separately from optional capabilities, content and rulesets.
- [ ] `CommandId` semantics, ordering, retries and bounded result-replay behavior prevent re-execution after duplicate delivery.
- [ ] Server authoritative sequencing survives eligible reconnect without allowing stale transport generations to regain command authority.
- [ ] Snapshot/delta/resync rules are deterministic and never guess through revision gaps.
- [ ] Liveness wire primitives support server-authoritative control-progress evidence without using gameplay-command absence as disconnect evidence.
- [ ] Exact externally controlled protocol limits are added to `RESOURCE_LIMITS_REGISTRY.json`.
- [ ] FND-02 error codes map to `FOUNDATION_ERROR_VOCABULARY.md`.
- [ ] Applicable `FOUNDATION_FAILURE_SCENARIOS.md` entries are classified by the contract.
- [ ] Canonical byte fixtures, malformed corpus, property tests, fuzzing and cross-version fixtures are required as implementation evidence; shared production codecs are not the sole oracle.
- [ ] The immutable old Platform contract remains historical reconciliation evidence and is not falsely marked as final Oteryn-v2 conformance.
- [ ] FND-03 becomes the next ordered gate only after FND-02 delivery is accepted and merged.
- [ ] No Rust runtime, listener, codec crate, database schema, Platform write or production activation is introduced.
- [ ] Complete changed-file review passes.
- [ ] Independent architecture/security audit reports zero open material findings.
- [ ] Exact-head required GitHub checks pass.

## Excluded scope

- Runtime implementation of `protocol-oteryn`, server listener, client adapter or codecs.
- Selection of a concrete Rust protobuf runtime/library; the wire contract may constrain compatibility but dependency choice remains an implementation decision with its own maintenance/security evidence.
- FND-03 scheduler/runtime execution details.
- FND-04 credential construction, admission/lease state machine, reconnect eligibility or final heartbeat policy timing.
- Gameplay-specific movement, combat, inventory, chat, quest or content message schemas beyond their extension/registry mechanism.
- Platform contract mutation or rollout.
- QUIC, application compression, live channel migration or Canary compatibility in v1.

## Implementation / findings

Discovery is in progress. The old Platform tuple is being decomposed into reusable security requirements versus stale runtime/wire assumptions. Transport, IDL, message registry, ordering and hard-limit decisions will be frozen only where required to unblock FND-03 and the first native vertical slice.

## Validation

### Focused

- command/run: repository documentation/governance validator on exact PR head
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture/contract/schema-definition documentation only; no executable component changes
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` for this contract-delivery PR; the contract defines mandatory later E2E/fixture evidence but does not implement the protocol
- result: `NOT_APPLICABLE`

### Exact-head CI

- final head: pending
- trigger source: pull_request
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: adversarial protocol/security/compatibility architecture review against accepted Oteryn-v2 ADRs, FND-ID, Platform reconciliation input, current TLS/Protobuf primary sources and full package diff
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: none open at task start
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Dedicated FND-02 architecture-only task created from current main after all open PRs were cleared.
status: investigating
branch: docs/OTV2-20260808-fnd02-protocol-contract
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
next_action: Freeze the smallest complete FND-02 transport, wire, ordering, reconciliation and resource-limit contract from primary evidence.
```
