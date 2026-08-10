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
updated_at: 2026-08-10T12:56:00+02:00
repair_cycles_for_current_gate: 0
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
- accepted `FND-04A_AUTHORITY_FRESH_ADMISSION_CONTRACT.md` and fresh-admission grant profile;
- accepted FND-02 transport, `connection_generation`, command/session sequencing, snapshot/resync and authenticated liveness primitives;
- accepted FND-03 runtime ownership/fencing/recovery semantics;
- accepted disconnect/re-entry owner decisions and privacy/forensic baselines;
- Foundation Error Vocabulary;
- Issue #127 / programme #112 / delivery PR #128;
- superseded PR #109 exact head `bf82e392...` as reviewed historical evidence only.

## Scope

Included: reconnect secret/proof semantics; healthy-binding non-preemption; PREPARE/COMMIT rebind; idempotent attempt reconciliation; server-authoritative liveness and `ControlLossEpoch`; exactly-once 4-second defensive PvE protection per eligible loss epoch; same-GameSession reconnect and reauthenticated recovery; post-grace existing-actor recovery with a fresh GameSession; recovery locator/current runtime placement; GameNode replacement/fencing; independent recovery revision bindings; recovery credential security profile; replay/race/crash/failover evidence.

Excluded: Rust/protobuf/TLS implementation; database/cache schema; Platform writes; concrete KMS/HSM/vendor; deployment; production traffic; entitlement/Premium/VIP implementation; healthy-session migration protocol; final FND-04 cross-component error catalogue/status/failure-scenario integration (FND-04C).

## Mandatory corrections versus historical candidate

1. Do not reintroduce historical `2s/5s/15s` reconnect/liveness numbers. Only the already accepted defensive PvE re-entry protection duration is exact: **4 seconds**. Liveness probe cadence, control-loss threshold, stale transport cleanup deadline and same-session grace duration remain bounded but require later evidence-backed numeric registration.
2. Do not use opaque signed `compatibility_revision`. Recovery validates protocol, transport, ruleset, content, map and world-policy revisions independently.
3. Recovery profile must use the same deterministic crypto/schema/binding precedence and verifier-anchored trust selection accepted by FND-04A.
4. Recovery Platform-security and signing-key/profile evidence must preserve authenticated source observation age `<=5s`, monotonic/comparable anti-rollback ordering and fail-closed restart floor reconstruction.
5. AccountId->CharacterId ownership must be proven before world/actor/controller classification.

## Validation plan

- exact three-path scope from trusted main;
- architecture/profile cross-check;
- full state-machine and race review;
- verify same-session versus post-grace transition never resets actor state;
- verify `ControlLossEpoch` cannot be manufactured/reset by failed reconnect, graceful logout or healthy migration;
- verify healthy current generation cannot be evicted by bearer proof;
- verify old/prepared/stale connection generation cannot command/fence winner;
- verify GameNode replacement cannot infer continuity without fenced recoverable evidence;
- verify recovery profile cannot select trust from token semantics or silently downgrade;
- full exact-head architecture/security self-review;
- exact-head Agent Governance, Dependency Review and CodeQL PASS;
- zero unresolved material threads;
- terminal exact-head architecture/security review with zero material findings;
- squash merge unchanged accepted head only;
- separate lifecycle closeout before FND-04C.

Runtime/component/browser E2E: `NOT_APPLICABLE` for architecture-only delivery. Future implementation must execute the named reconnect/recovery/security/failover fixtures.
