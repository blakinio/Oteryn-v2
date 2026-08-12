# OTV2-20260812-game-channel-01-architecture

```yaml
task_id: OTV2-20260812-game-channel-01-architecture
title: GAME-CHANNEL-01 multichannel product policy architecture
mode: CONTRACT
status: investigating
repository: blakinio/Oteryn-v2
base_branch: main
branch: agent/otv2-20260812-game-channel-01-architecture
pr: null
base_sha: f89685d585aab9c2ed3c69cabe8a4d9a2544bd0e
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: architecture-coordinator/current-session
created_at: 2026-08-12T16:16:00+02:00
updated_at: 2026-08-12T16:16:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260812-game-channel-01-architecture.md
  - docs/architecture/GAME-CHANNEL-01_CHANNEL_PRODUCT_POLICY_ANALYSIS.md
  - docs/architecture/GAME-CHANNEL-01_CHANNEL_PRODUCT_POLICY_CONTRACT.md
public_contracts:
  - GAME-CHANNEL-01
depends_on:
  - ADR-0001
  - ADR-0009
  - GAME-VISION-01
  - FND-03
  - FND-04
  - GAME-CHAR-01
  - GAME-ITEM-01
  - DUR-03
blocks:
  - multichannel product feature semantics
  - VSL-MULTICHANNEL-01 product-policy readiness
  - profile-specific channel-switch / anti-hopping policy closure
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Produce one bounded paper-only `GAME-CHANNEL-01` architecture candidate that turns the already accepted multichannel technical capability into an explicit player/economy/social/PvP product policy without redefining runtime ownership, deployment orchestration, persistence, item/value conservation or downstream gameplay domains.

The candidate must freeze only the channel-facing product invariants needed before multichannel can become a player-visible product feature: channel discovery/selection semantics, co-location, queue meaning, channel-switch/anti-hopping policy, channel multiplicity and value-source implications, event/reward scope, PvP consequences, social/community safeguards, drain/recovery player behavior and the boundary between GAME-CHANNEL policy and `OPS-CHANNEL-01`/`PERF-01` implementation decisions.

No Rust/runtime/client implementation, PostgreSQL DDL/migrations, production deployment/configuration, Platform write or entitlement activation is authorized. Maintained status/register/horizon/index/handoff files remain unchanged while the delivery candidate is open; acceptance promotion is deferred to a separate post-merge lifecycle closeout.

## Architecture and source of truth

- `PROVEN`: `main@f89685d585aab9c2ed3c69cabe8a4d9a2544bd0e` records `DUR-03 = ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED` and `GAME-CHANNEL-01 = PROPOSED / PLANNED / NOT_STARTED` as the earliest remaining owner-accepted recommended-order paper-only product gate.
- `PROVEN`: ADR-0001 defines one logical World as one product/economy/community boundary and each Channel as an independent public-world simulation; it already freezes channel change as a fresh session/admission transition rather than teleport/rebind.
- `PROVEN`: ADR-0001 already prohibits channel switching during combat lock, direct trade, unresolved item mutation, protected encounter or instance transition and prohibits hopping-based reward duplication/escape from consequences.
- `PROVEN`: ADR-0009 owns GameNode/channel runtime lifecycle, measured capacity, dynamic process/channel orchestration and same-ChannelId recovery; failure must not silently move a player to another channel.
- `PROVEN`: GAME-VISION-01 requires `solo viable, party rewarded`, PvP as a secondary pillar, conservation before tuning, no hidden macro economy tuning and no duplicated group reward eligibility.
- `PROVEN`: FND-04 owns final admission and grants are explicitly bound to one `WorldId + ChannelId`; no silent retarget to another channel is allowed and successful completed channel transition creates a fresh game-domain session as required by ADR-0001/FND-04.
- `PROVEN`: the multichannel scope matrix keeps world-shared character/economy/social state separate from channel-local positions/creatures/combat/ground loot/local speech; party membership may be world-shared while shared-experience gameplay is channel-local for colocated members.
- `PROVEN`: accepted DUR-03 prevents channel multiplication/switching from becoming an item/currency duplication path and retains value conservation, reward/source idempotency, typed custody and cross-world isolation.
- `PROVEN`: no active GAME-CHANNEL task or open GAME-CHANNEL PR owned this scope at task start; active tasks were the non-owning foundation checkpoint plus unrelated disconnect/lag tasks.
- `UNKNOWN`: exact Reference PvP formulas, boss/event eligibility, numeric switch cooldowns, queue limits, channel-capacity thresholds and exact economic impact targets are not established by current accepted evidence and may not be invented here.

## Acceptance criteria

- [ ] Freeze the semantic difference between `WorldId`, canonical `ChannelId`, player-visible channel label and current-session channel placement; no presentation alias becomes durable authority.
- [ ] Define player channel discovery/selection so automatic recommendation and explicit player choice remain separate from final FND-04 admission authority.
- [ ] Define fail-closed behavior when an explicitly selected/authorized target becomes full, draining, stale or incompatible; no silent retarget using the same authorization.
- [ ] Define queue semantics as bounded pre-admission/control-plane intent rather than GameSession/CharacterLease/value authority, while deferring exact service placement and numeric limits.
- [ ] Define party/friend co-location as a recommendation/join convenience without creating party-owned channel authority or implicit teleport/migration.
- [ ] Preserve ADR-0001 channel change as a fresh safe session/admission transition and define durable anti-hopping/cooldown policy semantics that cannot be reset by reconnect/relog; defer unevidenced numeric duration.
- [ ] Define exactly when a successful channel switch starts/reset its anti-hopping policy and distinguish failed attempts from completed transitions.
- [ ] Define channel multiplicity policy so ordinary channel-local spawn/loot/resource sources, world-scoped uniqueness/eligibility, character/account cooldown eligibility and explicit event policy cannot be confused.
- [ ] Make dynamic channel opening/closure economically explicit rather than an accidental hidden source multiplier, while leaving measured capacity/orchestration triggers to PERF-01/OPS-CHANNEL-01.
- [ ] Define world-global boss/event/reward scope requirements: every feature must declare runtime simulation scope and durable eligibility scope; channel copies never imply repeated world/account/character reward eligibility.
- [ ] Define PvP/channel behavior so channel-local combat execution and world-scoped consequences remain distinct and hopping cannot evade combat/PvP consequences; exact profile formulas remain downstream/parity-owned.
- [ ] Define social/community safeguards preserving one world-wide community/economy identity while local speech/position/combat remain channel-local.
- [ ] Define player-visible channel lifecycle classes (eligible/open, full/capacity-limited, draining, recovering/unavailable) only as product semantics mapped from accepted runtime state, without redefining GameNode lifecycle.
- [ ] Preserve same-ChannelId recovery after failure and require an explicit safe fresh channel-change flow if recovery cannot continue; never silently relocate a live actor into another simulation.
- [ ] Define drain behavior that stops new admission and reaches a safe player/session boundary without hidden cross-channel migration.
- [ ] Preserve GAME-CHANNEL versus OPS/PERF ownership: product policy/allowed multiplicity and player behavior here; process placement, autoscaling algorithms, numeric capacity thresholds and recovery mechanics elsewhere.
- [ ] Preserve downstream ownership for economy/trade/social/party detailed mechanics, event/boss gameplay, rewards, houses, PvP formulas, DUR-03 conservation, FND admission/runtime and entitlement policy.
- [ ] Apply architecture-decision discipline: must-decide-now, blocked work, future migration cost, supersession evidence and deliberate deferrals.
- [ ] Complete exact-head full-diff self-review, required genuinely independent review, exact-head documentation/governance CI and zero unresolved material review findings before merge.
- [ ] After accepted merge, use a separate bounded lifecycle closeout to promote GAME-CHANNEL status and update canonical programme handoff; do not pre-promote shared overlays in the delivery PR.

## Excluded scope

- Rust/runtime/client implementation, gameplay message schemas or UI implementation.
- PostgreSQL DDL/migrations, queue storage schema, orchestration/deployment code, capacity benchmark numbers or production configuration.
- Platform/Game Gateway repository writes or implementation changes.
- Exact PvP/skull/frag/combat formulas, encounter/boss mechanics, social/guild/party business logic, market/economy formulas or reward definitions.
- Exact numeric channel-switch cooldown, queue timeout/length, max channels/world, max players/channel or autoscaling thresholds without product/PERF evidence.
- Reopening ADR-0001 fresh channel-transition semantics, FND-04 admission authority, ADR-0009 same-channel recovery, DUR-03 conservation or accepted world/channel ownership.
- Monetization/Premium/VIP or `PROD-ENTITLEMENTS-01` activation.

## Implementation / findings

Preflight consumed post-DUR-03 `main@f89685d585aab9c2ed3c69cabe8a4d9a2544bd0e`, confirmed no active/open GAME-CHANNEL owner, and created one dedicated paper-only branch. Shared canonical status/register/horizon/index/handoff files are intentionally outside delivery ownership so the candidate cannot mark itself accepted before delivery merge + lifecycle closeout.

## Validation

### Focused

- source/ownership/option audit: in progress
- governance/document/link review: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — paper-only architecture candidate; no executable component change
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no runtime/client/production behavior is introduced
- result: `NOT_APPLICABLE`

### Exact-head CI

- final head: pending
- trigger source: pending
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Self-review

- exact head: pending
- method/reviewer: implementing/coordinating agent
- material findings: pending
- verdict: pending

## Independent review

- required: `YES` — GAME-CHANNEL changes multichannel product, reward anti-hopping, PvP consequence, world-shared/channel-local and failure/recovery policy boundaries, which can create value/authority/fairness errors if inconsistent with accepted FND/DUR architecture
- exact head: pending
- method/auditor: genuinely independent mechanism on frozen exact head
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related open PRs: unrelated work only; no GAME-CHANNEL overlap at preflight
- protected auto-merge: not configured
- merge commit/result: pending
- ownership release: after terminal lifecycle closeout only

## Context checkpoint

```yaml
last_progress: Post-DUR-03 main verified; GAME-CHANNEL-01 claimed on a dedicated paper-only branch with no overlapping task/PR ownership and accepted multichannel/product/runtime/value inputs identified.
status: investigating
branch: agent/otv2-20260812-game-channel-01-architecture
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
owner_action_required: false
blocker: null
next_action: Complete the bounded GAME-CHANNEL source/option audit and draft analysis plus candidate contract without modifying shared canonical status overlays.
```
