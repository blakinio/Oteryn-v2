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
updated_at: 2026-08-10T13:00:00+02:00
repair_cycles_for_current_gate: 1
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

Deliver only bounded FND-04B from replacement programme #112 after accepted FND-04A. Freeze reconnect, recovery and continuity authority/security semantics without runtime implementation and without duplicating the final FND-04C error/status integration layer.

## Trusted inputs

- `main@2fd7bac4879f381d5b97230732076df2e9c61f95`;
- accepted FND-04A fresh-admission authority/profile;
- accepted FND-02 transport/generation/reconciliation/liveness primitives;
- accepted FND-03 runtime ownership/fencing/recovery semantics;
- accepted disconnect/re-entry owner decisions and privacy/forensic baselines;
- Foundation Error Vocabulary;
- Issue #127 / programme #112 / delivery PR #128;
- superseded PR #109 exact head `bf82e392...` as reviewed historical evidence only.

## Scope

Included: reconnect proof; healthy-binding non-preemption; PREPARE/COMMIT; attempt reconciliation; server-authoritative liveness and `ControlLossEpoch`; one exact 4-second defensive PvE protection activation per eligible loss epoch; same-GameSession reconnect/reauth recovery; post-grace existing-actor recovery with new GameSession; recovery locator/current placement; GameNode replacement/fencing; independent revision bindings; recovery security profile; race/crash/failover evidence.

Excluded: runtime/protocol/persistence/Platform/KMS/deployment implementation; entitlement implementation; healthy-session migration protocol; final FND-04C integration.

## Repair history

### Cycle 1 — structural schema vs semantic binding/profile/revision classification

Initial profile tables used words such as `exact` for `iss`/`aud`/`purpose`/`profile`/protocol values while the normative precedence separately required authenticated binding or revision outcomes. That could let conforming implementations classify the same signed credential as `MALFORMED` versus `BINDING_MISMATCH`/`REVISION_UNSUPPORTED`.

Repair: authenticated payload schema now owns only claim membership, type and canonical lexical shape. After successful signature and structural schema validation, semantic `iss`/`aud`/`typ`/`purpose` mismatch maps to `RECOVERY_GRANT_BINDING_MISMATCH`; unsupported profile/protocol/transport or independent gameplay revision maps to `RECOVERY_GRANT_REVISION_UNSUPPORTED`. Invalid signature still preempts otherwise well-formed semantic defects. Recovery-profile fixtures explicitly cover this precedence.

## Mandatory historical corrections

- historical `2s/5s/15s` reconnect/liveness numbers are non-canonical; only the accepted 4-second protection is exact;
- no opaque `compatibility_revision`;
- verifier-anchored recovery trust scope + deterministic crypto/schema precedence;
- authenticated source-age <=5s + monotonic anti-rollback security/trust evidence;
- AccountId->CharacterId before world/actor/controller classification.

## Validation plan

- exact three-path scope from trusted main;
- architecture/profile cross-check and full state-machine/race review;
- verify protection epoch cannot be manufactured/reset;
- verify healthy current generation cannot be evicted by bearer proof;
- verify stale generation/proof/prepared candidate cannot command/fence winner;
- verify GameNode replacement never guesses continuity;
- full exact-head architecture/security self-review;
- exact-head Agent Governance, Dependency Review and CodeQL PASS;
- zero unresolved material threads;
- terminal exact-head architecture/security review with zero material findings;
- squash merge unchanged accepted head only;
- separate lifecycle closeout before FND-04C.

Runtime/component/browser E2E: `NOT_APPLICABLE` for architecture-only delivery.
