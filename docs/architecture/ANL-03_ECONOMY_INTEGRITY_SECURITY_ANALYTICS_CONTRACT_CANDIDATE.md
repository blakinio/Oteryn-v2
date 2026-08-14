# ANL-03 — Economy, Integrity and Security Analytics Contract Candidate

- Date: 2026-08-15
- Gate: `ANL-03`
- Issue: #264
- DecisionStatus: `CANDIDATE`
- DeliveryStatus: `IN_REVIEW`
- ImplementationStatus: `NOT_STARTED`
- Status on worker branch: **CANDIDATE / NONBINDING**
- Canonical semantic effect: only after Architecture Coordinator acceptance/merge under repository governance
- Runtime/client/Platform/PostgreSQL/production/enforcement authority: **NONE**
- Merge authority: `ARCHITECTURE_COORDINATOR_ONLY`
- Analysis source: `ANL-03_ECONOMY_INTEGRITY_SECURITY_ANALYTICS_ANALYSIS.md`

## 1. Purpose

Freeze the minimum read-only consumer contract for economy health, item/currency integrity, security anomaly detection and auditable human evidence handoff.

ANL-03 owns:

- integrity/economy analytical classifications;
- detector definition/version semantics;
- signal evidence requirements;
- deterministic-versus-statistical conclusion boundaries;
- false-positive controls;
- analytical case/evidence lifecycle through human disposition/referral;
- privacy/access/retention/resource requirements for these consumers.

ANL-03 does not own authoritative prevention, gameplay/database mutation, sanctions, rollback, GM policy, concrete producer event IDs, detector technology or production rollout.

## 2. Non-authority invariant

```text
ANL-03 detector/signal/case
= read-only evidence + triage input
!= authority to mutate gameplay/database/account state
!= sanction
!= rollback/confiscation
!= automatic economy/balance control
```

No detector score, anomaly, model output, graph feature, invariant observation or case disposition grants mutation/enforcement authority by itself.

## 3. Upstream authority

A conforming ANL-03 consumer preserves:

- ADR-0006 observational/investigative and human-review boundary;
- ANL-01 immutable event/schema/durability/privacy/retention/order/idempotency rules;
- DUR-03 authoritative item/currency/value conservation, transaction and prevention semantics;
- GAME-CHANNEL World economy and reward/source multiplicity semantics;
- SIM-DETERMINISM read-only replay/state provenance;
- FND session/runtime/admission/fencing semantics;
- owning market/trade/mail/depot/reward/gameplay semantics where applicable.

ANL-03 never replaces these owners with inferred analytics semantics.

## 4. Input-class rules

### Durable integrity input

Claims about complete item/currency/value provenance, conservation, transaction outcome or reward commit require accepted `DURABLE_AUDIT` evidence and source completeness appropriate to the declared scope.

Best-effort telemetry may enrich context but cannot be sole conservation/security completeness proof.

### Durable security observation

A non-mutating security observation may be consumed as durable audit only when its producer-owned ANL-01 event type explicitly permits that classification. Missing events are not invented by ANL-03.

### Best-effort behavioral input

Behavioral/statistical detectors may consume best-effort telemetry if their detector definition declares sampling/loss tolerance and propagates data quality. Their output remains hypothesis-class unless a separate accepted invariant proves the behavior impossible.

### Operational observability

Low-cardinality process/service health may contextualize pipeline lag/failure. Player/item/session identifiers remain forbidden as ordinary Prometheus labels.

## 5. Analytical classification

Every material ANL-03 output is classified as one of:

- `AUTHORITATIVE_INVARIANT_EVIDENCE` — evaluates an already-accepted FND/DUR/gameplay invariant from appropriate evidence;
- `AUDIT_PIPELINE_INTEGRITY` — identifies event/checkpoint/schema/hash/completeness problems in the evidence path;
- `STATISTICAL_SECURITY_ANOMALY` — hypothesis from rule/model/behavior/graph analysis;
- `ECONOMY_HEALTH_OBSERVATION` — non-guilt economy source/sink/supply/concentration/liquidity/scarcity evidence;
- `ENGINE_DEFECT_HYPOTHESIS` — evidence suggests a product defect, optionally replay-corroborated.

A statistical anomaly is never relabeled as deterministic proof merely because its score is high.

## 6. DUR-03 provenance projection

When producer event families exist, ANL-03 may maintain a read-only derived provenance/ledger graph from typed evidence including as applicable:

- ItemInstanceId lifecycle;
- source/destination semantic location/custody;
- quantity/value before/after required by the owning operation;
- DUR-03 conservation class: `TRANSFER`, `SPLIT_MERGE_QUANTITY`, `STATE_MUTATION`, `MINT`, `BURN`, `TRANSFORM`, `CONVERSION`;
- typed source/sink/occurrence/cause;
- TransactionId/OperationId/CommandRef/CausationRef;
- TransactionEventRef set/completeness;
- world/channel/instance and ownership-generation evidence;
- item/domain/ruleset/content/build revisions;
- reward/source occurrence and multiplicity/eligibility context.

This projection is evidence only. It is not a second authoritative item-location/value store and cannot repair production state.

## 7. Economy interpretation

1. `WorldId` is the default economy boundary; ChannelId is contextual simulation scope, not a separate economy namespace.
2. Channel-local simulation does not imply repeatable durable reward/source eligibility.
3. Reference analysis measures Oteryn's actual world history under Reference mechanical source/sink rules; Global historical market prices/supply are not parity constants.
4. Supply/concentration/liquidity/scarcity observations include world age, population/exposure and semantic revision context.
5. “Unexplained value” requires proven durable completeness for the declared scope; otherwise the result is partial/inconclusive.
6. Durable value truth outranks best-effort activity telemetry where they disagree.
7. Market valuation requires an accepted market semantic source; external scrape/value guesses do not become authority by convenience.
8. Economy-health evidence may recommend owner review but cannot change rates, sinks, drops, fees or other live policy.

## 8. Detector-definition identity

Every material detector has a stable logical `detector_id` and immutable positive `detector_revision`.

A detector definition declares at least:

1. purpose/threat/defect hypothesis;
2. detector class (`deterministic-rule`, `statistical-rule`, `model`, `graph`, `reconciliation` or later explicitly versioned class);
3. required input event/projection families and supported schema revisions;
4. required durability/completeness/privacy classes;
5. applicable World/ruleset/content/build/SIM revisions;
6. feature definitions/revisions;
7. observation-window/time basis;
8. subject scope;
9. rule/model/algorithm artifact identity and digest;
10. threshold/configuration revision where applicable;
11. output category/severity/confidence semantics;
12. source-quality prerequisites;
13. known false-positive modes/exclusions;
14. resource bounds/degradation behavior;
15. evaluation corpus/revision requirements;
16. privacy/retention/access policy.

Rule/feature/model/threshold semantic change receives a new explicit revision according to the detector contract. Historical outputs retain the exact detector/config/artifact revision used to produce them.

## 9. Signal contract

Every emitted detector signal has a stable non-reused reference and records at least:

```text
signal reference
detector_id + detector_revision
configuration/model/artifact digest
run/evaluation reference
observation window
subject scope/reference under correct privacy class
analytical classification + signal category
impact severity / triage priority
score/confidence semantics when applicable
invariant/rule/hypothesis evaluated
source evidence/checkpoint references
source completeness/quality vector
relevant World/Channel/Instance + semantic revisions
known exclusions/false-positive caveats
creation time
case/disposition linkage when later assigned
```

Severity is triage/impact context, not guilt. Confidence/score expresses detector semantics, not enforcement authorization.

Duplicate re-evaluation may coalesce operational noise only if original evidence/signal lineage remains addressable and historical outputs are not rewritten.

## 10. Evidence conclusion rules

### `INVARIANT_VIOLATION_SUPPORTED`

May be used only when:

- the invariant and relevant revisions are accepted;
- required durable source/checkpoint/event-set evidence is proven complete for the declared scope;
- EventId/schema/hash/order/TransactionEventRef prerequisites pass;
- detector/projection logic is reproducible/versioned;
- no known evidence-pipeline failure explains the mismatch.

Otherwise the result is data-quality/inconclusive, not deterministic subject attribution.

### `ANOMALY_HYPOTHESIS`

Statistical/rule/model/graph anomaly remains a hypothesis pending human review and corroborating evidence. A probability/score never converts directly into sanction authority.

### `REPLAY_CORROBORATED_DEFECT`

May be used when SIM-DETERMINISM exact provenance reproduces a product divergence/invariant failure under the relevant semantic revision set. Repair and player/account action remain foreign authority.

## 11. Case/evidence lifecycle

The ANL-03 analytical lifecycle is:

```text
SIGNAL_EMITTED
-> TRIAGED
-> CASE_OPENED (optional)
-> EVIDENCE_ASSEMBLED
-> HUMAN_DISPOSITION
-> CLOSED or REFERRED_TO_FOREIGN_OWNER
```

Required properties:

- original signal content/revision/evidence lineage remains immutable;
- one case may group multiple signals while preserving every source reference;
- evidence additions/annotations record actor, time and source;
- privileged identity resolution is separately purpose-authorized and audited;
- human disposition records reviewer role/identity, time, rationale category and evidence refs;
- any enforcement/remediation result is linked only as a foreign-owner reference and is not executed by ANL-03.

Allowed evidence dispositions:

- `SUPPORTED_INTEGRITY_OR_DEFECT_FINDING`;
- `NOT_SUPPORTED_FALSE_POSITIVE`;
- `INCONCLUSIVE_INSUFFICIENT_EVIDENCE`;
- `DATA_QUALITY_OR_PIPELINE_FAILURE`;
- `DUPLICATE_OR_ALREADY_COVERED`;
- `REFERRED_TO_SECURITY_GM_PRODUCT_OR_ENGINE_OWNER`.

These are analytical dispositions, not sanctions.

## 12. False-positive safety

To satisfy `FS-DETECTOR-FALSE-POSITIVE` at semantic level:

1. detector output creates no automatic sanction/mutation;
2. detector/rule/model/config revision is retained with every signal;
3. source evidence/checkpoints are traceable within policy;
4. human review/disposition is auditable;
5. threshold/model changes do not rewrite historical outputs;
6. any suppression/allow-list mechanism is separately versioned/scoped/audited and cannot be a hidden authority bypass;
7. false-positive outcomes may be used as detector-quality evidence without deleting historical errors;
8. incomplete data yields inconclusive/data-quality disposition where material;
9. pipeline failures are separated from player/gameplay findings.

Exact quality/precision/recall/calibration thresholds remain implementation/security-product decisions.

## 13. Security analytical scope

Subject to producer-owned typed event families, ANL-03 may analyze:

- command replay/duplicate/stale-session/stale-ownership attempts;
- admission/reconnect/channel-switch anomalies;
- cooldown/sequencing/action-rate anomalies;
- automation/bot-like patterns;
- repeated reward/source loops;
- item/currency provenance anomalies;
- unusual transfer fan-in/fan-out/cycles/concentration;
- market/trade/mail/depot inconsistencies once owning contracts exist;
- protocol capability/downgrade/revision anomaly evidence;
- engine defects exposed by invariant/replay mismatch.

No generalized device fingerprinting, invasive client surveillance, credential capture or secret retention is authorized. New device/network identity collection requires a separate named security/privacy purpose and owning contract.

## 14. Privacy/access/retention

1. Broad detection uses `PSEUDONYMOUS_ANALYTICS` or non-personal features where feasible.
2. Restricted item/transaction/session/player evidence uses `RESTRICTED_PLAYER_LINKED` or `SECURITY_SENSITIVE` as required by producer/purpose.
3. AnalyticsActorId mapping is separately protected; detector access is not implicit.
4. Privileged identity resolution is case-purpose-authorized and access-audited.
5. Fine location/time and any later device/network context are treated as re-identification/security-sensitive where applicable.
6. Raw evidence, detector features, signals, case evidence, identity-resolution logs and exports have separate finite retention profiles.
7. Legal hold is an explicit audited exception, never ordinary unlimited retention.
8. Privacy classification can be raised but never silently downgraded.

## 15. Read-only credential boundary

Future ANL-03 components must use least-privilege read-only credentials/views appropriate to their source and must not possess:

- gameplay mutation credentials;
- production DB write authority;
- sanction/account-action authority;
- rollback/confiscation/value-repair authority;
- deployment authority.

Enforcement/remediation requires referral to a foreign owner that independently validates its authority and evidence.

## 16. Resource bounds

ANL-03 inherits applicable ANL-01 event/replay/query/result/evidence-package limits.

Before implementation acceptance, externally controlled/high-growth detector work must register hard limits for applicable:

- observation-window duration/event count;
- per-subject retained state;
- feature cardinality/bytes;
- graph vertices/edges/depth/fan-out;
- join expansion;
- signals per run/window/subject;
- case evidence references/attachments;
- concurrent detector/backfill/reconciliation jobs;
- model/rule artifact size;
- investigator query/export scope;
- resumable provenance work units.

Exact numbers require implementation/PERF/OPS evidence and registry ownership. Large jobs are partitioned/resumable. Detector lag/unavailability never blocks gameplay solely to preserve analytics freshness; committed durable audit remains subject to ANL-01/DUR no-silent-drop rules.

## 17. Failure semantics

- Best-effort feature loss -> input partial; no completeness-dependent finding.
- Durable audit/event-set/checkpoint gap -> completeness-dependent detector stops/inconclusive; pipeline incident may be emitted.
- EventId conflict -> evidence-integrity incident; no overwrite.
- Unsupported durable schema -> quarantine/reject per ANL-01.
- Duplicate event -> one projection/evaluation effect per identical EventId.
- Out-of-order events -> bounded defer/reconcile; no fabricated provenance.
- Detector/model unavailable -> detector unavailable; gameplay unchanged.
- Model/threshold revision change -> new versioned evaluation; old signals preserved.
- Identity mapping unavailable -> no unauthorized fallback.
- Missing privacy/retention/access policy -> no collection/projection/disclosure.
- Oversized query/evidence -> page/partition/reject within registry bounds.
- Suspected violation + incomplete evidence -> `INCONCLUSIVE_INSUFFICIENT_EVIDENCE`, never automatic sanction.

## 18. Failure-scenario status

- `FS-AUDIT-OUTBOX-BACKLOG`: semantic `PASS` for consumer behavior; physical audit durability remains ANL-01/DUR.
- `FS-EVENT-DUPLICATE-DELIVERY`: semantic `PASS`.
- `FS-EVENT-OUT-OF-ORDER`: semantic `PASS`.
- `FS-AUDIT-MUTATION-MISMATCH`: semantic `PASS` as explicit integrity/data-quality evidence; prevention remains DUR-02/03.
- `FS-ANALYTICS-PRIVACY-POLICY`: semantic `PASS`.
- `FS-DETECTOR-FALSE-POSITIVE`: semantic `PASS` through no-auto-sanction + versioned evidence + human disposition.
- `FS-INVESTIGATION-MUTATION-ATTEMPT`: `DEFERRED_BY_ACCEPTED_GATE` for executable proof to ANL-04/implementation; ANL-03 requires read-only credentials.

Architecture status does not imply runtime proof.

## 19. Required producer boundary

This candidate does not register concrete DUR/FND/gameplay event type IDs or payload schemas.

Concrete detector/ledger coverage is implementable only after its producer owners register the required typed events under ANL-01 with sufficient provenance, revision, authority and privacy semantics.

The trusted-base empty `GAME_EVENT_FOUNDATION_REGISTRY.json.event_types` is therefore an explicit dependency, not permission for ANL-03 to define foreign producer schemas.

## 20. Required future evidence

Implementation acceptance requires, proportionally to each detector family:

- deterministic projection fixtures for DUR-03 conservation/location/lineage classes;
- TransactionEventRef complete/gap/duplicate/conflict cases;
- EventId duplicate/conflict and unsupported-schema cases;
- checkpoint loss/recovery and durable source-completeness tests;
- stable detector/model/config/artifact revision reproduction;
- known false-positive corpus and human-disposition workflow evidence;
- best-effort sampling/loss propagation tests for statistical detectors;
- privacy raw-ID/pseudonym mapping/access-audit tests;
- graph/query/export/resource boundary tests;
- SIM replay-corroboration fixtures where claimed;
- proof detector/investigation credentials cannot mutate gameplay/DB or sanction accounts.

## 21. DECISIONS_NOT_TAKEN

This candidate does not select or authorize:

- concrete producer event IDs/payload schemas;
- database/warehouse/lake/broker/vendor topology;
- detector framework/language/model architecture;
- exact detector algorithms/thresholds;
- production detector rollout;
- sanctions/GM/moderation/account-action policy;
- automatic ban/mute/kick/confiscation/rollback/value repair;
- device fingerprinting/client surveillance/network identity collection;
- exact retention/legal durations;
- market/trade/mail/depot/reward business policy;
- economy target values or automatic tuning;
- Platform/runtime/client/DDL/production implementation;
- ANL-04 AI implementation.

## 22. CROSS_DOMAIN_FINDINGS

- `ANL03-XD-01` (`P1`, report only): concrete DUR-03 item/currency/value durable event families are not yet registered; complete provenance/invariant coverage cannot be implemented until producer owners register them.
- `ANL03-XD-02` (`P2`, report only): enforcement/GM/account-remediation authority is intentionally outside ANL-03 and requires a separately owned accepted contract before production action.
- `ANL03-XD-03` (`P2`, report only): FND/session/admission/channel security producer event coverage is not registered; corresponding detectors cannot claim completeness.
- `ANL03-XD-04` (`P2`, report only): market/trade/mail/depot/reward fraud/business interpretation remains dependent on owning economy/gameplay contracts.

Full evidence is recorded in `ANL-03_ECONOMY_INTEGRITY_SECURITY_ANALYTICS_ANALYSIS.md`.

## 23. Acceptance boundary

This worker artifact is a nonbinding candidate. It may become canonical only through Architecture Coordinator audit/acceptance/merge under repository governance.

Even after architectural acceptance, implementation remains separately gated and no runtime, DDL, production or enforcement authority is granted.

`MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`
