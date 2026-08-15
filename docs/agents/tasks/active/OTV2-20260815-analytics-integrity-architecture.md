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
head_sha: dfca88975ee3157b9e5793d344cc0494745066d7
final_head_sha: null
final_head_frozen_at: null
owner: DOMAIN ARCHITECTURE DESIGN AGENT F
created_at: 2026-08-15T00:20:00+02:00
updated_at: 2026-08-15T00:33:00+02:00
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

`head_sha` records the previously reviewed exact head that received the current P2 findings. The exact repaired final head belongs in immutable PR/check/review evidence after the repair commits exist; this task does not create a self-referential metadata commit merely to copy its own SHA.

## Outcome

Produced the bounded ANL-02/ANL-03 architecture package defining non-authoritative gameplay/balance/world analytics and economy/integrity/security analytics over accepted ANL-01/DUR-03 foundations. Two earlier P2 repairs remain valid, and the current second stable-gate repair cycle closes the two additional P2 findings from the owner-authorized final review: deterministic hunt/session/reporting-window semantics for ANL-02 and the normative ADR-0006 deterministic invariant catalogue for ANL-03. Runtime implementation remains `NOT_STARTED`; no detector, warehouse, DDL, gameplay, enforcement or production code was modified.

Draft PR: `#270`.

## Architecture and source of truth

- `PROVEN` — issue #264 and its coordinator activation allocate worker F, branch `docs/arch-f-analytics-integrity`, trusted base `088b46638ac014cd7928d6b0b75cee44902fe22c`, these five worker-F paths and coordinator-only merge authority.
- `PROVEN` — current live `main` at this repair preflight is `4246b165473059c0ac81475d885d71350c2cfb36`; no worker-F owned path exists there, and sibling architecture work remains path-disjoint.
- `PROVEN` — ADR-0006 makes Game Intelligence observational/investigative, requires ANL-02 to define session/aggregate semantics, explicitly reuses UTC-day split as a deterministic reporting rule, and requires ANL-03 to define a deterministic invariant catalogue while DUR-03 remains authoritative prevention.
- `PROVEN` — ANL-01 freezes event identity/interchange, typed ordering/causation, durable audit semantics, privacy classes, retention gating and bounded query/evidence foundations; producer-owned event registration remains outside this task.
- `PROVEN` — DUR-03 owns item/currency/value prevention, conservation, idempotency, fencing and authoritative mutation semantics; ANL-03 may consume evidence but may not repair or mutate production state.
- `PROVEN` — GAME-CHANNEL keeps one World economy across Channels and requires explicit reward/source multiplicity semantics; Channel multiplicity is not automatically durable source multiplicity.
- `PROVEN` — SIM-DETERMINISM owns authoritative replay/state provenance; replay and analytics are read-only evidence and cannot become gameplay authority.
- `PROVEN` — prior owner-funded review on head `1c1980b9741ef58361c271ad8395bd10faa815a2` produced two P2 findings (non-adverse optional diagnostics and immutable case lifecycle history), which were repaired on `dfca88975ee3157b9e5793d344cc0494745066d7` and remain valid.
- `PROVEN` — the second owner-funded review on `dfca88975ee3157b9e5793d344cc0494745066d7` produced the current two P2 findings; its exact authorization is consumed and is not standing permission for another paid/limited AI review.
- `DERIVED` — the first material post-review repair from `1c1980...` to `dfca889...` is repair cycle 1 for the stable ANL-02/ANL-03 gate; the present bounded repair of the two new P2 findings is repair cycle 2. The previous task value `repair_cycles_for_current_gate: 0` was stale.
- `UNKNOWN` — exact producer event IDs/payload schemas, a concrete session/hunt correlation identifier representation, numeric late-data/finalization horizons, warehouse/vendor topology, detector algorithms/thresholds and new implementation resource maxima remain outside this paper gate and were not invented.

## Acceptance criteria

- [x] ANL-02 analysis/candidate preserve metric/evidence taxonomy, cohort/denominator/version semantics, world/balance dimensions, quality rules, privacy/retention/access and no-auto-balance authority boundary.
- [x] ANL-02 candidate now defines deterministic analytical session/hunt grouping without gameplay-session authority: explicit producer-owned grouping/boundary evidence is required; reconnect/session-generation and Channel/Instance transitions cannot be heuristically stitched; missing grouping/terminal evidence is partial/incomplete rather than guessed.
- [x] ANL-02 candidate freezes UTC calendar reporting as half-open `[D 00:00:00Z, D+1 00:00:00Z)`, assigns exact-midnight events to the new day using canonical source occurrence time, keeps hunts spanning midnight semantically continuous, and defines duplicate/out-of-order/late/replayed event behavior plus revision compatibility and deterministic fixtures.
- [x] ANL-03 analysis/candidate preserve detector/signal/case semantics, deterministic versus statistical evidence, false-positive controls, investigator access and no-sanction/no-mutation authority boundary.
- [x] ANL-03 candidate now normatively requires the ADR-0006 invariant catalogue: one live ItemInstanceId cannot occupy two authoritative locations; duplicate/idempotent delivery cannot duplicate item/currency/value; split/merge conserve quantity/value and identities; creation/credit and destruction/debit require authorized source/sink; rewards commit at most once per accepted source/idempotency occurrence; stale generation cannot transfer ownership; transaction/outbox evidence cannot silently disagree; retry/timeout/crash/rollback cannot create unexplained value; inventory/ground/container/depot/trade/market/mail views reconcile to authoritative owner/location.
- [x] DUR-03 remains authoritative prevention/conservation/mutation owner and ANL-03 remains read-only evidence/detection; no automatic ban, confiscation, rollback, DB mutation, value repair, economy tuning or balance mutation was introduced.
- [x] Previous P2 optional-diagnostics non-adverse semantics remain valid.
- [x] Previous P2 immutable reviewer/case lifecycle history remains valid.
- [x] Candidate contracts freeze only semantics mature enough to freeze without selecting warehouse/vendor/runtime implementation.
- [x] `DECISIONS_NOT_TAKEN` and existing report-only cross-domain ownership boundaries remain explicit.
- [x] Current repair changed only worker-F task and ANL-02/ANL-03 candidate paths; analysis paths are intentionally unchanged because the current findings require normative contract closure, not a foreign/new analysis scope.
- [ ] Final repaired exact-head full-diff self-review, reconciliation with live main, exact-head CI and coordinator re-audit remain external evidence generated after this repair commit.

## Excluded scope

No runtime detector/collector/warehouse implementation, PostgreSQL DDL/migrations, broker/lake/dashboard/vendor selection, gameplay or economy mutation, rollback, sanctions/GM policy, automatic balancing, automatic economy control, device fingerprinting/invasive client surveillance, Platform/production work, global architecture overlays, ANL-01 registry mutation, DUR-03 prevention changes, sibling worker paths or owner-funded AI/Codex invocation.

## Implementation / findings

### Delivered worker artifacts

- `ANL-02_GAMEPLAY_BALANCE_WORLD_ANALYTICS_ANALYSIS.md` — versioned metric semantics, evidence-quality vector, cohort/denominator discipline, gameplay/world dimensions, regression/replay/privacy/resource/failure analysis.
- `ANL-02_GAMEPLAY_BALANCE_WORLD_ANALYTICS_CONTRACT_CANDIDATE.md` — bounded non-authoritative consumer contract, now including deterministic analytical hunt/session grouping and UTC reporting-window semantics.
- `ANL-03_ECONOMY_INTEGRITY_SECURITY_ANALYTICS_ANALYSIS.md` — economy/integrity taxonomy, DUR-03 provenance projection, detector/signal versioning, deterministic-versus-statistical evidence, case lifecycle, false-positive/privacy/access/resource semantics.
- `ANL-03_ECONOMY_INTEGRITY_SECURITY_ANALYTICS_CONTRACT_CANDIDATE.md` — bounded non-authoritative read-only integrity/security contract, now including the normative deterministic invariant catalogue; enforcement remains foreign authority.

### Current P2 repair — ANL-02

- Session/hunt grouping is explicitly analytical, not game-session authority.
- Conforming session/hunt metrics require versioned producer-owned correlation/boundary evidence registered through owning producer + ANL-01/FND identity governance; absence cannot be replaced by an implicit inactivity heuristic.
- Reconnect/session-generation changes and Channel/Instance transitions retain exact segment context and do not independently decide hunt continuation; continuity requires the explicit grouping identity.
- UTC-day reporting uses half-open intervals and canonical source occurrence time, not ingestion/replay time; exact midnight belongs to the new day.
- Long hunts may span daily windows; daily contributions split by event occurrence without redefining the hunt boundary.
- Duplicates/replays are at-most-once by ANL-01 identity semantics; out-of-order/late events retain original grouping/time-window semantics and incomplete evidence does not become guessed state.
- Compatible revision stratification is mandatory; no silent cross-revision pooling.
- Deterministic fixtures cover midnight, reconnect, generation, Channel/Instance, duplicate/replay, out-of-order/late, missing grouping/terminal and revision-boundary cases.

### Current P2 repair — ANL-03

The normative candidate now requires the accepted deterministic invariant classes and explicit evidence preconditions. Missing/unregistered/incomplete evidence yields inconclusive/data-quality classification rather than a false pass or guilt inference. `INVARIANT_VIOLATION_SUPPORTED` still requires durable completeness/reproducibility. Analytics cannot repair the authoritative owner/location/value state.

### Cross-domain findings — `REPORT_ONLY`

- `ANL02-XD-01` / `P1`: concrete gameplay analytical event families, including producer-owned grouping evidence where needed, are not registered; gameplay/content producer owners + ANL-01 registry integration must provide them before concrete metric coverage claims.
- `ANL02-XD-02` / `P2`: detailed ability/AI/interaction/quest/event attribution remains dependent on owning gameplay domains.
- `ANL03-XD-01` / `P1`: concrete DUR-03 item/currency/value durable event families are not registered, blocking complete provenance/invariant implementation coverage.
- `ANL03-XD-02` / `P2`: enforcement/GM/account-remediation authority remains outside ANL-03 and requires a separately assigned/accepted owner contract before production action.
- `ANL03-XD-03` / `P2`: FND/session/admission/channel security observation families are not registered; corresponding detectors cannot claim complete coverage.
- `ANL03-XD-04` / `P2`: market/trade/mail/depot/reward fraud/business-policy interpretation remains downstream of owning economy/gameplay gates.

## Repair-cycle evidence

### Repair cycle 1 — completed

- reviewed head: `1c1980b9741ef58361c271ad8395bd10faa815a2`;
- findings: optional client diagnostics must be non-adverse; every material security-case lifecycle/reviewer action must be immutable/auditable;
- repaired exact head: `dfca88975ee3157b9e5793d344cc0494745066d7`;
- coordinator exact-head re-audit/CI: passed before the authorized second final review;
- second owner-funded review authorization: consumed on `dfca889...`.

### Repair cycle 2 — current

- reviewed head: `dfca88975ee3157b9e5793d344cc0494745066d7`;
- P2: deterministic ANL-02 session/hunt/reporting-window semantics including UTC-day split;
- P2: normative ANL-03 deterministic invariant catalogue;
- repair: current worker-F candidate/task changes;
- exact repaired head/CI/full-diff review: pending external exact-head evidence after this commit exists;
- owner-funded review: **NOT AUTHORIZED** for the current repaired head; previous authorization is consumed.

## Validation

### Focused

- command/run: complete current repair diff and source-of-truth review against ADR-0006, ANL-01, DUR-03, GAME-CHANNEL-01 and SIM-DETERMINISM after final repair head exists
- result: pending exact-head external review; current edits remain within worker-F ownership

### Component/integration

- command/run: `NOT_APPLICABLE`
- result: paper-only contract repair; no executable component changed

### E2E

- scenario: `NOT_APPLICABLE` for this delivery
- result: no runtime/client/protocol/DDL/production behavior changed; deterministic analytical fixtures are future implementation evidence obligations, not runtime claims

### Exact-head CI

- final head: recorded immutably on draft PR #270 after this repair commit exists
- trigger source: ordinary GitHub push/pull_request checks
- workflow/run/job: external PR/check evidence
- runner assignment: external PR/check evidence
- classification: documentation/governance exact-head validation
- result: pending current repaired-head checks

## Self-review

- exact head: recorded externally on PR #270 after the repair commit exists
- method/reviewer: full five-path PR diff + bounded current-repair delta + authority/dependency review
- material findings: two earlier P2 repairs preserved; current two P2 findings materially addressed in normative candidates; exact repaired-head review pending
- verdict: **PENDING CURRENT EXACT-HEAD FULL-DIFF SELF-REVIEW**

## Independent review

- required: `YES` — Architecture Coordinator exact-head audit is required before candidate semantics may become canonical
- exact head: current repaired final worker head recorded externally on PR #270
- method/auditor: Architecture Coordinator; any owner-funded Codex/OpenAI review requires a fresh exact authorization for the exact current head and invocation
- owner-funded authorization: previous authorization was consumed on `dfca88975ee3157b9e5793d344cc0494745066d7` and is not standing permission
- verdict: pending current exact-head coordinator re-audit

## PR and closeout

- changed-file review: current repaired exact-head result must be recorded externally on draft PR #270
- review threads: two older P2 threads are resolved; two current P2 threads remain open until exact-head proof confirms the repair
- related/superseded PRs: sibling A/B/C/D/E remain outside worker-F path ownership
- protected auto-merge: not enabled
- merge commit/result: NOT PERFORMED
- ownership release: coordinator-only after later lawful merge/lifecycle closeout
- owner-funded final review: NOT TRIGGERED for this repair; fresh exact owner authorization would be required

## Context checkpoint

```yaml
last_progress: second stable-gate repair cycle implemented for deterministic ANL-02 session/reporting semantics and normative ANL-03 invariant catalogue; exact-head reconciliation, full-diff review and CI pending
status: validating
branch: docs/arch-f-analytics-integrity
head_sha: dfca88975ee3157b9e5793d344cc0494745066d7
pr: 270
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: push/pull_request
ci_check_generation: repair-cycle-2-final-head-pending
ci_checks_for_current_head: 0
ci_run_ids: []
ci_job_ids: []
runner_assignment_state: unknown
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 2
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: fresh exact owner authorization before any owner-funded AI review or draft-to-ready transition that triggers it
blocker: null
next_action: RECONCILE_LIVE_MAIN_THEN_EXACT_HEAD_FULL_DIFF_SELF_REVIEW_CI_AND_COORDINATOR_REAUDIT
```

`MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`
