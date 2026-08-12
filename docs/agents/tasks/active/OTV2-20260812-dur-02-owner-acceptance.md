# OTV2-20260812-dur-02-owner-acceptance

```yaml
task_id: OTV2-20260812-dur-02-owner-acceptance
title: Persist owner-accepted whole DUR-02 Persistence-v1 baseline
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260812-dur-02-owner-acceptance
pr: null
base_sha: 4f4ac4f0891b9d37dcefd413d1baf724c20d301c
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-12T09:41:00+02:00
updated_at: 2026-08-12T09:41:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260812-dur-02-owner-acceptance.md
  - docs/architecture/DUR-02_PERSISTENCE_V1_OWNER_BASELINE.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
  - docs/architecture/GAMEPLAY_AND_PRODUCT_ARCHITECTURE_HORIZON.md
public_contracts: []
depends_on:
  - docs/architecture/DUR-02_PERSISTENCE_V1_WHOLE_GATE_RECONCILIATION.md
  - docs/architecture/DUR-02_PROFILE_NEUTRAL_CHARACTER_PERSISTENCE_OWNER_BASELINE.md
  - docs/architecture/ADR-0004-postgresql-and-data-ownership.md
  - docs/architecture/DUR-01_DURABLE_IDENTIFIER_REPRESENTATION_CONTRACT.md
  - docs/architecture/ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_CONTRACT.md
  - docs/architecture/FND-03_RUNTIME_EXECUTION_CONTRACT.md
  - docs/architecture/FND-04_IDENTITY_GAME_SESSION_ADMISSION_CHARACTER_LEASE_CONTRACT.md
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/architecture/ARCHITECTURE_STATUS_MODEL.md
blocks:
  - separately authorized server/persistence foundation implementation programme
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Persist the owner's explicit acceptance of the six-rule minimum whole-`DUR-02 — Persistence v1` closure package and the exhaustive fourteen-subject reconciliation disposition as the binding owner baseline for the whole gate.

After terminal delivery/closeout the intended architecture status is:

```text
DUR-02 — Persistence v1
DecisionStatus       = ACCEPTED
DeliveryStatus       = LIFECYCLE_CLOSED
ImplementationStatus = NOT_STARTED
Runtime authority    = NONE
DDL/migrations       = NOT_AUTHORIZED by architecture acceptance alone
```

## Owner source

`USER_SOURCE`: on 2026-08-12 at 09:41 +02:00, immediately after presentation of the complete six-rule whole-DUR-02 closure package and the fourteen-subject reconciliation, the owner replied:

> tak

This task treats that reply as explicit acceptance of the complete recommended package in `DUR-02_PERSISTENCE_V1_WHOLE_GATE_RECONCILIATION.md`, including the dispositions, scope boundaries, implementation consequences, non-decisions and supersession rules.

## Acceptance criteria

- [ ] Add `DUR-02_PERSISTENCE_V1_OWNER_BASELINE.md` as the binding whole-gate owner baseline.
- [ ] Bind the six remaining common Persistence-v1 rules without weakening the accepted Character persistence partial baseline.
- [ ] Bind all fourteen historical subject dispositions and exact destination ownership where moved.
- [ ] Set overall DUR-02 to `ACCEPTED` only in current coordination state; keep `ImplementationStatus=NOT_STARTED` and runtime/DDL authority `NONE`.
- [ ] Explicitly preserve GAME-ITEM-01/DUR-03 as the authority for item/currency/value semantics and conservation.
- [ ] Explicitly preserve ANL-01 event/audit semantic ownership, FND-03 runtime checkpoint/replay ownership and FND-04 session/lease/recovery authority.
- [ ] Preserve exact library/tool/index/partition/RPO/RTO/cadence choices as downstream unless later evidence creates an architecture constraint.
- [ ] State that accepted DUR-02 permits a separately authorized server/persistence foundation implementation programme without waiting for GAME-ITEM-01/DUR-03, while durable item/value mutation remains blocked on those gates.
- [ ] Update current status, global register and gameplay/product horizon narrowly.
- [ ] Do not implement SQL DDL, migrations, Rust persistence/server runtime, Platform writes or production actions.
- [ ] Complete exact-head self-review, mandatory independent exact-head review, repository-required CI, squash merge and lifecycle closeout.

## Excluded scope

- no PostgreSQL schema creation or migration execution;
- no Rust game-server or persistence implementation;
- no database credentials/provisioning;
- no item/currency/value persistence before GAME-ITEM-01 + DUR-03;
- no market/guild/house/reward semantic acceptance;
- no exact Rust DB/migration crate selection;
- no partitioning/sharding decision;
- no numeric RPO/RTO/backup cadence/retention values;
- no Platform database changes;
- no production rollout/traffic;
- no unresolved Reference behavior inference.

## Validation

### Focused

Reconcile the binding owner baseline against the lifecycle-closed whole-gate reconciliation, Character persistence partial baseline, ADR-0004, DUR-01, ANL-01, FND-03/FND-04 and current status model.

### Component/integration/runtime E2E

`NOT_APPLICABLE` — paper-only owner architecture acceptance; no executable database/runtime behavior changes.

### Independent review

Required: **YES**. Whole-gate acceptance makes persistence, migration, transaction, crash-recovery, publication-checkpoint and restore-safety guarantees binding architecture, so one genuinely independent exact-head review is mandatory before merge.

## Context checkpoint

```yaml
last_progress: Owner explicitly accepted the complete six-rule whole-DUR-02 closure package and fourteen-subject reconciliation; fresh owner-acceptance task claimed from main.
status: implementing
branch: docs/OTV2-20260812-dur-02-owner-acceptance
pr: null
final_head_sha: null
final_head_frozen_at: null
ci_checks_for_current_head: 0
repair_cycles_for_current_gate: 0
owner_action_required: null
blocker: null
next_action: Write the binding DUR-02 whole-gate owner baseline and synchronize current coordination state without creating implementation authority.
```
