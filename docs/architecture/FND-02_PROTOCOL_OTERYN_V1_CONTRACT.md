# FND-02 — `protocol-oteryn` v1 Foundation Contract

- Status: Accepted architecture contract when merged to `main`
- Date: 2026-08-08
- Gate: `FND-02`
- Decision authority: Oteryn-v2 architecture coordinator under owner-authorized execution
- Coordination ID: `OTV2-NATIVE-FOUNDATION`
- Applies to: native Rust client/server gameplay transport and wire foundation
- Canonical machine-readable companions:
  - `docs/contracts/protocol-oteryn/v1/foundation.proto`
  - `docs/contracts/PROTOCOL_OTERYN_V1_REGISTRY.json`
  - `docs/contracts/RESOURCE_LIMITS_REGISTRY.json`
- Reconciliation input:
  - `docs/architecture/FND-02_PLATFORM_PROTOCOL_RECONCILIATION_OWNER_BASELINE.md`
  - `docs/contracts/CROSS_REPOSITORY_CONTRACT_LOCK.json`
- Does not authorize: runtime implementation, production listener/advertisement, Platform writes, persistence schema, FND-03 runtime, FND-04 admission/lease implementation or gameplay-specific payload implementation

## 1. Purpose

`FND-02` freezes the smallest complete native gameplay wire contract needed to let later client/server implementation proceed without guessing protocol identity, security, framing, command ordering, reconnect continuity, reconciliation or hard input limits.

It deliberately does **not** design every gameplay packet. Movement, combat, items, chat, quests, content and later systems register their own typed command/state payloads against this foundation under their owning gates.

The protocol remains:

```text
one product-owned family
    protocol-oteryn

not:
    protocol-canary compatibility
    a Canary translation layer
    one protocol per ruleset
    one protocol per client profile
```

ADR-0008 remains binding: no Canary opcode, parser, fallback, listener sniffing or translation path is part of production `protocol-oteryn`.

## 2. Decision timing

- **Must decide now?** `YES`.
- **Concrete downstream work blocked:** `FND-03`, `FND-04` wire integration, the production `protocol-oteryn` crate/client adapter, `QA-E2E-01` wire fixtures and the first native vertical slice cannot be implemented safely without one stable framing/version/order/reconciliation contract.
- **What becomes harder later:** changing transport framing, command identity/order or snapshot semantics after deployed clients exist creates upgrade, rollback and compatibility cost. Therefore only those foundation mechanics are frozen now.
- **Evidence that may justify supersession:** production measurements showing unacceptable TCP head-of-line behavior, material parser/runtime security findings, a protobuf ecosystem failure, measured wire overhead that materially harms gameplay, or a new product requirement impossible to add safely through the registered extension model.
- **Deliberately undecided:** concrete Rust protobuf library, TLS library, socket/runtime implementation, heartbeat cadence, lease/reconnect credential construction, gameplay message schemas, compression, QUIC, persistence representation and operational queue sizing beyond externally controlled protocol limits.

## 3. Reconciliation with the historical Platform contract

The pinned Platform contract at `blakinio/Oteryn-Platform@c0b8703d326a04b43ae8e06f6192b0cb91c859b7` remains useful evidence but is not Oteryn-v2 protocol authority.

### Preserved requirements

FND-02 preserves these security/ownership requirements:

- Platform Identity remains the reusable-credential authority.
- Gateway/World Registry select an offered endpoint/protocol route; the gameplay server does not silently invent another route.
- admission material is opaque to the client and exact route/security context is validated server-side.
- after route/credential issuance there is no same-credential downgrade or fallback to Canary.
- protocol, transport, optional capability, content and ruleset versions are separate concepts.
- parsing is bounded and fails closed.
- server state/results are authoritative.
- commands are idempotent/retry-safe.
- snapshots/deltas have explicit revision reconciliation.
- secrets and credentials are redacted from protocol diagnostics.

### Explicitly superseded assumptions

The following historical Platform choices are **not** carried forward as Oteryn-v2 authority:

- Otheryn C++ is not the target runtime.
- a production `protocol-canary` client/server path is not part of Oteryn-v2.
- exact schema revision/hash equality is not a runtime compatibility lock.
- a fixed capability digest is not protocol identity.
- `CommandId` is not UUIDv4 plus a second independent sequence.
- the historical Game Session claim set does not issue canonical game-domain `GameSessionId`.
- schema revision `2` and its historical schema hash are not FND-02 schema identity.

The old fixed choices that are retained below—TCP, TLS 1.3, big-endian length framing and protobuf binary—are retained because this FND-02 analysis independently selects them for the native Rust design, not because the historical contract already used them.

## 4. Protocol identity and version dimensions

The accepted native identity is:

| Dimension | FND-02 v1 |
|---|---|
| family | `oteryn` |
| protocol major | `1` |
| transport profile | `1 = tcp_tls13_alpn_v1` |
| ALPN | `oteryn-game/1` |
| framing | `uint32_be length` + exactly one protobuf `WireEnvelope` |
| serialization | Protocol Buffers binary |
| source IDL syntax | `proto3` |
| foundation schema revision | `1` |
| application compression | `none` |

The following are **not** aliases for protocol-major compatibility:

- schema source SHA-256;
- client/server build revision;
- content revision;
- ruleset revision;
- world policy revision;
- optional capability set.

### Schema revision versus compatibility

`schema_revision` is build/evidence/diagnostic metadata. It is not an exact-equality production handshake gate.

Two peers under `protocol_major = 1` may interoperate with different schema revisions only when:

- every used field/type is wire-compatible;
- required core v1 semantics are unchanged;
- any additive semantic extension is capability-gated when older peers cannot safely ignore it;
- golden and cross-version fixtures prove compatibility.

Breaking wire or semantic changes require a new protocol major.

The SHA-256 recorded for `foundation.proto` is an immutable evidence fingerprint of that source artifact. It is **not** a runtime protocol credential and is **not** used to infer semantic message equality.

## 5. Transport and TLS

### 5.1 Selected transport

Native v1 uses one separately advertised **TCP** gameplay endpoint protected by **TLS 1.3**.

TLS 1.3 is interpreted against current RFC 9846. Server service identity verification follows RFC 9525.

Required behavior:

- TLS 1.3 only for this transport profile;
- ALPN exactly `oteryn-game/1`;
- normal trusted certificate-chain and reference-identifier verification;
- no plaintext mode;
- no protocol-family sniffing;
- no Canary fallback on the same listener;
- no application-layer encryption or MAC layered on top of TLS;
- TLS 0-RTT/early data is forbidden;
- TLS resumption, if later enabled, is only a transport optimization and never restores gameplay authority by itself.

A failed TLS/ALPN/identity check is terminal for that connection. A different route requires a fresh authorized Gateway flow; the same gameplay credential is never rebound to a silently downgraded endpoint.

### 5.2 Why TCP rather than QUIC for v1

TCP+TLS is selected because the first native gameplay contract already requires a predominantly ordered authoritative stream, Tokio networking support exists in the canonical Rust workspace, and TCP minimizes new operational and protocol complexity for the first vertical slice.

QUIC is deliberately deferred, not rejected forever. It may become a later transport profile only if measured latency/head-of-line/roaming requirements justify the complexity and the same authoritative semantics can be preserved.

### 5.3 Transport state is not gameplay liveness truth

An open TCP socket is not sufficient proof that the player retains usable control.

The protocol provides authenticated liveness probe/ack primitives, but `FND-03`/`FND-04` own the final cadence, timeout/hysteresis and server-overload discrimination needed to satisfy the accepted disconnect-protection policy.

## 6. Framing

Every post-TLS application frame is:

```text
uint32_be payload_length
payload_length bytes containing exactly one protobuf WireEnvelope
```

Rules:

1. the four-byte prefix is not included in `payload_length`;
2. zero-length frames are invalid;
3. the wire-frame hard maximum is registered as `1,048,576` bytes;
4. the length is checked **before** peer-controlled allocation/read reservation;
5. truncated, overlong, trailing/multiple-envelope or malformed input fails closed;
6. one frame contains one envelope and one envelope contains one registered typed payload;
7. application compression is forbidden in v1.

A future compression extension requires a dedicated contract amendment and explicit compressed-size, decompressed-size, expansion-ratio and CPU/work bounds before implementation acceptance.

## 7. Serialization and IDL

### 7.1 Protobuf binary is selected

FND-02 selects **Protocol Buffers binary** for foundation and later typed payload schemas.

Reasons:

- mature, well-understood binary evolution rules;
- cross-language tooling useful for Platform/test/diagnostic consumers;
- explicit stable numeric field tags;
- good fuzz/property/golden-fixture support;
- unknown additive fields can be ignored safely when semantics permit;
- less custom parser/security surface than inventing an Oteryn-specific binary serialization format;
- no current need for FlatBuffers/Cap'n Proto-style in-place/zero-copy object access to justify their additional schema/runtime constraints.

### 7.2 `proto3` source syntax for v1

The canonical v1 source IDL uses `syntax = "proto3"`.

This is a deliberate toolchain-compatibility choice, not a claim that Editions are architecturally inferior. Current Rust protobuf ecosystems do not have uniform Editions support. A later source-IDL migration to a Protobuf Edition is allowed under the same protocol major only when generated wire behavior remains compatible and cross-version/golden evidence proves no semantic break.

FND-02 does **not** select or pin a Rust protobuf crate. The implementation package must separately evaluate a compliant runtime/codegen path, maintenance/security posture and build reproducibility.

### 7.3 Protobuf evolution rules

For all protocol schemas:

- field numbers are never reused;
- deleted field numbers/names are reserved;
- existing field meaning is not silently changed;
- unknown fields never activate behavior;
- required semantic presence is validated after decode rather than inferred from default zero values;
- zero `UNSPECIFIED`/invalid identifiers are rejected where a concrete value is required;
- externally controlled strings/bytes/repeated fields are bounded by named registry limits;
- parsing limits apply before expensive domain work.

Serialized protobuf bytes are **not canonical semantic identity**. They must not be used as the definition of command equality, state identity or a security authorization decision.

## 8. Envelope and registry model

`WireEnvelope` is intentionally small:

```text
message_type
connection_generation
server_sequence
payload
```

The machine-readable registry maps every `message_type` to:

- canonical name;
- direction;
- allowed phase;
- sequencing class.

`message_type = 0` is invalid. Registered numeric IDs are never reused after merge.

The foundation envelope does not contain a giant gameplay `oneof`. Later owning contracts register typed command/state payloads and place their protobuf bytes inside the appropriate foundation carrier (`ClientCommand`, `CommandResult`, `StateDelta`, `StateDomainSnapshot`).

This preserves compile-time typed payload schemas without turning one central foundation message into a high-churn mega-schema.

## 9. Optional capability extension model

Core protocol-v1 semantics are **not optional capabilities**.

In particular, these are mandatory implications of `protocol_major = 1`:

- server-authoritative command results;
- CommandId ordering/idempotency;
- server sequencing;
- state revisions;
- snapshot/delta/resync;
- current transport-generation fencing;
- liveness probe/ack support;
- no Canary fallback.

The v1 registry initially contains **zero optional capability IDs**. This is intentional; FND-02 does not invent speculative extensions.

Future additive features may register numeric capability IDs when:

- an older same-major peer can safely continue without the feature;
- the feature does not weaken a core v1 invariant;
- sender behavior is enabled only after the capability is selected;
- required capabilities are bound to the authorized route/session context by the owning FND-04/Platform contract.

Capability lists are sorted, unique and bounded. Duplicate, unsorted or unsupported required capabilities fail closed.

There is no canonical capability digest and no exact full-list equality requirement.

## 10. Wire identifier representation

### 10.1 Foundation UUID identities

When a canonical FND-ID UUID identity appears on this wire, it is encoded as exactly **16 bytes** in standard UUID network byte order and validated by the receiving semantic wrapper.

All-zero/nil is invalid.

This applies to the IDs used directly by this foundation:

- `CharacterId`;
- `WorldId`;
- `ChannelId`;
- `GameSessionId`.

Other FND-ID identities are added to later payloads only when their owning contract demonstrates a client-visible need.

Wire bytes do not replace strong Rust semantic types. Decoders convert them to typed domain wrappers before domain use.

### 10.2 Identity is not authority

Possessing `GameSessionId`, `CharacterId`, route IDs or any other identifier never grants gameplay authority.

FND-04 owns credential proof, admission, lease/session state and reconnect eligibility. FND-02 only defines the safe wire slots required to transport the result of those decisions.

## 11. Bootstrap and admission boundary

### 11.1 New admission

After TLS/ALPN succeeds, the client sends `ClientBootstrap` containing:

- protocol major;
- transport profile ID;
- diagnostic schema revision;
- supported optional capability IDs;
- bounded opaque admission material;
- selected `CharacterId`;
- bounded client build ID.

The bootstrap does **not** contain a client-created canonical `GameSessionId`.

FND-04 later defines exact admission-material construction and validation. Until authoritative admission succeeds:

- no playable map/entity state is exposed;
- `connection_generation = 0` is the only allowed envelope value;
- gameplay commands are rejected.

After admission succeeds, `ServerAccepted` returns the game-issued `GameSessionId`, authoritative `WorldId`/`ChannelId`, current non-zero `connection_generation`, current server sequence boundary and `next_command_id`.

### 11.2 Resume

`ClientResume` carries:

- existing `GameSessionId`;
- opaque reconnect material;
- the last fully applied authoritative server sequence;
- protocol/transport/schema support evidence;
- optional capability support;
- client build ID.

FND-04 decides whether the logical session is still eligible for resume.

If accepted:

- the same `GameSessionId` is preserved;
- a strictly newer non-zero `connection_generation` is returned;
- the server returns its current `server_sequence` and authoritative `next_command_id`;
- the protocol performs replay or replacement snapshot reconciliation.

A reconnect cannot resurrect a terminally ended GameSession.

## 12. Connection-generation fencing

`connection_generation` is an unsigned 64-bit fencing value scoped to one `GameSessionId`.

Rules:

- zero is pre-admission only;
- successful initial admission establishes the first non-zero generation;
- every accepted transport rebind uses a strictly larger generation;
- generation never wraps/reuses; exhaustion is session-terminal;
- every post-admission client frame must carry the current generation;
- a frame from an older generation cannot submit a command, recover liveness or alter reconciliation state;
- detection of `STALE_CONNECTION_GENERATION` is transport-fatal for the stale connection but does not terminate a newer authoritative connection for the same logical session.

This freezes the wire representation while preserving FND-04 ownership of the actual admission/reconnect state machine.

## 13. `CommandId`: one scoped identity and order

FND-02 intentionally does **not** copy the historical `UUIDv4 CommandId + separate client_sequence` pair.

The accepted command identity is:

```text
CommandRef = (GameSessionId, CommandId)

CommandId:
    uint64
    starts at 1
    strictly increases by exactly 1
    scoped to one logical GameSessionId
    survives eligible reconnect of that same GameSessionId
```

Within a GameSession, `CommandId` is both the operation identity and total client-command order.

This is not a durable entity ID and is not a credential.

### 13.1 Processing rules

Let `next_command_id` be the server-authoritative next value.

- `command_id == next_command_id`:
  - the command may be validated/executed;
  - after a terminal accepted/rejected result is committed, the server advances `next_command_id` exactly once.
- `command_id < next_command_id`:
  - it is a retry/duplicate/stale command;
  - it is **never executed again**;
  - if the original terminal result is still retained, return it as `DUPLICATE_REPLAY`;
  - if the result is no longer retained, return `DUPLICATE_OUTCOME_EXPIRED` and reconcile state as needed.
- `command_id > next_command_id`:
  - reject without domain mutation as `COMMAND_SEQUENCE_GAP`;
  - return the expected ID and require bounded reconciliation before new commands continue.

The client may pipeline only a bounded contiguous range. The maximum outstanding count is in the resource registry.

### 13.2 Why this is safe without an unbounded UUID cache

Safety does not depend on remembering every historical command payload or random ID forever.

The monotonic high-water mark proves that any lower CommandId has already had its one allowed processing opportunity. Evicting an old result may remove the convenience of exact-result replay, but it never permits command re-execution.

A duplicate's new payload bytes are not reinterpreted. Therefore protobuf non-canonical serialization cannot turn duplicate detection into a hash/equality bug.

### 13.3 New session

A new terminally admitted `GameSessionId` receives a fresh command namespace beginning at `1`.

No command from a prior GameSession can become valid merely because it has the same numeric CommandId.

## 14. Server-authoritative sequence

The server maintains one unsigned 64-bit `server_sequence` per logical GameSession.

It starts at `1` for the first authoritative post-admission sequenced message and increases by exactly one.

Messages classified `SERVER_SEQUENCE` in the registry include authoritative command results and state deltas. Liveness and snapshot transfer-control frames are deliberately unsequenced.

Rules:

- the client applies only the next expected authoritative sequence;
- `server_sequence <= last_applied_server_sequence` is already represented and is not applied again;
- a gap suspends new affected-state application and causes one bounded resync request;
- the client never guesses/skips a missing authoritative sequence;
- sequence never wraps/reuses; exhaustion is session-terminal;
- the sequence continues across an eligible reconnect that preserves `GameSessionId`.

FND-03 owns runtime publication/queue mechanics. FND-02 owns the visible ordering contract.

## 15. State revisions

State synchronization uses explicit typed domain revisions:

```text
StateRevision {
    domain_id
    revision
}
```

Rules:

- `domain_id = 0` is invalid;
- each registered state domain owns one monotonic `uint64` revision stream for this client-visible contract;
- revisions never wrap/reuse within their scope;
- a delta names `base_revision` and `new_revision`;
- `new_revision` must be greater than `base_revision` under the domain contract;
- a client applies a delta only when its current domain revision equals `base_revision`;
- mismatch causes resync, never speculative application.

FND-02 defines the mechanism. Movement/combat/inventory/etc. gates later register the actual domains and typed snapshot/delta payload schemas.

## 16. Snapshot, delta and resync

### 16.1 Initial state

After admission, the server establishes an initial authoritative state boundary through the snapshot protocol before gameplay commands are accepted for the new session.

The exact set of state domains is owned by the vertical-slice/gameplay contracts, not FND-02.

### 16.2 Snapshot transfer

A logical `SnapshotBody` is encoded once as protobuf bytes and transferred as:

```text
SnapshotBegin
SnapshotChunk[0..N-1]
SnapshotCommit
```

`SnapshotBegin` declares:

- non-zero session-scoped monotonic `snapshot_id`;
- exact chunk count;
- exact total encoded `SnapshotBody` byte length;
- `target_server_sequence`.

Rules:

- every chunk has the same snapshot ID;
- chunk indexes are zero-based and unique;
- declared count/size and cumulative bytes are validated with checked arithmetic before allocation;
- duplicate conflicting chunks, mixed IDs, gaps, overflow or hard-limit excess discard the assembly;
- application is atomic only after all chunks are present, the total size matches and `SnapshotCommit` matches;
- protobuf decoding occurs only after the full bounded body is assembled;
- after successful atomic apply, `last_applied_server_sequence = target_server_sequence`;
- authoritative messages newer than the target sequence are applied only afterward.

TLS already supplies transport integrity; v1 does not add an application checksum/MAC.

### 16.3 Resync

`ResyncRequest` carries the client's last applied server sequence and bounded per-domain revisions.

The authoritative server chooses one of two outcomes:

1. replay a contiguous retained authoritative sequence; or
2. send a replacement snapshot.

If replay is unavailable, the server must snapshot. It never fabricates a missing delta or instructs the client to skip unknown state.

Resync requests are idempotent control operations and do not consume CommandIds.

## 17. Liveness primitives

`LivenessProbe`/`LivenessAck` are authenticated application-protocol control messages.

Properties:

- probe IDs are non-zero `uint64`, monotonic within one `connection_generation`;
- they do not consume CommandId or server_sequence;
- an idle healthy client must still process/respond to liveness traffic;
- gameplay-command silence is not liveness-loss evidence;
- receipt time at the authoritative server, current connection generation and server-local health evidence are authoritative;
- client timestamps or `I am lagging/disconnected` assertions are not authority;
- stale-generation acknowledgements are ignored/rejected and cannot recover authority.

The final probe cadence, grace/hysteresis and relationship to the accepted 2.0-second PvE protection boundary remain FND-03/FND-04 policy because local server stalls and network jitter must be distinguished safely.

## 18. Error model

FND-02 stable numeric error codes are registered in `PROTOCOL_OTERYN_V1_REGISTRY.json`.

Each code maps to one existing foundation category and one default disposition:

- `OPERATION_TERMINAL`;
- `RESYNC_REQUIRED`;
- `SESSION_FATAL`;
- `TRANSPORT_FATAL`.

The public wire does not send stack traces, internal exceptions, SQL details, tokens or arbitrary server diagnostic text.

`ProtocolError` may carry only stable safe correlation values such as related/expected CommandId or expected server sequence.

Important distinctions:

- a stale old transport may be closed without killing the newer GameSession binding;
- a rejected command is not proof that the session is invalid;
- a malformed/oversize frame is transport-fatal;
- revision/sequence gaps cause bounded resync, not speculative continuation;
- credential/admission-specific errors remain FND-04-owned codes mapped through the shared foundation vocabulary.

## 19. Hard resource limits

The exact FND-02 externally controlled wire limits live in `RESOURCE_LIMITS_REGISTRY.json`.

The contract currently freezes at least:

| Resource | Hard maximum |
|---|---:|
| encoded WireEnvelope frame | 1 MiB |
| bootstrap/resume payload | 64 KiB |
| admission material | 16 KiB |
| reconnect material | 16 KiB |
| client build ID | 128 UTF-8 bytes |
| capability IDs | 128 |
| ordinary repeated collection | 4096 |
| protobuf nesting | 32 levels |
| command expected revisions | 64 |
| command payload | 64 KiB |
| command-result payload | 64 KiB |
| outstanding commands / GameSession | 64 |
| state domains / sync unit | 256 |
| state-delta payload | 256 KiB |
| snapshot chunks | 256 |
| snapshot chunk bytes | 512 KiB |
| assembled SnapshotBody | 16 MiB |

Named downstream message types may define smaller limits. They may not silently exceed the FND-02 hard parent limit.

Every receive path validates length/count/depth **before** unsafe peer-sized allocation or expensive decode/domain work.

## 20. Privacy and logging

Protocol observability must support safe reconstruction without leaking credentials.

Never log at ordinary levels:

- raw admission/reconnect material;
- OAuth/ticket/session bearer material;
- full private chat payloads;
- unrestricted serialized frames;
- secrets or authentication headers.

Permitted correlation under access/retention rules may include:

- protocol major/transport profile/schema revision;
- safe build ID;
- `GameSessionId` only where the relevant diagnostics/privacy contract permits it;
- connection generation;
- CommandId;
- server sequence;
- domain revision;
- stable protocol error code;
- World/Channel/Node context where appropriate.

High-cardinality identities do not become ordinary Prometheus labels.

## 21. Failure-scenario obligations

FND-02 directly defines the wire behavior required for:

| Foundation scenario | FND-02 requirement |
|---|---|
| `FS-DUPLICATE-COMMAND` | lower CommandId is never re-executed; cached result replay or outcome-expired/resync |
| `FS-REVISION-MISMATCH` | delta/command revision mismatch cannot mutate guessed state; resync |
| `FS-SNAPSHOT-DELTA-MISMATCH` | invalid snapshot/delta chain discarded; replacement snapshot/replay |
| `FS-SLOW-CLIENT` | wire/input bounds exist; FND-03 later owns bounded egress queue/drop/disconnect policy |
| `FS-QUEUE-SATURATION` | 64 outstanding client commands is the protocol ingress hard bound; broader runtime backpressure belongs FND-03 |
| `FS-STALE-GENERATION` | old transport generation cannot command or restore liveness |
| `FS-DUPLICATE-LOGIN` | protocol preserves GameSession/generation fencing; FND-04 owns admission/takeover decision |
| `FS-GATEWAY-AFTER-REDEEM` | no fallback/reuse assumption; FND-04 owns credential state/recovery |
| `FS-KEY-ROTATION` | transport/admission credentials are not protocol IDs; FND-04 owns key-roll behavior |
| `FS-CLOCK-SKEW` | command/order/revision correctness uses counters, not client wall clock |

Passing this architecture contract does not claim the runtime scenarios are implemented. It defines the assertions later implementation/E2E must prove.

## 22. Independent compatibility and security evidence

Implementation acceptance for FND-02 requires more than “client and server using the same codec can talk.”

Required evidence includes:

1. canonical byte-level golden fixtures for every foundation message and framing boundary;
2. a tiny independent raw-byte fixture verifier/parser sufficient to validate framing and selected canonical fields without reusing the production codec path;
3. malformed/adversarial corpus covering length, truncation, unknown IDs, illegal phases/directions, invalid UUID lengths, zero sentinels, count/depth overflow and sequence/revision gaps;
4. property tests for encode/decode semantic round trips and boundedness invariants;
5. fuzzing of frame and protobuf ingress decoders;
6. cross-version fixtures proving permitted same-major additive evolution;
7. tests proving deleted protobuf tags are reserved and never reused;
8. tests proving schema source SHA differences do not themselves force incompatible same-major peers;
9. tests proving raw protobuf byte differences do not define command identity/equality;
10. reconnect tests proving stale transport generations cannot regain authority.

Shared generated schemas/codecs remain useful; they are simply not the only oracle.

## 23. Rollout and cross-repository coordination

FND-02 acceptance in Oteryn-v2 does not mutate Platform.

After this local contract is merged:

- `CROSS_REPOSITORY_CONTRACT_LOCK.json` records the exact merged Oteryn-v2 FND-02 commit/schema revision/hash as locally accepted evidence;
- the historical Platform rev2 contract remains `RECONCILIATION_INPUT_ONLY`;
- a separately authorized Platform task must later reconcile Gateway/World Registry/session-offer structures with the accepted FND-02 dimensions;
- Platform advertisement remains disabled until its own implementation/validation/rollout gates pass;
- client/server production implementation remains separately gated by FND-03/FND-04 and implementation tasks.

No mutable PR head is written into the contract lock as canonical evidence.

## 24. Rejected alternatives

### Custom Oteryn binary format for gameplay wire

Rejected for v1. It adds bespoke parser/evolution/tooling/security burden without a demonstrated gameplay benefit.

### FlatBuffers or Cap'n Proto as the foundation serializer

Deferred/rejected for v1. Their strengths do not currently justify a less familiar schema/runtime path for the first native vertical slice. Reconsider only with measured CPU/allocation/latency evidence.

### Protobuf Editions 2024 as mandatory source syntax today

Deferred. Editions are a valid future source-language direction, but current Rust ecosystem support is not uniform enough to make source-language novelty a foundation blocker. Proto3 wire compatibility gives the project a stable implementation path now.

### Exact schema SHA equality as runtime compatibility identity

Rejected. It turns safe additive evolution into unnecessary lockstep deployment and confuses artifact identity with semantic compatibility.

### Fixed capability digest

Rejected. Core v1 semantics are protocol-major invariants; optional extensions are explicit registered numeric capabilities. No digest is needed to recreate exact-list lockstep.

### UUIDv4 CommandId plus independent client sequence

Rejected. The two-dimensional identity/order state requires extra duplicate storage and conflict rules. A GameSession-scoped monotonic uint64 CommandId gives one deterministic order and a bounded duplicate-proof high-water mark.

### QUIC as v1 transport

Deferred until evidence demonstrates material benefit. The transport-profile registry leaves a safe future extension point.

### Application compression in v1

Rejected. It increases decompression/ratio/CPU attack surface before evidence shows bandwidth pressure. Any future compression contract must register all three mandatory bounds.

## 25. Deliberately unresolved after FND-02

FND-02 does **not** decide:

- server tick/scheduler/threading/queue implementation — `FND-03`;
- heartbeat cadence, authoritative liveness state machine, reconnect credential and lease/takeover rules — `FND-04`;
- durable sequence/session persistence across crash — `DUR-02` as required by FND-03/FND-04 recovery;
- movement domain/message definitions — `VSL-MOVE-01`;
- combat/death/loot messages — `VSL-COMBAT-01`;
- map/content snapshot payloads — `VSL-CONTENT-01`;
- inventory/item transactions — `GAME-ITEM-01`/`DUR-03`;
- optional future capability IDs until a real additive feature needs one;
- QUIC/compression until measured evidence requires them.

## 26. Acceptance invariant

A future implementation may claim `protocol-oteryn` v1 compatibility only when it can prove:

> it speaks only the registered Oteryn v1 transport/framing/schema foundation; authenticates TLS correctly with no 0-RTT or Canary downgrade; enforces all hard limits before unsafe allocation; treats `(GameSessionId, CommandId)` as the one ordered command identity; never re-executes a lower CommandId; fences stale connection generations; applies authoritative server sequence and state revisions without guessing; reconciles by bounded replay or atomic snapshot; and passes independent byte, malformed, property, fuzz and cross-version evidence.

Until those proofs exist, this document is architecture authority, **not** an implementation-complete claim.
