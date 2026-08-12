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
updated_at: 2026-08-12T17:02:00+02:00
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

Produce one bounded paper-only `GAME-CHANNEL-01` candidate defining player/economy/social/PvP policy for the accepted multichannel technical model without redefining FND runtime/admission, DUR conservation, OPS/PERF orchestration/capacity or downstream gameplay domains.

No runtime/client/Rust implementation, PostgreSQL DDL/migration execution, Platform write, production configuration or entitlement activation is authorized. Shared canonical status/register/horizon/index/handoff remain untouched while PR #209 is open; acceptance promotion is a separate post-merge closeout.

## Source truth

- `PROVEN`: post-DUR-03 `main@f89685d585aab9c2ed3c69cabe8a4d9a2544bd0e` exposes `GAME-CHANNEL-01 = PROPOSED / PLANNED / NOT_STARTED` as the earliest remaining owner-accepted ordered paper-only product gate.
- `PROVEN`: FND-ID/ADR-0001 own Channel identity, one-World community/economy and fresh-session Channel change semantics.
- `PROVEN`: ADR-0009/FND-03 own runtime lifecycle/capacity/same-Channel recovery and prohibit silent alternate-Channel failure relocation.
- `PROVEN`: FND-04 owns exact target-bound final admission and no silent grant retarget.
- `PROVEN`: GAME-VISION binds party/PvP/economy fairness direction; DUR-03 binds value conservation/idempotency/stale-authority safety.
- `UNKNOWN`: exact PvP/boss/reward/source formulas and all numeric cooldown/queue/channel-count/capacity thresholds remain downstream/evidence-owned.

## Candidate closure

The candidate freezes:

1. one World economy/community/profile boundary with canonical `ChannelRef=WorldId+ChannelId`; labels are presentation only;
2. current eligible directory + non-authoritative recommendation + explicit eligible player target;
3. fail-closed stale/full/draining/recovering/incompatible target with fresh offer/grant and no silent retarget;
4. optional bounded target-Channel pre-admission queue, never GameSession/lease/value authority;
5. no first-generation destination queue/reservation while Character remains authoritative in source Channel;
6. privacy-bounded party/friend co-location hints with independent admissions and no party-owned Channel;
7. same-Channel reconnect distinct from completed fresh-session Channel switch;
8. existing combat/trade/DUR/event/instance/authority switch locks;
9. durable GAME-CHANNEL/world-policy anti-hopping guard scoped to Character+World, surviving GameSession/relog/reconnect/restart;
10. durable remembered previous successful ChannelRef (or equivalent unambiguous representation) so logout/relog cannot make same-vs-different Channel classification ambiguous;
11. first admission establishes prior Channel without counting as switch; same prior Channel fresh login is not switch; different Channel fresh login is switch even after old GameSession ended;
12. time-based voluntary cooldown + hard locks, numeric duration deliberately deferred;
13. destination admission + remembered Channel/guard advancement as one recovery-safe authoritative semantic outcome;
14. no mandatory new ChannelSwitchId; consume existing FND/ANL identities unless later lifecycle evidence requires one;
15. trusted non-voluntary exception only typed/audited/unforgeable and consequence-preserving;
16. fail-closed explicit multiplicity classification for every channel-sensitive value-producing source; runtime locality is not a durable-output fallback;
17. classes `CHANNEL_LOCAL_REPEATABLE`, `CHANNEL_LOCAL_SHARED_ELIGIBILITY`, `WORLD_SCOPED_UNIQUE`, `EXPLICIT_EVENT_POLICY_REQUIRED`;
18. distinct event simulation scope and durable eligibility scope;
19. no hidden inverse rate tuning; GAME-CHANNEL product envelope / PERF numbers / OPS orchestration;
20. local PvP execution with world/Character consequences surviving switching; exact formulas downstream;
21. one World guild/economy/rankings/accepted cross-channel communication with local speech/combat/position;
22. product states `SELECTABLE`, `CAPACITY_LIMITED`, `DRAINING`, `RECOVERING`, `UNAVAILABLE`;
23. same-Channel recovery first; alternate Channel only after proven safe actor state + fresh admission;
24. existing `world_policy_revision` for channel-policy compatibility;
25. WorldId change is separate world lifecycle/transfer, not Channel switch.

## Acceptance criteria

- [x] Identity/display/current placement separated.
- [x] Recommendation/explicit target separated from final FND-04 admission.
- [x] Target failure/queue semantics fail closed.
- [x] Live-session destination queue deferred.
- [x] Party/friend co-location hint semantics preserve independent authority/privacy.
- [x] ADR-0001 switch flow and hard blockers preserved.
- [x] Durable anti-hopping guard survives session/relog/reconnect/restart.
- [x] Prior successful Channel retained sufficiently to classify fresh logins as same/different after logout.
- [x] Destination admission + guard/prior-placement advance is one recovery-safe semantic outcome.
- [x] No unnecessary new ChannelSwitchId.
- [x] Trusted forced exception constrained.
- [x] Value-source multiplicity explicit/fail-closed with no runtime fallback.
- [x] Simulation scope and eligibility scope separated.
- [x] Scaling product/OPS/PERF ownership separated.
- [x] PvP/community/drain/recovery/world-policy/cross-world boundaries frozen without downstream formula capture.
- [x] Decision timing/supersession/deferred scope documented.
- [ ] Freeze exact final head after this metadata commit.
- [ ] Terminal exact-head full-diff self-review PASS.
- [ ] Required independent exact-head review PASS.
- [ ] Exact-head Agent Governance / Dependency Review / CodeQL PASS.
- [ ] Zero unresolved material review threads and clean ownership before merge.
- [ ] Separate post-merge lifecycle closeout promotes status/releases ownership.

## Excluded scope

Runtime/client/Rust, protocol gameplay payloads, PostgreSQL DDL/migrations, Platform writes, production deployment/configuration, numeric cooldown/queue/channel-count/capacity/autoscaling values, exact PvP/boss/reward/spawn/loot/economy formulas, downstream business state machines and entitlement/paid-priority activation.

## Repair history

### Cycle 1 — source multiplicity and switch-commit crash gap

Pre-freeze adversarial review found:

- ChannelRuntime locality could be misread as implicit `CHANNEL_LOCAL_REPEATABLE`; repaired to require explicit compiled/validated multiplicity classification for every channel-sensitive value-producing source, with missing classification fail-closed;
- cooldown wording allowed a crash gap between destination playable authority and guard advance; repaired so destination admission + guard advance is one authoritative/recovery-safe semantic outcome;
- clarified GAME-CHANNEL owns the Character+World guard rather than automatically GAME-CHAR, no ChannelSwitchId is mandatory, and WorldId changes are separate.

### Cycle 2 — logout/relog prior-Channel ambiguity

A second pre-freeze review found that a durable cooldown without durable prior-placement semantics could not reliably distinguish a fresh same-Channel login from a different-Channel switch after the old GameSession ended.

Repaired contract requires enough durable guard state to retain the previous successful ChannelRef (or equivalent unambiguous representation). First admission establishes baseline without a switch; same prior Channel login is not a switch; different Channel login is a switch even after logout; failed attempts do not move prior placement; successful different-Channel admission advances prior placement + guard atomically/recovery-safely.

## Validation

- source/option/ownership audit: complete
- net changed scope before final metadata commit: exactly task + analysis + contract; shared overlays untouched
- component/integration/runtime E2E: `NOT_APPLICABLE` — paper-only architecture
- final exact-head CI/reviews: pending freeze

## Independent review

Required: `YES` because multichannel/world-shared/value/reward/PvP/failure behavior can create authority, fairness and anti-duplication defects.

## PR and closeout

- PR #209 is ready for review;
- target diff: exactly 3 owned paths;
- no shared canonical overlay in delivery candidate;
- ownership releases only after separate lifecycle closeout.

## Context checkpoint

```yaml
last_progress: Repair cycle 2 closed logout/relog same-vs-different Channel classification by retaining durable prior successful Channel semantics; candidate/task/PR metadata are now ready for exact-head freeze.
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
repair_cycles_for_current_gate: 2
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: false
blocker: null
next_action: Verify exact branch diff/live-main ownership, freeze final head in PR evidence, then perform terminal self-review, independent review and exact-head CI without moving the head unless a material finding requires repair.
```
