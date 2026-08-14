# ALPHA-CLIENT-01 — Native Client Architecture Analysis

- DecisionStatus: `PROPOSED`
- DeliveryStatus: `IN_REVIEW`
- ImplementationStatus: `NOT_STARTED`
- Date: 2026-08-15
- Issue: `#263`
- Worker: `DOMAIN ARCHITECTURE DESIGN AGENT / worker E`
- Branch: `docs/arch-e-alpha-client`
- Authority: analysis for Architecture Coordinator audit; not canonical until accepted/merged by coordinator
- Runtime authorization: **NONE**

## 1. Executive summary

Oteryn-v2 already has a real Windows-first native Rust shell and a deliberately fail-closed `pre-native-protocol` product state. The alpha-client problem is therefore not “choose a GUI framework and build a client from zero”. It is to define the boundaries that let the existing shell grow into a production gameplay client without allowing UI state, local simulation, content files, transport convenience or diagnostics to become a second gameplay authority.

This analysis recommends one production client composition root in `apps/client`, with explicit application/screen coordination and provider boundaries around Identity/Platform directory access, future gameplay admission and transport, client-safe content, configuration/filesystem, diagnostics/crash handling and release/update state. Renderer and OS input remain adapters. Network ingress is reduced into a **non-authoritative client projection** only after protocol generation, sequence, revision and snapshot rules have been satisfied. Player input becomes semantic intent before it can reach future protocol egress. No widget, renderer, local cache or synthetic simulation may write authoritative gameplay state.

The current `pre-native-protocol` behavior remains the only runtime truth. `ADR-0016` and `docs/contracts/PROTOCOL_OTERYN_TRANSPORT_POLICY.json` explicitly say that the gameplay transport adapter, listener and native-client gameplay entry are not implemented and every named client transport mode is unavailable now. This design therefore defines seams and evidence gates without exposing fake TCP/QUIC selectors or constructing placeholder gameplay credentials/routes.

For alpha readiness, the client architecture must also treat content compatibility, configuration migration, crash privacy, update/rollback, Windows packaging and E2E evidence as first-class product boundaries. A green renderer or synthetic harness is insufficient. `ADR-0007` requires separate Tier 1 headless system E2E through the production Platform/protocol/server path, Tier 2 real native-client E2E and Tier 3 release-binary smoke evidence.

## 2. Scope and authority boundary

### 2.1 In scope

This work decides or proposes only client-side architecture needed to make later implementation unambiguous:

- application/screen/composition boundaries;
- provider boundaries and dependency direction;
- local runtime/session observation state;
- future protocol ingress/egress and reconciliation seams;
- renderer/UI/input integration;
- client-safe content projection and active-content boundary;
- configuration, filesystem, logging and crash diagnostics boundaries;
- update, packaging, install and rollback boundaries;
- headless versus interactive testing paths;
- Windows-first platform assumptions;
- client production-readiness and E2E evidence gates.

### 2.2 Explicitly outside this worker's authority

This analysis does **not**:

- implement or authorize a gameplay transport adapter/listener;
- change `protocol-oteryn` framing, message schemas, sequencing, TLS, transport-profile or capability semantics;
- construct FND-04 admission/reconnect grants or change GameSession/CharacterLease authority;
- change server/gameplay legality, deterministic simulation or persistence semantics;
- promote synthetic client simulation to production gameplay authority;
- select a new UI toolkit, protobuf/TLS library, updater framework, installer technology or credential vault;
- define production numeric limits that belong to protocol, security, release or SRE owners;
- modify external repositories, global architecture overlays, executable client code, DDL or production configuration.

## 3. Verified baseline

| Source | Verified fact | Consequence for ALPHA-CLIENT-01 |
|---|---|---|
| `docs/architecture/ADR-0011-native-client-pre-protocol-migration-state.md` | The canonical migrated client is a launchable Windows-first production shell and gameplay is intentionally unavailable/fail-closed. | Alpha architecture must evolve this shell; it must not fabricate a native gameplay path. |
| `apps/client/src/lib.rs` | `ClientBootstrap` composes runtime/renderer/input and `request_gameplay_entry()` returns `NativeProtocolUnavailable`. | Preserve a single product composition root and an explicit gameplay-availability gate. |
| `apps/client/src/windows_shell.rs` | The current product shell is a real `winit` Windows window with renderer resize/render/suspend/close handling and `--smoke`. | Interactive lifecycle is already concrete; later UI belongs above this OS/render adapter boundary. |
| `crates/client-runtime/src/lib.rs` | The client owns an async runtime and cancellation/shutdown boundary. | Runtime ownership belongs to application composition, not individual screens/providers; current thread count is implementation detail, not new architecture authority. |
| `crates/platform-client/src/lib.rs` | Platform directory traffic is bounded and rejects gameplay route/credential/session fields. | Directory/selection and gameplay admission/transport must stay separate client providers. |
| `workspace-boundaries.toml` | `client-domain`, `client-simulation`, synthetic assets and synthetic harness are classified synthetic, not production. | Do not silently add them to the shipping client or call synthetic proof native gameplay proof. |
| `crates/client-domain/src/lib.rs` | Existing synthetic model explicitly describes itself as a protocol-neutral, non-authoritative client projection. | Its semantics are useful evidence for projection separation, but production promotion requires separate authorization. |
| `crates/client-simulation/src/lib.rs` | Existing synthetic simulation deterministically mutates only the non-authoritative projection. | It is not a server-authority substitute and is not a prediction contract. |
| `docs/architecture/FND-02_PROTOCOL_OTERYN_V1_CONTRACT.md` | Server authority, `connection_generation`, server sequence, state revisions, snapshot/delta/resync and bounded parsing are accepted wire semantics. Revision mismatch triggers resync, never speculative delta application. | Future ingress/reconciliation must enforce these semantics before presentation state changes. |
| `docs/architecture/FND-04_IDENTITY_GAME_SESSION_ADMISSION_CHARACTER_LEASE_CONTRACT.md` | Final gameplay admission/control belongs to current Oteryn-v2 game-domain authority; client evidence is corroborative only. | Local “session state” is an observation/progress state machine, never authority to create/restore a GameSession or lease. |
| `docs/contracts/PROTOCOL_OTERYN_TRANSPORT_POLICY.json` | TCP profile 1 is registered architecturally, but gameplay transport adapter/listener/native-client entry are unavailable; all client modes have `runtime_available_now=false`. | No player-visible transport selector or optimistic runtime capability may appear before exact implementation/proof. |
| `docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md` | Client artifacts are explicit allowlisted projections; incompatible revision/capability combinations fail closed; client content is non-authoritative. | Client content loading needs immutable compatible projection activation, not “load anything and hide server fields”. |
| `docs/architecture/CLIENT_CRASH_DIAGNOSTICS_PRIVACY_OWNER_BASELINE.md` | Eligible crash uploads are enabled by default with a persistent global opt-out; payloads are allowlisted/redacted/bounded and optional diagnostics cannot gate gameplay. | Diagnostics must be isolated from authority and respect durable privacy state before upload/retry. |
| `docs/architecture/ADR-0007-native-end-to-end-test-platform.md` | Three E2E tiers are accepted: headless production-protocol system E2E, instrumented native client, production-binary smoke. | Alpha client proof must include all relevant tiers; synthetic-only evidence cannot close gameplay readiness. |
| `docs/architecture/ARCHITECTURE_REVIEW_REFINEMENTS_2026-08-10.md` | External alpha requires maintained threat model, signed artifacts/updater and provenance/SBOM strategy, SRE baselines and player-readable operational states. | Packaging/update/security/operability are release gates, not post-alpha cleanup. |
| `docs/architecture/GAME-VISION-01_EVOLVED_RELIABILITY_UX_FIRST_OWNER_BASELINE.md` | Reliability/UX-first is owner-accepted for first Evolved differentiation; semantic-neutral quality may be shared with Reference. | Client reliability, scaling/input clarity, errors and recovery UX should remain shared foundation unless they intentionally change product semantics. |

## 4. Problem statement

The migrated shell has correct fail-closed behavior but does not yet have the architecture needed to connect future product flows safely. The risk is not primarily renderer selection. The risk is accidental authority leakage while implementation grows:

1. a screen could directly call Platform and later gameplay networking, coupling UI lifecycle to authority-bearing credentials;
2. a local client model could be mistaken for authoritative simulation or accept deltas over a missing revision;
3. Platform world/character selection could be coupled to gameplay route material that the current directory contract intentionally forbids;
4. update/content mutation could change assets or client semantics under a live session without a compatible revision boundary;
5. crash/logging convenience could capture credentials, private chat or unrelated files;
6. a test harness could bypass normal admission/networking and still be reported as end-to-end proof;
7. a current architectural transport target could be rendered as a runtime option despite no adapter existing.

The architecture must make these errors structurally difficult while remaining reversible on technologies that are not yet evidenced.

## 5. Architectural invariants

The following invariants are proposed for coordinator acceptance:

1. **One production composition root.** `apps/client` owns construction, lifecycle and shutdown of production client subsystems. Screens do not construct infrastructure.
2. **UI is not authority.** Screens render view state and emit semantic intent; they do not create GameSession, lease, route or authoritative gameplay mutations.
3. **Platform directory is not gameplay transport.** Identity/directory data ends at bounded selection intent; gameplay admission/transport is a distinct future seam governed by FND-04/FND-02.
4. **Local session state is observational.** It records what the client has requested/observed, never what the server “must” consider authoritative.
5. **Protocol ingress precedes projection mutation.** Connection-generation fencing, message/server sequencing, state revisions and snapshot barriers are validated before authoritative observations are reflected in the local projection.
6. **Revision mismatch fails closed.** Missing/contradictory state triggers resync or terminal handling according to FND-02; no guessed delta application.
7. **Input becomes intent before wire.** OS events are normalized by input adapters into semantic actions; future gameplay egress maps allowed intent to protocol commands only while an accepted binding is active.
8. **Client content is a projection.** Only verified, client-safe, compatible projected artifacts are exposed to renderer/UI; server-only content never enters the client package merely to be hidden later.
9. **Active release payload is immutable.** A running gameplay client does not self-mutate its executable/content payload under an active session.
10. **Optional diagnostics never grant or deny gameplay authority.** Crash/log upload state is independent of server security/audit evidence and cannot be used as an admission prerequisite.
11. **Capabilities are evidence-backed.** UI exposes gameplay/transport functionality only when an implementation-backed capability state says it is available; architectural targets alone are not runtime features.
12. **Tests do not create a hidden product path.** Test-only adapters may observe/invoke normal client paths but cannot forge admission, mutate server state, inject authoritative snapshots or ship enabled by default.

## 6. Recommended logical architecture

### 6.1 Interactive product path

```text
Windows process / event loop
        |
        v
apps/client composition root
        |
        +--> application lifecycle + cancellation
        +--> configuration/privacy/release state
        +--> Identity + Platform directory provider
        +--> client-safe content provider
        +--> diagnostics/crash provider
        +--> future gameplay admission provider     [UNAVAILABLE NOW]
        +--> future gameplay transport provider     [UNAVAILABLE NOW]
        |
        v
application/screen coordinator
        |
        +--> screen/view models ------------------------------+
        |                                                     |
        +--> semantic client intent                           v
        |                                               renderer adapter
        +--> local session-observation state                  ^
        |                                                     |
        +--> non-authoritative world/presentation projection--+
        ^
        |
future protocol reconciliation boundary
        ^
        |
future protocol ingress/egress [FND-02/FND-04 authority preserved]
```

The names above are responsibility labels, not frozen Rust trait/crate/API names.

### 6.2 Dependency direction

The preferred dependency direction is:

```text
OS/window/input/network/filesystem adapters
             -> application ports
             -> client application state / projection semantics
             -> immutable view data
             -> renderer/UI presentation
```

Infrastructure may satisfy application ports. Application/screen logic must not depend on concrete socket, TLS, installer, registry, crash-upload or renderer-backend details.

### 6.3 Current-to-target mapping

- `apps/client`: remains the production composition root and owner of interactive lifecycle.
- `crates/client-runtime`: remains an application-owned async execution/cancellation facility; no screen-specific runtime ownership.
- `crates/platform-client` + `crates/identity`: remain bounded Platform/Identity adapters and must not absorb gameplay transport.
- `crates/input-platform`: remains physical/OS event translation.
- `crates/input-actions`: remains the semantic-action boundary suitable for UI and future gameplay intent.
- `crates/renderer`: remains presentation infrastructure; it receives renderable state and never owns network/session authority.
- `crates/client-domain` and `crates/client-simulation`: remain synthetic under current workspace classification. A later implementation may propose promoting or replacing suitable non-authoritative projection semantics, but this task does not change their production status.
- `tools/synthetic-client-harness`: remains synthetic/non-release and is **not** equivalent to ADR-0007 Tier 1 headless system E2E.

## 7. Application and screen composition

The client should separate **navigation/application state** from **server-authoritative world state**.

Conceptual application states may include:

```text
Bootstrapping
InteractiveNoIdentity
IdentityFlowPending
DirectoryReady
GameplayUnavailable            # current canonical path

# Future states; not runtime-authorized by this document:
AdmissionPending
TransportConnecting
WorldSynchronizing
WorldActive
Reconnecting
TerminalSessionFailure

ShuttingDown
```

These labels are descriptive, not a frozen enum. The important rule is that transition to a future gameplay-active presentation requires positive evidence from the owning admission/transport/protocol path; it cannot be inferred from a selected character, an open socket or a UI button press.

Screens should consume immutable/read-only snapshots of application/view state and emit semantic commands such as “start identity flow”, “select world/channel/character”, “request gameplay entry”, “move north”, “use selected action”, “open settings”, or “shutdown”. The coordinator decides whether an intent is legal in the current local state and delegates to the owning provider. Server legality remains server-owned.

Player-facing operational states should be distinguishable without exposing secrets: world/channel selection, gameplay unavailable, queue/maintenance when later provided by authority, reconnect progress, version/content incompatibility, session conflict and bounded transport diagnostics. Error wording must not invent topology or credential detail that upstream contracts intentionally hide.

## 8. Future gameplay admission and transport seam

### 8.1 Separation from Platform directory

The current Platform client intentionally rejects fields that look like gameplay endpoint, protocol, credential, ticket, session or admission material. Preserve that safety property.

A future client flow should conceptually be:

```text
Identity + directory selection
        -> bounded player selection intent
        -> FND-04-owned admission acquisition
        -> FND-02 transport bootstrap
        -> game-domain acceptance / GameSession evidence
        -> synchronized world projection
```

The exact API, token shape, route field and provider implementation are **not** selected here.

### 8.2 Runtime capability gate

The client must have one semantic runtime capability view that distinguishes at least:

- architecture target exists;
- implementation exists;
- locally usable under the current build/configuration;
- currently authorized by accepted control-plane policy.

A target transport mode is not “available” merely because it appears in ADR-0014 or the transport policy. Under the verified current policy every gameplay mode is unavailable. Therefore the current client continues to present gameplay unavailability rather than a transport picker.

If future transport modes become available, UI selection must consume the accepted capability/policy result. It must not itself implement fallback/downgrade logic. Fallback requires a fresh authorized attempt under the accepted transport/admission contract.

## 9. Protocol ingress, egress and reconciliation

### 9.1 Egress

The application produces semantic player intent. A future gameplay command adapter may encode that intent only after:

- an accepted current GameSession/binding has been observed;
- the current `connection_generation` is active;
- the command is legal to send under client-side phase/shape checks;
- protocol resource limits can be satisfied.

Client-side checks improve UX and bound malformed output; they do not replace server legality. `CommandId` ownership/order, retry and duplicate semantics remain those accepted by FND-02/FND-03/FND-04.

### 9.2 Ingress

Before any server message changes the local world projection, the future ingress boundary must enforce the accepted protocol rules relevant to the message:

1. transport/frame/schema validation;
2. current connection-generation fence;
3. accepted message phase/direction/type;
4. server-sequence ordering where applicable;
5. state-domain revision preconditions;
6. snapshot begin/chunk/commit barrier semantics where applicable;
7. bounded payload/resource handling.

Stale-generation traffic is discarded as specified by FND-02. A delta whose `base_revision` does not equal the client's current domain revision is not applied; the client requests/enters resynchronization instead. Missing authoritative deltas are never fabricated.

### 9.3 Local projection model

The production gameplay client needs a protocol-neutral **non-authoritative projection** concept, but this analysis deliberately does not decide whether the existing synthetic `oteryn-client-domain` types are promoted, replaced or split.

The projection may contain only state required to present and interact with the current client-visible world. It may additionally hold purely local presentation state such as selection/highlight, camera interpolation, UI panel state and pending-input indicators. Those local fields must be distinguishable from server-observed state so they cannot be serialized back as authority or used to “repair” authoritative mismatch.

### 9.4 Prediction and correction

No gameplay prediction/rollback algorithm is accepted by this task. Visual interpolation and input responsiveness may be studied later, but any speculative representation of gameplay outcome must remain reversible presentation state and must never advance authoritative `StateRevision`, `server_sequence`, `CommandId` result or GameSession/lease state.

## 10. Renderer, UI and input integration

### 10.1 Main-thread shell boundary

The Windows event loop/window lifecycle remains at the process shell boundary. OS/window events must be handled without moving Identity/network/content authority into `windows_shell.rs`.

The interactive lifecycle must handle, at minimum, the already-relevant classes of:

- initial window/surface creation;
- DPI/scale and resize changes;
- focus and text/IME input;
- suspend/minimize/resume;
- graphics device/surface loss and recreation where supported by renderer implementation;
- close/shutdown and async cancellation.

Exact framework APIs remain implementation choices.

### 10.2 Semantic input

Physical keyboard/mouse/controller/text events should continue through `input-platform` -> `input-actions` before application/gameplay dispatch. Screen-specific routing decides whether a semantic action is consumed by UI navigation, text editing or future gameplay intent. Raw OS key codes must not become protocol commands.

### 10.3 UI/render model

UI widgets and renderer passes should receive view models/render descriptions derived from local application/projection state. They may keep renderer-local caches (GPU resources, glyph atlases, layout caches), but those caches have no gameplay/session authority and can be reconstructed after device/surface loss.

No exact retained/immediate UI framework is selected here. The current `winit`/renderer foundation is preserved until evidence requires supersession.

## 11. Client-safe content projection and patch boundary

DUR-04 requires an explicit allowlisted client projection. The alpha client should therefore treat content as a verified artifact set rather than loose source files.

Recommended lifecycle:

```text
installed/staged candidate projection
        -> integrity + compatibility verification
        -> immutable local availability
        -> selected active projection revision
        -> session/view consumption
```

Rules:

- server-only fields must be absent from client artifacts rather than hidden at UI time;
- content/build/protocol/capability compatibility metadata must be checked before activation;
- unknown/incompatible required semantics fail closed;
- an active gameplay session pins the accepted client projection/release compatibility context needed for that session;
- staged updates do not mutate the active gameplay projection in-place;
- hot-reload of gameplay-relevant content is not authorized by this task;
- caches may be deleted/rebuilt, but authoritative or compatibility meaning may not depend on cache survival.

The physical bundle encoding, patch delta format, CDN and signing mechanism remain DUR/release decisions.

## 12. Configuration and filesystem model

The Windows client should distinguish four logical storage classes:

1. **Installed release payload** — executable/libraries/resources and shipped client-safe content; immutable while running.
2. **Durable per-user state** — user settings, privacy choice, accessibility/input/layout preferences and versioned migration metadata.
3. **Rebuildable cache** — derived/download staging/cache data that can be removed without changing authority.
4. **Diagnostic spool** — bounded local logs/crash packages subject to redaction/privacy/upload policy.

The implementation should resolve Windows paths through OS-appropriate known-folder/platform abstractions instead of scattering hard-coded `%APPDATA%`, registry or install paths through domain/UI code. Exact directories and installer registry behavior are deferred.

Configuration needs an explicit schema/version and atomic migration/write behavior. A failed migration must preserve a recoverable prior configuration or fall back to safe defaults without silently re-enabling opted-out diagnostics.

Reusable Identity credentials, gameplay admission material and reconnect secrets must not be stored in general configuration, logs, crash packages or content caches. Whether any reusable sign-in material later uses a Windows credential facility is an Identity/security decision, not selected here.

## 13. Logging and crash diagnostics

The accepted privacy baseline is binding input to the client architecture:

- automatic eligible crash diagnostics are enabled by default;
- a clear global durable opt-out must exist;
- opt-out stops new uploads and pending automatic retries while disabled;
- optional client diagnostics cannot block launch/authentication/gameplay;
- opt-out itself is not abuse evidence;
- collection is allowlist-based and redaction occurs before transmission;
- reusable credentials, tokens, private chat content, arbitrary files and unrelated personal data are excluded;
- client diagnostics remain untrusted corroborating evidence, not server authority.

Architecture consequence: logging/crash collection should receive structured, already-classified diagnostic events rather than unrestricted access to every application object or filesystem directory. Secret-bearing provider types should not implement casual debug serialization into logs.

A bounded local crash package may include build/content/protocol identifiers, failure category and narrowly scoped client/session correlation identifiers only where the accepted diagnostics/privacy contracts allow them. Exact retention, upload endpoint and uploader implementation are deferred.

## 14. Update, packaging, install and rollback

### 14.1 Immutable running version

Release mutation must occur outside an active authority-bearing gameplay process. A running client may detect that an update is required/available and may stage non-active bytes through a dedicated release/update boundary, but it must not replace its live executable/content semantics mid-session.

### 14.2 Verification boundary

Before external alpha, accepted programme refinement requires signed artifacts/updater plus provenance/SBOM strategy. Therefore a future updater/installer must have a verification step before candidate bytes become an activatable release. This document does not select the signature format, trust-root layout or build service.

### 14.3 Atomic activation and rollback

Activation should be versioned and atomic at release granularity: either the verified candidate becomes the next active client release, or the previous known-good release remains available. Partial executable/content mixes must not be launched as a valid release.

Rollback is allowed only to a verified release that remains compatible with the current Platform/protocol/content policy. “Last file on disk” is not sufficient rollback authority.

### 14.4 Packaging

The current supported product target remains Windows-first `x86_64-pc-windows-msvc`. The install package should keep immutable release payload separate from user configuration/cache/diagnostics so update/uninstall does not silently destroy user privacy/settings state unless an explicit user action or retention rule requires it.

MSI/MSIX/portable bootstrapper/updater framework, install scope, Start Menu integration, code-signing provider and patch algorithm remain deliberately undecided.

## 15. Headless versus interactive paths

`ADR-0007` already decides that one test shape is insufficient.

### 15.1 Tier 1 — future headless system E2E client

A future QA-owned headless client must use the same accepted production protocol schemas/codecs, sequencing and admission contracts as the native client and traverse Platform/Gateway/game-server boundaries. It has no renderer or physical input requirement, but it cannot call authoritative domain mutation APIs directly.

This is a **real network/system client**, not the current synthetic harness.

### 15.2 Tier 2 — instrumented interactive native client

The real `apps/client` product path may later expose a test-only adapter that invokes normal input/client-command paths and reads semantic observations/screenshots/logs. It must not forge sessions, teleport/mutate server state, inject snapshots/results or exist in production-default builds.

### 15.3 Tier 3 — release-binary smoke

The exact release candidate must prove startup through supported product entry, world entry and bounded gameplay/relog/cleanup once native gameplay exists. The current `--smoke` window-launch path is useful shell evidence but does not by itself satisfy the future Tier 3 gameplay journey.

### 15.4 Existing synthetic harness

`tools/synthetic-client-harness` and synthetic projection/simulation crates remain useful deterministic rendering/input/migration fixtures. Their current workspace classification and absence of production networking mean they must not be reported as Tier 1 protocol E2E or native gameplay proof.

## 16. Windows-first assumptions

Windows is the first supported interactive product target. Architecture should optimize that path while confining OS-specific behavior to adapters so future platforms are not impossible by construction.

Alpha Windows concerns that belong to the shell/platform layer include:

- window/event-loop and graphics surface lifecycle;
- DPI/scaling and multi-monitor transitions;
- focus/capture and keyboard layout behavior;
- text/IME integration;
- filesystem known-folder resolution and permissions;
- process activation/exit/update handoff;
- crash capture integration;
- code-signing/installer presentation and SmartScreen/reputation considerations once release tooling is selected.

No Linux/macOS parity commitment or platform abstraction rewrite is made here.

## 17. Production-readiness gates

Architecture acceptance is not runtime readiness. Suggested alpha gate model:

### Gate AC0 — current pre-native shell

Already supported by accepted migration evidence:

- real Windows shell launches;
- renderer/input/runtime initialize;
- Platform directory boundary remains bounded;
- gameplay entry fails closed before route/credential/network use;
- shutdown is bounded.

This gate does **not** prove native gameplay.

### Gate AC1 — client product substrate implemented

Future implementation evidence should prove:

- versioned safe configuration/privacy persistence;
- client-safe content artifact verification/activation;
- structured bounded diagnostics/crash spool/redaction;
- release identity/version compatibility presentation;
- Windows packaging/install/update/rollback mechanics on disposable environments;
- no gameplay capability is surfaced when unavailable.

### Gate AC2 — native gameplay entry implemented

Blocked until owning programmes provide and prove at exact revisions:

- gameplay transport adapter;
- FND-04 admission/reconnect client integration;
- protocol codec/registry implementation;
- authoritative server endpoint;
- compatible content projection;
- client reconciliation path;
- Tier 1 and Tier 2 E2E across real boundaries.

Only then can gameplay availability change from `pre-native-protocol` for a supported build.

### Gate AC3 — external alpha release readiness

In addition to gameplay proof, external alpha needs the accepted security/SRE/release controls: threat model, signed artifacts/updater, provenance/SBOM strategy, incident/update rollback, required SLO/runbooks/operational states, privacy/legal review and Tier 3 release-candidate smoke.

This document does not declare any of AC1–AC3 implemented.

## 18. Required failure behavior

The client should fail closed and remain diagnostically clear for at least these classes once the owning components exist:

- gameplay runtime unavailable -> remain in non-gameplay UI, no credential/route attempt;
- unsupported protocol/transport/content capability -> no world activation;
- TLS/service identity/ALPN rejection -> terminal connection error; no same-authority downgrade;
- stale connection generation -> stale binding cannot mutate local active projection;
- server-sequence/revision gap -> reconciliation/resync instead of guessed application;
- snapshot incomplete/invalid -> no commit of partial snapshot;
- session/lease conflict -> show bounded user state while server remains authoritative;
- content/release mismatch -> do not enter incompatible world;
- renderer/device loss -> rebuild presentation resources without changing gameplay authority;
- config corruption/migration failure -> safe recoverable defaults/backup strategy without secret leakage or privacy reset;
- diagnostics opted out -> no automatic upload/retry, no gameplay impact;
- update activation failure -> preserve/recover verified previous release rather than launch a mixed payload.

## 19. E2E evidence matrix

| Concern | Unit/component | Tier 1 headless system | Tier 2 native | Tier 3 release |
|---|---|---|---|---|
| semantic input routing | required | semantic command coverage | required through normal input path | representative smoke |
| fail-closed unavailable gameplay | required | N/A before protocol runtime | required | required for pre-native builds |
| admission/session binding | adapter negative tests | required | required | required |
| connection generation / sequencing / revision resync | property/golden/negative | broad required | representative required | representative |
| renderer/UI operational state | renderer/view tests | N/A | required | required smoke |
| client-safe content compatibility | loader/manifest tests | exact revision declared | required | exact packaged artifact |
| disconnect/reconnect | reducer/adapter tests | broad fault injection | required user journey | release smoke/relog |
| diagnostics opt-out/redaction | required | N/A | required settings/restart path | packaged smoke as appropriate |
| updater/install/rollback | package harness | N/A | install-to-native journey | release gate |
| cleanup/evidence envelope | required where applicable | mandatory | mandatory | mandatory |

No hidden retry converts a failed attempt into a pass. Exact client/server/Platform/protocol/content/build revisions must be retained according to ADR-0007.

## 20. Security and privacy consequences

The client is an untrusted edge from the server's perspective and a secret-bearing process from the player's perspective. The architecture therefore minimizes authority and exposure:

- server never trusts client projection as gameplay truth;
- client does not keep general-purpose copies of admission/reconnect secrets;
- directory data and gameplay credentials remain different trust classes;
- protocol parsing is bounded before expensive work;
- content is allowlisted and compatibility-checked;
- update activation requires verified provenance/signing policy before external alpha;
- test-only control surfaces are compile/profile-bounded and cannot ship enabled by default;
- logs/crash packages are structured, bounded and redacted before transmission;
- optional diagnostics cannot be security authority or abuse-score input;
- renderer/UI caches are reconstructable and cannot confer gameplay rights.

## 21. Recommendation decision tests

### R1 — keep `apps/client` as the sole production composition root

- Must decide now? **YES**.
- Downstream blocked without it: screen/provider implementation and lifecycle ownership.
- Becomes harder later: multiple screens/providers can create runtimes/network clients and circular shutdown ownership.
- Superseding evidence: a proven process/deployment/security boundary requiring another production process/composition root.
- Deliberately not decided: exact module/DI framework or Rust trait layout.

### R2 — separate application/screen coordination from adapters

- Must decide now? **YES**.
- Downstream blocked: UI navigation, headless/native testability and provider substitution.
- Becomes harder later: networking/filesystem/render APIs leak into UI state and become expensive to disentangle.
- Superseding evidence: a simpler proven architecture that preserves the same authority/test boundaries with less coupling.
- Deliberately not decided: retained-mode versus immediate-mode UI toolkit.

### R3 — preserve directory versus gameplay admission/transport as separate provider boundaries

- Must decide now? **YES**.
- Downstream blocked: safe login-to-gameplay vertical slice.
- Becomes harder later: Platform directory begins carrying forbidden gameplay secret/route semantics.
- Superseding evidence: an accepted FND/Platform cross-repository contract explicitly changes ownership while preserving security invariants.
- Deliberately not decided: future provider API, token or route representation.

### R4 — use a non-authoritative client projection behind FND-02 reconciliation

- Must decide now? **YES**.
- Downstream blocked: gameplay UI/render state, reconnect and resync implementation.
- Becomes harder later: local state mutations become indistinguishable from server observations.
- Superseding evidence: a later accepted protocol/client model with equally explicit authority/revision semantics and proven migration.
- Deliberately not decided: production crate/type promotion and gameplay prediction algorithm.

### R5 — keep raw OS input and UI widgets out of protocol egress

- Must decide now? **YES**.
- Downstream blocked: deterministic input mapping and Tier 2 E2E control.
- Becomes harder later: key codes/widget callbacks become wire-coupled commands.
- Superseding evidence: none expected short of replacing the accepted input/action architecture with an equivalent tested semantic boundary.
- Deliberately not decided: complete keybind/controller/accessibility policy.

### R6 — require verified immutable client-safe content activation

- Must decide now? **YES**.
- Downstream blocked: content loader, version mismatch UX and release packaging.
- Becomes harder later: loose content/server-only fields become part of shipping compatibility surface.
- Superseding evidence: a later DUR-04 contract with a different but equally explicit projection/compatibility mechanism.
- Deliberately not decided: bundle encoding, delta patch format, CDN and signing format.

### R7 — separate installed payload, durable user state, rebuildable cache and diagnostic spool

- Must decide now? **YES**.
- Downstream blocked: installer/updater, privacy persistence and supportability.
- Becomes harder later: uninstall/update can destroy settings or mix mutable data with signed payload.
- Superseding evidence: platform packaging evidence showing a different layout preserves equivalent immutability/privacy semantics.
- Deliberately not decided: exact Windows paths/registry/install scope.

### R8 — make release activation atomic and outside an active gameplay process

- Must decide now? **YES** for the boundary, **NO** for updater technology.
- Downstream blocked: safe alpha package/update design.
- Becomes harder later: in-place partial updates become normalized and rollback becomes unreliable.
- Superseding evidence: a proven update mechanism that can safely guarantee equivalent atomicity and active-session immutability.
- Deliberately not decided: installer/updater vendor/framework, signature/trust-root implementation and patch algorithm.

### R9 — implement crash diagnostics as privacy-bounded optional client evidence

- Must decide now? **YES**, because owner baseline already exists.
- Downstream blocked: settings model, crash spool/uploader and privacy UX.
- Becomes harder later: unrestricted logging becomes entrenched before privacy controls.
- Superseding evidence: explicit owner/privacy/legal decision changing the accepted default/control while preserving security independence.
- Deliberately not decided: retention duration, upload backend and exact package schema.

### R10 — keep Windows-first OS details behind shell/platform adapters

- Must decide now? **YES** for boundary, **NO** for other-platform support.
- Downstream blocked: coherent Windows alpha implementation without cross-platform abstraction churn.
- Becomes harder later: OS APIs leak into application/session logic and prevent future porting/testing.
- Superseding evidence: accepted product decision to make the client permanently Windows-exclusive with measured simplification benefit.
- Deliberately not decided: Linux/macOS support dates or abstraction framework.

### R11 — preserve ADR-0007's three distinct E2E tiers

- Must decide now? **YES**; it is already accepted architecture.
- Downstream blocked: honest alpha proof and test-surface design.
- Becomes harder later: synthetic/native/headless results become conflated and missing real-boundary evidence is discovered late.
- Superseding evidence: explicit ADR superseding ADR-0007 with equivalent real-boundary proof.
- Deliberately not decided: test orchestration/UI automation libraries and final directory/crate layout.

### R12 — expose only implementation-backed runtime capabilities

- Must decide now? **YES**.
- Downstream blocked: transport/settings UX and pre-native fail-closed correctness.
- Becomes harder later: users/configs start depending on fake or unsupported modes.
- Superseding evidence: none expected; future capability availability changes through implementation/proof, not removal of this invariant.
- Deliberately not decided: exact capability-query API and future QUIC activation/default.

## 22. Alternatives considered

### A. Screen-owned services/networking

Rejected. It is fast initially but couples navigation/window lifecycle to credentials, retries and authority-bearing connection state and is difficult to test headlessly.

### B. Treat current synthetic client simulation as the production gameplay model now

Rejected. Workspace policy classifies it synthetic, it has no accepted FND-02 wire/reconciliation implementation, and this worker is not authorized to promote executable components.

### C. One “client state” store mixing UI, server state and protocol state

Rejected. It makes it too easy for UI/prediction/cache mutation to masquerade as authoritative revision progress.

### D. Let the gameplay process self-update in place

Rejected. It risks mixed executable/content versions and mutating semantics during an authority-bearing session.

### E. Only graphical E2E

Rejected by ADR-0007 because it is too slow/fragile for broad protocol and failure-injection coverage.

### F. Only headless E2E

Rejected by ADR-0007 because it cannot prove Windows UI, renderer, input, packaging and release behavior.

### G. Show TCP/QUIC choices now because architecture names them

Rejected. Current machine-readable policy says every client mode is unavailable and there is no gameplay adapter/listener/entry implementation.

## 23. Risks requiring later evidence

- **Client/server version skew:** compatibility policy exists at protocol/content layers but release/update skew matrix still needs an implementation/release owner.
- **Credential lifetime in process memory:** exact secret container/zeroization/OS credential reuse policy requires security/Identity implementation review.
- **Renderer recovery:** actual device-loss and multi-monitor/DPI behavior requires Windows hardware evidence.
- **Content footprint/patch cost:** physical format, caching and delta strategy require measured bundle/download data.
- **Update trust:** signed-artifact/updater/provenance/SBOM requirement is accepted, but trust root/toolchain is not selected.
- **Headless/native semantic drift:** shared protocol/generated semantics plus cross-tier scenario equivalence need implementation tests.
- **Error information disclosure:** useful diagnostics must be reconciled with hidden topology/credential constraints.
- **Accessibility/input policy:** architecture supports semantic input separation but product requirements remain a later owner decision.

## 24. DECISIONS_NOT_TAKEN

The following are deliberately **not** decided by ALPHA-CLIENT-01:

1. exact UI/widget framework or retained/immediate composition model;
2. replacement of `winit`, renderer backend or GPU API;
3. production promotion/replacement of `client-domain` or `client-simulation` crates;
4. gameplay prediction, interpolation, rollback or client-side combat simulation algorithm;
5. gameplay transport adapter implementation or activation of TCP/QUIC client modes;
6. QUIC profile ID, QUIC library, fallback timings or default promotion;
7. FND-04 grant/token/route/reconnect API or server authority semantics;
8. protocol message schemas, codec/TLS/protobuf Rust libraries or resource limits beyond accepted parent contracts;
9. physical client content bundle, patch/delta format, CDN or content-signing implementation;
10. exact Windows install directories, registry keys, install scope or installer technology;
11. updater framework, code-signing provider, trust-root mechanism or SBOM generator;
12. secure storage technology for any future reusable sign-in credential;
13. exact log/crash retention durations, upload backend or legal/privacy wording;
14. production timeouts, retry/backoff, cache/log/spool byte ceilings unless owned by an accepted parent contract;
15. Linux/macOS support commitment;
16. final accessibility/keybind/controller policy;
17. release-channel/version-skew/mandatory-update product policy;
18. server/gameplay legality, persistence, simulation or balance behavior.

## 25. CROSS_DOMAIN_FINDINGS

```yaml
cross_domain_finding:
  id: ALPHA-CLIENT-01-XD-01
  observed_in_domain: native-client
  target_owner: protocol-network-runtime
  severity: P1
  evidence: docs/architecture/ADR-0016-gameplay-transport-client-mode-runtime-readiness.md + docs/contracts/PROTOCOL_OTERYN_TRANSPORT_POLICY.json
  conflict_or_gap: Accepted TCP profile semantics exist, but gameplay transport adapter/listener/native-client gameplay entry are not implemented and all client transport modes are runtime-unavailable.
  required_before: Any client build may advertise or exercise native gameplay entry or transport-mode selection.
  worker_action: REPORT_ONLY
```

```yaml
cross_domain_finding:
  id: ALPHA-CLIENT-01-XD-02
  observed_in_domain: native-client
  target_owner: admission-session-integration
  severity: P1
  evidence: docs/architecture/FND-04_IDENTITY_GAME_SESSION_ADMISSION_CHARACTER_LEASE_CONTRACT.md + crates/platform-client/src/lib.rs
  conflict_or_gap: Server/admission authority semantics are accepted, while the current production client intentionally has no gameplay route/credential/session handoff implementation from Platform selection into FND-04 admission and transport binding.
  required_before: Real interactive Identity/directory selection can continue into authoritative gameplay admission/reconnect E2E.
  worker_action: REPORT_ONLY
```

```yaml
cross_domain_finding:
  id: ALPHA-CLIENT-01-XD-03
  observed_in_domain: native-client
  target_owner: content-release-toolchain
  severity: P1
  evidence: docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md
  conflict_or_gap: Client-safe projection and compatibility semantics are accepted, but physical client artifact/bundle encoding, patch distribution and production signing/activation implementation are deliberately not selected or implemented.
  required_before: Packaged gameplay client content can be updated and activated for external alpha.
  worker_action: REPORT_ONLY
```

```yaml
cross_domain_finding:
  id: ALPHA-CLIENT-01-XD-04
  observed_in_domain: native-client
  target_owner: security-release-sre
  severity: P1
  evidence: docs/architecture/ARCHITECTURE_REVIEW_REFINEMENTS_2026-08-10.md
  conflict_or_gap: External alpha requires signed artifacts/updater, build provenance/SBOM strategy, threat model and rollback/operability evidence, but this worker has no accepted concrete release trust/update implementation to consume.
  required_before: External alpha packaging/update channel is production-enabled.
  worker_action: REPORT_ONLY
```

```yaml
cross_domain_finding:
  id: ALPHA-CLIENT-01-XD-05
  observed_in_domain: native-client
  target_owner: qa-e2e
  severity: P2
  evidence: docs/architecture/ADR-0007-native-end-to-end-test-platform.md + workspace-boundaries.toml + tools/synthetic-client-harness
  conflict_or_gap: ADR-0007 requires a headless client that traverses production admission/transport/protocol boundaries, while the current synthetic harness is classified synthetic and does not constitute that Tier 1 path.
  required_before: Native gameplay readiness is reported as system-E2E proven.
  worker_action: REPORT_ONLY
```

```yaml
cross_domain_finding:
  id: ALPHA-CLIENT-01-XD-06
  observed_in_domain: native-client
  target_owner: diagnostics-privacy-platform
  severity: P2
  evidence: docs/architecture/CLIENT_CRASH_DIAGNOSTICS_PRIVACY_OWNER_BASELINE.md
  conflict_or_gap: Client privacy/default/opt-out/redaction rules are accepted, but crash-package transport backend, retention/deletion policy and production ingestion contract are not finalized by this client architecture task.
  required_before: Automatic client crash upload is production-enabled.
  worker_action: REPORT_ONLY
```

## 26. Coordinator audit questions

The Architecture Coordinator should explicitly verify that this proposal:

1. does not promote the synthetic client model into production by documentation alone;
2. preserves current pre-native fail-closed behavior and ADR-0016 runtime unavailability;
3. does not redefine FND-02/FND-04 server/protocol authority;
4. is compatible with DUR-04 client-safe projection and future bundle/toolchain work;
5. preserves ADR-0007's distinction among synthetic, Tier 1 headless, Tier 2 native and Tier 3 release evidence;
6. places external-alpha update/signing/security requirements in the correct owner domain rather than pretending they are solved here;
7. keeps technology choices reversible while freezing the authority/dependency boundaries needed before implementation.

## 27. Proposed disposition

Recommend coordinator acceptance of the boundary model as the implementation-guiding native-client baseline, while keeping all runtime implementation status `NOT_STARTED` and all cross-domain findings report-only until their owning programmes deliver accepted evidence.
