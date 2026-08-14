# OTV2-20260814-ability-combat-first-evidence-fixtures

```yaml
task_id: OTV2-20260814-ability-combat-first-evidence-fixtures
title: Add first ABILITY_COMBAT evidence cases and fixture specs
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/ability-combat-first-evidence-fixtures
pr: 255
base_sha: 996da4270beadc548781fb81e95ea342e84b6376
head_sha: cb6751eaf3edfad4892caf76a54c2c719ab77353
final_head_sha: null
final_head_frozen_at: null
owner: architecture continuation agent
created_at: 2026-08-14T12:47:53+02:00
updated_at: 2026-08-14T12:58:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260814-ability-combat-first-evidence-fixtures.md
  - docs/agents/evidence/OTV2-20260814-ability-combat-official-spell-library.md
  - docs/contracts/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1.json
  - docs/architecture/GAME-ABILITY-01_FIRST_REFERENCE_EVIDENCE_FIXTURE_PACKAGE.md
public_contracts:
  - docs/contracts/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1.json
  - docs/architecture/GAME-ABILITY-01_FIRST_REFERENCE_EVIDENCE_FIXTURE_PACKAGE.md
depends_on:
  - docs/architecture/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1_OWNER_ACCEPTANCE.md
  - docs/contracts/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1.schema.json
  - docs/architecture/GAME-ABILITY-01_REFERENCE_MECHANIC_CATALOGUE_ENTRY_PARITY_FIXTURE_CONTRACT.md
  - docs/architecture/GAME-ABILITY-01_EFFECT_FAMILIES_REFERENCE_CATALOGUE_OWNER_BASELINE.md
blocks:
  - target-continuity evidence for the first representative ABILITY_COMBAT cases
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Register the first bounded representative `ABILITY_COMBAT` target-case shapes for Light Healing and Ice Strike, plus non-executable pending fixture blueprints, while proving that current post-boundary official state cannot be promoted into the immutable 2026-07-28 target without continuity evidence.

## Architecture and source of truth

- **PROVEN:** `main@996da4270beadc548781fb81e95ea342e84b6376` has accepted/pinned/lifecycle-closed Reference manifest v1 revision 2 with `cases=[]` and `ABILITY_COMBAT=NO_MECHANIC_CASES_REGISTERED`.
- **PROVEN:** `REFERENCE_EVIDENCE_PARITY_MANIFEST_CONTRACT.md` requires post-target observations to remain `UNKNOWN` for the immutable target unless admissible continuity evidence bridges the target cut; patch-note/search absence is not continuity evidence.
- **PROVEN:** GAME-ABILITY partial baselines require typed targeting/legality, explicit commit/cost/cooldown anchors, distinct healing/damage semantics and catalogue-local evidence/fixture bindings.
- **CURRENT OFFICIAL OBSERVATION / DISCOVERY ONLY:** Tibia's current Library pages expose Light Healing and Ice Strike metadata/qualitative descriptions, but were retrieved after the 2026-07-28 boundary.
- **UNKNOWN FOR TARGET:** continuity of every current observed field/description to the 2026-07-28 cut, plus exact heal magnitude, damage formula, exact range, complete legality, mitigation/resistance and RNG semantics.
- **PROVEN:** Oteryn GAME-ABILITY runtime implementation remains `NOT_STARTED`; no passing parity fixture is available.

## Acceptance criteria

- [x] Evidence capture contains only bounded paraphrased official-public current-state observations, locators and explicit continuity uncertainty; no proprietary assets/code.
- [x] Manifest increments to revision 3, changes only `ABILITY_COMBAT` inventory plus bounded cases/history, and preserves the immutable target/policy/normative-contract envelope.
- [x] Every new target case is `UNKNOWN`, Oteryn `NOT_STARTED`, parity `PARITY_PENDING_EVIDENCE`, with legal review `PENDING`, no exact Oteryn revision and no fixture/test link.
- [x] Manifest source timestamps use RFC3339 UTC and current-state confidence is not presented as historical target confidence.
- [x] No case claims target-cut heal/damage metadata, magnitude, exact range, complete legality, resistance or RNG behavior.
- [x] Human-readable package separates current official observation from target truth and defines pending fixture blueprints without calling them passing/executable parity fixtures.
- [x] `FOUNDATION_PROGRAMME_CURRENT_STATUS.md` remains untouched in delivery because its currently selected action is this active package; lifecycle closeout will advance the canonical next action to target-continuity evidence.
- [ ] Complete final exact-head full-diff self-review, schema-shape audit, repository validation and lifecycle closeout.

## Excluded scope

No target classification above `UNKNOWN`; no runtime/client/protocol implementation; no physical catalogue schema/serializer/runner; no exact combat formulas or RNG; no DDL/Platform/production/external-repository writes; no new stable gate ID; no Codex/OpenAI/owner-funded AI use without separate exact authorization.

## Implementation / findings

Issue #254 / draft PR #255 own this bounded evidence package. Light Healing exercises the healing/self catalogue shape and Ice Strike the targeted attack/damage shape, but no immutable-target behavior is asserted from the current web pages alone.

**Material self-review finding 1 — repaired:** the initial package incorrectly classified post-boundary current official observations as target `OBSERVED`. Owning manifest continuity policy requires `UNKNOWN` without continuity evidence. The evidence capture, manifest revision 3, catalogue package and issue/PR metadata were repaired to separate current-state observation from immutable-target truth. `retrieved_at` values were also normalized to UTC `Z` timestamps.

The repair changes the recommended next evidence action: prove the target-continuity path for these four representative cases before broadening mechanic inventory or freezing physical catalogue tooling.

## Validation

### Focused

- manifest JSON construction/parse: **PASS**.
- fail-closed invariant audit: **PASS** — 4 unique cases; all target `UNKNOWN`; all Oteryn `NOT_STARTED`; all parity `PARITY_PENDING_EVIDENCE`; all exact revisions null; all fixture/test links empty; all legal-review states `PENDING`; no `PARITY_CONFIRMED`.
- inventory audit: **PASS** — only `ABILITY_COMBAT` changes to `MECHANIC_CASES_REGISTERED`; other domain coverage remains unchanged.
- continuity policy audit: **PASS after repair** — post-boundary current observations are discovery/current-state evidence only and cannot promote target evidence.
- source timestamp audit: **PASS after repair** — manifest retrieval timestamps are UTC RFC3339.
- accepted schema-shape compatibility: pending final manual audit against unchanged schema v1.

### Component/integration

- command/run: `NOT_APPLICABLE` — paper-only evidence/architecture package.
- result: `NOT_APPLICABLE`.

### E2E

- scenario: `NOT_APPLICABLE` — no executable gameplay behavior.
- result: `NOT_APPLICABLE`.

### Exact-head CI

- final head: pending after this task checkpoint commit.
- trigger source: pull_request.
- workflow/run/job: pending.
- runner assignment: pending.
- classification: pending.
- result: pending.

## Self-review

- superseded content head: `cb6751eaf3edfad4892caf76a54c2c719ab77353`.
- method/reviewer: implementing/coordinating architecture continuation agent.
- material findings: 1 evidence-classification/continuity finding; repaired across evidence/manifest/catalogue/metadata.
- verdict: pending final resulting-head full-diff recheck.

## Independent review

- required: NO unless a later material finding/risk expansion changes classification; this is paper-only public-evidence registration with no executable/security/durable-value authority.
- exact head: NOT_APPLICABLE.
- method/auditor: NOT_APPLICABLE.
- material findings: NOT_APPLICABLE.
- verdict: NOT_APPLICABLE.
- owner-funded AI: **NOT AUTHORIZED** for PR #255; prior authorizations do not carry forward.

## PR and closeout

- PR: #255 (draft).
- changed-file review: pending final resulting-head recheck; intended paths = 4.
- unresolved review threads: pending readback.
- related/superseded PRs: #239/#240 Dependabot and #191 GAME-CHAR are disjoint.
- protected auto-merge: pending.
- merge commit/result: pending.
- ownership release: pending.

## Context checkpoint

```yaml
last_progress: Repaired the first representative ABILITY_COMBAT package to keep all immutable-target cases UNKNOWN until continuity evidence bridges the 2026-07-28 cut; current official Library data is discovery/current-state evidence only.
status: validating
branch: docs/ability-combat-first-evidence-fixtures
head_sha: cb6751eaf3edfad4892caf76a54c2c719ab77353
pr: 255
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: pull_request
ci_check_generation: fresh resulting head required
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
owner_action_required: false
blocker: null
next_action: Perform final four-path diff/schema/review-thread audit on the resulting PR #255 head and inspect fresh exact-head repository gates without marking the PR ready.
```
