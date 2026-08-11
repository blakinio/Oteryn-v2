# OTV2-20260811-channel-selection-owner-baseline

```yaml
task_id: OTV2-20260811-channel-selection-owner-baseline
title: Persist previously accepted channel selection owner baseline
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260811-channel-selection-owner-baseline
pr: null
base_sha: 9a088675c8d9bec4e42036333076e24d4dc4785e
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-11T09:05:00+02:00
updated_at: 2026-08-11T09:05:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260811-channel-selection-owner-baseline.md
  - docs/architecture/GAME-CHANNEL-01_CHANNEL_SELECTION_OWNER_BASELINE.md
public_contracts:
  - docs/architecture/GAME-CHANNEL-01_CHANNEL_SELECTION_OWNER_BASELINE.md
depends_on:
  - GAME-CHANNEL-01 pre-decision dossier merged by PR 152
blocks: []
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Persist a narrow owner-accepted product baseline that was decided in the project conversation on 2026-07-22 but is not present in canonical repository documentation. The baseline must record only the already-decided channel-selection UX and explicitly leave all surrounding channel policy unresolved.

## Architecture and source of truth

- `USER_SOURCE`: on 2026-07-22 the owner accepted one Oteryn login with channels presented at the character/world selection flow rather than as separate login servers.
- `USER_SOURCE`: the same accepted concept uses an automatic/recommended channel path while retaining a manual `Change Channel` choice.
- `PROVEN`: current repository search does not contain this accepted wording/decision.
- `PROVEN`: PR #152 merged the nonbinding `GAME-CHANNEL-01` pre-decision dossier as `3128b1479ea5565b39b178f9419edcbac46905e9`; that dossier correctly leaves broader channel product policy unaccepted.
- `DERIVED`: recording the prior owner decision avoids asking the owner again and narrows the remaining `GAME-CHANNEL-01` decision surface without accepting unrelated recommendations.

## Acceptance criteria

- [ ] Record one-login / no-separate-login-server channel UX as owner accepted.
- [ ] Record channel presentation at character/world selection as owner accepted.
- [ ] Record automatic/recommended channel plus manual `Change Channel` choice as owner accepted.
- [ ] State exact precedence over conflicting/open presentation in the nonbinding pre-decision dossier for only this narrow scope.
- [ ] Keep in-world switching semantics, party co-location, anti-hopping, cooldowns, capacity triggers, PvP, event/reward scope and recovery policy unresolved unless already accepted elsewhere.
- [ ] Do not claim full `GAME-CHANNEL-01` acceptance.
- [ ] No runtime/client implementation, protocol, Platform, persistence or production changes.
- [ ] Exact-head self-review and repository-required CI pass before merge.

## Excluded scope

- no new owner/product decision;
- no assumption that manual `Change Channel` is available during active gameplay rather than through selection/session flow;
- no numeric channel limits/cooldowns;
- no party/friend co-location rule;
- no PvP or anti-hopping policy acceptance;
- no boss/event/reward policy acceptance;
- no runtime implementation.

## Implementation / findings

Pending.

## Validation

### Focused

- prior owner-decision recovery: PASS
- repository search for existing canonical copy: no matching decision found
- changed-file review: pending

### Component/integration

- result: `NOT_APPLICABLE` — owner-decision documentation only

### E2E

- result: `NOT_APPLICABLE` — no executable behavior

### Exact-head CI

- final head: pending
- result: pending

## Self-review

- exact head: pending
- method/reviewer: implementing/coordinating agent full-diff review
- material findings: pending
- verdict: pending

## Independent review

- required: `NO` — this task records a previously made owner decision without adding new semantics; it does not change security/protocol/durable-data/production authority.
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
last_progress: Recovered a prior owner-accepted channel-selection UX decision that is absent from canonical repository documentation.
status: implementing
branch: docs/OTV2-20260811-channel-selection-owner-baseline
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
next_action: Write the narrow GAME-CHANNEL-01 channel-selection owner baseline without expanding beyond the recovered owner decision.
```
