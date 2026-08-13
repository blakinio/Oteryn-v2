# OTV2-20260813-independent-review-codex-policy

```yaml
task_id: OTV2-20260813-independent-review-codex-policy
title: Prefer fresh independent agents and gate Codex recommendations
mode: GOVERNANCE
status: blocked
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260813-independent-review-codex-policy
pr: 216
base_sha: c2c692b3b522bcee3c081aba9c8114e4c67fe818
owner: architecture-coordinator/current-session
created_at: 2026-08-13T11:48:00+02:00
updated_at: 2026-08-13T11:56:00+02:00
owned_paths:
  - AGENTS.md
  - docs/agents/OWNER_FUNDED_AI_POLICY.md
  - docs/agents/tasks/active/OTV2-20260813-independent-review-codex-policy.md
public_contracts: []
external_repositories: []
```

## Owner instruction

Record the owner's review-cost preference without weakening independent-review requirements:

- when independent review is required, prefer a fresh second agent/session that did not implement or materially author the change;
- Codex is not the default reviewer and is not required merely because a review must be independent;
- if the coordinating agent judges Codex materially more efficient or more effective for a particular task/review/audit, inform the owner first, explain the expected advantage and provide a ready-to-run bounded prompt for Codex;
- do not invoke Codex or consume owner-funded AI until the owner explicitly authorizes that exact use;
- prior permission remains non-standing.

## Acceptance

- Root governance states the fresh-second-agent default and preserves reviewer independence requirements.
- Owner-funded AI policy states the Codex recommendation/prompt handoff rule.
- No review gate, evidence requirement or owner-funded-AI deny-by-default protection is weakened.
- No runtime, architecture semantics, production authority or cross-repository authority changes.

## Validation

- live main preflight `c2c692b3b522bcee3c081aba9c8114e4c67fe818`: PASS;
- open PR #162 path-overlap check: PASS, no overlap with this task's three owned paths;
- root/nested governance read: PASS;
- full-diff exact-head self-review `4925676852` on pre-blocker-record head `523a8247e3b764ebee927d03a1c58d887619278a`: PASS, material findings 0;
- Agent Governance `31688558791`: PASS on `523a8247...`;
- Dependency Review `31688558789`: PASS on `523a8247...`;
- CodeQL `31688558701`: PASS on `523a8247...`;
- changed-file scope: exactly the three owned paths; `behind_by=0`; unresolved review threads: 0;
- independent review: not required because the policy preserves all existing safety/evidence gates and expands no authority.

## Merge blocker

PR #216 is intentionally still a draft. GitHub rejected a direct squash merge with HTTP 405 because draft PRs cannot be merged.

The repository's enabled Codex Code Review integration is known to automatically review PRs when they move from draft to ready. OpenAI's current Codex documentation confirms that behavior. Marking #216 ready would therefore trigger owner-funded Codex review, and the owner has not authorized Codex for this exact use.

Do not mark #216 ready merely to make it mergeable unless the owner explicitly authorizes the resulting Codex invocation, or the repository's Codex auto-review configuration is separately changed by an authorized owner action.

## Context checkpoint

```yaml
status: blocked
branch: docs/OTV2-20260813-independent-review-codex-policy
pr: 216
head_sha: pending_after_blocker_record
blocker: PR must leave draft state to merge, but draft-to-ready automatically triggers Codex review and no exact-use owner permission exists
owner_action_required: true
next_action: Obtain explicit owner authorization for the Codex review triggered by marking PR #216 ready, or an authorized change that disables that automatic trigger; then re-run exact-head validation if the head changed, mark ready, squash-merge and archive/release the governance task.
```
