# OTV2-20260805-vsl02-client-migration-sequencing

```yaml
task_id: OTV2-20260805-vsl02-client-migration-sequencing
title: Move exact Rust client migration before identifier and protocol freeze
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: arch/vsl02-client-migration-sequencing-20260805
pr: null
base_sha: 14132133493a7e0990235c45fed63efa47233d9e
head_sha: null
owner: architecture-coordinator
created_at: 2026-08-05T14:56:00+02:00
updated_at: 2026-08-05T14:56:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/architecture/ADR-0002-repository-ownership-and-client-migration.md
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
  - docs/architecture/MULTICHANNEL_SYSTEM_SCOPE_MATRIX.md
  - docs/agents/tasks/active/OTV2-20260805-foundation-preimplementation-contracts.md
  - docs/agents/tasks/active/OTV2-20260805-vsl02-client-migration-sequencing.md
public_contracts:
  - docs/architecture/ADR-0002-repository-ownership-and-client-migration.md
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
depends_on:
  - FND-01 remains the first unresolved foundation contract
  - ADR-0002 accepted repository ownership and client migration direction
blocks:
  - FND-ID-01 and FND-02 sequencing until the client migration/cutover gate is recorded consistently
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/otclient
```

## Outcome

Record the owner-accepted architecture decision that `VSL-02` and the controlled Rust client migration/cutover must occur immediately after `FND-01` and before `FND-ID-01`, `FND-02`, `FND-03` or `FND-04` freeze shared client/server contracts in a destination workspace that does not yet contain the canonical client.

Also remove the stale statement that final database technology remains open, because ADR-0004 already selected PostgreSQL.

## Architecture and source of truth

- `PROVEN`: ADR-0002 makes `blakinio/Oteryn-v2` the canonical repository for the Rust client, server and shared protocol/domain contracts.
- `PROVEN`: the existing client workspace remains under `blakinio/otclient/oteryn-client` and contains substantial reusable Rust architecture.
- `PROVEN`: the accepted programme previously placed `VSL-02` after protocol, runtime, admission, persistence and content contracts.
- `DERIVED`: leaving the migration that late risks designing shared contracts against a stale client inventory and reintroduces cross-repository drift that ADR-0002 was accepted to eliminate.
- `ACCEPTED_OWNER_DECISION`: execute `FND-01`, then the separately authorized `VSL-02` migration/cutover programme, then create/complete the canonical workspace bootstrap and continue with `FND-ID-01` and layer contracts.

## Acceptance criteria

- [ ] ADR-0002 explicitly records the mandatory sequencing and stale-inventory protection.
- [ ] Foundation backlog and global register place `VSL-02` immediately after `FND-01`.
- [ ] The active programme checkpoint has exactly one next action and reflects the revised order.
- [ ] The multichannel matrix no longer lists database technology as unresolved.
- [ ] No runtime, Cargo workspace, client code or external repository is modified.
- [ ] Governance validation passes on the exact final head.
- [ ] Independent full-diff audit finds no material contradiction.

## Excluded scope

- no Rust workspace bootstrap;
- no client source migration;
- no writes to `blakinio/otclient`;
- no protocol, runtime, identifier or admission implementation;
- no decision on the exact migration mechanism or source SHA beyond requiring those to be frozen by `VSL-02`.

## Implementation / findings

- Owner accepted moving `VSL-02` immediately after `FND-01`.
- The migration remains a separate cross-repository programme with one task/branch/PR per written repository.
- Workspace bootstrap must not establish a competing canonical client copy. It may be combined with destination migration only if `VSL-02` explicitly owns and validates that operation.

## Validation

### Focused

- command/run: pending
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture-only package
- result: pending

### E2E

- scenario: `NOT_APPLICABLE` — no runtime behavior changes
- result: pending

### Exact-head CI

- head: pending
- workflow/run: Agent governance
- result: pending

## Independent audit

- exact head: pending
- method/auditor: full architecture diff review
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: none known
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Owner accepted moving VSL-02 and controlled client migration immediately after FND-01.
status: implementing
branch: arch/vsl02-client-migration-sequencing-20260805
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
next_action: Update ADR-0002, the foundation backlog, global register, active programme checkpoint and multichannel scope matrix with the accepted sequencing decision.
```
