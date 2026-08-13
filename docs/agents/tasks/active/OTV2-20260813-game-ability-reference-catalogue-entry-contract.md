# OTV2-20260813-game-ability-reference-catalogue-entry-contract

```yaml
task_id: OTV2-20260813-game-ability-reference-catalogue-entry-contract
title: Define Reference Mechanic Catalogue entry and parity-fixture binding contract
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: arch/game-ability-reference-catalogue-entry-contract
pr: 249
base_sha: 93f2ada35ef55ff53cf9e10f67fbc718ca773f67
head_sha: 07759c0d32bb7cd83f0b122213a923530fc563a8
final_head_sha: null
final_head_frozen_at: null
owner: architecture continuation agent
created_at: 2026-08-13T22:48:00+02:00
updated_at: 2026-08-13T22:59:00+02:00
execution_budget_minutes: 60
owned_paths:
  - docs/agents/tasks/active/OTV2-20260813-game-ability-reference-catalogue-entry-contract.md
  - docs/architecture/GAME-ABILITY-01_REFERENCE_MECHANIC_CATALOGUE_ENTRY_PARITY_FIXTURE_CONTRACT.md
public_contracts:
  - docs/architecture/GAME-ABILITY-01_REFERENCE_MECHANIC_CATALOGUE_ENTRY_PARITY_FIXTURE_CONTRACT.md
depends_on:
  - accepted GAME-ABILITY-01 partial baselines
  - current Reference evidence/parity manifest contract and schema
blocks: []
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Define the paper-only catalogue-entry and parity-fixture binding boundary. No executable authority is granted.

## Acceptance criteria

- [x] catalogue-local identity is not a runtime/protocol identity
- [x] evidence and implementation/parity classification remain separate
- [x] exact behavior-affecting revision bindings are required
- [x] owning-domain boundaries and durable-value conservation are preserved
- [x] missing/conflicting evidence fails closed
- [x] non-factual example is explicit
- [x] no runtime, DDL, Platform, production or external-repository change

## Findings

Full-diff self-review found one material issue: the initial contract treated the evidence-manifest design too strongly even though that manifest contract is still candidate. Commit `07759c0d32bb7cd83f0b122213a923530fc563a8` repaired this by preserving candidate status and requiring a future accepted pinned manifest/schema revision before parity confirmation.

## Validation

- Focused semantic review: PASS after one repair.
- Component/integration: NOT_APPLICABLE, paper-only.
- E2E: NOT_APPLICABLE, no executable behavior.
- Exact-head CI: pending after final checkpoint commit.

## Self-review

- reviewed head: `07759c0d32bb7cd83f0b122213a923530fc563a8`
- material findings: 1 repaired
- verdict: PASS; final checkpoint-only diff recheck pending

## Independent review

- required: NO
- reason: bounded paper-only contract with no security, protocol, durable mutation, production or safety-gate change

## PR and closeout

- PR: #249
- changed-file review: final recheck pending
- unresolved threads: pending
- exact-head merge gate: pending
- merge/ownership release: pending

## Context checkpoint

```yaml
last_progress: Contract drafted and one manifest-status coupling issue repaired.
status: validating
branch: arch/game-ability-reference-catalogue-entry-contract
head_sha: 07759c0d32bb7cd83f0b122213a923530fc563a8
pr: 249
final_head_sha: null
ci_checks_for_current_head: 0
repair_cycles_for_current_gate: 1
owner_action_required: false
blocker: null
next_action: Recheck final diff, mark PR #249 ready, and inspect exact-head required CI.
```
