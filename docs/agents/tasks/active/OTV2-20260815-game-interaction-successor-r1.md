# OTV2-20260815-game-interaction-successor-r1

```yaml
task_id: OTV2-20260815-game-interaction-successor-r1
title: GAME-INTERACTION-01 successor — child occurrence identity and retry semantics
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/arch-d-game-interaction-successor-r1
pr: 277
base_sha: cb98fd32a2bb71fce83234ebf8bf69bdd1a1970e
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: GAME-INTERACTION SUCCESSOR ARCHITECTURE AGENT D-R1
created_at: 2026-08-15T11:59:42+02:00
updated_at: 2026-08-15T12:09:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260815-game-interaction-successor-r1.md
  - docs/architecture/GAME-INTERACTION-01_SUCCESSOR_CHILD_IDENTITY_RETRY_ANALYSIS.md
  - docs/architecture/GAME-INTERACTION-01_SUCCESSOR_CHILD_IDENTITY_RETRY_CONTRACT_CANDIDATE.md
public_contracts:
  - GAME-INTERACTION-01 successor child-occurrence identity
  - GAME-INTERACTION-01 cross-owner/client result and retry semantics
depends_on:
  - issue #262 / PR #269 as read-only predecessor evidence
  - docs/contracts/FOUNDATION_ERROR_VOCABULARY.md
  - docs/contracts/FOUNDATION_FAILURE_SCENARIOS.md
  - docs/architecture/FND-02_PROTOCOL_OTERYN_V1_CONTRACT.md
  - docs/architecture/FND-03_RUNTIME_EXECUTION_CONTRACT.md
  - docs/architecture/FND-04C_ERROR_DIAGNOSTICS_FAILURE_COMPATIBILITY_CONTRACT.md
  - docs/architecture/DUR-03_ITEM_TRANSACTION_AND_ANTI_DUPLICATION_CONTRACT.md
  - docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md
  - docs/architecture/SIM-DETERMINISM-01_AUTHORITATIVE_SIMULATION_CONTRACT.md
  - accepted GAME-ITEM-01 contracts
  - accepted/future GAME-ABILITY-01 owning contract for ability-owned effect semantics
blocks:
  - GAME-INTERACTION-01 implementation until coordinator accepts an integrated contract
cross_repository_coordination_id: null
external_repositories: []
```

## Outcome

Create a fresh, bounded successor delivery for the unchanged `GAME-INTERACTION-01` gate that resolves only the two final findings left by predecessor issue #262 / draft PR #269:

1. a stable source-derived child-occurrence identity for fan-out/cascade siblings; and
2. complete cross-owner/client error, retry, ambiguity and reconciliation semantics conforming to `FOUNDATION_ERROR_VOCABULARY`.

This is **not repair cycle 4** for the predecessor. The predecessor task records `repair_cycles_for_current_gate: 3`; its exact reviewed head `71253a8d5805ed37ec451e40e2c7200c38031a52` and lifecycle remain read-only to this successor.

The gate ID remains `GAME-INTERACTION-01`. This task does not create a new global gate or generic global interaction UUID.

## Architecture and source of truth

### PROVEN

- `main@cb98fd32a2bb71fce83234ebf8bf69bdd1a1970e` was the trusted base when this successor branch was created.
- Issue #262 and draft PR #269 remain open/unmerged predecessor records.
- Predecessor task `docs/agents/tasks/active/OTV2-20260815-game-interaction-architecture.md` on reviewed head `71253a8d5805ed37ec451e40e2c7200c38031a52` records `repair_cycles_for_current_gate: 3`.
- PR #269's final coordinator reconciliation identifies exactly two remaining material findings: child fan-out identity and public/cross-owner retry/error semantics.
- FND-02 defines `CommandRef = (GameSessionId, CommandId)`, reserves a command once, never re-executes a lower already-reserved CommandId, and preserves authoritative pending/terminal command identity across eligible same-GameSession reconnect.
- SIM-DETERMINISM requires retry-stable gameplay random decisions derived from stable semantic identity and forbids process-global RNG, container iteration, worker order or transient generation as the semantic identity of a retry.
- DUR-03 requires same logical item transaction/operation reconciliation across ambiguous completion and forbids stale-generation completion from mutating a newer runtime owner.
- `FOUNDATION_ERROR_VOCABULARY.md` requires public/cross-component errors to specify stable category/code ownership, progression, retry authority, correlation, idempotency/partial-mutation outcome and bounded internal-to-public mapping.

### DERIVED / proposed in this successor

- A direct child is a stable composite of parent/root source occurrence, definition/object identity, authoritative target, typed edge/capability, optional semantically justified child ordinal and exact behavior-affecting semantic revision context.
- For nested cascades the parent source is the stable parent `InteractionChildOccurrenceRef`, yielding a bounded deterministic ancestry path without a global UUID.
- Runtime ownership generation and mutable state revisions fence application/completion but do not by themselves create a new logical child identity on failover.
- Cross-owner ambiguity surfaces as `PENDING` and reconciles the same child/foreign-owner operation; a new client `CommandRef` for the same intent is forbidden until the prior occurrence is proven terminal.
- Foundation `STALE_GENERATION` applies to rejection of the stale completion/application itself; if the underlying delegated operation may already have committed, the child remains separately `PENDING` under same-occurrence reconciliation.
- Foundation `CANCELLED` is emitted only after documented cleanup/retirement; an ambiguous cancel/commit race remains `PENDING` rather than being prematurely labelled cancelled.

### UNKNOWN / explicitly outside this task

- the final movement/teleport/handoff owner contract;
- the final durable writable-text owner contract;
- final GAME-ABILITY formulas/effect internals and any unmerged whole-gate candidate;
- numeric resource ceilings;
- concrete Rust/storage/wire implementation or numeric wire error values.

## Acceptance criteria

- [ ] Successor artifacts explicitly link predecessor #262/#269 and explain the repair-cycle stop condition.
- [ ] Gate remains `GAME-INTERACTION-01`; no new global gate ID is introduced.
- [ ] Composite child-occurrence identity distinguishes flat siblings and nested cascade paths without a generic global UUID.
- [ ] Same child retry/replay/recovery is exactly-once/idempotent and cannot reroll deterministic RNG.
- [ ] Canonical child ordering/ordinal assignment cannot derive from hash-map/container/thread/worker iteration order.
- [ ] Ownership generation/revision fencing remains fail-closed without turning failover into a fresh semantic child.
- [ ] Deterministic acceptance scenario covers one movement occurrence -> N contacts -> partial delivery/retry/recovery -> every child exactly once and replay-identical.
- [ ] Public/cross-owner error matrix covers at least `DEPENDENCY_UNAVAILABLE`, `TIMEOUT`, `CANCELLED`, stale/delegated completion ambiguity and coupled-workflow pending/recovery.
- [ ] Every public row states stable code/category, progression, retry authority, same/new `CommandRef` rule, correlation, local mutation possibility, caller-visible committed/pending/rejected state and final reconciliation owner.
- [ ] Foreign narrow-code ownership is named explicitly; missing foreign contracts become implementation blockers rather than caller guesswork.
- [ ] Predecessor good invariants remain intact: server target authority, typed state machines, explicit scope/lifetime, GAME-ITEM/DUR-03 value authority, GAME-ABILITY effect authority, delegated movement/handoff, named coupled workflows, bounded cascades, proposal-only scripts, deterministic revisions/order and no generic mutable `GLOBAL` scope.
- [ ] Full exact-head changed-file/diff self-review finds no coordinator-only/sibling/predecessor-path mutation.
- [ ] Ordinary required exact-head repository CI is green or any infrastructure-only blocker is recorded truthfully.
- [ ] PR remains draft; no Codex/OpenAI/owner-funded AI review is triggered.
- [ ] Worker leaves no merge/archive/issue-close/ownership-release action and hands off with `NEXT_ACTION: ARCHITECTURE_COORDINATOR_AUDIT`.

## Excluded scope

This successor MUST NOT decide, implement or mutate:

- teleport/movement/relocation/handoff owner selection;
- durable writable-text owner selection;
- GAME-ABILITY formulas/effect internals;
- numeric resource-limit values;
- Rust runtime/client/server/protocol implementation;
- PostgreSQL DDL/migrations;
- Platform or any external repository;
- production/deployment/live state;
- coordinator-only global architecture/status/register/horizon surfaces;
- predecessor #262/#269 task/PR lifecycle;
- generic global `InteractionId`/UUID or generic process-global interaction scope.

## Implementation / findings

### Successor governance

- New successor issue: #274.
- New draft PR: #277.
- Predecessor: issue #262 / draft PR #269 / `docs/arch-d-game-interaction`.
- Successor branch: `docs/arch-d-game-interaction-successor-r1`.
- This task has used one repair cycle for the current successor gate after self-review separated stale-completion application failure from underlying delegated-operation outcome and aligned cancellation semantics with the Foundation vocabulary.
- The predecessor remains at its independent exhausted count of three; this successor repair does not modify/reset that count.

### Intended semantic shape

```text
InteractionChildOccurrenceRef = (
  ParentSourceOccurrenceRef,
  InteractionDefinitionRef,
  AuthoritativeTargetDiscriminator,
  TypedEdgeOrCapabilityDiscriminator,
  OptionalCanonicalChildOrdinal,
  SemanticRevisionContext
)

first-level ParentSourceOccurrenceRef = RootSourceOccurrenceRef
nested ParentSourceOccurrenceRef = parent InteractionChildOccurrenceRef
```

The contract candidate defines tuple/path equality and lifecycle semantics while leaving physical serialization, digest/hash algorithm, storage schema and numeric wire representation unfrozen.

### Public result shape

```text
COMMITTED | PENDING | REJECTED
```

`PENDING` is not permission to issue a second logical attempt. It is explicit reconciliation state for the same source occurrence/child/foreign-owner operation.

## Validation

### Focused

- source-contract consistency review: final exact-head review pending after successor repair cycle 1
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — paper-only architecture delivery, no executable component changed
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no runtime/client/server implementation is authorized; deterministic scenarios are architecture acceptance fixtures only
- result: `NOT_APPLICABLE`

### Exact-head CI

- final head: recorded externally after this final metadata commit to avoid a self-referential SHA mutation
- trigger source: draft PR / final metadata commit
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Self-review

- exact head: recorded externally after final metadata commit
- method/reviewer: GAME-INTERACTION SUCCESSOR ARCHITECTURE AGENT D-R1
- material findings: one Foundation category/partial-mutation ambiguity found on first pass and repaired in successor repair cycle 1; final pass pending
- verdict: pending

## Independent review

- required: `NO` at worker stage — worker must not trigger Codex/OpenAI/owner-funded review; Architecture Coordinator owns any separately authorized audit/review action
- exact head: `NOT_APPLICABLE`
- method/auditor: `NOT_APPLICABLE` at worker stage
- material findings: `NOT_APPLICABLE`
- verdict: `NOT_APPLICABLE`

## PR and closeout

- changed-file review: pending final exact-head pass
- unresolved review threads: pending
- related/superseded PRs: predecessor draft PR #269 remains open/read-only to this worker
- protected auto-merge: forbidden
- merge commit/result: `NOT_APPLICABLE` — coordinator-only
- ownership release: `NOT_APPLICABLE` — coordinator-only

## Context checkpoint

```yaml
last_progress: successor repair cycle 1 aligned stale-completion and cancellation ambiguity with Foundation category semantics; metadata frozen for exact-head validation
status: validating
branch: docs/arch-d-game-interaction-successor-r1
head_sha: null
pr: 277
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: pull_request
ci_check_generation: null
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
owner_action_required: ARCHITECTURE_COORDINATOR_AUDIT_AFTER_WORKER_VALIDATION
blocker: null
next_action: perform final full exact-head diff self-review and exact-head CI validation
```

`MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`  
`IMPLEMENTATION_AUTHORITY: NONE`
