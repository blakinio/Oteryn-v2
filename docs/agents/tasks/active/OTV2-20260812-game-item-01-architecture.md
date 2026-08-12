# OTV2-20260812-game-item-01-architecture

```yaml
task_id: OTV2-20260812-game-item-01-architecture
title: GAME-ITEM-01 item model and equipment architecture
mode: CONTRACT
status: reviewing
repository: blakinio/Oteryn-v2
base_branch: main
branch: agent/otv2-20260812-game-item-01-architecture
pr: 205
base_sha: 93a49731ad91620748b87cdaba9525c9df70bc12
head_sha: e60188ff0fa60b00dd59edb9afe09ffcad7364b7
final_head_sha: null
final_head_frozen_at: null
owner: architecture-coordinator/current-session
created_at: 2026-08-12T11:37:00+02:00
updated_at: 2026-08-12T12:10:00+02:00
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

- [x] Freeze the semantic boundary between immutable/versioned item definitions and concrete durable item instances without redefining `ItemInstanceId`.
- [x] Define typed bounded state capabilities for stack quantity, charges, durability, decay/expiration, binding/restrictions, upgrades/modifiers and container capability; prohibit a generic authoritative JSON/EAV escape hatch.
- [x] Define equipment legality using server-authoritative slot/occupancy claims, requirements and mutually-exclusive constraints without hard-coding client authority.
- [x] Define deterministic modifier/derived-stat ordering responsibility and its boundary with ruleset/SIM formula ownership.
- [x] Define bounded container graph legality, nesting/capacity/weight limits and cycle prevention while leaving atomic transfer/single-location conservation to DUR-03.
- [x] Define content-definition revision compatibility, explicit migration requirements and no-silent-reinterpretation rules.
- [x] Define world/account/character binding/restriction semantics and separate item-instance semantics from non-item currency/value ledgers.
- [x] Define boundaries with loot, trade, market, bank, depot, mail, rewards, houses, content/scripting, persistence and audit without capturing their transaction policy.
- [x] Preserve Reference evidence classes and mark exact unevidenced behavior `PARITY_PENDING_EVIDENCE` rather than guessing.
- [x] Reconcile the gate in current-status/horizon/register and architecture index without granting runtime/DDL authority.
- [ ] Run terminal exact-head self-review, required independent review, exact-head CI and lifecycle closeout.

## Excluded scope

- Rust/runtime/client implementation, SQL DDL, migrations, production deployment or live data changes.
- `DUR-03` conservation, single-authoritative-location, idempotent transfer, split/merge survivor/new-ID rules, transaction isolation proof or anti-duplication implementation.
- Exact Reference numeric values/formulas/limits without accepted evidence.
- Broad item/content import, serializer/container format selection or scripting runtime selection (`DUR-04`).
- Combat/ability formula semantics, market pricing/order-book policy, house/social/reward lifecycle policy, or automatic economy tuning.
- Reintroducing `protocol-canary`, proprietary protocol/code/assets or OTS implementation as production authority.

## Implementation / findings

Task opened from live `main@93a49731ad91620748b87cdaba9525c9df70bc12` after verifying no active GAME-ITEM task/branch/PR ownership overlap. `main` was rechecked before terminal-review preparation and remained at the same commit.

The package selects typed capability composition over stable namespaced ItemType definitions, distinguishes authored static placements from durable ItemInstances, defines server-authoritative equipment occupancy and bounded container legality, and requires explicit item-definition compatibility/migration. It intentionally preserves all create/destroy/split/merge/transform identity transitions, atomic item location, idempotency, retry/crash recovery and item/currency/value conservation for `DUR-03`.

All exact Reference item behavior not established by accepted evidence remains parity-pending/fail-closed. Architecture-only scope; runtime/DDL/production authority remains none.

## Validation

### Focused

- command/run: PR #205 per-file patch review against `main` for programme status, global register, gameplay horizon and architecture index; source dependency inspection for GAME-VISION-01, ADR-0005, DUR-01, DUR-02 and ANL-01.
- result: PASS before terminal-head freeze; no unintended historical decision loss detected. One transient historical DUR-01 SHA typo introduced while editing the status overlay was found by self-review and corrected before terminal review; the net PR diff no longer changes that evidence.

### Component/integration

- command/run: `NOT_APPLICABLE` — paper-only architecture package; no runtime component changed.
- result: `NOT_APPLICABLE`.

### E2E

- scenario: `NOT_APPLICABLE` — no executable user/runtime outcome is introduced.
- result: `NOT_APPLICABLE`.

### Exact-head CI

- final head: pending after this checkpoint commit freezes content.
- trigger source: PR #205 / exact final delivery head.
- workflow/run/job: pending.
- runner assignment: pending.
- classification: documentation/governance exact-head CI.
- result: pending.

## Self-review

- exact head: pending after this checkpoint commit.
- method/reviewer: architecture-coordinator/current-session; full changed-path + per-file diff + boundary/authority audit.
- material findings: pending terminal review.
- verdict: pending.

## Independent review

- required: YES — this package makes item-integrity semantics binding and directly constrains later anti-duplication/conservation design.
- exact head: pending after this checkpoint commit.
- method/auditor: `@codex review` on frozen exact head; implementing-agent self-review is not independent evidence.
- material findings: pending.
- verdict: pending.

## PR and closeout

- changed-file review: seven declared task/architecture paths before this checkpoint; terminal recount pending.
- unresolved review threads: pending terminal review.
- related/superseded PRs: none found for GAME-ITEM-01 at task start; unrelated open PRs #191/#162 left untouched.
- protected auto-merge: pending after exact-head evidence.
- merge commit/result: pending.
- ownership release: pending lifecycle-closeout PR after delivery merge.

## Context checkpoint

```yaml
last_progress: Authored and reconciled the bounded GAME-ITEM-01 analysis/contract and coordination overlays in draft PR #205; content is ready to freeze for terminal exact-head self-review, independent Codex review and CI.
status: reviewing
branch: agent/otv2-20260812-game-item-01-architecture
head_sha: e60188ff0fa60b00dd59edb9afe09ffcad7364b7
pr: 205
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: PR #205
ci_check_generation: pending
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
owner_action_required: false
blocker: null
next_action: Freeze the new exact head, mark PR #205 ready, run terminal self-review + independent @codex review + exact-head CI, then merge and perform lifecycle closeout if all evidence passes.
```
