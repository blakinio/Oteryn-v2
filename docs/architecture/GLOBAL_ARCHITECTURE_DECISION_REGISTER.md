# Oteryn v2 Global Architecture Decision Register

- Status: **Active coordination register**
- Date: 2026-08-17
- Coordination ID: `OTV2-GLOBAL-ARCHITECTURE`
- Current execution status: `docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md`
- Detailed gameplay/product horizon: `docs/architecture/GAMEPLAY_AND_PRODUCT_ARCHITECTURE_HORIZON.md`
- Stable foundation backlog: `docs/architecture/FOUNDATION_DECISION_BACKLOG.md`

## 1. Purpose and precedence

This register preserves stable architecture gate IDs, their current decision role and the boundary between accepted architecture and later implementation/proof work.

Use with `ARCHITECTURE_STATUS_MODEL.md`:

```text
DecisionStatus != DeliveryStatus != ImplementationStatus
```

Accepted ADRs/contracts/owner baselines are semantic authority. `FOUNDATION_PROGRAMME_CURRENT_STATUS.md` is current execution-status authority. Historical proposal/candidate/backlog prose remains history when superseded by a later owner acceptance.

## 2. Accepted platform/foundation direction

The following architecture is accepted for its named scope:

| Gate / domain | DecisionStatus | ImplementationStatus | Canonical source / note |
|---|---|---|---|
| Native Rust client/server + project `protocol-oteryn` | `ACCEPTED` | mixed / gated | ADR-0001 |
| Repository ownership / client migration | `ACCEPTED` | `PROVEN` cutover | ADR-0002 + FND-01/VSL-02 |
| Platform Identity / Game Gateway / final game admission split | `ACCEPTED` | `NOT_STARTED` game runtime | ADR-0003 + FND-04 |
| PostgreSQL game ownership separation | `ACCEPTED` | `NOT_STARTED` physical game schema | ADR-0004 + DUR contracts |
| Native world/content format + Oteryn Studio boundary | `ACCEPTED` | `NOT_STARTED` executable content stack | ADR-0005 + DUR-04 |
| Game Intelligence / analytics / audit read-only direction | `ACCEPTED` | `NOT_STARTED` analytics runtime | ADR-0006 + ANL contracts |
| Native three-tier E2E evidence platform | `ACCEPTED` | `NOT_STARTED / EVIDENCE_REQUIRED` | ADR-0007 / QA-E2E-01 |
| `protocol-canary` reference-only | `ACCEPTED` | excluded from production graph | ADR-0008 |
| GameNode process / one-writer baseline | `ACCEPTED` | `NOT_STARTED` runtime | ADR-0009 + FND-03 |
| Reference/Evolved worlds over one engine/protocol | `ACCEPTED` | `NOT_STARTED` broad profile runtime | ADR-0010 |
| Fail-closed pre-native client state | `ACCEPTED` | currently applicable until implementation cutover | ADR-0011 |
| Character authority / Platform lifecycle split | `ACCEPTED` | `NOT_STARTED` native Character runtime | ADR-0012 |
| Platform DB independence from game PostgreSQL | `ACCEPTED` | policy | ADR-0013 |
| TCP-default / future QUIC-opt-in one-protocol strategy | `ACCEPTED` | transport runtime `NOT_STARTED` | ADR-0014 + NET-TRANSPORT-01 |
| GameNode internal shape evidence-driven | `ACCEPTED` | topology not frozen | ADR-0015 |
| Transport-mode vocabulary != runtime readiness | `ACCEPTED` | gameplay modes remain implementation-gated | ADR-0016 |

## 3. Accepted foundation/durability/gameplay/client/analytics gates

| Gate | DecisionStatus | DeliveryStatus | ImplementationStatus |
|---|---|---|---|
| `FND-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `PROVEN` |
| `VSL-02` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `PROVEN` |
| `FND-ID-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `FND-02` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `NET-TRANSPORT-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `FND-03` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `FND-04` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `DUR-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `DUR-02` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `DUR-03` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `DUR-04` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `ANL-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `GAME-VISION-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `GAME-CHANNEL-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `GAME-CHAR-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `GAME-ITEM-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `SIM-DETERMINISM-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `GAME-ABILITY-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `GAME-INTERACTION-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `ALPHA-CLIENT-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `GAME-AI-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `ANL-02` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `ANL-03` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `QA-E2E-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED / EVIDENCE_REQUIRED` |
| `VSL-MOVE-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `VSL-COMBAT-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |
| `VSL-CONTENT-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` |

First-wave acceptance is canonical through PR #309 / `bf2a2ae279516f62626a5d8f4dc1aeb587535c62`; its final task bookkeeping is consolidated into PR #314. Stage-C acceptance is canonical through PR #311 / `e0ea9ef87c01dec720a22e8df6d54bfd669cb62c`; independent exact-head review `4949739986` reported zero material findings; lifecycle/status closeout is PR #318 / `a6a5180d98cf7791e40d9e1d08b25a5c8b4eff96`.

## 4. Reference evidence/parity registry

Reference evidence/parity manifest v1 is accepted/pinned. Current `ABILITY_COMBAT` truth remains:

```yaml
target: Global Tibia after 2026-07-28 server-save boundary
registered_cases: 4
promoted_cases: 0
target_evidence: UNKNOWN
source_case_provenance: PENDING
legal_review: PENDING
oteryn_implementation: NOT_STARTED
parity: PARITY_PENDING_EVIDENCE
```

No architecture acceptance or prompt release may silently promote parity.

## 5. Registered product/alpha horizon

Stable registered gates remain visible even when they do not block the first technical slice:

| Gate | Current role / disposition |
|---|---|
| `VSL-01` | `PLANNED`; first technical vertical-slice proof programme |
| `VSL-MOVE-01` | `ACCEPTED / LIFECYCLE_CLOSED`; implementation not started |
| `VSL-COMBAT-01` | `ACCEPTED / LIFECYCLE_CLOSED`; implementation not started |
| `VSL-CONTENT-01` | `ACCEPTED / LIFECYCLE_CLOSED`; implementation not started |
| `VSL-02-NATIVE-CLIENT` | repository/native-client cutover context; runtime feature proof remains separate |
| `ALPHA-RULESET-01` | `REQUIRED_FOR_ALPHA` |
| `ALPHA-CONTENT-01` | `REQUIRED_FOR_ALPHA` |
| `ALPHA-CLIENT-01` | architecture `ACCEPTED`; runtime completeness not started |
| `ALPHA-GM-01` / `OPS-GM-01` | support/moderation/GM scope remains later product work |
| `ALPHA-QUALITY-01` | `REQUIRED_FOR_ALPHA` |
| `ALPHA-OPS-01` / `OPS-CHANNEL-01` | production operations/orchestration scope remains later work |
| `LIVE-OPS-01` / `PROD-LIVEOPS-01` | LiveOps/runtime configuration authority remains later work |
| `ALPHA-COMPAT-01` / `PROD-COMPAT-01` | release compatibility/version-train scope remains later work |
| `ALPHA-PRIVACY-01` / `DATA-PRIVACY-01` | product privacy/data lifecycle completion remains later work |
| `ALPHA-CLIENT-SEC-01` / `SEC-CLIENT-01` | client integrity/security boundary remains later work |
| `PERF-01` | measured resource/capacity/latency/headroom evidence remains required |
| `ANL-02` | architecture accepted; real coverage requires producer events and quality evidence |
| `ANL-03` | architecture accepted; real coverage requires producer events and quality evidence |
| `GM-01` | registered GM/support horizon |
| `PROD-ENTITLEMENTS-01` | `PROPOSED / PLANNED / NOT_STARTED`; game consumer/enforcement not accepted |

Detailed expansion/deferred scope remains in `GAMEPLAY_AND_PRODUCT_ARCHITECTURE_HORIZON.md`, including `GAME-META-01`, `GAME-INSTANCES-01`, `GAME-WORLD-LIFECYCLE-01`, `INTEGRATION-API-01`, `MOD-ECOSYSTEM-01`, `EXP-EVENTS-01`, `EXP-HOUSES-01`, `EXP-SOCIAL-01`, `EXP-ECONOMY-01`, `EXP-SECURITY-01`, `EXP-UPDATE-01`, `EXP-OPS-01`, `EXP-OBS-01` and `EXP-SCALE-01`.

Registration prevents omission; it does not authorize implementation.

## 6. Progressive execution policy

1. Do not re-open accepted architecture without named superseding evidence.
2. Proposal/candidate delivery is not owner acceptance.
3. Implementation may not choose unresolved authority, idempotency, durability, public protocol or persistent-value semantics.
4. Technology/library choices remain deferred when accepted architecture intentionally leaves them reversible.
5. Resource values come from accepted registries/PERF/OPS evidence, not arbitrary constants.
6. Cross-repository authority pins immutable merged revisions, not mutable PR heads.
7. Reference parity remains an evidence claim.
8. Permanent World Project/Bundle encoding still requires the DUR-04 format spike and later owner decision.
9. High-risk protocol/session/admission/persistence/item/loot/value/multichannel/fencing changes require genuinely independent exact-head review.
10. Entitlement implementation remains excluded until `PROD-ENTITLEMENTS-01` is separately accepted.

## 7. Released implementation handoff

When PR #314 merges, the evaluated implementation prompt package is released. Prompt release does not itself start implementation.

```text
EXECUTOR_PROMPTS: RELEASED
DEFAULT_ENTRYPOINT: Oteryn: implementation coordinator
DIRECT_WORKERS: ALLOCATION_GATED
IMPLEMENTATION_STARTED: NO
IMPLEMENTATION_AUTHORITY: NONE_UNTIL_OWNER_INVOCATION
```

After explicit owner invocation, the live implementation coordinator may create bounded implementation allocations in `blakinio/Oteryn-v2` under root governance. Production/protected-environment/live data/session/account, Platform, external-repository, entitlement, Reference-parity and owner-funded AI authority remain separately governed.
