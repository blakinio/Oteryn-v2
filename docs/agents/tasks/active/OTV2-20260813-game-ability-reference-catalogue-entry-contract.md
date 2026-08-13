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
head_sha: 794779edd663ee54ac6384593d7b08f523f2017b
final_head_sha: null
final_head_frozen_at: null
owner: architecture continuation agent
created_at: 2026-08-13T22:48:00+02:00
updated_at: 2026-08-13T23:57:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260813-game-ability-reference-catalogue-entry-contract.md
  - docs/architecture/GAME-ABILITY-01_REFERENCE_MECHANIC_CATALOGUE_ENTRY_PARITY_FIXTURE_CONTRACT.md
  - docs/agents/tasks/archive/OTV2-20260813-game-ability-reference-catalogue-parity-fixture-contract.md
public_contracts:
  - docs/architecture/GAME-ABILITY-01_REFERENCE_MECHANIC_CATALOGUE_ENTRY_PARITY_FIXTURE_CONTRACT.md
depends_on:
  - accepted GAME-ABILITY-01 partial baselines
  - current candidate Reference evidence/parity manifest contract and schema
blocks: []
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Define the paper-only catalogue-entry and parity-fixture binding boundary without executable authority.

## Acceptance criteria

- [x] catalogue-local identity is not runtime/protocol identity
- [x] evidence, implementation and parity remain separate
- [x] parity is case/scenario scoped; aggregate confirmation requires complete declared coverage
- [x] exact behavior-affecting revision bindings are required
- [x] owning-domain boundaries and durable-value conservation are preserved
- [x] missing/conflicting/uncovered evidence fails closed
- [x] non-factual example is explicit
- [x] consumed handoff is archived and no longer a second active ownership source
- [x] no runtime, DDL, Platform, production or external-repository change

## Findings and repairs

1. Self-review: the initial draft treated the candidate evidence-manifest design too strongly. Repaired by preserving candidate status and requiring a future accepted pinned manifest/schema before parity confirmation.
2. PR review: one passing fixture could over-promote a whole mechanic. Repaired with case/scenario coverage and complete-coverage requirements for any aggregate confirmation.
3. PR review: the PR #248 handoff remained a second `UNCLAIMED` active source. Repaired by consuming and archiving it; PR #249 is the sole active execution source.
4. Final self-review: the decision analysis did not state the downstream blocker and deferment cost explicitly enough. Repaired by adding `Blocked without it`, `Harder later` and explicit trade-off/risk language.

## Validation

- Focused/full-diff semantic review at content head `794779edd663ee54ac6384593d7b08f523f2017b`: PASS, no open material finding after four repairs.
- Component/integration: NOT_APPLICABLE — paper-only architecture.
- E2E: NOT_APPLICABLE — no executable behavior.
- Prior exact-head CI is invalidated by repairs; the checkpoint commit created by this file update requires a fresh exact-head generation.

## Self-review

- reviewed content head: `794779edd663ee54ac6384593d7b08f523f2017b`
- method/reviewer: implementing/coordinating architecture continuation agent
- material findings: 4 total across self-review and PR review; all repaired
- verdict: PASS for semantic/content diff; final checkpoint-only diff recheck required on resulting head

## Independent review

- required: NO — bounded paper-only contract with no security, protocol, durable mutation, production or safety-gate change
- automated PR review produced two material findings; it is not relied on as a required independent-review gate

## PR and closeout

- PR: #249
- changed-file review at content head: PASS
- unresolved review threads: 0
- current main ancestry: PASS at `main@93f2ada35ef55ff53cf9e10f67fbc718ca773f67`
- exact-head merge gate: fresh generation required after this checkpoint commit
- merge/ownership release: pending

## Context checkpoint

```yaml
last_progress: Full semantic diff rechecked PASS after four repairs; both material PR review threads resolved and consumed handoff archived.
status: validating
branch: arch/game-ability-reference-catalogue-entry-contract
head_sha: 794779edd663ee54ac6384593d7b08f523f2017b
pr: 249
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: pull_request
ci_check_generation: fresh checkpoint head required
ci_checks_for_current_head: 0
ci_run_ids: []
ci_job_ids: []
runner_assignment_state: unknown
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 3
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: false
blocker: null
next_action: Inspect fresh exact-head CI for the checkpoint head and merge PR #249 only if every required gate passes unchanged.
```
