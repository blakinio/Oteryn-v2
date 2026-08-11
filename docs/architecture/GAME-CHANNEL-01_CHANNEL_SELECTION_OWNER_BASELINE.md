# GAME-CHANNEL-01 — Channel Selection Owner Baseline

- Status: **OWNER_ACCEPTED PARTIAL BASELINE**
- Owner decision date: 2026-07-22
- Repository recording date: 2026-08-11
- Gate: `GAME-CHANNEL-01`
- Scope: login/world/character-selection channel UX only
- Source type: `USER_SOURCE`
- Full `GAME-CHANNEL-01` status: **NOT ACCEPTED**
- Does not authorize: runtime implementation, in-world switching, channel orchestration, PvP policy, anti-hopping policy, capacity thresholds, event/reward policy or production rollout

## 1. Purpose

This document persists a product-owner decision that predates the current `GAME-CHANNEL-01` pre-decision dossier and was not yet recorded in canonical repository architecture.

It intentionally freezes **only the already-decided selection UX**. It must not be used to infer answers to surrounding channel-policy questions.

## 2. Owner-accepted decision

### USER_SOURCE — accepted 2026-07-22

Oteryn uses **one Oteryn login flow**. Channels are not represented to the player as separate login servers requiring separate authentication/server-login flows.

Within the character/world selection experience:

- the player can see/select channel context rather than treating each channel as a separate game server/login destination;
- the normal path offers an **automatic/recommended channel**;
- the player retains a manual **`Change Channel`** choice.

This is the accepted product-selection model for the declared scope.

## 3. What this resolves in the pre-decision dossier

For this narrow scope, this owner baseline takes precedence over any option/recommendation wording in:

- `GAME-CHANNEL-01_PREDECISION_ANALYSIS.md`;
- `GAME-CHANNEL-01_PREDECISION_CAPACITY_TRIGGERS_ADDENDUM.md`.

The following questions are therefore **not open anymore**:

1. whether Oteryn should expose every channel as a separate login server — **NO**;
2. whether the default user path should require manual channel choice only — **NO**;
3. whether the client may provide an automatic/recommended channel choice — **YES**;
4. whether the player retains a manual channel-selection affordance — **YES**, represented by `Change Channel` in the accepted concept;
5. whether channel context belongs to the world/character selection flow — **YES**.

The parent dossier's broader recommendation of a “soft-visible sticky channel” model remains only partially resolved: the selection-flow visibility/default choice is accepted here, while in-session visibility/stickiness and switching mechanics remain open below.

## 4. Explicitly unresolved

The 2026-07-22 owner decision does **not** by itself establish:

- whether `Change Channel` executes directly while the character is actively in-world or first returns through a safe selection/session transition;
- the exact legal state required to change channel;
- party/friend automatic co-location semantics;
- whether a party leader/member can request `join their channel` while already in-world;
- anti-hopping eligibility/fencing or cooldown duration;
- PvP/combat restrictions beyond constraints already accepted elsewhere;
- channel capacity/create/drain/remove thresholds or orchestration;
- boss/raid/world-event runtime scope or reward eligibility;
- spawn/resource multiplication policy beyond already accepted system ownership;
- queue priority/fairness;
- recovery/failover behavior beyond accepted FND-04 and multichannel safety baselines;
- exact channel labels, numbering or final UI layout.

These remain for the owning `GAME-CHANNEL-01`, PvP/content, `PERF-01`, `OPS-CHANNEL-01` and UX contracts.

## 5. Architecture compatibility

This owner decision is compatible with the accepted architecture because:

- `WorldId` and `ChannelId` remain distinct identities;
- Platform/Gateway authentication remains a single control-plane flow rather than one identity silo per channel;
- selecting/recommending a channel does not make the client authoritative for admission;
- Gateway/World Registry/session admission still decides whether the selected/recommended channel is healthy, compatible and has capacity;
- manual choice cannot bypass FND-04 lease/session authority, capacity, compatibility, combat, transaction or other accepted safety rules;
- choosing another channel never changes the character's logical world/profile family.

No new wire/API/runtime shape is selected by this UX baseline.

## 6. Required downstream behavior

Future `GAME-CHANNEL-01` and client/admission design must preserve the following observable product intent:

```text
Oteryn login
-> authenticate once through the normal Oteryn/Platform flow
-> character/world selection
-> show/use channel context
-> offer automatic/recommended channel
-> retain manual Change Channel choice
-> server/Gateway remains authoritative for whether the requested channel can be admitted
```

A future UI may refine exact labels/layout, but it must not silently turn channels into separate login-server identities or remove the accepted recommended/manual-choice model without a superseding owner decision.

## 7. Acceptance boundary

This document is **accepted only for the declared partial scope**.

It does not make `GAME-CHANNEL-01` as a whole `ACCEPTED`. The remaining owner-decision packet from the pre-decision dossier still includes switching safety/placement, party co-location, anti-hopping, event/reward scope, PvP implications, social continuity, recovery presentation and capacity lifecycle semantics.

Any later decision that conflicts with this selection baseline must explicitly identify the superseded scope rather than silently drifting through client implementation.
