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
head_sha: f08ef9a3c7f9b1305962f797a0d7400073dfb3ec
final_head_sha: null
final_head_frozen_at: null
owner: DOMAIN ARCHITECTURE DESIGN AGENT F
created_at: 2026-08-15T00:20:00+02:00
updated_at: 2026-08-16
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
  - fresh exact-head repository validation after final task-truth checkpoint
  - genuinely independent non-Codex semantic review because cycle 4 changes security-analytics/evidentiary policy and the Architecture Coordinator materially authored the repair
  - later authorized analytics/integrity implementation contracts
cross_repository_coordination_id: null
external_repositories: []
repair_cycles_for_current_gate: 4
repair_cycle_4_owner_override: explicit owner instruction on 2026-08-16 authorizing C/D/E/F continuation beyond the three-cycle stop
owner_review_constraint: no Codex for this continuation
```

`head_sha` records the immediately preceding fully synchronized/self-reviewed checkpoint (`f08ef9a3...`). The exact final task-containing head is recorded externally on PR/check/review evidence after this truth-correction commit; no self-referential follow-up commit is created merely to record its own SHA.

## Outcome

ANL-02/ANL-03 remain paper-only, read-only analytics/integrity architecture. The stable gate completed **owner-authorized material repair cycle 4** after the owner explicitly overrode the ordinary three-cycle ceiling for C, D, E and F and instructed continuation without Codex.

All prior repairs remain preserved:

- optional client diagnostics are non-adverse;
- every material security-case lifecycle/reviewer action is append-only/auditable;
- deterministic session/hunt grouping and UTC-day reporting windows are explicit;
- ANL-03 normative deterministic invariant catalogue is explicit;
- DUR-03 remains authoritative prevention/conservation/mutation owner and ANL-03 remains read-only evidence;
- dashboard evidence truth/warning semantics are explicit;
- every triaged signal has an audited no-case terminal disposition path;
- `SUPPORTED_SECURITY_FINDING` remains non-sanctioning evidence.

Repair cycle 4 closes the two material findings from the final review of `49e1fe0b909d2d5b4a213435d3581235235b3288`.

The repaired worker-F blobs were reconciled to current `main@8722e565c6a0556934209820e3c14ee4f2dc6093` without semantic modification. Exact-head self-review on pre-checkpoint head `f08ef9a3c7f9b1305962f797a0d7400073dfb3ec` passed with zero material findings and confirmed the final scope remained exactly the five worker-F paths. The only post-repair main ancestry addition was unrelated Atlas lifecycle closeout #289.

## Repair cycle 4

### ANL-02 — fail-closed no-regression acceptance

The candidate makes `NO_MATERIAL_REGRESSION_SUPPORTED` impossible unless all applicable preconditions are positively satisfied:

1. required source completeness/schema quality is sufficient;
2. every applicable versioned minimum sample/exposure requirement is met and required evidence is unsuppressed;
3. baseline/current metric, cohort, denominator and material semantic revisions are compatible or explicitly stratified under the named method;
4. duplicate/order/late-event/source-checkpoint reconciliation and required backfill/recompute state are sufficiently terminal for the declared acceptance window;
5. privacy suppression does not remove evidence required for the declared conclusion;
6. exact baseline/method/threshold/windows/cohorts/checkpoint and confounders are retained.

If an evaluation is attempted and any applicable precondition fails, the mandatory disposition is `REGRESSION_EVIDENCE_INSUFFICIENT`. A dashboard warning or visual caveat may accompany that state but can never coexist with a green `NO_MATERIAL_REGRESSION_SUPPORTED` disposition on the same insufficient evidence. `REGRESSION_NOT_EVALUATED` remains only the pre-evaluation state.

### ANL-03 — evidentiary disposition before referral

The candidate separates **substantive evidentiary dispositions** from **routing actions**.

Allowed substantive dispositions remain:

- `SUPPORTED_INTEGRITY_OR_DEFECT_FINDING`;
- `SUPPORTED_SECURITY_FINDING`;
- `NOT_SUPPORTED_FALSE_POSITIVE`;
- `INCONCLUSIVE_INSUFFICIENT_EVIDENCE`;
- `DATA_QUALITY_OR_PIPELINE_FAILURE`;
- `DUPLICATE_OR_ALREADY_COVERED`.

`REFERRED_TO_SECURITY_GM_PRODUCT_OR_ENGINE_OWNER` is no longer an evidence disposition. It is an optional append-only routing action that MUST reference a preceding substantive disposition for the same review generation. This applies to both no-case and case workflows. A naked direct referral is invalid; if evidence is not positively supported, the reviewer still records the truthful inconclusive/data-quality/false-positive/duplicate disposition before routing.

Referral does not alter evidence quality, does not imply target-owner acceptance, and grants no enforcement authority. The ANL-03 companion analysis was reconciled to the same rule and no longer describes referral as a standalone evidence disposition.

## Acceptance criteria

- [x] ANL-02 metric/evidence/session/reporting semantics remain versioned and deterministic.
- [x] ANL-02 dashboards cannot hide metric revision, sample/exposure, quality, suppression or reconciliation state for material decision surfaces.
- [x] Minimum-sample warnings and suppression semantics remain explicit without speculative universal numeric thresholds.
- [x] Regression acceptance is a named auditable evidence record.
- [x] `NO_MATERIAL_REGRESSION_SUPPORTED` is normatively gated by quality/completeness, sample/exposure, comparability, reconciliation/finality, privacy sufficiency and method/provenance preconditions.
- [x] Any failed applicable precondition after evaluation mandates `REGRESSION_EVIDENCE_INSUFFICIENT`; warning-only green acceptance is forbidden.
- [x] ANL-03 deterministic invariant catalogue remains normative and read-only.
- [x] Optional diagnostics remain non-adverse.
- [x] Every material case lifecycle/reviewer action remains immutable/auditable.
- [x] Every triaged signal has a terminal audited substantive disposition even when no case is opened.
- [x] Corroborated security concerns can be represented as `SUPPORTED_SECURITY_FINDING` without becoming deterministic proof or sanction authority.
- [x] Referral is routing only and cannot stand alone; both no-case and case referral require a preceding substantive evidentiary disposition.
- [x] DUR-03 remains prevention/conservation/mutation authority; ANL-03 remains observation/evidence.
- [x] Changed paths remain within the five worker-F allocations; cycle 4 changes only task + two candidate contracts plus the necessary ANL-03 analysis consistency repair.
- [x] Branch was reconciled to current `main@8722e565c6a0556934209820e3c14ee4f2dc6093` without semantic loss before this task-truth checkpoint.
- [x] Full-diff self-review on synchronized pre-checkpoint head `f08ef9a3c7f9b1305962f797a0d7400073dfb3ec` was clean with zero material findings.
- [ ] Required repository checks pass on the final task-containing exact head after this checkpoint correction.
- [ ] Required genuinely independent non-Codex review on that unchanged final exact head is clean.

## Excluded scope

No runtime detector/collector/warehouse/dashboard implementation, no PostgreSQL DDL/migrations, no broker/lake/vendor selection, no gameplay/economy mutation, sanctions/GM policy, automatic balance/economy control, device fingerprinting/invasive surveillance, Platform/production, ANL-01 registry mutation, DUR-03 prevention changes, coordinator-overlay mutation or cross-repository write.

## Repair budget and history

```yaml
repair_cycles_for_current_gate: 4
ordinary_repair_ceiling: 3
override_status: OWNER_AUTHORIZED_2026_08_16
```

Repair history for this stable gate:

1. optional-diagnostics non-adverse + immutable security-case lifecycle audit;
2. deterministic ANL-02 session/UTC reporting + normative ANL-03 invariant catalogue;
3. dashboard/regression-acceptance truth + no-case terminal disposition + supported-security disposition;
4. owner-authorized strict no-regression evidence preconditions + substantive-evidence-before-referral rule.

The owner override permits bounded continuation beyond cycle 3; it does not reset history, waive exact-head validation, widen worker ownership or authorize runtime/production work.

## Validation

### Source reconciliation

- final P2 `PRRT_kwDOTuGrds6ZivQ0` established that warning-only sample/quality handling still allowed a green no-regression disposition; cycle 4 makes the disposition fail closed;
- final P2 `PRRT_kwDOTuGrds6ZivQ2` established that referral could still stand alone; cycle 4 removes referral from evidence dispositions and requires a preceding substantive disposition;
- earlier ADR-0006 dashboard/regression semantics, ANL-01 lifecycle evidence and DUR-03 authority remain preserved;
- historical material threads were resolved only after the semantic repairs and companion-analysis consistency repair were verified.

### Runtime/component/E2E

`NOT_APPLICABLE` — documentation-only architecture; no executable surface changed.

### Exact-head

The exact final task-containing head, changed-file review, full-diff self-review and repository CI are recorded externally after this checkpoint commit. Required scope remains exactly the five worker-F paths and current-main ancestry must remain `behind_by=0`.

## Self-review

- required: YES
- pre-checkpoint synchronized head: `f08ef9a3c7f9b1305962f797a0d7400073dfb3ec`
- result: PASS, zero material findings; final task-containing head requires focused truth-check/self-review after this checkpoint commit

## Independent review

- required: YES
- exact head: must be the unchanged final task-containing repair head
- allowed method: genuinely independent fresh separate non-authoring agent/session, qualified human reviewer or a dedicated independent audit mechanism that actually evaluates the semantic architecture diff
- Codex: **NOT TO BE USED** for this continuation per explicit owner instruction
- verdict: pending

## PR and closeout

- PR #270 remains open and unmerged during repair validation.
- Historical material review threads are repaired and resolved after semantic repair verification.
- No archive or ownership release before merge.
- Pre-merge current-main ancestry, exact-head CI, mandatory self-review, required independent review and zero unresolved material threads remain mandatory.

## Context checkpoint

```yaml
last_progress: cycle-4 ANL-02/ANL-03 repairs were reconciled to current main and self-reviewed clean; this commit corrects the durable task checkpoint to the real remaining gates
status: validating
branch: docs/arch-f-analytics-integrity
head_sha: f08ef9a3c7f9b1305962f797a0d7400073dfb3ec
pr: 270
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: push/pull_request
ci_check_generation: final-task-truth-checkpoint
ci_checks_for_current_head: 0
ci_run_ids: []
ci_job_ids: []
runner_assignment_state: unknown
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 4
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: null
blocker: independent non-Codex semantic review after exact-head repository validation
next_action: VALIDATE_FINAL_TASK_HEAD_THEN_INDEPENDENT_NON_CODEX_REVIEW
```

`MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`
`IMPLEMENTATION_AUTHORITY: NONE`