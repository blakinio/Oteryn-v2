# OTV2-20260808-reentry-pve-protection

```yaml
task_id: OTV2-20260808-reentry-pve-protection
title: Freeze four-second defensive PvE re-entry protection
mode: ARCHITECTURE_ONLY
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260808-reentry-pve-protection
pr: 96
base_sha: 19756eab0a66db37cb6f27ec367aaf2e4986df69
owner: Oteryn project owner
created_at: 2026-08-08T13:30:00+02:00
updated_at: 2026-08-08T17:51:00+02:00
execution_budget_minutes: 30
owned_paths:
  - docs/architecture/DISCONNECT_REENTRY_PVE_PROTECTION_OWNER_DECISION.md
  - docs/architecture/DISCONNECT_CLIENT_OS_FORENSICS_OWNER_DIRECTION.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
  - docs/agents/tasks/active/OTV2-20260808-reentry-pve-protection.md
public_contracts:
  - docs/architecture/DISCONNECT_REENTRY_PVE_PROTECTION_OWNER_DECISION.md
  - docs/architecture/DISCONNECT_CLIENT_OS_FORENSICS_OWNER_DIRECTION.md
depends_on:
  - LAG_DISCONNECT_PROTECTION_OWNER_BASELINE.md
  - LAG_DISCONNECT_REENTRY_ACTION_POLICY_OWNER_BASELINE.md
  - FND-ID-01_ACCOUNT_SINGLE_ONLINE_CHARACTER_OWNER_BASELINE.md
  - DISCONNECT_FORENSIC_EVIDENCE_OWNER_BASELINE.md
blocks:
  - FND-03/FND-04 must consume the reconciled re-entry protection semantics
  - later client diagnostics and ANL contracts must consume the client/OS corroborating-evidence direction
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Record the complete owner-accepted decision package from the 2026-08-08 disconnect/reconnect architecture discussion.

A valid reconnect/re-entry after an unexpected loss of playable control gives the same authoritative character a four-second defensive PvE protection window during which movement, self-healing, health/mana/resource potions and incoming healing from other players remain allowed, while the protected character may neither execute offensive actions against PvE monsters nor heal another player.

An accepted graceful logout followed by ordinary login does not create this protection window.

Also preserve the owner-accepted direction for bounded client/OS disconnect forensics so later contracts can distinguish observable evidence consistent with graceful exit, client crash, abrupt process loss, local network-interface loss, network-path loss, system crash/power interruption and Oteryn-side infrastructure failure without treating client evidence as authoritative proof of intent.

## Conflict resolved

The re-entry decision explicitly supersedes only the older generic `no protection / no invulnerability window` reconnect wording for this exact four-second PvE defensive window. All anti-reset, anti-duplication, session fencing, one-character-per-account and combat/PZ/logout invariants remain binding.

## Acceptance criteria

### Re-entry gameplay behavior

- [x] Freeze `reentry_pve_protection = 4 seconds`.
- [x] Limit protected re-entry to valid recovery after unexpected loss of playable control; accepted graceful logout/login does not manufacture the protection window.
- [x] Keep protection eligibility server-authoritative; client/OS evidence is not required synchronously to receive protection.
- [x] Allow ordinary self-healing subject to normal legality/cost/cooldown rules.
- [x] Allow health and mana/resource potion use subject to normal item/cooldown rules.
- [x] Preserve previously accepted movement permission.
- [x] Prohibit healing another player while the protected character remains inside the four-second window.
- [x] Allow the protected character to receive legal healing from another player.
- [x] Keep non-healing support actions unresolved for the owning combat/action contract.
- [x] Prohibit all offensive actions against PvE monsters during the window.
- [x] Prohibit buffering prohibited outgoing actions for post-protection execution.
- [x] Preserve already committed pre-protection effects.
- [x] Preserve ordinary resource consumption, cooldown, exhaustion, combat/PZ/logout state, threat/aggro and authoritative actor continuity.
- [x] Resolve the conflict with older generic no-protection reconnect wording explicitly and narrowly.
- [x] Keep PvP, non-healing support, non-combat interactions, UI and exact enforcement thresholds unresolved.

### Disconnect-abuse and forensic direction

- [x] Preserve server-generated disconnect/gameplay evidence as authoritative and client/OS evidence as corroborating only.
- [x] Record separate investigative classes for graceful exit, crash, abrupt process loss, NIC/interface loss, administrative interface-state change, network-path loss, system crash/power loss, infrastructure failure and unknown incidents without claiming intent from one event.
- [x] Reject unrestricted Event Viewer ingestion; allow only bounded, allowlisted, normalized incident evidence around the relevant episode.
- [x] Preserve native live network/interface-state observation plus bounded post-incident OS evidence as candidate implementation sources without freezing exact Windows APIs/providers/event IDs.
- [x] Preserve a client-side bounded rolling incident buffer as the preferred direction.
- [x] Preserve post-reconnect/post-boot submission of a bounded incident capsule when evidence could not be sent during the outage.
- [x] Preserve a lightweight independent launcher/guardian as an accepted design direction without freezing its process/transport details.
- [x] Keep a separate guardian diagnostic heartbeat as a candidate for later benchmark/contract rather than a frozen runtime requirement.
- [x] Record that guardian alive + game process lost + network alive is materially different evidence from simultaneous game/guardian/path loss.
- [x] Record that post-boot evidence may corroborate system crash, hard reset or power interruption where available without overclaiming the exact physical cause.
- [x] Record that abrupt process disappearance without normal crash evidence is suspicious but is not automatic proof of deliberate force-close.
- [x] Record that repeated local network-interface transitions around high-risk combat are a strong investigative signal but do not alone prove intent.
- [x] Require longitudinal Game Intelligence analysis combining combat risk, HP/resources, incoming damage, hostile pressure, reconnect timing, protection use, healing/potions, escape outcome, client/guardian/OS evidence and infrastructure correlation.
- [x] Preserve detection of unusually deterministic disconnect timing (for example repeated disconnects at similar risk/HP thresholds) as evidence potentially consistent with automation.
- [x] Require correlation with GameNode/runtime health and other affected players so Oteryn-side or regional failures are not misclassified as player abuse.
- [x] Prohibit automatic sanctions from one client/OS event or one disconnect episode.
- [x] Preserve Game Intelligence/AI as read-only investigative support; human-reviewed enforcement requires a separate policy.
- [x] Keep kernel-driver/invasive anti-cheat outside the scope of this decision.
- [x] Preserve privacy minimization: no arbitrary files, unrestricted process inventory, full Event Log export, unrelated SSID/MAC/device data, credentials or secrets.

### Coordination

- [x] Synchronize `FOUNDATION_PROGRAMME_CURRENT_STATUS.md` so PR #96 is an explicit required input before `FND-03`/`FND-04` finalize dependent reconnect/runtime semantics.
- [x] Preserve live/current-status precedence over stale long-lived coordination wording such as older `FND-02 is next` sentences.

### Governance

- [ ] Exact-head governance validation after final synchronization commit.
- [ ] Independent architecture review.
- [ ] Squash merge and task archive.

## Validation

Documentation-only architecture change. No runtime, protocol, persistence, database, client, launcher/guardian, Windows diagnostics, Platform, telemetry backend, Game Intelligence or production implementation is included.

## Context checkpoint

```yaml
last_progress: The full 2026-08-08 disconnect/reconnect discussion is captured in canonical architecture and the current programme-status overlay now requires FND-03/FND-04 to consume it. The package includes four-second defensive PvE re-entry behavior, graceful-logout exclusion, healing direction, non-buffering/anti-reset rules, bounded client/OS/Guardian forensics, incident classification, post-boot evidence, longitudinal automation/abuse analysis, privacy and human-review boundaries.
status: validating
branch: docs/OTV2-20260808-reentry-pve-protection
pr: 96
owned_paths:
  - docs/architecture/DISCONNECT_REENTRY_PVE_PROTECTION_OWNER_DECISION.md
  - docs/architecture/DISCONNECT_CLIENT_OS_FORENSICS_OWNER_DIRECTION.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
  - docs/agents/tasks/active/OTV2-20260808-reentry-pve-protection.md
next_action: Validate the exact PR head and obtain independent architecture review before squash merge.
```
