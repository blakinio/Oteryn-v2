# OTV2-20260807-architecture-audit-refinements

```yaml
task_id: OTV2-20260807-architecture-audit-refinements
title: Apply whole-foundation architecture review refinements
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260807-architecture-audit-refinements
pr: 92
base_sha: 10392eb89d11de2ea260c82587b4b1ef22ddd7e6
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-07T23:23:00+02:00
updated_at: 2026-08-07T23:30:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/AGENTS.md
  - docs/agents/ARCHITECTURE_DECISION_DISCIPLINE.md
  - docs/agents/prompts/OTV2_ARCHITECTURE_CONTINUATION_AGENT.md
  - docs/architecture/ADR-0013-platform-database-technology-independence.md
  - docs/architecture/ARCHITECTURE_REVIEW_REFINEMENTS_2026-08-07.md
  - docs/agents/tasks/active/OTV2-20260807-architecture-audit-refinements.md
public_contracts:
  - docs/architecture/ADR-0013-platform-database-technology-independence.md
  - docs/architecture/ARCHITECTURE_REVIEW_REFINEMENTS_2026-08-07.md
depends_on:
  - ADR-0001 through ADR-0012
  - docs/architecture/FND-ID-01_FOUNDATION_IDENTIFIER_CONTRACT.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
blocks: []
cross_repository_coordination_id: OTV2-ARCHITECTURE-REVIEW-20260807
external_repositories:
  - blakinio/Oteryn-Platform
```

## Outcome

Persist the owner-approved whole-foundation review without reopening sound architecture: make future Platform PostgreSQL migration conditional on a separately justified Platform decision, preserve FND-02 as the current next gate, add explicit vertical-slice/decision-timing discipline, strengthen protocol evidence against common-mode codec bugs and clarify analytics event/identity ownership.

## Architecture and source of truth

- `PROVEN`: live `main` at task start is `10392eb89d11de2ea260c82587b4b1ef22ddd7e6`.
- `PROVEN`: ADR-0004 selects PostgreSQL for native game persistence and also contains a stronger future Platform PostgreSQL mandate.
- `PROVEN`: `FOUNDATION_PROGRAMME_CURRENT_STATUS.md` identifies FND-02 as the next ordered gate after completed FND-ID reconciliation.
- `PROVEN`: issue #86 is closed/completed.
- `PROVEN`: final FND-ID scope leaves CommandId to FND-02, runtime handles to FND-03, admission/lease mechanics to FND-04 and later event/audit identities to ANL/DUR owners.
- `PROVEN`: PR #91 has a narrow task-archive diff; Dependency Review and CodeQL pass while Agent governance fails in PR metadata validation.
- `OWNER_ACCEPTED`: the project owner instructed execution of the architecture-review recommendations on 2026-08-07.

## Acceptance criteria

- [x] Native game PostgreSQL remains accepted.
- [x] Mandatory Platform PostgreSQL migration is superseded by an evidence-backed, Platform-owned conditional decision.
- [x] Current next gate is recorded as FND-02 without reopening FND-ID.
- [x] Stale progression wording is explicitly classified as historical rather than silently authoritative.
- [x] Analytics event identity ownership follows the final FND-ID contract.
- [x] Event foundation guidance prevents an unbounded nullable mega-event.
- [x] Protocol/E2E guidance includes independent byte fixtures, malformed corpus, property tests and fuzzing without requiring a second production implementation.
- [x] Architecture decisions require `Must decide now?`, blocked work, future constraint and supersession evidence.
- [x] A new continuation prompt consumes the strengthened decision discipline.
- [x] No Rust runtime, protocol codec, persistence schema, Platform repository or production state is changed.
- [x] Complete changed-file review passes: six declared paths only before task metadata update; the seventh change is this task checkpoint update.
- [ ] Independent architecture/governance audit reports zero material findings.
- [ ] Exact-head required GitHub checks pass.

## Excluded scope

- No runtime implementation.
- No `protocol-oteryn` schema/transport selection; that remains FND-02.
- No FND-03/FND-04 implementation.
- No Platform database migration or write to `blakinio/Oteryn-Platform`.
- No modification of PR #91.
- No mass rewrite of historical evidence/task archives.
- No change to the accepted game PostgreSQL direction or Platform/game ownership separation.

## Implementation / findings

The package uses one partial supersession ADR instead of rewriting ADR-0004 history. Architecture working policy is strengthened through a dedicated discipline file consumed by `docs/agents/AGENTS.md`. A current review reconciliation records stale-status precedence and downstream guidance without falsely rewriting historical tasks.

## Validation

### Focused

- command/run: `python tools/agents/validate_governance.py` via trusted GitHub workflow on the exact PR head
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — documentation/architecture/governance only; no executable component changed
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no runtime behavior or user journey changed
- result: `NOT_APPLICABLE`

### Exact-head CI

- final head: pending
- trigger source: pull_request
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: adversarial architecture/governance consistency review against current main, ADR-0004, FND-ID, current programme status and repository instructions
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: `PASS`; only declared architecture/governance/task paths are present
- unresolved review threads: pending
- related/superseded PRs: PR #91 reviewed as `FIX`; no path overlap with this package
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: PR #92 is open as a draft with the bounded owner-approved architecture review refinements; complete diff scope is clean.
status: validating
branch: docs/OTV2-20260807-architecture-audit-refinements
head_sha: null
pr: 92
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: pull_request
ci_check_generation: pending task-metadata commit
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
next_action: Inspect the exact PR head, run adversarial architecture/governance audit and verify required GitHub checks.
```
