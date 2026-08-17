# OTV2-20260817-governance-live-pr-metadata

```yaml
task_id: OTV2-20260817-governance-live-pr-metadata
title: Eliminate stale PR metadata dependence from Agent governance
mode: FIX
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: fix/governance-live-pr-metadata
pr: null
base_sha: 65b5711fc56f80c0407ce462e83cdc973535636f
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: governance repair agent
created_at: 2026-08-17T09:22:00+02:00
updated_at: 2026-08-17T09:22:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - .github/workflows/agent-governance.yml
  - docs/agents/tasks/active/OTV2-20260817-governance-live-pr-metadata.md
public_contracts: []
depends_on:
  - main@65b5711fc56f80c0407ce462e83cdc973535636f
blocks:
  - reliable automatic metadata recovery for PR validation, including OTV2-TOKIO-239-class races
cross_repository_coordination_id: OTERYN-GOV-LIVE-PR-METADATA-20260817
external_repositories:
  - blakinio/Oteryn-Platform
  - blakinio/Otheryn
  - blakinio/otclient
```

## Outcome

Make `Agent governance` validate the current live pull-request state instead of a stale event-body snapshot, and automatically revalidate metadata edits so `workflow_dispatch` remains only a break-glass exact-head recovery path.

## Proven problem

- `PROVEN`: PR #239 produced a fresh `synchronize` Agent-governance run whose event payload contained the old Dependabot body even though the PR body was repaired immediately afterwards.
- `PROVEN`: the failed run reported only missing `## Summary`, `## Scope`, and `## Validation`, while the current live PR body already contained those headings and the exact-head Merge-gate governance check passed.
- `PROVEN`: current `.github/workflows/agent-governance.yml` reads title/body directly from `github.event.pull_request.*` for normal pull-request events and only fetches live PR metadata for `workflow_dispatch`.
- `PROVEN`: the active GitHub connector exposes workflow rerun operations but no workflow-dispatch operation, so repository automation should not depend on manual dispatch for recoverable PR metadata edits.

## Acceptance criteria

- [ ] `pull_request` explicitly handles `opened`, `reopened`, `synchronize`, and `edited`.
- [ ] Pull-request validation resolves the PR number/head from the event but fetches title/body/base/head repository/state from the live GitHub API.
- [ ] A stale event whose recorded head no longer matches the live PR head fails closed.
- [ ] `workflow_dispatch` retains exact branch/SHA/PR identity verification and uses the same live-metadata validation path.
- [ ] Push-to-main validation behavior remains unchanged.
- [ ] Existing title/body/base/same-repository checks remain at least as strict as before.
- [ ] Governance/repository-policy validation passes on the exact final head.
- [ ] Full changed-file self-review finds no safety reduction or authority expansion.

## Excluded scope

- weakening any required check, branch protection, merge authority, or repository allowlist;
- adding `pull_request_target` or executing PR-controlled code with elevated permissions;
- changing production/deployment workflows;
- owner-funded Codex/OpenAI review;
- cross-repository writes unless separately authorized by the owner and each repository's trusted-base policy.

## Cross-repository audit

Read-only audit targets under coordination ID `OTERYN-GOV-LIVE-PR-METADATA-20260817`:

- `blakinio/Oteryn-Platform`;
- `blakinio/Otheryn`;
- `blakinio/otclient`.

Only repositories with the same stale-event-metadata dependency should receive an equivalent dedicated task/branch/PR.

## Context checkpoint

```yaml
checkpoint_status: implementing
last_verified_base_sha: 65b5711fc56f80c0407ce462e83cdc973535636f
current_branch: fix/governance-live-pr-metadata
current_pr: null
current_head_sha: null
findings:
  - Oteryn-v2 Agent governance uses stale event title/body on normal PR events.
  - Oteryn-Platform agent-governance does not validate PR body/title and is not affected by the #239 race in that workflow.
  - Otheryn and otclient have no .github/workflows/agent-governance.yml at main; broader workflow audit remains read-only.
next_action: Update Oteryn-v2 Agent governance to trigger on edited and resolve live PR metadata for every PR validation path.
```
