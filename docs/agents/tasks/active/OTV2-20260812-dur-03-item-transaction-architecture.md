# OTV2-20260812-dur-03-item-transaction-architecture

```yaml
task_id: OTV2-20260812-dur-03-item-transaction-architecture
title: DUR-03 item transaction and anti-duplication architecture
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: agent/otv2-20260812-dur-03-item-transaction-architecture
pr: 207
base_sha: 2521882253b04287e1243c54692440120e0b6c8e
head_sha: a2c2913b77d5ca21ccbeb726e4c08369c2ecbd22
final_head_sha: null
final_head_frozen_at: null
owner: architecture-coordinator/current-session
created_at: 2026-08-12T14:23:00+02:00
updated_at: 2026-08-12T14:44:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260812-dur-03-item-transaction-architecture.md
  - docs/architecture/DUR-03_ITEM_TRANSACTION_AND_ANTI_DUPLICATION_ANALYSIS.md
  - docs/architecture/DUR-03_ITEM_TRANSACTION_AND_ANTI_DUPLICATION_CONTRACT.md
public_contracts:
  - DUR-03
depends_on:
  - GAME-ITEM-01
  - DUR-01
  - DUR-02
  - ANL-01
  - FND-02
  - FND-03
  - FND-04
blocks:
  - durable item/currency/value runtime implementation
  - item/value portion of later VSL persistence/loot/pickup proofs
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Produce one bounded, paper-only `DUR-03` architecture candidate that freezes authoritative item/currency/value transaction, single-location, identity-transition, idempotency, retry/crash, provenance and anti-duplication invariants on top of accepted GAME-ITEM-01, DUR-01, DUR-02 and ANL-01.

The delivery must not implement Rust/runtime/client behavior, PostgreSQL DDL/migrations, production deployment or entitlement activation. Maintained programme/status/register/horizon/index sources remain at live-main pre-acceptance state while the candidate PR is open; any acceptance promotion is deferred to a separate post-merge lifecycle closeout.

## Architecture and source of truth

- `PROVEN`: `main@2521882253b04287e1243c54692440120e0b6c8e` records `GAME-ITEM-01 = ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED` and `DUR-03 = PROPOSED / PLANNED / NOT_STARTED` as the next eligible paper-only item/value architecture gate.
- `PROVEN`: `GAME-ITEM-01_ITEM_MODEL_AND_EQUIPMENT_CONTRACT.md` owns typed item legality, ItemType/ItemInstance/StaticItemPlacement semantics, equipment/container legality and definition compatibility while explicitly assigning atomic location, conservation and create/destroy/split/merge/transform identity transitions to DUR-03.
- `PROVEN`: `DUR-01_DURABLE_IDENTIFIER_REPRESENTATION_CONTRACT.md` defines `ItemInstanceId` as a strong UUIDv7, full 128-bit, non-reused durable identity and leaves lifecycle transition rules to DUR-03.
- `PROVEN`: `DUR-02_PERSISTENCE_V1_OWNER_BASELINE.md` owns common migration/transaction/outbox/durable-ack/PITR/schema-evolution rules and permits stricter DUR-03 domain transaction rules.
- `PROVEN`: `ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_CONTRACT.md` owns EventId/OperationId/TransactionId/TransactionEventRef semantics, immutable durable audit evidence and replay/read-only boundaries.
- `PROVEN`: FND-02 owns `CommandRef = (GameSessionId, CommandId)`, ordered exactly-once command reservation semantics and duplicate/result reconciliation; FND-03/FND-04 retain runtime ownership/session/lease/recovery fencing.
- `PROVEN`: ADR-0006 requires durable transactional evidence for security-relevant item/currency mutations including create/destroy, split/merge, location/ownership changes, loot, pickup, trade, market, mail, depot, rewards, currency, retry/rollback and commit resolution.
- `PROVEN`: open PR #191 changes only GAME-CHAR provenance paths; open PR #162 changes CI/governance paths and `BUILD_TEST_MATRIX.md`; neither overlaps the three owned DUR-03 paths.
- `UNKNOWN`: exact Reference-specific item source/sink, trade/market/bank/depot/mail/reward/crafting/decay edge behavior not established by accepted evidence remains parity-pending and may not be invented here.

## Acceptance criteria

- [x] Freeze one authoritative immediate-location invariant for every live ItemInstance without collapsing world scope, binding, custody or authorization.
- [x] Define create/destroy/split/merge/quantity-transfer/transform identity-transition rules that preserve DUR-01 non-reuse and do not invent Reference-specific transform policies.
- [x] Define deterministic item/currency/value conservation accounting that distinguishes pure transfer from explicit mint/burn/transform/conversion and records complete lineage rather than market-value equality.
- [x] Define player-command, cross-retry and multi-step idempotency ownership using CommandRef, OperationId and TransactionId without minting a new semantic operation on ambiguous retry.
- [x] Define ambiguous commit reconciliation, durable receipts and fail-closed duplicate/conflicting retry behavior.
- [x] Define transaction authority/fencing requirements for CharacterLease/GameSession and channel/instance ownership without treating ItemInstanceId, binding or transport identity as authorization.
- [x] Define bounded atomic participant sets, anomaly-proof locking/isolation obligations and safe multi-transaction custody for workflows that cannot fit one transaction.
- [x] Define container-subtree and equipment atomicity interactions without duplicating GAME-ITEM legality ownership.
- [x] Define mandatory ANL-compatible DURABLE_AUDIT/provenance evidence without selecting physical tables, broker or speculative event IDs.
- [x] Define cross-world and cross-authority behavior fail-closed; no implicit cross-world value transfer or cross-database distributed transaction.
- [x] Define restore/recovery reconciliation invariants preventing stale authority, duplicate remint and silent corruption repair.
- [x] Preserve downstream product/domain ownership for loot cause, trade, market, bank, depot, mail, rewards, houses, crafting/ruleset and entitlement policy.
- [x] Apply architecture decision discipline: decision timing, blocked work, future migration cost, supersession evidence and deliberately deferred scope.
- [ ] Complete exact-head self-review, required independent review, governance/document CI and merge only with zero unresolved material findings.
- [ ] After accepted merge, use one separate bounded lifecycle closeout to promote DUR-03 and refresh canonical programme handoff; do not promote status in the open delivery PR.

## Excluded scope

- Rust/runtime/client implementation or gameplay command payload implementation.
- PostgreSQL DDL, migration files/execution, physical table/index/constraint/locking syntax or concrete ORM/driver selection.
- Production deployment, traffic, credentials, live data/session mutation, protected-environment changes or backup operations.
- Exact unevidenced Reference values/formulas/source-sink rates/market semantics.
- Reopening accepted GAME-ITEM, DUR-01, DUR-02, ANL-01, FND-02/FND-03/FND-04 semantics except through an explicit conflict found in source audit.
- Business state machines for trade, market, bank, depot, mail, houses, rewards, crafting, loot generation or entitlement activation.
- Concrete ANL protobuf event IDs/payload schemas; this candidate defines mandatory evidence semantics and requires concrete registration before implementation conformance.

## Implementation / findings

Preflight on `main@2521882253b04287e1243c54692440120e0b6c8e` found no active DUR-03 task and no overlapping open PR ownership. Draft PR #207 was opened early from the dedicated branch. Shared canonical status/register/handoff files remain intentionally outside the delivery diff so the open candidate cannot mark itself accepted.

Source/option audit produced the following candidate architecture:

1. **Immediate location:** one live ItemInstance has exactly one typed immediate authoritative location. Contained descendants point to their immediate parent; moving a container does not rewrite descendants.
2. **Identity transitions:** same concrete lifecycle preserves ItemInstanceId; new independently locatable lifecycle gets a fresh ID; retired IDs never return. Split keeps source ID + mints one new stack ID; merge keeps receiving ID and retires an emptied source; type-changing transform identity policy is explicit and fail-closed when unresolved.
3. **Conservation:** transactions classify mutations as TRANSFER, SPLIT_MERGE_QUANTITY, STATE_MUTATION, MINT, BURN, TRANSFORM or CONVERSION. Conservation tracks exact units/input-output lineage and typed source/sink rules, never market-price equality.
4. **Transaction identity:** every atomic durable mutation has one ANL TransactionId; ambiguous outcome preserves/reconciles that identity. OperationId spans retryable/multi-step workflows; FND-02 CommandRef remains player-command ingress identity/order.
5. **Custody:** multi-transaction workflows may progress only through explicit typed immediate custody/escrow so committed intermediate steps cannot leave value spendable in the previous location.
6. **Authority:** CharacterLease/GameSession/runtime ownership fences remain current authority; binding, ItemInstanceId or location never grants authority. Same-GameSession reconnect is preserved without incorrectly demanding the old transport generation remain current at commit.
7. **Atomicity:** current v1 atomic item/value mutation stays inside one game-owned `oteryn_game` PostgreSQL transaction. Cross-database/service value transfer is unsupported until separately contracted.
8. **Evidence:** durable item/currency transaction evidence is ANL-compatible, fixed before ambiguous commit, atomically committed and read-only under replay/analytics. Concrete event IDs/schema and numeric resource ceilings remain implementation blockers, not guessed architecture values.
9. **Recovery:** restore resumes item/value mutation only after location, identity, container, receipt/source-cause, audit-completeness and authority-fence reconciliation passes.

The analysis rejects subsystem-specific location columns, generic authoritative transaction JSON/EAV, market-price conservation, event sourcing as mutation authority, blind retry with new identity, and implicit distributed transactions.

## Validation

### Focused

- full source/ownership/architecture consistency audit against GAME-ITEM, DUR-01, DUR-02, ANL-01, FND-02 and FND-04: complete for candidate drafting
- governance/document/link validation: pending exact final head

### Component/integration

- command/run: `NOT_APPLICABLE` — paper-only architecture candidate; no executable component changes
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no runtime/client/production outcome is introduced
- result: `NOT_APPLICABLE`

### Exact-head CI

- final head: pending
- trigger source: PR #207
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Self-review

- exact head: pending after final task/PR metadata freeze
- method/reviewer: implementing/coordinating agent
- material findings: pending
- verdict: pending

## Independent review

- required: `YES` — DUR-03 defines durable item/currency/value conservation, anti-duplication and authority/failure invariants, explicitly high risk under root review policy
- exact head: pending
- method/auditor: independent mechanism on frozen exact head
- material findings: pending
- verdict: pending

## PR and closeout

- PR: #207 draft
- changed-file review: currently exactly task + analysis + candidate contract
- unresolved review threads: pending
- related/superseded PRs: #191 and #162 are disjoint live work and remain untouched
- protected auto-merge: not configured
- merge commit/result: pending
- ownership release: after terminal lifecycle closeout only

## Context checkpoint

```yaml
last_progress: Completed DUR-03 source/option audit and authored the three-path paper-only candidate package in draft PR #207 without touching canonical status overlays.
status: validating
branch: agent/otv2-20260812-dur-03-item-transaction-architecture
head_sha: a2c2913b77d5ca21ccbeb726e4c08369c2ecbd22
pr: 207
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: pull_request #207
ci_check_generation: pending final freeze
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
owner_action_required: false
blocker: null
next_action: Perform full-diff adversarial self-review of the resulting exact branch head, repair any material finding before freeze, then run required independent review and exact-head CI.
```
