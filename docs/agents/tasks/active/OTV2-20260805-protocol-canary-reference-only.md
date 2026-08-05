# OTV2-20260805-protocol-canary-reference-only

```yaml
task_id: OTV2-20260805-protocol-canary-reference-only
title: Record protocol-canary as reference-only migration evidence
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/adr-0008-protocol-canary-reference-only
pr: null
base_sha: 52ef04882e13771829e0159b63410a7cd9e80150
head_sha: null
owner: GPT-5.6-Thinking-architecture-coordinator
created_at: 2026-08-05T18:59:00+02:00
updated_at: 2026-08-05T18:59:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/architecture/ADR-0008-protocol-canary-reference-only-migration-disposition.md
  - docs/agents/prompts/OTV2_GLOBAL_ARCHITECTURE_DECISION_COORDINATOR.md
  - docs/agents/tasks/active/OTV2-20260805-protocol-canary-reference-only.md
public_contracts:
  - docs/architecture/ADR-0008-protocol-canary-reference-only-migration-disposition.md
depends_on:
  - ADR-0001
  - ADR-0002
blocks:
  - FND-01 completion until the source-workspace inventory applies this fixed disposition
  - VSL-02 completion until protocol-canary is absent from the destination production runtime graph
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/otclient
```

## Outcome

Record the owner-accepted binding migration disposition for the existing Rust client's `protocol-canary` subsystem and remove stale coordinator instructions that could bypass the accepted `FND-01 -> VSL-02 -> atomic destination migration/workspace PR` sequence.

## Architecture and source of truth

### PROVEN

- ADR-0001 selects one project-owned gameplay protocol, `protocol-oteryn`, and excludes Canary/Tibia packet compatibility from the target runtime.
- ADR-0002 requires `protocol-canary` isolation or removal from the target production runtime graph during the atomic client migration/workspace PR.
- The source client workspace at `blakinio/otclient@c923ad8a1dff17b4933a6110931b0823cec2c590` currently includes `crates/protocol-canary`.
- The owner accepted on 2026-08-05 that Oteryn writes its native protocol from zero and does not want `protocol-canary` in production.

### CONFLICT

- The coordinator prompt contains stale ordering that permits a separate workspace bootstrap after `FND-01` and delays `VSL-02`, contrary to ADR-0002, the foundation backlog, the global register and the active programme checkpoint.

## Acceptance criteria

- [ ] An accepted ADR fixes `protocol-canary` to `REFERENCE_ONLY` for `FND-01` and `VSL-02`.
- [ ] The ADR prohibits production Cargo/runtime dependency edges, protocol negotiation, fallback and translation through Canary.
- [ ] Any retained Canary material is outside production workspace members and carries exact provenance and license treatment.
- [ ] The coordinator prompt requires `VSL-02` immediately after `FND-01` and one atomic destination migration/workspace PR.
- [ ] No runtime code, external repository or production system is changed.
- [ ] Exact-head governance validation and independent full-diff audit pass.

## Excluded scope

- Do not implement `protocol-oteryn`.
- Do not move client source.
- Do not create the canonical Cargo workspace.
- Do not modify `blakinio/otclient`, Platform, Otheryn or production systems.
- Do not classify unrelated source-client crates; that remains `FND-01` work.

## Implementation / findings

- Owner decision recorded: `protocol-canary = REFERENCE_ONLY`.
- Target production disposition is stronger than temporary dual-protocol compatibility: no Canary adapter, fallback, negotiation or server compatibility path exists in Oteryn v2 production.

## Validation

### Focused

- command/run: pending GitHub diff and governance review
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture-only package
- result: pending

### E2E

- scenario: `NOT_APPLICABLE` — no executable product change
- result: pending

### Exact-head CI

- head: pending
- workflow/run: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: adversarial full-diff review against ADR-0001, ADR-0002, backlog and global register
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: none
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Owner accepted protocol-canary as reference-only evidence and prohibited it from Oteryn v2 production.
status: implementing
branch: docs/adr-0008-protocol-canary-reference-only
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
next_action: Add ADR-0008 and reconcile the stale coordinator ordering.
```
