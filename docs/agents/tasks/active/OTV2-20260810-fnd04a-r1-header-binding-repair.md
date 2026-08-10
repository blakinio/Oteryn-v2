# OTV2-20260810-fnd04a-r1-header-binding-repair

```yaml
task_id: OTV2-20260810-fnd04a-r1-header-binding-repair
title: FND-04A-R1 deterministic protected-header/binding validation repair
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/fnd04a-r1-header-binding-repair
issue: 120
programme_issue: 112
pr: null
supersedes_delivery_pr: 114
superseded_delivery_head: 79678485d009c22ece2736c822d6b75b6d235ad2
trusted_base_sha: 43ca28f1f0f259c08a275c92946aa35f05d4d112
reconstruction_squash_sha: 6c34e48e868b604b824f079920694d007f7eb493
owner: GPT-5.6 Sol architecture continuation session
created_at: 2026-08-10T11:05:00+02:00
updated_at: 2026-08-10T11:05:00+02:00
repair_cycles_for_current_gate: 1
max_repair_cycles_for_current_gate: 3
final_head_sha: null
final_head_frozen_at: null
owner_action_required: null
blocker: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260810-fnd04a-r1-header-binding-repair.md
  - docs/architecture/FND-04A_AUTHORITY_FRESH_ADMISSION_CONTRACT.md
  - docs/contracts/FND-04_PRE_ADMISSION_GRANT_PROFILE_V1.md
public_contracts:
  - docs/architecture/FND-04A_AUTHORITY_FRESH_ADMISSION_CONTRACT.md
  - docs/contracts/FND-04_PRE_ADMISSION_GRANT_PROFILE_V1.md
```

## Goal

Deliver the bounded successor repair authorized by the product owner after PR #114 exhausted its `3/3` repair budget and an exact-head terminal review found one material interoperability contradiction. This task is a new gate with its own repair budget; it is not a fourth repair cycle on #114.

## Source / provenance

- current trusted reconstruction base: `main@43ca28f1f0f259c08a275c92946aa35f05d4d112`;
- reviewed but unmerged exhausted candidate: PR #114 exact head `79678485d009c22ece2736c822d6b75b6d235ad2`;
- staging reconstruction was squashed once onto the fresh current-main branch as `6c34e48e868b604b824f079920694d007f7eb493`, preserving content without importing #114's 11-commit history;
- all previously repaired #114 semantics remain candidate evidence unless explicitly changed by the single R1 finding below;
- Issue #120 records the owner disposition and bounded successor acceptance criteria.

## Material terminal finding carried from #114

The v1 profile simultaneously required an early `exact protected header/profile` check before signature verification and required a correctly signed wrong `typ` to map to `ADMISSION_GRANT_BINDING_MISMATCH` after authentication.

Because `typ` is itself a protected JOSE header member, conforming fail-fast consumers could classify the same token differently. That violates deterministic cross-component error semantics and risks exposing semantic binding information for unauthenticated tokens.

## Accepted R1 repair

The successor candidate now freezes this precedence:

```text
malformed protected-header structure
-> ADMISSION_GRANT_MALFORMED

structurally valid header
+ key trust/signature failure
-> ADMISSION_GRANT_AUTHENTICATION_FAILED

structurally valid header
+ successful signature
+ wrong exact typ/iss/aud/purpose
-> ADMISSION_GRANT_BINDING_MISMATCH
```

Specifically:

1. pre-signature processing validates JWS/parser bounds, exact `alg`, exact allowed protected-member set, `kid` syntax, syntactically valid bounded `typ`, and forbidden-member absence;
2. semantic exact `typ=oteryn-admission+jwt` comparison is deferred until trusted key lookup and successful Ed25519 verification;
3. malformed/missing/null/non-string/out-of-bound `typ` remains `ADMISSION_GRANT_MALFORMED`;
4. structurally valid wrong `typ` with failed/untrusted signature remains `ADMISSION_GRANT_AUTHENTICATION_FAILED` without a binding oracle;
5. correctly signed wrong exact `typ` maps deterministically to `ADMISSION_GRANT_BINDING_MISMATCH`, together with wrong exact `iss`/`aud`/`purpose`;
6. unsupported payload `profile` remains `ADMISSION_GRANT_REVISION_UNSUPPORTED`.

## Scope preserved from FND-04A

The successor keeps the #114 accepted candidate semantics for:

- Platform attempt versus game-domain final authority;
- AccountPresenceClaim, CharacterLease, GameSession, initial TransportBinding and RuntimeScopeAuthority separation;
- atomic fresh-admission revalidation/commit;
- current AccountId->CharacterId before CharacterId->WorldId/world-eligibility ordering;
- no stale-world retarget;
- independent protocol/transport/ruleset/content/map/world-policy/offer revisions;
- GrantNonce versus AdmissionAttemptRef;
- account-global duplicate-login non-preemption;
- authenticated source-age <=5s security/trust evidence and monotonic anti-rollback fences;
- complete FND-04A error-vocabulary rows;
- no reconnect/recovery/PREPARE-COMMIT implementation or finalization.

## Explicit exclusions

No Rust runtime, protocol codec/schema implementation, persistence schema, Platform write, KMS/HSM/vendor selection, deployment, production traffic, FND-04B reconnect/recovery semantics, FND-04C integration, entitlement implementation or Premium/VIP activation.

## Validation plan

- verify branch ancestry starts from exact current trusted main and reconstruction added only reviewed #114 content;
- verify final changed paths versus main are exactly this active task plus the two FND-04A public contracts;
- verify no stale #114 active task remains in the successor diff;
- verify architecture/profile agree on protected-header structural checks, authentication precedence and post-signature `typ` binding classification;
- verify malformed `typ`, wrong-well-formed-`typ` + invalid signature, and correctly signed wrong `typ` fixtures are all explicit;
- verify all prior #114 P1/P2 repairs remain intact;
- verify current-main entitlement dependency remains separate and does not alter FND-04A semantics;
- perform full exact-head architecture/security self-review;
- freeze exact final head only after PR metadata/task provenance are complete;
- require exact-head Agent Governance, Dependency Review and CodeQL PASS;
- require zero unresolved material review threads;
- require one terminal exact-head architecture/security review with zero material findings;
- squash merge unchanged accepted head only.

Runtime/component/browser E2E: `NOT_APPLICABLE` because this gate changes architecture/documentation only. Future implementation must execute the named interoperability/security fixtures.

## Current checkpoint

```yaml
status: validating
last_progress: FND-04A candidate reconstructed onto current main; terminal typ-order contradiction repaired in both public contracts; stale #114 active task removed and successor task registered.
repair_cycles_for_current_gate: 1
next_action: open bounded successor PR to main, bind its number into this task before final freeze, then run full diff review and exact-head validation.
```
