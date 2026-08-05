# OTV2-20260805-foundation-execution-guardrails

```yaml
task_id: OTV2-20260805-foundation-execution-guardrails
title: Refine foundation decision and implementation gates
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/workspace-dependency-contract-20260805
pr: null
base_sha: bd87792c92e26835d44c633a6064808f487a58a2
head_sha: pending
owner: chatgpt-github-agent
created_at: 2026-08-05T12:42:00+02:00
updated_at: 2026-08-05T12:42:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
  - docs/agents/prompts/OTV2_GLOBAL_ARCHITECTURE_DECISION_COORDINATOR.md
  - docs/agents/tasks/active/OTV2-20260805-foundation-preimplementation-contracts.md
  - docs/agents/tasks/active/OTV2-20260805-foundation-execution-guardrails.md
public_contracts:
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
depends_on:
  - ADR-0001 through ADR-0005
blocks:
  - execution of the Workspace and Dependency Contract with ambiguous implementation gates
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/Oteryn-Platform
  - blakinio/Otheryn
  - blakinio/otclient
```

## Outcome

Make the foundation programme safer and more executable by preserving architecture-first decisions while allowing compile-time feedback after the Workspace and Dependency Contract, preventing premature crate proliferation, assigning stable gate identifiers and separating the non-owning programme checkpoint from individual contract packages.

## Architecture and source of truth

### PROVEN

- ADR-0001 through ADR-0005 are accepted on `main`.
- The current backlog requires all four foundation contracts before creation of the root Cargo workspace.
- The candidate workspace horizon lists many possible crates but is not an accepted initial graph.
- The canonical foundation task is an umbrella checkpoint with no owner or owned paths.
- The global coordinator prompt defaults to execution and does not explicitly define a read-only analysis invocation.

### DERIVED

- Requiring protocol, runtime and admission contracts before any compilable workspace delays useful dependency and interface feedback.
- Treating the complete capability horizon as an initial workspace risks empty crates and premature abstraction.
- Stable gate IDs reduce cross-document drift.

## Acceptance criteria

- [ ] Only the Workspace and Dependency Contract blocks root workspace bootstrap.
- [ ] A separately authorized minimal compilable bootstrap is allowed after that contract, without authorizing production protocol, runtime, admission or durable gameplay implementation.
- [ ] Bounded technical spikes are explicitly non-canonical, reversible and evidence-producing.
- [ ] The candidate crate list is classified as a capability horizon, and initial members require an immediate consumer and observable acceptance.
- [ ] Stable gate IDs are consistent across backlog, register, programme task and coordinator prompt.
- [ ] The programme task is explicitly non-owning; every decision package requires its own task, branch and PR.
- [ ] The coordinator prompt supports explicit read-only analysis without creating repository state.
- [ ] Architecture dependency rules must become executable CI checks after workspace bootstrap.
- [ ] Full diff audit has zero material findings and exact-head governance CI passes.

## Excluded scope

- no change to ADR-0001 through ADR-0005;
- no root Cargo workspace or Rust code;
- no protocol, runtime, admission or persistence implementation;
- no external-repository writes;
- no production, database, asset or deployment mutation.

## Implementation / findings

- Task and ownership established on the existing clean branch.

## Validation

### Focused

- command/run: pending governance validation
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture/governance documentation only
- result: pending

### E2E

- scenario: `NOT_APPLICABLE` — no executable runtime behavior changes
- result: pending

### Exact-head CI

- head: pending
- workflow/run: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: adversarial full-diff architecture review
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: none found at start
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Created the bounded task and claimed the four coordination documents plus this task record.
status: implementing
branch: docs/workspace-dependency-contract-20260805
head_sha: pending
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
next_action: Reconcile the foundation backlog with progressive implementation gates and stable identifiers.
```
