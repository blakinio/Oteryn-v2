# OTV2-20260812-dur-02-whole-gate-reconciliation

```yaml
task_id: OTV2-20260812-dur-02-whole-gate-reconciliation
title: Reconcile the complete historical DUR-02 Persistence-v1 gate
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260812-dur-02-whole-gate-reconciliation
pr: null
base_sha: 710c4b5e00de9f14224a6949c3bc7364f4c724a4
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-12T09:12:00+02:00
updated_at: 2026-08-12T09:12:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260812-dur-02-whole-gate-reconciliation.md
  - docs/architecture/DUR-02_PERSISTENCE_V1_WHOLE_GATE_RECONCILIATION.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
public_contracts: []
depends_on:
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/architecture/ADR-0004-postgresql-and-data-ownership.md
  - docs/architecture/DUR-01_DURABLE_IDENTIFIER_REPRESENTATION_CONTRACT.md
  - docs/architecture/ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_CONTRACT.md
  - docs/architecture/DUR-02_PROFILE_NEUTRAL_CHARACTER_PERSISTENCE_OWNER_BASELINE.md
  - docs/architecture/FND-03_RUNTIME_EXECUTION_CONTRACT.md
  - docs/architecture/FND-04_IDENTITY_GAME_SESSION_ADMISSION_CHARACTER_LEASE_CONTRACT.md
  - docs/architecture/GAMEPLAY_AND_PRODUCT_ARCHITECTURE_HORIZON.md
blocks:
  - owner decision on the minimum remaining whole-DUR-02 closure package
  - later separately authorized Persistence-v1 implementation design
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Reconcile every historical subject listed under stable gate `DUR-02 — Persistence v1` against the architecture that was accepted later. Produce one nonbinding closure packet that distinguishes:

- already satisfied by binding architecture;
- still genuinely owned by DUR-02;
- moved to another named gate/domain;
- implementation/operations choices that should not remain architecture blockers;
- owner decisions still required before overall `DUR-02` may become `ACCEPTED`.

No SQL DDL, database migration, Rust persistence code, runtime behavior or production action is authorized.

## Architecture and source of truth

- `PROVEN`: current trusted base is `main@710c4b5e00de9f14224a6949c3bc7364f4c724a4`.
- `PROVEN`: profile-neutral Character persistence is already a binding `OWNER_ACCEPTED PARTIAL BASELINE / LIFECYCLE_CLOSED / NOT_STARTED`.
- `PROVEN`: overall `DUR-02` remains `PROPOSED / PLANNED / NOT_STARTED` specifically because historical Persistence-v1 scope is broader than that Character sub-scope.
- `PROVEN`: historical `FOUNDATION_DECISION_BACKLOG.md` lists migration mechanism/schema ownership, Character/lease state, item transfers, idempotency, isolation, outbox/audit, checkpoint/progress loss, market/guild/house/reward consistency, partitioning, backup/PITR/RPO/RTO and rollout/rollback under DUR-02.
- `PROVEN`: later accepted architecture gives item/economy conservation to `GAME-ITEM-01` + `DUR-03`, event/audit semantics to `ANL-01`, Character/session persistence semantics to the accepted partial baseline + FND-04, runtime checkpoint/replay semantics to FND-03, and production capacity/operations objectives to PERF/OPS gates.
- `PROVEN`: open PR #191 is a disjoint GAME-CHAR factual provenance correction and PR #162 is disjoint CI/governance work; neither is owned or modified here.

## Acceptance criteria

- [ ] Enumerate every historical DUR-02 subject without omission.
- [ ] Assign exactly one primary disposition to each subject: `SATISFIED`, `RETAIN_DUR02`, `MOVED`, or `IMPLEMENTATION_DEFERRED`.
- [ ] Name the canonical evidence/owner for every `SATISFIED` or `MOVED` subject.
- [ ] Do not silently move item/currency/market/house/social semantics back into generic Persistence-v1.
- [ ] Preserve the accepted Character persistence partial baseline unchanged.
- [ ] Separate architecture requirements from exact library/tool/index/partition/backup cadence choices.
- [ ] Define the smallest remaining owner decision package required for honest overall DUR-02 acceptance.
- [ ] State precisely what whole-DUR-02 acceptance would and would not unblock.
- [ ] Keep runtime/DDL/migrations/production unauthorized.
- [ ] Complete full exact-head self-review and repository-required documentation CI before merge.

## Excluded scope

- no whole-DUR-02 owner acceptance in this task;
- no PostgreSQL DDL or migrations;
- no Rust persistence implementation;
- no selection of ORM/query builder/database crate;
- no item/currency conservation design;
- no market/guild/house/reward gameplay semantics;
- no numeric production RPO/RTO/capacity/backup cadence;
- no Platform writes or external-repository mutation;
- no production deployment.

## Initial reconciliation hypothesis

The historical gate has accumulated subjects that no longer belong to one monolithic persistence contract. The likely remaining whole-DUR-02 architecture core is much smaller:

1. game-owned migration artifact/authority model;
2. cross-domain transaction/isolation policy principle;
3. common durable audit/outbox persistence substrate boundary;
4. durable-acknowledgement versus runtime-checkpoint/progress-loss distinction;
5. PostgreSQL backup/PITR/restore safety envelope without numeric operational targets;
6. game-wide compatible schema-evolution discipline.

Everything else must be proven already satisfied, moved to another gate, or deferred as an implementation/operations choice rather than kept as an artificial blocker.

## Validation

### Focused

- compare every historical backlog bullet with current binding architecture and named owner;
- verify no later gate is silently pre-accepted;
- result: pending.

### Component/integration/runtime E2E

`NOT_APPLICABLE` — nonbinding paper-only architecture reconciliation.

### Exact-head CI

Pending final immutable PR head.

## Self-review

Pending final immutable PR head.

## Independent review

- required: `NO` for the nonbinding reconciliation packet unless final review identifies material uncertainty or the delivery accidentally creates binding persistence/recovery authority; a later owner-acceptance delivery must reassess and is expected to require independent review.

## PR and closeout

- intended changed files: task + reconciliation packet + narrow current-status `PLANNED -> OPEN` while this concrete gate delivery exists;
- PR #191 and #162 remain untouched;
- closeout after merge returns overall DUR-02 delivery to `PLANNED` until owner decision is recorded.

## Context checkpoint

```yaml
last_progress: Whole-DUR-02 reconciliation task claimed from main after the Character persistence partial baseline lifecycle closed.
status: implementing
branch: docs/OTV2-20260812-dur-02-whole-gate-reconciliation
pr: null
final_head_sha: null
final_head_frozen_at: null
ci_checks_for_current_head: 0
repair_cycles_for_current_gate: 0
owner_action_required: null
blocker: null
next_action: Write the exhaustive historical-subject reconciliation and minimum whole-DUR-02 closure decision package.
```
