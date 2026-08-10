# FND-04C — Error, Diagnostics, Failure and Compatibility Integration Contract

- Status: Candidate final integration contract; canonical only when the owning FND-04C delivery merges
- Gate: `FND-04C`
- Programme: Issue #112
- Owning delivery: Issue #130
- Repository: `blakinio/Oteryn-v2`
- Trusted base: `main@3d07b3faaca683514fdfe6291e974f9195e2f763`
- Normative component contracts: accepted FND-04A + FND-04B and their two grant profiles
- Consumes: Foundation Error Vocabulary; Foundation Failure Scenario Catalogue; FND-ID-01; FND-02; accepted FND-03; ADR-0003; ADR-0012; accepted disconnect/re-entry owner decisions
- Historical evidence only: superseded PR #109; historical names do not override accepted A/B semantics
- Does not authorize: runtime/protocol/persistence/Platform/KMS/deployment/production implementation

## 1. Purpose and precedence

FND-04C closes the final integration surface of FND-04 without reopening accepted FND-04A or FND-04B semantics.

Precedence is explicit:

```text
FND-04A owns fresh-admission authority and fresh-grant semantics.
FND-04B owns reconnect/recovery/continuity and recovery-grant semantics.
FND-04C owns cross-component error/diagnostic integration,
failure-scenario disposition, compatibility/rollout obligations,
implementation evidence gates and the final FND-04 completion index.
```

If this integration table cannot faithfully represent an accepted A/B rule, FND-04C is invalid and must be repaired/blocked; C never silently rewrites A/B.

## 2. Common Foundation error envelope

Every FND-04 public or cross-component failure has:

```text
error_code                 stable symbolic contract code
category                   one Foundation Error Vocabulary category
progression                RETRYABLE | TERMINAL | SECURITY_TERMINAL
retry_authority             exact same/new attempt/session/owner rule
mutation_outcome            explicit authority/idempotency result
public_class                bounded client-facing category
redacted_diagnostic         stable secret-free internal template
request_trace_id            credential-free request correlation
safe_correlation            bounded typed fields permitted by policy
```

No implementation exception string, SQL error, raw TLS/JWT/parser stack, secret or private fence becomes API behavior.

### 2.1 Common correlation/privacy policy

Potentially safe correlation fields, only when already authenticated/authorized and policy permits, include:

- `request_trace_id`;
- `admission_attempt_ref` / recovery `attempt_ref` / `ReconnectAttemptRef`;
- `GameSessionId` as controlled diagnostic correlation, never bearer proof;
- WorldId/ChannelId where operational policy permits;
- profile identifier and `safe_kid` where policy permits;
- revision **dimension class** and non-secret revision identifier where approved;
- generation relation class (`current`, `stale`, `superseded`) rather than private raw fencing generations;
- evidence source class, source-age bucket and source-order/rollback class;
- lifecycle/controller/placement decision class.

Never include:

- raw admission/recovery JWT;
- GrantNonce/RecoveryGrantNonce;
- reconnect proof or candidate successor proof;
- OAuth/Game Login Ticket;
- private key/PoP material;
- Platform security-generation value;
- raw private lease/scope ownership/connection fencing value where policy treats it as sensitive;
- untrusted token semantic values before authentication;
- transfer/handoff details not required by the caller;
- AccountId/CharacterId as ordinary high-cardinality metric labels.

## 3. Mutation/idempotency vocabulary

The table uses these stable shorthand outcomes:

- `NO_AUTHORITY_MUTATION` — this rejected candidate commits no new presence/lease/session/transport/runtime authority;
- `COMMITTED_OR_RECONCILE_REQUIRED` — a prior transition may already have committed; reconcile exact attempt/current authority before any independent retry;
- `ISSUANCE_RECONCILE_REQUIRED` — producer may already have issued one capability; same operation reconciliation or deterministic retirement only;
- `BOUNDED_CURRENT_LEASE_ONLY` — retry can preserve only already-current CharacterLease authority before an evidence-backed fail-safe deadline; never grants replacement authority;
- `CURRENT_AUTHORITY_PRESERVED` — whatever authority is current at revalidation remains current; PREPARE-time state is not restored.

## 4. Canonical FND-04 error catalogue

This is the complete cross-component integration catalogue. Component-specific wording is normalized but semantic progression/retry/mutation remains identical to accepted A/B/profile contracts.

### 4.1 Fresh admission

| Code | Category | Progression | Retry authority | Mutation / idempotency | Public class | Redacted diagnostic | Safe correlation |
|---|---|---|---|---|---|---|---|
| `ADMISSION_GRANT_MALFORMED` | `INVALID_INPUT` | `TERMINAL` | newly issued valid capability; never same malformed grant | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `fresh admission grant malformed` | parser/schema stage; authenticated safe profile/header class only |
| `ADMISSION_GRANT_AUTHENTICATION_FAILED` | `AUTHENTICATION_FAILED` | `SECURITY_TERMINAL` | restart authenticated issuance; never same rejected credential | `NO_AUTHORITY_MUTATION` | `AUTHENTICATION_REQUIRED` | `fresh admission credential authentication failed` | safe algorithm/key/trust decision class |
| `ADMISSION_GRANT_BINDING_MISMATCH` | `SESSION_REJECTED` | `SECURITY_TERMINAL` | newly issued correct-bound grant | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `fresh admission credential bound to a different context` | authenticated mismatch dimension class only |
| `ADMISSION_GRANT_NOT_YET_VALID` | `SESSION_REJECTED` | `RETRYABLE` | same unconsumed grant only after accepted nbf boundary while every other binding remains current | `NO_AUTHORITY_MUTATION` | `TEMPORARILY_UNAVAILABLE` | `fresh admission grant not yet active` | trusted-time boundary class |
| `ADMISSION_GRANT_EXPIRED` | `SESSION_REJECTED` | `TERMINAL` | fresh Gateway/issuer attempt | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `fresh admission grant expired` | trusted-time boundary class |
| `ADMISSION_GRANT_REPLAYED` | `SESSION_REJECTED` | `SECURITY_TERMINAL` | reconcile prior admission; never reuse grant | `COMMITTED_OR_RECONCILE_REQUIRED` | `SESSION_UNAVAILABLE` | `fresh admission grant already consumed or replayed` | replay receipt/correlation reference |
| `ADMISSION_ATTEMPT_RECONCILIATION_REQUIRED` | `DEPENDENCY_UNAVAILABLE` | `RETRYABLE` | same AdmissionAttemptRef status/reconciliation only; new attempt only after deterministic retirement + proof old capability no longer acceptable | `ISSUANCE_RECONCILE_REQUIRED` | `TEMPORARILY_UNAVAILABLE` | `fresh admission issuance outcome requires reconciliation` | attempt_ref; operation-status class |
| `ADMISSION_GRANT_SECURITY_STATE_REVOKED` | `SESSION_REJECTED` | `SECURITY_TERMINAL` | newly authenticated attempt only after current account security permits | `NO_AUTHORITY_MUTATION` | `AUTHENTICATION_REQUIRED` | `fresh admission denied by current account security state` | decision/source-order bucket |
| `ADMISSION_GRANT_SECURITY_EVIDENCE_STALE` | `DEPENDENCY_UNAVAILABLE` | `RETRYABLE` | same unconsumed grant only after fresh authenticated non-rollback evidence while all bindings remain valid | `NO_AUTHORITY_MUTATION` | `TEMPORARILY_UNAVAILABLE` | `fresh admission security evidence unavailable, stale or superseded` | evidence source/age/order class |
| `ADMISSION_GRANT_ROUTE_STALE` | `STALE_GENERATION` | `TERMINAL` | fresh Gateway route + new grant; no retarget | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `fresh admission route no longer current` | world/channel/route revision where policy permits |
| `ADMISSION_GRANT_RUNTIME_GENERATION_STALE` | `STALE_GENERATION` | `TERMINAL` | current-owner evidence + new grant | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `fresh admission runtime ownership no longer current` | runtime observation + relation class; no private generation |
| `ADMISSION_GRANT_WORLD_STALE` | `STALE_GENERATION` | `TERMINAL` | resolve current world then new authorized route/grant; no retarget | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `fresh admission character world binding no longer matches` | signed world + relation class; no transfer detail |
| `ADMISSION_GRANT_REVISION_UNSUPPORTED` | `UNSUPPORTED_REVISION` | `TERMINAL` | compatible producer/client/consumer revision only; no downgrade | `NO_AUTHORITY_MUTATION` | `CLIENT_UPDATE_REQUIRED` | `fresh admission authoritative revision unsupported` | authenticated mismatch dimension + non-secret revision where permitted |
| `ADMISSION_ACCOUNT_CHARACTER_CONFLICT` | `CONFLICT` | `TERMINAL` | new attempt only after authoritative ownership/lifecycle change | `NO_AUTHORITY_MUTATION` | `SESSION_UNAVAILABLE` | `fresh admission account or character relationship conflicts with current authority` | ownership/lifecycle class; world only after ownership-safe evaluation |
| `ADMISSION_INCUMBENT_PROTECTED` | `CONFLICT` | `TERMINAL` | new attempt only after incumbent eligibility changes; same grant never becomes takeover | `NO_AUTHORITY_MUTATION` | `CHARACTER_ALREADY_ACTIVE` | `fresh admission blocked by current character authority` | incumbent state class; world/channel where permitted |
| `ADMISSION_CAPACITY_EXCEEDED` | `CAPACITY_EXCEEDED` | `RETRYABLE` | bounded backoff; same unconsumed grant only on same current route while valid | `NO_AUTHORITY_MUTATION` | `TEMPORARILY_UNAVAILABLE` | `fresh admission capacity unavailable` | capacity class; world/channel/route where permitted |

### 4.2 Same-GameSession reconnect

| Code | Category | Progression | Retry authority | Mutation / idempotency | Public class | Redacted diagnostic | Safe correlation |
|---|---|---|---|---|---|---|---|
| `RECONNECT_PROOF_INVALID` | `AUTHENTICATION_FAILED` | `SECURITY_TERMINAL` | valid current proof or reauthenticated recovery; never blind retry rejected proof | `NO_AUTHORITY_MUTATION` | `AUTHENTICATION_REQUIRED` | `reconnect proof authentication failed` | attempt/session + proof decision class; never proof bytes |
| `RECONNECT_HEALTHY_BINDING_PRESENT` | `CONFLICT` | `TERMINAL` for unsolicited replacement | incumbent remains authority; retry only after authoritative loss or future separately authorized migration | `CURRENT_AUTHORITY_PRESERVED` | `CHARACTER_ALREADY_ACTIVE` | `current playable controller remains authoritative` | session/controller-state class |
| `RECONNECT_NOT_ELIGIBLE` | `SESSION_REJECTED` | `TERMINAL` for same-session path | resolve current recovery/session path | `NO_AUTHORITY_MUTATION` | `SESSION_UNAVAILABLE` | `session is not eligible for same-session reconnect` | session lifecycle class |
| `RECONNECT_PREPARED_EXPIRED` | `TIMEOUT` | `TERMINAL` for candidate | new PREPARE only if original grace/current facts independently still permit | `CURRENT_AUTHORITY_PRESERVED`; candidate proof permanently invalid | `TEMPORARILY_UNAVAILABLE` | `prepared reconnect candidate expired` | attempt + prepared-state class |
| `RECONNECT_PREPARED_STALE` | `STALE_GENERATION` | `TERMINAL` | reconcile current authority; new candidate only if current state permits | `CURRENT_AUTHORITY_PRESERVED`; stale candidate cannot advance | `SESSION_UNAVAILABLE` | `prepared reconnect candidate no longer current` | attempt + generation-relation class |
| `RECONNECT_RECONCILIATION_UNAVAILABLE` | `INTERNAL_UNAVAILABLE` | bounded `RETRYABLE` | same-attempt/current-authority reconciliation only; no new authority until current winner/fence is proven | `CURRENT_AUTHORITY_PRESERVED` | `TEMPORARILY_UNAVAILABLE` | `reconnect authority outcome requires reconciliation` | attempt/session + reconciliation-state class |
| `RECONNECT_GRACE_EXPIRED` | `SESSION_REJECTED` | `TERMINAL` for old GameSession | eligible post-grace recovery or separate fresh path as authoritative state permits | `NO_AUTHORITY_MUTATION`; old GameSession never revives | `SESSION_UNAVAILABLE` | `same-session reconnect window expired` | session/grace-boundary class; no guessed duration |

### 4.3 Reauthenticated recovery

| Code | Category | Progression | Retry authority | Mutation / idempotency | Public class | Redacted diagnostic | Safe correlation |
|---|---|---|---|---|---|---|---|
| `RECOVERY_GRANT_MALFORMED` | `INVALID_INPUT` | `TERMINAL` | new valid recovery grant | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `recovery grant malformed` | parser/schema stage; authenticated safe profile/header class only |
| `RECOVERY_GRANT_AUTHENTICATION_FAILED` | `AUTHENTICATION_FAILED` | `SECURITY_TERMINAL` | fresh Platform-authenticated recovery; never same rejected credential | `NO_AUTHORITY_MUTATION` | `AUTHENTICATION_REQUIRED` | `recovery credential authentication failed` | safe algorithm/key/trust class |
| `RECOVERY_GRANT_BINDING_MISMATCH` | `SESSION_REJECTED` | `SECURITY_TERMINAL` | newly issued correct-bound recovery grant | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `recovery credential bound to a different context` | authenticated mismatch dimension class |
| `RECOVERY_GRANT_NOT_YET_VALID` | `SESSION_REJECTED` | `RETRYABLE` | same unconsumed grant only after accepted nbf boundary while security/target/revisions remain valid | `NO_AUTHORITY_MUTATION` | `TEMPORARILY_UNAVAILABLE` | `recovery grant not yet active` | trusted-time boundary class |
| `RECOVERY_GRANT_EXPIRED` | `SESSION_REJECTED` | `TERMINAL` | fresh recovery attempt | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `recovery grant expired` | trusted-time boundary class |
| `RECOVERY_GRANT_REPLAYED` | `SESSION_REJECTED` | `SECURITY_TERMINAL` | reconcile prior recovery; never reuse nonce | `COMMITTED_OR_RECONCILE_REQUIRED` | `SESSION_UNAVAILABLE` | `recovery grant already consumed or replayed` | recovery receipt/correlation reference |
| `RECOVERY_ATTEMPT_RECONCILIATION_REQUIRED` | `DEPENDENCY_UNAVAILABLE` | `RETRYABLE` | same attempt_ref issuance/status reconciliation only; new attempt after deterministic retirement + proof old capability unavailable | `ISSUANCE_RECONCILE_REQUIRED` | `TEMPORARILY_UNAVAILABLE` | `recovery issuance outcome requires reconciliation` | attempt_ref + operation-status class |
| `RECOVERY_GRANT_SECURITY_STATE_REVOKED` | `SESSION_REJECTED` | `SECURITY_TERMINAL` | new recovery only after current account security permits | `NO_AUTHORITY_MUTATION` | `AUTHENTICATION_REQUIRED` | `recovery denied by current account security state` | security decision/source-order class |
| `RECOVERY_GRANT_SECURITY_EVIDENCE_STALE` | `DEPENDENCY_UNAVAILABLE` | `RETRYABLE` | same unconsumed grant only while token/target/revisions remain valid after fresh authenticated non-rollback evidence | `NO_AUTHORITY_MUTATION` | `TEMPORARILY_UNAVAILABLE` | `recovery security evidence unavailable, stale or superseded` | evidence source/age/order class |
| `RECOVERY_GRANT_WORLD_STALE` | `STALE_GENERATION` | `TERMINAL` | resolve current world + new recovery grant; never retarget old grant | `NO_AUTHORITY_MUTATION` | `RETRY_LOGIN` | `recovery character world binding no longer matches` | signed world + relation class |
| `RECOVERY_GRANT_REVISION_UNSUPPORTED` | `UNSUPPORTED_REVISION` | `TERMINAL` | compatible producer/consumer revision only; no downgrade | `NO_AUTHORITY_MUTATION` | `CLIENT_UPDATE_REQUIRED` | `recovery authoritative revision unsupported` | authenticated mismatch dimension + non-secret revision where permitted |
| `RECOVERY_HEALTHY_CONTROLLER_PRESENT` | `CONFLICT` | `TERMINAL` | incumbent remains authority; recovery only after authoritative loss | `CURRENT_AUTHORITY_PRESERVED` | `CHARACTER_ALREADY_ACTIVE` | `recovery blocked by current playable controller` | controller-state class |
| `RECOVERY_TARGET_NOT_ELIGIBLE` | `SESSION_REJECTED` | `TERMINAL` | resolve authoritative actor/session lifecycle; separate flow if later legal | `NO_AUTHORITY_MUTATION` | `SESSION_UNAVAILABLE` | `recovery target is not eligible` | actor/session lifecycle class after ownership-safe evaluation |
| `RECOVERY_PLACEMENT_UNAVAILABLE` | `DEPENDENCY_UNAVAILABLE` | bounded `RETRYABLE` | same unconsumed recovery grant only while time/security/revisions remain valid after current placement becomes resolvable | `NO_AUTHORITY_MUTATION` | `TEMPORARILY_UNAVAILABLE` | `current recovery placement is unavailable` | locator/source/current-owner decision class; no stale owner authority |
| `RECOVERY_STATE_UNSAFE` | `INTERNAL_UNAVAILABLE` | `TERMINAL` for this transition until reconciliation | no control attachment until authoritative state becomes provably safe | `CURRENT_AUTHORITY_PRESERVED` | `SESSION_UNAVAILABLE` | `recovery state cannot be reconciled safely` | reconciliation/state-safety class |

`RECOVERY_PLACEMENT_UNAVAILABLE` and `RECOVERY_STATE_UNSAFE` are FND-04C integration codes for B-defined locator/fail-closed conditions; they do not change B transition authority.

### 4.4 CharacterLease integration

CharacterLease remains a game-domain fence whose numeric TTL/renew/safety parameters are deferred to measured DUR/OPS evidence. These errors freeze semantics without inventing numbers.

| Code | Category | Progression | Retry authority | Mutation / idempotency | Public class | Redacted diagnostic | Safe correlation |
|---|---|---|---|---|---|---|---|
| `CHARACTER_LEASE_STALE` | `STALE_GENERATION` | `TERMINAL` for stale holder | reconcile current owner/session; stale holder never renews/replaces authority | `NO_AUTHORITY_MUTATION` | `SESSION_UNAVAILABLE` | `character lease authority is stale` | character correlation under policy + lease relation class, never raw generation |
| `CHARACTER_LEASE_RENEW_TIMEOUT` | `TIMEOUT` | bounded `RETRYABLE` for already-current lease only | bounded same-current-lease renewal before evidence-backed fail-safe deadline; then fail safe | `BOUNDED_CURRENT_LEASE_ONLY` | `TEMPORARILY_UNAVAILABLE` | `character lease renewal deadline unavailable` | lease state/deadline class, no guessed numeric values |
| `CHARACTER_LEASE_DEPENDENCY_UNAVAILABLE` | `DEPENDENCY_UNAVAILABLE` | bounded `RETRYABLE` for already-current lease only | bounded renewal/reconciliation while accepted safety deadline remains; never replacement authority | `BOUNDED_CURRENT_LEASE_ONLY` | `TEMPORARILY_UNAVAILABLE` | `character lease authority dependency unavailable` | dependency + lease-state class |

## 5. Historical/superseded error aliases

Superseded #109 names are **not** additional production codes when an accepted A/B/C code already owns the condition.

| Historical name | Canonical handling |
|---|---|
| `RECONNECT_PROOF_REPLAYED` | stale/rejected proof -> `RECONNECT_PROOF_INVALID`; uncertainty after a possibly committed exact attempt -> `RECONNECT_RECONCILIATION_UNAVAILABLE` |
| `RECONNECT_SESSION_TERMINAL` | `RECONNECT_NOT_ELIGIBLE`, or `RECONNECT_GRACE_EXPIRED` when the known cause is the original same-session grace boundary |
| `RECONNECT_GENERATION_STALE` | prepared/rebind candidate stale -> `RECONNECT_PREPARED_STALE`; ordinary stale post-commit transport is rejected by FND-02 connection-generation fencing and is not a second FND-04 API code |
| `RECONNECT_ATTEMPT_CONFLICT` | exact current attempt state is reconciled; use `RECONNECT_PREPARED_STALE`, `RECONNECT_RECONCILIATION_UNAVAILABLE` or stable already-committed result according to authoritative state |
| `SESSION_TAKEOVER_NOT_ALLOWED` | operation-specific accepted conflict: `ADMISSION_INCUMBENT_PROTECTED`, `RECONNECT_HEALTHY_BINDING_PRESENT` or `RECOVERY_HEALTHY_CONTROLLER_PRESENT`; no generic bearer takeover path exists |

Implementations MUST NOT expose both an alias and its canonical replacement as alternative outcomes for the same contract revision.

## 6. Failure-scenario architecture disposition

`PASS (ARCHITECTURE)` below means the accepted contracts define the required deterministic outcome and named future evidence. It does **not** claim runtime tests exist. `DEFERRED_BY_ACCEPTED_GATE` means the named numeric/physical evidence belongs to another accepted gate.

| Scenario | FND-04 disposition | Contract evidence / future proof |
|---|---|---|
| `FS-PLATFORM-UNAVAILABLE` | `PASS (ARCHITECTURE)` | no alternate credential authority; A/recovery stale/dependency errors; Platform cannot create GameSession |
| `FS-GATEWAY-AFTER-REDEEM` | `PASS (ARCHITECTURE)` | AdmissionAttemptRef vs GrantNonce reconciliation; no blind second capability |
| `FS-ADMISSION-VALIDATION-COMMIT-ELIGIBILITY-CHANGE` | `PASS (ARCHITECTURE)` | A final atomic revalidation; changed predicate creates no partial candidate authority |
| `FS-DUPLICATE-LOGIN` | `PASS (ARCHITECTURE)` | account-global exclusion and incumbent protection; at most one winner |
| `FS-ADMISSION-GRANT-REPLAY` | `PASS (ARCHITECTURE)` | one GrantNonce success maximum + prior-result reconciliation |
| `FS-RECOVERY-GRANT-ISSUANCE-AMBIGUITY` | `PASS (ARCHITECTURE)` | same attempt_ref reconciliation; blind second recovery grant forbidden |
| `FS-RECOVERY-OWNERSHIP-WORLD-CHANGE` | `PASS (ARCHITECTURE)` | ownership first/world second repeated at recovery commit; no retarget/recreate |
| `FS-RECONNECT-CREDENTIAL-REPLAY` | `PASS (ARCHITECTURE)` | predecessor proof/generation fenced; healthy binding non-preemption |
| `FS-RECONNECT-PREPARE-COMMIT-ELIGIBILITY-CHANGE` | `PASS (ARCHITECTURE)` | B COMMIT revalidates generation/grace/controller/lease/runtime/security/revisions before switch |
| `FS-RECONNECT-COMMIT-RESPONSE-LOSS` | `PASS (ARCHITECTURE)` | inactive candidate successor proof + same-attempt stable reconciliation; no predecessor revival |
| `FS-REENTRY-PROTECTION-REARM-FAILOVER` | `PASS (ARCHITECTURE)` | ControlLossEpoch/grace/protection/re-arm state survives failover; no retry/restart reset or disconnect-loop extension |
| `FS-GAMENODE-SESSION-CONTINUITY-AMBIGUOUS` | `PASS (ARCHITECTURE)` | same GameSession only with complete fenced continuity evidence; otherwise no guessing/restarted deadline |
| `FS-KEY-ROTATION` | `PASS (ARCHITECTURE)` | both grant profiles require authenticated source-age <=5s + anti-rollback trust; PREPARE is not trust escrow |
| `FS-CLOCK-SKEW` | `PASS (ARCHITECTURE)` | signed profiles have trusted-server bounded skew; liveness/grace/protection use server authority/monotonic-safe implementation evidence |
| `FS-REVISION-MISMATCH` | `PASS (ARCHITECTURE)` | independent protocol/transport/ruleset/content/map/world-policy/offer checks; no opaque compatibility/downgrade |
| `FS-SNAPSHOT-DELTA-MISMATCH` | `PASS (ARCHITECTURE)` | same-session continuation uses FND-02 explicit snapshot/delta/resync; no guessing through gaps |
| `FS-LEASE-RENEW-TIMEOUT` | `DEFERRED_BY_ACCEPTED_GATE` for numeric acceptance | stale writer fails closed now; exact TTL/renew/safety deadline requires DUR/OPS measured evidence before implementation |
| `FS-POSTGRES-UNAVAILABLE` | `DEFERRED_BY_ACCEPTED_GATE` | durable transaction/lease physical policy belongs DUR; FND-04 forbids unfenced authority assumption |

All other Foundation scenarios remain owned by their dedicated contracts unless explicitly referenced here.

## 7. Cross-repository compatibility model

Compatibility is multidimensional. No FND-04 credential may carry or rely on one opaque `compatibility_revision`.

### 7.1 Fresh admission dimensions

FND-04A independently binds/validates:

```text
fresh profile revision
protocol_major
transport_profile
ruleset_revision
content_revision
map_revision
world_policy_revision
offer_revision
route_revision
runtime_observation_revision
scope ownership/current runtime facts
```

FND-02 `schema_revision` remains diagnostic/build evidence rather than exact-equality gameplay admission identity.

### 7.2 Recovery dimensions

FND-04B recovery independently binds/validates:

```text
recovery profile revision
protocol_major
transport_profile
ruleset_revision
content_revision
map_revision
world_policy_revision
current ownership/world/actor/runtime/reconciliation facts
```

Recovery intentionally does not carry ChannelId/InstanceId/NodeId/runtime owner or HandoffId authority.

## 8. Producer/consumer rollout and rollback

Platform is producer of bounded fresh/recovery attempt grants; Oteryn-v2 is final game-domain consumer/authority.

A production rollout requires separately authorized cross-repository work and MUST prove:

1. exact producer profile/issuer/audience/purpose/key-purpose matches consumer profile revision;
2. fully specified `Ed25519` identifiers and key material interoperate; no deprecated `EdDSA`, algorithm negotiation or fallback;
3. producer emits only claims registered by the exact profile revision;
4. consumer rejects unknown/unsupported profile/revision without reinterpretation as the other credential type;
5. Platform security and signing-key/profile trust evidence expose authenticated source-observation provenance + comparable non-rollback revision semantics required by A/B;
6. rollout maintains accepted source-age <=5s security/trust ceilings and cannot extend them by cache refresh;
7. each gameplay revision dimension is independently current for the chosen target; no mixed-state rollout;
8. Canary/fresh/recovery downgrade or alternate credential authority is impossible;
9. rollback cannot restore an older allow/trusted key/profile/revision after a newer deny/revoke/retirement floor has been accepted;
10. a producer rollback never makes a terminal GameSession, consumed nonce, stale proof or old runtime owner authoritative again.

### 8.1 Safe staged activation

Before a new profile/revision becomes issuable:

- consumer support and trust policy for that exact revision must be deployed/validated;
- independent producer/consumer golden fixtures must pass;
- current and retiring key/profile overlap, when used, is explicit and bounded by security policy;
- issuance remains disabled until consumer compatibility evidence is green.

Retirement occurs in the reverse safe order: stop new issuance, preserve bounded validation only for still-legally-live capabilities, prove no required live capability remains, then remove trust/support. Emergency revoke may fail closed immediately according to accepted current trust evidence.

## 9. Implementation acceptance evidence

FND-04 architecture acceptance does **not** authorize implementation. A future implementation claim must provide named evidence at least for:

### Credential interoperability/security

- independent producer/consumer golden byte/semantic fixtures for both grant profiles;
- malformed corpus covering parser/header/schema canonicality;
- algorithm/key/signature/binding/profile/revision precedence tests;
- token-directed trust/key discovery negative tests;
- time/skew/lifetime boundary tests;
- nonce concurrent-consume/replay and issuer lost-response reconciliation;
- source-age/anti-rollback/restart-floor/key-rotation/revocation tests.

### Concurrency/authority

- fresh admission validation-to-commit race matrix for every mutable predicate;
- duplicate-account/character admission races;
- reconnect PREPARE/COMMIT races, healthy-binding preemption attacks and stale generation/proof tests;
- lost PREPARE/COMMIT response and process-crash ambiguity reconciliation;
- recovery healthy-controller, same-session, post-grace and target-state races;
- ownership/world transfer changes before admission/recovery commit;
- CharacterLease stale-owner/fail-safe fault injection.

### Continuity/gameplay

- same-session CommandId/server_sequence/domain-revision continuity;
- snapshot/delta mismatch -> explicit resync, no gap guessing;
- ControlLossEpoch origin tests;
- exact 4-second protection gameplay matrix;
- repeated disconnect before stable-control re-arm -> no new protection entitlement;
- stable-control re-arm then new unexpected loss -> one new entitlement;
- GameNode failover during grace/protection/re-arm preserves deadlines/state;
- actor ABSENT retires old epoch/protection state;
- post-grace recovery proves no respawn/teleport/heal/resource/condition/combat reset.

### Failure/diagnostics/privacy

- every Section 4 error has machine-code/public mapping tests;
- every error verifies mutation/idempotency outcome under fault injection;
- diagnostic snapshots prove redaction and credential-free correlation;
- unauthenticated token differences cannot oracle binding/profile/world/actor/controller state;
- AccountId/CharacterId are not ordinary metric labels;
- analytics/investigation has no runtime mutation authority.

### Numeric/resource evidence still required

Before runtime activation, accepted successor registries/OPS/PERF/DUR gates must freeze measured finite values for:

- liveness probe cadence/hysteresis/control-loss threshold;
- same-session grace;
- stale-transport cleanup;
- stable-control protection re-arm threshold;
- prepared reconnect candidates/rates/retention;
- CharacterLease TTL/renew/safety/fail-safe deadlines;
- recovery locator/cache/resource limits;
- relevant queue/resource caps.

FND-04 intentionally does not invent these numbers.

## 10. Security/privacy integration

FND-04 accepts no invasive anti-cheat prerequisite.

- server gameplay/liveness/runtime evidence is authority for loss/reconnect/protection;
- client/OS/Launcher/Guardian evidence is corroborative only;
- no broad Windows Event Log ingestion;
- diagnostics global opt-out remains respected; missing client evidence is not adverse evidence;
- no kernel driver or mandatory device fingerprint;
- Game Intelligence may analyze bounded/audited reconnect/recovery patterns but cannot autonomously ban, sanction, balance, fence, reconnect, recover or mutate gameplay;
- raw credentials/proofs/nonces/private keys/private fences never enter ordinary telemetry.

## 11. FND-04 completion boundary

FND-04 is architecture-complete only when:

- FND-04A is accepted and lifecycle-closed;
- FND-04B is accepted and lifecycle-closed;
- this FND-04C integration contract, thin final index, failure catalogue and current status are merged;
- FND-04C lifecycle closeout archives/releases ownership and programme #112 closes.

Completion means **semantic architecture accepted**, not runtime implemented.

Downstream implementation still requires the evidence gates in Section 9 plus DUR/OPS/PERF decisions for deferred physical/numeric values.
