# OTV2-20260813-game-ability-reference-catalogue-entry-contract

```yaml
task_id: OTV2-20260813-game-ability-reference-catalogue-entry-contract
title: Define Reference Mechanic Catalogue entry and parity-fixture binding contract
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: arch/game-ability-reference-catalogue-entry-contract
pr: null
base_sha: 93f2ada35ef55ff53cf9e10f67fbc718ca773f67
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: architecture continuation agent
created_at: 2026-08-13T22:48:00+02:00
updated_at: 2026-08-13T22:48:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260813-game-ability-reference-catalogue-entry-contract.md
  - docs/architecture/GAME-ABILITY-01_REFERENCE_MECHANIC_CATALOGUE_ENTRY_PARITY_FIXTURE_CONTRACT.md
public_contracts:
  - docs/architecture/GAME-ABILITY-01_REFERENCE_MECHANIC_CATALOGUE_ENTRY_PARITY_FIXTURE_CONTRACT.md
depends_on:
  - docs/architecture/GAME-ABILITY-01_TYPED_EFFECT_PIPELINE_OWNER_BASELINE.md
  - docs/architecture/GAME-ABILITY-01_TARGETING_AND_LEGALITY_BOUNDARY_OWNER_BASELINE.md
  - docs/architecture/GAME-ABILITY-01_CAST_CHANNEL_COMMIT_OWNER_BASELINE.md
  - docs/architecture/GAME-ABILITY-01_COOLDOWN_CHARGE_CONDITION_OWNER_BASELINE.md
  - docs/architecture/GAME-ABILITY-01_EFFECT_COMPOSITION_DAMAGE_HEAL_OWNER_BASELINE.md
  - docs/architecture/GAME-ABILITY-01_EFFECT_FAMILIES_REFERENCE_CATALOGUE_OWNER_BASELINE.md
  - docs/architecture/REFERENCE_EVIDENCE_PARITY_MANIFEST_CONTRACT.md
  - docs/contracts/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1.schema.json
blocks: []
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Define a paper-only semantic contract for one Reference Mechanic Catalogue entry and its parity-fixture bindings so future mechanic cases can be added without collapsing evidence, implementation and parity into one status or inventing runtime authority.

## Architecture and source of truth

- PROVEN: the accepted GAME-ABILITY partial baselines separate concrete mechanics, effect families, domain-owned transitions and the Reference Mechanic Catalogue.
- PROVEN: the current Reference manifest has zero mechanic-level cases and therefore supplies no factual Reference mechanic suitable for promotion in this task.
- PROVEN: the manifest contract keeps target evidence class, Oteryn implementation state and parity status independent and requires fail-closed handling for UNKNOWN and CONFLICT.
- DERIVED: the safest representative deliverable is a normative entry/binding contract plus an explicitly non-factual example shape, not a synthetic Global Tibia mechanic claim.

## Acceptance criteria

- [ ] Define catalogue-local mechanic identity without creating a new global/runtime/protocol identity.
- [ ] Bind evidence-manifest cases and exact behavior-affecting revisions without duplicating or overriding manifest classifications.
- [ ] Define parity-fixture binding requirements and the conditions required before any parity-confirmed claim.
- [ ] Preserve typed Effect Family and owning-domain boundaries, including GAME-ITEM/DUR-03 conservation.
- [ ] Define explicit handling for missing/conflicting evidence and cross-domain atomicity gaps.
- [ ] Include one explicitly non-factual example shape that cannot be mistaken for a Reference behavior claim.
- [ ] Make no runtime/client/protocol/DDL/Platform/production or external-repository change.

## Excluded scope

No factual Global Tibia mechanic population, manifest case mutation, runtime implementation, combat formula/value selection, protocol schema, persistence schema, PostgreSQL DDL, Platform write, production rollout, proprietary asset/code acquisition or external-repository write.

## Implementation / findings

Bounded contract drafting in progress on a dedicated branch from `main@93f2ada35ef55ff53cf9e10f67fbc718ca773f67`.

## Validation

### Focused

- command/run: pending
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — paper-only architecture contract
- result: pending

### E2E

- scenario: `NOT_APPLICABLE` — no executable behavior changes
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
- method/reviewer: architecture continuation agent
- material findings: pending
- verdict: pending

## Independent review

- required: NO — bounded paper-only semantics, no safety gate reduction, runtime authority, durable-value mutation, protocol/security or production change
- exact head: NOT_APPLICABLE
- method/auditor: NOT_APPLICABLE
- material findings: NOT_APPLICABLE
- verdict: NOT_APPLICABLE

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: PR #191 remains separate GAME-CHAR provenance work; Dependabot PRs are unrelated
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Claimed a fresh bounded branch from current main after verifying the handoff checkpoint, GAME-ABILITY baselines and empty mechanic-level manifest state.
status: implementing
branch: arch/game-ability-reference-catalogue-entry-contract
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
next_action: Draft the bounded Reference Mechanic Catalogue entry and parity-fixture binding contract.
```
