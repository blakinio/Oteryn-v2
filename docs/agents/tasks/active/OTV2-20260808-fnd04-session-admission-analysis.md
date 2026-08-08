# OTV2-20260808-fnd04-session-admission-analysis

```yaml
task_id: OTV2-20260808-fnd04-session-admission-analysis
title: Analyze FND-04 identity session admission and lease semantics
mode: CONTRACT
status: investigating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260808-fnd04-session-admission-analysis
pr: null
base_sha: 3c32fb08ddf52939159c0ace5fe607ca4fb18332
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: GPT-5.6 Sol architecture continuation session
created_at: 2026-08-08T20:46:00+02:00
updated_at: 2026-08-08T20:46:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260808-fnd04-session-admission-analysis.md
  - docs/architecture/FND-04_SESSION_ADMISSION_LEASE_ANALYSIS_BASELINE.md
public_contracts:
  - docs/architecture/FND-04_SESSION_ADMISSION_LEASE_ANALYSIS_BASELINE.md
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
blocks:
  - final FND-04 Identity Game Session Admission and Character Lease Contract
  - production admission reconnect takeover and character lease implementation claims
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/Oteryn-Platform (read-only reconciliation evidence)
```

## Outcome

Produce a bounded architecture-analysis baseline for `FND-04` before freezing its security-sensitive final contract. The baseline must reconcile accepted identity, Platform/Gateway, protocol, runtime, reconnect, duplicate-login, combat-presence and character-ownership decisions; classify which FND-04 choices must be decided before implementation versus measured/deferred; and recommend one coherent admission/session/lease state model without implementing runtime, persistence or Platform changes.

## Architecture and source of truth

- **PROVEN:** `main@3c32fb08ddf52939159c0ace5fe607ca4fb18332` contains accepted FND-01/FND-ID-01/FND-02/FND-03 foundation semantics and the FND-03 lifecycle closeout.
- **PROVEN:** no open pull request existed at task start.
- **PROVEN:** Platform Identity owns reusable account credentials, OAuth/PKCE, MFA and Game Login Ticket issuance; Game Gateway remains a Platform control-plane component and is not gameplay authority.
- **PROVEN:** canonical `GameSessionId` is game-domain-owned and is issued only after successful authoritative admission.
- **PROVEN:** FND-02 already fixes `connection_generation` as a non-zero post-admission `uint64` fence scoped to one GameSessionId, with strictly newer generation on accepted rebind.
- **PROVEN:** one AccountId may have at most one authoritative online CharacterId; a healthy combat/PZ/logout-locked incumbent cannot be kicked by a duplicate login.
- **PROVEN:** an eligible short reconnect preserves GameSessionId, advances connection generation, and starts from an owner-accepted initial 15-second reconnect-grace policy.
- **PROVEN:** FND-03 owns monotonic execution of accepted 2-second disconnect protection, 5-second stale-transport cleanup and 4-second defensive PvE re-entry effects; FND-04 owns which current-generation evidence is sufficient and the exact logical session/reconnect state semantics.
- **PROVEN:** the canonical current-status overlay on main still contains transition-safe historical wording around PR #102 and therefore needs a later narrow synchronization after the FND-04 analysis/final package selects the correct progression wording.
- **DERIVED:** FND-04 needs separate semantic concepts for account presence exclusion, character player-control authority and transport binding even if later persistence stores them in one transaction/record family.
- **UNKNOWN:** exact pre-admission credential format/algorithm, reconnect credential construction, physical lease store/schema, exact heartbeat cadence, lease durations/safety margin and final public error codes.

## Acceptance criteria

### Authority and state model

- [ ] Reconcile Platform authorization-to-attempt-admission with game-domain final admission and canonical GameSessionId creation.
- [ ] Separate account-global online-character exclusion from CharacterId-specific player-control/session authority and from concrete transport binding.
- [ ] Define semantic linearization points for fresh admission, duplicate-login takeover, same-session reconnect, fresh-session recovery, logout and terminal session end.
- [ ] Preserve Character Authority ownership revalidation at final admission.

### Credential and replay analysis

- [ ] Compare signed, opaque and hybrid pre-admission credentials against Platform availability, replay prevention, key rotation, revocation and cross-language rollout needs.
- [ ] Define minimum binding fields and validation order without changing FND-02 framing/schema ownership.
- [ ] Analyze reconnect credential replay/rotation and lost-response/crash ambiguity.
- [ ] Decide whether `AdmissionId` or `CharacterLeaseId` is actually required; default is no new foundation identity without proof.

### Liveness reconnect and takeover

- [ ] Define sufficient current-generation liveness evidence conceptually without using socket-open state or client timestamps as authority.
- [ ] Analyze exact server-authoritative start of the accepted 15-second reconnect window relative to the 2-second control-loss boundary.
- [ ] Preserve 5-second transport cleanup independence from logical GameSession continuity.
- [ ] Define same-character recovery after reconnect-grace expiry while the actor still has mandatory combat/PZ/logout presence.
- [ ] Preserve healthy combat-locked incumbent protection and account-global one-online-character invariant under races.
- [ ] Identify anti-flap/re-entry-protection abuse risk without inventing an unapproved gameplay penalty.

### Lease fencing and failure

- [ ] Define account/character lease-generation semantics and stale-owner behavior without freezing PostgreSQL schema.
- [ ] Define renewal failure, expiry, revocation and safe-loss-of-control semantics consistent with FND-03 fencing.
- [ ] Classify every shared foundation failure scenario for FND-04 and identify any truly missing stable scenario IDs.
- [ ] Define key rotation/emergency revocation requirements and fail-closed behavior for revision/route/audience mismatch.

### Governance

- [ ] Architecture analysis only; no Rust, protocol runtime, persistence schema, Platform write, deployment or production activation.
- [ ] Full changed-path review has zero unresolved material conflicts.
- [ ] Exact-head Agent governance, Dependency review and CodeQL pass.
- [ ] Independent exact-head architecture/security audit passes with zero open material findings.
- [ ] Squash merge only after all final-head gates pass; archive/release ownership separately.

## Excluded scope

This task does not implement or authorize:

- Rust Game Session/admission/lease runtime;
- Platform/Gateway code or external-repository writes;
- PostgreSQL tables, locks, isolation levels or migrations;
- production key infrastructure or secret material;
- `protocol-oteryn` codecs/listeners/client adapters or new production message registration;
- exact gameplay combat/logout formulas;
- production heartbeat/lease numeric values unless the architecture analysis proves a value is forced by an already accepted invariant;
- production traffic or deployment.

## Implementation / findings

Initial preflight found no open PR ownership conflict. Existing active historical task records are treated as prior evidence only; this package claims only the two paths listed above and does not edit another active task.

The analysis must prefer a small number of explicit authority states over a monolithic "session token" abstraction. In particular, it must not make `GameSessionId`, AccountId, CharacterId, NodeId or HandoffId act as bearer credentials.

## Validation

### Focused

- accepted-input reconciliation: in progress
- result: pending

### Component/integration

- result: `NOT_APPLICABLE` — architecture-analysis delivery only.

### E2E

- result: `NOT_APPLICABLE` — no executable capability introduced.

### Exact-head CI

- final head: pending
- trigger source: pull_request
- workflow/run/job: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: pending
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: none at task start
- merge policy: squash after exact-head validation
- merge commit/result: pending
- ownership release: pending separate closeout

## Context checkpoint

```yaml
last_progress: FND-04 analysis task started from main after FND-03 final contract and lifecycle closeout; accepted Platform/session/reconnect/account-concurrency inputs are being reconciled before any security-sensitive mechanism is frozen.
status: investigating
branch: docs/OTV2-20260808-fnd04-session-admission-analysis
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
next_action: Write the bounded FND-04 session/admission/lease analysis baseline and inspect it against every accepted failure/race invariant.
```
