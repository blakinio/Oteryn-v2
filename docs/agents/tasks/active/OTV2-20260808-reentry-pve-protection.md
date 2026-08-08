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
updated_at: 2026-08-08T16:06:00+02:00
execution_budget_minutes: 30
owned_paths:
  - docs/architecture/DISCONNECT_REENTRY_PVE_PROTECTION_OWNER_DECISION.md
  - docs/agents/tasks/active/OTV2-20260808-reentry-pve-protection.md
public_contracts:
  - docs/architecture/DISCONNECT_REENTRY_PVE_PROTECTION_OWNER_DECISION.md
depends_on:
  - LAG_DISCONNECT_PROTECTION_OWNER_BASELINE.md
  - LAG_DISCONNECT_REENTRY_ACTION_POLICY_OWNER_BASELINE.md
  - FND-ID-01_ACCOUNT_SINGLE_ONLINE_CHARACTER_OWNER_BASELINE.md
blocks:
  - FND-03/FND-04 must consume the reconciled re-entry protection semantics
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Record the owner-accepted decision that a valid reconnect/re-entry gives the same authoritative character a four-second defensive PvE protection window during which movement, self-healing, health/mana/resource potions and incoming healing from other players remain allowed, while the protected character may neither execute offensive actions against PvE monsters nor heal another player.

## Conflict resolved

The new architecture decision explicitly supersedes only the older generic `no protection / no invulnerability window` reconnect wording for this exact four-second PvE defensive window. All anti-reset, anti-duplication, session fencing, one-character-per-account and combat/PZ/logout invariants remain binding.

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
- [ ] Exact-head governance validation.
- [ ] Independent architecture review.
- [ ] Squash merge and task archive.

## Validation

Documentation-only architecture change. No runtime, protocol, persistence, database, client, Platform or production implementation is included.

## Context checkpoint

```yaml
last_progress: Owner clarified healing direction for PR #96: the protected player cannot heal another player during the four-second window but may receive legal healing from other players; architecture and task records were updated accordingly.
status: validating
branch: docs/OTV2-20260808-reentry-pve-protection
pr: 96
owned_paths:
  - docs/architecture/DISCONNECT_REENTRY_PVE_PROTECTION_OWNER_DECISION.md
  - docs/agents/tasks/active/OTV2-20260808-reentry-pve-protection.md
next_action: Verify exact-head governance and independent architecture review on PR #96 before merge.
```
