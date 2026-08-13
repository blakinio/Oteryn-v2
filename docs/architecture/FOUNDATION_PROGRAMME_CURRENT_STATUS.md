# Oteryn v2 Foundation Programme — Current Status

- Status: Canonical current execution-status overlay
- Date: 2026-08-13
- Coordination ID: `OTV2-NATIVE-FOUNDATION`
- Applies to: accepted foundation progression and next ordered architecture gates
- FND-04 lifecycle closeout merge: `adb0882a5ddbe42944fe955f5effb78fd5495422`
- DUR-01 lifecycle closeout merge: `ef42fa47ab054ab8aa304c017307c1945f931b59`
- ANL-01 delivery merge: `af2fa495c1126080ffc1d0717b7d0ef54f6b29ca`
- Dual-transport architecture closeout merge: `05544969baf58c3a40354f366438d759bfd159e5`
- Platform entitlement producer-remediation merge: `blakinio/Oteryn-Platform@afaa6d1d8340e44b1152b62d6d27e5fd1649804a`
- DUR-04 delivery merge: `568236c33cd23da017bca1dbd1ed98afc8da71f4`
- SIM-DETERMINISM delivery merge: `1e16b32069868f14aa1761a512b6cd8b1024e277`
- Current phase: `foundation/game/content/determinism architecture accepted/lifecycle-closed where delivered + runtime largely NOT_STARTED; all executable runtime/DDL/production work still requires separate explicit owner authority; the one selected next paper-only programme action is the versioned Reference evidence/parity manifest under its owning contract`

## 1. Authority of this overlay

This document answers what is accepted now and what may happen next. Detailed review/CI/repair evidence lives in accepted contracts, archived task records and merged PRs.

Older backlog/register prose that describes completed FND/DUR/ANL/gameplay/SIM gates as live is historical execution narrative. Accepted contracts plus this overlay govern current progression. Stable decision IDs and future dependency requirements remain valid unless explicitly superseded.

`docs/architecture/ARCHITECTURE_REVIEW_REFINEMENTS_2026-08-10.md` adds owner-accepted programme ordering and product/operations refinements. `docs/architecture/ADR-0014-dual-gameplay-transport-tcp-default-quic-opt-in.md` accepts the long-term dual-transport strategy but explicitly preserves TCP transport profile `1` as the only currently registered gameplay transport profile. QUIC player admission remains blocked until `PROTOCOL_OTERYN_V1_REGISTRY.json` and both FND-04 fresh/recovery grant profiles are reconciled by a later accepted delivery. The application protocol and all security/sequencing/fencing semantics remain one `protocol-oteryn` contract.

`ARCHITECTURE_STATUS_MODEL.md` is normative for current status presentation. Every row below separates `DecisionStatus`, `DeliveryStatus` and `ImplementationStatus`; one axis never implies another. `PLANNED` means the gate is registered for future work but no active task/PR currently owns delivery; `OPEN` is reserved for a concrete active delivery or unresolved lifecycle record.

## 2. Foundation and Stage-B progression

| Gate | DecisionStatus | DeliveryStatus | ImplementationStatus | Canonical evidence / note |
|---|---|---|---|---|
| `FND-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `PROVEN` | applied 19-member workspace/dependency cutover proven by PR #50 exact final head `5092f868a42d545f47a98c0b9723210570cd9d45`, squash merge `78988f72a80cc904aa9176ae850c50d4efa0b0f0`; exact-head Agent Governance `31095853261`, Dependency Review `31095853437`, CodeQL `31095853606`, Rust workspace `31095853343` and adversarial migration audit `31095053578` all PASS |
| `VSL-02` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `PROVEN` | native-client cutover/migration proven by the same PR #50 exact final head `5092f868a42d545f47a98c0b9723210570cd9d45` and merge `78988f72a80cc904aa9176ae850c50d4efa0b0f0`; Linux/Windows build, tests, pre-native fail-closed, supply-chain and named exact-head checks recorded PASS in PR #50 |
| `FND-ID-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | semantic identity architecture is accepted; PR #147 merge `81db47966d76709a0e44dfbf1bc3979f38a24ffa` archived stale support records; no runtime identity implementation is claimed |
| `FND-02` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | `protocol-oteryn` v1 architecture accepted and task lifecycle archived; TCP profile `1` is registered architecturally, but gameplay protocol/transport runtime remains separately gated |
| `NET-TRANSPORT-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | final successor PR #149 exact head `641de04b1397cb910f6f26e7dd1594babb8ad1ac` passed exact-head self-review, Agent Governance, Dependency Review, CodeQL and required independent review; squash merge `05544969baf58c3a40354f366438d759bfd159e5`; no gameplay transport adapter/listener or player mode is runtime-available |
| `FND-03` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | authoritative runtime execution architecture accepted and task lifecycle archived; GameNode runtime implementation not claimed |
| `FND-04A/B/C` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | admission + reconnect/recovery + integration architecture accepted; runtime implementation separately gated |
| `FND-04` overall | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | programme #112 architecture lifecycle complete; no gameplay admission runtime claimed |
| `DUR-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | durable representation + ItemInstanceId accepted; physical PostgreSQL implementation is downstream |
| `ANL-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | event/audit foundation accepted; no runtime event collector/outbox/broker/warehouse implementation |
| `GAME-VISION-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | minimum product-vision baseline and immutable first Reference target accepted; target PR #181 final head `2a07643653d6d56a94ada89caf79005fce09e58a` passed self-review `4910439614`, Agent Governance `31532701302`, Dependency Review `31532701303`, CodeQL `31532701319`, squash merge `b57b382cb929b2c8a20d5c81197e933b0526764f`; no runtime authority |
| `GAME-CHANNEL-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | canonical `GAME-CHANNEL-01_CHANNEL_PRODUCT_POLICY_CONTRACT.md`; delivery #209 final head `ca1112191ede7d316c874189f3053ad7f8247579`, self-review `4918161329`, independent review evidence, Agent Governance `31611424137`, Dependency Review `31611424147`, CodeQL `31611424261`, merge `54dddbcfcb64baaf66e6cfd9fcd2cc3e1b4f04f1`; no runtime/client/Platform/DDL/production authority |
| `GAME-CHAR-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | Stage A + Stage B semantic architecture owner-accepted; PR #193 exact head `bc4942cab0e58b3aa4ed9713cc3f23b11b83aaa6`, self-review `4911343351`, Governance `31542939497`, Dependency `31542939533`, CodeQL `31542939487`, merge `08775e378db8c1fd6bb97bedf66bf08b3541f35f`; unresolved target rules remain hard parity gates |
| `GAME-ITEM-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | canonical `GAME-ITEM-01_ITEM_MODEL_AND_EQUIPMENT_CONTRACT.md`; delivery #205 final head `53d0189a114c99b4e7d44ca8d0db7a6bf5f3ea1a`, self-review `4915880173`, independent review evidence, Governance `31591336315`, Dependency `31591336312`, CodeQL `31591336340`, merge `5c502d24557621efc798def87b68f137ba23fad8`; no runtime/DDL/entitlement authority |
| `SIM-DETERMINISM-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | canonical `SIM-DETERMINISM-01_AUTHORITATIVE_SIMULATION_CONTRACT.md`; delivery PR #214 exact repaired final head `4c6684328123aebd657696808372a5855980d34e`; independent review `4924203877` found one replay-provenance P1 on superseded head `5dc628f32ca4573725bcb4a42c3a7702536d7f35`; owner-authorized repair cycle 4 restored server/build, protocol and exact World Bundle provenance; terminal self-review `4924321455` PASS, repeat self-review `4924423397` PASS, Governance `31676250271`, Dependency `31676250273`, CodeQL `31676250272` PASS; owner explicitly overrode the otherwise-required fresh independent-review-after-repair gate for exact final head and instructed finalization; squash merge `1e16b32069868f14aa1761a512b6cd8b1024e277`; no runtime/combat/AI/script/formula/dependency/DDL/production authority |
| `DUR-02` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | owner-accepted whole Persistence-v1 baseline in `DUR-02_PERSISTENCE_V1_OWNER_BASELINE.md`; PR #201 exact head `900be9f499981e638a6f8089fb46331b43ba321c`, self-review `4914253621`, independent review `5264011166`, Governance `31576235871`, Dependency `31576235909`, CodeQL `31576235921`, merge `ec4b840b0742967370a4235d87094b29a802fe28`; no DDL/migration/runtime authority |
| `DUR-03` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | canonical `DUR-03_ITEM_TRANSACTION_AND_ANTI_DUPLICATION_CONTRACT.md`; delivery #207 final head `a1d949362e219373a5d314c0e9ddf8de110362dd`, self-review `4916797999`, independent review evidence, Governance `31599369738`, Dependency `31599369737`, CodeQL `31599369780`, merge `63380bcba469027e90677aaf4db571fa941be2f4`; no runtime/DDL/production authority |
| `DUR-04` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | canonical `DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md`; delivery #212 final head `77e68ffb9e9e0e31ca751d42ff5f7c03466b2b23`, owner-directed self-review `4921665072`, Governance `31646998515`, Dependency `31646998564`, CodeQL `31646998517`, merge `568236c33cd23da017bca1dbd1ed98afc8da71f4`; no runtime/client/compiler/loader/Studio/DDL/content-import/production authority |
| `PROD-ENTITLEMENTS-01` | `PROPOSED` | `PLANNED` | `NOT_STARTED` | Platform producer security prerequisite #944 is satisfied by Oteryn-Platform merge `afaa6d1d8340e44b1152b62d6d27e5fd1649804a`; Oteryn-v2 consumer/enforcement contract remains unaccepted and Premium/VIP/game-consumed entitlement activation remains unauthorized |

The `ImplementationStatus` column describes only the scope of the named gate. `NOT_STARTED` does not mean adjacent repository code is absent; it means this overlay does not claim the gate's production/runtime behavior as implemented. `PROVEN` is used only where exact revision and named evidence are present in the row or directly named delivery record.

## 3. Accepted baseline preserved

FND-02 retains one `protocol-oteryn` application protocol, TLS/protobuf gameplay semantics, GameSession-scoped nonzero uint64 CommandId, server sequencing/revisions, reconciliation, bounded inputs and fail-closed compatibility/security behavior. TCP+TLS 1.3 transport profile `1` is architecturally registered; no gameplay transport adapter/listener is implemented or authorized. QUIC remains future profile/reconciliation/evidence work under ADR-0014 and matching FND-04 semantics.

FND-03 retains one logical authoritative mutation owner per channel/instance, separate ownership generation, owner-scoped RuntimeExecutionOrdinal, bounded queues, fail-closed stale work and measured capacity requirements. ADR-0009 remains binding that one `GameNode` is one game-server process. ADR-0015 leaves internal module/crate decomposition evidence-driven.

FND-04 remains accepted/lifecycle-closed with ownership-before-world admission, purpose-separated grants, anti-rollback evidence, PREPARE/COMMIT reconnect, healthy-binding non-preemption, ControlLossEpoch, exactly four seconds eligible defensive PvE re-entry protection and fail-closed recovery.

DUR-01 remains accepted/lifecycle-closed: UUIDv7 native durability uses PostgreSQL `uuid`, persisted CommandId preserves full uint64 via `numeric(20,0)`, ItemInstanceId is game-owned UUIDv7, legacy imports use stable source namespace identity, internal IDs are not automatically public.

`GAME-VISION-01` minimum product semantics and `GAME-VISION-01_FIRST_REFERENCE_BASELINE_OWNER_BASELINE.md` remain binding. The first Reference target is **Global Tibia production-observable behavior after the 2026-07-28 server-save/maintenance change boundary**. The target is immutable; later Global changes are candidate evidence for a later explicit Reference revision. Individual behaviors may remain `PROVEN`, `OBSERVED`, `DERIVED`, `UNKNOWN`, `CONFLICT` or `DECLARED_DIFFERENCE`; evidence gaps never become parity by convenience. Official public sources are primary but not assumed exhaustive; controlled black-box observation may provide evidence; community sources are corroborative/discovery; Canary/crystalserver/other OTS remain hypothesis/inventory inputs; search/patch-note absence is not proof of no change.

`GAME-CHAR-01` remains binding for baseline-neutral and Reference-sensitive Character semantics while exact unresolved arithmetic/content/profile behavior remains fail-closed. Formula-neutral authoritative progression facts do not silently become physical schema or numeric formula acceptance.

`DUR-02` remains binding for game-owned migrations, anomaly-proof transaction/locking/retry, ANL-compatible durable journal/publication substrate, durable-ack versus runtime-checkpoint/disaster-RPO separation, PITR/restore safety and expand/migrate/validate/cut-over/contract schema evolution. Acceptance grants no DDL/runtime authority.

`GAME-ITEM-01` remains binding for ItemType/ItemInstance/StaticItemPlacement semantics, typed capabilities, equipment/container legality and definition compatibility. It delegates exact item/value transaction/conservation/anti-duplication semantics to DUR-03.

`DUR-03` remains binding for one typed immediate durable item location, runtime↔durable value handoff, ItemInstanceId lifecycle transitions, exact conservation/provenance, retry/ambiguous-commit behavior, current lease/runtime fencing, custody, bounded audit and fail-closed restore reconciliation. Downstream trade/market/bank/depot/mail/reward/house/crafting/entitlement business policy remains separate.

`GAME-CHANNEL-01` remains binding for ChannelRef identity, selection/recommendation/queue/co-location, durable anti-hopping/prior-Channel state, source/reward multiplicity classes, qualitative create/drain/abort/retirement predicates, same-Channel recovery and one-World community/economy semantics. Numeric thresholds/windows/headroom/hysteresis remain PERF/OPS-owned.

`DUR-04` remains binding for stable semantic package/content identity, exact dependency locks, deterministic compilation, immutable bundle staging/activation/migration, client-safe/server-authoritative projection, bounded fail-closed loading, provenance/conversion and the target WebAssembly Component Model + project-owned WIT capability boundary. Scripts use snapshot-bound reads, proposal-only mutations, authority-scoped action plans and versioned deterministic execution profiles. Final physical serializer/container/chunk/compression/numeric limits/Wasmtime version remain separately evidenced.

`SIM-DETERMINISM-01_AUTHORITATIVE_SIMULATION_CONTRACT.md` is accepted/lifecycle-closed architecture. It freezes:

- reproducibility from canonical future-determining deterministic state + exact FND-03 owner-local normalized input order + exact semantic revision/profile set + normalized external facts;
- no global total order and no second runtime commit ordinal;
- versioned `SimulationDeterminismProfileRevision` for cross-cutting numeric/RNG/tie-break/hash/supported-target semantics;
- exact behavior-affecting revision binding for retryable/delayed occurrences;
- explicit numeric semantic classes, formula descriptors, rounding boundaries/modes and fail-closed invalid-state behavior;
- DUR-03 exact conservation remaining exact and non-floating;
- purpose-isolated deterministic gameplay RNG with retry/failover stability, authoritative advancement and anti-prediction protection;
- separation of wall clock, monotonic elapsed time and authoritative execution order; no global fixed tick;
- deterministic simultaneous/conflict policy and normalized external nondeterminism;
- replay envelopes retaining exact server/build, `protocol-oteryn`, World Bundle, semantic revision, input/order, formula/script profile, RNG and normalized external/time evidence;
- optional original NodeId/process-incarnation forensic attribution without making placement a replay prerequisite;
- canonical deterministic state/hash coverage of active revisions, gameplay state, RNG state, pending work, occurrence identities and semantically relevant fences/revisions;
- hierarchical divergence evidence that remains read-only;
- identical normalized authoritative outcomes across supported server targets;
- required replay/hash/RNG/formula/pending-state resource limits before implementation acceptance.

SIM acceptance does not choose numeric/RNG/hash crates, the exact gameplay RNG algorithm, exact fixed scales/formulas, global tick, scheduler/thread counts, replay backend or production hash cadence.

## 4. Accepted ANL-01 foundation

ANL-01 retains a protobuf semantic event foundation with distinct EventId/OperationId/TransactionId/CorrelationId identities, typed causation, purpose-scoped pseudonymous analytics identity, `BEST_EFFORT_TELEMETRY` versus `DURABLE_AUDIT`, stable semantic envelope/payload identity, owner-scoped runtime order references, complete transaction event-set references, no global event total order, atomic durable mutation evidence where required, at-least-once EventId-stable publication, typed/versioned event families, privacy/access/finite-retention policy and bounded event/replay/query/export resources. Game Intelligence remains observational/investigative and cannot autonomously mutate gameplay, ban, balance, rollback or deploy.

ANL-01 acceptance creates no event table, outbox implementation, broker, runtime collector, detector, warehouse or production collection.

## 5. Runtime/implementation status

Accepted FND/DUR/ANL/NET/GAME/SIM architecture does **not** itself authorize:

- TCP or QUIC gameplay adapter/listener implementation or any functional gameplay transport client mode;
- QUIC profile/admission/recovery/library/0-RTT/DATAGRAM activation;
- runtime event collector, database table/outbox/checkpoint/migration implementation or PostgreSQL DDL/migration execution;
- Character schema/progression/death/offline-training runtime implementation;
- unresolved `UNKNOWN/CONFLICT` Character/item/gameplay behavior as Reference behavior;
- item/currency transaction runtime, ground↔durable handoff or anti-duplication runtime;
- Channel directory/recommendation/queue/switch-guard/dynamic-scaling runtime/Platform implementation;
- compiler/loader/Studio/WIT host/scripting runtime, final physical world/bundle encoding, broad content import or live content activation;
- authoritative SIM kernel/RNG/state-hash/replay implementation, numeric/RNG/hash dependency adoption, combat/AI/progression/script implementation or exact gameplay/Reference/balance formula activation merely because SIM is accepted;
- broker/stream/warehouse/lake/dashboard selection/deployment;
- balance/security detector implementation or investigation/AI write authority;
- Platform migrations/writes;
- production analytics collection, gameplay runtime/deployment/traffic activation or Premium/VIP/game-consumed entitlement activation.

The native client therefore remains legitimately pre-native-protocol until separately authorized implementation proves the transport/session/runtime path.

## 6. Next ordered architecture and proof work

Whole DUR-02, GAME-ITEM, DUR-03, GAME-CHANNEL, DUR-04 and SIM-DETERMINISM architecture are accepted/lifecycle-closed while implementation remains `NOT_STARTED`. A separately authorized implementation programme may consume accepted common scopes, but architecture acceptance does not grant implementation authority.

The remaining named pre-VSL paper-only programme action is now:

1. **Build the versioned Reference evidence/parity manifest under its owning contract.** Preserve the accepted first Reference target and evidence hierarchy; record provenance/status per exercised mechanic; unresolved Reference-sensitive rules remain fail-closed until evidenced or explicitly `DECLARED_DIFFERENCE`. Do not invent a new stable gate ID unless explicitly registered.
2. Obtain explicit implementation authority before any bounded server/persistence/Channel/DUR/content/SIM executable increment. A safe decomposition remains GameNode/bootstrap shell -> `protocol-oteryn` transport/runtime adapter -> admission/GameSession/CharacterLease -> PostgreSQL migration/persistence substrate -> Character/FND-04 persistence -> minimal ChannelRuntime, then bounded movement/combat/item/content slices under their owning contracts.
3. `NET-TRANSPORT-02` or equivalent remains later evidence work for QUIC profile/FND-04 reconciliation.
4. Expand `VSL-01` only through real-boundary slices after each owning architecture/implementation gate is ready: admission, movement, combat, persistence, recovery, multichannel.
5. Establish minimal admin/security/SRE readiness before external alpha.

`PROD-ENTITLEMENTS-01` remains independently deferred. Its Platform producer prerequisite is satisfied, but game-consumed Premium/VIP/commerce behavior still requires its own Oteryn-v2 consumer/enforcement contract and rollout proof.

## 7. Vertical-slice execution rule

```text
VSL-ADMISSION-01
-> VSL-MOVE-01
-> VSL-COMBAT-01
-> VSL-PERSISTENCE-01
-> VSL-RECOVERY-01
-> VSL-MULTICHANNEL-01
```

Each slice must cross the real boundaries it claims. A mock that bypasses Gateway, transport, GameNode authority or PostgreSQL cannot be terminal proof for that boundary.

## 8. Concise current rule

```text
accepted foundation/game/content/SIM architecture
!= implemented runtime
!= proven production system

GAME-VISION-01 / GAME-CHANNEL-01 / GAME-CHAR-01 / GAME-ITEM-01
DUR-01 / DUR-02 / DUR-03 / DUR-04
ANL-01 / SIM-DETERMINISM-01
-> ACCEPTED / LIFECYCLE_CLOSED / implementation mostly NOT_STARTED

SIM-DETERMINISM-01
-> deterministic arithmetic/RNG/order/replay/state-hash architecture accepted
-> exact formulas/libraries/runtime NOT_AUTHORIZED

next paper-only programme action
-> versioned Reference evidence/parity manifest
-> no invented stable gate ID

server/persistence/channel/content/SIM implementation
-> explicit owner implementation authorization still REQUIRED

PROD-ENTITLEMENTS-01
-> Platform producer prerequisite SATISFIED
-> Oteryn-v2 consumer contract NOT_ACCEPTED
-> Premium/VIP activation NOT_AUTHORIZED

runtime / production activation
-> still separately unauthorized
```
