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
disconnect_protection_activation = 2.0 seconds
```

The protection becomes eligible after **2.0 seconds without sufficient server-authoritative evidence that the player still has valid control/liveness**.

The timer is measured from server-observed state, not from an untrusted client statement such as `I have lag` or `I disconnected`.

The exact heartbeat packets, evidence aggregation and low-level state names remain later `FND-03` / `FND-04` work, but the gameplay-visible protection threshold is owner-accepted as 2 seconds.

## Relationship to gameplay ticks

The owner selected 2 seconds because Oteryn's intended Tibia-like combat/gameplay cadence uses a 2-second gameplay tick boundary for this class of behavior.

This does **not** require the authoritative Rust server main loop, scheduler or networking runtime to execute only once every 2 seconds. Internal simulation, liveness detection and transport processing may run at a finer cadence.

The architecture requirement is the gameplay result:

```text
last sufficient server-authoritative control/liveness evidence
        |
        | 2.0 s
        v
PvE disconnect protection becomes active
```

## Owner-accepted PvE monster behavior

Once the 2-second protection threshold is reached, **PvE monsters must stop actively attacking the disconnected/protected character**.

For architecture purposes, `stop actively attacking` means that while protection is active, monster AI does not emit new offensive actions against that protected actor.

Protection activation does not retroactively roll back authoritative gameplay that was already committed before the threshold was reached.

Therefore, unless a later gameplay contract explicitly changes a case, effects already committed before activation may still resolve, including conceptually:

- an attack already authoritatively committed;
- a projectile already emitted;
- damage-over-time already applied;
- a field/hazard already present;
- an area effect already committed by the simulation.

The protection is not invulnerability.

## Aggro and combat-state preservation

Stopping new monster attacks must not be implemented by clearing authoritative combat state.

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

This 2-second protection threshold is separate from the already accepted reconnect continuity window:

```text
disconnect protection activation = 2 seconds
reconnect grace window           = 15 seconds
```

The 2-second value determines when the PvE protection policy becomes active.

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

- the exact liveness/heartbeat evidence required before the 2-second timer is considered continuously elapsed;
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

1. before 2 seconds, normal PvE combat behavior is not silently rewritten by the protection system;
2. once the server-authoritative 2-second threshold is reached, monsters stop emitting new offensive actions against the protected actor;
3. already committed effects are not rolled back by protection activation;
4. reconnect resumes control of the same actor without healing, teleport, combat-state reset or duplicate authority;
5. stale old transport generations cannot resume command authority after reconnect;
6. deliberate repeated disconnects cannot create duplicate actors or account-level double-online state.

## Programme effect

Accepted now:

```text
PvE disconnect protection activates after 2.0 s of insufficient server-authoritative control/liveness evidence
once active, PvE monsters stop issuing new attacks against the protected character
protection is not invulnerability and does not roll back already committed gameplay
2 s protection activation remains separate from the accepted 15 s reconnect grace
2 s is a gameplay-policy threshold, not a requirement for a 2 s server main loop
```

No runtime, protocol, persistence, database, client or Platform implementation is authorized by this baseline.
