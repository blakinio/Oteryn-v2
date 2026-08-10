# OTV2-20260810-fnd04c-integration-closeout

```yaml
task_id: OTV2-20260810-fnd04c-integration-closeout
title: FND-04C error diagnostics failure compatibility integration
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/fnd04c-error-failure-compatibility-integration
issue: 130
programme_issue: 112
pr: null
trusted_base_sha: 3d07b3faaca683514fdfe6291e974f9195e2f763
owner: GPT-5.6 Sol architecture continuation session
created_at: 2026-08-10T13:12:00+02:00
updated_at: 2026-08-10T13:22:00+02:00
repair_cycles_for_current_gate: 1
max_repair_cycles_for_current_gate: 3
blocker: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260810-fnd04c-integration-closeout.md
  - docs/architecture/FND-04C_ERROR_DIAGNOSTICS_FAILURE_COMPATIBILITY_CONTRACT.md
  - docs/architecture/FND-04_IDENTITY_GAME_SESSION_ADMISSION_CHARACTER_LEASE_CONTRACT.md
  - docs/contracts/FOUNDATION_FAILURE_SCENARIOS.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
public_contracts:
  - docs/architecture/FND-04C_ERROR_DIAGNOSTICS_FAILURE_COMPATIBILITY_CONTRACT.md
  - docs/architecture/FND-04_IDENTITY_GAME_SESSION_ADMISSION_CHARACTER_LEASE_CONTRACT.md
  - docs/contracts/FOUNDATION_FAILURE_SCENARIOS.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
```

## Goal

Deliver the final bounded FND-04 gate after accepted/closed FND-04A and FND-04B. Integrate their semantics without duplication, close the diagnostics/correlation gap, freeze failure/compatibility/evidence obligations and prepare transition-safe final FND-04 completion.

## Normative inputs

Current `main@3d07b3faaca683514fdfe6291e974f9195e2f763`; accepted FND-04A/FND-04B and profiles; Foundation Error Vocabulary/Failure Scenarios; accepted FND-02/FND-03; accepted disconnect/re-entry owner decisions; Issue #112/#130; superseded #109 only as historical evidence where not contradicted.

## Scope

Included: complete FND-04 error/diagnostic/correlation catalogue; alias disposition; Foundation failure scenarios; producer/consumer compatibility rollout/rollback; implementation evidence gates; security/privacy integration; thin final FND-04 index; current programme status.

Excluded: runtime/protocol/persistence/Platform/KMS/deployment implementation; entitlement/Premium/VIP activation; gameplay/content implementation; numeric liveness/grace/re-arm/lease values; Platform repository writes.

## Repair history

### Cycle 1 — transition-safe programme status

Initial status wording would have become stale in the short but canonical interval after the FND-04C delivery merge and before lifecycle closeout: it said C was `VALIDATING` even though delivery would already be accepted.

Repair: the delivery candidate now records `FND-04C = FINAL DELIVERY / CLOSEOUT PENDING`. That statement is valid both before merge (final candidate validation is in progress) and after merge (only archival/ownership release remains). The separate closeout is explicitly required to update the same overlay to `FND-04C = ACCEPTED AND LIFECYCLE-CLOSED` and `FND-04 = ACCEPTED AND CLOSED` before programme #112 closes.

## Non-regression rules

- C integrates but does not silently modify A/B semantics;
- no opaque `compatibility_revision`;
- no historical `2s/5s/15s` timing resurrection; only exact 4s protection is frozen;
- source-age <=5s + anti-rollback trust/security remains binding;
- ownership-before-world remains binding;
- healthy-binding non-preemption, PREPARE/COMMIT, protection re-arm and no-guessed GameNode continuity remain binding;
- historical aliases conflicting with accepted A/B names are non-canonical rather than parallel production codes.

## Acceptance plan

- exact five-path diff / clean ancestry;
- full cross-contract Error Vocabulary review;
- scenario-to-error-to-mutation review;
- rollout/rollback and privacy review;
- exact-head Governance/Dependency/CodeQL PASS;
- zero unresolved material threads;
- terminal exact-head architecture/security review with zero material findings;
- squash merge unchanged accepted head;
- separate lifecycle closeout updates final status, archives/releases ownership and closes #130/#112.

Runtime/component/browser E2E: `NOT_APPLICABLE`; future implementation is gated by FND-04C evidence matrix.
