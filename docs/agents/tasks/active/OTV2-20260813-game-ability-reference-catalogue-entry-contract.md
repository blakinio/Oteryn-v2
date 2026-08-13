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
head_sha: 62b4bb8187273a651f69d6230ad55567f92b7819
final_head_sha: null
owner: architecture continuation agent
execution_budget_minutes: 60
owned_paths:
  - docs/agents/tasks/active/OTV2-20260813-game-ability-reference-catalogue-entry-contract.md
  - docs/architecture/GAME-ABILITY-01_REFERENCE_MECHANIC_CATALOGUE_ENTRY_PARITY_FIXTURE_CONTRACT.md
  - docs/agents/tasks/archive/OTV2-20260813-game-ability-reference-catalogue-parity-fixture-contract.md
public_contracts:
  - docs/architecture/GAME-ABILITY-01_REFERENCE_MECHANIC_CATALOGUE_ENTRY_PARITY_FIXTURE_CONTRACT.md
depends_on:
  - accepted GAME-ABILITY-01 partial baselines
  - current candidate Reference evidence/parity manifest contract and schema
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
2. PR review: one passing fixture could over-promote a whole mechanic. Repaired with explicit case/scenario coverage and complete-coverage requirements for any aggregate confirmation.
3. PR review: the PR #248 handoff remained a second `UNCLAIMED` active source. Repaired by consuming and archiving that handoff; PR #249 is the sole active execution source.

## Validation

- Focused/full-diff review: repaired-head recheck pending.
- Component/integration: NOT_APPLICABLE — paper-only.
- E2E: NOT_APPLICABLE — no executable behavior.
- Exact-head CI: prior head `da3baeb8eeaa9742f98ab196208faf31b4f9879d` passed but is invalidated by repairs; fresh final-head generation required.

## Self-review

- prior reviewed head: `da3baeb8eeaa9742f98ab196208faf31b4f9879d`
- material findings: 3 total; all repaired in later commits
- final exact-head verdict: pending

## Independent review

- required: NO — bounded paper-only contract; no security, protocol, durable mutation, production or safety-gate change
- automated PR review produced two material findings; it is not relied on as a required independent-review gate

## PR and closeout

- PR: #249
- prior review threads: 2 material findings; repair verification pending
- exact-head merge gate: fresh generation required
- merge/ownership release: pending

## Context checkpoint

```yaml
last_progress: Repaired aggregate parity overclaim and duplicate handoff ownership; archived consumed handoff.
status: validating
branch: arch/game-ability-reference-catalogue-entry-contract
head_sha: 62b4bb8187273a651f69d6230ad55567f92b7819
pr: 249
final_head_sha: null
ci_checks_for_current_head: 0
repair_cycles_for_current_gate: 2
owner_action_required: false
blocker: null
next_action: Recheck the repaired PR #249 diff and resolve only review threads whose findings are demonstrably fixed.
```
