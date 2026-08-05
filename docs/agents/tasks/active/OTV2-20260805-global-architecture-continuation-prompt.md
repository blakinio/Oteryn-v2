# OTV2-20260805-global-architecture-continuation-prompt

```yaml
task_id: OTV2-20260805-global-architecture-continuation-prompt
title: Persist the global architecture continuation prompt and decision register
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/global-architecture-continuation-prompt-20260805
pr: null
base_sha: 98b7193f285f64268bee16969a0d2d1c5b026132
head_sha: null
owner: chatgpt-github-agent
created_at: 2026-08-05T12:04:00+02:00
updated_at: 2026-08-05T12:04:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/prompts/OTV2_GLOBAL_ARCHITECTURE_DECISION_COORDINATOR.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/agents/tasks/active/OTV2-20260805-foundation-preimplementation-contracts.md
  - docs/agents/README.md
  - docs/agents/tasks/active/OTV2-20260805-global-architecture-continuation-prompt.md
public_contracts:
  - docs/agents/prompts/OTV2_GLOBAL_ARCHITECTURE_DECISION_COORDINATOR.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
depends_on:
  - ADR-0001 through ADR-0005
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
blocks: []
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories:
  - blakinio/Oteryn-Platform
  - blakinio/Otheryn
  - blakinio/otclient
```

## Outcome

Provide a self-contained repository execution prompt that lets a replacement agent continue the full Oteryn v2 architecture decision programme without chat history, while preserving one durable global register of unresolved project domains and one exact next action.

The delivered state must:

- preserve all accepted ADR invariants;
- include the global unresolved decision horizon, not only map/editor topics;
- prioritize decisions by workspace, durable-gameplay, vertical-slice, alpha, expansion and deferred stages;
- authorize autonomous technical decisions within repository and safety boundaries;
- require durable task/branch/PR/validation/audit/merge/archive lifecycle;
- route the canonical foundation checkpoint to the prompt;
- keep Workspace and Dependency Contract as the immediate next package.

## Architecture and source of truth

### PROVEN

- ADR-0001 through ADR-0005 are accepted on `main` at the task base.
- The canonical active foundation task still predates ADR-0005 in parts of its baseline and has no durable coordinator-prompt reference.
- `FOUNDATION_DECISION_BACKLOG.md` contains the ordered foundation gates but does not enumerate the complete later global product decision horizon.
- Repository prompt standards require exact authority, sources, ownership, acceptance, validation, autonomy, handover and stop conditions.

### DERIVED

- A dedicated coordinator prompt plus a staged global decision register reduces chat dependency and prevents late systems such as item transactions, houses, social systems, operations and product milestones from being forgotten or prematurely frozen.

## Acceptance criteria

- [x] Self-contained global coordinator prompt exists under `docs/agents/prompts/`.
- [x] Prompt includes role/mode, write allowlist, source order, accepted baseline, decision order, lifecycle, validation, audit, stop conditions and handover.
- [x] Prompt requires autonomous execution without plan-only completion and limits owner escalation to irreducible decisions.
- [x] Global decision register captures foundation, gameplay, client/world/content, operations and product domains.
- [x] Register classifies subjects by stage and preserves deferred extension points.
- [ ] Foundation backlog links the global register and coordinator prompt.
- [ ] Canonical active foundation task is reconciled with ADR-0005 and names the prompt.
- [ ] Agent governance index routes agents to reusable prompts.
- [ ] Full changed-file audit has zero open material findings.
- [ ] Prompt evaluation verdict is `PASS` under `PROMPT_EVAL_STANDARD.md`.
- [ ] Exact-head `Agent governance` passes.
- [ ] PR is squash-merged and this task is archived with ownership released.

## Excluded scope

- no architecture package beyond recording the accepted/global decision horizon;
- no Workspace and Dependency Contract implementation in this delivery;
- no Rust workspace, protocol, server, client or Studio implementation;
- no external-repository writes;
- no production, database, asset or release mutation;
- no change to accepted ADR decisions.

## Implementation / findings

- Added the global architecture coordinator prompt.
- Added the staged global architecture decision register.
- Remaining work is routing/reconciliation, validation, audit and lifecycle closeout.

## Validation

### Focused

- method: prompt evaluation against `PROMPTING_STANDARD.md`, `PROMPTING_HANDOVER.md` and `PROMPT_EVAL_STANDARD.md`
- result: pending final diff

### Component/integration

- result: `NOT_APPLICABLE` — documentation/prompt coordination only

### E2E

- result: `NOT_APPLICABLE` — no executable runtime behavior changes

### Exact-head CI

- head: pending
- workflow/run: `Agent governance`, pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: adversarial full-diff architecture, prompt and handover review
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
last_progress: Added the global coordinator prompt and staged architecture decision register on a dedicated branch.
status: implementing
branch: docs/global-architecture-continuation-prompt-20260805
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
next_action: Reconcile the foundation backlog, canonical foundation checkpoint and agent index with the new prompt and global register.
```
