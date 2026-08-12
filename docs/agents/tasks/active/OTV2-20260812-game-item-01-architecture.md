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
head_sha: 4270fa6001e1676742d6e3fd9274635e697f0a18
final_head_sha: null
final_head_frozen_at: null
owner: architecture-coordinator/current-session
created_at: 2026-08-12T11:37:00+02:00
updated_at: 2026-08-12T12:15:00+02:00
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

- parent reviewed head: `4270fa6001e1676742d6e3fd9274635e697f0a18`.
- Dependency Review run `31586112275`: PASS.
- CodeQL run `31586112271`: PASS.
- Agent Governance run `31586112278`: FAIL at PR metadata validation only; title exceeded 72 characters and PR body lacked `## Summary` and `## Validation`. No repository validation step ran in that failed generation.
- repair: PR title shortened to `docs(architecture): define GAME-ITEM-01 item semantics`; body now contains mandatory `## Summary`, `## Scope`, `## Validation` and records the frozen head/evidence. Metadata repair did not alter `4270fa...`.
- current exact head after this audit checkpoint: pending from this commit; fresh PR `synchronize` workflows are required and supersede the failed generation.
- trigger source: PR #205 / exact current delivery head.
- runner assignment: GitHub-hosted Ubuntu 24.04 for the failed governance generation; fresh generation pending.
- classification: documentation/governance exact-head CI.
- result: pending fresh generation.

## Self-review

- parent exact head `4270fa6001e1676742d6e3fd9274635e697f0a18`: review `4915367495`, PASS, zero material architecture findings.
- current exact head: pending after this task-only audit checkpoint.
- method/reviewer: architecture-coordinator/current-session; full changed-path + per-file diff + boundary/authority audit.
- material findings: PR metadata governance failure only after parent-head content review; repository architecture content unchanged by the metadata repair/checkpoint.
- verdict: pending current-head confirmation.

## Independent review

- required: YES — this package makes item-integrity semantics binding and directly constrains later anti-duplication/conservation design.
- parent exact head request: issue comment `5265327419` for `4270fa6001e1676742d6e3fd9274635e697f0a18`; superseded for terminal evidence by this audit-checkpoint commit.
- current exact head: pending after this commit.
- method/auditor: fresh `@codex review` on current exact head; implementing-agent self-review is not independent evidence.
- material findings: pending.
- verdict: pending.

## PR and closeout

- changed-file review: exactly seven declared task/architecture paths.
- unresolved review threads: pending terminal review.
- related/superseded PRs: none found for GAME-ITEM-01 at task start; unrelated open PRs #191/#162 left untouched.
- protected auto-merge: pending after current exact-head evidence.
- merge commit/result: pending.
- ownership release: pending lifecycle-closeout PR after delivery merge.

## Repair history

### Repair cycle 1 — transient status-overlay evidence typo

A historical DUR-01 closeout SHA was mistyped while editing `FOUNDATION_PROGRAMME_CURRENT_STATUS.md`. Self-review found and corrected it before terminal review. The net PR diff preserves the canonical historical SHA.

### Repair cycle 2 — PR metadata governance

Exact-head Agent Governance run `31586112278` failed only its metadata preflight because the initial PR title exceeded 72 characters and the body lacked mandatory `## Summary` / `## Validation` headings. The PR metadata was corrected without changing architecture content. This task-only checkpoint intentionally creates a new PR head so GitHub emits a fresh `synchronize` validation generation using the corrected metadata.

## Context checkpoint

```yaml
last_progress: Corrected PR #205 metadata after exact-head Agent Governance identified title/body contract violations; recorded the repair in-task to force a fresh synchronize generation without changing GAME-ITEM architecture semantics.
status: reviewing
branch: agent/otv2-20260812-game-item-01-architecture
head_sha: 4270fa6001e1676742d6e3fd9274635e697f0a18
pr: 205
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: PR #205
ci_check_generation: pending fresh synchronize generation
ci_checks_for_current_head: 0
ci_run_ids:
  - 31586112278
  - 31586112275
  - 31586112271
ci_job_ids:
  - 94080213201
runner_assignment_state: GitHub-hosted Ubuntu 24.04 observed for failed governance generation; fresh exact-head state pending
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 2
ci_recovery_actions_for_current_head: 1
stall_warnings: 0
owner_action_required: false
blocker: null
next_action: Freeze the new exact head from this checkpoint, re-run terminal self-review and independent @codex review on that SHA, require fresh exact-head governance/dependency/CodeQL PASS, then merge and lifecycle-close if all evidence passes.
```
