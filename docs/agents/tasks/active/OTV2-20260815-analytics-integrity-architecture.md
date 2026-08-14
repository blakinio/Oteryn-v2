# OTV2-20260815-analytics-integrity-architecture

```yaml
task_id: OTV2-20260815-analytics-integrity-architecture
title: ANL-02/ANL-03 gameplay analytics and integrity architecture
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/arch-f-analytics-integrity
pr: null
base_sha: 088b46638ac014cd7928d6b0b75cee44902fe22c
head_sha: 088b46638ac014cd7928d6b0b75cee44902fe22c
final_head_sha: null
final_head_frozen_at: null
owner: DOMAIN ARCHITECTURE DESIGN AGENT F
created_at: 2026-08-15T00:20:00+02:00
updated_at: 2026-08-15T00:20:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260815-analytics-integrity-architecture.md
  - docs/architecture/ANL-02_GAMEPLAY_BALANCE_WORLD_ANALYTICS_ANALYSIS.md
  - docs/architecture/ANL-02_GAMEPLAY_BALANCE_WORLD_ANALYTICS_CONTRACT_CANDIDATE.md
  - docs/architecture/ANL-03_ECONOMY_INTEGRITY_SECURITY_ANALYTICS_ANALYSIS.md
  - docs/architecture/ANL-03_ECONOMY_INTEGRITY_SECURITY_ANALYTICS_CONTRACT_CANDIDATE.md
public_contracts:
  - docs/architecture/ANL-02_GAMEPLAY_BALANCE_WORLD_ANALYTICS_CONTRACT_CANDIDATE.md
  - docs/architecture/ANL-03_ECONOMY_INTEGRITY_SECURITY_ANALYTICS_CONTRACT_CANDIDATE.md
depends_on:
  - issue #264 coordinator allocation
  - ADR-0006-game-intelligence-analytics-and-audit
  - ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_CONTRACT.md
  - DUR-03_ITEM_TRANSACTION_AND_ANTI_DUPLICATION_CONTRACT.md
  - GAME-CHANNEL-01_CHANNEL_PRODUCT_POLICY_CONTRACT.md
  - SIM-DETERMINISM-01_AUTHORITATIVE_SIMULATION_CONTRACT.md
blocks:
  - coordinator acceptance of ANL-02/ANL-03 candidate architecture
  - later authorized analytics/integrity implementation contracts
cross_repository_coordination_id: null
external_repositories: []
```

## Outcome

Produce a bounded, reviewable ANL-02/ANL-03 architecture package that defines non-authoritative gameplay/balance/world analytics and economy/integrity/security analytics on top of accepted ANL-01/DUR-03, including metric/evidence quality, detector/case lifecycle, false-positive controls, privacy/retention/access and resource-bound semantics, without granting runtime, enforcement or production authority.

## Architecture and source of truth

- `PROVEN` — issue #264 and its coordinator activation comment allocate worker F, branch `docs/arch-f-analytics-integrity`, trusted base `088b46638ac014cd7928d6b0b75cee44902fe22c`, ANL-02/ANL-03-owned new artifacts and coordinator-only merge authority.
- `PROVEN` — ADR-0006 makes Game Intelligence observational/investigative and separates operational observability, best-effort gameplay telemetry and durable economy/security audit.
- `PROVEN` — ANL-01 freezes event identity/interchange, typed ordering/causation, durable audit semantics, privacy classes, retention gating and bounded query/evidence foundations; the initial event-type registry is deliberately empty and domain owners register concrete families later.
- `PROVEN` — DUR-03 owns item/currency/value prevention, conservation, idempotency, fencing and authoritative mutation semantics; analytics may consume evidence but may not repair or mutate production state.
- `PROVEN` — GAME-CHANNEL keeps one World economy across Channels and requires explicit reward/source multiplicity semantics; Channel multiplicity is not automatically durable source multiplicity.
- `PROVEN` — SIM-DETERMINISM owns authoritative replay/state provenance; replay and analytics are read-only evidence and cannot become gameplay authority.
- `DERIVED` — ANL-02/03 can close consumer/evidence semantics now while leaving concrete producer event-family registration to owning gameplay/DUR gates and warehouse/vendor/runtime topology to later authorized implementation work.

## Acceptance criteria

- [ ] ANL-02 analysis defines metric/evidence taxonomy, cohort/denominator/version semantics, world/balance dimensions, quality/confidence rules, privacy/retention/access and no-auto-balance authority boundary.
- [ ] ANL-03 analysis defines economy/integrity/security evidence, detector inputs/outputs/versioning, case lifecycle, deterministic versus statistical findings, false-positive controls, investigator access and no-sanction/no-mutation authority boundary.
- [ ] Candidate contracts are included only for semantics mature enough to freeze without selecting warehouse/vendor/runtime implementation.
- [ ] `DECISIONS_NOT_TAKEN` and `CROSS_DOMAIN_FINDINGS` are explicit in both domain artifacts and the draft PR.
- [ ] Changed paths remain within this task's owned-path allowlist and do not touch coordinator-only/sibling-owned surfaces.
- [ ] Documentation-focused validation, exact-head full-diff self-review, ordinary exact-head PR CI and review-thread inspection are recorded.
- [ ] Final PR remains draft with `MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`; next action is Architecture Coordinator audit only.

## Excluded scope

No runtime detector/collector/warehouse implementation, PostgreSQL DDL/migrations, broker/lake/dashboard/vendor selection, gameplay or economy mutation, rollback, sanctions/GM policy, automatic balancing, automatic economy control, Platform/production work, global architecture overlays, ANL-01 registry mutation, DUR-03 prevention changes, sibling worker paths or owner-funded AI/Codex invocation.

## Implementation / findings

- Branch/trusted-base ownership and live sibling overlap were checked before mutation.
- Live `main` has one later orchestration lifecycle-closeout commit, but issue #264 explicitly requires work from the coordinator-activated trusted worker branch; no semantic ANL dependency drift was identified.
- The empty ANL-01 event registry is an intentional owner boundary, not permission for worker F to mint foreign gameplay/DUR event types. Any missing producer evidence needed by ANL-02/03 will be reported cross-domain.
- Candidate-contract maturity will be judged against the accepted ADR-0006, ANL-01, DUR-03, GAME-CHANNEL and SIM boundaries before inclusion.

## Validation

### Focused

- command/run: pending until coherent document set exists
- result: pending

### Component/integration

- command/run: documentation-only architecture consistency review against accepted ANL/DUR/channel/SIM contracts
- result: pending

### E2E

- scenario: `NOT_APPLICABLE` — this task changes paper-only architecture and grants no executable/runtime behavior
- result: `NOT_APPLICABLE`

### Exact-head CI

- final head: pending
- trigger source: pull_request to `main`
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Self-review

- exact head: pending
- method/reviewer: DOMAIN ARCHITECTURE DESIGN AGENT F; mandatory full PR diff and authority-boundary review
- material findings: pending
- verdict: pending

## Independent review

- required: `YES` — Architecture Coordinator audit is required before any candidate semantics may become canonical
- exact head: pending
- method/auditor: Architecture Coordinator/Auditor under multi-agent orchestration policy
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: sibling worker PRs checked for ownership overlap; no overlap identified at startup
- protected auto-merge: forbidden for worker F
- merge commit/result: coordinator-owned; worker must not merge
- ownership release: coordinator-owned; worker must not archive/release own task

## Context checkpoint

```yaml
last_progress: created assigned active task after trusted-base, governance and overlap verification
status: implementing
branch: docs/arch-f-analytics-integrity
head_sha: 088b46638ac014cd7928d6b0b75cee44902fe22c
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
next_action: write ANL-02/ANL-03 analyses and bounded candidate contracts, then open/update the worker draft PR
```
