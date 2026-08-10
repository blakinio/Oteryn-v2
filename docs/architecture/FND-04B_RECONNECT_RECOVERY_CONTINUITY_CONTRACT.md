# FND-04B — Reconnect, Recovery and Continuity Contract

- Status: Candidate bounded architecture contract; canonical only when the owning FND-04B delivery merges
- Gate: `FND-04B`
- Programme: Issue #112
- Owning delivery: Issue #127 / PR #128
- Repository: `blakinio/Oteryn-v2`
- Trusted base: `main@2fd7bac4879f381d5b97230732076df2e9c61f95`
- Historical reviewed evidence only: superseded PR #109 exact head `bf82e392d6ef8b1e627849cdc7383af9a7c987ae`
- Normative recovery profile: `docs/contracts/FND-04_REAUTHENTICATED_RECOVERY_GRANT_PROFILE_V1.md`
- Consumes: accepted FND-04A; FND-02; accepted FND-03; ADR-0003; ADR-0012; FND-ID-01; disconnect/re-entry owner decisions; Foundation Error Vocabulary
- Does not authorize: runtime/protocol/persistence/Platform/KMS/deployment/production implementation or final FND-04C integration

## 1. Purpose

FND-04B freezes the game-domain rules for restoring player control after transport/process loss without split control, stale-writer resurrection, replayable authority, actor reset or security downgrade.

Central invariant:

```text
one GameSession
-> at most one current playable TransportBinding generation
-> replacement authority changes only at one revalidated atomic boundary
-> stale/prepared/old transports never regain command/liveness/fencing authority
```

FND-04A fresh-admission authority remains unchanged. A fresh grant is never a reconnect or recovery credential.

## 2. Authority layers consumed from FND-04A

These remain distinct:

- `AccountPresenceClaim` — account-global mandatory-presence ownership;
- `CharacterLease` + non-reused generation — current character writer/control fence;
- `GameSessionId` — logical control lifecycle identity, never bearer proof;
- `TransportBinding = GameSessionId + connection_generation` — current concrete playable transport fence;
- `RuntimeScopeAuthority` — current ChannelRuntime/InstanceRuntime owner + ownership generation.

`NodeId` remains process-incarnation/placement evidence, not authority.

FND-04B adds no foundation identity. `HandoffId` is not used for ordinary reconnect/recovery; it remains conditional for a separately accepted real handoff transition.

## 3. Actor and GameSession continuity states

Actor presence uses:

```text
ABSENT
PRESENT_CONTROLLED
PRESENT_UNCONTROLLED
```

The continuity state machine MUST preserve the semantics of:

```text
ACTIVE
CONTROL_SUSPECTED
RECONNECTABLE
TERMINATING
TERMINAL
```

### ACTIVE

One current `connection_generation` has sufficient server-authoritative playable-control evidence.

### CONTROL_SUSPECTED

Evidence is late/ambiguous but authoritative unexpected-control loss is not yet proven. Suspicion alone:

- does not permit bearer-proof preemption;
- does not create `ControlLossEpoch`;
- does not start same-session grace;
- does not grant PvE protection;
- does not terminalize the GameSession.

### RECONNECTABLE

The server crossed the accepted unexpected playable-control-loss boundary. The GameSession remains eligible for finite same-session continuity until its grace deadline.

### TERMINATING / TERMINAL

No new ordinary command authority is created. A terminal `GameSessionId` never becomes authoritative again. The actor may remain `PRESENT_UNCONTROLLED` until ordinary gameplay/logout/lifecycle rules permit `ABSENT`.

## 4. Server-authoritative liveness

FND-02 authenticated probe/ack semantics are the primitive. Liveness MUST NOT be inferred solely from:

- socket-open state;
- TCP keepalive state;
- gameplay-command silence;
- client self-report;
- OS/Launcher/Guardian evidence.

Client/OS/Launcher/Guardian evidence remains corroborative only under accepted privacy/forensic baselines.

The following numeric values are deliberately **not** frozen here:

- probe cadence;
- missed-probe threshold/hysteresis;
- exact control-loss detection delay;
- stale transport cleanup delay;
- same-GameSession grace duration;
- scheduler/clock safety margins.

They MUST be finite/bounded before implementation activation and require measured OPS/PERF/network/fault evidence. Historical `2s/5s/15s` candidate values from superseded #109 are non-canonical.

## 5. ControlLossEpoch

`ControlLossEpoch` is a logical server-authoritative loss episode, not a new foundation entity identity and not a client-provided value.

An epoch begins only when the current game authority crosses the accepted unexpected playable-control-loss boundary for a previously controlled actor/GameSession.

It does **not** begin from:

- graceful logout;
- ordinary fresh login;
- healthy-session migration;
- socket close alone;
- PREPARE creation;
- failed/stale reconnect or recovery attempt;
- client crash report alone;
- process restart without proof that playable control was actually lost.

One continuous loss episode has one logical epoch. Retries, multiple candidates, failed COMMITs, recovery-grant retries or runtime-owner relocation do not create a new epoch.

A new epoch may be created only after playable control was successfully restored and later independently lost again.

The implementation MUST preserve an internal non-reused epoch discriminator/ordinal or equivalently strong evidence sufficient to distinguish epochs and prove whether the exact epoch's protection was already activated. This is internal continuity state, not a public foundation ID.

## 6. Same-session grace semantics

The same-session grace duration is finite but its numeric value is deferred.

Its **origin is not deferred**:

```text
same-session grace begins at the authoritative ControlLossEpoch boundary
```

It does not begin at socket close, first missed probe, stale-transport cleanup or first reconnect attempt.

The grace deadline is server-authoritative continuity state. Runtime/process replacement MUST preserve the original deadline/remaining eligibility; failover or restart cannot restart/extend grace.

If current authority cannot prove the original epoch/deadline safely, it MUST NOT guess a new same-session window.

Stale-transport cleanup is a separate resource lifecycle and does not redefine the logical grace deadline.

## 7. Defensive PvE re-entry protection

The accepted owner decision is exact:

```text
eligible valid re-entry after unexpected playable-control loss
-> exactly 4 seconds defensive PvE protection
```

Protection begins when authoritative playable control is successfully restored for that eligible `ControlLossEpoch`, not when suspicion/loss begins.

Per epoch:

- activation occurs at most once;
- repeated reconnect/recovery within the same epoch does not reset/extend it;
- failed PREPARE/COMMIT does not activate it;
- graceful logout/login does not receive it;
- healthy migration does not receive it.

The protection deadline itself is authoritative continuity state and MUST survive runtime-owner/process replacement without restarting the 4-second interval.

During protection:

- movement allowed;
- self-healing allowed under ordinary costs/cooldowns/exhaustion;
- health/mana/resource potions allowed under ordinary rules;
- offensive PvE actions prohibited and not buffered;
- healing another player prohibited;
- receiving otherwise legal healing allowed;
- no HP/resource/position/condition/cooldown/combat/PZ/logout/threat/aggro/encounter/committed-effect reset.

Protection is derived from server-authoritative loss/re-entry state, never from client diagnostics.

## 8. Fast reconnect proof

Fast reconnect is game-domain same-session continuity and does not require new Platform authorization while current game-domain proof remains valid.

The reconnect proof MUST be:

- high entropy and unguessable;
- bearer-sensitive secret material distinct from GameSessionId;
- issued only after a successful authoritative session/control boundary;
- scoped to one current GameSession continuity chain;
- accepted only over authenticated FND-02/TLS transport;
- secret-safe: raw proof never enters ordinary logs/metrics/analytics;
- rotated on every successful same-GameSession replacement;
- predecessor-fenced so an old proof cannot authorize a later generation.

Exact hashing/storage/KMS mechanics and future sender-constrained/PoP form are deferred.

Possession alone never permits eviction of a healthy current binding.

## 9. Healthy current binding is non-preemptible

When current `connection_generation` still has sufficient server-authoritative playable-control evidence, an unsolicited reconnect/recovery contender MUST fail without authority change, even if it presents:

- current reconnect proof;
- correctly signed reauthenticated recovery grant;
- matching identity/session data;
- fresh attempt reference.

The rejected contender:

- gets no command/liveness authority;
- does not advance generation;
- does not fence/close incumbent as an authority effect;
- does not activate/rotate successor proof;
- does not create loss epoch/protection;
- consumes no recovery nonce as success.

Healthy-session migration is a separate future contract requiring authorization rooted in current authoritative generation; reconnect proof alone is insufficient.

## 10. ReconnectAttemptRef and PREPARE

Every rebind attempt has an idempotency/correlation reference `ReconnectAttemptRef`. It is operation identity, not foundation entity identity and not bearer authority.

A successful PREPARE creates a bounded candidate transition semantically bound to:

```text
GameSessionId
ReconnectAttemptRef
predecessor connection_generation
candidate connection_generation = strict successor
exact candidate authenticated transport
proof class used
finite prepared deadline
current authority/reconciliation observations needed for revalidation
```

### 10.1 Candidate successor reconnect proof

PREPARE MAY generate and deliver one candidate successor reconnect proof to the exact prepared candidate transport.

Rules:

- before COMMIT it is **inactive** and grants no authority;
- it is bound to the exact prepared attempt/session/candidate generation;
- retrying the same PREPARE on the same eligible candidate transport returns the same logical candidate/proof, not another independently usable proof;
- if candidate aborts/expires/supersedes, that candidate proof is permanently invalid;
- COMMIT atomically activates exactly that candidate proof while invalidating/fencing predecessor proof;
- this pattern allows a client to already possess the successor proof if COMMIT succeeds but its final response is lost.

An implementation may use an equivalently safe secret-delivery construction only if it proves the same lost-response and predecessor-fencing invariants.

### 10.2 PREPARE has no authority

Prepared state:

- grants no gameplay command authority;
- grants no liveness authority;
- does not fence predecessor;
- does not make successor proof current;
- does not consume RecoveryGrantNonce as success;
- cannot survive its finite deadline;
- cannot be rebound to a different transport/attempt/session.

At most one candidate may commit for one predecessor generation. Pending-candidate resources MUST be bounded; exact numeric limits are later registry evidence.

## 11. PREPARE eligibility

Fast reconnect PREPARE requires at minimum:

- GameSession `RECONNECTABLE`, not terminal/superseded;
- same-session grace still valid from original loss epoch;
- no healthy current controller;
- reconnect proof current for that continuity chain;
- predecessor generation/session match;
- AccountPresenceClaim and CharacterLease compatible;
- current runtime owner/placement resolves same session/actor;
- FND-02 reconciliation state can continue safely.

Reauthenticated same-session recovery uses the recovery profile in place of missing reconnect proof.

PREPARE is eligibility only; it never escrows authority.

## 12. COMMIT atomic revalidation and switch

Immediately before and atomically with same-session switch, COMMIT revalidates:

1. exact candidate exists, unexpired, bound to candidate transport/session/attempt;
2. predecessor generation still exactly matches preparation source;
3. GameSession remains reconnect-eligible and original grace deadline remains valid;
4. no healthy playable controller regained current-generation authority;
5. AccountPresenceClaim still denotes same CharacterId;
6. CharacterLease generation/current authority remains compatible;
7. RuntimeScopeAuthority/placement/ownership generation still owns transition;
8. FND-02 command/server-sequence/state-domain reconciliation boundary remains safe;
9. no newer handoff/takeover/fence/terminal transition supersedes candidate;
10. proof-specific requirements remain current, including recovery-grant time/security/trust/revisions/nonce when applicable.

Only if all succeed does one atomic boundary:

```text
fence predecessor transport authority
+ make candidate connection_generation current
+ bind command/liveness/reconciliation authority to candidate transport
+ activate candidate successor reconnect proof
+ invalidate predecessor reconnect proof
+ preserve GameSessionId
+ preserve CommandId/server_sequence/domain revisions under FND-02
+ preserve actor/gameplay state
+ mark eligible ControlLossEpoch re-entered
+ activate that epoch's one-time exact 4s PvE protection if not previously activated
```

Success is externally visible only after commit.

## 13. Failed/stale COMMIT

A failed candidate is non-mutating with respect to gameplay authority.

It MUST NOT:

- advance candidate generation;
- revive predecessor already fenced/superseded;
- activate candidate successor proof;
- invalidate a currently valid proof due only to failed candidate;
- consume RecoveryGrantNonce as success;
- manufacture loss epoch/protection;
- roll current authority back to PREPARE-time state.

Candidate successor proof becomes permanently unusable when candidate aborts/expires/supersedes.

Whatever authority is actually current at revalidation remains current.

Prepared expiry is distinct from grace expiry: an expired candidate cannot resume, but a new PREPARE may be attempted only if current state/proof and original grace deadline still independently permit it.

## 14. Lost response and idempotent reconciliation

Retrying the same `ReconnectAttemptRef` receives stable disposition:

- committed/already committed;
- prepared/pending if still valid;
- aborted;
- prepared expired;
- terminally superseded.

A lost COMMIT response cannot cause a blind second authority switch.

If COMMIT succeeded:

- predecessor generation/proof remain fenced;
- candidate generation/proof remain current;
- same attempt reconciles the committed result;
- the committed response may be replayed only on the exact current authenticated candidate transport or another equivalently proven current-generation channel; it MUST NOT leak current proof to an unproven transport.

Because the candidate successor proof may be delivered inactive during PREPARE, loss of the COMMIT response alone does not necessarily strand the client.

If both the committed transport and its successor proof are lost/unavailable, old predecessor proof does not revive; recovery proceeds through reauthenticated recovery.

If server/process recovery cannot prove whether a candidate committed, current authority/generation/proof state must be reconstructed from fenced authoritative evidence before accepting further same-session authority. If that cannot be proven, fail closed; do not guess a winner or revive predecessor.

## 15. Same-GameSession continuity

Successful same-session reconnect/recovery:

- preserves GameSessionId;
- establishes strictly newer `connection_generation`;
- preserves actor identity/state;
- preserves FND-02 `CommandId` identity/order;
- preserves `server_sequence` and typed domain revisions;
- resumes only from provable reconciliation boundary;
- uses explicit resync/snapshot when sequence/revision continuity cannot be proven;
- never guesses through gaps.

A stale physically open old socket has zero command/liveness/fencing authority after new generation commits.

## 16. Reauthenticated recovery grant

When reconnect proof is unavailable, Platform may freshly authenticate and issue only `oteryn-reauth-recovery-v1`.

It proves only:

```text
Platform freshly authenticated AccountId
AND Platform currently authorizes an attempt to recover CharacterId in WorldId
```

It does not prove session existence, reconnectability, actor presence, current placement, lease/runtime ownership, right to evict healthy controller or right to recreate/reset actor.

Before world/actor/controller classification, Oteryn-v2 MUST prove current `AccountId -> CharacterId` ownership/lifecycle first. Only then may it validate current `CharacterId -> WorldId`/eligibility and resolve current actor/session.

Recovery carries no ChannelId, InstanceId, NodeId or runtime ownership generation as authority.

## 17. Recovery revision/security rules

Recovery independently binds:

```text
protocol_major
transport_profile
ruleset_revision
content_revision
map_revision
world_policy_revision
```

No opaque `compatibility_revision` exists. Each dimension validates independently against current actor/session/runtime transition boundary.

FND-02 `schema_revision` remains diagnostic/build evidence, not exact recovery equality.

Platform-security and recovery signing-key/profile trust evidence preserve accepted FND-04A model:

- authenticated source authority/purpose/scope;
- authenticated source observation provenance;
- conservative `upper_bound_source_age <= 5s` including uncertainty;
- cache operations never re-age evidence;
- monotonic/comparable source revision/fence;
- older allow/trust cannot roll back newer deny/revoke;
- equal revision contradictory content fails closed;
- restart must reconstruct current non-rollback floor before authorizing.

PREPARE/earlier validation is never trust escrow; mutable proof-specific security/trust facts revalidate at COMMIT.

## 18. Recovery result ordering

After credential authentication/security and ownership-safe account/character/world validation:

1. healthy current playable controller -> dedicated conflict;
2. same GameSession reconnect-eligible and original grace deadline valid -> same-session recovery via PREPARE/COMMIT;
3. prior GameSession terminal but same actor remains `PRESENT_UNCONTROLLED` -> post-grace recovery with new GameSession;
4. otherwise -> recovery target not eligible.

Healthy-controller conflict cannot be hidden as generic no-target.

## 19. Same-session reauthenticated recovery

Uses same PREPARE/COMMIT state machine, with recovery grant replacing missing reconnect proof.

COMMIT additionally revalidates atomically:

- recovery JWT time/lifetime/skew;
- exact recovery credential authentication/trust state;
- authenticated key/profile trust evidence source age/order/current decision;
- authenticated Platform-security evidence source age/order/account generation/state;
- RecoveryGrantNonce eligibility;
- each independent protocol/transport/ruleset/content/map/world-policy revision;
- AccountId->CharacterId ownership first;
- CharacterId->WorldId/eligibility second.

RecoveryGrantNonce is consumed only with successful authority switch.

## 20. Grace expiry and post-grace recovery

Once the authoritative same-session grace deadline expires:

- old GameSession proceeds to terminality under lifecycle rules;
- that GameSessionId cannot revive;
- reconnect proof cannot resurrect it;
- old prepared candidates cannot commit;
- actor may remain `PRESENT_UNCONTROLLED` while gameplay/combat/logout rules require presence.

Later eligible control uses reauthenticated post-grace recovery and a **new GameSessionId**.

Post-grace recovery requires:

- valid AccountId->CharacterId ownership;
- current CharacterId->WorldId/eligibility matches grant;
- prior GameSession terminal;
- same actor remains `PRESENT_UNCONTROLLED`;
- no current playable controller;
- AccountPresenceClaim remains same CharacterId;
- current CharacterLease/runtime authority owns actor;
- current placement resolved by game authority;
- all independent recovery revisions current/supported.

One atomic commit revalidates all mutable facts plus recovery JWT/security/trust/nonce.

Success:

```text
preserve existing actor exactly
+ create new canonical GameSessionId
+ establish connection_generation = 1
+ establish new current reconnect proof
+ establish fresh authoritative snapshot/reconciliation boundary
+ consume RecoveryGrantNonce
+ restore playable control
```

It MUST NOT respawn, teleport, heal, refill resources, clear conditions/cooldowns/combat/PZ/logout/threat/aggro/encounter state or undo committed effects.

If the same original `ControlLossEpoch` remains provably eligible and its protection was never activated, this valid re-entry may activate that epoch's single 4-second protection. Post-grace status alone does not create a new epoch.

## 21. Recovery locator and current placement

Platform grant does not authorize concrete Channel/Instance/Node.

Game domain resolves current recovery location using authoritative indexes/state, then revalidates with current runtime owner before commit.

Requirements:

- locator result is routing evidence, not authority;
- stale locator cannot attach control to former owner;
- current RuntimeScopeAuthority generation fences old owners;
- NodeId/process replacement is not session/actor authority;
- current owner must prove actor/session state it continues/recovers.

## 22. GameNode/process failure

GameNode crash is distinct from ordinary client network loss.

After process/scope-owner replacement:

- new NodeId never implies prior session authority;
- old ownership generation cannot commit command/save/control transition;
- same-GameSession continuity is allowed only if fenced recoverable evidence proves at minimum current GameSessionId, current/last connection generation, reconnect-proof current/candidate/rotation state, ReconnectAttempt dispositions needed for ambiguity resolution, original ControlLossEpoch and grace deadline, protection activation/expiry state, session terminality, actor/lease state and FND-02 reconciliation boundary;
- if continuity cannot be proven, same GameSession MUST NOT be guessed/recreated;
- when actor remains authoritative but same-session continuity cannot be proven or grace is invalid, recovery may proceed only through accepted post-grace path once old GameSession is terminal/fenced;
- if actor presence itself cannot be proven safely, fail closed rather than respawn/duplicate.

Process failure may create a loss epoch only when current game authority can prove previously playable control was unexpectedly lost; process restart itself is not trigger.

## 23. Channel/Instance continuity and handoff

Ordinary reconnect/recovery follows current authoritative actor placement; it does not choose a new Channel/Instance from stale credential.

If legitimate handoff is concurrently in progress:

- handoff/fencing state participates in COMMIT revalidation;
- stale reconnect cannot resurrect source owner;
- locator resolves current post-handoff authority;
- `HandoffId` appears only if separately accepted handoff contract requires it;
- ordinary reconnect does not manufacture `HandoffId`.

## 24. Security/privacy

Never log/export raw reconnect proof, candidate successor proof, recovery JWT, RecoveryGrantNonce, OAuth/Game Login Ticket/private key/future PoP material.

Before successful recovery authentication, diagnostics MUST NOT expose whether semantic issuer/audience/profile/purpose/typ/schema/world/actor/controller state matched.

AccountId/CharacterId remain privacy-controlled, not ordinary metric labels. Game Intelligence may consume bounded/audited security events for investigation but cannot autonomously ban, sanction, mutate gameplay or decide reconnect authority.

No kernel driver, invasive anti-cheat or mandatory device fingerprint is authorized.

## 25. FND-04B error subset

FND-04C will integrate the complete catalogue. FND-04B freezes semantic outcomes of its transitions.

| Code | Category | Progression | Retry / next authority | Mutation outcome | Public class | Redacted diagnostic |
|---|---|---|---|---|---|---|
| `RECONNECT_PROOF_INVALID` | `AUTHENTICATION_FAILED` | `SECURITY_TERMINAL` | current proof or reauthenticated recovery | none | `AUTHENTICATION_REQUIRED` | `reconnect proof authentication failed` |
| `RECONNECT_HEALTHY_BINDING_PRESENT` | `CONFLICT` | `TERMINAL` for unsolicited attempt | incumbent remains authority | none | `CHARACTER_ALREADY_ACTIVE` | `current playable controller remains authoritative` |
| `RECONNECT_NOT_ELIGIBLE` | `SESSION_REJECTED` | `TERMINAL` for same-session path | resolve current recovery path | none | `SESSION_UNAVAILABLE` | `session is not eligible for same-session reconnect` |
| `RECONNECT_PREPARED_EXPIRED` | `TIMEOUT` | `TERMINAL` for candidate | new PREPARE only if original grace/current facts permit | candidate aborted; current authority unchanged | `TEMPORARILY_UNAVAILABLE` | `prepared reconnect candidate expired` |
| `RECONNECT_PREPARED_STALE` | `STALE_GENERATION` | `TERMINAL` | reconcile current authority; new attempt if eligible | none | `SESSION_UNAVAILABLE` | `prepared reconnect candidate no longer current` |
| `RECONNECT_RECONCILIATION_UNAVAILABLE` | `INTERNAL_UNAVAILABLE` | `RETRYABLE` bounded same-attempt/current-authority reconciliation | do not create new authority until current winner/fence can be proven | none | `TEMPORARILY_UNAVAILABLE` | `reconnect authority outcome requires reconciliation` |
| `RECONNECT_GRACE_EXPIRED` | `SESSION_REJECTED` | `TERMINAL` for old GameSession | post-grace recovery/fresh path as state permits | old GameSession cannot revive | `SESSION_UNAVAILABLE` | `same-session reconnect window expired` |
| `RECOVERY_GRANT_AUTHENTICATION_FAILED` | `AUTHENTICATION_FAILED` | `SECURITY_TERMINAL` | fresh authenticated recovery | none | `AUTHENTICATION_REQUIRED` | `recovery credential authentication failed` |
| `RECOVERY_GRANT_REVISION_UNSUPPORTED` | `UNSUPPORTED_REVISION` | `TERMINAL` | compatible producer/consumer revisions; no downgrade | none | `CLIENT_UPDATE_REQUIRED` | `recovery authoritative revision unsupported` |
| `RECOVERY_GRANT_SECURITY_EVIDENCE_STALE` | `DEPENDENCY_UNAVAILABLE` | `RETRYABLE` while proof/target remains valid | refresh authenticated non-rollback evidence | no nonce/authority mutation | `TEMPORARILY_UNAVAILABLE` | `recovery security evidence unavailable, stale or superseded` |
| `RECOVERY_HEALTHY_CONTROLLER_PRESENT` | `CONFLICT` | `TERMINAL` | incumbent remains authority | none | `CHARACTER_ALREADY_ACTIVE` | `recovery blocked by current playable controller` |
| `RECOVERY_TARGET_NOT_ELIGIBLE` | `SESSION_REJECTED` | `TERMINAL` | resolve current actor/session flow | none | `SESSION_UNAVAILABLE` | `recovery target is not eligible` |

Recovery-profile-specific malformed/binding/time/replay/security/world outcomes remain normative in the companion profile and are integrated by FND-04C.

Correlation fields must be credential-free and may include safe attempt reference, session/world identifiers where policy permits, generation relation class, transition state class and source-age/order buckets; never raw proofs/nonces/private fencing values.

## 26. Required race/fault evidence for implementation

### Reconnect

- stale/predecessor proof replay;
- two contenders after eligible loss -> one commit winner;
- healthy current generation + stolen proof -> incumbent not preempted;
- PREPARE then incumbent regains sufficient control -> COMMIT rejected;
- PREPARE then generation/session/lease/runtime owner changes -> reject;
- PREPARE expiry while original grace still valid -> new PREPARE only after fresh evaluation;
- grace expiry -> old GameSession cannot revive;
- PREPARE response loss -> same attempt returns same candidate proof, no second active proof;
- COMMIT success + lost response -> same attempt reconciles winner; predecessor remains fenced;
- COMMIT success + subsequent transport loss before usable successor proof -> predecessor proof does not revive; reauthenticated recovery required;
- physically open stale socket after winner -> commands/liveness rejected.

### Protection/liveness

- socket close without authoritative loss -> no epoch/grace/protection;
- grace origin equals loss epoch, not socket close/cleanup;
- graceful logout/login -> no protection;
- one loss epoch + multiple retries -> protection activates once for exactly 4s;
- process/runtime-owner replacement during grace/protection -> deadline is preserved, not restarted;
- restored stable control then later independently lost -> new epoch may receive own one-time protection;
- client/OS diagnostics cannot override server liveness classification.

### Recovery security

- companion profile crypto/schema/binding precedence fixtures;
- older allow/trust evidence cannot roll back newer deny/revoke while still <5s;
- cache refresh cannot re-age;
- restart without provable anti-rollback floor cannot authorize;
- key/profile revoke or Platform-security change after PREPARE before COMMIT -> fail before nonce/authority mutation.

### Ownership/world/actor

- non-owned CharacterId -> failure before world/actor/controller classification;
- valid ownership + stale world -> no recovery/retarget;
- healthy controller conflict not hidden as no-target;
- post-grace actor present -> new GameSession, no state reset;
- actor becomes ABSENT before commit -> reject, no recreation.

### GameNode/failover

- old owner command/control/save after ownership-generation replacement -> reject;
- new owner has complete fenced continuity evidence -> same-session continuation may proceed;
- new owner lacks proof/reconciliation/loss/grace/protection evidence -> same GameSession not guessed/recreated and deadlines not reset;
- stale locator -> current owner fence wins;
- handoff/reconnect race -> source owner never revived.

## 27. Decision timing

| Decision | Now? | Blocks | Risk if wrong later | Superseding evidence | Deferred |
|---|---|---|---|---|---|
| one current transport generation per GameSession | `YES` | protocol/session/runtime reconnect | split command/liveness authority | formal/fault proof of equivalent fencing | socket/session data structures |
| healthy binding non-preemptible by bearer proof | `YES` | reconnect/recovery security | stolen proof can kick healthy player | reviewed current-generation-authorized migration | healthy migration UX/protocol |
| PREPARE/COMMIT + COMMIT revalidation | `YES` | reconnect wire/runtime | stale authorization/lost-response ambiguity | proof of alternative linearizable protocol | persistence encoding/storage |
| inactive candidate successor proof activated at COMMIT or equivalent | `YES` | safe lost-response handling | commit-response loss can strand or resurrect predecessor proof | proof of equivalent secret-delivery/fencing scheme | exact secret encoding/storage |
| grace origin at ControlLossEpoch; deadline preserved across failover | `YES` | reconnect eligibility/abuse prevention | socket/restart timing changes player authority window | measured evidence + explicit semantic supersession | numeric grace duration |
| server-authoritative ControlLossEpoch + non-reused internal discriminator | `YES` | 4s protection/exactly-once semantics | retries/failover manufacture safety | evidence preserving same invariant | internal representation |
| exactly 4s PvE protection per eligible epoch | `YES`, already accepted | gameplay reconnect semantics | fairness/abuse contract | explicit owner gameplay supersession + evidence | timer implementation |
| exact liveness/grace/cleanup numbers | `NO` | implementation acceptance only | guessed values create false loss/abuse | measured network/load/fault/UX evidence | cadence/threshold/grace/cleanup |
| post-grace existing-actor recovery uses new GameSession | `YES` | actor/session recovery | reset/respawn exploit paths | proof preserving all actor state | physical storage |
| independent recovery revision dimensions | `YES` | recovery profile/rollout | opaque compatibility masks mixed state | coordinated supersession | physical revision registry |
| GameNode replacement requires complete fenced continuity evidence | `YES` | failover/recovery | guessed session resurrection/split authority | durable fault proof | checkpoint storage/RPO/RTO |

## 28. Acceptance boundary

FND-04B acceptance freezes reconnect/recovery/continuity semantics only.

FND-04C must still integrate complete errors/diagnostics, failure scenarios, compatibility/rollout evidence, programme status and thin final FND-04 index.

No runtime implementation is authorized.
