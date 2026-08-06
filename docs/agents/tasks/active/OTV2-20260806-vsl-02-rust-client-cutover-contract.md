# OTV2-20260806-vsl-02-rust-client-cutover-contract

```yaml
task_id: OTV2-20260806-vsl-02-rust-client-cutover-contract
title: Define exact Rust client migration and cutover contract
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/vsl-02-rust-client-cutover-contract
pr: null
base_sha: 9034bd4bfa491eac6a898b29bc8151c94a4c2b89
head_sha: null
owner: GPT-5.6-Thinking-architecture-coordinator
created_at: 2026-08-06T09:50:00+02:00
updated_at: 2026-08-06T09:50:00+02:00
execution_budget_minutes: 120
large_budget_reason: VSL-02 must pin the exact source revision, reconcile source drift/PRs/tasks, define file/path/provenance/dependency mapping, one atomic destination PR, source freeze/marker sequencing, validation and rollback across two repositories.
owned_paths:
  - docs/migration/VSL-02_RUST_CLIENT_MIGRATION_AND_CUTOVER_CONTRACT.md
  - docs/migration/VSL-02_SOURCE_RECONCILIATION.md
  - docs/migration/rust-client-path-map.json
  - docs/migration/rust-client-provenance-plan.json
  - docs/agents/tasks/active/OTV2-20260806-vsl-02-rust-client-cutover-contract.md
public_contracts:
  - docs/migration/VSL-02_RUST_CLIENT_MIGRATION_AND_CUTOVER_CONTRACT.md
  - docs/migration/rust-client-path-map.json
  - docs/migration/rust-client-provenance-plan.json
depends_on:
  - FND-01 accepted at 3e11cf36ffdc1191fabd60c09e8da9818594e189
  - ADR-0002
  - ADR-0008
  - ADR-0011
blocks:
  - the one atomic destination Rust-client migration/workspace PR
  - FND-ID-01
  - FND-02
  - FND-03
  - FND-04
cross_repository_coordination_id: OTV2-RUST-CLIENT-CUTOVER-20260806
external_repositories:
  - blakinio/otclient (read-only source evidence; later marker PR requires separate authorized task)
```

## Outcome

Deliver an accepted, implementation-ready `VSL-02` contract that pins the exact Rust-client source revision and determines the complete destination import, transformation, provenance, dependency, validation, rollout, freeze, source-marker and rollback procedure without moving code in this task.

## Architecture and source of truth

### PROVEN

- Destination `main` at task start is `9034bd4bfa491eac6a898b29bc8151c94a4c2b89`.
- FND-01 is accepted and archived; the 19-member initial workspace and source-member dispositions are canonical.
- Source `blakinio/otclient:main` still equals the FND-01 inventory revision `c923ad8a1dff17b4933a6110931b0823cec2c590`.
- Source Rust root manifest blob is `037013e8e4a762a65f0f2a30f7761ee14725a3fc`; root lockfile blob is `2143408c12c50132883890f0821278320a331fde`.
- Source has no open PR changing `oteryn-client/**`.
- Open source PRs #23, #48 and #97 belong to legacy C++/Lua UI, operational package analysis and legacy asset-install security respectively.
- Six source active-task records are stale/historical; the only Rust-specific active record owns `protocol-canary`, which is reference-only under ADR-0008.

### DERIVED / TO BE FROZEN BY THIS CONTRACT

- The exact cutover source commit can be pinned to `c923ad8a1dff17b4933a6110931b0823cec2c590` with no source-drift reconciliation delta.
- One atomic destination implementation PR can create the root workspace and apply every FND-01 disposition without retaining Canary or an empty native-protocol crate.
- Cross-repository ancestry must be represented by immutable provenance manifests rather than a false Git-history claim.
- The source marker must occur only after verified destination merge and must not affect legacy C++/Lua lanes.

## Acceptance criteria

- [x] Exact destination and source heads are verified.
- [x] Source drift since FND-01 is determined.
- [x] Every open source PR and active task is classified for cutover.
- [ ] Exact source-to-destination path map is complete and machine-readable.
- [ ] Provenance and history policy is complete and machine-readable.
- [ ] Exact dependency delta, including async HTTP/TLS selection, is fixed.
- [ ] Atomic destination PR contents, branch, validation and equivalence evidence are fixed.
- [ ] Source freeze and later source-marker paths/order are fixed.
- [ ] Forward rollout and rollback orders prevent zero or dual canonical ownership.
- [ ] Independent audit reports zero open material findings.
- [ ] Exact-head governance, Dependency Review and CodeQL pass.
- [ ] Contract PR is squash-merged and task archived.

## Excluded scope

- No Rust source code or Cargo workspace is created in this task.
- No write is made to `blakinio/otclient`.
- No source marker, source task archival or source freeze enforcement is implemented yet.
- No `protocol-oteryn`, server runtime, admission, persistence, content or Studio code is introduced.
- No production deployment or live Identity/Game Gateway call is performed.

## Implementation / findings

In progress:

- exact source reconciliation;
- open PR and active task classification;
- path/provenance manifests;
- dependency selection and release-closure policy;
- atomic migration, source-marker and rollback contract.

## Validation

### Focused

- command/run: exact source/destination head checks; open PR/task review; JSON schema/syntax validation; full contract consistency review
- result: in progress

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture/migration-contract task only
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no executable migration occurs in this task
- result: `NOT_APPLICABLE`

### Exact-head CI

- head: pending final contract head
- workflow/run: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: adversarial audit against FND-01, ADR-0002, ADR-0008, ADR-0011, source live state, cross-repository ordering, provenance truthfulness and rollback safety
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related PRs: source #23, #48 and #97 classified but not modified; destination #38 unrelated lifecycle cleanup
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: VSL-02 task claimed after proving source main still equals the accepted FND-01 inventory revision and no open Rust-client PR exists.
status: implementing
branch: docs/vsl-02-rust-client-cutover-contract
head_sha: null
pr: null
ci_check_generation: null
ci_checks_for_current_head: 0
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 0
stall_warnings: 0
blocker: null
next_action: Persist the exact path/provenance manifests and complete the migration/cutover contract.
```
