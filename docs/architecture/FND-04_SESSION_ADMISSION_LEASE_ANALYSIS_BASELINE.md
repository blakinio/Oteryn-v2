# FND-04 — Identity, Game Session, Admission and Character Lease Analysis Baseline

- Status: Architecture analysis; recommendations only until a later accepted FND-04 contract freezes them
- Date: 2026-08-08
- Gate: `FND-04`
- Coordination ID: `OTV2-NATIVE-FOUNDATION`
- Repository: `blakinio/Oteryn-v2`
- Consumes: ADR-0003, ADR-0012, FND-ID-01, FND-02, accepted FND-03, reconnect/duplicate-login/disconnect owner baselines, foundation error vocabulary and failure catalogue
- External reconciliation evidence: `blakinio/Oteryn-Platform@c0b8703d326a04b43ae8e06f6192b0cb91c859b7` remains read-only/reconciliation-only and cannot override later Oteryn-v2 semantics
- Does not authorize: Rust/runtime/protocol implementation, PostgreSQL schema, Platform writes, key deployment, production traffic, production heartbeat/lease settings or live account/session mutation

## 1. Purpose

`FND-04` is the point where several already accepted truths must become one coherent authority state machine:

```text
Platform authentication
    != authorization to attempt admission
    != canonical GameSessionId
    != player-control authority
    != character world presence
    != concrete transport
```

The architecture is unsafe if these concepts collapse into one generic "session token" or one database row whose semantics change depending on caller.

This baseline therefore analyzes the final contract before freezing security-sensitive mechanisms. It identifies what the final FND-04 contract must decide, recommends one coherent model, and explicitly leaves benchmark/library/schema details open where accepted architecture does not force them yet.

## 2. Accepted constraints — not open for redesign in FND-04

### 2.1 Identity/control-plane boundary

- Platform Identity owns reusable account credentials, OAuth/PKCE, MFA, recovery and Game Login Ticket issuance.
- Game Gateway remains in Oteryn Platform and owns route/offer orchestration, not gameplay authority.
- The game domain owns final gameplay admission, Game Session lifecycle and canonical `GameSessionId` issuance.
- `GameSessionId` is identity only, never a bearer credential.
- Character Authority owns the authoritative `AccountId <-> CharacterId` relation and admission must revalidate it.

### 2.2 Protocol boundary

FND-02 already fixes:

- TLS 1.3 + ALPN `oteryn-game/1`;
- bounded opaque admission and reconnect material;
- no client-created canonical `GameSessionId` during bootstrap;
- game-issued `GameSessionId` after admission;
- `connection_generation` as a `uint64` fence scoped to one `GameSessionId`;
- generation zero only before admission/resume authority;
- strictly newer non-zero generation on every accepted transport rebind;
- `(GameSessionId, CommandId)` command identity and ordered ingress;
- stale generation cannot command, restore liveness or apply state;
- `LivenessProbe` / `LivenessAck` as authenticated application liveness primitives.

FND-04 may define meanings carried by admission/reconnect material and may register later admission/session messages under FND-02 rules, but it cannot redefine the wire foundation silently.

### 2.3 Runtime/liveness boundary

FND-03 already fixes that:

- FND-04 decides which current-generation evidence counts as sufficient control/liveness evidence;
- FND-03 records accepted evidence against a process-monotonic clock;
- after the accepted boundary, FND-03 executes 2-second disconnect protection, 5-second stale concrete transport cleanup and 4-second defensive PvE re-entry effects;
- stale-generation evidence cannot advance liveness;
- runtime/server-health evidence must distinguish GameNode stall from isolated client/path loss.

### 2.4 Account and combat-presence boundary

- one `AccountId` may have at most one authoritative online `CharacterId`;
- a healthy combat/PZ/logout-locked incumbent cannot be kicked or revoked merely because a second client authenticated;
- a genuinely unavailable incumbent may be recovered through same-character reconnect/recovery;
- a different character remains blocked while the incumbent actor has mandatory world presence;
- reconnect/takeover cannot reset HP/resources/position/conditions/cooldowns/combat/PZ/threat/encounter state or committed effects.

### 2.5 Identifier boundary

FND-ID-01 intentionally did **not** add `AdmissionId` or `CharacterLeaseId`.

FND-04 must not invent either unless its final state machine proves that an admission attempt or lease is a separately addressable durable semantic entity that cannot safely be represented by existing identities plus scoped generation/state.

## 3. Decision timing

### Must decide now — YES

Before any production admission/session/lease implementation can be accepted, FND-04 must freeze:

- exact semantic authority model for account presence, character authority, Game Session and transport binding;
- fresh admission and final commit linearization point;
- pre-admission credential class: signed, opaque or hybrid;
- issuer/audience/key-purpose boundaries and key rotation/revocation semantics;
- replay prevention and consumed-credential behavior;
- reconnect credential semantics, rotation and replay handling;
- initial and rebind `connection_generation` commit semantics;
- account-global exclusion and character-lease generation/fencing semantics;
- same-session reconnect, full reauthentication recovery and intentional takeover behavior;
- exact server-authoritative start/end semantics of the accepted 15-second reconnect grace;
- relationship among 2-second loss protection, 5-second transport cleanup and 15-second logical grace;
- fresh-session recovery of the same in-world actor after old GameSession terminality;
- failure behavior for Platform/Gateway/lease/key/revision/race scenarios;
- public/internal error categorization and credential redaction.

### Must decide now — NO

The following should remain open until a bounded implementation/security/performance spike or owning later gate provides evidence:

- JWS/JWT versus PASETO/COSE or another exact signed-container library/encoding, provided the accepted signed-capability semantics are preserved;
- exact asymmetric algorithm/library and key-storage product;
- exact pre-admission TTL and verification-key cache staleness values;
- exact liveness-probe cadence below the already accepted 2-second behavior boundary;
- exact lease TTL, renewal cadence and safety margin;
- PostgreSQL table/index/locking/isolation representation;
- whether Redis, PostgreSQL or another later accepted component physically accelerates non-authoritative caches;
- concrete rate limits and abuse thresholds;
- client proof-of-possession as a first-release requirement;
- final user-facing wording/UX for blocked takeover and reconnect states.

These values must still be concrete before their corresponding implementation is accepted; they are not permission for unlimited/default-library behavior.

### What becomes hard if the model is wrong

A wrong authority model can create:

- two playable characters for one account;
- two transports commanding one GameSession;
- stale GameNode/session writers overwriting current state;
- replayable login capabilities;
- second-client combat disconnect abuse;
- inability to recover a character after an ambiguous successful admission;
- session identity tied incorrectly to current socket, GameNode or channel placement;
- cross-repository coupling that forces Platform to become gameplay authority.

### Evidence that may supersede later

A later contract may reopen a FND-04 choice only with named evidence such as:

- admission/reconnect penetration-test findings;
- cross-language token-library security/maintenance evidence;
- measured key-distribution or introspection latency/availability evidence;
- failover/fault-injection showing a lease model cannot fence split ownership;
- player telemetry showing accepted reconnect timing materially harms fairness or recovery;
- a product requirement for sender-constrained credentials, device binding or stronger takeover authentication.

## 4. Recommended semantic authority model

The final contract should separate four nested authority layers.

```text
A. AccountPresenceClaim
   scope: AccountId
   value: current CharacterId (or none)
   purpose: account-global one-online-character exclusion / mandatory presence

B. CharacterAuthorityLease
   scope: CharacterId
   binds: AccountId + current character_lease_generation + current authoritative actor/runtime context
   purpose: fence stale character authority and durable writes

C. GameSession
   identity: GameSessionId
   binds: AccountId + CharacterId + current character lease + world/placement/revisions
   purpose: logical player-control lifecycle

D. TransportBinding
   scope: GameSessionId
   fence: connection_generation
   purpose: exactly one current concrete transport may submit player commands/liveness/resync authority
```

The names are semantic. The final implementation may physically store them together where atomicity and ownership remain explicit.

### Why account presence and GameSession must be separate

A GameSession can become terminal after reconnect-grace expiry while the actor remains in mandatory combat/PZ/logout world presence.

Therefore:

```text
GameSession terminal
!= actor absent
!= account free to play another CharacterId
```

The account presence claim must follow authoritative world-presence eligibility, not socket lifetime or GameSession lifetime alone.

### Why character authority and GameSession must be separate

Server-driven simulation may still need to commit damage, death, conditions or other authoritative effects after player control is lost. A character authority fence therefore cannot be synonymous with "current TCP connection exists".

The current GameSession controls player input. The authoritative runtime/character lease continues to protect server-originated character mutation according to FND-03/DUR ownership while the actor exists.

## 5. Recommended generation vocabulary

The final contract should prefer scoped generation/fencing values over new durable entity IDs.

### 5.1 `account_presence_generation`

Conceptual scope:

```text
AccountId + account_presence_generation
```

Recommended semantics:

- non-zero monotonically increasing `uint64` class-4 fencing value;
- advances when a new authoritative account-presence claim replaces a prior released/invalid claim;
- protects account-global exclusion from stale admission/takeover attempts;
- does not necessarily advance when the same continuously present actor receives a fresh GameSession after reconnect-grace expiry;
- never wraps/reuses; exhaustion fails safe.

### 5.2 `character_lease_generation`

Conceptual scope:

```text
CharacterId + character_lease_generation
```

Recommended semantics:

- non-zero monotonically increasing `uint64` class-4 fencing value;
- fences stale character/session/process durable writes;
- may survive transport reconnect and GameSession replacement while the same authoritative actor/lease remains current;
- must advance when authoritative character lease ownership is replaced/recovered in a way that must fence a stale former holder;
- never wraps/reuses; exhaustion fails safe.

### 5.3 `connection_generation`

Already fixed by FND-02:

```text
GameSessionId + connection_generation
```

Recommended FND-04 commit semantics:

- first successful GameSession transport binding starts at `1`;
- every accepted same-GameSession rebind atomically establishes one strictly newer generation;
- simple `+1` is preferred unless implementation evidence proves a gap-based allocator is required;
- failed/rejected rebind does not consume/advance the generation unless a commit actually replaced authority;
- wrap/reuse is session-terminal.

### 5.4 No new `AdmissionId` / `CharacterLeaseId` recommendation

Current analysis finds no requirement for a new canonical foundation entity.

A credential-scoped random nonce and scoped lease generation are sufficient for:

- one-time grant replay prevention;
- bounded admission correlation;
- idempotent/fenced state transitions;
- lease fencing.

The final contract should keep `AdmissionId` and `CharacterLeaseId` absent unless later detailed crash-recovery design proves otherwise.

## 6. Fresh admission — recommended linearization

The safe conceptual flow is:

```text
Platform Identity
    -> one-time Game Login Ticket
Game Gateway
    -> redeem ticket
    -> choose authorized WorldId + ChannelId + protocol/revisions
    -> obtain/issue bounded pre-admission grant
Rust game admission boundary
    -> cryptographically validate grant
    -> validate current route/revisions
    -> revalidate AccountId owns CharacterId
    -> evaluate account presence / duplicate-login state
    -> acquire or transition account presence claim
    -> acquire current CharacterAuthorityLease
    -> generate candidate GameSessionId
    -> atomically commit:
         grant consumption
         account/character fences
         logical GameSession
         connection_generation = 1
         initial reconnect-credential verifier
    -> only then publish successful admission
    -> FND-02 initial authoritative snapshot boundary
```

`GameSessionId` may be generated before the transaction/linearization point, but it becomes canonical only if the authoritative admission commit succeeds. A generated-but-uncommitted value is discarded and never reused.

### Required atomic invariant

Fresh admission must behave as one logical linearizable commit even if later DUR-02 maps it to multiple rows/records:

```text
consume grant
+ prove account exclusion
+ prove character authority
+ create one GameSession
+ create first transport generation
= one externally unambiguous admission outcome
```

External success must never precede that commit.

## 7. Pre-admission credential options

### Option A — opaque credential with online introspection/consume

**Benefits**

- immediate central revocation;
- simple claim confidentiality;
- replay state naturally centralized.

**Costs/risks**

- every gameplay admission depends synchronously on Platform/admission service availability and latency;
- game admission correctness becomes coupled to a remote online lookup;
- failure after Game Login Ticket redemption becomes more operationally complex.

### Option B — purely self-contained signed credential

**Benefits**

- game server validates without synchronous Platform call;
- easy horizontal verification and route-local admission.

**Costs/risks**

- signature validity alone does not provide one-time semantics;
- emergency revocation and replay still require explicit state/policy;
- token-type/key/audience confusion becomes security-sensitive.

### Option C — hybrid signed capability + stateful one-time consumption

**Benefits**

- no synchronous Platform introspection on the normal game-server admission path;
- issuer/audience/route/revision claims are cryptographically authenticated;
- a random grant nonce can be atomically consumed with admission/lease state;
- replay and ambiguous retry behavior are explicit rather than assumed from token expiry alone;
- Platform and game domains retain their accepted authority split.

**Costs/risks**

- requires verification-key distribution plus a game-side one-time consumption record/window;
- key rotation/revocation and replay retention must be governed;
- exact cross-language token format needs independent fixture/security evidence.

### Recommendation

Use **Option C: hybrid signed pre-admission capability + stateful one-time consumption** as the final-contract direction unless a bounded security/availability spike disproves it.

This is a semantic recommendation, not selection of JWT/PASETO/COSE or a library yet.

## 8. Recommended pre-admission grant ownership and key purpose

The pre-admission grant should be issued by a **Platform-owned Game Admission Grant issuer** invoked through the Game Gateway flow.

It must be distinct semantically from:

- reusable account/OAuth credentials;
- the one-time Game Login Ticket;
- the canonical game-domain GameSessionId;
- reconnect credentials.

Recommended key-purpose model:

```text
Platform Identity credentials/tickets -> their own keys/purpose
Platform Game Admission Grant         -> dedicated asymmetric signing key purpose
Game reconnect credential             -> game-domain secret/verifier; not the Platform signing key
```

The Game Gateway process should not gain broad reusable account-signing authority merely because it orchestrates issuance.

If a JWT/JWS-style container is later selected, current IETF JWT security guidance requires strict algorithm allowlisting, issuer/audience validation, explicit typing and mutually exclusive validation rules for different token kinds. FND-04 should preserve those properties independent of final library/format.

## 9. Minimum pre-admission grant bindings

The signed/authenticated grant should carry or authenticate at minimum:

- explicit token/credential type and contract revision;
- trusted issuer identifier;
- exact game-admission audience/purpose;
- `AccountId`;
- `CharacterId`;
- `WorldId`;
- `ChannelId`;
- selected protocol major and transport profile;
- required ruleset/content/map/world-policy/server compatibility revisions needed by current accepted contracts;
- issue/not-before/expiry timestamps under bounded wall-clock skew policy;
- cryptographically random one-time grant nonce;
- key identifier/version from an allowlisted issuer key set;
- any exact route/offer revision required to prevent stale offer substitution.

The grant should **not** contain or imply:

- canonical GameSessionId;
- connection_generation;
- character lease authority;
- NodeId as a substitute for current ChannelRuntime ownership;
- reusable account credential material;
- arbitrary verifier/JWK URLs supplied by the token itself;
- client-chosen issuer/audience/route authority.

NodeId binding is not recommended by default because NodeId is process-incarnation placement, not channel identity. Current channel ownership must be validated independently.

## 10. Pre-admission validation order

The final contract should fail closed in an order that bounds attacker-controlled work before expensive/game-state work.

Recommended sequence:

1. FND-02 frame/material size and structural limits;
2. explicit credential type/version parsing;
3. allowlisted issuer/key selection and signature verification;
4. issuer/audience/time/skew validation;
5. protocol/transport/revision/route binding validation;
6. one-time grant nonce replay/consumption eligibility check;
7. authoritative AccountId -> CharacterId ownership revalidation;
8. account-presence/duplicate-login eligibility;
9. current character/world/channel/lifecycle eligibility;
10. atomic admission/lease/GameSession commit.

No failure before step 10 may leave a partial active GameSession or player-control authority.

## 11. Grant replay and ambiguous response policy

### Recommendation: consumed means consumed

The same pre-admission grant must never create a second GameSession or a second admission commit.

After successful consumption, replay of the same grant is classified as `SESSION_REJECTED` with a narrower stable code such as `ADMISSION_GRANT_REPLAYED`/`ADMISSION_GRANT_CONSUMED` in the final registry.

### Lost `ServerAccepted` response

Do **not** weaken one-time grant semantics merely to recover an ambiguous network response.

If the client cannot determine whether admission succeeded:

1. establish a fresh Platform/Gateway admission attempt and fresh grant;
2. game admission re-evaluates current account/character state;
3. if an existing same-character GameSession is genuinely reconnectable, the fresh authenticated attempt may enter the controlled reauthenticated-recovery path described below;
4. it must not create a second actor/session blindly.

This separates replay prevention from recovery and avoids making a consumed admission grant a long-lived reconnect credential.

## 12. Reconnect credential — recommended model

Reconnect material should be a game-domain-issued **high-entropy opaque rotating secret**, not GameSessionId and not a Platform token.

Recommended properties:

- bound server-side to exactly one GameSessionId and current reconnect-credential generation/state;
- transmitted only over the accepted TLS channel;
- server stores a one-way verifier/digest or equivalent secret-safe representation where practical;
- never logged or exported to analytics;
- rotated on every successful authoritative rebind;
- predecessor becomes unusable after the new binding commits, except for a narrowly defined idempotent crash/retry reconciliation record if later required;
- replay outside the accepted transition returns `SESSION_REJECTED` or `STALE_GENERATION` with no authority change;
- expiration/terminality follows GameSession lifecycle and the accepted 15-second fast-resume policy.

The exact secret byte length and cryptographic primitive must be fixed before implementation acceptance, with at least modern cryptographic entropy and library review; this analysis does not invent a number without that implementation/security evidence.

### Proof-of-possession

Client-held proof-of-possession keys could reduce bearer-secret replay risk, and standards such as DPoP demonstrate the general sender-constraining pattern. This analysis does **not** make PoP mandatory for the first native vertical slice because it adds key lifecycle/client-storage/recovery complexity. The final credential envelope should not prevent a later sender-constrained revision if threat evidence justifies it.

## 13. GameSession lifecycle — recommended state vocabulary

Keep GameSession lifecycle separate from actor world presence.

Recommended logical session states:

```text
ACTIVE
CONTROL_SUSPECTED
RECONNECTABLE
TAKEOVER_DRAINING
TERMINATING
TERMINAL
```

### `ACTIVE`

- one current non-zero connection_generation;
- current liveness evidence is sufficient;
- player commands may be accepted subject to FND-02/FND-03/gameplay rules.

### `CONTROL_SUSPECTED`

- sufficient-control evidence is late but terminal loss is not yet established;
- no new GameSession is created;
- exact gameplay protection follows accepted FND-03 timing, not this state name alone.

### `RECONNECTABLE`

- unexpected control loss is server-authoritatively established;
- old concrete transport may already be closed;
- logical GameSession remains eligible for same-session rebind inside the accepted grace window;
- actor state is not reset or recreated.

### `TAKEOVER_DRAINING`

- an intentional authenticated newcomer takeover is allowed only because incumbent is logout-eligible;
- old session remains the only authority until its defined fence/logout boundary;
- a fresh destination/new session is not granted before the old authority is revoked safely.

### `TERMINATING`

- no new ordinary command admission;
- session reaches a bounded terminal boundary while preserving required actor/world state semantics.

### `TERMINAL`

- GameSessionId can never regain authority;
- later gameplay control requires a new GameSessionId;
- terminality alone does not imply the actor is absent if combat/PZ/logout rules require continued world presence.

The final contract may refine names, but it should preserve this separation.

## 14. Actor/account-presence state — separate from GameSession

Recommended conceptual world-presence states:

```text
ABSENT
PRESENT_CONTROLLED
PRESENT_UNCONTROLLED
```

`PRESENT_UNCONTROLLED` is required for combat-X-log/disconnect semantics: the actor remains authoritative in world simulation even when no playable client transport or resumable GameSession currently exists.

AccountPresenceClaim remains occupied for both `PRESENT_CONTROLLED` and `PRESENT_UNCONTROLLED` until the actor is legally removed/terminally resolved under gameplay rules.

## 15. Sufficient-control/liveness evidence

### Recommended authority

The primary sufficient liveness evidence should be a **valid current-generation response to a recent server-issued authenticated liveness probe**.

Binding requirements:

- current GameSessionId;
- current connection_generation;
- current probe ID;
- server-observed receive time;
- server-side runtime-health context.

Client wall-clock timestamps, self-declared lag/disconnect state, socket-open state and stale-generation acknowledgements never count.

### Gameplay traffic

Ordinary gameplay-command silence is not evidence of disconnect.

The final contract may allow a small explicitly enumerated set of current-generation bidirectional control exchanges to count as equivalent sufficient-control evidence only if they prove the same property as a liveness probe. Arbitrary inbound bytes or one-way command traffic should not reset the authoritative loss timer.

### Probe cadence

Because the accepted player-facing protection boundary begins after 2.0 seconds without sufficient control evidence, healthy-idle evidence must be refreshed comfortably inside that interval.

The exact cadence should be selected by a bounded latency/load/fault spike before implementation acceptance. A candidate range such as sub-second to one-second probing may be measured, but this analysis does not freeze a number without evidence.

## 16. Exact reconnect grace timing — recommended semantic choice

The accepted initial reconnect grace is **15 seconds**.

Recommended definition:

```text
last_sufficient_control_at = T0
control_loss_declared_at   = T0 + 2.0 s
stale_transport_cleanup    = T0 + 5.0 s
reconnect_grace_expires    = control_loss_declared_at + 15.0 s
```

Therefore the logical same-GameSession grace is a full 15 seconds from the server-authoritative control-loss boundary, not 15 seconds from the last good probe.

Reasons:

- it gives the stated grace duration after loss is actually classified;
- it keeps liveness detection and reconnect policy conceptually separate;
- it does not let client timestamps influence the window;
- 5-second concrete transport cleanup remains independent and does not end the logical GameSession.

The final contract should explicitly accept or reject this timing composition; leaving it ambiguous is unsafe.

## 17. Same-GameSession fast reconnect

Recommended eligible path inside the 15-second grace:

```text
existing GameSessionId S
+ actor still belongs to same AccountId/CharacterId
+ session not terminal/revoked
+ current CharacterAuthorityLease still compatible
+ reconnect credential valid
+ old transport classified stale/lost
+ current route/revisions valid
    -> atomically commit newer connection_generation
    -> rotate reconnect credential
    -> old generation immediately loses authority
    -> same GameSessionId S continues
    -> FND-03 starts accepted 4-second defensive PvE re-entry effect
```

The rebind commit is the authority linearization point. TLS connection establishment alone is not.

If the rebind commit crashes after authority changes but before the client receives the result, later retry handling must never restore the old generation. The final contract/DUR design must preserve or terminally reconcile enough state to return one unambiguous outcome.

## 18. Reauthenticated same-character recovery

A fresh Platform/Gateway admission grant may be used as strong account/character authentication when a client lacks the old reconnect credential, but it must not bypass incumbent protection.

Recommended policy:

### Existing incumbent is healthy

- do not use fresh authentication as a forced reconnect/takeover shortcut;
- healthy combat/PZ/logout-locked incumbent remains authoritative;
- logout-eligible intentional takeover follows the takeover state machine and creates a fresh logical session after the old one terminates.

### Existing incumbent has server-proven control loss and old GameSession is still reconnectable

A fresh, valid Platform-authenticated same-character attempt may be allowed to recover the **existing GameSessionId** inside the same 15-second grace, provided all normal same-session safety checks pass and a new connection_generation is committed.

This is an alternate authentication path into the same recovery state, not a second GameSession.

Benefits:

- recovers from lost/never-received reconnect material;
- supports device/application restart after genuine network/process failure;
- avoids turning admission-grant replay into a reconnect mechanism.

The final contract must decide whether additional MFA/risk policy is required for this path; Platform owns that policy.

## 19. Recovery after reconnect-grace expiry while actor remains present

The old GameSession becomes terminal when the same-session reconnect grace expires.

However, if combat/PZ/logout policy still requires the actor to remain in world simulation:

```text
old GameSessionId -> TERMINAL
actor             -> PRESENT_UNCONTROLLED
AccountPresenceClaim remains held for CharacterId
CharacterAuthorityLease/runtime actor remains authoritative
```

### Recommended same-character behavior

A later fresh fully authenticated admission for the **same CharacterId** may attach a **new GameSessionId** to that existing in-world actor after proving:

- old GameSession is terminal;
- no current playable controller exists;
- AccountId still owns CharacterId;
- AccountPresenceClaim still points to that character;
- current CharacterAuthorityLease/runtime actor state is valid;
- route/placement/revision checks pass.

This is a fresh logical GameSession, **not** a respawn or reset.

It must preserve all authoritative actor state and use a new connection_generation namespace beginning at 1.

### Re-entry protection

If this fresh-session attachment is still classified as re-entry after the same unexpected loss of playable control, the accepted defensive PvE re-entry policy should apply. The final contract should bind protection eligibility to server-owned control-loss episode state so session-identity replacement does not accidentally erase or duplicate the policy decision.

### Different CharacterId

A different character remains blocked while the incumbent actor has mandatory world presence. Only legal actor removal/release frees the account presence claim for another CharacterId.

## 20. Intentional duplicate-login takeover

### Healthy incumbent + combat/PZ/logout blocker

Binding direction from accepted owner baseline:

```text
new login authenticated
-> no fence
-> no close
-> no revoke
-> no second CharacterId admission
-> incumbent remains fully authoritative
```

Return a bounded `CONFLICT`/`SESSION_REJECTED`-mapped outcome without exposing sensitive combat/session details beyond product policy.

### Healthy incumbent + logout-eligible

Recommended safe transition:

1. authenticate/authorize newcomer;
2. establish takeover eligibility;
3. move incumbent to `TAKEOVER_DRAINING`;
4. stop accepting new ordinary incumbent commands at the committed fence boundary;
5. complete legal logout/removal or another explicitly accepted handoff boundary;
6. release/advance applicable account/character authority generations;
7. create a **fresh GameSessionId** for the newcomer;
8. do not grant disconnect/re-entry protection merely because this was an intentional takeover.

No interval may contain two player-controlled authoritative characters.

## 21. Account presence and character lease atomicity

Fresh admission of a character must atomically prove both:

```text
AccountId may claim this CharacterId as the one online/present character
AND
CharacterId may acquire current authoritative character lease/control binding
```

Two different CharacterIds for the same AccountId racing on different worlds/channels must not independently succeed.

Physical implementation may use transactions/locks/CAS in DUR-02, but FND-04 must require linearizable equivalent semantics.

Recommended deterministic acquisition order for later implementation design:

```text
account exclusion/presence claim
-> character authority lease
-> GameSession binding
```

A later physical schema may optimize this, but it must not invert safety or expose partial success.

## 22. Character lease lifecycle

### Semantic owner

The game-domain Character/Game Session admission boundary owns the logical character lease contract. Current runtime scope ownership and DUR persistence provide the physical/fencing mechanisms needed to enforce it.

### Acquire

- only after credential/route/ownership checks;
- current account presence claim must be compatible;
- acquire/advance generation atomically with the authoritative transition;
- stale previous generation can never commit after replacement.

### Renew

- only current generation/session/runtime authority may renew;
- renewal extends authority only after the lease authority accepts it;
- a local request sent before expiry but not committed is not proof of renewal;
- lease store time/authority, not client time, defines authoritative expiry.

### Grace / local safety margin

The GameNode must stop relying on a lease **before** there is any possibility that another authority can legitimately acquire a newer generation.

A local safety deadline shorter than the external/authoritative lease expiry is recommended so network/clock uncertainty cannot create overlap.

Exact TTL, renewal cadence and safety margin require DUR/OPS/fault-injection evidence before implementation acceptance.

### Expiry / renewal uncertainty

When renewal cannot be proven in time:

- current player command authority fails closed;
- stale durable writes under the old character lease generation are prohibited;
- scope/session enters a non-authoritative/suspected/fenced path appropriate to FND-03;
- server-driven actor presence may continue only under an independently current runtime/character authority path that cannot overlap a newer writer;
- a newer lease generation is not granted until the old generation is safely fenced according to the durable authority contract.

### Release

Release is explicit on clean terminal lifecycle where possible, but correctness must not rely on receiving a release from a crashed/stale owner. Generation fencing and expiry/recovery must handle omission safely.

## 23. Key discovery, rotation and emergency revocation

The final contract should require:

- asymmetric verification so game nodes do not need Platform signing secrets;
- dedicated admission-grant key purpose separate from other Platform token types;
- allowlisted issuer/key-set source; never follow arbitrary key URLs from untrusted credential headers;
- stable key identifier/version;
- current and bounded retiring verification-key overlap sufficient for already-issued unexpired grants;
- no grant accepted after its own expiry even if a key remains trusted;
- emergency revocation capable of invalidating a compromised key before normal overlap completes;
- bounded cached-key staleness and explicit failure behavior when key status cannot be trusted;
- exact rotation/revocation E2E fixtures before production enablement.

Exact KMS/HSM/provider and key algorithm remain implementation/security choices until the bounded spike.

## 24. Revision and route binding

Admission must fail closed when grant bindings and current authority disagree.

At minimum reject:

- wrong WorldId/ChannelId;
- retired/stale route revision where the current contract requires freshness;
- incompatible protocol major/transport profile;
- incompatible ruleset/content/map/world-policy/server revision fences;
- wrong audience/issuer;
- expired/not-yet-valid credential outside accepted skew;
- current GameNode not holding accepted authority for the target scope.

There is no silent fallback to another channel, protocol family, Canary listener or downgraded route using the same credential.

## 25. Channel/instance handoff interaction

FND-04 should not redesign FND-03 handoff execution.

Recommended session-level rules:

- `HandoffId` identifies one authorized ownership transition;
- source GameSession/lease/account presence remain explicit bindings;
- source and destination may prepare concurrently but at most one current gameplay owner may accept player mutation;
- Channel -> Instance handoff can preserve the same GameSessionId when the accepted activity transition is continuous logical session control and the relevant contract says so;
- a Channel -> Channel transition already accepted as a fresh logical Game Session receives a fresh GameSessionId;
- source authority is not released until destination commit/fence is established;
- stale/replayed HandoffId or generation cannot commit;
- failure before commit returns/preserves the source-safe state; failure after commit recovers destination authority evidence rather than client claims.

The final contract must reconcile these rules with the accepted FND-ID statement that channel transitions establishing a fresh GameSession use a fresh GameSessionId.

## 26. Disconnect/re-entry abuse boundary

The session contract must not accidentally create unlimited protection by treating every socket flap as a new semantic event.

Required analysis result for the final contract:

- re-entry protection eligibility is server-owned state associated with a classified unexpected loss of playable control;
- graceful logout/intentional takeover never creates that protection;
- connection_generation changes alone do not automatically grant protection;
- stale/replayed reconnect attempts cannot restart the timer;
- same control-loss episode must not receive duplicate overlapping protection because the GameSession identity changed during recovery;
- repeated genuine later loss episodes remain observable/auditable for Game Intelligence under the accepted non-automatic-sanction policy.

This baseline does **not** introduce an unapproved punishment, cooldown or sanction for repeated disconnects. Whether a minimum healthy interval/hysteresis is needed before a later loss is treated as a new protection-eligible episode remains a final FND-04/product decision.

## 27. Foundation failure-scenario disposition

These are architecture-analysis dispositions, not executable proof.

| Scenario | FND-04 analysis disposition | Required final-contract behavior |
|---|---|---|
| `FS-PLATFORM-UNAVAILABLE` | `PASS direction` | no alternate credential authority; fresh login/admission requiring Platform fails/holds boundedly; already active gameplay/session continuity is not invalidated merely by Platform outage |
| `FS-GATEWAY-AFTER-REDEEM` | `PASS direction` | no reuse/downgrade of redeemed ticket; client obtains a fresh bounded Platform flow; no GameSession unless final game admission committed |
| `FS-POSTGRES-UNAVAILABLE` | `DEFERRED_BY_ACCEPTED_GATE` | DUR-02 decides physical dependency; FND-04 requires no admission/lease transition that cannot prove atomic/fenced state |
| `FS-LEASE-RENEW-TIMEOUT` | `PASS direction` | old player/durable authority stops before a newer lease generation may commit; no split authority |
| `FS-DUPLICATE-LOGIN` | `PASS direction` | account-global exclusion + character/session fencing yields at most one player-controlled authoritative character; healthy combat-locked incumbent cannot be kicked |
| `FS-STALE-GENERATION` | `PASS direction` | stale connection/account/character/ownership generation cannot command, renew, reconnect or commit |
| `FS-DUPLICATE-COMMAND` | `NOT_APPLICABLE/consumed` | FND-02 command high-water semantics remain authoritative once a GameSession exists |
| `FS-CHANNEL-SPLIT-OWNER` | `DEFERRED_BY_ACCEPTED_GATE` | FND-03/OPS own runtime scope fence; FND-04 validates current scope/lease before admission/handoff |
| `FS-CHANNEL-DRAIN` | `DEFERRED_BY_ACCEPTED_GATE` | FND-03/OPS own drain; FND-04 blocks new admission/handoff to non-open destination and preserves session safety |
| `FS-QUEUE-SATURATION` | `DEFERRED_BY_ACCEPTED_GATE` | FND-03/resource registry owns queue limits; admission/session work remains bounded and fails before partial authority |
| `FS-SLOW-CLIENT` | `DEFERRED_BY_ACCEPTED_GATE` | FND-02/FND-03 own bounded resync/transport behavior; FND-04 owns logical reconnect eligibility after transport loss |
| `FS-CLOCK-SKEW` | `PASS direction` | credential timestamps use bounded trusted wall-clock skew; liveness/reconnect duration uses server monotonic state, not client time |
| `FS-KEY-ROTATION` | `PASS direction` | bounded current/retiring verification overlap + emergency revocation; no acceptance outside key/credential policy |
| `FS-REVISION-MISMATCH` | `PASS direction` | no implicit downgrade or mixed authoritative state |
| `FS-SNAPSHOT-DELTA-MISMATCH` | `NOT_APPLICABLE/consumed` | FND-02/FND-03 reconciliation after accepted admission/rebind |
| `FS-DB-OUTBOX-BOUNDARY` | `DEFERRED_BY_ACCEPTED_GATE` | DUR-02/ANL-01 own atomic durable event boundary; FND-04 must not announce success before required durable admission/session commit |
| `FS-WORLD-BUNDLE-CORRUPT` | `NOT_APPLICABLE/consumed` | invalid world/content activation must already prevent routable target scope |
| `FS-CLIENT-CUTOVER-ROLLBACK` | `NOT_APPLICABLE` | historical migration lifecycle |
| `FS-ANALYTICS-TELEMETRY-OVERFLOW` | `NOT_APPLICABLE/consumed` | telemetry cannot become session/admission authority |
| `FS-AUDIT-OUTBOX-BACKLOG` | `DEFERRED_BY_ACCEPTED_GATE` | ANL/DUR own durable audit backlog; security-required admission/takeover audit may not silently downgrade |
| `FS-EVENT-DUPLICATE-DELIVERY` | `NOT_APPLICABLE/consumed` | analytics replay cannot alter session authority |
| `FS-EVENT-OUT-OF-ORDER` | `NOT_APPLICABLE/consumed` | analytics order cannot alter session authority |
| `FS-AUDIT-MUTATION-MISMATCH` | `DEFERRED_BY_ACCEPTED_GATE` | final durable admission/takeover/audit atomicity remains ANL/DUR-owned |
| `FS-ANALYTICS-PRIVACY-POLICY` | `NOT_APPLICABLE/consumed` | session credentials never enter analytics payloads |
| `FS-DETECTOR-FALSE-POSITIVE` | `NOT_APPLICABLE` | analytics cannot revoke/sanction autonomously |
| `FS-INVESTIGATION-MUTATION-ATTEMPT` | `NOT_APPLICABLE` | investigation cannot mutate session/runtime authority |

### Candidate missing scenarios

The existing catalogue can express most FND-04 safety through current IDs, but two attack/failure cases deserve explicit consideration before the final contract freezes the catalogue:

1. replay of a consumed/expired/wrong-bound **pre-admission grant** without a simultaneous duplicate-login race;
2. replay/loss-race of an old **reconnect credential** during transport rebind.

They can technically map to `FS-GATEWAY-AFTER-REDEEM`, `FS-STALE-GENERATION`, `SESSION_REJECTED` and existing replay invariants. The final FND-04 review should decide whether distinct stable failure IDs improve E2E/audit clarity enough to justify adding them. This analysis does not expand the global catalogue yet.

## 28. Error mapping direction

Recommended category mapping:

| Condition | Foundation category |
|---|---|
| malformed admission/reconnect payload | `INVALID_INPUT` |
| bad signature/proof/unknown trusted issuer | `AUTHENTICATION_FAILED` |
| expired, consumed, replayed, wrong-audience or wrong-bound credential | `SESSION_REJECTED` |
| protocol/ruleset/content/route revision mismatch | `UNSUPPORTED_REVISION` |
| stale connection/account/character/ownership generation | `STALE_GENERATION` |
| healthy incumbent or current lifecycle prevents takeover | `CONFLICT` |
| admission/session resource bound reached | `CAPACITY_EXCEEDED` |
| required Platform/key/lease/persistence authority unavailable | `DEPENDENCY_UNAVAILABLE` |
| bounded admission/reconnect/takeover deadline expired | `TIMEOUT` |
| explicit safe cancellation before commit | `CANCELLED` |
| unexpected internal state where safe authority cannot be proven | `INTERNAL_UNAVAILABLE` |

The final public numeric codes should be narrower and stable but must never expose raw SQL errors, key IDs beyond safe diagnostics, token contents, secret hashes, internal stack traces or exact combat state unless product/privacy policy explicitly allows it.

## 29. Security and privacy requirements

The final contract should require:

- no reusable account password/OAuth bearer token sent to the game server;
- admission and reconnect credentials redacted from logs/traces/crash reports;
- GameSessionId alone never authorizes control;
- AccountId/CharacterId ownership revalidated at current authority, not trusted from UI/cache alone;
- no client timestamp as expiry/liveness authority;
- no token-selected arbitrary verification URL/key source;
- key purpose separation and explicit credential typing;
- bounded replay records and credential material size;
- rate limits for repeated admission/reconnect/takeover attempts defined before production implementation;
- auditable takeover, lease replacement and security-terminal failures;
- high-cardinality session/player IDs excluded from ordinary metrics labels;
- current generation/fence evidence included in authorized diagnostic correlation without credential contents.

## 30. Player-facing consequences

The recommended model aims to provide:

- fast same-session recovery for genuine brief connection loss;
- no surprise logout merely because the concrete socket is closed at five seconds;
- no combat escape by switching characters;
- no malicious second-client kick of a healthy combat-locked player;
- the ability to recover the same in-world actor even after the old GameSession expires, using a fresh session when safe;
- no hidden heal/teleport/reset from reconnect;
- clear bounded rejection instead of ambiguous dual-login behavior.

Risk to watch: excessive liveness false positives or repeated disconnect-protection farming. Those require measured fault tests and player-behavior evidence before production values are frozen.

## 31. Producer/operations consequences

The recommended separation allows:

- Platform/Gateway outage to block **new** authorization without necessarily killing existing gameplay;
- GameNodes to validate signed pre-admission grants without a synchronous Platform introspection on every normal admission;
- key rotation independent from game deployment when compatible key sets are staged;
- character/account fencing to remain game-domain authority;
- GameSession recovery to remain independent of concrete NodeId;
- future proof-of-possession or stronger device security without redefining GameSessionId.

Costs include explicit key-distribution/revocation operations, bounded grant-consumption state, account/character lease coordination and more failure-state tests than a legacy password login server.

## 32. Final FND-04 contract inputs still required

Before the final contract can be accepted, the package should resolve these remaining items explicitly:

1. accept/reject hybrid signed + one-time-consume grant direction;
2. select exact signed container/algorithm/library contract through a bounded cross-language security spike or named evidence;
3. define concrete pre-admission TTL and wall-clock skew limits;
4. choose exact verification-key refresh/retiring/emergency-revocation windows;
5. define reconnect secret entropy/representation and bounded verifier retention;
6. accept/reject reauthenticated same-GameSession recovery inside the 15-second grace;
7. accept/reject fresh-GameSession attachment to an existing `PRESENT_UNCONTROLLED` actor after grace expiry;
8. accept the proposed 15-second grace start at `control_loss_declared_at`;
9. define concrete liveness-probe cadence/hysteresis compatible with the 2-second boundary;
10. define concrete lease TTL/renewal/safety margin or explicitly assign a pre-implementation measured gate with hard acceptance before production;
11. decide whether a control-loss episode needs anti-flap hysteresis to prevent repeated 4-second protection farming;
12. decide whether admission-grant and reconnect-credential replay deserve new stable `FOUNDATION_FAILURE_SCENARIOS` IDs;
13. reconcile exact Channel↔Instance versus Channel↔Channel GameSession continuity rules;
14. define final stable session/takeover/admission error codes and their safe client presentation classes.

## 33. Recommended concise model

```text
Platform password/OAuth/MFA
-> Platform Identity only

Game Login Ticket
-> one-time Platform identity authorization
-> Gateway redeems it

PreAdmissionGrant
-> Platform-owned dedicated admission issuer
-> short-lived signed capability
-> bound AccountId + CharacterId + WorldId + ChannelId + revisions + audience
-> random one-time grant nonce
-> game-side atomic consume
-> never GameSessionId

fresh admission commit
-> revalidate current AccountId -> CharacterId ownership
-> atomically establish AccountPresenceClaim
-> establish/fence CharacterAuthorityLease
-> consume grant
-> create canonical GameSessionId
-> connection_generation = 1
-> issue opaque rotating reconnect secret
-> only then publish admission success

brief unexpected control loss
-> FND-04 accepts sufficient current-generation liveness evidence semantics
-> FND-03 measures T0 monotonic
-> T0 + 2s: accepted disconnect PvE protection
-> T0 + 5s: stale concrete transport may close
-> control_loss_declared_at + 15s: same-GameSession grace expires

eligible fast resume
-> same GameSessionId
-> newer connection_generation
-> rotate reconnect secret
-> old transport generation fenced
-> FND-03 applies accepted 4s defensive PvE re-entry effect

old GameSession grace expired but actor must remain
-> old GameSession terminal
-> actor PRESENT_UNCONTROLLED
-> account presence still occupied by same CharacterId
-> fresh authenticated same-character admission may create new GameSessionId and attach to existing actor if final contract accepts this direction
-> different CharacterId remains blocked

intentional newcomer takeover
-> healthy combat-locked incumbent: reject/hold, do not kick
-> logout-eligible incumbent: fenced legal logout/transition
-> newcomer gets fresh GameSessionId only after old authority is safely gone
```

## 34. Gate result of this analysis

If this analysis baseline passes review and merges, it does **not** complete FND-04.

It authorizes no runtime implementation.

It should become the bounded evidence input for one later final architecture-only `FND-04 Identity, Game Session, Admission and Character Lease Contract` package that freezes only the decisions genuinely required before implementation.
