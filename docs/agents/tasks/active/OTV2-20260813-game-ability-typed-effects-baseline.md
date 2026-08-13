# OTV2-20260813-game-ability-typed-effects-baseline

```yaml
task_id: OTV2-20260813-game-ability-typed-effects-baseline
title: Record GAME-ABILITY-01 typed effect pipeline owner baseline
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/game-ability-typed-effects-222
pr: null
issue: 222
base_sha: 5518a562bfea55f4f75e3aae03775b33fb55581e
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-13T17:41:00+02:00
updated_at: 2026-08-13T17:41:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260813-game-ability-typed-effects-baseline.md
  - docs/architecture/GAME-ABILITY-01_TYPED_EFFECT_PIPELINE_OWNER_BASELINE.md
public_contracts:
  - docs/architecture/GAME-ABILITY-01_TYPED_EFFECT_PIPELINE_OWNER_BASELINE.md
depends_on:
  - docs/architecture/GAMEPLAY_AND_PRODUCT_ARCHITECTURE_HORIZON.md
  - docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md
  - docs/architecture/SIM-DETERMINISM-01_AUTHORITATIVE_SIMULATION_CONTRACT.md
  - docs/architecture/ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_CONTRACT.md
  - docs/architecture/GAME-ITEM-01_ITEM_MODEL_AND_EQUIPMENT_CONTRACT.md
  - docs/architecture/DUR-03_ITEM_TRANSACTION_AND_ANTI_DUPLICATION_CONTRACT.md
blocks:
  - safe continuation of GAME-ABILITY-01 targeting, legality, timing, cost, cooldown and condition decisions
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Record the owner-accepted first bounded `GAME-ABILITY-01` subdecision: Oteryn abilities are data-first semantic definitions resolved through a typed, deterministic, server-authoritative effect pipeline; DUR-04 Wasm/WIT may extend mechanics only through bounded proposal interfaces and cannot directly mutate authoritative gameplay state.

This task does **not** accept or close the whole `GAME-ABILITY-01` gate.

## Architecture and source of truth

- **PROVEN:** `GAME-ABILITY-01` is already registered as `REQUIRED_FOR_ALPHA` in `GAMEPLAY_AND_PRODUCT_ARCHITECTURE_HORIZON.md`; the foundation vertical slice may use a bounded minimal combat contract first.
- **PROVEN:** DUR-04 accepts deterministic, capability-bounded Component Model/WIT scripting with proposal-only mutations and no unbounded direct authority.
- **PROVEN:** SIM-DETERMINISM-01 requires exact semantic revision binding, deterministic arithmetic/RNG/order and reproducible authoritative results.
- **PROVEN:** server authority, item/value conservation and typed event/audit boundaries are already accepted under FND/DUR/ANL contracts.
- **PROVEN:** on 2026-08-13 the repository owner explicitly accepted the proposed `data-first + typed effects + bounded Wasm extension` foundation for `GAME-ABILITY-01`.
- **UNKNOWN:** targeting semantics, legality partitioning, cast timing, interruption, costs, cooldowns, charges, condition lifecycle, exhaustive effect families, exact Reference formulas and physical authoring format remain undecided.

## Acceptance criteria

- [ ] Add one canonical owner baseline under `docs/architecture/` recording only the accepted typed-effect pipeline subdecision.
- [ ] Preserve `GAME-ABILITY-01` overall status as still open/`REQUIRED_FOR_ALPHA`; do not claim full gate acceptance.
- [ ] Define the semantic stages and authority boundary without selecting a physical serializer, Rust implementation type graph or runtime library.
- [ ] Make Wasm/WIT extension proposal-only and incapable of bypassing authoritative validation, conservation, fencing, determinism or resource limits.
- [ ] Preserve exact revision/provenance requirements from DUR-04 and SIM-DETERMINISM-01.
- [ ] State the mandatory architecture decision test and explicit supersession evidence.
- [ ] Keep runtime/client/protocol/DDL/Platform/production implementation unauthorized.
- [ ] Inspect the complete changed-file diff and obtain exact-head documentation/governance validation before merge.

## Excluded scope

No Rust gameplay implementation, protocol messages, database schema/migration, content serializer, editor UI, spell catalogue, Reference formula claims, target-selection rules, cooldown/cast-time values, Wasmtime version/function inventory, broad content import, Platform write, production behavior or external-repository mutation.

## Implementation / findings

The accepted subdecision is intentionally semantic and data-model-neutral. It establishes where authority lives and how extensibility is bounded so later targeting/timing/condition decisions cannot accidentally create a second mutation engine inside content scripts.

## Validation

### Focused

- command/run: inspect exact changed-file diff for owner-accepted scope, cross-contract consistency and unsupported claims
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture-only documentation; no executable component changes
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no runtime or player-visible executable behavior changes
- result: `NOT_APPLICABLE`

### Exact-head CI

- final head: pending
- trigger source: pull request
- workflow/run/job: pending
- runner assignment: pending
- classification: documentation/governance
- result: pending

## Self-review

- exact head: pending
- method/reviewer: implementing/coordinating agent
- material findings: pending
- verdict: pending

## Independent review

- required: `NO` unless self-review discovers material uncertainty; bounded paper-only subdecision with no security/protocol/persistence/production authority change
- exact head: `NOT_APPLICABLE`
- method/auditor: `NOT_APPLICABLE`
- material findings: `NOT_APPLICABLE`
- verdict: `NOT_APPLICABLE`

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: #162 governance-only and #191 GAME-CHAR provenance are non-overlapping
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Owner accepted data-first typed-effect pipeline with bounded Wasm extension as the first GAME-ABILITY-01 subdecision; bounded architecture task and issue #222 created from main@5518a562.
status: implementing
branch: docs/game-ability-typed-effects-222
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
owner_action_required: false
blocker: null
next_action: Add the canonical GAME-ABILITY-01 typed-effect pipeline owner baseline and open the bounded documentation PR.
```
