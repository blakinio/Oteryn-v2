# OTV2-20260809-architecture-continuation-prompt-refresh

```yaml
task_id: OTV2-20260809-architecture-continuation-prompt-refresh
title: Refresh reusable architecture continuation prompt
mode: GOVERNANCE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/architecture-continuation-prompt-refresh
pr: null
base_sha: 0dfde85673b985bd00d6f3dcd3690dbf068fdeed
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: GPT-5.6-Sol-session
created_at: 2026-08-09T20:52:00+02:00
updated_at: 2026-08-09T20:52:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/prompts/OTV2_ARCHITECTURE_CONTINUATION_AGENT.md
  - docs/agents/prompts/README.md
  - docs/agents/tasks/active/OTV2-20260809-architecture-continuation-prompt-refresh.md
public_contracts: []
depends_on: []
blocks: []
cross_repository_coordination_id: null
external_repositories: []
```

## Outcome

The existing canonical reusable Oteryn-v2 architecture continuation prompt is refreshed rather than duplicated, preserving current repository governance while incorporating the owner's supplied architecture-analysis requirements and a stable short invocation alias.

## Architecture and source of truth

- `PROVEN`: `docs/agents/prompts/OTV2_ARCHITECTURE_CONTINUATION_AGENT.md` is the existing canonical prompt for this purpose on `main`.
- `PROVEN`: repository governance requires a dedicated task/branch/PR for this documentation change.
- `PROVEN`: the owner-supplied prompt emphasizes full startup PR review, architecture-analysis-only runtime gate, proactive gap detection, player/producer perspectives, AI-maintainable architecture, decision documentation and safe PR close criteria.
- `PROVEN`: open PR #114 currently owns only FND-04A architecture/contract/task paths and does not overlap this task.

## Acceptance criteria

- [ ] Update the canonical architecture continuation prompt without creating a duplicate prompt file.
- [ ] Preserve accepted Oteryn-v2 architecture, trust boundaries and runtime implementation gate.
- [ ] Incorporate the material requirements from the owner-supplied prompt that are missing or weaker in the current canonical prompt.
- [ ] Document one stable short invocation alias: `Oteryn: architektura`.
- [ ] Evaluate the final prompt against `docs/agents/PROMPT_EVAL_STANDARD.md` with no material ambiguity.
- [ ] Run applicable governance/document validation on the final exact head.

## Excluded scope

No runtime code, protocol schema, persistence, architecture decision, production, Platform repository or live-operation change. Do not modify or close unrelated PR #114.

## Implementation / findings

The existing prompt is already a condensed, current-repository-aware version of the owner's longer supplied prompt. The change should therefore be a narrow augmentation, not replacement by a second long-form prompt.

## Validation

### Focused

- command/run: pending
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — documentation-only prompt/governance change
- result: pending

### E2E

- scenario: `NOT_APPLICABLE` — no executable runtime/user-product behavior changes
- result: pending

### Exact-head CI

- final head: pending
- trigger source: pending
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: pending
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: #114 reviewed; no overlap
- protected auto-merge: not requested
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: canonical prompt and prompting standards inspected; no overlapping open PR found
status: implementing
branch: docs/architecture-continuation-prompt-refresh
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
owner_action_required: null
blocker: null
next_action: update the canonical prompt and prompt index on this branch
```
