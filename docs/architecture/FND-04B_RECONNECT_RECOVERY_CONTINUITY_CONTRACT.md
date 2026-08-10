# FND-04B — Reconnect, Recovery and Continuity Contract

- Status: Candidate bounded architecture contract; canonical only when the owning FND-04B delivery merges
- Gate: `FND-04B`
- Programme: Issue #112
- Owning delivery: Issue #127
- Repository: `blakinio/Oteryn-v2`
- Trusted base: `main@2fd7bac4879f381d5b97230732076df2e9c61f95`
- Historical reviewed evidence only: superseded PR #109 exact head `bf82e392d6ef8b1e627849cdc7383af9a7c987ae`
- Normative recovery profile: `docs/contracts/FND-04_REAUTHENTICATED_RECOVERY_GRANT_PROFILE_V1.md`
- Consumes: accepted FND-04A; FND-02; accepted FND-03; ADR-0003; ADR-0012; FND-ID-01; disconnect/re-entry owner decisions; Foundation Error Vocabulary
- Does not authorize: runtime/protocol/persistence/Platform/KMS/deployment/production implementation or final FND-04C integration

## 1. Purpose

FND-04B freezes the game-domain rules for restoring player control after transport/process loss without creating split control, stale-writer resurrection, replayable authority, actor reset or security downgrade.

Central continuity invariant:

```text
one GameSession
-> at most one current playable TransportBinding generation
-> replacement authority changes only at one revalidated atomic boundary
-> stale/prepared/old transports never regain command or liveness authority
```

FND-04B does not alter FND-04A fresh-admission authority. A fresh grant is not a reconnect or recovery credential.

## 2. Authority and state consumed from FND-04A

The following remain distinct and MUST NOT be collapsed:

- `AccountPresenceClaim` — account-global mandatory-presence ownership;
- `CharacterLease` + non-reused generation — current character writer/control fence;
- `GameSessionId` — logical control lifecycle identity, never bearer proof;
- `TransportBinding = GameSessionId + connection_generation` — current concrete playable transport fence;
- `RuntimeScopeAuthority` — current ChannelRuntime/InstanceRuntime owner + ownership generation.

`NodeId` remains process-incarnation/placement evidence, not authority.

FND-04B adds no new foundation identity. `HandoffId` is not used for ordinary reconnect/recovery; it remains conditional for a separately defined real handoff transition.

## 3. Actor and GameSession continuity states

Actor presence uses the canonical states:

```text
ABSENT
PRESENT_CONTROLLED
PRESENT_UNCONTROLLED
```

FND-04B requires at minimum these GameSession continuity states or an implementation-equivalent state machine preserving the same externally relevant invariants:

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

Liveness evidence is late/ambiguous but the authoritative unexpected-control-loss boundary has not been crossed. Suspicion alone:

- does not permit bearer-proof preemption;
- does not create `ControlLossEpoch`;
- does not grant disconnect protection;
- does not terminalize the GameSession.

### RECONNECTABLE

The server has authoritatively classified unexpected loss of playable control. The GameSession remains eligible for bounded same-session continuity according to the evidence-backed grace policy.

### TERMINATING / TERMINAL

No new ordinary command authority is created. A terminal `GameSessionId` never becomes authoritative again. The actor may still remain `PRESENT_UNCONTROLLED` until ordinary gameplay/logout/lifecycle rules permit `ABSENT`.

## 4. Server-authoritative liveness

FND-02 authenticated probe/ack semantics are the primitive. Liveness MUST NOT be inferred solely from:

- socket-open state;
- TCP keepalive state;
- gameplay-command silence;
- client self-report;
- OS/Launcher/Guardian evidence.

Client/OS/Launcher/Guardian evidence remains corroborative only under the accepted privacy/forensic baselines.

The following numeric values are deliberately **not** frozen by FND-04B:

- probe cadence;
- missed-probe threshold/hysteresis;
- exact control-loss detection delay;
- stale transport cleanup delay;
- same-GameSession grace duration;
- scheduler/clock safety margins.

They MUST be finite/bounded before implementation activation and require measured OPS/PERF/network/fault evidence. Historical `2s/5s/15s` candidate values from superseded #109 are non-canonical.

## 5. ControlLossEpoch

`ControlLossEpoch` is a logical server-authoritative loss episode, not a new foundation identifier and not a client-provided value.

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

One continuous loss episode has one logical epoch. Transport retries, multiple PREPARE candidates, failed COMMITs, recovery-grant retries or current-owner relocation do not create a new epoch.

A new epoch may be created only after playable control was successfully restored and later lost again under a new independently classified unexpected-loss episode.

## 6. Defensive PvE re-entry protection

The accepted owner decision is exact:

```text
eligible valid re-entry after unexpected playable-control loss
-> exactly 4 seconds defensive PvE protection
```

The protection begins when authoritative playable control is successfully restored for that eligible `ControlLossEpoch`, not when suspicion or socket loss begins.

Per epoch:

- the 4-second protection may activate at most once;
- repeated rebind/recovery within the same epoch does not reset/extend it;
- failed PREPARE/COMMIT does not start it;
- graceful logout/login does not receive it;
- healthy migration does not receive it.

During protection, existing accepted gameplay semantics remain binding:

- movement allowed;
- self-healing allowed under ordinary costs/cooldowns/exhaustion;
- health/mana/resource potions allowed under ordinary rules;
- offensive PvE actions prohibited and not buffered;
- healing another player prohibited;
- receiving otherwise legal healing allowed;
- no HP/resource/position/condition/cooldown/combat/PZ/logout/threat/aggro/encounter/committed-effect reset.

Protection is gameplay state derived from server-authoritative loss/re-entry evidence, never from client diagnostics.

## 7. Fast reconnect proof

Fast reconnect is game-domain same-session continuity and does not require a new Platform authorization when the current game-domain proof remains valid.

The reconnect proof MUST be:

- high entropy and unguessable;
- bearer-sensitive secret material distinct from GameSessionId;
- issued only after a successful authoritative session/control boundary;
- scoped to exactly one current logical GameSession continuity chain;
- accepted only over the authenticated FND-02/TLS transport profile;
- stored/logged/exported only through secret-safe handling; raw proof MUST NOT enter ordinary logs/metrics/analytics;
- rotated on every successful rebind/recovery authority switch that preserves the GameSession;
- invalidated/fenced so predecessor proof cannot authorize a later generation.

Exact storage/hashing/KMS mechanism and future sender-constrained/PoP form are deferred. Possession alone never permits eviction of a healthy current binding.

## 8. Healthy current binding is non-preemptible

When the current `connection_generation` still has sufficient server-authoritative playable-control evidence, an unsolicited reconnect/recovery contender MUST fail without changing authority, even if it presents:

- the current reconnect proof;
- a correctly signed reauthenticated recovery grant;
- matching AccountId/CharacterId/GameSession information;
- a fresh attempt reference.

The rejected contender:

- gets no command/liveness authority;
- does not advance `connection_generation`;
- does not fence/close the incumbent as an authority effect;
- does not rotate reconnect proof;
- does not create `ControlLossEpoch` or 4-second protection;
- consumes no recovery nonce as a successful recovery.

Healthy-session migration is a separate future contract requiring authorization rooted in the current authoritative generation; reconnect proof alone is insufficient.

## 9. ReconnectAttemptRef and prepared transition

Every rebind attempt has an idempotency/correlation reference `ReconnectAttemptRef`. It is an operation reference, not a new foundation entity identity and not bearer authority.

A successful PREPARE creates a bounded candidate transition containing at least the semantic bindings:

```text
GameSessionId
ReconnectAttemptRef
predecessor connection_generation
candidate connection_generation = strict successor
exact candidate authenticated transport binding
proof class used (fast reconnect or reauthenticated recovery)
prepared-state deadline
current authority/reconciliation observations needed for revalidation
```

Prepared state:

- grants no gameplay command authority;
- grants no liveness authority;
- does not fence the predecessor;
- does not rotate the reconnect proof;
- does not consume RecoveryGrantNonce as success;
- cannot survive past its registered finite deadline;
- cannot be rebound to a different transport/attempt/session.

At most one candidate may commit for one predecessor generation. Implementations may allow multiple syntactically pending attempts only if linearization guarantees one winner and bounded resources; the safer default is one effective prepared candidate per session/predecessor generation.

## 10. PREPARE eligibility

Fast reconnect PREPARE requires at minimum:

- GameSession is `RECONNECTABLE` and not terminal/superseded;
- same-session grace remains valid;
- no healthy current controller;
- reconnect proof is current for that continuity chain;
- predecessor generation/current session identity match;
- AccountPresenceClaim and CharacterLease remain compatible;
- current runtime scope owner/placement can resolve the same session/actor;
- FND-02 reconciliation state can continue safely.

Reauthenticated same-session recovery uses the recovery profile and all requirements in Section 15 in place of the missing reconnect proof.

PREPARE is eligibility only; it never escrows authority.

## 11. COMMIT atomic revalidation and switch

Immediately before and atomically with a same-session authority switch, COMMIT MUST revalidate:

1. exact prepared transition exists, remains within its finite deadline and is bound to this candidate transport/session/attempt;
2. predecessor `connection_generation` is still exactly the generation from which this candidate was prepared;
3. GameSession remains reconnect-eligible and same-session grace remains valid;
4. no healthy playable controller has regained current-generation authority;
5. AccountPresenceClaim still denotes the same CharacterId;
6. CharacterLease generation/current authority remains compatible;
7. current RuntimeScopeAuthority/placement/ownership generation still owns the actor/session transition;
8. FND-02 command/server-sequence/state-domain reconciliation boundary remains safe;
9. no newer handoff/takeover/fence/terminal transition supersedes the candidate;
10. proof-specific requirements remain current, including recovery-grant time/security/trust/revisions/nonce where applicable.

Only if all revalidation succeeds does one atomic boundary:

```text
fence predecessor transport authority
+ make candidate connection_generation current
+ bind command/liveness/reconciliation authority to candidate transport
+ rotate current reconnect proof
+ preserve GameSessionId
+ preserve CommandId/server_sequence/domain revisions according to FND-02
+ preserve actor/gameplay state
+ mark the eligible ControlLossEpoch as re-entered
+ activate its one-time exact 4s defensive PvE protection if not already activated
```

Success becomes externally visible only after the switch commits.

## 12. Failed/stale COMMIT

A failed candidate is non-mutating with respect to gameplay authority.

It MUST NOT:

- advance candidate generation;
- revive a predecessor already fenced/superseded;
- rotate current proof;
- consume RecoveryGrantNonce as success;
- manufacture `ControlLossEpoch`/protection;
- roll current authority back to PREPARE-time state.

Whatever GameSession/TransportBinding/lease/runtime authority is actually current at revalidation remains current.

Prepared expiry is distinct from same-session grace expiry: an expired prepared candidate cannot resume, but a new PREPARE may be attempted only if current state/proof and same-session grace still independently permit it.

## 13. Lost response and idempotent reconciliation

A caller retrying the same `ReconnectAttemptRef` MUST receive a stable disposition for the same transition:

- committed/already committed;
- prepared/pending if still valid;
- aborted;
- prepared expired;
- terminally superseded.

A lost COMMIT response cannot permit a blind second authority switch. If the original transition committed, reconciliation reports that result; stale predecessor proof never regains authority.

A different `ReconnectAttemptRef` is a new candidate and must re-evaluate current authority from scratch.

## 14. Same-GameSession continuity

Successful same-session reconnect/recovery:

- preserves `GameSessionId`;
- establishes a strictly newer `connection_generation`;
- preserves current authoritative actor identity/state;
- preserves FND-02 `CommandId` identity/order semantics;
- preserves `server_sequence` and typed state-domain revisions;
- resumes only from a provable reconciliation boundary;
- requires explicit resync/snapshot if sequence/revision continuity cannot be proven;
- never guesses through gaps.

A stale old socket may remain physically open but has zero command/liveness/fencing authority after the new generation commits.

## 15. Reauthenticated recovery grant

When the reconnect proof is unavailable, Platform may freshly authenticate the account and issue only the dedicated `oteryn-reauth-recovery-v1` attempt grant.

The grant proves only:

```text
Platform freshly authenticated AccountId
AND Platform currently authorizes an attempt to recover CharacterId in WorldId
```

It does not prove:

- GameSession existence;
- reconnectability;
- actor presence;
- current Channel/Instance/Node placement;
- CharacterLease/runtime ownership;
- right to evict a healthy controller;
- right to respawn/reset/recreate the actor.

Oteryn-v2 owns those facts.

Before any recovery classification that could reveal world/actor/controller state, Oteryn-v2 MUST prove current `AccountId -> CharacterId` ownership/lifecycle first. Only then may it validate current `CharacterId -> WorldId`/world eligibility and resolve the actor/session.

Recovery does not carry ChannelId, InstanceId, NodeId or runtime ownership generation as authority.

## 16. Recovery grant revision/security rules

Recovery independently binds:

```text
protocol_major
transport_profile
ruleset_revision
content_revision
map_revision
world_policy_revision
```

No opaque `compatibility_revision` exists in v1. Each dimension is validated independently against the current actor/session/runtime boundary required by the chosen recovery transition.

FND-02 `schema_revision` remains diagnostic/build evidence, not exact recovery equality.

Platform-security evidence and recovery signing-key/profile trust evidence MUST use the same accepted model as FND-04A:

- authenticated source authority/purpose/scope;
- authenticated source observation provenance;
- conservative `upper_bound_source_age <= 5s` including clock uncertainty;
- cache receive/refresh/re-read never re-ages evidence;
- monotonic/comparable source revision/fence;
- older allow/trust cannot roll back a newer deny/revoke;
- equal revision with contradictory authenticated content fails closed;
- restart/recovery must reconstruct a current non-rollback floor before authorizing.

Earlier PREPARE/lookup validation is never trust escrow; proof-specific mutable security/trust facts are revalidated at COMMIT.

## 17. Recovery result ordering

After credential authentication/security and ownership-safe account/character/world validation, authoritative state is classified in this order:

1. **healthy current playable controller exists** -> dedicated conflict; bearer recovery proof cannot hide/preempt it;
2. **same GameSession is reconnect-eligible and same-session grace valid** -> same-session recovery via PREPARE/COMMIT;
3. **prior GameSession is terminal but same actor remains `PRESENT_UNCONTROLLED` and recoverable** -> post-grace existing-actor recovery with a fresh GameSession;
4. otherwise -> recovery target not eligible.

This ordering prevents generic no-target responses from becoming a bypass for healthy-controller protection.

## 18. Same-session reauthenticated recovery

Uses the same PREPARE/COMMIT state machine as fast reconnect, except recovery proof substitutes for the unavailable reconnect secret.

COMMIT additionally revalidates atomically:

- recovery JWT time/lifetime/skew;
- exact recovery credential authentication/trust state;
- authenticated key/profile trust evidence source age/order/current decision;
- authenticated Platform-security evidence source age/order/account generation/state;
- RecoveryGrantNonce eligibility;
- each independent protocol/transport/ruleset/content/map/world-policy revision;
- current AccountId->CharacterId ownership first;
- current CharacterId->WorldId/world eligibility second.

RecoveryGrantNonce is consumed only with a successful authority switch.

## 19. Same-session grace expiry

The same-session grace duration is finite but not numerically frozen here.

Once the authoritative grace boundary expires:

- the old GameSession transitions toward/into terminal according to the session lifecycle;
- that `GameSessionId` cannot be revived;
- reconnect proof cannot resurrect it;
- old prepared candidates cannot commit;
- the actor may remain `PRESENT_UNCONTROLLED` while gameplay/combat/logout rules require presence.

Later control, when eligible, uses post-grace recovery and a **new GameSessionId**.

## 20. Post-grace existing-actor recovery

A reauthenticated recovery grant may attach new control only when:

- current AccountId->CharacterId ownership is valid;
- current CharacterId->WorldId/world eligibility matches the grant;
- prior GameSession is terminal;
- same authoritative actor still exists as `PRESENT_UNCONTROLLED`;
- no current playable controller exists;
- AccountPresenceClaim still denotes the same CharacterId;
- current CharacterLease/runtime authority owns the actor;
- current runtime placement is resolved by game-domain authority;
- all independent recovery revisions are supported/current for the new session/snapshot boundary.

One atomic commit revalidates all mutable facts plus recovery JWT/security/trust/nonce immediately before authority creation.

Success:

```text
preserve existing actor exactly
+ create new canonical GameSessionId
+ establish connection_generation = 1 for the new session
+ establish new reconnect proof
+ establish fresh authoritative snapshot/reconciliation boundary
+ consume RecoveryGrantNonce
+ restore playable control
```

It MUST NOT respawn, teleport, heal, refill resources, clear conditions/cooldowns/combat/PZ/logout/threat/aggro/encounter state or undo committed effects.

If the original `ControlLossEpoch` is the eligible unresolved loss episode and its 4-second protection has not yet been activated, this valid re-entry may activate that same one-time protection. Post-grace status alone does not create a new epoch.

## 21. Recovery locator and current placement

Platform recovery grant intentionally does not authorize a concrete Channel/Instance/Node.

The game domain resolves current recovery location using current authoritative indexes/state, then revalidates with the current runtime owner before commit.

Requirements:

- locator result is routing evidence, not authority;
- stale locator cannot cause control attachment to a former owner;
- current RuntimeScopeAuthority ownership generation fences old owners;
- NodeId/process replacement is not session/actor authority;
- current owner must prove the actor/session state it is continuing or recovering.

## 22. GameNode/process failure

GameNode crash is distinct from ordinary client network loss.

After process/scope-owner replacement:

- new `NodeId` never implies authority over prior session state by itself;
- old ownership generation cannot commit commands/saves/control transitions;
- same-GameSession continuity is allowed only if recoverable/fenced evidence proves the current GameSessionId, current/last connection generation, reconnect-proof verifier/rotation state, session terminality/grace, actor/lease state and FND-02 reconciliation boundary required for safe continuation;
- if that continuity cannot be proven, the system MUST NOT guess/recreate the same GameSession;
- when the actor remains authoritative but same-session continuity cannot be proven or grace is no longer valid, recovery may proceed only through the accepted post-grace existing-actor path once the old GameSession is terminal/fenced;
- if actor presence itself cannot be proven safely, fail closed rather than respawn/duplicate it.

Process failure may cause a `ControlLossEpoch` only if the current game authority can prove that previously playable control was unexpectedly lost; process restart by itself is not the epoch trigger.

## 23. Channel/Instance continuity and handoff

Ordinary reconnect/recovery follows the current authoritative actor placement; it does not choose a new Channel/Instance from a stale credential.

If a legitimate Channel/Instance handoff is concurrently in progress:

- handoff/fencing state participates in COMMIT revalidation;
- stale reconnect candidate cannot resurrect the source owner;
- recovery locator resolves the current post-handoff authority;
- `HandoffId` is used only if a separately accepted handoff contract actually requires it;
- ordinary reconnect does not manufacture `HandoffId`.

## 24. Security/privacy

Never log/export raw reconnect proof, prepared successor proof, recovery JWT, RecoveryGrantNonce, OAuth/Game Login Ticket/private key/future PoP secret.

Before successful recovery credential authentication, diagnostics MUST NOT expose whether token semantic issuer/audience/profile/purpose/typ/schema/world/actor/controller state would have matched.

AccountId/CharacterId remain privacy-controlled and are not ordinary high-cardinality metric labels. Game Intelligence may consume bounded/audited security events for longitudinal investigation but cannot autonomously ban, sanction, mutate gameplay or decide runtime reconnect authority.

No kernel driver, invasive anti-cheat or mandatory device fingerprint is authorized.

## 25. FND-04B error subset

FND-04C will integrate the final cross-component catalogue. FND-04B nonetheless freezes the semantic outcome of its own transitions.

| Code | Category | Progression | Retry / next authority | Mutation outcome | Public class | Redacted diagnostic |
|---|---|---|---|---|---|---|
| `RECONNECT_PROOF_INVALID` | `AUTHENTICATION_FAILED` | `SECURITY_TERMINAL` | use current proof or reauthenticated recovery | no authority mutation | `AUTHENTICATION_REQUIRED` | `reconnect proof authentication failed` |
| `RECONNECT_HEALTHY_BINDING_PRESENT` | `CONFLICT` | `TERMINAL` for unsolicited attempt | incumbent remains authority | no authority mutation | `CHARACTER_ALREADY_ACTIVE` | `current playable controller remains authoritative` |
| `RECONNECT_NOT_ELIGIBLE` | `SESSION_REJECTED` | `TERMINAL` for this path | resolve current session/recovery path | no authority mutation | `SESSION_UNAVAILABLE` | `session is not eligible for same-session reconnect` |
| `RECONNECT_PREPARED_EXPIRED` | `TIMEOUT` | `TERMINAL` for candidate | new PREPARE only if grace/current facts permit | candidate aborted; current authority unchanged | `TEMPORARILY_UNAVAILABLE` | `prepared reconnect candidate expired` |
| `RECONNECT_PREPARED_STALE` | `STALE_GENERATION` | `TERMINAL` | reconcile current authority; new attempt if eligible | no authority mutation | `SESSION_UNAVAILABLE` | `prepared reconnect candidate no longer current` |
| `RECONNECT_GRACE_EXPIRED` | `SESSION_REJECTED` | `TERMINAL` for same GameSession | reauthenticated post-grace recovery or ordinary fresh path as state permits | old GameSession cannot revive | `SESSION_UNAVAILABLE` | `same-session reconnect window expired` |
| `RECOVERY_GRANT_MALFORMED` | `INVALID_INPUT` | `TERMINAL` | obtain valid grant | no authority mutation | `RETRY_LOGIN` | `recovery grant malformed` |
| `RECOVERY_GRANT_AUTHENTICATION_FAILED` | `AUTHENTICATION_FAILED` | `SECURITY_TERMINAL` | fresh authenticated recovery | no authority mutation | `AUTHENTICATION_REQUIRED` | `recovery credential authentication failed` |
| `RECOVERY_GRANT_BINDING_MISMATCH` | `SESSION_REJECTED` | `SECURITY_TERMINAL` | newly issued correct-bound grant | no authority mutation | `RETRY_LOGIN` | `recovery credential bound to a different context` |
| `RECOVERY_GRANT_REVISION_UNSUPPORTED` | `UNSUPPORTED_REVISION` | `TERMINAL` | compatible producer/consumer revisions; no downgrade | no authority mutation | `CLIENT_UPDATE_REQUIRED` | `recovery authoritative revision unsupported` |
| `RECOVERY_GRANT_SECURITY_EVIDENCE_STALE` | `DEPENDENCY_UNAVAILABLE` | `RETRYABLE` while grant/current state remains valid | refresh authenticated non-rollback evidence | no nonce/authority mutation | `TEMPORARILY_UNAVAILABLE` | `recovery security evidence unavailable, stale or superseded` |
| `RECOVERY_GRANT_REPLAYED` | `SESSION_REJECTED` | `SECURITY_TERMINAL` | reconcile prior recovery; never reuse nonce | prior success may exist; no duplicate | `SESSION_UNAVAILABLE` | `recovery grant already consumed or replayed` |
| `RECOVERY_HEALTHY_CONTROLLER_PRESENT` | `CONFLICT` | `TERMINAL` | incumbent remains authority | no nonce/authority mutation | `CHARACTER_ALREADY_ACTIVE` | `recovery blocked by current playable controller` |
| `RECOVERY_TARGET_NOT_ELIGIBLE` | `SESSION_REJECTED` | `TERMINAL` | resolve current actor/session state; new flow as permitted | no nonce/authority mutation | `SESSION_UNAVAILABLE` | `recovery target is not eligible` |

Correlation fields must be credential-free and may include safe attempt reference, session/world identifiers where policy permits, generation relation class, transition state class and source-age/order buckets; never raw proofs/nonces/private fencing values.

## 26. Required race/fault evidence for implementation

Future implementation acceptance MUST include independent/fault-injected evidence for at least:

### Reconnect

- stale/predecessor reconnect proof replay;
- two contenders after eligible loss -> one commit winner;
- healthy current generation + stolen reconnect proof -> incumbent not preempted;
- PREPARE then incumbent regains sufficient control -> COMMIT rejected;
- PREPARE then predecessor generation/session/lease/runtime owner changes -> candidate rejected;
- PREPARE expiry while grace still valid -> new PREPARE allowed only after fresh evaluation;
- same-session grace expiry -> old GameSession cannot revive;
- lost COMMIT response -> same attempt reconciles committed result without second switch;
- physically open stale socket after winner -> commands/liveness rejected by generation fence.

### Protection / liveness

- socket close without authoritative loss -> no epoch/protection;
- graceful logout/login -> no protection;
- one loss epoch + multiple reconnect retries -> protection activates once for exactly 4s;
- control restored, stable, later independently lost -> new epoch may receive its own one-time protection;
- no client/OS diagnostic can override server liveness classification.

### Recovery security

- malformed crypto/header/schema cases according to profile precedence;
- invalid signature + wrong binding/profile/schema -> authentication failure without oracle;
- correctly signed wrong binding -> binding mismatch;
- correctly signed unsupported independent revision -> revision unsupported;
- older allow/trust evidence cannot roll back newer deny/revoke while still <5s;
- cache refresh cannot re-age evidence;
- restart without provable anti-rollback floor cannot authorize;
- key/profile revoke or Platform-security change after PREPARE but before COMMIT -> fail before nonce/authority mutation.

### Ownership/world/actor

- non-owned CharacterId -> ownership failure before world/actor/controller classification;
- valid ownership + wrong/stale world -> no recovery/retarget;
- healthy controller conflict cannot be hidden as generic target-not-eligible;
- post-grace actor remains present -> new GameSession attaches without state reset;
- actor becomes ABSENT before commit -> recovery target rejected, no recreation.

### GameNode/failover

- old owner/process submits command/control/save after ownership-generation replacement -> rejected;
- new owner has complete fenced continuity evidence -> safe same-session continuation may proceed;
- new owner lacks required session/proof/reconciliation evidence -> same GameSession is not guessed/recreated;
- locator points to stale owner -> current owner fence wins;
- handoff/reconnect race -> stale source owner never revived.

## 27. Decision timing

| Decision | Now? | Blocks | Risk if wrong later | Superseding evidence | Deferred |
|---|---|---|---|---|---|
| one current transport generation per GameSession | `YES` | protocol/session/runtime reconnect | split command/liveness authority | formal/fault proof of equivalent fencing | physical socket/session data structures |
| healthy binding non-preemptible by bearer proof | `YES` | reconnect/recovery security | stolen proof can kick healthy player | reviewed current-generation-authorized migration design | healthy migration UX/protocol |
| PREPARE/COMMIT + COMMIT revalidation | `YES` | reconnect wire/runtime | lost-response/stale authorization ambiguity | proof of alternative linearizable protocol | persistence encoding/storage |
| reconnect proof rotation/fencing | `YES` | same-session security | predecessor proof resurrection | reviewed PoP/sender-constrained replacement | exact secret hash/storage mechanism |
| server-authoritative ControlLossEpoch | `YES` | 4s protection/abuse prevention | client/network manipulation manufactures safety | gameplay/liveness evidence preserving same invariant | internal epoch representation |
| exactly 4s PvE protection per eligible epoch | `YES`, already accepted | gameplay reconnect semantics | player-visible fairness/abuse contract | explicit owner gameplay supersession + evidence | implementation timer mechanism |
| exact liveness/grace/cleanup numbers | `NO` | implementation acceptance only | guessed timing creates false loss/abuse/availability issues | measured network/load/fault/UX evidence | exact cadence/threshold/grace/cleanup values |
| post-grace existing-actor recovery uses new GameSession | `YES` | actor/session recovery | reset/respawn exploit paths | proof of alternative preserving all gameplay state | physical session/actor storage |
| independent recovery revision dimensions | `YES` | recovery profile/rollout | opaque compatibility masks mixed state | coordinated version-contract supersession | physical revision registry |
| GameNode replacement requires fenced recoverable continuity evidence | `YES` | failover/recovery | guessed session resurrection/split authority | durable fault proof of equivalent continuity | checkpoint storage/RPO/RTO |

## 28. Acceptance boundary

FND-04B acceptance means only reconnect/recovery/continuity semantics are frozen.

It does not complete FND-04. FND-04C must still integrate complete errors/diagnostics, failure scenarios, compatibility/rollout evidence, programme status and the thin final FND-04 index.

No runtime implementation is authorized by this contract.
