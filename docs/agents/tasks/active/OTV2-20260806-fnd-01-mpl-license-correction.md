# OTV2-20260806-fnd-01-mpl-license-correction

```yaml
task_id: OTV2-20260806-fnd-01-mpl-license-correction
title: Correct FND-01 workspace software license to MPL-2.0
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/fnd-01-mpl-license-correction
pr: null
base_sha: 33dc15dab82cfe5347e569036296204763270508
head_sha: null
owner: GPT-5.6-Thinking-architecture-coordinator
created_at: 2026-08-06T12:02:00+02:00
updated_at: 2026-08-06T12:02:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/architecture/FND-01_OWNER_ACCEPTANCE_AND_CRATE_FITNESS_REVIEW.md
  - docs/agents/tasks/active/OTV2-20260806-fnd-01-mpl-license-correction.md
public_contracts:
  - docs/architecture/FND-01_OWNER_ACCEPTANCE_AND_CRATE_FITNESS_REVIEW.md
depends_on:
  - docs/repository/LICENSING.md
  - FND-01
blocks:
  - merge of PR #50 while workspace.package.license remains MIT
cross_repository_coordination_id: OTV2-RUST-CLIENT-CUTOVER-20260806
external_repositories: []
```

## Outcome

Record the product owner's explicit correction that the Oteryn-v2 Rust workspace and newly authored workspace packages use `MPL-2.0`, not `MIT`, while imported material retains any separately applicable compatible license and provenance through explicit file- or component-level notices.

## Architecture and source of truth

### PROVEN

- `docs/repository/LICENSING.md` makes MPL-2.0 the repository default for source code, build tooling, configuration, schemas, tests and technical documentation.
- The accepted FND-01 contract blob contains a conflicting root Cargo policy line: `license = MIT`.
- Draft PR #50 currently carries `workspace.package.license = "MIT"`.
- The product owner explicitly accepted the MPL-2.0 correction on 2026-08-06.

### DERIVED

- The FND-01 MIT line cannot remain authoritative because it conflicts with the earlier repository-wide licensing decision and the owner's explicit correction.
- The correction changes licensing metadata only; it does not reopen the accepted 19-member workspace graph, migration dispositions or dependency boundaries.

## Acceptance criteria

- [ ] The FND-01 owner-acceptance record explicitly supersedes the contract's `license = MIT` line with `MPL-2.0`.
- [ ] The record states that imported material keeps explicit compatible licenses and provenance at file or component scope.
- [ ] The record requires PR #50 to correct Cargo workspace metadata before merge.
- [ ] No Rust code, Cargo manifest, migration implementation or external repository is changed by this package.
- [ ] Full changed-file review and exact-head governance checks pass.

## Excluded scope

- Do not modify PR #50 code or Cargo files in this architecture package.
- Do not change the accepted 19-member workspace, crate dispositions, toolchain, dependency graph or migration order.
- Do not relicense third-party material or creative assets.
- Do not modify external repositories or production systems.

## Implementation / findings

- Owner decision received: Oteryn-v2 workspace default software license is `MPL-2.0`.
- PR #50 must replace `workspace.package.license = "MIT"` with `"MPL-2.0"` before merge.

## Validation

### Focused

- command/run: pending full changed-file review
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — documentation-only contract correction
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no executable product change
- result: `NOT_APPLICABLE`

### Exact-head CI

- head: pending
- workflow/run: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: licensing-policy and FND-01 conflict review
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: PR #50 requires implementation-side metadata correction
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Dedicated branch and task created for the owner-approved MPL-2.0 correction.
status: implementing
branch: docs/fnd-01-mpl-license-correction
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
next_action: Update the FND-01 owner-acceptance record with the binding MPL-2.0 correction.
```
