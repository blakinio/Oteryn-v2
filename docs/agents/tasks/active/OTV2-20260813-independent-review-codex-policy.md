# OTV2-20260813-independent-review-codex-policy

```yaml
task_id: OTV2-20260813-independent-review-codex-policy
title: Prefer fresh independent agents and gate Codex recommendations
mode: GOVERNANCE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260813-independent-review-codex-policy
base_sha: c2c692b3b522bcee3c081aba9c8114e4c67fe818
owner: architecture-coordinator/current-session
created_at: 2026-08-13T11:48:00+02:00
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

- full-diff self-review;
- repository governance validation / Agent Governance;
- standard exact-head PR checks applicable to documentation/governance;
- independent review: not required unless final diff reduces a safety gate or expands authority.

## Context checkpoint

```yaml
status: implementing
branch: docs/OTV2-20260813-independent-review-codex-policy
pr: null
head_sha: null
blocker: null
owner_action_required: false
next_action: Apply the narrow root AGENTS.md and OWNER_FUNDED_AI_POLICY.md changes, then validate the exact three-path diff and merge only after exact-head checks pass.
```
