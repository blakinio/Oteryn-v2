# OTV2-20260813-game-ability-effect-composition-baseline

```yaml
task_id: OTV2-20260813-game-ability-effect-composition-baseline
title: Record GAME-ABILITY-01 effect composition and damage/heal calculation baseline
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/game-ability-effect-composition-baseline
pr: null
base_sha: 2b813f713a70c2be91c4ef7b6f052836a4658d16
owner: ChatGPT architecture coordinator
created_at: 2026-08-13T19:07:00+02:00
updated_at: 2026-08-13T19:07:00+02:00
execution_budget_minutes: 60
owned_paths:
  - docs/agents/tasks/active/OTV2-20260813-game-ability-effect-composition-baseline.md
  - docs/architecture/GAME-ABILITY-01_EFFECT_COMPOSITION_DAMAGE_HEAL_OWNER_BASELINE.md
public_contracts:
  - docs/architecture/GAME-ABILITY-01_EFFECT_COMPOSITION_DAMAGE_HEAL_OWNER_BASELINE.md
depends_on:
  - docs/architecture/GAME-ABILITY-01_TYPED_EFFECT_PIPELINE_OWNER_BASELINE.md
  - docs/architecture/GAME-ABILITY-01_TARGETING_AND_LEGALITY_BOUNDARY_OWNER_BASELINE.md
  - docs/architecture/GAME-ABILITY-01_CAST_CHANNEL_COMMIT_OWNER_BASELINE.md
  - docs/architecture/GAME-ABILITY-01_COOLDOWN_CHARGE_CONDITION_OWNER_BASELINE.md
  - docs/architecture/SIM-DETERMINISM-01_AUTHORITATIVE_SIMULATION_CONTRACT.md
  - docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md
  - docs/architecture/ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_CONTRACT.md
blocks:
  - safe continuation of GAME-ABILITY-01 Reference combat/formula catalogue
external_repositories: []
```

## Outcome

Record the owner-accepted fifth bounded `GAME-ABILITY-01` subdecision: damage/heal use one typed staged deterministic composition framework; damage and healing remain distinct semantics; RNG is explicit/replayable; mutation happens only through the existing Effect Plan/PRIMARY COMMIT; reactive mechanics are bounded descendant occurrences, not recursive mutation.

Overall `GAME-ABILITY-01` remains open / `REQUIRED_FOR_ALPHA`.

## Source of truth

- Prior GAME-ABILITY baselines establish one Effect Plan/commit engine, deterministic targeting/legality, lifecycle/commit anchors and typed condition transitions.
- Current SIM-DETERMINISM defines versioned numeric semantics, explicit rounding/clamp/invalid handling and purpose-isolated retry-stable gameplay RNG.
- DUR-04 keeps content/Wasm proposal-only and bounded.
- Owner accepted this effect-composition direction on 2026-08-13.
- Exact Reference formulas, damage taxonomy, per-mechanic stage order and reaction ordering remain later evidence-driven policy.

## Acceptance criteria

- [ ] Add canonical effect-composition/damage-heal owner baseline.
- [ ] Damage and healing remain distinct typed semantics using shared deterministic composition infrastructure.
- [ ] No arbitrary per-ability/script authoritative formula callback or direct mutation during calculation.
- [ ] Versioned typed contributions with deterministic ordering and explicit numeric/RNG semantics.
- [ ] Mitigation/resistance/absorb stay typed and non-mutating during calculation; state-consuming absorbs emit companion typed plan consequences.
- [ ] Multi-hit/multi-target ordering and snapshot/sequential semantics are explicit and bounded.
- [ ] Reflect/thorns/lifesteal/procs are explicit bounded reactive descendant occurrences with lineage/depth/work budgets.
- [ ] Record realistic alternatives, trade-offs, risks, player/producer impact and mandatory decision test.
- [ ] Exact formulas/values, runtime, protocol, DDL, Platform and production remain out of scope.
- [ ] Complete exact-head self-review, review classification, zero unresolved material threads and Agent Governance/Dependency Review/CodeQL before merge.

## Excluded scope

No Rust combat runtime, physical formula DSL/serializer, exact damage types or Reference formulas, scheduler, protocol/client combat UI, database migration, Platform write, production behavior or external-repository mutation.

## Open PR classification

PR #162 is non-overlapping governance work and its own body states its repair budget is exhausted. PR #191 is non-overlapping stale-base GAME-CHAR provenance work. Neither is modified by this task.

## Review classification

Independent review defaults to `NOT_REQUIRED` only if final scope remains bounded paper-only and self-review finds no mandatory trigger or unusual unresolved complexity. If a trigger appears, merge must stop for genuinely independent exact-head review. Owner-funded Codex/OpenAI review is not authorized.

## Context checkpoint

```yaml
status: implementing
branch: docs/game-ability-effect-composition-baseline
pr: null
owner_action_required: false
blocker: null
next_action: Add canonical baseline, open draft PR, inspect full diff and repair findings before final-head freeze.
```
