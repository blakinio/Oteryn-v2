# OTV2-20260814-ability-combat-first-evidence-fixtures

```yaml
task_id: OTV2-20260814-ability-combat-first-evidence-fixtures
title: Add first ABILITY_COMBAT evidence cases and fixture specs
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/ability-combat-first-evidence-fixtures
pr: null
base_sha: 996da4270beadc548781fb81e95ea342e84b6376
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: architecture continuation agent
created_at: 2026-08-14T12:47:53+02:00
updated_at: 2026-08-14T12:47:53+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260814-ability-combat-first-evidence-fixtures.md
  - docs/agents/evidence/OTV2-20260814-ability-combat-official-spell-library.md
  - docs/contracts/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1.json
  - docs/architecture/GAME-ABILITY-01_FIRST_REFERENCE_EVIDENCE_FIXTURE_PACKAGE.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
public_contracts:
  - docs/contracts/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1.json
  - docs/architecture/GAME-ABILITY-01_FIRST_REFERENCE_EVIDENCE_FIXTURE_PACKAGE.md
depends_on:
  - docs/architecture/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1_OWNER_ACCEPTANCE.md
  - docs/contracts/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1.schema.json
  - docs/architecture/GAME-ABILITY-01_REFERENCE_MECHANIC_CATALOGUE_ENTRY_PARITY_FIXTURE_CONTRACT.md
  - docs/architecture/GAME-ABILITY-01_EFFECT_FAMILIES_REFERENCE_CATALOGUE_OWNER_BASELINE.md
blocks:
  - next representative ABILITY_COMBAT evidence package
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Register the first bounded representative `ABILITY_COMBAT` Reference evidence cases for Light Healing and Ice Strike, plus non-executable pending fixture specifications, without claiming exact target-cut continuity, Oteryn implementation or parity confirmation.

## Architecture and source of truth

- **PROVEN:** `main@996da4270beadc548781fb81e95ea342e84b6376` has accepted/pinned/lifecycle-closed Reference manifest v1 revision 2 with `cases=[]` and `ABILITY_COMBAT=NO_MECHANIC_CASES_REGISTERED`.
- **PROVEN:** GAME-ABILITY partial baselines require typed targeting/legality, explicit commit/cost/cooldown anchors, distinct healing/damage semantics and catalogue-local evidence/fixture bindings.
- **OBSERVED EXTERNAL:** official Tibia Library currently lists Light Healing and Ice Strike metadata and qualitative behavior; these pages were retrieved after the 2026-07-28 boundary, not captured exactly at it.
- **UNKNOWN:** exact 2026-07-28 continuity of every observed field, exact heal magnitude, exact damage formula, exact tile range, full legality, mitigation/resistance and RNG semantics.
- **PROVEN:** Oteryn GAME-ABILITY runtime implementation remains `NOT_STARTED`; no passing parity fixture is available.

## Acceptance criteria

- [ ] Evidence capture contains only bounded paraphrased official-public facts, locators and uncertainty; no proprietary assets/code.
- [ ] Manifest increments revision and changes only `ABILITY_COMBAT` inventory plus new bounded cases/history.
- [ ] Every new case is `OBSERVED`, Oteryn `NOT_STARTED`, parity `PARITY_PENDING_EVIDENCE`, with legal review `PENDING` and explicit exact-cut uncertainty.
- [ ] No case claims exact heal/damage magnitude, exact tile range, complete legality, resistance or RNG behavior.
- [ ] Human-readable package maps only evidenced aspects to existing GAME-ABILITY owners and defines pending fixture specifications without calling them passing/executable parity fixtures.
- [ ] Current-status selects the next bounded paper-only evidence step without authorizing implementation.
- [ ] Full-diff self-review and exact-head repository gates pass before merge.

## Excluded scope

No runtime/client/protocol implementation; no physical catalogue schema/serializer/runner; no exact combat formulas or RNG; no DDL/Platform/production/external-repository writes; no new stable gate ID; no Codex/OpenAI/owner-funded AI use without separate exact authorization.

## Implementation / findings

Issue #254 owns this bounded evidence package. Light Healing exercises healing/self semantics; Ice Strike exercises targeted attack/damage semantics. Current official Library observations are intentionally weaker than a time-locked 2026-07-28 capture and therefore remain `OBSERVED` with explicit uncertainty. Fixture specifications are paper test intents only until an exact Oteryn implementation revision and executable locator exist.

## Validation

### Focused

- manifest JSON/schema compatibility: pending
- evidence/source-to-case field audit: pending
- case fail-closed invariant audit: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — paper-only evidence/architecture package
- result: pending

### E2E

- scenario: `NOT_APPLICABLE` — no executable gameplay behavior
- result: pending

### Exact-head CI

- final head: pending
- trigger source: pull_request
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Self-review

- exact head: pending
- method/reviewer: implementing/coordinating architecture continuation agent
- material findings: pending
- verdict: pending

## Independent review

- required: NO unless a later material finding/risk expansion changes classification; this is paper-only public evidence population with no executable/security/durable-value authority
- exact head: NOT_APPLICABLE
- method/auditor: NOT_APPLICABLE
- material findings: NOT_APPLICABLE
- verdict: NOT_APPLICABLE
- owner-funded AI: NOT AUTHORIZED for this task/PR

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: #239/#240 Dependabot and #191 GAME-CHAR are disjoint
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Claimed issue #254 from main@996da4270beadc548781fb81e95ea342e84b6376 after verifying no overlapping open PR/task ownership.
status: implementing
branch: docs/ability-combat-first-evidence-fixtures
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
owner_action_required: false
blocker: null
next_action: Add bounded official-public evidence capture, manifest cases and the human-readable GAME-ABILITY evidence/fixture package.
```
