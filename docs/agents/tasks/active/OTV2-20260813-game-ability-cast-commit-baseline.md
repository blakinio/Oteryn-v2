# OTV2-20260813-game-ability-cast-commit-baseline

```yaml
task_id: OTV2-20260813-game-ability-cast-commit-baseline
title: Record GAME-ABILITY-01 cast/channel/interruption and commit-point baseline
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/game-ability-cast-commit-baseline
pr: null
base_sha: b4ea6d26ee8e783c4ce26a03655904e5f7786bb6
owner: ChatGPT architecture coordinator
created_at: 2026-08-13T18:22:00+02:00
updated_at: 2026-08-13T18:22:00+02:00
execution_budget_minutes: 60
owned_paths:
  - docs/agents/tasks/active/OTV2-20260813-game-ability-cast-commit-baseline.md
  - docs/architecture/GAME-ABILITY-01_CAST_CHANNEL_COMMIT_OWNER_BASELINE.md
public_contracts:
  - docs/architecture/GAME-ABILITY-01_CAST_CHANNEL_COMMIT_OWNER_BASELINE.md
depends_on:
  - docs/architecture/GAME-ABILITY-01_TYPED_EFFECT_PIPELINE_OWNER_BASELINE.md
  - docs/architecture/GAME-ABILITY-01_TARGETING_AND_LEGALITY_BOUNDARY_OWNER_BASELINE.md
  - docs/architecture/FND-03_RUNTIME_EXECUTION_CONTRACT.md
  - docs/architecture/SIM-DETERMINISM-01_AUTHORITATIVE_SIMULATION_CONTRACT.md
  - docs/architecture/DUR-03_ITEM_TRANSACTION_AND_ANTI_DUPLICATION_CONTRACT.md
  - docs/architecture/ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_CONTRACT.md
blocks:
  - safe continuation of GAME-ABILITY-01 cooldown/charge, condition lifecycle and effect-composition decisions
external_repositories: []
```

## Outcome

Record the owner-accepted third bounded `GAME-ABILITY-01` subdecision: explicit authoritative ability lifecycle, explicit logical commit point, and versioned anchor policies for costs/cooldowns/charges. Overall `GAME-ABILITY-01` remains open / `REQUIRED_FOR_ALPHA`.

## Source of truth

- **PROVEN:** prior GAME-ABILITY baselines establish one authoritative typed-effect pipeline and deterministic target/legality boundary.
- **PROVEN:** FND-03/SIM require deterministic authoritative ordering; client or thread timing cannot decide interrupt-versus-commit races.
- **PROVEN:** DUR-03 conservation/idempotency prevents hidden rollback from bypassing item/value ownership.
- **PROVEN:** owner accepted this lifecycle/commit model on 2026-08-13.
- **UNKNOWN:** exact cast/GCD/cooldown/cost values, Reference timing rules, target revalidation timing and crash/logout/reconnect behavior remain later decisions.

## Acceptance criteria

- [ ] Add the canonical lifecycle/commit owner baseline.
- [ ] Define optional casting/channel phases and explicit terminal states without freezing scheduler implementation.
- [ ] Define `COMMIT` as a logical authoritative boundary, not a physical database or CPU transaction.
- [ ] Require costs/cooldowns/charges to use explicit versioned anchor policies; no single global anchor is frozen.
- [ ] Allow only explicit resource reservation; pre-commit interruption releases only explicit reservations.
- [ ] Require post-commit reversal to be a new explicit compensation, never history erasure.
- [ ] Model channel ticks/pulses as bounded deterministic authoritative occurrences, not an unbounded script loop.
- [ ] Resolve interrupt/commit races by authoritative ordering with replay evidence.
- [ ] Preserve targeting, fencing/ownership, conservation and audit/event boundaries.
- [ ] Keep exact values/formulas, protocol/client UX, DDL/runtime/production implementation out of scope.
- [ ] Complete full-diff self-review and exact-head documentation/governance CI before merge.

## Excluded scope

No Rust gameplay runtime, scheduler, protocol schema, database migration, numeric cast/GCD/cooldown/cost/refund rules, Reference spell timing claims, client animation/UI, Platform write, production behavior or external-repository mutation.

## Implementation / findings

Open PRs #162 and #191 are non-overlapping and remain untouched. #162 has separate exhausted repair authority and is not authorized for repair by this task.

## Validation

Focused: full PR diff against prior GAME-ABILITY, FND-03, SIM, DUR-03 and ANL-01 boundaries — pending.

Component/integration/E2E: `NOT_APPLICABLE` — architecture-only documentation.

Exact-head CI: pending.

Self-review: pending.

Independent review: `NO` unless material uncertainty appears; bounded paper-only partial baseline.

## Context checkpoint

```yaml
status: implementing
branch: docs/game-ability-cast-commit-baseline
pr: null
owner_action_required: false
blocker: null
next_action: Add canonical cast/channel/commit baseline, open draft PR and inspect the full diff.
```
