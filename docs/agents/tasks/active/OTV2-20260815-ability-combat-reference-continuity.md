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
base_sha: 088b46638ac014cd7928d6b0b75cee44902fe22c
head_sha: 21eddf2033857cfdc8149802d7f5870278e39b7f
final_head_sha: null
final_head_frozen_at: null
owner: DOMAIN ARCHITECTURE DESIGN AGENT / Agent A worker
created_at: 2026-08-15T00:20:22+02:00
updated_at: 2026-08-15T00:22:19+02:00
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
  - issue #259 and coordinator activation comments
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

Produce a bounded evidence package for exactly the four registered `ABILITY_COMBAT` Reference cases in issue #259. Promotion requires admissible evidence that captures or bridges `global-tibia-observable-2026-07-28-post-server-save` and satisfies provenance/legal requirements; otherwise the cases remain fail-closed `UNKNOWN / PENDING`.

## Architecture and source of truth

- **PROVEN:** coordinator comment on issue #259 activated this worker lane from reviewed orchestration base `088b46638ac014cd7928d6b0b75cee44902fe22c` and requires work to start from this branch/trusted base.
- **PROVEN:** live `main@cb98fd32a2bb71fce83234ebf8bf69bdd1a1970e` has exactly that worker base as its parent; the later #267 commit is orchestration lifecycle closeout and explicitly preserves the activated A-F lanes unchanged.
- **PROVEN:** the accepted continuity contract requires evidence from the 2026-07-28 boundary for post-target observations and says patch-note/search absence is not continuity proof; provenance other than `CLEARED` blocks promotion.
- **PROVEN:** manifest revision 3 contains exactly the four scoped cases from PR #255. Each is target `UNKNOWN`, Oteryn `NOT_STARTED`, parity `PARITY_PENDING_EVIDENCE`, with source/case provenance and legal review `PENDING`.
- **PROVEN RESEARCH:** official Tibia search-index surfaces still show the expected Light Healing and Ice Strike metadata/descriptions, but direct opens of both exact Library locators still return HTTP 403 in the research environment.
- **PROVEN RESEARCH:** an indexed official Tibia spell-list surface reports both spells and basic metadata with an approximate three-week crawl age, but no exact crawl timestamp is exposed; this does not time-lock the evidence to the 2026-07-28 boundary.
- **PROVEN RESEARCH:** official July 27/28 news establishes the maintenance/change boundary and lists July 28 changes, but absence of these two spells from that change list is forbidden as continuity proof.
- **UNKNOWN:** no admissible provenance-cleared, exact-time capture or chain that directly crosses the target boundary has yet been found.

## Acceptance criteria

- [ ] Preflight evidence table records exact target cases, current classes and unresolved blockers before research.
- [ ] Research remains bounded to the four issue #259 cases and records source, locator, timing relation, provenance, uncertainty and conflicts.
- [ ] Every case receives explicit promote/reject reasoning; insufficient evidence remains `UNKNOWN`.
- [ ] No patch-note/search silence, OTS/community evidence or unverified later behavior is treated as independent target-continuity proof.
- [ ] Manifest/fixture/contract changes occur only if evidence materially changes classification/provenance or reveals a necessary contract clarification.
- [x] No runtime/client/protocol/DDL/Platform/production or external-repository write has been performed; no proprietary code/assets have been used.
- [ ] Governance validation and applicable JSON/schema checks are recorded for the exact final PR head.
- [ ] Full-diff self-review is clean and draft PR is ready for coordinator audit without merge/lifecycle closeout.

## Excluded scope

No mechanic-inventory expansion; no formulas/range/legality discovery beyond the four registered case boundaries; no runtime/client/server/protocol/persistence/content implementation; no DDL, Platform or production authority; no external-repository writes; no proprietary/restricted evidence; no issue close, task archive, merge, auto-merge or lifecycle publication.

## Implementation / findings

The initial task checkpoint contained two incorrect full SHAs copied from a truncated preflight summary. Direct GitHub branch inspection and the coordinator activation comment established the authoritative worker base and live-main SHA above; this checkpoint repairs that bookkeeping error. No branch force-move was performed.

Current research supports a fail-closed direction: indexed official content is useful corroboration, but direct official-page fetch remains blocked and no exact-time capture bridges the immutable cut. Final decision awaits completion of the bounded source matrix and self-review.

## Validation

### Focused

- command/run: pending
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` unless machine manifest content changes; paper-only evidence package
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
- material findings: initial SHA bookkeeping error repaired; final review pending
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
- related/superseded PRs: PR #255 is accepted predecessor evidence package
- protected auto-merge: FORBIDDEN BY ISSUE #259 / user instruction
- merge commit/result: NOT PERFORMED
- ownership release: NOT PERFORMED; lifecycle closeout explicitly excluded

## Context checkpoint

```yaml
last_progress: worker-base bookkeeping repaired; bounded public-source research shows no admissible exact-time continuity chain yet
status: investigating
branch: docs/arch-a-reference-continuity
head_sha: 21eddf2033857cfdc8149802d7f5870278e39b7f
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
next_action: finish four-case source/classification matrix and persist bounded evidence artifact
```
