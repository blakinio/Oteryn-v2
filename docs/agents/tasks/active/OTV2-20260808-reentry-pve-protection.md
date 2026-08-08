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
updated_at: 2026-08-08T16:20:00+02:00
execution_budget_minutes: 30
owned_paths:
  - docs/architecture/DISCONNECT_REENTRY_PVE_PROTECTION_OWNER_DECISION.md
  - docs/architecture/DISCONNECT_CLIENT_OS_FORENSICS_OWNER_DIRECTION.md
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

Record the owner-accepted decision that a valid reconnect/re-entry gives the same authoritative character a four-second defensive PvE protection window during which movement, self-healing, health/mana/resource potions and incoming healing from other players remain allowed, while the protected character may neither execute offensive actions against PvE monsters nor heal another player.

Also preserve the owner-accepted direction for bounded client/OS disconnect forensics so later contracts can distinguish observable evidence consistent with graceful exit, client crash, abrupt process loss, local network-interface loss, network-path loss, system crash/power interruption and Oteryn-side infrastructure failure without treating client evidence as authoritative proof of intent.

## Conflict resolved

The re-entry decision explicitly supersedes only the older generic `no protection / no invulnerability window` reconnect wording for this exact four-second PvE defensive window. All anti-reset, anti-duplication, session fencing, one-character-per-account and combat/PZ/logout invariants remain binding.

## Acceptance criteria

- [x] Freeze `reentry_pve_protection = 4 seconds`.
- [x] Allow ordinary self-healing subject to normal legality/cost/cooldown rules.
- [x] Allow health and mana/resource potion use subject to normal item/cooldown rules.
- [x] Preserve previously accepted movement permission.
- [x] Prohibit healing another player while the protected character remains inside the four-second window.
- [x] Allow the protected character to receive legal healing from another player.
- [x] Keep non-healing support actions unresolved for the owning combat/action contract.
- [x] Prohibit all offensive actions against PvE monsters during the window.
- [x] Prohibit buffering prohibited outgoing actions for post-protection execution.
- [x] Preserve already committed pre-protection effects.
- [x] Resolve the conflict with older generic no-protection reconnect wording explicitly and narrowly.
- [x] Keep PvP, non-healing support, non-combat interactions, UI and enforcement thresholds unresolved.
- [x] Preserve server-generated disconnect/gameplay evidence as authoritative and client/OS evidence as corroborating only.
- [x] Record separate investigative classes for graceful exit, crash, abrupt process loss, NIC/interface loss, network-path loss, system crash/power loss, infrastructure failure and unknown incidents without claiming intent from one event.
- [x] Reject unrestricted Event Viewer ingestion; allow only bounded, allowlisted, normalized incident evidence.
- [x] Preserve a client-side bounded rolling incident buffer as the preferred direction.
- [x] Preserve a lightweight independent launcher/guardian as an accepted design direction without freezing its process/transport details.
- [x] Keep a separate guardian diagnostic heartbeat as a candidate for later benchmark/contract rather than a frozen runtime requirement.
- [x] Record that post-boot evidence may corroborate system crash/power interruption where available.
- [x] Require longitudinal Game Intelligence analysis and prohibit automatic sanctions from one client/OS event.
- [x] Keep kernel-driver/invasive anti-cheat outside the scope of this decision.
- [ ] Exact-head governance validation.
- [ ] Independent architecture review.
- [ ] Squash merge and task archive.

## Validation

Documentation-only architecture change. No runtime, protocol, persistence, database, client, launcher/guardian, Windows diagnostics, Platform, telemetry backend, Game Intelligence or production implementation is included.

## Context checkpoint

```yaml
last_progress: Owner accepted preservation of the client/OS disconnect-forensics ideas. PR #96 now records bounded allowlisted OS evidence, incident classification, post-boot crash/power evidence, a preferred client forensic ring, a lightweight launcher/guardian direction, and a candidate separate guardian heartbeat while retaining server evidence as authoritative.
status: validating
branch: docs/OTV2-20260808-reentry-pve-protection
pr: 96
owned_paths:
  - docs/architecture/DISCONNECT_REENTRY_PVE_PROTECTION_OWNER_DECISION.md
  - docs/architecture/DISCONNECT_CLIENT_OS_FORENSICS_OWNER_DIRECTION.md
  - docs/agents/tasks/active/OTV2-20260808-reentry-pve-protection.md
next_action: Re-run exact-head governance and independent architecture review on PR #96 before merge.
```
