# OTV2-20260811-game-vision-channel-decision-dossier

```yaml
task_id: OTV2-20260811-game-vision-channel-decision-dossier
title: Prepare GAME-VISION-01 and GAME-CHANNEL-01 owner decision dossiers
mode: COORDINATE
status: investigating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260811-game-vision-channel-decision-dossier
pr: null
base_sha: c1f115621acd7ba87fc47954f0e8b7d94f63e037
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-11T08:40:00+02:00
updated_at: 2026-08-11T08:40:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260811-game-vision-channel-decision-dossier.md
  - docs/architecture/GAME-VISION-01_PREDECISION_ANALYSIS.md
  - docs/architecture/GAME-CHANNEL-01_PREDECISION_ANALYSIS.md
public_contracts: []
depends_on:
  - ADR-0010-reference-and-evolved-world-product-profiles.md
  - PRODUCT_DIRECTION_BASELINE.md
  - ARCHITECTURE_REVIEW_REFINEMENTS_2026-08-10.md
  - MULTICHANNEL_SYSTEM_SCOPE_MATRIX.md
  - FOUNDATION_PROGRAMME_CURRENT_STATUS.md
blocks: []
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Produce two nonbinding, owner-decision-ready architecture analyses for `GAME-VISION-01` and `GAME-CHANNEL-01`. Each dossier must separate accepted invariants from open product choices, evaluate realistic options, state risks/trade-offs, give an explicit recommendation, identify the exact owner decisions that remain, and avoid converting recommendations into accepted product policy.

## Architecture and source of truth

- `PROVEN`: ADR-0010 accepts Reference and Evolved profile families over one engine/client/`protocol-oteryn`, but does not require simultaneous launch.
- `PROVEN`: `PRODUCT_DIRECTION_BASELINE.md` accepts Global Tibia observable behavior as the initial reference direction while leaving exact parity target, launch sequence and first Oteryn differences unresolved.
- `PROVEN`: `ARCHITECTURE_REVIEW_REFINEMENTS_2026-08-10.md` requires a minimum `GAME-VISION-01` before broad gameplay/content production and a dedicated `GAME-CHANNEL-01` before multichannel becomes a player-facing feature.
- `PROVEN`: `MULTICHANNEL_SYSTEM_SCOPE_MATRIX.md` already freezes system ownership such as channel-local simulation, world-shared market/social state, shared character durability and channel-switch safety gates; this task must not redesign those accepted boundaries.
- `PROVEN`: current `main` is `c1f115621acd7ba87fc47954f0e8b7d94f63e037` and no open Oteryn-v2 PR exists at task start.
- `DERIVED`: the missing work is product-policy selection and measurable launch scope, not another foundation technology choice.

## Acceptance criteria

- [ ] `GAME-VISION-01_PREDECISION_ANALYSIS.md` contains problem, constraints, realistic options, trade-offs, risks, recommendation, future impact and mandatory decision-timing test.
- [ ] Vision analysis gives a recommended launch sequencing and parity-baseline policy without marking it owner-accepted.
- [ ] Vision analysis identifies the minimum owner decisions necessary to unblock `GAME-CHAR-01`, broad gameplay/content work and later alpha milestone design.
- [ ] `GAME-CHANNEL-01_PREDECISION_ANALYSIS.md` separates already accepted system ownership from unresolved player-facing channel policy.
- [ ] Channel analysis covers assignment/co-location, visibility/manual switching, anti-hopping, spawn/resource multiplication, boss/event eligibility, PvP, social fragmentation, recovery and capacity lifecycle.
- [ ] Channel analysis states which decisions block `VSL-MULTICHANNEL-01` versus which can remain deferred while single-channel vertical slices proceed.
- [ ] Relevant external MMO observations are used only as comparative evidence, not copied as policy or implementation.
- [ ] Existing disconnect/forensics active checkpoints are audited for lifecycle relevance; they are changed only if direct evidence proves they are stale and fully superseded.
- [ ] No runtime code, wire schema, persistence schema, production policy or owner-only gameplay rule is implemented or silently accepted.
- [ ] Exact-head self-review and repository-required CI pass before merge.

## Excluded scope

- no owner decision on Reference versus Evolved launch;
- no exact Global Tibia patch/version selection;
- no final death/progression/economy/PvP formulas;
- no final numeric channel capacity thresholds or cooldown values;
- no runtime/client/server implementation;
- no Platform or other external-repository writes;
- no acceptance of GAME-VISION-01 or GAME-CHANNEL-01 through this analysis task.

## Implementation / findings

Pending.

## Validation

### Focused

- source reconciliation: pending
- full changed-file review: pending

### Component/integration

- result: `NOT_APPLICABLE` — architecture analysis only

### E2E

- result: `NOT_APPLICABLE` — no executable behavior

### Exact-head CI

- final head: pending
- result: pending

## Self-review

- exact head: pending
- method/reviewer: implementing/coordinating agent full-diff architecture review
- material findings: pending
- verdict: pending

## Independent review

- required: pending after final risk classification
- exact head: pending or `NOT_APPLICABLE`
- method/auditor: pending or `NOT_APPLICABLE`
- material findings: pending or `NOT_APPLICABLE`
- verdict: pending or `NOT_APPLICABLE`

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: none at task start
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Created bounded pre-decision analysis task after post-closeout main became clean.
status: investigating
branch: docs/OTV2-20260811-game-vision-channel-decision-dossier
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
owner_action_required: null
blocker: null
next_action: Write the two nonbinding decision dossiers from accepted Oteryn invariants and verified comparative evidence.
```
