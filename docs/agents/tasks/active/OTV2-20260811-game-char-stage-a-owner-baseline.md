# OTV2-20260811-game-char-stage-a-owner-baseline

```yaml
task_id: OTV2-20260811-game-char-stage-a-owner-baseline
title: Persist owner-accepted GAME-CHAR-01 Stage A partial baseline
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260811-game-char-stage-a-owner-baseline
pr: null
base_sha: 55e576b4d6d5c51ca2531538e29acb2a0e6a1a3d
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-11T18:28:00+02:00
updated_at: 2026-08-11T18:28:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260811-game-char-stage-a-owner-baseline.md
  - docs/architecture/GAME-CHAR-01_STAGE_A_OWNER_BASELINE.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
  - docs/architecture/GAMEPLAY_AND_PRODUCT_ARCHITECTURE_HORIZON.md
public_contracts:
  - docs/architecture/GAME-CHAR-01_STAGE_A_OWNER_BASELINE.md
depends_on:
  - docs/architecture/GAME-CHAR-01_PREDECISION_ANALYSIS.md
  - docs/architecture/GAME-VISION-01_MINIMUM_OWNER_BASELINE.md
  - docs/architecture/ADR-0012-character-authority-and-platform-lifecycle-boundary.md
  - docs/contracts/CHARACTER_AUTHORITY_PLATFORM_BOUNDARY.md
  - docs/architecture/FND-ID-01_CHARACTER_ID_ACCOUNT_LINK_OWNER_BASELINE.md
  - docs/architecture/FND-ID-01_ACCOUNT_SINGLE_ONLINE_CHARACTER_OWNER_BASELINE.md
  - docs/architecture/FND-04_IDENTITY_GAME_SESSION_ADMISSION_CHARACTER_LEASE_CONTRACT.md
  - docs/architecture/DUR-01_DURABLE_IDENTIFIER_REPRESENTATION_CONTRACT.md
blocks:
  - canonical recording of owner-accepted Stage A scope
  - Stage B decision dossier on the exact first Reference baseline
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Persist the product owner's explicit acceptance of the complete recommended baseline-neutral `GAME-CHAR-01` Stage A package from section 22 of `GAME-CHAR-01_PREDECISION_ANALYSIS.md`, while preserving the overall gate as not fully accepted until Reference-sensitive Stage B is resolved.

## Source of truth

- `PROVEN`: trusted base is `main@55e576b4d6d5c51ca2531538e29acb2a0e6a1a3d`.
- `USER_SOURCE`: on 2026-08-11 at 18:28 +02:00 the product owner explicitly answered `tak` to acceptance of the complete recommended GAME-CHAR Stage A package.
- `PROVEN`: `ARCHITECTURE_STATUS_MODEL.md` has no partial DecisionStatus; therefore Stage A is recorded as an owner-accepted partial baseline while the overall `GAME-CHAR-01` gate remains `PROPOSED / PLANNED / NOT_STARTED` after lifecycle closeout.
- `PROVEN`: exact first Global Tibia Reference baseline remains a hard prerequisite for Reference-sensitive Stage B semantics.
- `PROVEN`: open PR #162 owns disjoint CI/repository-governance paths and is out of scope.

## Acceptance criteria

- [ ] Add a canonical `GAME-CHAR-01_STAGE_A_OWNER_BASELINE.md` recording all fourteen accepted Stage-A decisions and their exact boundary.
- [ ] Keep overall `GAME-CHAR-01` formally `PROPOSED / PLANNED / NOT_STARTED`; do not invent a `PARTIAL` DecisionStatus.
- [ ] Update current status/register/horizon to identify Stage A as binding input and Stage B as hard-blocked on the exact first Reference baseline.
- [ ] Preserve Character Authority, FND-ID, FND-04, DUR-01, GAME-ITEM/DUR-03 and GAME-VISION ownership boundaries.
- [ ] Do not select the Reference baseline, formulas, physical schema, runtime APIs, content or production behavior.
- [ ] Preserve bounded DUR-02 discovery only; final character-bearing DUR-02 schema remains blocked on full GAME-CHAR acceptance.
- [ ] Keep PR #162 and external repositories untouched.
- [ ] Perform full exact-head self-review and all repository-required documentation CI before merge.

## Excluded scope

This task does not:

- accept Stage B or the complete GAME-CHAR gate;
- select any Global Tibia patch/date/behavior target;
- choose exact XP/skill/stat/death/vocation/name/quota/offline-training rules;
- create PostgreSQL DDL, migrations, indexes, locks or transaction implementations;
- implement runtime/client/protocol/content/Platform behavior;
- authorize live world/account transfer or any product launch capability;
- modify governance/CI or PR #162;
- modify external repositories.

## Validation

### Focused

Reconcile owner acceptance against `GAME-CHAR-01_PREDECISION_ANALYSIS.md`, accepted GAME-VISION, Character Authority/FND-ID/FND-04 boundaries, DUR-01 and `ARCHITECTURE_STATUS_MODEL.md`.

### Component/integration

`NOT_APPLICABLE` — paper-only architecture owner baseline and coordination updates.

### E2E

`NOT_APPLICABLE` — no executable or player-visible runtime behavior changes.

### Exact-head CI

Pending final immutable PR head.

## Self-review

Pending final immutable PR head.

## Independent review

- required: `NO` unless final diff introduces an accepted high-risk security/protocol/persistence/production authority change; intended scope is paper-only product architecture semantics already explicitly owner-approved.

## Context checkpoint

```yaml
last_progress: Owner explicitly accepted the complete GAME-CHAR Stage A recommendation; dedicated branch claimed from current main and task ownership recorded.
status: implementing
branch: docs/OTV2-20260811-game-char-stage-a-owner-baseline
head_sha: null
pr: null
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: null
ci_check_generation: null
ci_checks_for_current_head: 0
ci_run_ids: []
runner_assignment_state: unknown
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 0
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: null
blocker: null
next_action: Persist Stage A owner baseline and synchronize current status/register/horizon without closing the overall GAME-CHAR gate.
```
