# OTV2-20260814-reference-evidence-manifest-v1-acceptance

```yaml
task_id: OTV2-20260814-reference-evidence-manifest-v1-acceptance
title: Accept and pin Reference evidence/parity manifest v1
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/reference-evidence-manifest-v1-acceptance
pr: null
base_sha: 76d65d8bbd2a8eaca46b671fcd5d71a9d6382fa3
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: architecture continuation agent
created_at: 2026-08-14T10:15:00+02:00
updated_at: 2026-08-14T10:15:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260814-reference-evidence-manifest-v1-acceptance.md
  - docs/architecture/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1_OWNER_ACCEPTANCE.md
  - docs/contracts/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1.json
public_contracts:
  - docs/architecture/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1_OWNER_ACCEPTANCE.md
  - docs/contracts/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1.json
depends_on:
  - docs/architecture/GAME-VISION-01_FIRST_REFERENCE_BASELINE_OWNER_BASELINE.md
  - docs/architecture/REFERENCE_EVIDENCE_PARITY_MANIFEST_CONTRACT.md
  - docs/contracts/REFERENCE_EVIDENCE_PARITY_MANIFEST_V1.schema.json
  - docs/architecture/GAME-ABILITY-01_REFERENCE_MECHANIC_CATALOGUE_ENTRY_PARITY_FIXTURE_CONTRACT.md
blocks:
  - reviewed mechanic-level Reference evidence/parity population
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Promote the already-delivered v1 Reference evidence/parity registry to an owner-accepted semantic pin without rewriting the historical candidate contract, changing schema v1, adding mechanic cases or authorizing executable work.

## Architecture and source of truth

- **PROVEN:** PR #220/#221 delivered and lifecycle-closed the candidate manifest/schema package; current schema blob is `208506f461231eb3ed8966ae16dade0764eb39b8`.
- **PROVEN:** the current machine manifest is revision 1 with `status=CANDIDATE_NOT_ACCEPTED`, empty `cases`, all nine domains `NO_MECHANIC_CASES_REGISTERED`, and `canonical_digest=null`.
- **PROVEN:** PR #249/#250 added the catalogue-entry/parity-fixture contract and explicitly blocks trustworthy parity promotion until an accepted manifest/schema revision is pinned.
- **DERIVED:** preserving the candidate contract as history and adding a later owner-acceptance baseline is safer than editing historical candidate status prose in place.
- **UNKNOWN:** no mechanic-level Reference behavior is promoted by this task.
- **CONFLICT:** none introduced by this task; PR #191 remains separate GAME-CHAR provenance work.

## Acceptance criteria

- [ ] Preserve the immutable first Reference target ID and 2026-07-28 boundary.
- [ ] Keep schema version 1 byte-for-byte unchanged and record its exact repository blob identity.
- [ ] Promote the machine manifest to revision 2 with `status=ACCEPTED`.
- [ ] Keep `cases` empty and every domain coverage entry fail-closed.
- [ ] Preserve independent evidence / implementation / parity axes and all existing fail-closed policy flags.
- [ ] Keep `canonical_digest=null` truthful until accepted digest tooling exists; do not hand-compute a digest.
- [ ] Add an explicit acceptance/pin contract that supersedes only candidate-status/pinning clauses, not evidence semantics.
- [ ] Do not create a new stable architecture gate ID.
- [ ] Do not authorize runtime/client/protocol/DDL/Platform/production/external-repository work.
- [ ] Run full-diff self-review, exact-head repository validation and close the linked issue/lifecycle only after merge.

## Excluded scope

No mechanic cases or factual parity promotions; no evidence acquisition/official-client automation; no runtime/client/server/protocol implementation; no persistence/DDL/migrations; no Platform/external-repository writes; no production changes; no proprietary assets/code/protocol acquisition; no canonical digest tooling; no new stable gate ID.

## Implementation / findings

Issue #251 owns this acceptance promotion. Schema v1 is intentionally not edited. The acceptance pin will use the immutable target ID, `schema_version=1`, `manifest_revision=2`, `status=ACCEPTED` and the exact unchanged schema blob identity. Until canonical digest tooling is accepted, executable consumers remain unauthorized and paper consumers must additionally bind exact repository revision/evidence.

## Validation

### Focused

- manifest JSON parse: pending
- schema-shape compatibility review: pending
- acceptance pin invariants: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — paper-only contract/registry promotion
- result: pending

### E2E

- scenario: `NOT_APPLICABLE` — no executable behavior changes
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

- required: NO unless a later material finding or risk expansion changes classification; this is paper-only status/pinning with no security/protocol/durable mutation/production authority expansion
- exact head: NOT_APPLICABLE
- method/auditor: NOT_APPLICABLE
- material findings: NOT_APPLICABLE
- verdict: NOT_APPLICABLE
- owner-funded Codex/OpenAI use: NOT AUTHORIZED for this PR/task

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: #220/#221 historical candidate delivery; #249/#250 downstream catalogue contract; #191 separate and untouched
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Claimed bounded acceptance task from main@76d65d8bbd2a8eaca46b671fcd5d71a9d6382fa3 after verifying candidate delivery history and downstream catalogue dependency.
status: implementing
branch: docs/reference-evidence-manifest-v1-acceptance
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
next_action: Add the owner-acceptance baseline and promote the machine manifest to accepted revision 2 without changing schema v1.
```
