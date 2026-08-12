# OTV2-20260812-game-channel-01-architecture

```yaml
task_id: OTV2-20260812-game-channel-01-architecture
title: GAME-CHANNEL-01 multichannel product policy architecture
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: agent/otv2-20260812-game-channel-01-architecture
pr: 209
base_sha: f89685d585aab9c2ed3c69cabe8a4d9a2544bd0e
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: architecture-coordinator/current-session
created_at: 2026-08-12T16:16:00+02:00
updated_at: 2026-08-12T16:48:00+02:00
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

Produce one bounded paper-only `GAME-CHANNEL-01` candidate defining player/economy/social/PvP policy for the already accepted multichannel technical model without redefining FND runtime/admission, DUR conservation, OPS/PERF orchestration/capacity or downstream gameplay domains.

No Rust/runtime/client implementation, PostgreSQL DDL/migrations, Platform write, production configuration or entitlement activation is authorized. Shared canonical status/register/horizon/index/handoff files stay live-main while PR #209 is open; any `ACCEPTED/LIFECYCLE_CLOSED` promotion is a separate post-merge closeout.

## Architecture and source of truth

- `PROVEN`: `main@f89685d585aab9c2ed3c69cabe8a4d9a2544bd0e` closes DUR-03 and exposes `GAME-CHANNEL-01 = PROPOSED / PLANNED / NOT_STARTED` as the earliest remaining owner-accepted ordered paper-only product gate.
- `PROVEN`: ADR-0001 defines one World economy/community with independent Channel simulations and already fixes Channel change as safe source exit -> fresh destination authorization/admission -> fresh GameSessionId.
- `PROVEN`: FND-ID-01 defines `ChannelRef=WorldId+ChannelId`, topology-owned durable ChannelId, non-reuse after retirement and presentation label separate from identity.
- `PROVEN`: ADR-0009/FND-03 own ChannelRuntime/GameNode lifecycle/capacity/recovery; failed players recover the same ChannelId and are not silently moved to another simulation.
- `PROVEN`: FND-04 owns final admission and exact target-bound grants; no silent target retarget is allowed.
- `PROVEN`: GAME-VISION-01 binds solo viability, party reward, PvP secondary pillar, conservation before tuning and no duplicated group eligibility/hidden macro tuning.
- `PROVEN`: DUR-03 owns item/currency/value transaction idempotency, conservation, stale-authority rejection and reward/source duplicate prevention.
- `PROVEN`: no active/open GAME-CHANNEL owner existed at task start.
- `UNKNOWN`: exact PvP formulas, boss/reward business rules, numeric switch cooldown, queue limits, public Channel counts, capacity thresholds and economy targets remain unevidenced/downstream.

## Candidate closure

The candidate now defines:

1. **One World, many simulations:** Channel placement is session/runtime placement, never Character/economy/social/progression identity.
2. **Identity:** durable ChannelRef is canonical; labels/ordinals are presentation only.
3. **Entry:** current eligible-set + recommendation with explicit eligible player override; recommendation is never admission authority.
4. **Target failure:** stale/full/draining/recovering/incompatible target fails closed and requires a fresh offer/grant; no silent retarget.
5. **Queue:** optional bounded target-Channel pre-admission queue; never GameSession/lease/value authority; short-lived FND grant created/refreshed only when ready.
6. **No live-session destination reservation:** first generation preserves ADR-0001 safe source exit before destination queue/selection.
7. **Co-location:** party/friend placement is a privacy-bounded hint; independent FND admissions; no atomic group admission or party-owned Channel.
8. **Switch:** same-Channel reconnect is not a switch; completed switch uses fresh destination GameSession.
9. **Hard blockers:** combat/PvP, trade, DUR-03 mutation, protected event, unsafe instance/house/authority transition and target unavailability remain fail-closed.
10. **Anti-hopping:** durable `CharacterId+WorldId` guard owned by GAME-CHANNEL/world channel-policy authority, not automatically GAME-CHAR progression state; initial mechanism is time-based cooldown plus hard blockers, numeric duration deferred to evidence.
11. **Switch atomicity:** destination playable admission and durable guard advancement form one authoritative/recovery-safe semantic outcome; crash/retry cannot create a destination session while skipping guard advancement.
12. **No new identity by default:** no mandatory `ChannelSwitchId`; consume FND attempt/session and ANL correlation/operation identities unless later evidence proves a separate durable lifecycle.
13. **Trusted exceptions:** maintenance/incident exception may exist only as typed, audited, server/operator-authoritative behavior that cannot clear PvP/reward/value consequences.
14. **Fail-closed source classification:** Channel-local runtime placement does not automatically imply per-Channel durable output. Every channel-sensitive value-producing source/encounter family must explicitly compile/validate one supported multiplicity class; missing class blocks activation.
15. **Multiplicity classes:** `CHANNEL_LOCAL_REPEATABLE`, `CHANNEL_LOCAL_SHARED_ELIGIBILITY`, `WORLD_SCOPED_UNIQUE`, `EXPLICIT_EVENT_POLICY_REQUIRED`.
16. **Scope separation:** reward/event `simulation_scope` and `eligibility_scope` are different; ChannelId cannot silently enter shared reward reset keys.
17. **Scaling boundary:** product multiplicity semantics here; numeric capacity PERF-01; activation/orchestration OPS-CHANNEL-01; no hidden inverse rate tuning.
18. **PvP:** execution local, world/Character consequences survive switches; no failure/switch escape; exact formulas downstream.
19. **Community:** one guild/economy/ranking/world communications boundary; local speech/combat/position remain Channel-local.
20. **Availability/drain/recovery:** `SELECTABLE`, `CAPACITY_LIMITED`, `DRAINING`, `RECOVERING`, `UNAVAILABLE`; same-Channel recovery first; alternate Channel only after safe actor state + fresh admission.
21. **World-policy:** use existing `world_policy_revision`; switch guard and offers migrate/invalidate explicitly under policy changes.
22. **Cross-world:** WorldId change is not Channel switch and cannot bypass world-scoped value/profile/Character lifecycle policy.

## Acceptance criteria

- [x] WorldId/ChannelId/display/current-placement semantics separated; presentation cannot become durable authority.
- [x] Recommendation + explicit eligible selection separated from FND-04 final admission.
- [x] Explicit target failure fails closed with fresh offer/grant and no silent retarget.
- [x] Queue is bounded pre-admission/control-plane intent, not GameSession/lease/value authority.
- [x] First generation defers live-session destination queue/reservation.
- [x] Party/friend co-location is privacy-bounded hint with independent admissions and no party-owned Channel.
- [x] ADR-0001 fresh switch flow preserved; reconnect is not switch.
- [x] Hard switch blockers preserved.
- [x] Durable anti-hopping guard survives GameSession/reconnect/restart; numeric cooldown deferred.
- [x] Destination switch admission + guard advancement is one recovery-safe authoritative semantic outcome.
- [x] No mandatory new ChannelSwitchId without separate lifecycle evidence.
- [x] Trusted forced exceptions cannot be client forged or clear PvP/reward/value consequence.
- [x] Channel-sensitive value source multiplicity classification is explicit/fail-closed; runtime locality is not a fallback.
- [x] Simulation scope and durable eligibility scope remain separate.
- [x] Dynamic Channel multiplicity is explicit product/economy behavior; OPS/PERF own algorithms/numbers.
- [x] PvP consequence/hopping and same-Channel recovery constraints frozen without inventing PvP formulas.
- [x] One-World social/economy community semantics preserved.
- [x] Product-facing Channel lifecycle classes and drain/recovery behavior defined without redefining runtime state.
- [x] Existing `world_policy_revision` owns channel-policy compatibility; cross-world changes remain separate.
- [x] Downstream social/economy/event/reward/PvP/house/instance/entitlement ownership preserved.
- [x] Architecture decision timing/supersession/deferred scope documented.
- [ ] Freeze exact final head after current task/PR metadata is complete.
- [ ] Terminal exact-head full-diff self-review PASS.
- [ ] Required genuinely independent exact-head review PASS with zero material findings.
- [ ] Exact-head Agent Governance / Dependency Review / CodeQL PASS.
- [ ] Zero unresolved material review threads and clean ownership before squash merge.
- [ ] After accepted delivery merge, separate lifecycle closeout promotes status and releases ownership.

## Excluded scope

- runtime/client/Rust implementation and protocol gameplay message implementation;
- PostgreSQL DDL/migrations or physical queue/guard schema;
- Platform/Game Gateway writes;
- production deployment/configuration;
- numeric cooldown/queue/capacity/autoscaling values;
- exact PvP/boss/reward/spawn/loot/economy formulas;
- party/social/economy business state machines;
- entitlement activation or paid queue/switch priority.

## Repair history

### Repair cycle 1 — adversarial pre-freeze authority/economy audit

The first complete draft exposed two material failure windows and was repaired before final-head freeze:

1. **runtime-locality -> reward multiplicity ambiguity:** wording could have made ordinary ChannelRuntime placement an implicit `CHANNEL_LOCAL_REPEATABLE` value policy. The repaired contract requires explicit compiled/validated multiplicity classification for every channel-sensitive value-producing source; missing classification fails closed. A profile may author a bounded category default, but runtime has no implicit value fallback.
2. **switch cooldown crash gap:** wording recorded cooldown at successful destination entry without proving atomic relation to destination GameSession/placement authority. The repaired contract requires destination admission and durable switch-guard advance to be one authoritative/recovery-safe semantic outcome; no playable destination authority may exist while guard advancement is absent/unknown.

The same repair clarifies that the switch guard is GAME-CHANNEL/world channel-policy state scoped to Character+World rather than automatically GAME-CHAR progression state, that no new ChannelSwitchId is mandatory by default, and that WorldId changes are not Channel switches.

## Validation

### Focused

- source/option/ownership audit: complete for candidate drafting
- final net diff scope: pending after this task update
- governance/document/link validation: pending frozen exact head

### Component/integration

- `NOT_APPLICABLE` — paper-only architecture candidate

### E2E

- `NOT_APPLICABLE` — no executable runtime/client/production behavior

### Exact-head CI

- final head: pending freeze
- trigger source: PR #209
- workflow/run/job: pending
- result: pending

## Self-review

- exact head: pending freeze
- implementing/coordinating agent
- material findings: repair cycle 1 fixed before freeze; terminal review pending

## Independent review

- required: `YES` — multichannel/world-shared/value/reward/PvP/failure policy is high-risk for authority/fairness/anti-duplication
- exact head: pending
- auditor: independent mechanism on frozen head

## PR and closeout

- PR: #209 draft
- changed-file target: exactly task + analysis + candidate contract
- shared canonical status overlays: intentionally untouched until post-merge closeout
- ownership release: only after lifecycle closeout

## Context checkpoint

```yaml
last_progress: Candidate analysis/contract completed and adversarial repair cycle 1 closed runtime-locality reward-multiplicity fallback and destination-admission/switch-guard crash gap; task is ready for final diff/metadata freeze and terminal review/CI.
status: validating
branch: agent/otv2-20260812-game-channel-01-architecture
head_sha: null
pr: 209
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: pull_request #209
ci_check_generation: pending final freeze
ci_checks_for_current_head: 0
ci_run_ids: []
ci_job_ids: []
runner_assignment_state: unknown
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 1
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: false
blocker: null
next_action: Verify net diff is exactly the three owned paths and live main has not advanced; then freeze PR #209 head, perform terminal self-review, required independent review and exact-head CI.
```
