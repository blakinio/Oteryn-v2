# OTV2-20260815-ability-combat-reference-continuity

```yaml
task_id: OTV2-20260815-ability-combat-reference-continuity
title: Build target-continuity and provenance-clearance evidence package for first ABILITY_COMBAT cases
mode: CONTRACT
status: investigating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/arch-a-reference-continuity
pr: null
base_sha: 088b466c689f55b308cbdfafa545394baeacf0c5
head_sha: 088b466c689f55b308cbdfafa545394baeacf0c5
final_head_sha: null
final_head_frozen_at: null
owner: DOMAIN ARCHITECTURE DESIGN AGENT / Agent A worker
created_at: 2026-08-15T00:20:22+02:00
updated_at: 2026-08-15T00:20:22+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260815-ability-combat-reference-continuity.md
  - docs/agents/evidence/OTV2-20260815-ability-combat-reference-continuity.md
  - docs/contracts/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1.json
  - docs/architecture/GAME-ABILITY-01_FIRST_REFERENCE_EVIDENCE_FIXTURE_PACKAGE.md
  - docs/architecture/REFERENCE_EVIDENCE_PARITY_MANIFEST_CONTRACT.md
public_contracts:
  - docs/contracts/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1.json
  - docs/architecture/GAME-ABILITY-01_FIRST_REFERENCE_EVIDENCE_FIXTURE_PACKAGE.md
  - docs/architecture/REFERENCE_EVIDENCE_PARITY_MANIFEST_CONTRACT.md
depends_on:
  - issue #259
  - docs/agents/prompts/OTV2_DOMAIN_ARCHITECTURE_DESIGN_AGENT.md
  - docs/agents/programs/OTERYN_V2_ARCHITECTURE_PARALLEL_WORK_ALLOCATION.md
  - docs/architecture/GAME-VISION-01_FIRST_REFERENCE_BASELINE_OWNER_BASELINE.md
  - docs/architecture/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1_OWNER_ACCEPTANCE.md
  - docs/architecture/REFERENCE_EVIDENCE_PARITY_MANIFEST_CONTRACT.md
  - docs/contracts/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1.schema.json
  - docs/architecture/GAME-ABILITY-01_FIRST_REFERENCE_EVIDENCE_FIXTURE_PACKAGE.md
  - PR #255 / merge d04f0939f0078cb677ca3ad66f5949e9f3dadc8d
blocks:
  - coordinator audit of Agent A continuity/provenance evidence package
cross_repository_coordination_id: OTV2-ARCH-PARALLEL-20260814
external_repositories: []
```

## Outcome

Produce a bounded, provenance-aware evidence package for exactly the four registered `ABILITY_COMBAT` Reference cases in issue #259. Promote a case only if admissible evidence directly captures or bridges the immutable `global-tibia-observable-2026-07-28-post-server-save` boundary and provenance/legal requirements are satisfied; otherwise retain `UNKNOWN / PENDING` fail closed.

## Architecture and source of truth

- **PROVEN:** live `main@cb98fd379a61c7cf395d30261cef0ee202e34bcf` contains the published #257/#258 programme prerequisites and selects this exact Agent A package as current paper-only work.
- **PROVEN:** the dedicated worker branch was provisioned at `088b466c689f55b308cbdfafa545394baeacf0c5`; live `main` is one later lifecycle-orchestration commit ahead. Connector fast-forward attempts returned GitHub ref-update 422 for the slash-bearing branch, so no force update was performed. The missing main commit only archives the programme-orchestration task; accepted architecture/evidence dependencies consumed by this task are already present on the worker base.
- **PROVEN:** `REFERENCE_EVIDENCE_PARITY_MANIFEST_CONTRACT.md` requires evidenced continuity from the 2026-07-28 target boundary for any post-target observation and blocks evidence promotion whenever provenance is not `CLEARED`.
- **PROVEN:** manifest revision 3 registers exactly four scoped `ABILITY_COMBAT` cases from PR #255; all are `UNKNOWN`, Oteryn `NOT_STARTED`, parity `PARITY_PENDING_EVIDENCE`, with provenance/legal review `PENDING`.
- **UNKNOWN:** whether admissible time-appropriate evidence exists that can clear continuity and provenance for any of the four cases. This task researches that question without broadening mechanic inventory.

## Acceptance criteria

- [ ] Preflight evidence table records exact target cases, current classes and unresolved blockers before research.
- [ ] Research is bounded to the four issue #259 cases and records exact source, locator, retrieval/capture timing, target-time relation, provenance and uncertainty/conflict.
- [ ] Each case receives an explicit promote/reject decision under accepted continuity/provenance rules; insufficient evidence stays `UNKNOWN`.
- [ ] No patch-note/search absence, OTS/community source or unverified later behavior is treated as independent target-continuity proof.
- [ ] Manifest/fixture/contract changes occur only if evidence materially changes classification/provenance or reveals a necessary contract clarification.
- [ ] No proprietary code/assets, runtime/client/protocol/DDL/Platform/production changes, external-repository writes or unapproved Codex/OpenAI invocation.
- [ ] Repository governance validation and applicable JSON/schema checks are recorded for the exact final PR head.
- [ ] Full-diff self-review has zero unresolved material findings and the draft PR is ready for coordinator audit without merge or lifecycle closeout.

## Excluded scope

No mechanic-inventory expansion; no exact heal/damage formula discovery beyond what is necessary to classify the four registered cases; no runtime/client/server/protocol/persistence/content implementation; no DDL, Platform or production authority; no external-repository writes; no proprietary/restricted evidence; no issue close, task archive, merge, auto-merge or lifecycle publication.

## Implementation / findings

Initial ownership acquired on the dedicated Agent A branch. The branch is intentionally not force-moved after the connector rejected a non-force fast-forward; research consumes live `main` as the canonical source of truth and will verify the complete PR diff against current `main` before handover.

## Validation

### Focused

- command/run: pending
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — paper-only architecture/evidence package unless machine manifest content changes
- result: pending

### E2E

- scenario: `NOT_APPLICABLE` — no runtime authority or implementation
- result: pending

### Exact-head CI

- final head: pending
- trigger source: pending
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Self-review

- exact head: pending
- method/reviewer: DOMAIN ARCHITECTURE DESIGN AGENT / Agent A worker
- material findings: pending
- verdict: pending

## Independent review

- required: YES — issue #259 explicitly requires coordinator audit of the worker draft PR
- exact head: pending
- method/auditor: coordinator after handover
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: PR #255 is accepted predecessor evidence package; no Agent A PR existed at task start
- protected auto-merge: FORBIDDEN BY ISSUE #259 / user instruction
- merge commit/result: NOT PERFORMED
- ownership release: NOT PERFORMED; lifecycle closeout explicitly excluded

## Context checkpoint

```yaml
last_progress: ownership acquired; canonical continuity/provenance rules and predecessor package verified
status: investigating
branch: docs/arch-a-reference-continuity
head_sha: 088b466c689f55b308cbdfafa545394baeacf0c5
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
next_action: research provenance-cleared time-appropriate evidence for exactly the four registered ABILITY_COMBAT cases
```
