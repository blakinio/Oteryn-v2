# OTV2-20260808-fnd04-session-admission-analysis

```yaml
task_id: OTV2-20260808-fnd04-session-admission-analysis
title: Analyze FND-04 identity session admission and lease semantics
mode: CONTRACT
status: repairing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260808-fnd04-session-admission-analysis-repair
pr: null
base_sha: c638ad524772f227dabc90e88a1381cc01e907ce
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: GPT-5.6 Sol architecture continuation session
created_at: 2026-08-08T20:46:00+02:00
updated_at: 2026-08-08T21:13:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260808-fnd04-session-admission-analysis.md
  - docs/architecture/FND-04_SESSION_ADMISSION_LEASE_ANALYSIS_BASELINE.md
  - docs/architecture/FND-04_PLATFORM_PRE_ADMISSION_RECONCILIATION_REFINEMENT.md
public_contracts:
  - docs/architecture/FND-04_SESSION_ADMISSION_LEASE_ANALYSIS_BASELINE.md
  - docs/architecture/FND-04_PLATFORM_PRE_ADMISSION_RECONCILIATION_REFINEMENT.md
depends_on:
  - docs/architecture/ADR-0003-platform-identity-game-gateway-and-admission-boundary.md
  - docs/architecture/ADR-0012-character-authority-and-platform-lifecycle-boundary.md
  - docs/architecture/FND-ID-01_FOUNDATION_IDENTIFIER_CONTRACT.md
  - docs/architecture/FND-ID-01_GAME_SESSION_ID_OWNER_ISSUER_BASELINE.md
  - docs/architecture/FND-ID-01_GAME_SESSION_RECONNECT_GENERATION_OWNER_BASELINE.md
  - docs/architecture/FND-ID-01_ACCOUNT_SINGLE_ONLINE_CHARACTER_OWNER_BASELINE.md
  - docs/architecture/FND-02_PROTOCOL_OTERYN_V1_CONTRACT.md
  - docs/architecture/FND-03_RUNTIME_EXECUTION_CONTRACT.md
  - docs/architecture/DISCONNECT_REENTRY_PVE_PROTECTION_OWNER_DECISION.md
  - docs/contracts/FOUNDATION_ERROR_VOCABULARY.md
  - docs/contracts/FOUNDATION_FAILURE_SCENARIOS.md
  - blakinio/Oteryn-Platform@216f5b2817e9d102337608609e344518512c2a0d:docs/contracts/OTERYN_V2_PRE_ADMISSION_HANDOFF_CONTRACT.md
  - blakinio/Oteryn-Platform@216f5b2817e9d102337608609e344518512c2a0d:docs/contracts/OTERYN_V2_RUNTIME_STATUS_PROJECTION_CONTRACT.md
blocks:
  - final FND-04 Identity Game Session Admission and Character Lease Contract
  - production admission reconnect takeover and character lease implementation claims
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/Oteryn-Platform (read-only reconciliation evidence)
```

## Outcome

Repair the already-merged FND-04 analysis after a delayed exact-head review identified a material reconciliation gap against current `Oteryn-Platform/main` contracts. Preserve the accepted analysis, add one bounded companion refinement for the missing Platform producer/consumer semantics, revalidate exact head, then complete lifecycle closeout before the final FND-04 contract begins.

The repair remains architecture-analysis only. It does not authorize runtime, protocol, persistence, Platform, key, deployment or production implementation.

## Architecture and source of truth

- **PROVEN:** PR #104 merged the primary analysis baseline as `c638ad524772f227dabc90e88a1381cc01e907ce`.
- **PROVEN:** exact delivery head `e14a386c8cc998f69075f99890e6fe68a930b396` passed Agent governance, Dependency review, CodeQL and the then-current exact-head audit.
- **PROVEN:** delayed exact-head review after merge identified a material P1 because the analysis reconciled against historical Platform evidence but not the current accepted Platform native pre-admission/runtime-status contracts.
- **PROVEN:** premature closeout PR #105 was closed unmerged; ownership therefore remains active on `main`.
- **PROVEN:** current Platform reconciliation pin is `blakinio/Oteryn-Platform@216f5b2817e9d102337608609e344518512c2a0d`.
- **PROVEN:** Platform `OTERYN_V2_PRE_ADMISSION_HANDOFF_CONTRACT.md` requires explicit disposition of Platform account-security changes after grant issuance, runtime observation/owner-generation applicability, and a Platform-generated admission-attempt correlation/idempotency reference.
- **PROVEN:** Platform `OTERYN_V2_RUNTIME_STATUS_PROJECTION_CONTRACT.md` requires admission routing to use fresh current-owner runtime evidence and reject superseded owner/generation observations.
- **DERIVED:** producer issuance-attempt identity and game-domain one-time consume nonce are different semantic objects and must not be collapsed merely because both can be random values.
- **DERIVED:** an unexpired grant cannot be assumed valid after material Platform account-security revocation unless the final FND-04 security profile provides an explicit bounded mechanism.
- **DERIVED:** issuance-time runtime observation/owner generation must have an explicit applicability rule; final game-domain current-owner validation remains mandatory even when the grant carries observation context.

## Acceptance criteria

### Existing analysis — preserved

- [x] Platform authorization is distinct from final game-domain admission/GameSession authority.
- [x] AccountPresenceClaim, CharacterLease, GameSession and TransportBinding are semantically distinct.
- [x] GameSession terminality does not release account presence while actor presence remains mandatory.
- [x] Lease expiry/uncertainty cannot self-grant replacement authority.
- [x] Hybrid signed PreAdmissionGrant + game-domain one-time consumption remains the recommended credential class.
- [x] Reconnect lost-response reconciliation is mandatory; rotate-and-forget is rejected.
- [x] PvE re-entry protection is tied to eligible classified unexpected control loss, not routine rebind.
- [x] Recovery uses current game-domain actor placement rather than stale client/Platform routing.

### Platform reconciliation repair

- [ ] Define Platform account-security change after grant issuance as an explicit FND-04 final-contract decision and testable failure boundary.
- [ ] Preserve at least one reviewed mechanism family: sufficiently short bounded risk window, account-security generation binding/current projection, emergency revocation/introspection, or another explicit accepted design; do not silently assume nominal expiry is enough.
- [ ] Define issuance-time runtime observation / route generation / ownership-generation applicability and the conditions under which a generation change invalidates an otherwise unexpired grant.
- [ ] Preserve final game-domain current-owner validation even when Platform grant contains issuance-time runtime evidence.
- [ ] Preserve a distinct Platform `AdmissionAttemptRef`-class producer operation/correlation identity for issuance idempotency/reconciliation, without promoting it to a canonical foundation entity ID unless proven necessary.
- [ ] Keep `AdmissionAttemptRef` distinct from game-domain grant nonce / consume replay key and from GameSessionId.
- [ ] Add required race/failure tests for account-security revocation, stale runtime owner generation and ambiguous grant issuance.

### Governance

- [x] Closeout PR #105 is closed unmerged and non-authoritative.
- [ ] Add one bounded companion refinement rather than rewriting unrelated baseline content.
- [ ] Exact-head changed-path review finds zero unresolved material conflicts.
- [ ] Exact-head Agent governance, Dependency review and CodeQL pass.
- [ ] Independent exact-head architecture/security audit passes with zero open material findings.
- [ ] Squash merge repair before any lifecycle archive/release.

## Excluded scope

This repair does not:

- write `blakinio/Oteryn-Platform`;
- implement grant issuer/consumer code;
- choose JWT/PASETO/COSE library or KMS/HSM vendor;
- define PostgreSQL/Redis schema;
- implement GameSession/lease/reconnect runtime;
- register new protocol messages;
- activate production routes/keys/traffic;
- authorize final FND-04 implementation.

## Implementation / findings

The merged baseline remains valid except where the companion refinement explicitly narrows or supersedes Platform pre-admission semantics.

The repair must make three distinctions binding for the final contract:

1. **Account-security freshness/revocation:** successful Platform issuance is not indefinite proof that the account remains eligible until nominal grant expiry. FND-04 must select a bounded testable post-issuance security-change disposition.
2. **Runtime observation applicability:** a Platform grant may carry issuance-time current-owner evidence, but that evidence is not self-refreshing authority. Current Oteryn-v2 route/runtime ownership is revalidated at final admission; final contract must state which observed generation/revision changes invalidate the grant.
3. **Producer attempt vs consumer nonce:** Platform issuance retry/idempotency has an operation/correlation identity distinct from the game-domain consume nonce. They may be correlated but not silently treated as one lifecycle object.

## Validation

### Focused

- current Platform contract reconciliation: in progress
- exact repair scope: active task + one companion refinement expected

### Component/integration

- `NOT_APPLICABLE` — architecture-analysis repair only.

### E2E

- `NOT_APPLICABLE` — no executable capability introduced; the refinement defines future E2E cases.

### Exact-head CI

- final repair head: pending
- trigger source: pull_request
- result: pending

## Independent audit

- exact repair head: pending
- verdict: pending

## PR and closeout

- original delivery PR: 104, merged
- original delivery merge: c638ad524772f227dabc90e88a1381cc01e907ce
- superseded premature closeout PR: 105, closed unmerged
- repair PR: pending
- ownership release: blocked until repair merge + replacement closeout

## Context checkpoint

```yaml
last_progress: Delayed exact-head review of merged PR #104 exposed a material current-Platform reconciliation gap. Premature closeout #105 was closed unmerged; the active FND-04 analysis task now owns one bounded companion refinement to resolve post-issuance account-security changes, runtime ownership-generation applicability and producer issuance-attempt idempotency.
status: repairing
branch: docs/OTV2-20260808-fnd04-session-admission-analysis-repair
head_sha: null
pr: null
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: null
ci_check_generation: repair-pending
ci_checks_for_current_head: 0
ci_run_ids: []
ci_job_ids: []
runner_assignment_state: unknown
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 1
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: null
blocker: null
next_action: Add and review the Platform pre-admission reconciliation refinement, then open the bounded repair PR and rerun exact-head CI/audit.
```
