# OTV2-20260810-fnd04b-reconnect-recovery-continuity

```yaml
task_id: OTV2-20260810-fnd04b-reconnect-recovery-continuity
title: FND-04B reconnect recovery and continuity bounded contract
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/fnd04b-reconnect-recovery-continuity
issue: 127
programme_issue: 112
pr: 128
trusted_base_sha: 2fd7bac4879f381d5b97230732076df2e9c61f95
historical_reviewed_evidence_pr: 109
historical_reviewed_evidence_head: bf82e392d6ef8b1e627849cdc7383af9a7c987ae
owner: GPT-5.6 Sol architecture continuation session
created_at: 2026-08-10T12:50:00+02:00
updated_at: 2026-08-10T13:08:00+02:00
repair_cycles_for_current_gate: 2
max_repair_cycles_for_current_gate: 3
blocker: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260810-fnd04b-reconnect-recovery-continuity.md
  - docs/architecture/FND-04B_RECONNECT_RECOVERY_CONTINUITY_CONTRACT.md
  - docs/contracts/FND-04_REAUTHENTICATED_RECOVERY_GRANT_PROFILE_V1.md
public_contracts:
  - docs/architecture/FND-04B_RECONNECT_RECOVERY_CONTINUITY_CONTRACT.md
  - docs/contracts/FND-04_REAUTHENTICATED_RECOVERY_GRANT_PROFILE_V1.md
```

## Goal

Deliver bounded FND-04B from programme #112 after accepted FND-04A. Freeze reconnect, recovery and continuity authority/security semantics without runtime implementation and without duplicating FND-04C integration.

## Trusted inputs

Current `main@2fd7bac4879f381d5b97230732076df2e9c61f95`; accepted FND-04A/FND-02/FND-03; accepted disconnect/re-entry owner decisions; Foundation Error Vocabulary; Issue #127 / PR #128; superseded #109 as reviewed historical evidence only.

## Repair history

### Cycle 1 — structural schema vs semantic binding/profile/revision

Recovery profile schema now owns only claim membership/type/canonical lexical shape. Authenticated semantic `iss`/`aud`/`typ`/`purpose` mismatch maps to `RECOVERY_GRANT_BINDING_MISMATCH`; unsupported profile/protocol/transport or independent gameplay revision maps to `RECOVERY_GRANT_REVISION_UNSUPPORTED`. Invalid signature preempts otherwise well-formed semantic defects.

### Cycle 2 — grace origin, failover deadline continuity and reconnect-proof delivery

Review found that numeric grace may be deferred but its origin cannot be ambiguous, and proof rotation needed a safe lost-COMMIT-response contract.

Accepted repair:

- same-session grace begins exactly at the server-authoritative `ControlLossEpoch` boundary, never at socket close, first missed probe, cleanup or reconnect attempt;
- original grace deadline/remaining eligibility survives GameNode/runtime-owner replacement and may never restart on failover;
- `ControlLossEpoch` has internal non-reused discriminator/equivalent evidence and protection activation/expiry state survives failover, preventing a second 4-second window from restart/retry;
- PREPARE may deliver an **inactive candidate successor reconnect proof** bound to exact attempt/session/candidate generation/transport; it has no authority before COMMIT;
- COMMIT atomically activates candidate proof and fences predecessor proof;
- aborted/expired/superseded candidate proof is permanently invalid;
- same-attempt PREPARE/COMMIT reconciliation does not mint a second proof or authority transition;
- if a committed transport/proof is lost, predecessor proof never revives; reauthenticated recovery is required;
- ambiguous post-crash commit state must be reconstructed from fenced authority evidence before any further same-session authority, otherwise fail closed.

## Historical corrections retained

- historical `2s/5s/15s` values are non-canonical; only exact 4-second protection is frozen;
- no opaque `compatibility_revision`;
- verifier-anchored trust + deterministic crypto/schema precedence;
- source-age <=5s + anti-rollback security/trust evidence;
- AccountId->CharacterId before world/actor/controller classification.

## Validation plan

- exact three-path scope;
- architecture/profile/state-machine/race cross-check;
- protection/grace/proof exactly-once and failover continuity review;
- healthy-binding non-preemption review;
- stale generation/proof/prepared candidate fencing review;
- GameNode no-guessed-continuity review;
- exact-head Governance/Dependency/CodeQL PASS;
- zero unresolved material threads;
- terminal exact-head architecture/security review with zero material findings;
- squash merge unchanged accepted head;
- separate lifecycle closeout before FND-04C.

Runtime/component/browser E2E: `NOT_APPLICABLE`.
