# OTV2-20260807-game-session-id-owner

```yaml
task_id: OTV2-20260807-game-session-id-owner
title: Freeze GameSessionId ownership and issuer semantics
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260807-game-session-id-owner
pr: null
base_sha: 96760a99ce09bf20417a4a9d6dc1961785156b6c
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-07T20:36:00+02:00
updated_at: 2026-08-07T20:36:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260807-game-session-id-owner.md
  - docs/architecture/FND-ID-01_GAME_SESSION_ID_OWNER_ISSUER_BASELINE.md
public_contracts:
  - docs/architecture/FND-ID-01_GAME_SESSION_ID_OWNER_ISSUER_BASELINE.md
depends_on:
  - ADR-0001 through ADR-0011
  - docs/architecture/FND-ID-01_MINIMUM_CROSS_BOUNDARY_SCOPE_OWNER_BASELINE.md
  - docs/architecture/FND-ID-01_GAME_SESSION_RECONNECT_GENERATION_OWNER_BASELINE.md
  - docs/architecture/FND-ID-01_ACCOUNT_SINGLE_ONLINE_CHARACTER_OWNER_BASELINE.md
  - docs/architecture/ADR-0003-platform-identity-game-gateway-and-admission-boundary.md
blocks:
  - complete FND-ID-01 contract must consume this GameSessionId decision before FND-02/FND-04 freeze dependent fields and state machines
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/Oteryn-Platform
```

## Outcome

Record the owner-accepted `GameSessionId` foundation identity decision without implementing runtime behavior.

The canonical result must separate Platform authorization-to-attempt from the existence of an authoritative gameplay session, preserve reconnect continuity, and prevent Gateway, ChannelRuntime, transport or deployment topology from becoming the semantic owner of a logical game session.

## Architecture and source of truth

- `PROVEN` — ADR-0003 keeps Identity, Game Login Ticket, Game Gateway and World Registry in Platform while the authoritative game server validates admission and owns gameplay authority.
- `PROVEN` — the minimum `FND-ID-01` scope includes `GameSessionId` because downstream protocol/runtime/admission contracts cannot be unambiguous without its semantic owner and lifetime.
- `PROVEN` — the reconnect baseline already preserves one logical `GameSessionId` across eligible transport reconnects while advancing transport/connection generation.
- `PROVEN` — the project owner accepted that `GameSessionId` belongs to game-domain Game Session / Admission authority, not Platform/Gateway or ChannelRuntime.
- `DERIVED` — treating Platform-issued authorization and an actually admitted gameplay session as the same identity would create orphan/pre-admission sessions and blur the trust boundary.

## Acceptance criteria

- [x] Make game-domain Game Session / Admission authority the canonical owner and logical issuer of `GameSessionId`.
- [x] Explicitly exclude Platform Identity, Game Gateway, World Registry, ChannelRuntime, GameNode transport and orchestrator from `GameSessionId` issuance.
- [x] Freeze `GameSessionId` as a strongly typed UUIDv7 preserving all 128 bits.
- [x] Freeze global uniqueness and make `GameSessionId` the semantic session identity rather than `WorldId + GameSessionId`.
- [x] Preserve mandatory binding to `AccountId`, `CharacterId`, `WorldId` and current channel/session authority state.
- [x] State that `GameSessionId` is not a credential and never grants mutation/reconnect authority by itself.
- [x] Preserve the same logical `GameSessionId` across eligible reconnect while transport/connection generation advances.
- [x] Require a new `GameSessionId` after terminal session end and for a fresh channel-session transition.
- [x] Preserve logical-owner-versus-deployment separation; a dedicated microservice is not required by this decision.
- [x] Keep exact admission transaction commit point, credential form, lease transaction mechanics and terminal state machine for `FND-04`.
- [x] Keep wire encoding/byte order/framing for `FND-02`.
- [x] Keep `AdmissionId` optional/unresolved unless later foundation design proves it is a distinct required identity.
- [x] Preserve no-implementation mode.
- [ ] Review exact changed-file diff.
- [ ] Independent architecture audit against final exact head.
- [ ] Required exact-head documentation/governance checks.

## Excluded scope

This task does not:

- implement login, admission, lease, reconnect or duplicate-login behavior;
- define the exact atomic transaction boundary at which admission becomes committed;
- decide whether an `AdmissionId`, `CharacterLeaseId` or handoff ID is required;
- define reconnect credentials or transport cryptography;
- define protocol field encoding or message layout;
- define PostgreSQL storage, indexes, retention or recovery implementation;
- modify `blakinio/Oteryn-Platform`;
- create a new microservice;
- change production systems.

## Implementation / findings

Accepted separation:

```text
Platform / Gateway
    -> authenticates identity and grants/routs an attempt

Game Session / Admission authority
    -> decides successful gameplay admission
    -> issues GameSessionId
    -> binds authoritative gameplay-session state

ChannelRuntime
    -> executes gameplay after handoff
    -> does not own or issue GameSessionId
```

Accepted representation:

```text
GameSessionId = strongly typed UUIDv7, full 128 bits, globally unique
```

Accepted reconnect rule:

```text
same logical session + eligible reconnect
    -> same GameSessionId
    -> newer transport/connection generation

terminal session end / fresh session transition
    -> new GameSessionId
```

The exact atomic creation/commit point inside the future admission state machine remains deliberately deferred to `FND-04`.

## Validation

### Focused

- command/run: pending documentation/governance validation
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture documentation only
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no executable runtime behavior changes
- result: `NOT_APPLICABLE`

### Exact-head CI

- final head: recorded in immutable PR/check evidence after content freeze
- trigger source: pull_request
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: architecture consistency review against accepted FND-ID-01, ADR-0003 and reconnect/session baselines
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related PR #81: bookkeeping-only closeout for prior task; no owned-path overlap
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Owner accepted game-domain ownership/issuance of GameSessionId and the bounded architecture task was opened on current main.
status: validating
branch: docs/OTV2-20260807-game-session-id-owner
pr: null
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: pull_request
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
next_action: Add the canonical GameSessionId owner/issuer baseline, open the bounded PR, then audit and validate its exact final head.
```
