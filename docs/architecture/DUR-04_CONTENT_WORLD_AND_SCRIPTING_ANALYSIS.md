# DUR-04 — Content, World Detail and Scripting Analysis

- Status: `PROPOSED / IN_REVIEW / NOT_STARTED`
- Date: 2026-08-12
- Gate: `DUR-04`
- Coordination ID: `OTV2-NATIVE-WORLD-CONTENT`
- Scope: paper-only architecture analysis; no runtime, DDL, compiler, loader, Studio or production implementation is authorized.

## 1. Purpose

`DUR-04` completes the architecture intentionally left open by ADR-0005 for native content packaging, deterministic compilation, immutable runtime bundles, safe content activation/migration and bounded scripting.

The gate must not redesign accepted world semantics. ADR-0005 already owns the greenfield native world/content direction, the separation of World Project / canonical model / World Bundle, stable namespaced keys, semantic geography versus technical chunks, bounded legacy conversion, Oteryn Studio and the separation of authored static definitions from durable dynamic state.

This gate therefore answers a narrower question:

> How does a validated, versioned source graph become an immutable, reproducible and safely activatable runtime content revision, and how can scripted behavior execute without becoming a second authority path or a nondeterministic/unbounded escape hatch?

## 2. Consumed accepted contracts

### ADR-0005

Must preserve:

- canonical source identity is semantic and project-owned, not OTBM/OTB/legacy numeric IDs;
- editable World Project, canonical semantic model and runtime World Bundle are distinct representations;
- exact physical source/bundle encoding remains unfrozen until the required bounded spike and benchmark evidence exists;
- source references use stable namespaced content keys;
- compiled numeric IDs are revision-scoped implementation mappings;
- client-safe and server-authoritative sections may differ;
- runtime loading is bounded, checksummed, versioned and fail-closed;
- authored static definitions are not runtime persistence.

### GAME-ITEM-01 and DUR-03

Scripts and content definitions may request/describe item behavior but must not bypass:

- typed item legality and equipment/container rules;
- one authoritative location per live item instance;
- transaction identity/idempotency;
- conservation/source-sink policy;
- stale-authority fencing;
- atomic persistence/audit boundaries.

### GAME-CHANNEL-01

Content compilation must make simulation scope and durable eligibility scope explicit for relevant reward/value-producing content. Runtime locality is not sufficient evidence that an event or source may multiply per channel.

### FND-03

The authoritative simulation writer requires bounded work and deterministic stale-result rejection. Script execution therefore requires explicit budgets and cannot receive unrestricted blocking I/O or arbitrary host mutation.

### DUR-02

Persisted character/world extension state must remain schema-versioned and migration-safe. Content activation must not reinterpret existing persisted values silently.

### ANL-01

Audit/security/economy-relevant mutations remain emitted through the authoritative event/audit boundary. A script cannot emit trusted audit truth independently of the accepted mutation.

## 3. Facts, inferences and deliberate unknowns

### FACT

ADR-0005 requires a deterministic compiler and immutable World Bundle but deliberately leaves exact physical encodings, compression and final chunk/floor packing behind a bounded spike.

### FACT

The resource-limit registry requires every externally controlled size/count/depth to have an explicit hard maximum before implementation acceptance; missing required limits fail review rather than becoming unlimited.

### FACT

Current Wasmtime documentation provides deterministic fuel-based interruption and distinguishes it from nondeterministic epoch interruption. Current Wasmtime deterministic-execution guidance also warns that nondeterministic imports, unconstrained memories/tables and memory/table growth can break deterministic behavior.

### FACT

The WebAssembly Component Model/WIT provides typed import/export interface contracts, which is suitable as a project-owned capability boundary independent of the concrete Wasmtime host API.

### INFERENCE

A Component Model + WIT host ABI gives Oteryn a better long-term compatibility and capability boundary than embedding a process-global Lua state or exposing Rust internals directly. Confidence: high.

### UNKNOWN / DELIBERATELY DEFERRED

This gate does **not** select:

- YAML, RON, JSON5 or a custom textual syntax as the final authoring serialization;
- the `.omap`/`.owb` final extension names;
- final binary container format;
- 32x32 versus 64x64 chunk size or vertical floor packing;
- compression codec;
- exact numeric bundle/decompression/script-fuel/memory/table limits;
- exact Wasmtime crate version.

These require the already mandated spike/benchmark or implementation dependency review. Freezing them here would contradict ADR-0005.

## 4. Canonical content graph

The canonical unit is not a directory tree or serializer. It is a typed semantic graph.

### 4.1 Package identity

Every content package has:

- `PackageKey` — stable namespaced semantic identity;
- `PackageRevision` — immutable revision identity of one package publication;
- `schema_version` — version of the semantic schema understood by compiler/migration tooling;
- explicit dependency constraints;
- provenance/licensing metadata;
- source manifest digest.

A resolved build produces a **Content Lock** containing exact package revisions and digests. Runtime never resolves floating dependencies.

### 4.2 Content identity

Every canonical content object has one stable `ContentKey`, for example:

- `oteryn:item.currency.crystal_coin`;
- `oteryn:creature.dragon`;
- `package.example:quest.sunken_gate`.

Aliases/deprecations are explicit migration metadata. Alias chains must be acyclic and deterministically resolved. Compiled numeric IDs are scoped to a specific compiled revision and never become durable semantic identity.

### 4.3 Separate revision domains

The following are distinct and must not be collapsed into one opaque build number:

- `content_revision` — resolved semantic content graph;
- `map_revision` — authored map/spatial content revision where independently useful;
- `ruleset_revision` — gameplay rules/profile revision;
- `world_policy_revision` — world-level policy configuration revision;
- `compiler_identity` — compiler version/build identity and canonicalization profile;
- `bundle_artifact_id` — content-addressed digest of exact compiled artifact bytes.

A deployment/replay record can bind several of these together, but one value does not semantically replace the others.

## 5. Deterministic build pipeline

Normative logical pipeline:

```text
source packages
  -> parse/import
  -> typed canonical model
  -> schema + semantic validation
  -> dependency/key resolution
  -> migration normalization
  -> deterministic lowering
  -> server/client view partition
  -> deterministic serialization/container assembly
  -> checksums/digests
  -> immutable World Bundle artifact(s)
  -> staging verification
  -> explicit activation
```

### 5.1 Determinism requirements

For identical:

- exact source bytes;
- Content Lock;
- compiler identity;
- canonicalization profile;
- target capability/profile inputs;

compilation must produce identical logical output and identical artifact digest.

The compiler must canonicalize or reject nondeterministic inputs including:

- filesystem enumeration order;
- unordered map/set iteration where order affects output;
- locale/timezone-dependent parsing;
- current wall clock in artifact content;
- machine-specific absolute paths;
- nondeterministic random seeds;
- unstable floating serialization where byte identity matters;
- unspecified duplicate-key precedence.

Timestamps used for release metadata must be outside reproducibility-critical content or supplied as explicit build inputs.

### 5.2 Fail-closed resolution

Compilation fails on:

- duplicate canonical keys;
- ambiguous aliases;
- dependency cycles not explicitly allowed by a future package contract;
- unresolved references;
- incompatible schema/runtime capability requirements;
- unsupported critical fields;
- invalid spatial references;
- missing required script capability declarations;
- relevant value-producing content without an explicit GAME-CHANNEL multiplicity/eligibility classification;
- missing mandatory resource-limit registry entries required by the selected physical format/runtime.

## 6. Client-safe and server-authoritative views

The project may compile multiple artifacts/views from the same locked semantic graph.

Server-authoritative data may include hidden encounter/loot/quest conditions, authoritative AI/script modules, security-sensitive rules and server-only metadata.

Client-safe data may include rendering/appearance/audio/public navigation metadata and other explicitly published definitions.

Rules:

1. client artifacts are generated by allowlisted projection, not by “serialize everything then hide a few fields”;
2. server-only fields cannot be reachable through client bundle references;
3. both views carry compatible revision identity so mismatched client/server content fails compatibility checks rather than silently drifting;
4. client content never becomes authoritative merely because it mirrors a server definition.

## 7. Immutable bundle and loader boundary

A World Bundle is immutable after publication. Activation points to an exact verified artifact; runtime never edits it in place.

### 7.1 Required metadata

At least:

- format/schema versions;
- content/map/ruleset/world-policy compatibility metadata where applicable;
- compiler identity;
- exact Content Lock digest;
- artifact/manifest digest;
- section/chunk integrity metadata;
- required runtime/protocol capabilities;
- provenance summary;
- server/client view classification.

### 7.2 Loader phases

```text
untrusted artifact
 -> header/minimal metadata validation
 -> hard size/count/decompression-ratio checks
 -> version/capability validation
 -> integrity verification
 -> dependency/manifest verification
 -> bounded section/index validation
 -> semantic consistency checks
 -> isolated staging representation
 -> activation gate
```

No partially validated section is published into authoritative runtime state.

Checked arithmetic is mandatory for byte/count/offset calculations. Unknown critical sections or unsupported required capabilities fail closed.

## 8. Staging, activation, rollback and revision coexistence

Content loading and content activation are separate operations.

### 8.1 Staging

A staged revision may be parsed, validated, indexed and prewarmed without becoming authoritative.

### 8.2 Activation

Activation is explicit and records exact revision/artifact identity. The activation boundary must be atomic from the perspective of a new authoritative simulation scope: it starts with one coherent revision set, never a mixture caused by partial reload.

Existing running scopes may continue on the old compatible revision under a separately accepted rollout policy; silent in-place mutation of their definitions is forbidden.

### 8.3 Rollback

Rollback means activation of a previously verified compatible artifact. It does not mean restoring old bytes while leaving persisted state migrated beyond them.

If a content revision requires a durable-state migration, rollback eligibility must be proven by the migration contract before activation.

## 9. Durable state and content migrations

Persisted state stores semantic identity and schema/revision information sufficient to avoid silent reinterpretation.

Migration classes:

- `COMPATIBLE_NO_MIGRATION` — old persisted data has identical accepted meaning;
- `READ_COMPATIBLE_NORMALIZE` — loader/domain may deterministically normalize to the new representation without changing gameplay value/authority;
- `EXPLICIT_DATA_MIGRATION` — persisted authoritative state must be transactionally migrated before activation;
- `INCOMPATIBLE_REQUIRES_PRODUCT_DECISION` — no automatic activation;
- `REMOVED_WITH_EXPLICIT_POLICY` — removal requires an accepted tombstone/replacement/refund/conversion policy where durable player value is affected.

Scripts cannot implement ad-hoc persistence migrations by direct database access. Durable migrations are typed domain/persistence operations under DUR-02/DUR-03 ownership.

## 10. Legacy conversion and provenance

Every external source set used for migration/evidence requires:

- exact repository/source revision or archive digest;
- license/provenance disposition;
- source-area classification: `COPY`, `CONVERT`, `REWRITE`, `REFERENCE_ONLY` or `REJECT`;
- importer version;
- deterministic conversion report;
- unresolved/lossy-semantics report;
- legacy-ID mapping where applicable.

Legacy Intermediate Representation remains quarantined at the importer boundary. LIR types do not become the canonical Oteryn semantic model.

Reference OTS/Otheryn/Canary content can establish inventory, candidate values and migration fixtures. It does not by itself prove current Global Tibia behavior; Reference parity claims continue to require the accepted evidence hierarchy.

## 11. Script architecture options

### Option A — process-global Lua-style runtime

Rejected as target architecture because it encourages global mutable state, weak capability boundaries and accidental coupling to process internals. A bounded legacy adapter may exist only under a later explicit migration contract.

### Option B — embedded language with custom sandbox but direct host-object bindings

Rejected as the primary long-term boundary. Even if safe initially, direct host-object bindings make API compatibility and authority review dependent on runtime internals.

### Option C — WebAssembly Component Model with project-owned WIT capability ABI

Recommended.

Benefits:

- typed explicit imports/exports;
- capability-oriented host surface;
- module isolation;
- language-neutral guest possibility;
- project-owned ABI versioning independent from Rust struct layout;
- deterministic compute budget support through Wasmtime fuel;
- straightforward denial-by-absence of filesystem/network/process/environment capabilities.

Wasmtime is the first implementation candidate, not the semantic owner of the ABI.

## 12. Script execution model

A content script is a pure/bounded decision component over typed inputs as far as practical.

Conceptual interface:

```text
InvocationContext + ReadSnapshot + ExplicitCapabilities
              |
              v
         Script Component
              |
              v
     ProposedActionPlan / Result
              |
              v
 host validates every action against domain authority
              |
              v
 accepted authoritative commands/transaction(s)
```

The script does **not** receive:

- PostgreSQL connection;
- filesystem access;
- network/socket access;
- process spawning;
- environment variables/secrets;
- unrestricted wall clock;
- OS randomness;
- mutable Rust/server object references;
- a global `Game` object;
- direct transaction commit APIs.

## 13. Capabilities

Capabilities are explicit imports, versioned in the project-owned WIT contract. Example capability families may include:

- bounded read of actor/target state;
- bounded spatial query within declared scope;
- deterministic RNG stream supplied by simulation context;
- deterministic simulation time/tick read;
- propose combat/effect/action intent;
- propose item/domain transaction intent;
- emit non-authoritative diagnostic data;
- read/write typed script extension state only through approved domain APIs.

Possessing a capability to **propose** an action never bypasses domain validation, ownership, cooldown, GAME-CHANNEL eligibility, DUR-03 conservation or fencing.

## 14. Determinism and budgets

For authoritative scripts:

- deterministic imports only;
- host-supplied deterministic RNG keyed by accepted simulation/replay seed and invocation identity;
- simulation tick/logical time instead of wall clock;
- deterministic fuel budget;
- bounded memory/table/instance counts;
- no unconstrained memory/table growth;
- bounded host-call count and returned collection sizes;
- bounded action-plan size;
- deterministic trap/error mapping.

Wall-clock watchdogs/epoch interruption may exist as a secondary operational kill switch, but their firing point cannot define gameplay semantics or replay results. The deterministic semantic budget is fuel/host-call/resource based.

Numeric maxima must be entered in `RESOURCE_LIMITS_REGISTRY.json` before runtime implementation acceptance. This paper-only gate deliberately does not invent numbers.

## 15. Script failure policy

Default fail-closed behavior:

- validation/instantiation failure: content revision cannot activate when the script is required;
- missing required capability: activation failure;
- fuel exhaustion/trap/invalid result during invocation: no proposed action is committed;
- invalid/unauthorized action in a returned plan: reject the entire plan unless a future domain-specific contract explicitly proves partial-plan semantics safe;
- repeated runtime script failure may trip a bounded circuit breaker/disable policy, but disabling authoritative quest/reward logic cannot silently substitute a different gameplay result;
- failure diagnostics are bounded and must not leak secrets/server-only content to clients.

## 16. Script persistent state

VM memory is not durable state.

A script may own only typed, versioned extension state declared through a registered schema/key namespace and accessed through host/domain APIs. Durable state is stored/fenced/migrated by accepted persistence mechanisms.

Opaque arbitrary binary blobs are disallowed for authoritative durable gameplay state unless a later contract defines schema/version/size/migration/audit semantics.

## 17. Hot reload terminology

“Hot reload” must not mean mutating a live immutable revision in place.

Allowed conceptual operations:

- compile a new revision;
- stage and validate it;
- activate it for new or explicitly migratable scopes;
- drain/restart or migrate old scopes under an accepted rollout contract;
- rollback to a previously verified compatible artifact.

This preserves deterministic replay and incident forensics because a running scope can always name the exact content/script artifact revision that governed it.

## 18. Security and supply-chain model

Before activation:

- package dependencies are locked;
- source/import provenance is recorded;
- script component digest is bound to the content revision;
- unknown imports/capabilities are rejected;
- bundle/section integrity is verified;
- physical parser/decompressor limits exist in the resource registry;
- server-only content remains outside client projection;
- no unreviewed remote package resolution occurs in production runtime.

Release signing/trust roots are deliberately deferred to a dedicated distribution/release contract; hashes/integrity metadata are required now even if signing is added later.

## 19. Acceptance scenarios

A future implementation must prove at least:

1. identical locked source/compiler inputs produce identical artifact digest;
2. shuffled source enumeration does not change output;
3. duplicate key/ambiguous alias/unresolved dependency fails compilation;
4. client projection contains no marked server-only fixture;
5. corrupted manifest/section/checksum fails before activation;
6. oversized/decompression-bomb fixture fails before unbounded allocation;
7. unsupported required capability/schema fails closed;
8. missing mandatory resource-limit entry blocks implementation acceptance;
9. infinite-loop script terminates by deterministic fuel exhaustion with zero committed action;
10. script requesting unavailable filesystem/network/clock capability cannot instantiate or call it;
11. deterministic RNG/script replay produces identical proposed action plan;
12. unauthorized/invalid action plan is rejected before mutation;
13. content change requiring durable migration cannot activate before migration proof;
14. rollback incompatible with migrated durable state is rejected;
15. relevant reward/spawn/encounter definition without GAME-CHANNEL multiplicity/eligibility classification fails compilation;
16. two channels of one world cannot silently run incompatible active content revisions under one claimed homogeneous revision set;
17. legacy import report is reproducible from exact source revision and importer identity.

## 20. Must decide now vs defer

### Must decide now

- stable semantic package/content identity;
- exact dependency lock for runtime builds;
- deterministic compiler contract;
- immutable artifact/staging/activation model;
- migration class semantics;
- server/client projection boundary;
- capability-oriented deterministic script boundary;
- no direct authoritative mutation from scripts;
- fail-closed resource-limit policy.

### Deliberately defer

- exact authoring syntax/serializer;
- exact binary container/codec;
- chunk dimensions/floor packing;
- compression algorithm;
- exact numeric limits;
- final Wasmtime version;
- production signing/CDN;
- Studio implementation details;
- domain-specific quest/NPC/combat formulas.

## 21. Recommendation

Accept DUR-04 with the semantic architecture above, then require a separate bounded non-canonical format/compiler/loader spike before freezing physical source/bundle encoding. Scripting implementation should start only after project-owned WIT interfaces and resource limits are separately reviewed as implementation artifacts.

This structure preserves the greenfield Oteryn design, supports complex quests/mechanics without making content opaque, is reviewable by humans and AI tooling at the semantic-model level, enables deterministic migration/build/replay, and prevents scripts from becoming a second unsafe server runtime.
