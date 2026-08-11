# OTV2-20260811-player-promise-owner-baseline

```yaml
task_id: OTV2-20260811-player-promise-owner-baseline
title: Persist GAME-VISION-01 player promise owner baseline
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260811-player-promise-owner-baseline
pr: null
base_sha: f28fc8c0d6646cd63122408028962fdf3dae961b
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-11T10:18:00+02:00
updated_at: 2026-08-11T10:18:00+02:00
execution_budget_minutes: 60
owned_paths:
  - docs/agents/tasks/active/OTV2-20260811-player-promise-owner-baseline.md
  - docs/architecture/GAME-VISION-01_PLAYER_PROMISE_OWNER_BASELINE.md
public_contracts:
  - docs/architecture/GAME-VISION-01_PLAYER_PROMISE_OWNER_BASELINE.md
depends_on:
  - GAME-VISION-01_REFERENCE_FIRST_OWNER_BASELINE.md
  - GAME-VISION-01_REFERENCE_HYBRID_TRACKING_OWNER_BASELINE.md
  - GAME-VISION-01_PREDECISION_ANALYSIS.md
  - ADR-0010-reference-and-evolved-world-product-profiles.md
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
```

## Outcome

Persist the owner's explicit acceptance of the internal Oteryn product/player promise: preserve recognizable Tibia depth, readability and persistent-world character; rebuild on a modern reliable native stack; and require intentional Oteryn differences from Reference to be explicit, versioned and measurable.

## Source of truth

- `USER_SOURCE`: on 2026-08-11, after the proposed promise was explained in concrete product terms, the owner answered `saakceptuje`.
- `PROVEN`: Reference-first and hybrid Reference tracking are already owner-accepted and lifecycle-closed.
- `DERIVED`: this acceptance resolves the internal product-promise question but does not freeze exact gameplay mechanics, public marketing wording, the full design-pillar set, first Evolved changes, PvP, solo/party emphasis, progression/risk or economy/scarcity policy.

## Acceptance criteria

- [ ] Record recognizable Tibia depth/readability/persistent-world identity as an internal product foundation without freezing exact mechanics.
- [ ] Record modern reliable native quality as part of the product promise, not authority for silent Reference divergence.
- [ ] Require intentional Oteryn differences to be explicit, versioned and measurable/reviewable against appropriate evidence.
- [ ] Preserve one canonical engine/client/`protocol-oteryn` and existing Reference/Evolved profile boundaries.
- [ ] Keep final public marketing wording and branding unresolved.
- [ ] Keep the remaining `GAME-VISION-01` owner decisions explicitly unresolved.
- [ ] Include mandatory decision-timing, downstream-consumer, cost-of-delay and supersession-evidence records.
- [ ] No runtime/client/server/content/production implementation is authorized.
- [ ] Exact-head self-review and repository-required CI pass before merge.

## Validation

- base: `main@f28fc8c0d6646cd63122408028962fdf3dae961b`
- open PRs at task start: 0
- component/integration/E2E: `NOT_APPLICABLE` — architecture documentation only
- exact-head self-review: pending
- exact-head CI: pending
- independent review: `NOT_REQUIRED` under current risk policy; this changes product-definition semantics only and no security/protocol/durable-data/production authority

## Context checkpoint

```yaml
last_progress: Owner accepted the explained Oteryn product/player promise; bounded task and baseline document created to persist only that partial GAME-VISION decision.
status: implementing
branch: docs/OTV2-20260811-player-promise-owner-baseline
pr: null
final_head_sha: null
owner_action_required: null
blocker: null
next_action: Validate the narrow baseline, open PR, freeze exact head, perform mandatory self-review and verify CI before merge.
```
