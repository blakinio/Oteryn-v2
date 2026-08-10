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
updated_at: 2026-08-10T13:12:00+02:00
repair_cycles_for_current_gate: 0
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

Deliver the final bounded FND-04 gate after accepted/closed FND-04A and FND-04B. Integrate their accepted semantics without duplicating or weakening them, close the carried diagnostics/correlation gap, freeze failure/compatibility/evidence obligations and transition the Foundation programme status to FND-04 accepted when this delivery merges.

## Normative inputs

- current `main@3d07b3faaca683514fdfe6291e974f9195e2f763`;
- accepted FND-04A fresh-admission contract/profile;
- accepted FND-04B reconnect/recovery contract/profile;
- Foundation Error Vocabulary;
- Foundation Failure Scenario Catalogue;
- accepted FND-02/FND-03;
- accepted disconnect/re-entry owner decisions;
- Issue #112 / #130;
- superseded #109 only as historical reviewed evidence for names not contradicted by A/B.

## Scope

Included: complete FND-04 cross-component error/diagnostic/correlation catalogue; superseded-alias disposition; Foundation failure scenarios; producer/consumer compatibility and rollout/rollback contract; implementation acceptance evidence gates; security/privacy integration; thin final FND-04 index; current programme status.

Excluded: runtime/protocol/persistence/Platform/KMS/deployment/production implementation; entitlement/Premium/VIP activation; gameplay/content implementation; numerical liveness/grace/re-arm values; Platform repository writes.

## Non-regression rules

- FND-04C integrates but does not silently modify accepted A/B semantics;
- no opaque `compatibility_revision`;
- no historical `2s/5s/15s` reconnect timing resurrection;
- only accepted exact 4-second defensive PvE protection remains frozen;
- Platform-security and key/profile trust source-age <=5s + anti-rollback semantics remain binding;
- ownership-before-world ordering remains binding for both admission and recovery;
- healthy-binding non-preemption, PREPARE/COMMIT fencing, protection re-arm and no-guessed GameNode continuity remain binding;
- historical aliases conflicting with accepted A/B names must be explicitly non-canonical, not implemented alongside them.

## Acceptance plan

- exact five-path diff on fresh trusted main;
- full cross-contract consistency and Foundation Error Vocabulary review;
- scenario-to-error-to-mutation matrix review;
- rollout/rollback and privacy review;
- full exact-head architecture/security self-review;
- exact-head Agent Governance, Dependency Review and CodeQL PASS;
- zero unresolved material review threads;
- terminal exact-head architecture/security review with zero material findings;
- squash merge unchanged accepted head;
- separate lifecycle closeout archives/releases ownership and closes #130/#112.

Runtime/component/browser E2E: `NOT_APPLICABLE` for architecture-only delivery. Future implementation is gated by the evidence matrix defined by FND-04C.
