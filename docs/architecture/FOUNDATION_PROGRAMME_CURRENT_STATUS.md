# Oteryn v2 Foundation Programme — Current Status

- Status: Canonical current execution-status overlay
- Date: 2026-08-10
- Coordination ID: `OTV2-NATIVE-FOUNDATION`
- Applies to: current foundation gate progression and next-action interpretation
- Current trusted main at FND-04C start: `3d07b3faaca683514fdfe6291e974f9195e2f763`
- Active final foundation delivery: Issue #130 (`FND-04C`)

## 1. Authority of this overlay

This document answers **what is accepted now and what may happen next**. Detailed historical review/CI/repair evidence lives in the accepted contracts, archived task records and merged PRs.

If an older coordination/backlog/register paragraph still describes FND-02, FND-03 or FND-04 as the current live gate, that wording is historical execution narrative. Accepted contracts plus this overlay govern current progression. Stable decision IDs and future dependency requirements in the global register/backlog remain valid unless explicitly superseded.

No status row below implies runtime implementation unless it explicitly says so.

## 2. Foundation progression summary

| Gate | Current status | Canonical evidence / note |
|---|---|---|
| `FND-01` | `ACCEPTED AND APPLIED` | workspace/dependency contract + canonical 19-member destination cutover; destination merge `78988f72a80cc904aa9176ae850c50d4efa0b0f0` |
| `VSL-02` | `ACCEPTED AND COMPLETE` | exact Rust-client migration/cutover contract; source-only historical/non-canonical closeout completed |
| `FND-ID-01` | `ACCEPTED` | `FND-ID-01_FOUNDATION_IDENTIFIER_CONTRACT.md`; merge `2c584543cd1e3758958755478a6cc6ed3d39a8a9` |
| `FND-02` | `ACCEPTED` | `protocol-oteryn` v1 contract; PR #94 merged as `769ecd2ce2dfe0a7644d8dc1d67c54d40da5d202`; runtime codec/listener implementation remains separately gated |
| `FND-03` | `ACCEPTED` | `FND-03_RUNTIME_EXECUTION_CONTRACT.md`; PR #102 merged as `e72f2514924e8bbf8d1a729721cce9e67d977544`; runtime implementation/capacity/OPS claims remain separately gated |
| `FND-04A` | `ACCEPTED AND LIFECYCLE-CLOSED` | fresh admission authority/profile; PR #125 merge `cae318b8891844891c734012eb2020e669ebaff4`; closeout #126 `2fd7bac4879f381d5b97230732076df2e9c61f95` |
| `FND-04B` | `ACCEPTED AND LIFECYCLE-CLOSED` | reconnect/recovery/continuity + recovery profile; PR #128 merge `e6282b9c48713b2a2980f2598a81775f78725cff`; closeout #129 `3d07b3faaca683514fdfe6291e974f9195e2f763` |
| `FND-04C` | `VALIDATING` until owning PR merges | final errors/diagnostics/failure/compatibility integration, thin FND-04 index and status transition; Issue #130 |
| `FND-04` overall | `INCOMPLETE UNTIL FND-04C + LIFECYCLE CLOSEOUT` | A/B are accepted; C is the only remaining semantic architecture gate in programme #112 |

## 3. Accepted FND-02 baseline

Canonical production protocol family is `oteryn`.

Accepted foundation includes:

- TCP + TLS 1.3;
- ALPN `oteryn-game/1`;
- verified server identity;
- no TLS 0-RTT/plaintext/Canary fallback;
- `uint32_be` bounded framing + protobuf binary/proto3 IDL;
- exact 16-byte wire form for exposed foundation UUID identities;
- GameSessionId issued only after authoritative game admission;
- monotonic non-zero post-admission `connection_generation` fencing;
- `(GameSessionId, CommandId)` command identity with monotonic uint64 CommandId total client order;
- server_sequence + typed state-domain revisions;
- explicit snapshot/delta/resync with no gap guessing;
- authenticated liveness probe/ack distinct from gameplay silence/socket-open;
- registered hard limits and stable protocol errors;
- independent byte fixtures/malformed corpus/property/fuzz/cross-version evidence required before implementation claims.

FND-02 `schema_revision` is diagnostic/build evidence, not an opaque exact gameplay compatibility token.

## 4. Accepted FND-03 baseline

Canonical runtime semantics include:

- multithreaded GameNode with many independent authoritative scopes;
- one logical ordered mutation owner per ChannelRuntime/InstanceRuntime;
- logical owner is not a dedicated OS thread;
- NodeId is process-incarnation/placement identity, not scope authority;
- scope ownership generation is separate from NodeId and semantic ChannelId/InstanceId;
- RuntimeExecutionOrdinal/order is distinct from CommandId order;
- wall clock, monotonic time and authoritative execution order are separate concepts;
- mutation-capable timers/async results re-enter through the current owner and stale generation/revision/local handles fail closed;
- control/fencing work cannot starve behind gameplay backlog;
- queues/executors are bounded;
- capacity values require measured evidence;
- deterministic replay records normalized authoritative inputs/clocks/randomness/order rather than CPU/thread interleaving.

No async runtime product, worker count, CPU affinity, global tick numeric capacity, orchestrator or heartbeat cadence is selected merely by FND-03 architecture acceptance.

## 5. Accepted FND-04A baseline

Fresh admission now canonically requires:

- Platform authenticates/authorizes one bounded attempt; Oteryn-v2 alone decides current game-domain admission;
- AccountId->CharacterId ownership/lifecycle is proven before CharacterId->WorldId/world eligibility, including final atomic revalidation;
- valid ownership + stale world -> `ADMISSION_GRANT_WORLD_STALE`, no candidate nonce/presence/lease/session/transport mutation and no retarget;
- AccountPresenceClaim, CharacterLease, GameSession, TransportBinding and RuntimeScopeAuthority remain distinct;
- one atomic final admission boundary creates all candidate authority or none;
- fresh JWS profile uses fully specified `Ed25519`, verifier-anchored trust selection and deterministic malformed/authentication/schema/binding/profile precedence;
- independent protocol/transport/ruleset/content/map/world-policy/offer revision bindings; no opaque `compatibility_revision`;
- Platform-security and signing-key/profile trust require authenticated source observation provenance, conservative source-age <=5s and monotonic anti-rollback ordering;
- cache refresh cannot re-age evidence; older allow/trust cannot roll back newer deny/revoke; equal revision contradiction fails closed; restart reconstructs current non-rollback floor or fails closed.

## 6. Accepted FND-04B baseline

Reconnect/recovery now canonically requires:

- one current playable `connection_generation` per GameSession;
- healthy current binding cannot be preempted by reconnect bearer proof or recovery JWT;
- PREPARE grants no gameplay/liveness/fencing authority;
- COMMIT revalidates current session/generation/grace/controller/presence/lease/runtime/reconciliation/security/revisions and atomically switches authority;
- inactive candidate successor reconnect proof may be delivered during PREPARE; COMMIT activates it and fences predecessor proof; lost-response reconciliation never creates a second transition;
- same-session grace begins exactly at server-authoritative `ControlLossEpoch`, not socket close/first missed probe/cleanup/reconnect attempt;
- original grace/protection/re-arm state and deadlines survive GameNode/runtime-owner replacement without restart;
- valid eligible re-entry activates exactly 4 seconds defensive PvE protection at most once per eligible protection entitlement;
- successful control restoration does not automatically re-arm protection; server-authoritative stable-control evidence is required before a later unexpected loss may receive a new entitlement;
- historical candidate `2s/5s/15s` liveness/reconnect/grace numbers are non-canonical;
- exact liveness/grace/cleanup/re-arm numeric values remain finite but deferred to measured implementation evidence;
- recovery uses separate purpose-bound `oteryn-reauth-recovery-v1` Ed25519 profile;
- recovery independently validates protocol/transport/ruleset/content/map/world-policy revisions; no opaque compatibility revision;
- AccountId->CharacterId ownership is proven before recovery world/actor/controller classification;
- same-session recovery preserves GameSessionId/CommandId/server_sequence/domain revisions and actor state;
- post-grace existing-actor recovery creates a new GameSessionId and never respawns/resets/teleports/heals the existing actor;
- GameNode replacement may preserve same-session continuity only with complete fenced recoverable continuity evidence; NodeId or restart never guesses authority;
- ordinary reconnect does not manufacture HandoffId.

## 7. FND-04C current acceptance target

FND-04C must merge, unchanged after final exact-head validation, with:

- complete FND-04 cross-component error catalogue conforming Foundation Error Vocabulary;
- stable redacted diagnostics + credential-free correlation per error;
- historical superseded error aliases explicitly non-canonical where A/B already own the condition;
- Foundation failure scenarios for admission/recovery/reconnect replay/races, lost responses, security/key rotation, ownership/world changes, GameNode continuity ambiguity and protection re-arm/failover;
- independent producer/consumer compatibility and rollout/rollback rules;
- implementation evidence gates;
- security/privacy integration;
- thin final `FND-04_IDENTITY_GAME_SESSION_ADMISSION_CHARACTER_LEASE_CONTRACT.md` linking A/B/C without duplicating them;
- this current-status transition.

After the FND-04C delivery merge, a separate lifecycle closeout must archive/release its active task. **Only then** is FND-04 marked `ACCEPTED AND CLOSED` and programme #112 may close.

## 8. Foundation decisions that remain deliberately deferred

FND-04 acceptance does not freeze implementation-sensitive numbers/products without evidence. Still deferred include:

- CharacterLease TTL/renew/safety/fail-safe deadlines;
- reconnect liveness probe cadence/hysteresis/control-loss threshold;
- same-session grace duration;
- stale-transport cleanup;
- stable-control protection re-arm threshold;
- prepared reconnect/resource/rate/retention limits;
- async runtime/worker/affinity choices;
- production channel/player capacity and automatic scaling;
- persistence schema/isolation/outbox/RPO/RTO;
- KMS/HSM/secret-management vendor;
- healthy-session migration protocol;
- handoff implementation details beyond accepted fencing extension points.

These are not permission to use defaults. Their owning DUR/OPS/PERF or future dedicated contract must accept measured evidence before implementation can claim correctness.

## 9. Runtime/implementation status

Foundation architecture acceptance is **not runtime implementation**.

Current architecture work does not authorize:

- production protocol listener/client gameplay adapter;
- GameNode/session/admission/reconnect runtime implementation;
- CharacterLease persistence/schema;
- Platform issuer/security projection writes;
- production signing keys/KMS/HSM;
- deployment/traffic cutover;
- entitlement/Premium/VIP implementation;
- broad gameplay/content production.

The migrated Rust client remains governed by ADR-0011 pre-native-protocol fail-closed requirements until separately authorized implementation proves FND-02/FND-03/FND-04 conformance.

## 10. Next ordered work after FND-04 closes

The foundation identity/protocol/runtime/admission architecture chain is no longer the blocker once FND-04C closeout completes.

The next Stage-B dependency work must respect the global register:

1. `ANL-01 — Game Event and Audit Foundation` must be accepted before `DUR-02`/`DUR-03` finalize transactional outbox and critical audit evidence.
2. `DUR-01 — Durable Identifier Representation Contract` remains required before authoritative durable gameplay representation.
3. `DUR-02 — Persistence v1` and `DUR-03 — Item Transaction and Anti-Duplication Invariants` remain hard gates before authoritative durable character/item/currency mutation and consume both DUR-01 and relevant ANL-01 decisions.
4. `DUR-04 — Content, World Detail and Scripting` remains required before broad import/scripted durable behavior.
5. `GAME-VISION-01` still blocks broad gameplay/content production and must define measurable reference-vs-evolved world launch/parity strategy.

ANL consumers remain observational and never replace authoritative invariants. In particular, DUR-03 prevents duplication; ANL-03 later detects/investigates economy integrity anomalies.

## 11. Concise current rule

```text
FND-01 / VSL-02 / FND-ID-01 / FND-02 / FND-03
-> accepted

FND-04A
-> accepted + closed

FND-04B
-> accepted + closed

FND-04C
-> final validation / integration gate

FND-04C delivery + lifecycle closeout
-> FND-04 ACCEPTED AND CLOSED
-> programme #112 closes

then
-> ANL-01 + DUR-01 dependency work
-> DUR-02 / DUR-03 only after their required inputs
-> no broad gameplay/content production before GAME-VISION-01
```
