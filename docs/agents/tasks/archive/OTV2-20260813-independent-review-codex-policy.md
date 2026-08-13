# OTV2-20260813-independent-review-codex-policy — archived

```yaml
task_id: OTV2-20260813-independent-review-codex-policy
title: Prefer fresh independent agents and gate Codex recommendations
mode: GOVERNANCE
status: completed
repository: blakinio/Oteryn-v2
base_branch: main
delivery_branch: docs/OTV2-20260813-independent-review-codex-policy
delivery_pr: 216
base_sha: c2c692b3b522bcee3c081aba9c8114e4c67fe818
final_head_sha: 64fa828f2bf56ba1a69bdd6a97b6bda33843066c
delivery_merge_sha: 41dffacb4aa706aeae5affbc4a3a0ea1643fde33
lifecycle_closeout_branch: docs/OTV2-20260813-independent-review-codex-policy-closeout
lifecycle_closeout_pr: pending
owner: released_after_closeout
created_at: 2026-08-13T11:48:00+02:00
completed_at: 2026-08-13T13:40:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - AGENTS.md
  - docs/agents/OWNER_FUNDED_AI_POLICY.md
  - docs/agents/tasks/archive/OTV2-20260813-independent-review-codex-policy.md
public_contracts: []
depends_on:
  - root AGENTS.md review/audit and owner-funded-AI policy
  - docs/agents/AGENTS.md task-record and governance requirements
blocks: []
cross_repository_coordination_id: null
external_repositories: []
```

## Outcome

The owner review-cost preference is now canonical on `main`:

- a qualified fresh separate agent/session is the default independent-review mechanism when one is available and suitable;
- the reviewer must verify the exact final SHA and governing requirements independently and must not inherit implementing-agent conclusions as trusted facts;
- Codex is optional rather than the default reviewer;
- when Codex is expected to provide a material efficiency or review-quality advantage, the coordinator must first inform the owner, explain that advantage and provide a bounded ready-to-run prompt;
- providing a prompt or recommendation does not authorize Codex;
- Codex/OpenAI API/owner-funded AI remains deny-by-default and requires explicit authorization for the exact current use;
- prior permission is never standing permission;
- no independent-review trigger, safety/evidence gate, repository/write/merge/production/cross-repository authority or architecture/runtime semantic boundary was weakened or expanded.

Canonical policy sources after delivery:

- root `AGENTS.md`;
- `docs/agents/OWNER_FUNDED_AI_POLICY.md`.

## Delivery history

Delivery PR #216 started as a draft to avoid automatically consuming owner-funded Codex through the repository's enabled Code Review integration.

A direct squash-merge attempt while draft was rejected by GitHub with HTTP 405. The owner was informed that moving #216 from draft to ready would automatically trigger Codex Review and then explicitly instructed the coordinator to finish the task. That authorization was limited to the automatic review of PR #216 at exact head `27067c79dcc701244c46931fcf40c1dfdbef9334`; it was not standing permission.

Automatic Codex review `4926598862` on that superseded head found one material P1 limited to the active task record: the abbreviated record omitted template-required execution budget, dependency/blocking metadata, cross-repository coordination, excluded scope and component/E2E classification. The review did not report a material defect in the root independent-review policy or owner-funded-AI policy semantics.

Repair cycle 1 updated only the task record to the canonical `docs/agents/tasks/TASK_TEMPLATE.md` shape. Root `AGENTS.md` and `docs/agents/OWNER_FUNDED_AI_POLICY.md` policy semantics were unchanged by the repair. No additional Codex/OpenAI API/owner-funded AI invocation was triggered after that owner-authorized automatic review.

The Codex P1 thread was answered with exact-head evidence and resolved before merge.

## Terminal validation

Final delivery head: `64fa828f2bf56ba1a69bdd6a97b6bda33843066c`.

- changed-file scope: exactly `AGENTS.md`, `docs/agents/OWNER_FUNDED_AI_POLICY.md`, and the active task record;
- live compare immediately before merge: `behind_by=0`;
- terminal exact-head self-review `4926617834`: **PASS**, material findings `0`;
- Agent Governance `31697002920`: **PASS**;
- Dependency Review `31697002987`: **PASS**;
- CodeQL `31697002896`: **PASS**;
- Codex review `4926598862` on superseded `27067c79...`: one task-record P1, repaired;
- Codex P1 thread: resolved;
- unresolved review threads before merge: `0`;
- component/integration validation: `NOT_APPLICABLE` — governance/documentation-only;
- E2E: `NOT_APPLICABLE` — no runtime/client/service behavior changed;
- mandatory independent review on repaired final head: `NOT_REQUIRED` because the final change reduced no safety gate, expanded no authority and weakened no evidence requirement;
- squash delivery merge: `41dffacb4aa706aeae5affbc4a3a0ea1643fde33`.

## Excluded authority preserved

This delivery does not:

- authorize standing Codex/OpenAI API/owner-funded AI use;
- make self-review count as independent review;
- weaken any mandatory independent-review trigger;
- alter Codex repository settings;
- alter runtime/client/protocol/persistence/gameplay/content/Platform behavior;
- alter production/protected-environment/repository/cross-repository authority.

## Lifecycle closeout

The lifecycle closeout may only archive this completed task and release its path ownership. It must not change `AGENTS.md`, `docs/agents/OWNER_FUNDED_AI_POLICY.md` or any architecture/runtime semantics.

## Context checkpoint

```yaml
last_progress: PR #216 merged final repaired head 64fa828f2bf56ba1a69bdd6a97b6bda33843066c as 41dffacb4aa706aeae5affbc4a3a0ea1643fde33 after one owner-authorized automatic Codex review found and the delivery repaired a task-record-only P1.
status: completed
delivery_pr: 216
final_head_sha: 64fa828f2bf56ba1a69bdd6a97b6bda33843066c
delivery_merge_sha: 41dffacb4aa706aeae5affbc4a3a0ea1643fde33
lifecycle_closeout_pr: pending
terminal_self_review: 4926617834
supplemental_codex_review_superseded_head: 4926598862
ci_run_ids:
  - 31697002920
  - 31697002987
  - 31697002896
repair_cycles_for_delivery_gate: 1
owner_action_required: false
blocker: null
next_action: Complete the bounded lifecycle closeout by removing the active task record and retaining this archive; do not invoke additional Codex or modify policy semantics.
```
