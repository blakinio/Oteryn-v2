# OTV2-20260816-architecture-semantic-audit

```yaml
task_id: OTV2-20260816-architecture-semantic-audit
title: Deterministic independent semantic-contract audit workflow
mode: TOOLING_GOVERNANCE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/architecture-semantic-audit
owner: ARCHITECTURE_COORDINATOR
created_at: 2026-08-16
updated_at: 2026-08-16
owned_paths:
  - .github/workflows/architecture-semantic-audit.yml
  - tools/architecture/semantic_contract_audit.py
  - docs/agents/tasks/active/OTV2-20260816-architecture-semantic-audit.md
public_contracts: []
external_repositories: []
implementation_authority: TOOLING_ONLY
merge_authority: ARCHITECTURE_COORDINATOR_ONLY
owner_funded_ai_authorized: false
```

## Goal

Add a non-AI, fail-closed GitHub-hosted mechanism allowed by root `AGENTS.md` as a dedicated independent audit workflow. It binds itself to the live exact PR head, inspects the complete changed-file set and evaluates semantic invariants for the pending `ALPHA-CLIENT-01` and `ANL-02`/`ANL-03` architecture profiles.

It is reusable repository tooling, not a one-off PASS record. It grants no merge authority and cannot replace normal exact-head CI, self-review, thread resolution or current-main drift checks.

## Acceptance criteria

- [ ] exact open same-repository PR head is resolved through GitHub API and head movement fails closed;
- [ ] exact-SHA checkout uses no persisted credentials;
- [ ] only exact known E/F architecture path sets activate semantic profiles; unrelated PRs are explicit `NOT_APPLICABLE`;
- [ ] ALPHA-CLIENT profile checks admission/Gateway/FND authority, fail-closed readiness, production codec plus independent wire evidence, scene/audio non-authority, settings scopes/precedence/privacy migration and Studio sharing/export/dependency boundaries;
- [ ] ANL-02/03 profile checks read-only authority, fail-closed no-regression prerequisites, insufficient-evidence disposition, immutable evidence lifecycle, referral-after-substantive-disposition semantics, false-positive safety and absence of enforcement authority;
- [ ] logs/job summary identify audit method/profile/exact SHA/verdict;
- [ ] no Codex/OpenAI API/paid AI/owner credential is used;
- [ ] full-diff self-review and normal repository CI pass before merge.

## Validation

Runtime/gameplay E2E: `NOT_APPLICABLE` — repository audit tooling only. After merge the workflow must execute on fresh E/F synchronize events and produce exact-head PASS evidence before those architecture PRs can merge.

## Context checkpoint

```yaml
status: implementing
next_action: ADD_WORKFLOW_AND_AUDITOR_THEN_SELF_REVIEW_CI_MERGE
```

`MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`
`IMPLEMENTATION_AUTHORITY: TOOLING_ONLY`
