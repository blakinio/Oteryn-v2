# OTV2-20260811-evolved-reliability-ux-owner-baseline

```yaml
task_id: OTV2-20260811-evolved-reliability-ux-owner-baseline
title: Persist GAME-VISION-01 Evolved reliability/UX-first owner baseline
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260811-evolved-reliability-ux-owner-baseline
pr: null
base_sha: f184930fac66fdf9ae0cc7f606d3502c17626a79
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-11T10:59:00+02:00
updated_at: 2026-08-11T10:59:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260811-evolved-reliability-ux-owner-baseline.md
  - docs/architecture/GAME-VISION-01_EVOLVED_RELIABILITY_UX_FIRST_OWNER_BASELINE.md
public_contracts:
  - docs/architecture/GAME-VISION-01_EVOLVED_RELIABILITY_UX_FIRST_OWNER_BASELINE.md
depends_on:
  - GAME-VISION-01_PLAYER_PROMISE_OWNER_BASELINE.md
  - GAME-VISION-01_REFERENCE_FIRST_OWNER_BASELINE.md
  - GAME-VISION-01_REFERENCE_HYBRID_TRACKING_OWNER_BASELINE.md
  - GAME-VISION-01_PREDECISION_ANALYSIS.md
  - ADR-0010-reference-and-evolved-world-product-profiles.md
blocks: []
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Persist the owner's explicit acceptance that the **first Evolved differentiation strategy is reliability/UX-first**: Oteryn should first improve player-visible trust, usability, recovery and clarity while avoiding an initial broad redesign of combat power, progression, death, PvP, boss rewards or economy.

## Architecture and source of truth

- `USER_SOURCE`: on 2026-08-11, after the recommendation was stated as “first Evolved difference = reliability/UX-first; better client, reconnect, messages, interface, convenience and technical quality before balance/death/economy/core progression”, the owner answered `tak`.
- `PROVEN`: `GAME-VISION-01_PLAYER_PROMISE_OWNER_BASELINE.md` requires modern reliable native quality and explicit/versioned/measurable intentional Oteryn differences.
- `PROVEN`: `GAME-VISION-01_REFERENCE_FIRST_OWNER_BASELINE.md` makes the first external evaluation Reference-first rather than Evolved-first.
- `PROVEN`: `GAME-VISION-01_REFERENCE_HYBRID_TRACKING_OWNER_BASELINE.md` preserves immutable released Reference revisions and explicit promotion.
- `PROVEN`: `GAME-VISION-01_PREDECISION_ANALYSIS.md` defines reliability/UX-first as Strategy 1 and contrasts it with immediate systemic gameplay redesign and a broad feature pack.
- `PROVEN`: ADR-0010 keeps Reference and Evolved on one canonical engine/client/`protocol-oteryn` and requires Evolved differences to be explicit and reviewable.
- `DERIVED`: this decision selects the ordering/character of the first Evolved package, not its exact feature list. Semantically neutral reliability/UX improvements that preserve Reference gameplay should not be artificially withheld from Reference merely to manufacture Evolved differentiation.

## Acceptance criteria

- [ ] Record reliability/UX-first as the owner-accepted first Evolved strategy.
- [ ] State that the first Evolved package should minimize gameplay-power/economy disturbance while improving trust, usability, recovery and clarity.
- [ ] Preserve server authority, persistence/value integrity, Reference parity and one shared engine/client/protocol foundation.
- [ ] Make clear that shared semantic-neutral reliability/UX improvements may benefit Reference too and need not be Evolved-exclusive.
- [ ] Keep exact feature inventory, UI design, numeric KPIs and rollout mechanics unresolved.
- [ ] Keep death/progression/PvP/economy/boss-loot/systemic redesign out of the first package unless separately owner-accepted.
- [ ] Keep full `GAME-VISION-01` explicitly `NOT ACCEPTED`.
- [ ] Include decision-timing, downstream-consumer, cost-of-delay and supersession-evidence records.
- [ ] No runtime/client/server/content/production implementation is authorized.
- [ ] Exact-head self-review and repository-required CI pass before merge.

## Excluded scope

This task must not:

- implement any client, server, protocol, persistence, content, deployment or production change;
- freeze an exact Evolved feature list or UI mockup;
- select exact reconnect timers, grace periods, channel-switch mechanics or recovery algorithms;
- redesign or accept death penalty, progression rates, PvP rules, vocation balance, boss rewards, spawn economics or economy formulas;
- claim that every reliability/UX improvement is Evolved-only;
- alter the Reference-first or hybrid Reference tracking baselines;
- finalize public branding, monetization, KPI targets or LiveOps cadence;
- modify the parallel PR #162 merge-gate/governance owned paths.

## Implementation / findings

- Current main at task start: `f184930fac66fdf9ae0cc7f606d3502c17626a79`.
- Open PR at task start: #162 (`ci: enforce aggregate pull request merge gate`). Its changed paths are repository engineering/governance files plus `docs/agents/tasks/active/OTV2-20260811-merge-gate-hardening.md`; no overlap exists with this task's two owned paths.
- This task therefore proceeds as a disjoint documentation change while preserving #162 ownership.
- The owner acceptance resolves only owner-decision packet item 5 from `GAME-VISION-01_PREDECISION_ANALYSIS.md`.

## Validation

### Focused

- command/run: compare owner wording with `GAME-VISION-01_PREDECISION_ANALYSIS.md`, `GAME-VISION-01_PLAYER_PROMISE_OWNER_BASELINE.md`, accepted Reference baselines and ADR-0010; inspect parallel PR #162 changed paths for ownership collision
- result: pending final document and exact-head review

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture/task documentation only; no executable component/integration behavior changes
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no runtime/client/server/content behavior changes
- result: `NOT_APPLICABLE`

### Exact-head CI

- final head: pending
- trigger source: pending PR creation/synchronize
- workflow/run/job: pending
- runner assignment: pending
- classification: repository-required documentation checks applicable to exact PR head
- result: pending

## Audit

- scope: owner-authority fidelity, accidental gameplay-policy freeze, accidental Reference degradation, shared-stack/profile-boundary conflict, task-template completeness, parallel ownership collision
- material findings: pending
- unresolved findings: pending
- verdict: pending

## Self-review

- exact head: pending
- method/reviewer: implementing/coordinating agent full-diff product/architecture/governance review
- material findings: pending
- verdict: pending

## Independent review

- required: `NO` under current risk policy — bounded product-definition documentation only; no authentication/session, protocol/wire, durable-data/economy conservation, security, production or multichannel-authority semantics are changed
- exact head: `NOT_APPLICABLE`
- method/auditor: `NOT_APPLICABLE`
- material findings: `NOT_APPLICABLE`
- verdict: `NOT_APPLICABLE`

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: parallel disjoint PR #162; no supersession
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending lifecycle archive after merge

## Context checkpoint

```yaml
last_progress: Owner accepted reliability/UX-first as the first Evolved differentiation strategy; verified parallel PR #162 owns disjoint repository-engineering paths and created a dedicated branch/task.
status: implementing
branch: docs/OTV2-20260811-evolved-reliability-ux-owner-baseline
head_sha: null
pr: null
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: null
ci_check_generation: pre-pr
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
next_action: Add the narrow owner baseline, then open and validate a PR without touching #162-owned paths.
```
