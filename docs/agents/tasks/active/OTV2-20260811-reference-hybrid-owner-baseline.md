# OTV2-20260811-reference-hybrid-owner-baseline

```yaml
task_id: OTV2-20260811-reference-hybrid-owner-baseline
title: Persist GAME-VISION-01 hybrid Reference tracking owner baseline
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260811-reference-hybrid-owner-baseline
pr: null
base_sha: cd041f0da4e38ec87990a4924cb7a8a2b1f66f5e
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-11T09:57:00+02:00
updated_at: 2026-08-11T09:57:00+02:00
execution_budget_minutes: 60
owned_paths:
  - docs/agents/tasks/active/OTV2-20260811-reference-hybrid-owner-baseline.md
  - docs/architecture/GAME-VISION-01_REFERENCE_HYBRID_TRACKING_OWNER_BASELINE.md
public_contracts:
  - docs/architecture/GAME-VISION-01_REFERENCE_HYBRID_TRACKING_OWNER_BASELINE.md
depends_on:
  - GAME-VISION-01_REFERENCE_FIRST_OWNER_BASELINE.md
  - GAME-VISION-01_PREDECISION_ANALYSIS.md
  - ADR-0010-reference-and-evolved-world-product-profiles.md
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
```

## Outcome

Persist the owner's explicit acceptance that Reference uses a **hybrid upstream-tracking model**: Global Tibia is observed continuously, while every released Oteryn Reference revision remains immutable and changes reach a later Reference revision only through an explicit controlled promotion/release decision.

## Source of truth

- `USER_SOURCE`: on 2026-08-11, after the three tracking models were explained, the owner selected: `no to hybryda`.
- `PROVEN`: the existing Reference-first owner baseline already requires the evaluated Reference build to identify an immutable named Reference baseline/revision.
- `DERIVED`: accepting hybrid tracking resolves the long-term Reference tracking-policy question, but does not select a concrete Global Tibia patch/date, update cadence, migration mechanics, release naming, inclusion policy for every upstream change, or any other remaining GAME-VISION decision.

## Acceptance criteria

- [ ] Record continuous upstream observation/evidence intake.
- [ ] Record immutable released Reference revisions; no live mutation of released rules merely because Global changes.
- [ ] Require explicit promotion into a later Reference revision before upstream changes become Reference product semantics.
- [ ] Preserve reproducibility of tests, bug reports and parity evidence against the named revision.
- [ ] Leave exact cadence, concrete Global baseline, migration/rollback mechanics and revision naming unresolved.
- [ ] Keep full `GAME-VISION-01` explicitly `NOT ACCEPTED`.
- [ ] Include decision-timing, downstream-consumer, cost-of-delay and supersession-evidence records.
- [ ] No runtime/client/server/content/production implementation is authorized.
- [ ] Exact-head self-review and repository-required CI pass before merge.

## Validation

- base: `main@cd041f0da4e38ec87990a4924cb7a8a2b1f66f5e`
- open PRs at task start: 0
- component/integration/E2E: `NOT_APPLICABLE` — architecture documentation only
- exact-head self-review: pending
- exact-head CI: pending
- independent review: `NOT_REQUIRED` under current risk policy; no security/protocol/durable-data/production authority changes

## Context checkpoint

```yaml
last_progress: Owner accepted hybrid Reference tracking; task and branch created to persist only that partial GAME-VISION decision.
status: implementing
branch: docs/OTV2-20260811-reference-hybrid-owner-baseline
pr: null
final_head_sha: null
owner_action_required: null
blocker: null
next_action: Write the narrow hybrid Reference tracking owner baseline, then validate via PR exact-head self-review and CI.
```
