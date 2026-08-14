# ANL-02 — Gameplay, Balance and World Analytics Contract Candidate

- Date: 2026-08-15
- Gate: `ANL-02`
- Issue: #264
- DecisionStatus: `CANDIDATE`
- DeliveryStatus: `IN_REVIEW`
- ImplementationStatus: `NOT_STARTED`
- Status on worker branch: **CANDIDATE / NONBINDING**
- Canonical semantic effect: only after Architecture Coordinator acceptance/merge under repository governance
- Runtime/client/Platform/PostgreSQL/production authority: **NONE**
- Merge authority: `ARCHITECTURE_COORDINATOR_ONLY`
- Analysis source: `ANL-02_GAMEPLAY_BALANCE_WORLD_ANALYTICS_ANALYSIS.md`

## 1. Purpose

Freeze the minimum consumer semantics required for trustworthy gameplay, balance and world/content analytics without selecting implementation technology or granting mutation authority.

ANL-02 owns:

- analytical metric-definition identity/versioning;
- observation/cohort/denominator semantics;
- evidence-quality representation;
- revision-aware comparison/regression semantics;
- privacy-safe gameplay/world analytical projections;
- bounded analytical evidence-package requirements.

ANL-02 does **not** own gameplay formulas, content rules, channel/reward policy, item/currency prevention, authoritative replay, sanctions, warehouse/DB technology, runtime implementation or production rollout.

## 2. Authority invariant

```text
ANL-02 output
= observation / comparison / hypothesis / reproducible evidence
!= gameplay authority
!= balance authority
!= content mutation authority
!= economy mutation authority
```

No ANL-02 metric, anomaly, model output or evidence packet may directly change authoritative gameplay state, ruleset/content, reward rates or production configuration.

## 3. Upstream contracts

A conforming ANL-02 consumer preserves:

- ADR-0006 data-class and read-only boundaries;
- ANL-01 EventId/schema/durability/privacy/retention/order/idempotency semantics;
- DUR-03 conservation/prevention authority when value facts are consumed;
- GAME-CHANNEL World/Channel/multiplicity semantics;
- SIM-DETERMINISM replay/state provenance when deterministic corroboration is claimed;
- owning gameplay/content semantics for every domain payload it interprets.

It must never invent a missing gameplay semantic from generic event fields or presentation logs.

## 4. Metric-definition identity

Every material metric has a stable logical `metric_id` and immutable positive `metric_revision`.

A metric definition declares at least:

1. purpose/analytical question;
2. semantic grain and unit;
3. aggregation operation;
4. required typed source event families and supported schema revisions;
5. required source durability/completeness class;
6. observation-window/time basis;
7. cohort dimensions;
8. denominator/exposure definition;
9. inclusion/exclusion rules;
10. sampling/weighting policy;
11. duplicate/order/late/missing-data handling;
12. mandatory semantic revision dimensions;
13. privacy floor and permitted projection purpose;
14. derived-dataset retention profile;
15. source-lineage/reproducibility requirements;
16. known confounders/interpretation limits.

A semantic change to any item above creates a new metric revision. Historical results retain the revision under which they were computed.

## 5. Observation contract

Every material observation binds:

```text
metric_id + metric_revision
observation window
WorldId
Channel/Instance scope policy when applicable
ruleset/content/world-policy revisions when material
server build/protocol revision when material
SIM profile/replay provenance when used
cohort/denominator definition revision
source event type/schema set
source checkpoint/window identity
sampling/loss/coverage summary
transform/query implementation revision or digest
sample/exposure size
result + unit
evidence-quality vector
privacy/retention/export classification
```

A value lacking required context is not a conforming decision-grade ANL-02 observation.

## 6. Evidence-quality vector

Every observation records explicit quality dimensions rather than only one opaque confidence score.

### Source completeness

- `PROVEN_COMPLETE_FOR_DECLARED_DURABLE_SCOPE`
- `NO_KNOWN_GAP_BEST_EFFORT`
- `PARTIAL`
- `UNKNOWN`

Only accepted durable source/checkpoint/event-set evidence may establish `PROVEN_COMPLETE_FOR_DECLARED_DURABLE_SCOPE`.

`NO_KNOWN_GAP_BEST_EFFORT` means no observed loss in the declared best-effort path; it is not conservation/security completeness.

### Schema compatibility

- `SUPPORTED`
- `MIXED_SUPPORTED_REVISIONS`
- `PARTIAL_UNSUPPORTED`
- `UNKNOWN`

### Required recorded dimensions

The observation additionally records:

- duplicate/order reconciliation status;
- sampling policy revision and weighting state;
- semantic revision homogeneity/stratification;
- material privacy suppression;
- source checkpoint/gap state.

Known source loss or unsupported semantics may not be hidden by an aggregate.

## 7. Cohort and denominator rules

1. Every comparative metric has an explicit denominator/exposure definition.
2. World/ruleset/profile is mandatory context for gameplay-value interpretation.
3. Reference and Evolved Worlds are separate cohorts unless an explicit comparison intentionally places them side by side; they are never silently pooled.
4. Incompatible ruleset/content/formula/metric revisions are stratified or rejected, not averaged into one homogeneous result.
5. Channel/Instance dimensions are included when they can alter exposure/simulation; Channel multiplicity does not imply independent durable reward/source multiplicity.
6. Solo/party, class/vocation, progression band, encounter/content and equipment/power dimensions are used only when their owning domain exposes stable semantics.
7. Sample/exposure size accompanies every aggregate/comparison.
8. Missing required evidence is `UNKNOWN`/partial, not zero.
9. Post-outcome cohort filters that can create survivorship bias must be declared.
10. One universal statistical method or numeric significance threshold is not frozen by this contract; any method used in a material decision is versioned/named in the evidence.

## 8. Gameplay/balance analytical families

Subject to concrete producer events registered by owning gameplay domains, ANL-02 supports definitions for:

- progression/activity efficiency;
- damage dealt/received and combat pressure;
- effective healing/overhealing;
- death/survival and recovery burden;
- mana/resource/consumable use;
- ability/spell/item-use efficiency and failure/cancellation outcomes;
- encounter/monster performance and attribution;
- class/vocation/progression-band comparisons;
- solo/party/shared-experience comparisons;
- equipment/power-band comparisons where privacy-safe semantics exist;
- gameplay cost/loot/profit analysis using durable value evidence where correctness requires it;
- pre/post build/content/ruleset regression analysis.

These families define analytical questions, not expected numeric outcomes.

## 9. World/content analytical families

Subject to exact World Bundle/content revision semantics and owning domain events, ANL-02 supports:

- occupancy/exposure by authored `Area`, `Subarea`, `EncounterZone`, `RaidCell`, `RaidAnchor`, `Region` or `Chunk`;
- spawn/encounter utilization and lifetime;
- unusually unused/lethal content;
- privacy-minimized travel flow;
- pathfinding/collision/teleport/accessibility indicators;
- quest/event/raid/content participation/completion;
- Channel/Instance distribution and channel-friction observations;
- change attribution across World Bundle/content/ruleset/server-build revisions.

Precise continuous player movement history is not an ordinary ANL-02 requirement.

## 10. Balance/world-health evidence packet

A bounded packet handed to a gameplay/product/content owner contains at least:

- analytical question and intended decision owner;
- metric IDs/revisions;
- exact Worlds/windows/cohorts/denominators;
- relevant semantic/build/content revisions;
- source event/schema/durability set;
- sample/exposure size;
- evidence-quality vector;
- result distribution/summary appropriate to the metric;
- known confounders and alternative explanations;
- comparison baseline/method revision;
- reproducible source checkpoint/query/transform references;
- conclusion classification;
- explicit `IMPLEMENTATION_AUTHORITY: NONE` / no automatic mutation statement.

Allowed conclusion classifications are:

- `DESCRIPTIVE` — reports observed distribution/rate;
- `REGRESSION_SIGNAL` — material compatible-baseline change requiring owner review;
- `BALANCE_HYPOTHESIS` — evidence suggests a gameplay/product imbalance but does not decide it;
- `REPLAY_CORROBORATED` — SIM evidence reproduces/isolates a behavioral divergence.

These values express analytical use, not architecture acceptance status.

## 11. Regression rule

A regression claim must name a compatible baseline and account for, as applicable:

- server build;
- ruleset/formula revision;
- content/World Bundle revision;
- channel/instance/product policy;
- metric/cohort revision;
- sampling/collection policy;
- population/exposure composition.

Multiple material simultaneous changes keep the cause ambiguous unless a controlled experiment, deterministic replay or owning-domain evidence isolates it.

## 12. SIM integration

ANL-02 may consume SIM-DETERMINISM evidence to reproduce behavior, compare exact supported-target outcomes and locate first deterministic divergence.

It may not:

- substitute best-effort event order for SIM authoritative order;
- invent missing authoritative state;
- replay live commands into production;
- repair/mutate state from replay results;
- equate deterministic difference with product undesirability.

## 13. Privacy and access

1. Ordinary balance/world projections prefer `INTERNAL_NON_PERSONAL` or `PSEUDONYMOUS_ANALYTICS`.
2. Raw AccountId/CharacterId is not admitted to ordinary analyst datasets merely for convenience.
3. `AnalyticsActorId` follows ANL-01 domain/epoch rules; cross-epoch correlation requires separately authorized/audited mapping.
4. Fine geography, exact time, rare cohort or party composition is treated as potential re-identification risk.
5. Presentation/export applies purpose-specific aggregation/suppression before disclosure; exact thresholds remain privacy-policy owned.
6. Balance/world analyst roles do not receive the privileged pseudonym-to-operational-identity mapping by default.
7. Raw, intermediate, aggregate and exported datasets each bind finite accepted retention profiles.
8. Privacy classification may be raised but not silently downgraded.

## 14. Resource and execution bounds

ANL-02 inherits all applicable ANL-01 registry limits, including bounded query pages/results, replay windows and evidence packages.

Any implementation must additionally register hard bounds before acceptance for externally controlled:

- time-range/window count;
- group-by/result cardinality;
- cohort expansion;
- cross-source join fan-out;
- geography resolution/result cells;
- backfill/recompute work units;
- concurrent jobs/intermediate memory.

Large work is paged/partitioned/resumable. Analytical storage failure does not block authoritative gameplay. ANL-02 processing may lag or become unavailable but never acquires gameplay mutation authority.

## 15. Failure semantics

- Best-effort loss/sampling -> explicit quality degradation; no completeness claim.
- Durable source gap/conflict -> affected durable-derived observation stops/marks incomplete; no fabricated state.
- Duplicate event -> one derived effect per identical EventId.
- Out-of-order related events -> bounded reconcile/defer or incomplete result.
- Unsupported schema -> ANL-01 class-specific behavior; no reinterpretation.
- Missing denominator/revision -> observation invalid/unknown for that use.
- Privacy/retention/access policy absent -> collection/projection/disclosure fails closed.
- Analytical dependency unavailable -> gameplay unchanged.
- SIM provenance incomplete -> no `REPLAY_CORROBORATED` claim.

## 16. Required producer boundary

This contract does not register gameplay event IDs or payload schemas.

A concrete metric becomes implementable only after every required producer owner has registered typed payloads compatible with ANL-01, including required attribution, semantic scope and revision context.

`GAME_EVENT_FOUNDATION_REGISTRY.json.event_types=[]` at the trusted base is therefore a known dependency, not permission for ANL-02 to mint foreign event semantics.

## 17. Required future evidence

Implementation acceptance requires, proportionally to each metric family:

- versioned metric-definition fixtures;
- duplicate/out-of-order/unsupported-schema tests;
- known best-effort drop/sampling propagation into quality metadata;
- mixed-revision rejection/stratification tests;
- denominator/cohort edge cases including empty/partial windows;
- replay-recompute determinism for analytical transforms where applicable;
- privacy raw-ID rejection and cross-epoch mapping separation;
- geography suppression/redaction tests;
- query/result/evidence-package boundary tests;
- proof no analytical path can mutate gameplay or synchronously block authoritative execution.

## 18. DECISIONS_NOT_TAKEN

This candidate does not select or authorize:

- concrete producer event IDs/payload schemas;
- database/warehouse/lake/broker/dashboard/vendor;
- physical schemas/indexes/partitions;
- collector/service topology;
- exact KPI/balance thresholds or statistical significance numbers;
- sampling percentages/late-data windows;
- exact retention durations or anonymity/suppression thresholds;
- gameplay/content/reward/formula policy;
- automatic balancing/LiveOps control;
- runtime/client/Platform/production implementation.

## 19. CROSS_DOMAIN_FINDINGS

- `ANL02-XD-01` (`P1`, report only): concrete gameplay analytical event families are not yet registered; owning gameplay/content domains plus ANL-01 registry integration must supply them before concrete coverage claims.
- `ANL02-XD-02` (`P2`, report only): ability/AI/interaction/quest/event attribution semantics remain dependent on their owning gameplay gates and cannot be invented by analytics.

Full evidence is recorded in `ANL-02_GAMEPLAY_BALANCE_WORLD_ANALYTICS_ANALYSIS.md`.

## 20. Acceptance boundary

This worker artifact is a nonbinding candidate. It may become canonical only through Architecture Coordinator audit/acceptance/merge under repository governance.

Even after architectural acceptance:

```text
DecisionStatus: ACCEPTED only if coordinator promotes it
ImplementationStatus: NOT_STARTED until separately proven
Runtime/production authority: NONE
```

`MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`
