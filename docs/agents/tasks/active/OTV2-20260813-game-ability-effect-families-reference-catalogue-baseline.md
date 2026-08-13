# OTV2-20260813-game-ability-effect-families-reference-catalogue-baseline

```yaml
task_id: OTV2-20260813-game-ability-effect-families-reference-catalogue-baseline
title: Record GAME-ABILITY-01 effect-family and Reference mechanic catalogue boundary
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/game-ability-effect-families-reference-catalogue-baseline
pr: null
base_sha: 463ee694edb5edc156e801e456a9c6298482b485
owner: ChatGPT architecture coordinator
created_at: 2026-08-13T20:28:00+02:00
updated_at: 2026-08-13T20:28:00+02:00
execution_budget_minutes: 60
owned_paths:
  - docs/agents/tasks/active/OTV2-20260813-game-ability-effect-families-reference-catalogue-baseline.md
  - docs/architecture/GAME-ABILITY-01_EFFECT_FAMILIES_REFERENCE_CATALOGUE_OWNER_BASELINE.md
public_contracts:
  - docs/architecture/GAME-ABILITY-01_EFFECT_FAMILIES_REFERENCE_CATALOGUE_OWNER_BASELINE.md
depends_on:
  - docs/architecture/GAME-ABILITY-01_TYPED_EFFECT_PIPELINE_OWNER_BASELINE.md
  - docs/architecture/GAME-ABILITY-01_TARGETING_AND_LEGALITY_BOUNDARY_OWNER_BASELINE.md
  - docs/architecture/GAME-ABILITY-01_CAST_CHANNEL_COMMIT_OWNER_BASELINE.md
  - docs/architecture/GAME-ABILITY-01_COOLDOWN_CHARGE_CONDITION_OWNER_BASELINE.md
  - docs/architecture/GAME-ABILITY-01_EFFECT_COMPOSITION_DAMAGE_HEAL_OWNER_BASELINE.md
  - docs/architecture/GAME-ITEM-01_ITEM_MODEL_AND_EQUIPMENT_CONTRACT.md
  - docs/architecture/DUR-03_ITEM_TRANSACTION_AND_ANTI_DUPLICATION_CONTRACT.md
  - docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md
  - docs/architecture/SIM-DETERMINISM-01_AUTHORITATIVE_SIMULATION_CONTRACT.md
  - docs/architecture/ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_CONTRACT.md
  - docs/architecture/REFERENCE_EVIDENCE_PARITY_MANIFEST_CONTRACT.md
blocks:
  - safe construction of the Reference ability/combat mechanic catalogue and later representative parity fixtures
external_repositories: []
```

## Outcome

Record the owner-accepted sixth bounded `GAME-ABILITY-01` subdecision: a small stable typed effect-family vocabulary is distinct from concrete Reference mechanics; cross-domain effects remain subordinate to their owning domains; and the Reference Mechanic Catalogue is an evidence-linked declarative index/composition layer rather than runtime code, protocol vocabulary or a second mutation engine.

Overall `GAME-ABILITY-01` remains open / `REQUIRED_FOR_ALPHA`.

## Acceptance criteria

- [ ] Add one canonical owner baseline separating effect families, domain-owned transitions and concrete Reference mechanic catalogue entries.
- [ ] Freeze the separation/selection criteria without freezing an exhaustive effect enum, Rust type graph or physical serializer.
- [ ] Keep item/currency/loot/durable-value effects subordinate to `GAME-ITEM` / `DUR-03`.
- [ ] Keep movement/spatial, entity lifecycle, AI/threat and world/tile interactions under their respective domain owners; ability may propose/initiate but not take mutation ownership.
- [ ] Prevent generic state-patch/event-bus or per-mechanic hardcoded effect families from becoming alternate mutation engines.
- [ ] Require new core effect families to satisfy explicit reuse/invariant/boundedness/ownership/testability criteria; prefer composition or bounded Wasm for exceptional mechanics.
- [ ] Define the Reference Mechanic Catalogue as stable mechanic identity + evidence references + behavior-affecting revision bindings + parity/unknown state, not executable truth.
- [ ] Make evidence-manifest `UNKNOWN`/`CONFLICT`/empty cases fail closed; catalogue presence must never imply Reference parity.
- [ ] Record realistic options, trade-offs, risks, player/producer/operations impact and the mandatory architecture decision test.
- [ ] Keep exact formulas, exact catalogue population, exact effect taxonomy, AI/world/item domain internals, runtime, protocol, DDL, Platform and production out of scope.
- [ ] Complete exact-head full-diff self-review, review classification, zero unresolved threads and the aggregate `Merge gate / validate` before merge.

## Excluded scope

No Rust runtime implementation, exhaustive effect enum, Reference spell/mechanic population, physical catalogue schema/serializer, formula values, movement/world/AI/item implementation, protocol/client UX, database migration, Platform write, production behavior or external-repository mutation.

## Open PR classification

PR #191 remains a non-overlapping stale-base GAME-CHAR provenance correction and is classified `REBASE/FIX`; it is not merged, closed or absorbed by this task.

## Review classification

Independent review defaults to `NOT_REQUIRED` only if final scope remains bounded paper-only and no AGENTS.md mandatory trigger, unusual unresolved complexity or material uncertainty appears. Cross-domain references explicitly do not transfer durable/security/multichannel ownership into GAME-ABILITY. Owner-funded Codex/OpenAI use is not authorized.

## Context checkpoint

```yaml
status: implementing
branch: docs/game-ability-effect-families-reference-catalogue-baseline
pr: null
owner_action_required: false
blocker: null
next_action: Open a draft PR, add the canonical owner baseline, inspect the exact full diff and repair any boundary ambiguity before final-head freeze.
```
