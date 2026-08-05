# OTV2-20260805-mpl2-licensing

```yaml
task_id: OTV2-20260805-mpl2-licensing
title: Establish MPL-2.0 licensing and protected asset boundaries
mode: GOVERNANCE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: governance/mpl-2.0-licensing-20260805
pr: null
base_sha: cb35e11a22754ad0946b5676090863598950c474
head_sha: null
owner: GPT-5.6 Thinking
created_at: 2026-08-05T16:51:00+02:00
updated_at: 2026-08-05T16:51:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - LICENSE
  - LICENSE-ASSETS.md
  - TRADEMARKS.md
  - README.md
  - CONTRIBUTING.md
  - docs/repository/LICENSING.md
  - docs/repository/GITHUB_GOVERNANCE.md
  - .github/repository-policy.json
  - tools/repository/validate_repository_policy.py
  - docs/agents/tasks/active/OTV2-20260805-mpl2-licensing.md
  - docs/agents/tasks/archive/OTV2-20260805-mpl2-licensing.md
public_contracts:
  - LICENSE
  - LICENSE-ASSETS.md
  - TRADEMARKS.md
  - docs/repository/LICENSING.md
depends_on: []
blocks: []
cross_repository_coordination_id: null
external_repositories: []
```

## Outcome

Publish Oteryn-v2 source code and technical documentation under the Mozilla Public License 2.0 while explicitly reserving project branding and creative game assets unless a file-specific license grants additional rights.

## Architecture and source of truth

- `PROVEN`: the repository is public and currently contains no root license file.
- `PROVEN`: no other active task owns the paths declared by this task.
- `PROVEN`: Mozilla identifies MPL 2.0 as the current MPL and publishes the canonical license text and SPDX identifier `MPL-2.0`.
- `DERIVED`: a file-level weak copyleft license provides a suitable balance between reusable modules and requiring distributed modifications to covered files to remain available.

## Acceptance criteria

- [ ] Root `LICENSE` contains the unmodified canonical MPL-2.0 text.
- [ ] The licensing scope clearly covers code, scripts, configuration, tests, schemas and technical documentation unless overridden by a file-specific notice.
- [ ] Creative game assets and project branding are explicitly outside the MPL grant unless separately licensed.
- [ ] Contribution guidance establishes inbound licensing under MPL-2.0 and requires third-party provenance.
- [ ] Repository policy validation requires and verifies the licensing contract.
- [ ] Focused validators and exact-head GitHub checks pass.
- [ ] Independent audit finds no material ambiguity or contradiction.

## Excluded scope

- No CLA, copyright assignment, dual-commercial licensing programme or registered-trademark claim.
- No relicensing of third-party material.
- No changes to runtime architecture, protocol, persistence or product implementation.
- No cross-repository licensing change.

## Implementation / findings

Implementation in progress.

## Validation

### Focused

- command/run: pending
- result: pending

### Component/integration

- command/run: repository policy and governance validators
- result: pending

### E2E

- scenario: `NOT_APPLICABLE` — licensing governance has no executable runtime outcome.
- result: `NOT_APPLICABLE`

### Exact-head CI

- head: pending
- workflow/run: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: pending
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: none found at task start
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Claimed bounded licensing-governance scope on a dedicated branch.
status: implementing
branch: governance/mpl-2.0-licensing-20260805
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
next_action: Add the canonical MPL-2.0 license and repository licensing boundary documents.
```
