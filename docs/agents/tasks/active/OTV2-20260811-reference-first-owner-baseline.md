# OTV2-20260811-reference-first-owner-baseline

```yaml
task_id: OTV2-20260811-reference-first-owner-baseline
title: Persist GAME-VISION-01 Reference-first owner baseline
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260811-reference-first-owner-baseline
pr: null
base_sha: ae5b6ff9feeb2a608583cd34e16675a1f4639299
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-11T09:31:00+02:00
updated_at: 2026-08-11T09:31:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260811-reference-first-owner-baseline.md
  - docs/architecture/GAME-VISION-01_REFERENCE_FIRST_OWNER_BASELINE.md
public_contracts:
  - docs/architecture/GAME-VISION-01_REFERENCE_FIRST_OWNER_BASELINE.md
depends_on:
  - ADR-0010-reference-and-evolved-world-product-profiles.md
  - PRODUCT_DIRECTION_BASELINE.md
  - GAME-VISION-01_PREDECISION_ANALYSIS.md
  - GAME-VISION-01_PREDECISION_ECONOMY_SCARCITY_ADDENDUM.md
blocks: []
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Persist the owner's current-session acceptance that the first externally evaluated Oteryn build is **Reference-first**. Record only the accepted launch/evaluation ordering and its direct implications; do not silently accept the remaining `GAME-VISION-01` product packet.

## Architecture and source of truth

- `USER_SOURCE`: on 2026-08-11 the owner explicitly answered `tak` to the proposed `Reference-first` direction for the first externally evaluated Oteryn build.
- `PROVEN`: ADR-0010 already permits Reference and Evolved product-profile families over one canonical engine/client/`protocol-oteryn` and does not require simultaneous launch.
- `PROVEN`: `GAME-VISION-01_PREDECISION_ANALYSIS.md` recommends Reference-first specifically to reduce ambiguity while the native runtime is not yet proven.
- `DERIVED`: the owner's acceptance resolves launch/evaluation ordering but does not resolve the whole GAME-VISION gate, exact Global Tibia target revision, long-term reference tracking cadence, PvP, solo/party emphasis, economy goals or evolved-system priorities.

## Acceptance criteria

- [ ] Record first externally evaluated build as one Reference profile rather than Evolved-first or simultaneous Reference+Evolved.
- [ ] Record that Evolved follows later from the same engine/client/protocol foundation rather than launching in parallel with the first external build.
- [ ] Preserve one canonical engine/client/`protocol-oteryn`, distinct `WorldId` values and default cross-profile gameplay-value isolation.
- [ ] Require the first external Reference build to name an immutable reference baseline/revision for reproducible claims, without selecting the exact Global Tibia version/date now.
- [ ] Explicitly leave long-term pinned/continuous/hybrid tracking policy unresolved.
- [ ] Explicitly leave the remaining GAME-VISION owner packet unresolved and do not claim full gate acceptance.
- [ ] Include mandatory decision-timing, downstream-consumer, cost-of-delay and supersession-evidence records.
- [ ] No runtime/client/server implementation, content production, public branding or production rollout is authorized.
- [ ] Exact-head self-review and repository-required CI pass before merge.

## Excluded scope

- no exact Global Tibia patch/date selection;
- no long-term Reference update cadence selection;
- no final public naming/branding or `1:1` claim;
- no player-promise/design-pillar acceptance beyond already accepted architecture;
- no first Evolved-system package selection;
- no PvP, solo/party, death/progression or economy/scarcity decision;
- no gameplay/content/runtime implementation.

## Implementation / findings

Pending.

## Validation

### Focused

- owner decision: current-session `USER_SOURCE`, explicit acceptance
- base: `main@ae5b6ff9feeb2a608583cd34e16675a1f4639299`
- open PRs at task start: 0
- changed-file review: pending

### Component/integration

- result: `NOT_APPLICABLE` — product architecture documentation only

### E2E

- result: `NOT_APPLICABLE` — no executable behavior

### Exact-head CI

- final head: pending
- result: pending

## Self-review

- exact head: pending
- method/reviewer: implementing/coordinating agent full-diff product/architecture review
- material findings: pending
- verdict: pending

## Independent review

- required: `NO` under current risk policy — this is a product launch-order decision and changes no authentication/session, protocol/wire, persistence/economy conservation, security, production or multichannel-authority semantics.
- exact head: `NOT_APPLICABLE`
- method/auditor: `NOT_APPLICABLE`
- material findings: `NOT_APPLICABLE`
- verdict: `NOT_APPLICABLE`

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Owner explicitly accepted Reference-first for the first externally evaluated Oteryn build; bounded task created to persist that partial GAME-VISION decision.
status: implementing
branch: docs/OTV2-20260811-reference-first-owner-baseline
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
next_action: Write the narrow Reference-first owner baseline without accepting the remaining GAME-VISION-01 decisions.
```
