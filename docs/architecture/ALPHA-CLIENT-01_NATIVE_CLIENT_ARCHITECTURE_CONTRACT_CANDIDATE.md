# ALPHA-CLIENT-01 — Native Client Architecture Contract Candidate

- DecisionStatus: `CANDIDATE`
- DeliveryStatus: `IN_REVIEW`
- ImplementationStatus: `NOT_STARTED`
- Date: 2026-08-15
- Issue: `#263`
- Worker: `DOMAIN ARCHITECTURE DESIGN AGENT / worker E`
- Depends on:
  - `docs/architecture/ADR-0003-platform-identity-game-gateway-and-admission-boundary.md`
  - `docs/architecture/ADR-0011-native-client-pre-protocol-migration-state.md`
  - `docs/architecture/ADR-0016-gameplay-transport-client-mode-runtime-readiness.md`
  - `docs/architecture/FND-02_PROTOCOL_OTERYN_V1_CONTRACT.md`
  - `docs/architecture/FND-04_IDENTITY_GAME_SESSION_ADMISSION_CHARACTER_LEASE_CONTRACT.md`
  - `docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md`
  - `docs/architecture/ADR-0007-native-end-to-end-test-platform.md`
  - `docs/architecture/ARCHITECTURE_REVIEW_REFINEMENTS_2026-08-07.md`
  - `docs/architecture/CLIENT_CRASH_DIAGNOSTICS_PRIVACY_OWNER_BASELINE.md`
- Companion analysis: `docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_ANALYSIS.md`
- Authority: candidate for Architecture Coordinator audit; not canonical until coordinator acceptance/merge
- Runtime authorization: **NONE**

## 1. Purpose

This candidate defines the minimum normative client-side boundaries required to evolve the accepted Windows-first `pre-native-protocol` shell into the native gameplay client without creating a second gameplay authority or fabricating runtime readiness.

Responsibility labels in this document are architectural roles. They are **not** frozen Rust trait, type, crate, module or library names unless an already accepted parent contract says otherwise.

## 2. Parent authority

This candidate does not supersede or reinterpret its parent contracts.

`ADR-0003-platform-identity-game-gateway-and-admission-boundary.md` is an explicit consumed parent authority for the client game-entry control-plane chain. It owns the separation of Platform Identity, one-time Game Login Ticket issuance/redemption, Platform-owned Game Gateway route selection and short-lived pre-admission material from final game-domain admission. `FND-04` remains authoritative for final gameplay admission, `GameSessionId` creation/replacement and `CharacterLease`; Platform/Gateway pre-admission material MUST NOT be promoted into final gameplay authority.

Where a conflict exists:

1. accepted protocol/admission/content/security/E2E parent contracts win over this candidate;
2. current machine-readable runtime availability wins over architectural target descriptions;
3. the client MUST fail closed rather than infer missing authority;
4. coordinator acceptance of this document MUST NOT be reported as runtime implementation or production activation.

## 3. Current runtime truth

Until exact implementation and E2E evidence supersede the verified pre-native state:

```text
native Windows shell                  = AVAILABLE
renderer/input/runtime bootstrap      = AVAILABLE
bounded Identity/Platform directory   = AVAILABLE_AS_MIGRATED_BASELINE
native gameplay entry                 = UNAVAILABLE
gameplay transport adapter            = UNAVAILABLE
gameplay listener                     = UNAVAILABLE
TCP/QUIC player modes                 = UNAVAILABLE
```

The production client MUST therefore continue to fail gameplay entry before requesting or consuming gameplay authority material, including a one-time Game Login Ticket for a connection that cannot complete, before gameplay route/credential consumption and before gameplay network connection while those capabilities remain unavailable.

## 4. Production composition contract

### 4.1 Composition root

`apps/client` MUST remain the sole production client composition root unless a later accepted decision introduces a real process/deployment/security boundary.

The composition root owns:

- application lifecycle and ordered shutdown;
- async runtime lifetime;
- renderer/window/input adapter lifetime;
- audio provider and audio-device/session lifetime;
- Identity/Platform provider lifetime;
- client configuration/privacy state;
- client-safe content provider lifetime;
- diagnostics/crash provider lifetime;
- future Game Gateway/pre-admission control-plane and gameplay transport provider lifetime when separately implemented and authorized;
- release/update status presented to the application.

Screens/widgets MUST NOT construct infrastructure clients, async runtimes, audio devices, gameplay sessions or authority-bearing transports.

### 4.2 Dependency direction

Application and presentation logic MUST depend on semantic ports/state rather than concrete OS, socket, TLS, filesystem, installer, audio-device or renderer-backend APIs.

Infrastructure adapters MAY depend inward on those semantic boundaries. The inward layer MUST NOT depend outward on a concrete installer/updater/network/UI/audio technology solely for convenience.

## 5. Application and screen contract

The client MUST separate:

- process/application lifecycle state;
- Identity/directory/navigation state;
- local gameplay-session **observation** state;
- non-authoritative world projection;
- purely local UI/presentation state;
- renderer resource/cache state;
- audio presentation state/resource state.

A screen MUST:

- consume read-only/immutable view state or an equivalent one-way presentation projection;
- emit semantic user intent;
- present bounded operational/failure states without exposing secrets or hidden topology.

A screen MUST NOT:

- create or restore `GameSessionId` authority;
- grant/acquire a `CharacterLease` by local decision;
- treat a selected character/world/channel as accepted gameplay admission;
- mutate authoritative gameplay state;
- apply raw network payloads directly to renderer/UI state.

## 6. Runtime capability contract

Player-facing functionality MUST be gated by **runtime capability evidence**, not by the existence of an architecture target.

The client capability view MUST be able to distinguish conceptually:

```text
architecture target
implementation present
locally usable in this build/environment
currently authorized/eligible under accepted policy
```

Exact representation is deferred.

A transport mode MUST NOT be shown as selectable/usable if its runtime implementation is unavailable. In particular, current `AUTO_TCP_FIRST`, `PREFER_QUIC`, `TCP_ONLY` and `QUIC_ONLY` architecture targets MUST NOT be exposed as working player options while `runtime_available_now=false`.

The UI MUST NOT implement security downgrade/fallback semantics. Any future cross-transport retry/fallback MUST be driven by accepted admission/transport policy and fresh authority where required.

## 7. Identity, directory, Gateway and gameplay boundary

The client MUST preserve a hard semantic separation between:

1. Platform Identity and reusable credential handling;
2. Platform world/channel/character directory data and bounded player selection intent;
3. one-time Game Login Ticket issuance for the selected gameplay attempt;
4. Platform-owned Game Gateway ticket redemption, bounded supported protocol offer where applicable, World Registry route selection and returned selected endpoint/channel/revisions plus short-lived pre-admission session/admission material;
5. FND-02 `protocol-oteryn` transport/bootstrap to the Gateway-selected endpoint using only the selected route/revision context;
6. final game-owned FND-04 admission, `CharacterLease` acquisition/validation and canonical `GameSessionId` authority.

Platform directory responses MUST NOT be reinterpreted as gameplay credentials, Gateway authorization or final game-domain authority. A client MUST NOT bypass Game Gateway ticket redemption/route selection by turning directory selection directly into FND-04 admission or a direct gameplay endpoint choice.

### 7.1 Current Platform-directory parser precision

The current implementation in `crates/platform-client/src/lib.rs` does **not** provide complete-schema or generic unknown-gameplay-field rejection. It recursively rejects only these 12 literal JSON key names:

```text
host
port
endpoint
endpoint_uri
protocol
protocol_profile
ticket
credential
game_session
admission
route
address
```

Unknown compound keys such as `game_session_id`, `admission_token` or `selected_endpoint` are not proven rejected by that denylist and may be ignored by the current manual parser when the otherwise required directory shape is valid. Documentation and conformance evidence MUST describe the current behavior at exactly this scope.

Before a future implementation may claim a complete directory-schema boundary against unknown gameplay-shaped fields, it MUST provide explicit schema/allowlist or equivalent reject-unknown-field evidence that closes that gap. This is a future implementation requirement; this paper contract does not modify `platform-client` runtime code.

The conceptual fresh-entry flow is:

```text
Platform Identity
  -> bounded Platform directory + player selection intent
  -> one-time Game Login Ticket
  -> Platform-owned Game Gateway
       -> redeem ticket through Platform authority
       -> consume bounded supported protocol offer where applicable
       -> apply World Registry route/channel policy
       -> select endpoint/channel/revisions
       -> return short-lived pre-admission session/admission material
  -> establish FND-02 protocol-oteryn transport/bootstrap to the selected endpoint
  -> final game-owned FND-04 admission
       -> validate/consume pre-admission material and route/revision bindings
       -> acquire/validate CharacterLease
       -> create/replace canonical GameSession authority only on successful final admission
  -> synchronized non-authoritative client projection
```

Opening the selected transport or presenting valid Gateway material is not final gameplay admission. Platform/Gateway remain the pre-admission/control-plane boundary; final `GameSessionId`/`CharacterLease` gameplay authority remains in the Oteryn-v2 game domain under FND-04.

This contract does not freeze the future API/token/route representation at those seams.

## 8. Local gameplay-session observation contract

Client session state is an observation/progress model only.

The client MAY record that it is locally:

- requesting admission;
- connecting;
- synchronizing;
- active under an observed binding;
- reconnecting/resynchronizing;
- terminally rejected/disconnected.

Those states MUST NOT independently create, extend, resume or replace server-owned gameplay authority.

An open socket MUST NOT mean “gameplay active”. A selected character MUST NOT mean “lease acquired”. A cached `GameSessionId` MUST NOT mean “session resumable”. The owning server/admission contract remains authoritative.

## 9. Gameplay protocol egress contract

Future protocol egress MAY accept only semantic client/player intent from the application boundary.

Before encoding/sending an authority-relevant command, the client MUST have positive local evidence of the binding/phase required by FND-02/FND-04 and MUST satisfy parent protocol resource/shape limits.

Client-side legality/UX checks are advisory/bounding checks. They MUST NOT replace server gameplay legality.

`CommandId`, command ordering, retry, duplicate and terminal-result semantics MUST follow accepted FND-02/FND-03/FND-04 contracts and MUST NOT be redefined by UI/input code.

Raw OS key codes, widget callbacks and renderer events MUST NOT be serialized directly as protocol commands.

## 10. Gameplay protocol ingress and reconciliation contract

Before a server observation can alter the client world projection, the future ingress path MUST enforce all applicable accepted boundaries, including:

1. bounded frame/schema/type/phase validation;
2. active `connection_generation` fencing;
3. `server_sequence` rules where applicable;
4. typed state-domain revision preconditions;
5. snapshot begin/chunk/commit barriers where applicable;
6. accepted protocol resource ceilings.

Stale-generation server traffic MUST NOT mutate the active projection.

A state delta MUST be applied only when the client's current domain revision equals its required `base_revision`. A mismatch MUST cause the accepted reconciliation/resync behavior. The client MUST NOT fabricate missing authoritative deltas or skip unknown authoritative state.

An incomplete/invalid replacement snapshot MUST NOT partially replace the active authoritative-observation baseline.

## 11. Non-authoritative client projection contract

The interactive client MUST maintain a representation that is explicitly non-authoritative from the server/gameplay perspective.

The representation MUST distinguish:

- state observed from accepted server protocol messages;
- purely local presentation/UI state;
- any future speculative presentation state.

Local presentation state MAY include camera/layout/selection/interpolation/pending-indicator data. It MUST NOT advance or synthesize authoritative `server_sequence`, state-domain revision, command result, GameSession/lease or durable gameplay state.

This candidate does not authorize a prediction/rollback algorithm and does not promote the current synthetic `client-domain` / `client-simulation` crates into production.

## 12. Input contract

Physical/OS input MUST pass through a semantic action boundary before application/gameplay handling.

The application MAY route a semantic action to:

- UI/navigation;
- text/IME editing;
- settings/accessibility;
- future gameplay intent when gameplay is actually available.

Focus/modal/text-entry routing MUST prevent the same physical event from accidentally becoming both UI text/navigation and an unintended gameplay command unless explicitly designed and tested.

Exact keybind/controller/accessibility policy is deferred.

## 13. Renderer/UI contract

Renderer/UI code MUST consume client view/projection state and MUST NOT own gameplay admission, transport or server-authoritative mutation.

Renderer-local caches and GPU resources MUST be reconstructable without creating gameplay rights or changing authoritative observation state.

The Windows interactive shell MUST keep OS/window/surface lifecycle handling at the platform adapter boundary, including implementation-appropriate handling of resize/DPI/focus/suspend/resume/device/surface loss/shutdown.

The exact UI toolkit and renderer implementation remain unfrozen by this candidate.

### 13.1 Audio presentation contract

Audio is a client-side **presentation-only** subsystem. It MUST NOT own or decide gameplay legality, authoritative simulation, RNG, combat outcomes, timers, session/admission state or server reconciliation. Audio cues MAY be derived from already-accepted client observations and local presentation/UI events, but loss or delay of audio MUST NOT alter the authoritative or client-observed gameplay state machine.

The `apps/client` production composition root MUST own audio-provider construction, selected output-device/session lifetime, ordered shutdown and recovery. Screens, widgets and gameplay reducers MUST NOT open devices or own long-lived audio infrastructure directly.

Audio assets MUST come only from the same client-safe content/release projection boundary used by the shipping client. Audio lookup/activation MUST be compatible with the active build/content/release revision; an incompatible or missing required audio asset MUST fail/degrade as presentation rather than reinterpret content semantics or authorize gameplay. Staged release/content updates MUST NOT mutate the active audio asset set in place for a running release/session compatibility context.

The implementation MUST bound audio resource use, including simultaneously active voices/streams, decoded/streaming buffers, queued events and retry/reopen work. Exact numeric ceilings are implementation/evidence-driven and are deliberately not fixed here. Device loss, initialization failure, unsupported format or unavailable output MUST degrade to a clear recoverable/muted presentation state; gameplay entry and server authority MUST NOT depend on audio availability.

Settings/accessibility MUST expose the semantic controls needed by product requirements, including at least master/effect/music class controls or an equivalent extensible category model, mute, selected output where supported, and accessibility-safe operation when audio is disabled. Exact UX and category taxonomy remain product/implementation decisions.

Audio conformance evidence belongs to the native-client implementation/test owner. It MUST prove provider/device lifecycle and recovery, bounded-resource behavior, client-safe asset/revision compatibility, deterministic mapping from eligible presentation events to requested cues where determinism is claimed, settings persistence/accessibility behavior, and non-interference with gameplay authority. This candidate intentionally does **not** select an audio library, codec stack, mixer, OS backend or vendor.

## 14. Client-safe content contract

The client MUST consume only the DUR-04-approved client-safe projection of content/world semantics.

Client release/content activation MUST:

- verify artifact integrity through the accepted release/content mechanism;
- verify required build/protocol/content/capability compatibility metadata;
- fail closed on incompatible required semantics;
- prevent server-only data from entering the client merely to be UI-hidden;
- keep activated gameplay-relevant content immutable for the active compatibility/session context.

A staged update MUST NOT mutate the active gameplay content projection in place.

Gameplay-relevant hot reload is not authorized by this candidate.

Physical bundle encoding, patch/delta format, CDN and signing implementation remain with their owning programmes.

## 15. Configuration and filesystem contract

The client filesystem model MUST distinguish at least:

```text
installed immutable release payload
durable per-user configuration/privacy state
rebuildable cache/staging state
bounded diagnostic/crash spool
```

OS-specific paths MUST be resolved by the platform/filesystem boundary, not hard-coded throughout application/UI logic.

Durable client configuration MUST be versioned and migration-aware. Writes/migrations MUST avoid leaving a partially updated configuration as the only recoverable copy.

A normal update/restart/settings migration MUST NOT silently re-enable diagnostics after the user has disabled them unless a separately accepted privacy decision explicitly requires a new choice.

Reusable credentials, gameplay admission material and reconnect secrets MUST NOT be written to general configuration, logs, content cache or crash spool.

Exact directories, registry behavior, install scope and credential-vault technology are deferred.

## 16. Logging and crash diagnostics contract

Client logging/crash collection MUST follow an allowlist/data-minimization model.

Automatic eligible crash diagnostics MUST follow the accepted owner baseline:

- enabled by default;
- clear durable global opt-out;
- opt-out stops new automatic uploads and queued retries while disabled;
- opt-out cannot block client startup/authentication/gameplay;
- opt-out is not adverse security/abuse evidence;
- local redaction/allowlisting occurs before transmission;
- report/attachments are bounded;
- reusable credentials/tokens, private chat, arbitrary user files and unrelated personal data are excluded.

Client diagnostic evidence MUST remain optional corroborating evidence. It MUST NOT weaken, suppress or replace required server-side authoritative/security evidence.

Exact retention/deletion, upload transport/backend and crash package schema are deferred.

## 17. Release/update/install contract

### 17.1 Running-release immutability

An active authority-bearing gameplay process MUST NOT replace its own executable or gameplay-relevant release/content semantics in place.

Release activation MUST occur at a safe lifecycle boundary outside the active gameplay session/process mutation path.

### 17.2 Verification

Before external alpha, a candidate release MUST be verified according to the separately accepted signed-artifact/updater and provenance/SBOM policy before activation.

This candidate does not define the cryptographic/signing/vendor implementation.

### 17.3 Atomicity

Release activation MUST prevent a mixed partial version from being treated as valid. The activation mechanism MUST yield either:

- a complete verified candidate release; or
- retention/recovery of a complete verified prior release.

Rollback MUST NOT bypass current Platform/protocol/content compatibility policy merely because an older payload exists locally.

### 17.4 User state separation

Update/install/uninstall mechanics MUST keep release payload identity separate from per-user settings/cache/diagnostics. Destruction/migration of user data requires an explicit product/retention action rather than being an accidental side effect of binary replacement.

Installer/updater technology remains deferred.

## 18. Windows-first platform contract

The first interactive product target remains Windows-first `x86_64-pc-windows-msvc`.

Windows-specific concerns MUST be contained at shell/platform adapters where practical, including:

- event loop/window lifecycle;
- DPI/monitor/focus/text/IME behavior;
- filesystem known-folder/permission resolution;
- process handoff for update/install activation;
- crash integration;
- later selected package/signature UX.

This boundary MUST NOT be represented as a commitment to Linux/macOS parity. It exists to keep application/session logic independent of unnecessary Win32 details and testable without a window where appropriate.

## 19. Headless and interactive test contract

The accepted ADR-0007 tiers remain distinct.

### 19.1 Tier 1 headless system E2E

The future headless system client MUST:

- traverse the supported Platform Identity -> Game Login Ticket -> Game Gateway -> selected route/pre-admission -> gameplay transport/protocol -> final FND-04 game-domain admission/server boundaries;
- use the same accepted production protocol schemas/codecs, sequencing and admission contracts as the product client where useful;
- emit normal player intent/commands;
- expose deterministic semantic observations;
- never call authoritative game-domain mutation APIs directly.

Shared production schemas/codecs MAY be reused by Tier 1, but they MUST NOT be the only oracle for wire correctness. Tier-1/future protocol evidence MUST consume the independent-proof property required by FND-02 and the owner-accepted 2026-08-07 refinement, including as applicable:

- canonical byte-level golden fixtures for framing/messages;
- malformed/adversarial corpus coverage;
- property/invariant encode/decode round-trip tests;
- fuzzing of externally controlled framing/decoders/parsers;
- cross-version compatibility fixtures for permitted same-major evolution;
- explicit resource ceilings and stable failure classes/dispositions.

This requirement is for independent evidence against common-mode codec defects. It MUST NOT be interpreted as requiring or authorizing a second production protocol implementation or duplicated production stack.

The current `tools/synthetic-client-harness` MUST NOT be reported as Tier 1 system E2E under its current synthetic/no-production-network classification.

### 19.2 Tier 2 native-client E2E

A test-only native-client adapter MAY invoke normal input/client-command paths and read semantic observations/UI/frame/log evidence.

It MUST NOT:

- forge Platform/Game Sessions;
- teleport or mutate server-owned state;
- inject authoritative snapshots/results;
- bypass normal networking/protocol/server legality;
- ship in production-default builds.

### 19.3 Tier 3 release binary

Release-candidate proof MUST run the actual packaged product artifacts without the Tier 2 in-process adapter and prove the named product journey required by ADR-0007 once gameplay exists.

A window-only smoke test MUST NOT be reported as gameplay E2E.

## 20. Player-facing failure-state contract

Without exposing credentials or hidden topology, the client MUST be able to present bounded distinct states for applicable future failures including:

- gameplay runtime unavailable;
- version/content incompatibility;
- maintenance/queue/readiness state when supplied by owning authority;
- session/lease conflict;
- transport connection/security failure;
- reconnect/resynchronization progress;
- terminal gameplay-session failure;
- update required/activation failure;
- audio unavailable/degraded where audio is implemented.

A lower-level socket error MUST NOT automatically become a security downgrade or a claim that the server ended/accepted gameplay authority. Error mapping must respect the owning contract.

## 21. Shutdown contract

Shutdown MUST be coordinated by the production composition root.

It MUST:

1. stop accepting new user/gameplay intents;
2. cancel/close application-owned asynchronous work through bounded ownership;
3. close/release future transport/session client resources without inventing server success;
4. stop/release audio playback/device resources without blocking gameplay/session authority cleanup;
5. flush only bounded, policy-permitted local state/diagnostics;
6. release renderer/window resources;
7. terminate without orphaned client worker ownership.

Exact timeout values are implementation/SRE decisions unless already fixed by a parent contract.

## 22. Readiness contract

The following statuses MUST remain distinct:

```text
architecture accepted
implementation present
implementation proven at exact revision
production/external-alpha enabled
```

### 22.1 Current pre-native readiness

The current shell MAY claim only the capabilities proven by the migrated baseline. It MUST NOT claim native gameplay readiness.

### 22.2 Native gameplay enablement

A product build MUST NOT change gameplay availability to enabled until exact-revision evidence proves, together:

- ADR-0003-compatible Platform Identity/Game Login Ticket/Game Gateway route/pre-admission client integration;
- gameplay transport client implementation to the Gateway-selected endpoint;
- FND-04 final game-owned admission/reconnect and `CharacterLease` integration without moving canonical GameSession authority to Platform/Gateway;
- FND-02 codec/registry/reconciliation implementation;
- authoritative server counterpart;
- compatible client-safe content projection;
- native client projection/input/render integration;
- required Tier 1 and Tier 2 E2E journeys with FND-02 independent wire evidence.

Audio implementation is not gameplay-authority readiness. When audio is in the shipped alpha scope, its independent provider/content/degradation/settings evidence MUST be satisfied without making gameplay availability depend on the presence of an output device.

### 22.3 External alpha

External-alpha production enablement additionally requires accepted release/security/SRE/privacy evidence, including signed artifact/updater strategy and implementation, build provenance/SBOM strategy, threat model, rollback/operability, required runbooks/SLOs and Tier 3 release-binary evidence.

Coordinator acceptance of this document alone satisfies none of those implementation/proof gates.

## 23. Required future evidence

Implementation claiming conformance to this candidate should prove at minimum:

1. application/screen code cannot bypass provider/capability gates to create gameplay network activity while runtime is unavailable;
2. current Platform directory parsing recursively rejects the 12 literal denylisted keys `host`, `port`, `endpoint`, `endpoint_uri`, `protocol`, `protocol_profile`, `ticket`, `credential`, `game_session`, `admission`, `route`, `address`; any stronger complete-schema/reject-unknown-fields claim is made only after explicit evidence for that stronger implementation, and directory handling cannot bypass the ADR-0003 Game Login Ticket -> Game Gateway redemption/route-selection boundary;
3. fresh gameplay entry follows the authorized chain through selected endpoint/channel/revisions and short-lived pre-admission material before final FND-04 admission, while final `GameSessionId`/`CharacterLease` authority remains game-owned;
4. stale `connection_generation` traffic cannot mutate the active projection;
5. state revision mismatch enters resync and never applies a speculative authoritative delta;
6. incomplete snapshot cannot become active world state;
7. canonical byte-level protocol/framing golden fixtures provide an independent wire oracle rather than only shared production-code round trips;
8. malformed/adversarial corpus and property/invariant tests cover bounded decode/encode semantics;
9. externally controlled decoders/parsers are fuzzed under explicit resource ceilings and stable failure classes;
10. cross-version fixtures prove permitted same-major compatibility without duplicating the production protocol stack;
11. semantic input routing prevents UI/text events from unintended gameplay egress;
12. renderer/device/resource recreation does not alter gameplay/session authority;
13. incompatible client-safe content fails closed before world activation;
14. audio provider/device lifecycle, bounded-resource behavior, compatible client-safe audio assets, non-authoritative cue mapping, degradation/recovery and settings/accessibility behavior are proven when audio is implemented;
15. config migration is recoverable and preserves diagnostic opt-out;
16. logs/crash packages reject/redact prohibited secret/private data before upload;
17. update activation cannot launch an accepted mixed partial release and rollback remains compatibility-checked;
18. Tier 1 headless, Tier 2 native and Tier 3 release evidence are classified distinctly with exact build/Platform/protocol/content revisions retained;
19. no hidden retry converts failed physical E2E attempts into pass evidence;
20. exact-head implementation review and CI prove the claimed build, not a parent commit.

## 24. Decision timing

### Must these boundaries be decided now?

**YES** for composition/authority/projection/content/filesystem/update/test/audio-ownership boundaries. Client implementation would otherwise hard-code cross-domain ownership before the missing gameplay runtime exists.

**NO** for the concrete GUI/network/updater/installer/content-packaging/audio libraries. Those choices remain safely reversible and require implementation evidence.

### Downstream work blocked without this contract

- safe native gameplay client implementation after ADR-0003/FND-02/FND-04 runtime integration exists;
- stable UI/navigation/provider composition;
- client content loader/update packaging work;
- client audio provider/content/settings implementation without authority leakage;
- Tier 2 native-client automation design;
- honest external-alpha client readiness gate.

### What becomes expensive if delayed

- direct screen-to-network coupling;
- UI state accidentally becoming gameplay state authority;
- direct screen/reducer ownership of audio devices and unbounded playback queues;
- irreversible loose-content/file layouts;
- updater/install mutation mixed into the gameplay process;
- test hooks that bypass product boundaries;
- unsupported transport settings becoming user-visible compatibility promises.

### Superseding evidence

A future change may supersede these boundaries only with explicit accepted evidence showing an alternative preserves or improves:

- server/gameplay authority separation;
- protocol revision/reconciliation safety;
- content allowlisting/compatibility;
- credential/privacy isolation;
- release atomicity/rollback;
- real-boundary E2E proof;
- presentation/audio non-authority and resource boundedness;
- implementation simplicity/operability on measured production constraints.

Framework preference alone is insufficient superseding evidence.

## 25. DECISIONS_NOT_TAKEN

This candidate intentionally does not select:

- exact UI toolkit or renderer replacement;
- exact Rust trait/module/crate layout for proposed ports;
- promotion/replacement of synthetic client-domain/simulation crates;
- gameplay prediction/interpolation/rollback semantics;
- gameplay transport adapter implementation or TCP/QUIC activation;
- QUIC library/profile/fallback timing/default;
- Game Gateway/admission/reconnect credential/API representation;
- protocol/TLS/protobuf implementation libraries;
- client bundle/patch/CDN format;
- installer/updater framework or code-signing provider;
- Windows directory/registry/install-scope details;
- credential vault technology;
- crash backend/retention/legal text;
- audio library, codec/mixer stack, device backend/vendor or exact category taxonomy;
- release channel/version-skew/forced-update product policy;
- Linux/macOS support plan;
- exact numeric retry/cache/log/spool/audio-voice/buffer limits outside accepted parent contracts;
- any server/gameplay/persistence/balance authority.

## 26. CROSS_DOMAIN_FINDINGS

Normative cross-domain findings for this worker remain in the companion analysis section `CROSS_DOMAIN_FINDINGS`. They are `REPORT_ONLY` and do not grant this contract authority to solve those owner domains.

## 27. Acceptance boundary

If accepted by the Architecture Coordinator, this candidate should become the client implementation baseline for ALPHA-CLIENT-01 while all runtime implementation remains `NOT_STARTED` until separately authorized tasks provide exact code and proof.

`MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`