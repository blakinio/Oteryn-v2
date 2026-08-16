# Oteryn v2 — Implementation Executor DAG

- Programme ID: `OTV2-NATIVE-IMPLEMENTATION`
- Status: `PREPARED / HOLD` until Stage-C acceptance delivery is merged and lifecycle/status reconciliation is complete.
- Canonical repository: `blakinio/Oteryn-v2`.
- External repositories: read-only unless separately owner-authorized.
- Production/protected-environment/live-data authority: **NONE**.
- Reference parity authority: **NONE**.

## 1. Purpose

This programme converts the accepted Oteryn-v2 architecture into a bounded implementation sequence without allowing workers to make unresolved architecture decisions inside code.

The implementation is coordinator-led and dependency-driven. Workers do not choose final crate/service topology before the bootstrap cutover establishes real repository paths and machine-enforced ownership.

## 2. Global invariants

Every lane MUST preserve:

- native Rust client/server stack and one `protocol-oteryn` gameplay protocol;
- server-authoritative legality, ordering, movement, combat, items and value;
- FND-02 command/sequence/revision/resync semantics;
- FND-03 one logical authoritative mutation owner per runtime scope;
- FND-04 admission/GameSession/CharacterLease/fencing semantics;
- DUR-01/02/03 durability, idempotency, anti-duplication and crash-recovery semantics;
- DUR-04 content/compiler/bundle/script authority and final-format evidence gate;
- SIM deterministic numeric/RNG/order/replay requirements;
- accepted GAME-ABILITY / GAME-INTERACTION / GAME-AI / ALPHA-CLIENT / ANL contracts;
- accepted Stage-C movement/combat/content contracts once merged;
- QA-E2E real-boundary proof rules;
- `PROVEN / DERIVED / UNKNOWN / CONFLICT` evidence discipline;
- no Codex/owner-funded AI without exact authorization for that use;
- no production, Platform write, protected secrets, live account/session/data or external-repository mutation without separate explicit authority.

Reference-unknown behavior MUST remain fail-closed or use an explicitly test-only non-shipping fixture profile. A fixture is never Reference parity evidence.

## 3. Why bootstrap is serial

Current `main` is intentionally `pre-native-protocol`:

- only `apps/client` exists as an application;
- `workspace-boundaries.toml` enumerates exactly 19 current members;
- `tools/architecture-check` requires exactly that pre-native shape;
- current policy forbids package-name fragments including `protocol-oteryn`, `transport`, `game-session`, `game-server`, `persistence`;
- Rust CI contains client-only negative closure checks;
- FND-02 registry intentionally has empty gameplay `command_types`, `state_domains` and capabilities;
- game-event registry intentionally has no domain event types.

Therefore the first implementation PR MUST be an atomic, reviewed transition from the pre-native policy to a real immediate-consumer implementation shape. Creating speculative empty crates first is forbidden.

## 4. Canonical DAG

```text
OTV2-IMPL-COORD
  |
  v
OTV2-IMPL-BOOTSTRAP                         SERIAL GATE
  |
  +--> OTV2-IMPL-FOUNDATION                 protocol/runtime/admission
  +--> OTV2-IMPL-DURABILITY                 persistence substrate
  +--> OTV2-IMPL-CONTENT                    minimum VSL compiler/loader
  +--> OTV2-IMPL-CLIENT                     native gameplay integration seam
  +--> OTV2-IMPL-QA                         real-boundary test platform
          |
          v
      OTV2-IMPL-MOVE                        first authoritative movement slice
          |
          v
      OTV2-IMPL-COMBAT                      death/loot/XP/pickup slice

OTV2-CONTENT-FORMAT-SPIKE                   evidence-only after content seam
OTV2-IMPL-ANALYTICS                         later, after producer event families exist
```

The coordinator MAY overlap Foundation, Durability, Content, Client and QA only after bootstrap has merged and an exact path/allocation record proves their owned paths do not overlap. Movement and Combat remain serial integration gates unless the coordinator proves a narrower non-overlapping decomposition.

## 5. Lane contract — `OTV2-IMPL-BOOTSTRAP`

### Goal

Create the first real server-side implementation shape and update repository policy/tooling atomically so accepted FND implementation has immediate consumers and CI can validate it.

### Must own

The coordinator allocates exact paths. The lane normally includes the minimum necessary set from:

- root Cargo workspace membership/dependencies;
- `workspace-boundaries.toml`;
- `tools/architecture-check` policy model/tests;
- Rust/merge CI assumptions affected by moving beyond pre-native state;
- minimum real server application/composition root and immediate-consumer crates required by accepted FND contracts;
- nearest `AGENTS.md` files for newly high-risk ownership areas;
- focused bootstrap tests and migration/readiness documentation.

### Must not do

No gameplay movement/combat/content semantics, no PostgreSQL production schema, no broad client gameplay enablement, no final content format, no fake protocol adapter, no placeholder crate with no real consumer.

### Completion

A merged bootstrap head must make the new workspace shape truthful and machine-enforced, with build/test/Clippy/supply-chain CI green. Pre-native guards removed or narrowed only where superseded by real accepted implementation; Canary remains absent.

## 6. Lane contract — `OTV2-IMPL-FOUNDATION`

Implement the minimum FND-ID/FND-02/FND-03/FND-04 stack necessary for a real local game-server endpoint and native client/server test path:

- typed identifiers;
- FND-02 foundation schema/codegen/codec/framing/TLS profile and resource limits;
- CommandRef, connection generation, server sequence, state revision, snapshot/delta/resync foundation;
- authoritative runtime owner/lane/lifecycle scaffolding;
- admission/GameSession/CharacterLease/reconnect fencing;
- typed foundation errors and failure scenarios;
- no gameplay command/state IDs invented by this lane unless an owning domain contract is integrated in the same coordinator-approved boundary.

Protocol/admission/session changes are high risk and require genuinely independent final review plus negative/replay/fencing evidence.

## 7. Lane contract — `OTV2-IMPL-DURABILITY`

Implement only accepted profile-neutral durability needed by the first slice:

- durable ID representation;
- PostgreSQL migration/test substrate where explicitly implementation-authorized;
- Character/session/value transaction abstractions required by FND and VSL;
- DUR-03 stable transaction/idempotency/reconciliation/anti-dup semantics;
- outbox/audit coupling where mandatory;
- isolated migration, rollback, concurrency and crash-recovery tests.

No market/bank/depot/entitlement breadth. Physical schemas must not encode unresolved Reference formulas or generic misc-state escape hatches. High-risk persistence/value changes require genuinely independent review.

## 8. Lane contract — `OTV2-IMPL-CONTENT`

Implement the minimum typed canonical semantic graph and deterministic compiler/loader seam required by Stage-C:

- stable content keys/revisions/provenance;
- bounded synthetic/VSL content fixture builder/source;
- deterministic server-authoritative and allowlisted client-safe projections;
- `VSL_BUNDLE_EVIDENCE_PROFILE` or equivalent explicitly non-production evidence artifact;
- corruption/oversize/incompatibility rejection;
- staged all-or-nothing activation;
- movement collision/local-relocation, one creature/spawn, one ability, one loot table, one XP fixture, one materializable item and required presentation data.

The lane MUST NOT select permanent World Project/Bundle encoding. That remains the content-format spike + owner format decision.

## 9. Lane contract — `OTV2-IMPL-CLIENT`

Implement native gameplay integration only after the production FND seam is real:

- client protocol transport/codec consumer;
- admission/session/reconnect integration;
- semantic input to typed command intent;
- authoritative state-domain projection/reconciliation;
- bounded settings/diagnostics/privacy behavior;
- no client-authoritative movement/combat/item/value;
- fail-closed gameplay capability until compatible server/content/runtime requirements are present.

Tier-2 evidence is mandatory for supported native-client journeys; production-binary claims require Tier 3 where the milestone requires it.

## 10. Lane contract — `OTV2-IMPL-QA`

Implement the smallest real-boundary QA-E2E platform required to prove foundation and VSL work:

- deterministic scenario/evidence model;
- exact artifact/revision/seed/topology/fault evidence;
- Tier 1 server/protocol/persistence journeys;
- Tier 2 instrumented native-client journeys;
- cleanup and failure evidence;
- no mock success accepted as terminal proof;
- no test adapter in production artifacts.

QA may start after real production wire/runtime seams exist and should provide harness primitives before Movement/Combat terminal acceptance.

## 11. Lane contract — `OTV2-IMPL-MOVE`

Implement the accepted Stage-C movement slice:

- owner-local authoritative step and same-scope relocation;
- static exact-revision collision/spatial legality;
- current-runtime dynamic legality;
- stable movement occurrence lineage;
- post-movement GAME-INTERACTION children;
- bounded deterministic visibility/interest state domain;
- typed FND-02 command/result/state registration owned jointly with this domain;
- client intent/reconciliation only;
- deterministic component tests plus real Tier 1/Tier 2 evidence.

Cross-Channel/Instance handoff remains outside the local movement slice unless separately allocated under accepted FND/Channel authority.

## 12. Lane contract — `OTV2-IMPL-COMBAT`

Implement the accepted first creature combat/death/value slice:

- GAME-ABILITY as the only combat effect pipeline;
- one stable creature death occurrence per lifecycle generation;
- deterministic loot selection using purpose-isolated SIM RNG and exact content revisions;
- DUR-03 stable durable loot materialization and ambiguity reconciliation;
- separate idempotent single-principal GAME-CHAR XP settlement;
- GAME-INTERACTION + GAME-ITEM + DUR-03 pickup;
- authoritative client results/state projection;
- typed protocol registrations owned with the domain;
- crash/lost-response/retry/no-dup tests plus Tier 1/Tier 2 evidence.

Use only explicit non-shipping fixture formula/rate values until Reference evidence is promoted. No PvP/party/boss/market breadth.

## 13. Evidence lane — `OTV2-CONTENT-FORMAT-SPIKE`

This is an evidence-producing implementation experiment, not a permanent-format implementation authorization.

Compare bounded candidate physical representations against accepted DUR-04/ADR-0005 criteria: deterministic output, source-control diffability, partial/atomic authoring, bounded parsing/decompression, streaming locality, patchability, compatibility, corruption recovery and tooling ergonomics. Keep benchmark fixtures legally safe. Produce a decision dossier; do not silently ship the winning prototype as canonical format before owner acceptance.

## 14. Later lane — `OTV2-IMPL-ANALYTICS`

Do not start as a full analytics implementation while `GAME_EVENT_FOUNDATION_REGISTRY.json` has no concrete domain producer families.

After Foundation/Move/Combat/DUR lanes register typed producer events, implement read-only ANL-02/03 ingestion/quality/invariant/reporting slices. Analytics must never mutate gameplay, sanction players or invent producer authority. Missing/partial evidence remains fail-closed for regression/integrity conclusions.

## 15. Coordinator responsibilities

`OTV2-IMPL-COORD` MUST:

1. read live main and this programme before every allocation wave;
2. maintain one canonical implementation allocation/status record with exact branches, PRs, owned paths, dependencies and merge order;
3. serialize public-contract/registry/workspace-policy mutations;
4. prevent two workers from owning the same path or stable ID range concurrently;
5. merge only exact-head validated PRs under repository policy;
6. require high-risk independent reviews where root `AGENTS.md` requires them;
7. run real-boundary E2E before marking a VSL implementation `PROVEN`;
8. never convert architecture acceptance into Reference parity or production enablement;
9. keep `PROD-ENTITLEMENTS-01` excluded until separately accepted;
10. stop on a genuinely unresolved owner/authority decision rather than letting a worker improvise.

## 16. Suggested invocation order

After this programme is released by a merged prompt-package delivery:

```text
1. Oteryn: implementation coordinator
2. Coordinator runs OTV2-IMPL-BOOTSTRAP serially
3. Coordinator releases Foundation / Durability / Content / Client / QA as dependencies permit
4. Coordinator releases Movement
5. Coordinator releases Combat
6. Coordinator may release Content Format Spike and later Analytics when prerequisites exist
```

The user should normally start only the coordinator. Direct worker aliases exist for recovery/manual allocation but MUST verify an active coordinator allocation naming their exact lane and paths before writing.

## 17. Completion truth

`architecture accepted` != `implementation complete` != `Reference parity` != `production ready`.

A lane is complete only when its owned implementation, focused tests, required integration/E2E, independent review where applicable, exact-head CI, merge, task archive and ownership release are all terminally complete.
