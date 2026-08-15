# OTV2-20260815-tibia-reference-harvest

```yaml
task_id: OTV2-20260815-tibia-reference-harvest
title: Harvest canonical Tibia reference worldmap tooling
mode: MIGRATE
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: tools/OTV2-20260815-tibia-reference-harvest
pr: null
base_sha: 0cfd8d8ee3ecf4fbb1cb76cbc9680b53a152e3c1
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: chatgpt-github
created_at: 2026-08-15T23:24:00+02:00
updated_at: 2026-08-15T23:24:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260815-tibia-reference-harvest.md
  - docs/agents/evidence/OTV2-20260815-tibia-reference-harvest.md
  - tools/tibia-worldmap-reconstruction/**
  - .github/workflows/tibia-reference-tools.yml
public_contracts: []
depends_on:
  - blakinio/Oteryn-Platform#1006
  - blakinio/Oteryn-Platform#988
  - ADR-0002 repository ownership and native Rust client migration
blocks: []
cross_repository_coordination_id: OTER-CLIENT-REFERENCE-HARVEST-20260815
external_repositories:
  - blakinio/Oteryn-Platform
```

## Outcome

Move the durable, proprietary-data-free worldmap normalization/comparison tool and the client/game semantic handoff from stale Platform research into the canonical native game/client repository, without importing Platform runner orchestration, credentials, screenshots, official binaries, or live-client control scaffolding.

## Architecture and source of truth

- **PROVEN:** `docs/architecture/ADR-0002-repository-ownership-and-client-migration.md` makes `blakinio/Oteryn-v2` canonical for the native Rust client/server/protocol and makes `blakinio/otclient` historical migration/reference evidence.
- **PROVEN:** Platform ADR 0041 assigns native Client, Game Server, `protocol-oteryn`, native game E2E mechanics, world/content tooling and bounded OTBM migration semantics to the Oteryn-Game lineage, whose current source lineage is `blakinio/Oteryn-v2`.
- **PROVEN:** Platform PR #1006 head `97f8df9e64e1e4f0520440073e497f24dad929ef` contains a proprietary-data-free `tools/tibia-worldmap-reconstruction/**` package with deterministic validation, merge, comparison and fail-closed OTBM export planning.
- **PROVEN:** Platform PR #988 head `f9ff34b37cf81c400a48f7ab9329393416ac304d` is an official-client offline/reference infrastructure task; its game/client conclusions belong here, while its host/isolation harness remains a Platform infrastructure concern.
- **DERIVED:** `blakinio/otclient` is not an eligible target for new harvested work after the accepted cutover.

## Acceptance criteria

- [x] Source ownership is reconciled against current Oteryn-v2 and Platform architecture authority.
- [x] The six safe worldmap reconstruction files are copied from Platform PR #1006 without proprietary assets or live-client material.
- [x] Durable evidence records what was and was not migrated from PRs #1006 and #988.
- [x] No Platform-specific GitHub runner workflow, credential path, login automation, VNC path, gdb/ptrace workflow, private-message action, screenshot/base64 evidence or proprietary binary is migrated.
- [ ] Focused Python compile/unit/example validation passes on the exact PR head.
- [ ] Oteryn-v2 merge-gate/governance/CodeQL checks pass on the exact PR head.
- [ ] Whole-diff self-review finds no material ownership, provenance or safety defect.
- [ ] Merge and task closeout are terminal before the Platform source research PRs are closed/deleted.

## Excluded scope

- No official Tibia client execution, login, account/session data, gameplay automation or live research.
- No BattlEye modification/bypass, hooking, injection, ptrace/debugging or network interception.
- No implementation of `protocol-oteryn`, native runtime, OTBM binary writer or client/server behavior.
- No change to `apps/client/**` in this migration.
- No attempt to prove exact player XYZ, tile passability or collision-aware navigation; those remain separate future research questions.

## Implementation / findings

The migrated worldmap tool remains fail-closed: unobserved data is distinct from empty data, unknown client-to-server ID mappings remain `UNMAPPED`, and the OTBM export plan refuses readiness when observed static data lacks proven mapping or ground identity.

The current Platform-side official Linux reference harness is not copied by this task. It is classified as infrastructure/reference execution tooling rather than native product code. Only its durable client/game findings are recorded in the evidence document.

## Validation

### Focused

- command/run: `.github/workflows/tibia-reference-tools.yml`
- result: pending exact-head run

### Component/integration

- command/run: deterministic synthetic worldmap validation only
- result: pending exact-head run

### E2E

- scenario: `NOT_APPLICABLE` — this migration does not execute a user/runtime journey; it relocates a deterministic offline reference tool with synthetic fixtures only.
- result: NOT_APPLICABLE

### Exact-head CI

- final head: pending
- trigger source: pull_request
- workflow/run/job: pending
- runner assignment: GitHub-hosted
- classification: migration/reference-tooling
- result: pending

## Self-review

- exact head: pending
- method/reviewer: implementing/coordinating agent
- material findings: pending
- verdict: pending

## Independent review

- required: NO — bounded migration of proprietary-data-free Python tooling and evidence; no runtime, protocol, credential, DDL or production behavior changes.
- exact head: NOT_APPLICABLE
- method/auditor: NOT_APPLICABLE
- material findings: NOT_APPLICABLE
- verdict: NOT_APPLICABLE

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: Platform #1006 and #988 remain open until destination/Platform harvest is merged
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: ownership audit completed and clean migration package prepared
status: validating
branch: tools/OTV2-20260815-tibia-reference-harvest
head_sha: null
pr: null
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: pull_request
ci_check_generation: initial
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
next_action: Create the destination PR, run the focused reference-tool validation and repository merge gate, then merge before closing the Platform source research PRs.
```
