# OTV2-20260812-game-item-01-architecture

```yaml
task_id: OTV2-20260812-game-item-01-architecture
title: GAME-ITEM-01 item model and equipment architecture
mode: CONTRACT
status: investigating
repository: blakinio/Oteryn-v2
base_branch: main
branch: agent/otv2-20260812-game-item-01-architecture
pr: null
base_sha: 93a49731ad91620748b87cdaba9525c9df70bc12
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: architecture-coordinator/current-session
created_at: 2026-08-12T11:37:00+02:00
updated_at: 2026-08-12T11:37:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260812-game-item-01-architecture.md
  - docs/architecture/GAME-ITEM-01_ITEM_MODEL_AND_EQUIPMENT_ANALYSIS.md
  - docs/architecture/GAME-ITEM-01_ITEM_MODEL_AND_EQUIPMENT_CONTRACT.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
  - docs/architecture/GAMEPLAY_AND_PRODUCT_ARCHITECTURE_HORIZON.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
  - docs/architecture/README.md
public_contracts:
  - GAME-ITEM-01
depends_on:
  - GAME-VISION-01
  - DUR-01
  - DUR-02
  - ANL-01
  - ADR-0005
blocks:
  - DUR-03
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Produce one bounded, paper-only `GAME-ITEM-01` architecture package that closes the native item-model and equipment semantic boundary needed by `DUR-03`, while preserving the accepted first Reference target, stable content identity, durable ItemInstanceId semantics, common persistence/audit boundaries and fail-closed parity discipline.

## Architecture and source of truth

- `PROVEN`: `GAME-VISION-01_FIRST_REFERENCE_BASELINE_OWNER_BASELINE.md` fixes the first Reference target to Global Tibia production-observable behavior after the 2026-07-28 server-save/maintenance change boundary and requires `UNKNOWN`/`CONFLICT` behavior to remain fail-closed.
- `PROVEN`: ADR-0005 makes stable namespaced Content Registry keys canonical and compact numeric item/content IDs revision-scoped runtime mappings only.
- `PROVEN`: `DUR-01_DURABLE_IDENTIFIER_REPRESENTATION_CONTRACT.md` defines `ItemInstanceId` as a strongly typed UUIDv7 and leaves create/destroy/split/merge/transform identity-transition rules to `DUR-03`.
- `PROVEN`: `DUR-02_PERSISTENCE_V1_OWNER_BASELINE.md` keeps common transaction/audit substrate in DUR-02 while moving inventory/equipment/ground-item transfer semantics to GAME-ITEM-01 + DUR-03.
- `PROVEN`: `ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_CONTRACT.md` owns event/audit identity and durable evidence semantics; analytics never becomes gameplay authority.
- `UNKNOWN`: exact Reference item limits, formula ordering and edge-case behavior not established by accepted evidence remain parity-pending and may not be invented in this task.

## Acceptance criteria

- [ ] Freeze the semantic boundary between immutable/versioned item definitions and concrete durable item instances without redefining `ItemInstanceId`.
- [ ] Define typed bounded state capabilities for stack quantity, charges, durability, decay/expiration, binding/restrictions, upgrades/modifiers and container capability; prohibit a generic authoritative JSON/EAV escape hatch.
- [ ] Define equipment legality using server-authoritative slot/occupancy claims, requirements and mutually-exclusive constraints without hard-coding client authority.
- [ ] Define deterministic modifier/derived-stat ordering responsibility and its boundary with ruleset/SIM formula ownership.
- [ ] Define bounded container graph legality, nesting/capacity/weight limits and cycle prevention while leaving atomic transfer/single-location conservation to DUR-03.
- [ ] Define content-definition revision compatibility, explicit migration requirements and no-silent-reinterpretation rules.
- [ ] Define world/account/character binding/restriction semantics and separate item-instance semantics from non-item currency/value ledgers.
- [ ] Define boundaries with loot, trade, market, bank, depot, mail, rewards, houses, content/scripting, persistence and audit without capturing their transaction policy.
- [ ] Preserve Reference evidence classes and mark exact unevidenced behavior `PARITY_PENDING_EVIDENCE` rather than guessing.
- [ ] Reconcile the gate in current-status/horizon/register only if the package has enough evidence to change canonical truth.
- [ ] Run repository governance/document validation and exact-head review/CI required for architecture-only delivery.

## Excluded scope

- Rust/runtime/client implementation, SQL DDL, migrations, production deployment or live data changes.
- `DUR-03` conservation, single-authoritative-location, idempotent transfer, split/merge survivor/new-ID rules, transaction isolation proof or anti-duplication implementation.
- Exact Reference numeric values/formulas/limits without accepted evidence.
- Broad item/content import, serializer/container format selection or scripting runtime selection (`DUR-04`).
- Combat/ability formula semantics, market pricing/order-book policy, house/social/reward lifecycle policy, or automatic economy tuning.
- Reintroducing `protocol-canary`, proprietary protocol/code/assets or OTS implementation as production authority.

## Implementation / findings

Task opened from live `main@93a49731ad91620748b87cdaba9525c9df70bc12` after verifying no active GAME-ITEM task/branch/PR ownership overlap. Architecture-only scope; runtime/DDL/production authority remains none.

## Validation

### Focused

- command/run: pending
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — paper-only architecture package; no runtime component change
- result: pending

### E2E

- scenario: `NOT_APPLICABLE` — no executable user/runtime outcome is introduced
- result: pending

### Exact-head CI

- final head: pending
- trigger source: pending
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Self-review

- exact head: pending
- method/reviewer: architecture-coordinator/current-session
- material findings: pending
- verdict: pending

## Independent review

- required: pending
- exact head: pending
- method/auditor: pending
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: none found for GAME-ITEM-01 at task start
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Created bounded paper-only GAME-ITEM-01 task from live main after ownership and dependency verification.
status: investigating
branch: agent/otv2-20260812-game-item-01-architecture
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
next_action: Create the draft GAME-ITEM-01 PR, then author the bounded semantic analysis and contract without taking DUR-03 transaction authority.
```
