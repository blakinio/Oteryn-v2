# DUR-04 — Content, World Detail and Scripting Contract

- Status: `PROPOSED / IN_REVIEW / NOT_STARTED`
- Date: 2026-08-12
- Gate: `DUR-04`
- Scope: paper-only architecture contract.
- Runtime implementation authority: **NONE**.
- DDL/migration authority: **NONE**.
- Production activation authority: **NONE**.

## 1. Contract purpose

This contract completes the architecture intentionally left open by ADR-0005 for native content packaging, deterministic compilation, immutable World Bundle activation, migration/provenance and bounded scripted behavior.

It does not replace ADR-0005. It makes ADR-0005 implementable without freezing physical file encodings that still require the mandated spike/benchmark evidence.

## 2. Normative language

`MUST`, `MUST NOT`, `SHOULD` and `MAY` are normative.

Unknown physical-format details or numeric limits MUST fail closed at implementation review rather than be inferred as unlimited.

## 3. Canonical semantic identity

### 3.1 Package identity

Every package MUST have:

- a stable namespaced `PackageKey`;
- an immutable `PackageRevision`;
- a semantic schema version;
- declared dependencies;
- provenance/licensing metadata;
- a source-manifest digest.

A runtime build MUST use a deterministic **Content Lock** that resolves every dependency to an exact immutable package revision/digest. Runtime dependency resolution MUST NOT use floating versions, mutable branches or network-time “latest” selection.

### 3.2 Content identity

Every canonical content definition MUST have one stable namespaced `ContentKey`.

Legacy numeric IDs and compact runtime IDs MUST NOT become canonical semantic identity. Compiled numeric IDs MAY exist only within the scope of one compiled revision/artifact.

Aliases/deprecations MUST be explicit, deterministic and acyclic. Ambiguous or cyclic alias resolution MUST fail compilation.

## 4. Revision domains

The architecture MUST keep these concepts distinct:

- `content_revision`;
- `map_revision` where separately tracked;
- `ruleset_revision`;
- `world_policy_revision`;
- compiler identity/canonicalization profile;
- exact bundle artifact digest.

A release/deployment record MAY bind them together, but one opaque revision number MUST NOT replace their semantic distinction.

## 5. Source-model boundary

The canonical Oteryn content model is a typed semantic graph independent of its concrete serializer.

Therefore DUR-04 does **not** accept YAML, RON, JSON5, a custom text syntax, `.omap`, `.owb` or any specific binary container as the permanent canonical physical encoding.

Any final physical source/bundle encoding MUST be selected only after the ADR-0005 bounded non-canonical spike proves deterministic hashes, random access, corruption/decompression handling, source-to-bundle-to-load equivalence and representative chunk/floor-packing behavior.

## 6. Deterministic compiler pipeline

The logical pipeline MUST be:

```text
source packages
 -> parse/import
 -> typed canonical model
 -> schema/semantic validation
 -> dependency/key/alias resolution
 -> migration normalization
 -> deterministic lowering
 -> client/server view projection
 -> deterministic artifact assembly
 -> integrity digests
 -> immutable artifact
 -> isolated staging verification
 -> explicit activation
```

For identical source bytes, Content Lock, compiler identity, canonicalization profile and target capability/profile inputs, compilation MUST produce the same logical output and exact artifact digest.

The compiler MUST either canonicalize or reject nondeterminism from filesystem order, unordered collections, locale/timezone, wall clock, machine paths, uncontrolled randomness, duplicate-key precedence and unstable serialization behavior.

## 7. Compile-time fail-closed rules

Compilation MUST fail on at least:

- duplicate canonical content keys;
- ambiguous/cyclic aliases;
- unresolved references;
- incompatible dependency/schema/runtime capability requirements;
- unsupported critical fields;
- invalid spatial references;
- script references lacking declared required capabilities;
- client/server visibility violations;
- relevant value-producing source/encounter definitions lacking explicit GAME-CHANNEL multiplicity and durable eligibility classification;
- missing mandatory resource-limit definitions required by the selected implementation format/runtime.

## 8. Client-safe versus server-authoritative projection

Client artifacts MUST be produced by explicit allowlisted projection from the locked semantic graph.

Server-only authoritative fields MUST NOT be serialized into client artifacts and then merely hidden by UI logic.

Client and server artifacts MUST carry compatible revision/capability metadata so incompatible pairs fail closed.

Client data MUST remain non-authoritative even when it mirrors server definitions.

## 9. Immutable World Bundle

A published World Bundle or equivalent runtime artifact MUST be immutable and content-addressed by integrity digest.

It MUST contain sufficient metadata to identify:

- format/schema version;
- content/map/ruleset/world-policy compatibility where applicable;
- compiler identity;
- Content Lock digest;
- artifact/manifest digest;
- required runtime/protocol capabilities;
- integrity metadata for independently loaded sections/chunks;
- provenance summary;
- client-safe or server-authoritative projection class.

Runtime MUST NOT deserialize unstable Rust memory layout as a public format contract.

## 10. Loader and staging safety

The loader MUST treat every artifact as untrusted until validation completes.

Before authoritative publication it MUST perform, in bounded order:

1. minimal header/metadata validation;
2. size/count/decompression-ratio checks before untrusted-size allocation;
3. checked arithmetic for offsets/counts/byte totals;
4. format/schema/runtime capability validation;
5. manifest/section integrity verification;
6. dependency/lock verification;
7. bounded index/section validation;
8. semantic consistency validation;
9. isolated staging construction.

No partially validated section MAY become authoritative runtime state.

Unknown critical sections or required capabilities MUST fail closed.

All externally controlled counts, lengths, depths, compressed/decompressed sizes, ratios, memory/table counts and equivalent resources MUST have entries in `docs/contracts/RESOURCE_LIMITS_REGISTRY.json` before implementation acceptance.

## 11. Staging and activation

Loading and activation MUST be separate operations.

A staged revision MAY be parsed, verified, indexed and prewarmed without becoming authoritative.

Activation MUST bind an exact coherent revision/artifact set. A new authoritative simulation scope MUST NOT begin with a partial mixture of old/new definitions caused by incremental mutation.

A currently active immutable revision MUST NOT be edited in place.

A later rollout contract MAY permit old and new compatible scopes to coexist temporarily, but every authoritative scope MUST identify the exact revision set governing it.

## 12. Rollback

Rollback means activation of a previously verified compatible artifact.

Rollback MUST NOT restore an older content artifact while leaving authoritative durable state in a semantically incompatible post-migration representation.

If activation requires durable migration, forward and rollback compatibility MUST be proven before production activation.

## 13. Durable-state migration classes

Every content change affecting durable semantic interpretation MUST be classified as exactly one of:

- `COMPATIBLE_NO_MIGRATION`;
- `READ_COMPATIBLE_NORMALIZE`;
- `EXPLICIT_DATA_MIGRATION`;
- `INCOMPATIBLE_REQUIRES_PRODUCT_DECISION`;
- `REMOVED_WITH_EXPLICIT_POLICY`.

`READ_COMPATIBLE_NORMALIZE` MUST be deterministic and MUST NOT create/destroy player value or bypass domain validation.

`EXPLICIT_DATA_MIGRATION` MUST execute through accepted persistence/domain transaction ownership, never direct script/database mutation.

Player-value-bearing removals MUST NOT silently discard, reinterpret or duplicate durable value.

## 14. Legacy conversion and provenance

Each external source area used for migration/evidence MUST record:

- exact source repository revision/archive digest;
- license/provenance status;
- one disposition: `COPY`, `CONVERT`, `REWRITE`, `REFERENCE_ONLY` or `REJECT`;
- importer/converter identity;
- deterministic conversion report;
- unresolved/lossy-semantics report;
- legacy-ID mappings where relevant.

Legacy Intermediate Representation MUST remain an importer-boundary type and MUST NOT become canonical Oteryn content schema.

Otheryn/Canary/other OTS sources MUST NOT by themselves establish Global Tibia parity truth.

## 15. Scripting architecture

The target scripting boundary MUST use WebAssembly Component Model components with a **project-owned, versioned WIT capability ABI**, unless a later accepted ADR explicitly supersedes this decision.

Wasmtime is the initial implementation candidate, but Wasmtime APIs/types MUST NOT define the public Oteryn script contract.

A process-global Lua/game object model is NOT accepted as the target authoritative architecture. A bounded compatibility adapter MAY be considered only in a separate migration contract.

## 16. Script authority model

A script MUST be treated as a bounded decision/proposal component, not as an authoritative mutation owner.

Conceptually:

```text
InvocationContext + bounded read snapshot + explicit capabilities
 -> script component
 -> ProposedActionPlan / typed result
 -> host/domain validation
 -> accepted authoritative command/transaction
```

A script MUST NOT directly:

- commit PostgreSQL transactions;
- mutate arbitrary server/domain objects;
- bypass DUR-03 conservation/idempotency/fencing;
- bypass GAME-ITEM legality;
- bypass GAME-CHANNEL multiplicity/eligibility;
- mint trusted audit/economy truth outside the authoritative mutation boundary.

## 17. Capability security

Capabilities MUST be explicit versioned WIT imports.

The default authoritative script environment MUST provide no ambient:

- filesystem;
- network/socket;
- process spawning;
- environment variable/secret access;
- unrestricted wall clock;
- OS randomness;
- direct SQL;
- global mutable Game object;
- mutable Rust/server object reference.

Capability absence is the default denial mechanism.

Candidate capability families MAY include bounded typed reads, scoped spatial queries, deterministic simulation time/tick, deterministic RNG, proposal of domain actions, bounded diagnostics and typed extension-state access.

Every capability call MUST remain subject to host/domain authorization and resource bounds.

## 18. Deterministic script execution

Authoritative script execution MUST use deterministic inputs/imports.

Deterministic semantic execution MUST use:

- simulation logical time instead of wall clock;
- host-supplied deterministic RNG bound to accepted simulation/replay identity;
- deterministic fuel accounting;
- bounded memory/table/instance resources;
- bounded host-call count;
- bounded query/result collection sizes;
- bounded action-plan size;
- deterministic error/trap mapping.

Fuel exhaustion MUST terminate an invocation without committing its proposed action.

Epoch/wall-clock interruption MAY exist as a secondary operational kill switch but MUST NOT define authoritative gameplay outcome or deterministic replay semantics.

Unconstrained memory/table growth is forbidden for authoritative scripts. The implementation contract MUST choose deterministic memory/table constraints consistent with current runtime capabilities and register exact maxima before acceptance.

## 19. Script failure isolation

Required script validation/instantiation failure MUST block activation of the affected required content.

Missing required capability MUST fail activation or invocation closed.

On invocation trap, fuel exhaustion or invalid result:

- no proposed action from that invocation is committed;
- diagnostics remain bounded;
- the host returns a deterministic domain-level failure category;
- server-only content/secrets MUST NOT leak to clients.

An action plan containing any unauthorized/invalid authoritative action MUST be rejected atomically by default. Partial-plan semantics require a separate domain-specific accepted contract.

Repeated failures MAY feed a circuit-breaker/disable mechanism, but failover MUST NOT silently substitute different reward/quest/economy semantics.

## 20. Script persistent state

VM linear memory/table state MUST NOT be treated as durable gameplay persistence.

Persistent script-owned extension state MUST be:

- typed;
- namespaced;
- schema-versioned;
- size-bounded;
- accessed through project-owned host/domain APIs;
- persisted/fenced/migrated through accepted DUR-02/DUR-03 ownership.

Opaque arbitrary binary blobs are forbidden for authoritative durable state unless a later accepted contract defines their schema/version/limit/migration/audit semantics.

## 21. Hot reload semantics

“Hot reload” MUST NOT mean mutating a live immutable revision in place.

Permitted conceptual workflow:

```text
compile new revision
 -> stage
 -> validate/prewarm
 -> explicit activation for eligible scopes
 -> drain/restart/migrate older scopes under accepted rollout policy
```

Every authoritative scope MUST be able to report which exact content/script artifact revision governed it for replay, diagnostics and audit.

## 22. Package/runtime supply-chain rules

Production runtime MUST NOT fetch unresolved content packages from the network.

Activation MUST use a reviewed immutable lock and verified artifact digests.

Script component digests MUST be bound into the content revision/manifest.

Unknown script imports/capabilities MUST fail closed.

Release signing/trust-root/CDN policy is deferred, but integrity hashes are mandatory now.

## 23. Resource limits

DUR-04 deliberately does not invent numeric ceilings.

Before any parser/compiler/loader/script runtime is accepted, `RESOURCE_LIMITS_REGISTRY.json` MUST contain applicable hard maxima and boundary tests at least for:

- source file/package bytes and file counts;
- manifest/dependency/key/reference counts and nesting;
- bundle/section/chunk compressed bytes;
- decompressed bytes and compression ratio;
- index entries and spatial/object densities where allocation risk exists;
- script component bytes;
- script instance count;
- memory/table minima/maxima and growth policy;
- fuel per invocation;
- host calls per invocation;
- query/result/action-plan counts/bytes;
- persistent script extension-state bytes.

Absent required limits block implementation acceptance.

## 24. Required implementation evidence

A future implementation MUST prove at minimum:

- reproducible artifact digest under identical locked inputs;
- source enumeration/order independence;
- deterministic rejection of duplicate keys/ambiguous aliases/unresolved dependencies;
- server-only fixture absent from client artifact;
- corruption/integrity failure before activation;
- decompression-bomb/oversized fixture rejection before unbounded allocation;
- unsupported required capability/schema rejection;
- mandatory resource-limit registry completeness;
- infinite-loop script stopped by deterministic fuel with zero mutation;
- forbidden filesystem/network/wall-clock capability inaccessible;
- deterministic RNG/replay yields same action plan;
- invalid action plan rejected before mutation;
- migration-required content cannot activate before migration proof;
- incompatible rollback rejected;
- relevant channel-sensitive reward/encounter source lacking multiplicity/eligibility metadata fails compile;
- incompatible content revisions cannot silently coexist under one claimed homogeneous world/channel revision set;
- legacy conversion output/report reproducible from exact source/importer revisions.

## 25. Physical-format spike gate

Before final World Project/World Bundle encoding is accepted, a bounded reversible spike MUST compare candidate encodings against:

- deterministic byte identity;
- source-control diff/review behavior;
- random access;
- corruption detection;
- decompression/resource safety;
- source-to-bundle-to-load equivalence;
- editor save/recovery requirements;
- representative world scale;
- 32x32 versus 64x64 candidate chunking and floor packing;
- patch/download granularity;
- client/server load locality.

Spike artifacts MUST remain non-canonical and non-production until a subsequent accepted contract freezes the encoding.

## 26. Non-authority statements

Acceptance of DUR-04 does NOT authorize:

- creation of production compiler/loader/scripting crates;
- adding Wasmtime or any scripting dependency;
- WIT ABI implementation files;
- PostgreSQL migrations;
- broad content import;
- production content activation;
- Oteryn Studio implementation;
- final physical source/bundle encoding;
- final numeric resource limits;
- production signing/CDN;
- exact gameplay/NPC/quest/AI behavior.

## 27. Lifecycle rule

This document is a candidate while its delivery PR is open.

`DUR-04` becomes `ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED` only after:

1. this delivery candidate is reviewed and merged;
2. a separate lifecycle-closeout change reconciles maintained programme status/register/horizon/index/handoff and archives/releases the active task.

No downstream implementation or broad content-import authority may treat an open delivery PR as accepted architecture.
