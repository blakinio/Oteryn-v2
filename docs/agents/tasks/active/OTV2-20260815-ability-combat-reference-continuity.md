# OTV2-20260815-ability-combat-reference-continuity

```yaml
task_id: OTV2-20260815-ability-combat-reference-continuity
title: Build target-continuity and provenance-clearance evidence package for first ABILITY_COMBAT cases
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/arch-a-reference-continuity
pr: null
base_sha: 088b46638ac014cd7928d6b0b75cee44902fe22c
head_sha: 174c2fe8056fcb3b36ab82cd2451349fa886bdb1
final_head_sha: null
final_head_frozen_at: null
owner: DOMAIN ARCHITECTURE DESIGN AGENT / Agent A worker
created_at: 2026-08-15T00:20:22+02:00
updated_at: 2026-08-15T00:27:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260815-ability-combat-reference-continuity.md
  - docs/agents/evidence/OTV2-20260815-ability-combat-reference-continuity.md
public_contracts: []
depends_on:
  - issue #259 and coordinator activation comments
  - docs/agents/prompts/OTV2_DOMAIN_ARCHITECTURE_DESIGN_AGENT.md
  - docs/agents/programs/OTERYN_V2_ARCHITECTURE_PARALLEL_WORK_ALLOCATION.md
  - docs/architecture/GAME-VISION-01_FIRST_REFERENCE_BASELINE_OWNER_BASELINE.md
  - docs/architecture/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1_OWNER_ACCEPTANCE.md
  - docs/architecture/REFERENCE_EVIDENCE_PARITY_MANIFEST_CONTRACT.md
  - docs/contracts/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1.schema.json
  - docs/contracts/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1.json
  - docs/architecture/GAME-ABILITY-01_FIRST_REFERENCE_EVIDENCE_FIXTURE_PACKAGE.md
  - PR #255 / merge d04f0939f0078cb677ca3ad66f5949e9f3dadc8d
blocks:
  - coordinator audit of Agent A continuity/provenance evidence package
cross_repository_coordination_id: OTV2-ARCH-PARALLEL-20260814
external_repositories: []
```

## Outcome

Deliver a bounded evidence package for exactly the four registered `ABILITY_COMBAT` Reference cases in issue #259. Promotion requires admissible evidence that captures or bridges `global-tibia-observable-2026-07-28-post-server-save` and satisfies provenance/legal requirements; insufficient evidence remains fail-closed `UNKNOWN / PENDING`.

**Research outcome: `INSUFFICIENT_FOR_PROMOTION`; 0/4 cases promoted.**

## Architecture and source of truth

- **PROVEN:** coordinator comment on issue #259 activated this worker lane from reviewed orchestration base `088b46638ac014cd7928d6b0b75cee44902fe22c` and requires work to start from this branch/trusted base.
- **PROVEN:** live `main@cb98fd32a2bb71fce83234ebf8bf69bdd1a1970e` has exactly that worker base as its parent; the later #267 commit is orchestration lifecycle closeout and explicitly preserves the activated A-F lanes unchanged.
- **PROVEN:** the accepted continuity contract requires evidence from the 2026-07-28 boundary for post-target observations and says patch-note/search absence is not continuity proof; provenance other than `CLEARED` blocks promotion.
- **PROVEN:** manifest revision 3 contains exactly the four scoped cases from PR #255. Each is target `UNKNOWN`, Oteryn `NOT_STARTED`, parity `PARITY_PENDING_EVIDENCE`, with source/case provenance and legal review `PENDING`.
- **PROVEN RESEARCH:** official Tibia search-index surfaces still show the expected Light Healing and Ice Strike metadata/descriptions, but direct opens of both exact Library locators return HTTP 403 in the research environment.
- **PROVEN RESEARCH:** an indexed official Tibia aggregate spell-list surface reports both spells and basic metadata with an approximate three-week crawl age, but no exact crawl timestamp is exposed; it does not time-lock the evidence to the 2026-07-28 boundary.
- **PROVEN RESEARCH:** official July 27/28 news establishes the maintenance/change boundary and describes selected July 28 changes, but absence of these two spells is forbidden as continuity proof. An official delayed Echo Raid disclosure also demonstrates why publication silence is not a reliable no-change oracle.
- **UNKNOWN:** a provenance-cleared exact-time capture or affirmative evidence chain that directly crosses the target boundary may exist elsewhere, but bounded research in this task did not obtain one.

## Acceptance criteria

- [x] Preflight evidence table records all four target cases and their current `UNKNOWN / PENDING` blockers.
- [x] Research is bounded to the four issue #259 cases and records exact official locators, retrieval mode, relative timing, target relation, provenance limitations, uncertainty and conflict handling in `docs/agents/evidence/OTV2-20260815-ability-combat-reference-continuity.md`.
- [x] Every case has explicit promotion rejection reasoning; all four retain `UNKNOWN`, provenance/legal `PENDING` and `PARITY_PENDING_EVIDENCE`.
- [x] Patch-note/search silence, approximate crawl ages, community documentation, OTS similarity and implementation convenience are explicitly rejected as independent continuity proof.
- [x] Conditional manifest/fixture changes were not made because evidence does not change an existing classification or provenance state; no contract defect requiring clarification was found.
- [x] No runtime/client/protocol/DDL/Platform/production or external-repository write was performed; no proprietary code/assets or restricted material were used.
- [ ] Exact-head repository governance/PR checks are recorded after draft PR creation.
- [ ] Exact-head full-diff self-review is clean and the draft PR is ready for coordinator audit.

## Excluded scope

No mechanic-inventory expansion; no formulas/range/legality discovery beyond the four registered case boundaries; no runtime/client/server/protocol/persistence/content implementation; no DDL, Platform or production authority; no external-repository writes; no proprietary/restricted evidence; no coordinator-owned overlay edits; no issue close, task archive, merge, auto-merge or lifecycle publication.

## Implementation / findings

### Evidence result

The persisted source matrix and four-case analysis are in `docs/agents/evidence/OTV2-20260815-ability-combat-reference-continuity.md`.

The research found official-domain corroboration but not admissible continuity/provenance clearance:

- exact Light Healing and Ice Strike Library locators remain search-index readable, while direct opens return HTTP 403;
- their index freshness is only approximate (`2 weeks`), with no exact timestamp;
- an aggregate official spell list containing both mechanics has only approximate `3 weeks` crawl age and incomplete case-aspect coverage;
- July 27/28 official news establishes the maintenance/change boundary but cannot prove continuity through omission;
- the accepted project baseline is independently supported by an official July 20 delayed-disclosure example for a July 16 Echo Raid change.

Therefore the correct evidence action is **rejection of promotion**, not a manifest update.

### Self-repair findings

1. The initial task checkpoint contained incorrect full SHAs copied from a truncated preflight summary. Direct GitHub branch inspection repaired them to worker base `088b46638ac014cd7928d6b0b75cee44902fe22c` and live main `cb98fd32a2bb71fce83234ebf8bf69bdd1a1970e`.
2. Preflight initially treated the later main lifecycle commit as a stale-branch problem. Coordinator issue comments prove the worker lane was intentionally activated from `088b46638...`; no force-move occurred and no further branch-sync attempt is warranted.
3. The initial task record over-declared `REFERENCE_EVIDENCE_PARITY_MANIFEST_CONTRACT.md` as an owned path. Agent A does not own that contract. Ownership is corrected to the task record and new evidence artifact only; manifest/package are dependencies and remain unchanged.

## Validation

### Focused

- source/case matrix completeness: **PASS** — four registered cases, source timing/provenance and explicit promotion decisions are present.
- classification discipline: **PASS** — 0/4 promoted; all remain `UNKNOWN / PENDING`.
- scope audit: **PASS** — no fifth mechanic/case and no runtime/conditional-contract edit.
- manifest/schema mutation check: **NOT_APPLICABLE** — `docs/contracts/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1.json` and its schema are unchanged from the trusted base; no new JSON payload exists to validate.

### Component/integration

- command/run: `NOT_APPLICABLE` — paper-only evidence artifact and task bookkeeping; no machine contract/runtime component changed.
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no executable behavior or runtime authority.
- result: `NOT_APPLICABLE`

### Exact-head CI

- final head: pending after final PR/task metadata commit
- trigger source: draft PR
- workflow/run/job: pending
- runner assignment: pending
- classification: governance/documentation gates only
- result: pending

## Self-review

- exact head: pending after final PR/task metadata commit
- method/reviewer: DOMAIN ARCHITECTURE DESIGN AGENT / Agent A worker
- material findings: three bookkeeping/ownership findings above repaired; full PR diff review pending
- verdict: pending

## Independent review

- required: YES — issue #259 explicitly requires coordinator audit of the worker draft PR
- exact head: pending
- method/auditor: architecture coordinator after handover
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending draft PR
- unresolved review threads: pending draft PR
- related/superseded PRs: PR #255 is accepted predecessor evidence package
- protected auto-merge: FORBIDDEN BY ISSUE #259 / user instruction
- merge commit/result: NOT PERFORMED
- ownership release: NOT PERFORMED; task remains active for coordinator audit
- lifecycle closeout: NOT PERFORMED / FORBIDDEN FOR THIS WORKER

## Context checkpoint

```yaml
last_progress: bounded continuity/provenance evidence artifact persisted; all four promotion attempts rejected fail closed
status: validating
branch: docs/arch-a-reference-continuity
head_sha: 174c2fe8056fcb3b36ab82cd2451349fa886bdb1
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
next_action: create draft PR and perform exact-head changed-file/governance validation for coordinator audit
```
