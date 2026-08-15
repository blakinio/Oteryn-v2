# OTV2-20260815-analytics-integrity-architecture

```yaml
task_id: OTV2-20260815-analytics-integrity-architecture
title: ANL-02/ANL-03 gameplay analytics and integrity architecture
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/arch-f-analytics-integrity
pr: 270
base_sha: 088b46638ac014cd7928d6b0b75cee44902fe22c
head_sha: 83edbad65e787c967d7afde6aeebcdd51f578602
final_head_sha: null
final_head_frozen_at: null
owner: DOMAIN ARCHITECTURE DESIGN AGENT F
created_at: 2026-08-15T00:20:00+02:00
updated_at: 2026-08-15T22:45:00+02:00
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
  - main@dc1eecae7952902bee3fb1e2d88aefc2be792cae
  - ADR-0006-game-intelligence-analytics-and-audit
  - ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_CONTRACT.md
  - DUR-03_ITEM_TRANSACTION_AND_ANTI_DUPLICATION_CONTRACT.md
  - GAME-CHANNEL-01_CHANNEL_PRODUCT_POLICY_CONTRACT.md
  - SIM-DETERMINISM-01_AUTHORITATIVE_SIMULATION_CONTRACT.md
blocks:
  - exact-head final validation and independent review before coordinator merge
  - later authorized analytics/integrity implementation contracts
cross_repository_coordination_id: null
external_repositories: []
```

`head_sha` records the immediately preceding repaired candidate revision. The exact final task-containing head is recorded externally on PR/check/review evidence rather than via self-referential commit churn.

## Outcome

ANL-02/ANL-03 remain paper-only, read-only analytics/integrity architecture. The branch was reconciled with canonical `main@dc1eecae7952902bee3fb1e2d88aefc2be792cae` without changing the five semantic worker files, then completed the **third and final ordinary material repair cycle** for the stable ANL-02/ANL-03 gate.

All prior repairs remain preserved:

- optional client diagnostics are non-adverse;
- every material security-case lifecycle/reviewer action is append-only/auditable;
- deterministic session/hunt grouping and UTC-day reporting windows are explicit;
- ANL-03 normative deterministic invariant catalogue is explicit;
- DUR-03 remains authoritative prevention/conservation/mutation owner and ANL-03 remains read-only evidence.

The current repair closes the three P2 findings from the owner-authorized review of `7cd840e7e4650c55fc088e997f62443d80be2268`.

## Current repairs

### ANL-02 dashboard presentation / regression acceptance

Repaired in the normative candidate:

- any material dashboard/panel exposes or provides unambiguous drill-down to metric ID/revision, window/cohort, denominator/exposure, sample size, material semantic revisions, quality/completeness/schema/reconciliation/sampling/suppression state and checkpoint/as-of identity;
- partial/unknown/unsupported/reconciliation-pending/loss/suppression states produce visible warning and cannot look like normal complete data;
- missing/suppressed/unknown data cannot be represented as semantic zero;
- sample-sensitive metrics require minimum-sample/exposure warning semantics without inventing one universal numeric threshold;
- material regression decisions retain a separate versioned acceptance record with exact baseline/method/revisions, sample/exposure, evidence quality, checkpoint, confounders and responsible owner disposition;
- `REGRESSION_EVIDENCE_INSUFFICIENT` prevents poor-quality data from becoming a green acceptance;
- dashboard colors/flags and analytical dispositions grant no gameplay/deployment authority.

### ANL-03 no-case terminal disposition

Repaired in the normative candidate:

- after `TRIAGED`, lifecycle explicitly branches to `SIGNAL_DISPOSITION_RECORDED -> SIGNAL_CLOSED` when no case is needed, or to `CASE_OPENED`;
- every no-case triage outcome receives immutable signal-level disposition/close evidence and remains reconstructable/countable;
- later evidence appends a new review/reopen generation instead of overwriting prior terminal history;
- audit record requires signal identity, case identity when one exists, correlation, actor/capability, ordering/time, state/action, rationale/evidence and detector revision linkage.

### ANL-03 supported security disposition

Repaired in the normative candidate:

- `SUPPORTED_SECURITY_FINDING` records a human-reviewed/corroborated bot/automation/protocol-misuse or other security concern without pretending statistical/model evidence became deterministic invariant proof;
- it is explicitly non-sanctioning and grants no ban/mute/kick/confiscation/rollback/DB/account/deploy authority;
- referral may follow as routing action without erasing the evidentiary disposition;
- source quality/caveats remain attached and independent enforcement-owner validation is still required.

## Acceptance criteria

- [x] ANL-02 metric/evidence/session/reporting semantics remain versioned and deterministic.
- [x] ANL-02 dashboards cannot hide metric revision, sample/exposure, quality, suppression or reconciliation state for material decision surfaces.
- [x] Minimum-sample warnings and suppression semantics are explicit without speculative universal numeric thresholds.
- [x] Regression acceptance is a named auditable evidence record and cannot silently convert insufficient evidence into approval.
- [x] ANL-03 deterministic invariant catalogue remains normative and read-only.
- [x] Optional diagnostics remain non-adverse.
- [x] Every material case lifecycle/reviewer action remains immutable/auditable.
- [x] Every triaged signal has a terminal audited disposition even when no case is opened.
- [x] Corroborated security concerns can be represented as `SUPPORTED_SECURITY_FINDING` without becoming deterministic proof or sanction authority.
- [x] DUR-03 remains prevention/conservation/mutation authority; ANL-03 remains observation/evidence.
- [x] Changed paths remain within the five worker-F allocations; current material repair changes only task + two candidate contracts.
- [ ] Exact-final-head full-diff self-review and exact-head repository CI are recorded externally.
- [ ] Final independent review on the unchanged exact head is clean.

## Excluded scope

No runtime detector/collector/warehouse/dashboard implementation, no PostgreSQL DDL/migrations, no broker/lake/vendor selection, no gameplay/economy mutation, sanctions/GM policy, automatic balance/economy control, device fingerprinting/invasive surveillance, Platform/production, ANL-01 registry mutation, DUR-03 prevention changes or coordinator-overlay mutation.

## Repair budget

```yaml
repair_cycles_for_current_gate: 3
```

Repair history for this stable gate:

1. optional-diagnostics non-adverse + immutable security-case lifecycle audit;
2. deterministic ANL-02 session/UTC reporting + normative ANL-03 invariant catalogue;
3. dashboard/regression-acceptance truth + no-case terminal disposition + supported-security disposition.

This is the final ordinary repair generation. Any further material repair requires explicit owner override of the stable-gate three-cycle stop.

## Validation

### Source reconciliation

- ADR-0006 dashboard/regression requirement and minimum-sample-warning migration direction: independently verified;
- no-case lifecycle gap: independently verified from optional `CASE_OPENED` branch and prior disposition structure;
- supported-security disposition gap: independently verified from `ANOMALY_HYPOTHESIS` semantics and prior disposition vocabulary;
- live main reconciliation: completed before current repair.

### Runtime/component/E2E

`NOT_APPLICABLE` — documentation-only architecture; no executable surface changed.

### Exact-head

Current exact head, changed-file review, full-diff self-review and repository CI are recorded externally after this task commit exists.

## Context checkpoint

```yaml
last_progress: third/final ordinary ANL-02/ANL-03 repair applied for dashboard/regression semantics and complete signal/security dispositions after canonical-main reconciliation
status: validating
branch: docs/arch-f-analytics-integrity
head_sha: 83edbad65e787c967d7afde6aeebcdd51f578602
pr: 270
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: push/pull_request
ci_check_generation: final-repair-head-pending
ci_checks_for_current_head: 0
ci_run_ids: []
ci_job_ids: []
runner_assignment_state: unknown
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 3
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: null
blocker: null
next_action: EXACT_HEAD_FULL_DIFF_SELF_REVIEW_AND_CI_THEN_OWNER_AUTHORIZED_INDEPENDENT_REVIEW
```

`MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`
`IMPLEMENTATION_AUTHORITY: NONE`