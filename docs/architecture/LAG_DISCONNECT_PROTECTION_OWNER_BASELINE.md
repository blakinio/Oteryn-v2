# Lag / Disconnect Protection Owner Baseline

- Status: Owner-accepted pre-contract baseline
- Date: 2026-08-07
- Decision owner: Oteryn project owner
- Coordination ID: `OTV2-NATIVE-FOUNDATION`
- Applies to: server-authoritative connection-health detection, PvE disconnect protection and later `FND-03` / `FND-04` contracts

## Purpose

Record the owner-accepted first gameplay rule for protection against genuine loss of Internet connectivity or loss of player control.

This baseline is architecture only. It does not authorize runtime implementation and does not yet freeze the final heartbeat format, transport timeout mechanism, monster AI implementation, PvP behavior, boss behavior, protection exhaustion policy or mass-outage compensation.

## Owner-accepted activation threshold

The initial gameplay-policy target is:

```text
0.0 s <= elapsed < 2.0 s  -> normal PvE monster attacks
elapsed >= 2.0 s          -> disconnect protection active
```

In player-facing terms, the first and second seconds after loss of sufficient server-authoritative control/liveness evidence remain normal combat. **From the beginning of the third second, all PvE monsters must stop actively attacking the disconnected/protected character.**

The activation boundary is therefore exactly **2.0 seconds elapsed**, not 3.0 seconds elapsed. Saying "from the third second" describes the interval that begins immediately after the first two full seconds have passed.

The timer is measured from server-observed state, not from an untrusted client statement such as `I have lag` or `I disconnected`.

The exact heartbeat packets, evidence aggregation and low-level state names remain later `FND-03` / `FND-04` work, but this gameplay-visible boundary is owner-accepted.

## Relationship to gameplay ticks

The owner selected the two-full-second boundary because Oteryn's intended Tibia-like combat/gameplay cadence uses a 2-second gameplay tick boundary for this class of behavior.

This does **not** require the authoritative Rust server main loop, scheduler or networking runtime to execute only once every 2 seconds. Internal simulation, liveness detection and transport processing may run at a finer cadence.

The architecture requirement is the gameplay result:

```text
last sufficient server-authoritative control/liveness evidence
        |
        | first 2 full seconds: normal PvE combat
        v
start of third second / elapsed >= 2.0 s
        |
        v
all PvE monsters stop actively attacking the protected actor
```

## Owner-accepted PvE monster behavior

From the beginning of the third second of continuous insufficient server-authoritative control/liveness evidence, **all PvE monsters must stop actively attacking the disconnected/protected character**, including monsters that were already targeting or engaged with that actor.

For architecture purposes, `stop actively attacking` means that while protection is active, monster AI does not emit any new offensive action against that protected actor. Existing targeting, aggro or threat bookkeeping may remain preserved internally, but it cannot continue producing attacks while protection is active.

Protection activation does not retroactively roll back authoritative gameplay that was already committed before the 2.0-second boundary.

Therefore, unless a later gameplay contract explicitly changes a case, effects already committed before activation may still resolve, including conceptually:

- an attack already authoritatively committed before the boundary;
- a projectile already emitted before the boundary;
- damage-over-time already applied;
- a field/hazard already present;
- an area effect already committed by the simulation.

No monster may begin or commit a **new** offensive action against the protected actor at or after the activation boundary while protection remains active.

The protection is not invulnerability.

## Aggro and combat-state preservation

Stopping all monster attacks must not be implemented by clearing authoritative combat state.

In particular, protection activation must not by itself:

- clear combat/PZ/logout lock;
- erase threat/aggro history merely to manufacture a clean state;
- heal HP, mana or resources;
- clear damage-over-time, debuffs, cooldowns or exhaustion;
- teleport or reposition the character;
- reset an encounter or instance;
- roll back committed actions;
- despawn the character solely because transport was lost;
- admit another character from the same account while the protected actor still has mandatory world presence.

The same authoritative in-world actor remains present.

A later gameplay contract must define the exact preserved aggro representation and how normal monster attacks resume after protection ends, but the disconnect path must not become a combat-reset exploit.

## Relationship to reconnect grace

This start-of-third-second protection boundary is separate from the already accepted reconnect continuity window:

```text
disconnect protection: first 2 full seconds normal; active from start of third second
reconnect grace window: 15 seconds
```

The 2.0-second elapsed boundary determines when the PvE protection policy becomes active.

The 15-second value determines the initial eligibility window in which the same logical `GameSessionId` may be resumed with a newer transport/connection generation, subject to later `FND-04` validation.

Neither threshold by itself permits combat escape, character duplication or state reset.

## Anti-abuse consequence

The architecture must assume that the server cannot reliably distinguish every genuine ISP/router failure from a player deliberately cutting connectivity.

Therefore the accepted protection must remain deterministic and bounded so deliberate disconnect cannot create a stronger state reset primitive.

The following anti-abuse mechanisms have been discussed but are **not owner-accepted by this baseline**:

- `Disconnect Protection Exhaustion`;
- a regenerating `Disconnect Protection Budget`;
- reduced protection after repeated disconnects;
- separate PvE/PvP/boss/high-value activity policies;
- telemetry-based suspicion scoring;
- mass-outage classification that bypasses individual exhaustion;
- any emergency defensive controller that heals, casts spells or otherwise plays the character.

These require separate owner decisions.

## Explicitly not decided here

This baseline does not yet decide:

- the exact liveness/heartbeat evidence required before the two-second timer is considered continuously elapsed;
- whether short packet loss below the threshold enters a named `DEGRADED` state;
- the exact monster-AI targeting/aggro data structure while attacks are suppressed;
- whether bosses use identical protection behavior;
- whether summons, environmental hazards or scripted encounter actors count as PvE monsters for this rule;
- PvP protection behavior;
- protection duration after activation;
- what happens if the player remains disconnected beyond the 15-second reconnect grace while mandatory world presence continues;
- how same-character recovery works after the reconnect grace expires;
- disconnect-protection exhaustion/budget rules;
- mass infrastructure failure compensation;
- final telemetry and Game Intelligence detector contract.

## Required consumers

This baseline is mandatory input to later:

- `FND-03` runtime/timer/state-transition design;
- `FND-04` connection liveness, reconnect and session state machine;
- gameplay combat/monster-AI policy;
- QA/E2E disconnect and reconnect scenarios;
- Game Intelligence telemetry design for disconnect-abuse analysis.

Tests must eventually prove at minimum that:

1. throughout the first two full seconds, normal PvE combat behavior is not silently rewritten by the protection system;
2. from the beginning of the third second (`elapsed >= 2.0 s`), every PvE monster stops emitting new offensive actions against the protected actor, including monsters that already had that actor targeted;
3. already committed effects from before the activation boundary are not rolled back by protection activation;
4. no new monster offensive action is committed against the actor while protection remains active;
5. reconnect resumes control of the same actor without healing, teleport, combat-state reset or duplicate authority;
6. stale old transport generations cannot resume command authority after reconnect;
7. deliberate repeated disconnects cannot create duplicate actors or account-level double-online state.

## Programme effect

Accepted now:

```text
first 2 full seconds after loss of sufficient server-authoritative control/liveness evidence -> normal PvE attacks
from start of third second / elapsed >= 2.0 s -> ALL PvE monsters stop actively attacking the protected character
already-targeting monsters are also suppressed from issuing new attacks
protection is not invulnerability and does not roll back gameplay committed before the boundary
2 s gameplay boundary remains separate from the accepted 15 s reconnect grace
2 s is a gameplay-policy boundary, not a requirement for a 2 s server main loop
```

No runtime, protocol, persistence, database, client or Platform implementation is authorized by this baseline.
