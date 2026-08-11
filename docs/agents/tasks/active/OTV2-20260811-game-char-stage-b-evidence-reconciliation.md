# OTV2-20260811-game-char-stage-b-evidence-reconciliation

```yaml
task_id: OTV2-20260811-game-char-stage-b-evidence-reconciliation
title: Reconcile GAME-CHAR-01 Stage B against first Reference target
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260811-game-char-stage-b-evidence-reconciliation
pr: null
base_sha: ef906b3c2d9cbb9cb7a455a94f84068fb6175795
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-11T22:37:00+02:00
updated_at: 2026-08-11T22:37:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260811-game-char-stage-b-evidence-reconciliation.md
  - docs/architecture/GAME-CHAR-01_STAGE_B_REFERENCE_EVIDENCE_RECONCILIATION.md
public_contracts: []
depends_on:
  - docs/architecture/GAME-VISION-01_FIRST_REFERENCE_BASELINE_OWNER_BASELINE.md
  - docs/architecture/GAME-CHAR-01_STAGE_A_OWNER_BASELINE.md
  - docs/architecture/GAME-CHAR-01_PREDECISION_ANALYSIS.md
  - docs/architecture/GAME-VISION-01_REFERENCE_PARITY_PRECEDENCE_OWNER_BASELINE.md
  - docs/architecture/FND-ID-01_CHARACTER_ID_ACCOUNT_LINK_OWNER_BASELINE.md
  - docs/architecture/FND-ID-01_ACCOUNT_SINGLE_ONLINE_CHARACTER_OWNER_BASELINE.md
  - docs/architecture/FND-04_IDENTITY_GAME_SESSION_ADMISSION_CHARACTER_LEASE_CONTRACT.md
  - docs/architecture/DUR-01_DURABLE_IDENTIFIER_REPRESENTATION_CONTRACT.md
blocks:
  - evidence-backed GAME-CHAR-01 Stage-B owner decision package
  - final character-bearing DUR-02 schema semantics
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Produce one nonbinding paper-only Stage-B evidence reconciliation against the owner-accepted 2026-07-28 Reference target. Separate target-proven/derived facts from current-only evidence and unresolved historical continuity, identify which character semantics are safe to freeze now, and fail closed on every `UNKNOWN` or `CONFLICT` rather than guessing.

## Source of truth

- `PROVEN`: trusted base is `main@ef906b3c2d9cbb9cb7a455a94f84068fb6175795`.
- `PROVEN`: the first Reference target is Global Tibia production-observable behavior after the 2026-07-28 server-save/maintenance boundary.
- `PROVEN`: target selection does not imply evidence completeness; accepted evidence states are `PROVEN`, `OBSERVED`, `DERIVED`, `UNKNOWN`, `CONFLICT`, `DECLARED_DIFFERENCE`.
- `PROVEN`: Stage A remains binding for aggregate/lifecycle/revision/migration safety and overall GAME-CHAR remains unaccepted.
- `PROVEN`: current official manuals/FAQ are primary current evidence but cannot automatically prove July-28 historical behavior without continuity evidence.
- `OBSERVED TARGET-ERA PRIMARY`: official Character Bazaar surfaces dated July 28-30 show live character levels, professions/promotions, weapon/magic/shielding skills, blessings and world-transfer state around the selected cut.
- `PROVEN PRE-TARGET PRIMARY`: official 2025 Monk launch material raised the account active-character limit from 20 to 25 before the selected target.
- `PROVEN HISTORICAL + CURRENT PRIMARY`: offline training retains the documented 10-minute start threshold and 12-hour maximum from its 2012 introduction through the current official FAQ; exact advancement formulas remain unspecified.
- `PROVEN HISTORICAL + CURRENT PRIMARY`: the general death-loss model introduced in 2009 and the seven-blessing extension introduced in 2017 are still represented in the current official manual; target-specific sub-rules still require per-claim continuity/evidence review.
- `PROVEN`: open PR #162 remains disjoint CI/repository-governance work and is out of scope.

## Acceptance criteria

- [ ] Reconcile creation inputs/starter-state evidence against the July-28 target.
- [ ] Reconcile name length/character restrictions, uniqueness/reuse/deletion implications and identify normalization/recycling gaps.
- [ ] Reconcile active/deleted character quotas and deletion/undelete timing evidence.
- [ ] Freeze only sufficiently evidenced durable progression vocabulary; distinguish exact formulas from state categories.
- [ ] Reconcile five-vocation/promotion vocabulary and target-era evidence without importing combat/ability details into Character authority.
- [ ] Reconcile death/respawn/experience/skill/blessing/item-loss boundaries and leave item conservation with GAME-ITEM/DUR-03.
- [ ] Reconcile offline-training capability/timing from formula/effectiveness semantics.
- [ ] Identify Wheel/proficiency/Monk/build facts that need durable representation versus later GAME-ABILITY/GAME-ITEM/SIM ownership.
- [ ] Produce an owner-ready Stage-B decision package only for claims with sufficient target evidence; explicitly list evidence blockers for full GAME-CHAR closure.
- [ ] Do not treat current official docs, community pages, Canary/crystalserver or absence of patch notes as automatic July-28 proof.
- [ ] Do not update current status/register/horizon or accept Stage B in this analysis PR.
- [ ] Do not implement runtime, schema, content, protocol or external-repository behavior.
- [ ] Perform full exact-head self-review and repository-required documentation CI before merge.

## Excluded scope

This task does not:

- accept GAME-CHAR Stage B or overall GAME-CHAR;
- decide an intentional Reference difference without owner approval;
- create PostgreSQL DDL/indexes/locking/migrations;
- freeze combat/ability/item formulas owned by later gates;
- use current Global observations as historical proof without continuity evidence;
- write Canary, crystalserver, Platform or other external repositories;
- modify PR #162.

## Validation

### Focused

Reconcile every proposed Stage-B fact against accepted July-28 target/evidence rules and existing Character Authority/FND-ID/FND-04/DUR boundaries.

### Component/integration

`NOT_APPLICABLE` — nonbinding paper-only evidence analysis.

### E2E

`NOT_APPLICABLE` — no executable/player-visible runtime behavior changes.

### Exact-head CI

Pending final immutable PR head.

## Self-review

Pending final immutable PR head.

## Independent review

- required: `NO` unless final diff unexpectedly changes accepted high-risk authority/security/protocol/persistence/production semantics; intended scope is nonbinding evidence analysis only.

## Context checkpoint

```yaml
last_progress: Accepted first Reference target lifecycle is closed and the Stage-B evidence-reconciliation branch is claimed; initial official primary evidence has been gathered for creation/quota, target-era professions/skills, offline training and death/blessings.
status: implementing
branch: docs/OTV2-20260811-game-char-stage-b-evidence-reconciliation
pr: null
final_head_sha: null
ci_check_generation: null
ci_checks_for_current_head: 0
repair_cycles_for_current_gate: 0
owner_action_required: null
blocker: null
next_action: Write the target-evidence matrix, distinguish freeze-ready facts from current-only/unknown historical semantics, and define the next evidence-acquisition or owner-decision boundary.
```
