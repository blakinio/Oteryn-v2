# FND-04C — Error, Diagnostics, Failure and Compatibility Integration Contract

- Status: Candidate final integration contract; canonical only when the owning FND-04C delivery merges
- Gate: `FND-04C`
- Programme: Issue #112
- Owning delivery: Issue #130
- Repository: `blakinio/Oteryn-v2`
- Trusted base: `main@3d07b3faaca683514fdfe6291e974f9195e2f763`
- Normative component contracts: accepted FND-04A + FND-04B and their two grant profiles
- Consumes: Foundation Error Vocabulary; Foundation Failure Scenario Catalogue; FND-ID-01; FND-02; accepted FND-03; ADR-0003; ADR-0012; accepted disconnect/re-entry decisions
- Historical evidence only: superseded PR #109; historical names do not override accepted A/B semantics
- Does not authorize: runtime/protocol/persistence/Platform/KMS/deployment/production implementation

## 1. Purpose and precedence

FND-04C closes the final integration surface without reopening accepted FND-04A/B semantics.

```text
FND-04A owns fresh-admission authority/profile semantics.
FND-04B owns reconnect/recovery/continuity and recovery-profile semantics.
FND-04C owns cross-component errors/diagnostics, failure-scenario disposition,
compatibility/rollout obligations, implementation evidence and final FND-04 indexing.
```

If C cannot faithfully represent an accepted A/B rule, C is invalid; C never silently rewrites A/B.

## 2. Common Foundation error envelope

Every FND-04 cross-component failure defines:

```text
error_code
category
progression = RETRYABLE | TERMINAL | SECURITY_TERMINAL
retry_authority
mutation_outcome / idempotency outcome
public_class
redacted_diagnostic
request_trace_id
safe_correlation
```

No exception string, SQL error, parser stack, raw credential or private fence becomes API behavior.

### 2.1 Correlation/privacy policy

Potentially safe fields, only after the relevant authentication/authorization boundary and when policy permits:

- `request_trace_id`;
- AdmissionAttemptRef / recovery `attempt_ref` / ReconnectAttemptRef;
- GameSessionId as controlled diagnostic correlation, never bearer proof;
- WorldId/ChannelId where operational policy permits;
- profile ID and `safe_kid` where policy permits;
- revision dimension class and non-secret revision ID where approved;
- generation relation class (`current`, `stale`, `superseded`) rather than raw private fence values;
- evidence source class, source-age bucket, source-order/rollback class;
- lifecycle/controller/placement decision class.

Never include raw admission/recovery JWT, GrantNonce/RecoveryGrantNonce, reconnect/candidate proof, OAuth/Game Login Ticket, private/PoP key material, Platform security-generation value, raw private lease/scope/connection fencing value, unauthenticated semantic token values, unnecessary transfer/handoff detail, or AccountId/CharacterId as ordinary high-cardinality metric labels.

## 3. Mutation/idempotency vocabulary

- `NO_AUTHORITY_MUTATION` — rejected candidate commits no new presence/lease/session/transport/runtime authority.
- `COMMITTED_OR_RECONCILE_REQUIRED` — prior transition may already have committed; reconcile exact attempt/current authority before independent retry.
- `ISSUANCE_RECONCILE_REQUIRED` — producer may already have issued one capability; same-operation reconciliation or deterministic retirement only.
- `BOUNDED_CURRENT_LEASE_ONLY` — retry may preserve only already-current CharacterLease authority before an evidence-backed fail-safe deadline; it never grants replacement authority.
- `CURRENT_AUTHORITY_PRESERVED` — whatever authority is current at revalidation remains current; PREPARE-time state is not restored.

## 4. Canonical FND-04 error catalogue

This is the complete FND-04 integration catalogue. Component-owned progression/retry/mutation semantics remain identical to accepted A/B/profile contracts.

### 4.1 Fresh admission

| Code | Category | Progression | Retry authority | Mutation / idempotency | Public class | Redacted diagnostic | Safe correlation |
|---|---|---|---|---|---|---|---|
| `ADMISSION_GRANT_MALFORMED` | `INVALID_INPUT` | `TERMINAL` | newly issued valid capability; never same malformed grant | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `fresh admission grant malformed` | parser/schema stage; authenticated safe profile/header class only |
| `ADMISSION_GRANT_AUTHENTICATION_FAILED` | `AUTHENTICATION_FAILED` | `SECURITY_TERMINAL` | restart authenticated issuance; never same rejected credential | `NO_AUTHORITY_MUTATION` | `AUTHENTICATION_REQUIRED` | `fresh admission credential authentication failed` | safe algorithm/key/trust decision class |
| `ADMISSION_GRANT_BINDING_MISMATCH` | `SESSION_REJECTED` | `SECURITY_TERMINAL` | newly issued correct-bound grant | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `fresh admission credential bound to a different context` | authenticated mismatch dimension only |
| `ADMISSION_GRANT_NOT_YET_VALID` | `SESSION_REJECTED` | `RETRYABLE` | same unconsumed grant after accepted nbf boundary only while all other bindings remain current | `NO_AUTHORITY_MUTATION` | `TEMPORARILY_UNAVAILABLE` | `fresh admission grant not yet active` | trusted-time boundary class |
| `ADMISSION_GRANT_EXPIRED` | `SESSION_REJECTED` | `TERMINAL` | fresh Gateway/issuer attempt | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `fresh admission grant expired` | trusted-time boundary class |
| `ADMISSION_GRANT_REPLAYED` | `SESSION_REJECTED` | `SECURITY_TERMINAL` | reconcile prior admission; never reuse grant | `COMMITTED_OR_RECONCILE_REQUIRED` | `SESSION_UNAVAILABLE` | `fresh admission grant already consumed or replayed` | replay receipt/correlation ref |
| `ADMISSION_ATTEMPT_RECONCILIATION_REQUIRED` | `DEPENDENCY_UNAVAILABLE` | `RETRYABLE` | same AdmissionAttemptRef reconciliation; new attempt only after deterministic retirement + proof old capability unavailable | `ISSUANCE_RECONCILE_REQUIRED` | `TEMPORARILY_UNAVAILABLE` | `fresh admission issuance outcome requires reconciliation` | attempt_ref + operation-status class |
| `ADMISSION_GRANT_SECURITY_STATE_REVOKED` | `SESSION_REJECTED` | `SECURITY_TERMINAL` | new authenticated attempt only after current account security permits | `NO_AUTHORITY_MUTATION` | `AUTHENTICATION_REQUIRED` | `fresh admission denied by current account security state` | decision/source-order bucket |
| `ADMISSION_GRANT_SECURITY_EVIDENCE_STALE` | `DEPENDENCY_UNAVAILABLE` | `RETRYABLE` | same unconsumed grant only after fresh authenticated non-rollback evidence while all bindings remain valid | `NO_AUTHORITY_MUTATION` | `TEMPORARILY_UNAVAILABLE` | `fresh admission security evidence unavailable, stale or superseded` | evidence source/age/order class |
| `ADMISSION_GRANT_ROUTE_STALE` | `STALE_GENERATION` | `TERMINAL` | fresh route + grant; no retarget | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `fresh admission route no longer current` | world/channel/route revision where permitted |
| `ADMISSION_GRANT_RUNTIME_GENERATION_STALE` | `STALE_GENERATION` | `TERMINAL` | current-owner evidence + new grant | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `fresh admission runtime ownership no longer current` | runtime observation + relation class |
| `ADMISSION_GRANT_WORLD_STALE` | `STALE_GENERATION` | `TERMINAL` | resolve current world then new authorized route/grant; no retarget | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `fresh admission character world binding no longer matches` | signed world + relation class |
| `ADMISSION_GRANT_REVISION_UNSUPPORTED` | `UNSUPPORTED_REVISION` | `TERMINAL` | compatible producer/client/consumer revision only; no downgrade | `NO_AUTHORITY_MUTATION` | `CLIENT_UPDATE_REQUIRED` | `fresh admission authoritative revision unsupported` | authenticated mismatch dimension + approved revision |
| `ADMISSION_ACCOUNT_CHARACTER_CONFLICT` | `CONFLICT` | `TERMINAL` | new attempt only after authoritative ownership/lifecycle change | `NO_AUTHORITY_MUTATION` | `SESSION_UNAVAILABLE` | `fresh admission account or character relationship conflicts with current authority` | ownership/lifecycle class |
| `ADMISSION_INCUMBENT_PROTECTED` | `CONFLICT` | `TERMINAL` | new attempt only after incumbent eligibility changes; same grant never becomes takeover | `NO_AUTHORITY_MUTATION` | `CHARACTER_ALREADY_ACTIVE` | `fresh admission blocked by current character authority` | incumbent-state class |
| `ADMISSION_CAPACITY_EXCEEDED` | `CAPACITY_EXCEEDED` | `RETRYABLE` | bounded backoff; same unconsumed grant only on same current route while valid | `NO_AUTHORITY_MUTATION` | `TEMPORARILY_UNAVAILABLE` | `fresh admission capacity unavailable` | capacity/world/channel/route class |

### 4.2 Same-GameSession reconnect

| Code | Category | Progression | Retry authority | Mutation / idempotency | Public class | Redacted diagnostic | Safe correlation |
|---|---|---|---|---|---|---|---|
| `RECONNECT_PROOF_INVALID` | `AUTHENTICATION_FAILED` | `SECURITY_TERMINAL` | valid current proof or reauthenticated recovery; no blind retry | `NO_AUTHORITY_MUTATION` | `AUTHENTICATION_REQUIRED` | `reconnect proof authentication failed` | attempt/session + proof decision class |
| `RECONNECT_HEALTHY_BINDING_PRESENT` | `CONFLICT` | `TERMINAL` for unsolicited replacement | incumbent remains authority; retry only after authoritative loss/future authorized migration | `CURRENT_AUTHORITY_PRESERVED` | `CHARACTER_ALREADY_ACTIVE` | `current playable controller remains authoritative` | session/controller-state class |
| `RECONNECT_NOT_ELIGIBLE` | `SESSION_REJECTED` | `TERMINAL` for same-session path | resolve current recovery/session path | `NO_AUTHORITY_MUTATION` | `SESSION_UNAVAILABLE` | `session is not eligible for same-session reconnect` | session lifecycle class |
| `RECONNECT_PREPARED_EXPIRED` | `TIMEOUT` | `TERMINAL` for candidate | new PREPARE only if original grace/current facts independently permit | `CURRENT_AUTHORITY_PRESERVED`; candidate proof invalid | `TEMPORARILY_UNAVAILABLE` | `prepared reconnect candidate expired` | attempt + prepared-state class |
| `RECONNECT_PREPARED_STALE` | `STALE_GENERATION` | `TERMINAL` | reconcile current authority; new candidate only if current state permits | `CURRENT_AUTHORITY_PRESERVED`; stale candidate cannot advance | `SESSION_UNAVAILABLE` | `prepared reconnect candidate no longer current` | attempt + generation-relation class |
| `RECONNECT_RECONCILIATION_UNAVAILABLE` | `INTERNAL_UNAVAILABLE` | `RETRYABLE` bounded | same-attempt/current-authority reconciliation only; no new authority until winner/fence proven | `CURRENT_AUTHORITY_PRESERVED` | `TEMPORARILY_UNAVAILABLE` | `reconnect authority outcome requires reconciliation` | attempt/session + reconciliation class |
| `RECONNECT_GRACE_EXPIRED` | `SESSION_REJECTED` | `TERMINAL` for old GameSession | eligible post-grace recovery or separate fresh path as state permits | `NO_AUTHORITY_MUTATION`; old GameSession never revives | `SESSION_UNAVAILABLE` | `same-session reconnect window expired` | session/grace-boundary class |

### 4.3 Reauthenticated recovery

| Code | Category | Progression | Retry authority | Mutation / idempotency | Public class | Redacted diagnostic | Safe correlation |
|---|---|---|---|---|---|---|---|
| `RECOVERY_GRANT_MALFORMED` | `INVALID_INPUT` | `TERMINAL` | new valid recovery grant | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `recovery grant malformed` | parser/schema stage; authenticated safe profile/header class only |
| `RECOVERY_GRANT_AUTHENTICATION_FAILED` | `AUTHENTICATION_FAILED` | `SECURITY_TERMINAL` | fresh Platform-authenticated recovery | `NO_AUTHORITY_MUTATION` | `AUTHENTICATION_REQUIRED` | `recovery credential authentication failed` | safe algorithm/key/trust class |
| `RECOVERY_GRANT_BINDING_MISMATCH` | `SESSION_REJECTED` | `SECURITY_TERMINAL` | newly issued correct-bound recovery grant | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `recovery credential bound to a different context` | authenticated mismatch dimension |
| `RECOVERY_GRANT_NOT_YET_VALID` | `SESSION_REJECTED` | `RETRYABLE` | same unconsumed grant after accepted nbf boundary while security/target/revisions remain valid | `NO_AUTHORITY_MUTATION` | `TEMPORARILY_UNAVAILABLE` | `recovery grant not yet active` | trusted-time boundary class |
| `RECOVERY_GRANT_EXPIRED` | `SESSION_REJECTED` | `TERMINAL` | fresh recovery attempt | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `recovery grant expired` | trusted-time boundary class |
| `RECOVERY_GRANT_REPLAYED` | `SESSION_REJECTED` | `SECURITY_TERMINAL` | reconcile prior recovery; never reuse nonce | `COMMITTED_OR_RECONCILE_REQUIRED` | `SESSION_UNAVAILABLE` | `recovery grant already consumed or replayed` | recovery receipt/correlation ref |
| `RECOVERY_ATTEMPT_RECONCILIATION_REQUIRED` | `DEPENDENCY_UNAVAILABLE` | `RETRYABLE` | same attempt_ref reconciliation; new attempt only after deterministic retirement + proof old capability unavailable | `ISSUANCE_RECONCILE_REQUIRED` | `TEMPORARILY_UNAVAILABLE` | `recovery issuance outcome requires reconciliation` | attempt_ref + operation-status class |
| `RECOVERY_GRANT_SECURITY_STATE_REVOKED` | `SESSION_REJECTED` | `SECURITY_TERMINAL` | new recovery only after current account security permits | `NO_AUTHORITY_MUTATION` | `AUTHENTICATION_REQUIRED` | `recovery denied by current account security state` | decision/source-order class |
| `RECOVERY_GRANT_SECURITY_EVIDENCE_STALE` | `DEPENDENCY_UNAVAILABLE` | `RETRYABLE` | same unconsumed grant only while token/target/revisions remain valid after fresh non-rollback evidence | `NO_AUTHORITY_MUTATION` | `TEMPORARILY_UNAVAILABLE` | `recovery security evidence unavailable, stale or superseded` | evidence source/age/order class |
| `RECOVERY_GRANT_WORLD_STALE` | `STALE_GENERATION` | `TERMINAL` | current world + new recovery grant; no retarget | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `recovery character world binding no longer matches` | signed world + relation class |
| `RECOVERY_GRANT_REVISION_UNSUPPORTED` | `UNSUPPORTED_REVISION` | `TERMINAL` | compatible revision only; no downgrade | `NO_AUTHORITY_MUTATION` | `CLIENT_UPDATE_REQUIRED` | `recovery authoritative revision unsupported` | authenticated mismatch dimension + approved revision |
| `RECOVERY_HEALTHY_CONTROLLER_PRESENT` | `CONFLICT` | `TERMINAL` | incumbent remains authority; recovery after authoritative loss only | `CURRENT_AUTHORITY_PRESERVED` | `CHARACTER_ALREADY_ACTIVE` | `recovery blocked by current playable controller` | controller-state class |
| `RECOVERY_TARGET_NOT_ELIGIBLE` | `SESSION_REJECTED` | `TERMINAL` | resolve authoritative actor/session lifecycle | `NO_AUTHORITY_MUTATION` | `SESSION_UNAVAILABLE` | `recovery target is not eligible` | actor/session lifecycle class after ownership-safe evaluation |
| `RECOVERY_PLACEMENT_UNAVAILABLE` | `DEPENDENCY_UNAVAILABLE` | `RETRYABLE` bounded | same unconsumed grant only while time/security/revisions remain valid after current placement resolves | `NO_AUTHORITY_MUTATION` | `TEMPORARILY_UNAVAILABLE` | `current recovery placement is unavailable` | locator/source/current-owner class |
| `RECOVERY_STATE_UNSAFE` | `INTERNAL_UNAVAILABLE` | `TERMINAL` for this transition until reconciliation | no control attachment until state is provably safe | `CURRENT_AUTHORITY_PRESERVED` | `SESSION_UNAVAILABLE` | `recovery state cannot be reconciled safely` | reconciliation/safety class |

`RECOVERY_PLACEMENT_UNAVAILABLE` and `RECOVERY_STATE_UNSAFE` are C integration codes for B-defined locator/fail-closed conditions; they do not change B authority semantics.

### 4.4 CharacterLease integration

Exact lease TTL/renew/safety values remain deferred to measured DUR/OPS evidence.

| Code | Category | Progression | Retry authority | Mutation / idempotency | Public class | Redacted diagnostic | Safe correlation |
|---|---|---|---|---|---|---|---|
| `CHARACTER_LEASE_STALE` | `STALE_GENERATION` | `TERMINAL` for stale holder | reconcile current owner/session; stale holder never renews/replaces | `NO_AUTHORITY_MUTATION` | `SESSION_UNAVAILABLE` | `character lease authority is stale` | lease relation class; no raw generation |
| `CHARACTER_LEASE_RENEW_TIMEOUT` | `TIMEOUT` | `RETRYABLE` bounded for current lease only | same-current-lease renewal before measured fail-safe deadline; then fail safe | `BOUNDED_CURRENT_LEASE_ONLY` | `TEMPORARILY_UNAVAILABLE` | `character lease renewal deadline unavailable` | lease state/deadline class |
| `CHARACTER_LEASE_DEPENDENCY_UNAVAILABLE` | `DEPENDENCY_UNAVAILABLE` | `RETRYABLE` bounded for current lease only | same-current renewal/reconciliation while safety deadline remains | `BOUNDED_CURRENT_LEASE_ONLY` | `TEMPORARILY_UNAVAILABLE` | `character lease authority dependency unavailable` | dependency + lease-state class |

## 5. Historical/superseded error aliases

Superseded #109 names are not parallel production codes when accepted A/B/C owns the condition.

| Historical name | Canonical handling |
|---|---|
| `RECONNECT_PROOF_REPLAYED` | stale/rejected proof -> `RECONNECT_PROOF_INVALID`; uncertainty after a possibly committed exact attempt -> `RECONNECT_RECONCILIATION_UNAVAILABLE` |
| `RECONNECT_SESSION_TERMINAL` | `RECONNECT_NOT_ELIGIBLE`, or `RECONNECT_GRACE_EXPIRED` when original grace expiry is the known cause |
| `RECONNECT_GENERATION_STALE` | prepared candidate stale -> `RECONNECT_PREPARED_STALE`; ordinary old post-commit transport is rejected by FND-02 generation fencing rather than a second FND-04 API code |
| `RECONNECT_ATTEMPT_CONFLICT` | reconcile exact attempt state; use `RECONNECT_PREPARED_STALE`, `RECONNECT_RECONCILIATION_UNAVAILABLE` or stable committed result according to current authority |
| `SESSION_TAKEOVER_NOT_ALLOWED` | operation-specific accepted conflict: `ADMISSION_INCUMBENT_PROTECTED`, `RECONNECT_HEALTHY_BINDING_PRESENT` or `RECOVERY_HEALTHY_CONTROLLER_PRESENT` |

Implementations MUST NOT expose both an alias and canonical replacement for the same contract revision.

## 6. Failure-scenario disposition

The disposition column uses exactly the canonical catalogue vocabulary: `PASS`, `NOT_APPLICABLE`, `BLOCKED`, `DEFERRED_BY_ACCEPTED_GATE`.

`PASS` here means **architecture contract coverage exists and names the required future implementation evidence**; it does not claim executable runtime evidence already exists.

| Scenario | Disposition | Contract evidence / future proof |
|---|---|---|
| `FS-PLATFORM-UNAVAILABLE` | `PASS` | no alternate credential authority; A/recovery dependency/security failures; Platform cannot create GameSession |
| `FS-GATEWAY-AFTER-REDEEM` | `PASS` | AdmissionAttemptRef/GrantNonce reconciliation; no blind second capability |
| `FS-ADMISSION-VALIDATION-COMMIT-ELIGIBILITY-CHANGE` | `PASS` | A atomic final revalidation; changed predicate creates no partial candidate authority |
| `FS-DUPLICATE-LOGIN` | `PASS` | account-global exclusion/incumbent protection; one winner |
| `FS-ADMISSION-GRANT-REPLAY` | `PASS` | one GrantNonce success maximum + prior-result reconciliation |
| `FS-RECOVERY-GRANT-ISSUANCE-AMBIGUITY` | `PASS` | same attempt_ref reconciliation; blind second recovery grant forbidden |
| `FS-RECOVERY-OWNERSHIP-WORLD-CHANGE` | `PASS` | ownership first/world second, repeated at commit; no retarget/recreate |
| `FS-RECONNECT-CREDENTIAL-REPLAY` | `PASS` | predecessor proof/generation fenced; healthy binding non-preemption |
| `FS-RECONNECT-PREPARE-COMMIT-ELIGIBILITY-CHANGE` | `PASS` | B COMMIT revalidates generation/grace/controller/lease/runtime/security/revisions |
| `FS-RECONNECT-COMMIT-RESPONSE-LOSS` | `PASS` | inactive candidate successor proof + same-attempt reconciliation; no predecessor revival |
| `FS-REENTRY-PROTECTION-REARM-FAILOVER` | `PASS` | loss/grace/protection/re-arm state survives failover; no retry/restart reset/loop extension |
| `FS-GAMENODE-SESSION-CONTINUITY-AMBIGUOUS` | `PASS` | same GameSession only with complete fenced evidence; otherwise no guessing/restarted deadline |
| `FS-KEY-ROTATION` | `PASS` | both profiles require source-age <=5s + anti-rollback trust; PREPARE not trust escrow |
| `FS-CLOCK-SKEW` | `PASS` | bounded signed timestamp skew + server-authoritative monotonic-safe lifecycle deadlines |
| `FS-REVISION-MISMATCH` | `PASS` | independent revision dimensions; no opaque compatibility/downgrade |
| `FS-SNAPSHOT-DELTA-MISMATCH` | `PASS` | FND-02 explicit snapshot/delta/resync; no gap guessing |
| `FS-LEASE-RENEW-TIMEOUT` | `DEFERRED_BY_ACCEPTED_GATE` | stale-writer semantics frozen; exact TTL/renew/safety deadline requires DUR/OPS measured evidence |
| `FS-POSTGRES-UNAVAILABLE` | `DEFERRED_BY_ACCEPTED_GATE` | physical durable/lease policy belongs DUR; FND-04 forbids unfenced authority assumption |

Other Foundation scenarios remain owned by their dedicated contracts unless explicitly referenced.

## 7. Cross-repository compatibility model

Compatibility is multidimensional; no credential may use one opaque `compatibility_revision`.

Fresh admission independently binds profile, protocol_major, transport_profile, ruleset/content/map/world_policy/offer revisions, route/runtime observation and current scope facts.

Recovery independently binds profile, protocol_major, transport_profile, ruleset/content/map/world_policy revisions and current ownership/world/actor/runtime/reconciliation facts. Recovery intentionally carries no ChannelId/InstanceId/NodeId/runtime-owner/HandoffId authority.

FND-02 `schema_revision` remains diagnostic/build evidence rather than exact gameplay admission/recovery equality.

## 8. Producer/consumer rollout and rollback

Platform is producer of bounded fresh/recovery attempt grants; Oteryn-v2 is final game-domain consumer/authority.

A separately authorized production rollout MUST prove:

1. exact producer profile/issuer/audience/purpose/key-purpose matches consumer profile revision;
2. fully specified `Ed25519` interoperation; no deprecated `EdDSA`, negotiation or fallback;
3. producer emits only claims registered by the exact profile;
4. consumer rejects unknown/unsupported profile without reinterpretation as another credential type;
5. Platform security and signing-key/profile trust provide authenticated source provenance + comparable anti-rollback revision;
6. accepted source-age <=5s ceilings cannot be extended by cache refresh;
7. every gameplay revision dimension is independently current; no mixed-state rollout;
8. Canary/fresh/recovery downgrade/alternate authority is impossible;
9. rollback cannot restore older allow/key/profile/revision after newer deny/revoke/retirement floor;
10. producer rollback never revives terminal GameSession, consumed nonce, stale proof or old runtime owner.

### Safe staged activation

Before new profile/revision issuance: deploy/validate consumer support/trust first; pass independent producer/consumer golden fixtures; bound any current/retiring key overlap; keep issuance disabled until compatibility evidence is green.

Retire in reverse safe order: stop new issuance, preserve bounded validation only for still-legally-live capability, prove none remain, then remove support/trust. Emergency revoke may fail closed immediately according to accepted current trust evidence.

## 9. Implementation acceptance evidence

FND-04 architecture acceptance is not implementation authorization. Future implementation must provide at least:

### Credential/security

- independent producer/consumer golden fixtures for both grant profiles;
- malformed corpus + algorithm/key/signature/schema/binding/profile/revision precedence;
- trust/key-discovery negatives;
- time/skew/lifetime boundaries;
- nonce concurrency/replay + producer lost-response reconciliation;
- source-age/anti-rollback/restart-floor/key-rotation/revocation tests.

### Concurrency/authority

- fresh-admission mutable-predicate commit race matrix;
- duplicate-account/character races;
- PREPARE/COMMIT, healthy-preemption, stale generation/proof and lost-response/crash tests;
- same-session/post-grace/healthy-controller recovery races;
- ownership/world transfer before admission/recovery commit;
- CharacterLease stale-owner/fail-safe fault injection.

### Continuity/gameplay

- CommandId/server_sequence/domain-revision same-session continuity;
- snapshot/delta mismatch -> resync, no guessing;
- ControlLossEpoch origin;
- exact 4-second protection matrix;
- repeated disconnect before stable-control re-arm -> no new entitlement;
- stable re-arm then new unexpected loss -> one new entitlement;
- failover during grace/protection/re-arm preserves state/deadlines;
- actor ABSENT retires old protection state;
- post-grace recovery proves no reset/respawn/teleport/heal.

### Failure/diagnostics/privacy

- every Section 4 code/public mapping test;
- mutation/idempotency verification under fault injection;
- redacted diagnostic snapshots + credential-free correlation;
- no unauthenticated binding/profile/world/actor/controller oracle;
- no AccountId/CharacterId ordinary metric labels;
- analytics/investigation cannot mutate runtime authority.

### Deferred numeric/resource evidence

Before runtime activation, successor registry/OPS/PERF/DUR gates must freeze measured finite values for liveness cadence/hysteresis/control-loss threshold, same-session grace, stale-transport cleanup, stable-control re-arm threshold, prepared candidate/rate/retention limits, CharacterLease TTL/renew/safety/fail-safe deadlines, recovery locator/cache limits and relevant queue/resource caps.

## 10. Security/privacy integration

- server gameplay/liveness/runtime evidence is authority for loss/reconnect/protection;
- client/OS/Launcher/Guardian evidence remains corroborative only;
- diagnostics opt-out remains respected; missing client evidence is not adverse;
- no broad Windows Event Log ingestion, kernel driver, invasive anti-cheat or mandatory fingerprint;
- Game Intelligence may analyze bounded/audited patterns but cannot sanction/mutate/fence/reconnect/recover gameplay;
- credentials/proofs/nonces/private keys/private fences never enter ordinary telemetry.

## 11. Completion boundary

FND-04 is architecture-complete only when A and B are accepted/lifecycle-closed, this C package merges, and C lifecycle closeout archives/releases ownership and closes programme #112.

Completion means **semantic architecture accepted**, not runtime implemented. Downstream implementation still requires Section 9 evidence plus DUR/OPS/PERF decisions for deferred physical/numeric values.
