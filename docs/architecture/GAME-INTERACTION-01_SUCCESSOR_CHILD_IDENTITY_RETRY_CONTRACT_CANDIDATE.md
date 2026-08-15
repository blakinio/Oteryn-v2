# GAME-INTERACTION-01 successor contract candidate — child identity, retry and reconciliation

- Status: `PROPOSED / NONCANONICAL`
- Gate: `GAME-INTERACTION-01` (same gate; no new global gate ID)
- Successor issue/task: #274 / `OTV2-20260815-game-interaction-successor-r1`
- Predecessor issue/PR: #262 / draft PR #269
- Predecessor reviewed head: `71253a8d5805ed37ec451e40e2c7200c38031a52`
- Base: `main@cb98fd32a2bb71fce83234ebf8bf69bdd1a1970e`
- Mode: `PAPER-ONLY / CONTRACT`
- Merge authority: `ARCHITECTURE_COORDINATOR_ONLY`
- Implementation authority: `NONE`

## 1. Contract purpose and predecessor boundary

This candidate is a fresh bounded successor for the unchanged `GAME-INTERACTION-01` gate.

The predecessor task reached `repair_cycles_for_current_gate: 3`. The final coordinator review of draft PR #269 identified two remaining material findings. Repository governance forbids treating another edit under the predecessor task as repair cycle 4. Therefore:

- predecessor issue #262, PR #269, branch and three worker-owned files remain read-only evidence to this successor;
- this candidate resolves only the child-occurrence identity and cross-owner/client retry/error findings;
- no predecessor lifecycle state is rewritten;
- no new global gate ID is created.

If accepted, this successor is intended to be integrated by the Architecture Coordinator with the sound predecessor contract, not to erase its other design work.

## 2. Normative inherited invariants

The successor MUST preserve all of the following predecessor invariants:

1. **server-authoritative target resolution** — client selection/hints never create target authority;
2. **typed/versioned state machines** — interaction state is typed rather than free-form mutable bags;
3. **explicit scope/lifetime/reset/recovery** — no implicit process lifetime defines gameplay semantics;
4. **GAME-ITEM + DUR-03 value authority** — interaction cannot mint/move/consume durable value outside owning item/value contracts;
5. **GAME-ABILITY effect authority** — interaction can trigger an ability-owned proposal/operation but cannot own formulas/effect commit semantics;
6. **movement/relocation/handoff delegation** — this candidate does not select that owner;
7. **named coupled workflows** — no generic distributed multi-owner transaction is introduced;
8. **bounded cascades** — depth/fan-out/work remain bounded by owning policy, although numeric values are out of scope here;
9. **proposal-only scripts** — DUR-04 guest code proposes typed effects and never self-grants authoritative mutation;
10. **deterministic revisions/order/RNG** — SIM-DETERMINISM remains authoritative;
11. **no generic mutable `GLOBAL` interaction scope** — authoritative state belongs to explicit World/Channel/Instance/domain scope.

Nothing in the retry contract below weakens those invariants.

## 3. Consumed contracts and ownership

This candidate consumes, without redefining:

- `docs/contracts/FOUNDATION_ERROR_VOCABULARY.md` — public/cross-component error requirements;
- `docs/contracts/FOUNDATION_FAILURE_SCENARIOS.md` — ambiguity/retry/reconciliation expectations;
- `docs/architecture/FND-02_PROTOCOL_OTERYN_V1_CONTRACT.md` — `CommandRef`, command ordering/idempotency, generation fence, client reconciliation transport;
- `docs/architecture/FND-03_RUNTIME_EXECUTION_CONTRACT.md` — authoritative runtime ownership/execution/fencing;
- `docs/architecture/FND-04C_ERROR_DIAGNOSTICS_FAILURE_COMPATIBILITY_CONTRACT.md` — accepted session/admission/recovery error pattern and security-terminal semantics;
- `docs/architecture/DUR-03_ITEM_TRANSACTION_AND_ANTI_DUPLICATION_CONTRACT.md` — item/value transaction identity, durable commit and ambiguity reconciliation;
- `docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md` — proposal-only script boundary;
- `docs/architecture/SIM-DETERMINISM-01_AUTHORITATIVE_SIMULATION_CONTRACT.md` — semantic revision binding, canonical order and retry-stable RNG;
- accepted GAME-ITEM-01 authority contracts;
- an eventually accepted GAME-ABILITY-01 owning contract for ability-owned effect internals.

Where a narrow operation code belongs to another owner, this candidate names that dependency and does not invent the owner's code.

## 4. Terms

### 4.1 Root source occurrence

A `RootSourceOccurrenceRef` is a stable authoritative occurrence identity owned by the domain that accepted the causal input.

Examples include:

- FND-02 `CommandRef` for a client command;
- committed movement occurrence reference for movement-derived contact/enter/leave;
- stable timer occurrence;
- accepted domain `OperationId`/`TransactionId`/cause reference;
- accepted event occurrence identity.

A root source occurrence is not a client visual target, pointer, callback instance or transport packet identity.

### 4.2 Child occurrence

An `InteractionChildOccurrenceRef` identifies one semantic child of a root/parent occurrence. It is not a globally allocated UUID and is not a credential.

### 4.3 Owner operation reference

`OwnerOperationRef` means the stable typed operation/transaction/attempt identity owned by a delegated domain. Examples may include a DUR-03 TransactionId or a future movement/handoff operation reference.

GAME-INTERACTION MUST NOT define one generic process-wide/global `OperationId` type to replace those owner-specific identities.

### 4.4 Semantic revision context

`SemanticRevisionContext` is the exact immutable behavior-affecting revision/artifact set bound to one logical occurrence, as required by SIM/content/owning contracts.

### 4.5 Authority fences

`AuthorityFenceEvidence` includes current runtime ownership generation and relevant mutable state/domain revisions used to prove the current owner may apply/complete work.

Authority fences are not logical child identity merely because they change over failover.

## 5. Stable child-occurrence identity

### 5.1 Direct child shape

A direct child MUST have semantic identity equivalent to:

```text
InteractionChildOccurrenceRef = (
    ParentSourceOccurrenceRef,
    InteractionDefinitionRef,
    AuthoritativeTargetDiscriminator,
    TypedEdgeOrCapabilityDiscriminator,
    OptionalCanonicalChildOrdinal,
    SemanticRevisionContext
)
```

For first-level fan-out:

```text
ParentSourceOccurrenceRef = RootSourceOccurrenceRef
```

For a cascaded child:

```text
ParentSourceOccurrenceRef = parent InteractionChildOccurrenceRef
```

Thus a bounded cascade forms a stable source-derived ancestry path without allocating a new global UUID:

```text
RootSourceOccurrenceRef
  / child-step-1
  / child-step-2
  / ...
```

The full logical identity is the bounded recursive tuple/path. A compact implementation representation may be derived later, but semantic equality remains defined by the path fields, not by a transient allocation.

### 5.2 Why parent ancestry is required for cascades

If two distinct parent children in the same root cascade can both reach the same interaction definition, target and typed edge, using only the ultimate root plus final target/edge could merge semantically distinct siblings.

Including the stable parent child reference prevents this collision while remaining deterministic and source-derived.

If an owning mechanic intentionally defines two paths as one idempotent semantic join, that join rule MUST be explicit in the owning typed interaction definition. Runtime MUST NOT accidentally create such a join through dedup-key truncation.

### 5.3 `InteractionDefinitionRef`

`InteractionDefinitionRef` MUST be stable within the exact bound content artifact/revision and MUST identify the authored/compiled interaction semantics being executed.

It MUST NOT be:

- memory address;
- process-local loader index unless that index is itself a versioned stable authored key;
- unordered registry position;
- source file line number used as accidental runtime identity.

### 5.4 `AuthoritativeTargetDiscriminator`

The target discriminator MUST come from server-authoritative resolution in the applicable semantic scope and MUST be stable enough to replay/reconcile the bound occurrence.

Allowed shapes are owner-contract-defined strong semantic object/entity identity or canonical typed world-object keys.

It MUST NOT derive authority or identity from:

- client hints;
- UI selection order;
- pointer/reference addresses;
- hash buckets;
- physical vector/map iteration index;
- thread/worker discovery order;
- unspecified database row order.

If no stable target discriminator exists for an interaction family, implementation of that family is `BLOCKED` until its owning contract supplies one.

### 5.5 `TypedEdgeOrCapabilityDiscriminator`

Multiple semantic edges/capabilities on the same object MUST remain distinguishable.

The discriminator MUST be an authored/compiled stable typed key such as an accepted `ON_ENTER`, `ON_LEAVE`, `ON_CONTACT`, `USE` edge kind or versioned mechanic-specific capability key.

Free-form callback names or function pointers MUST NOT become authoritative identity.

### 5.6 `OptionalCanonicalChildOrdinal`

The ordinal MUST be absent unless all non-ordinal fields still identify more than one **intentionally distinct** semantic child.

When present:

1. multiplicity MUST be explicit in the accepted interaction definition;
2. ordinal assignment MUST derive from explicit authored semantic order or a canonical typed comparator over stable semantic fields;
3. the same content/revision MUST reproduce the same ordinal;
4. hash-map/container iteration, thread scheduling, worker completion, pointer order or unspecified DB row order MUST NOT assign it;
5. an ordinal MUST NOT be used to hide an invalid duplicate definition.

If two configured children are accidentally indistinguishable, validation MUST reject the definition fail-closed rather than inventing runtime ordinals.

### 5.7 `SemanticRevisionContext`

Every child MUST bind the exact behavior-affecting semantic context needed to interpret it. Depending on the mechanic this includes the applicable subset of:

- World Bundle/content artifact identity;
- interaction-definition revision;
- ruleset/world-policy revision;
- SIM profile revision;
- script artifact/WIT/execution-profile revision;
- delegated owner semantic revision required to interpret its result.

Retry/replay/recovery MUST use the same bound context or an explicit accepted compatibility/reconciliation rule. A newer active content revision MUST NOT silently reinterpret an already accepted child.

### 5.8 Logical identity versus current authority

Transient runtime ownership generation MUST NOT be appended to logical child equality merely to make a new key after failover.

Normative separation:

```text
logical occurrence identity = InteractionChildOccurrenceRef
current right to apply work = validate AuthorityFenceEvidence now
```

A completion produced under stale generation/revision is rejected before mutation. The replacement/current owner then reconciles the **same** child/OwnerOperationRef.

Mutable optimistic state revisions used only as preconditions/fences do not create a new logical child when they change. Immutable behavior-affecting revision context does remain bound to the logical child.

### 5.9 Representation

This candidate deliberately does not freeze:

- UUID allocation;
- hash/digest algorithm;
- binary layout;
- database primary key;
- retention count/window;
- protocol numeric field/code values.

An implementation MAY derive a compact digest/index from the canonical tuple/path, but collision handling MUST preserve semantic tuple equality and MUST NOT turn the digest into a new authority source.

A diagnostic trace/correlation ID MUST NOT be used as dedup authority.

## 6. Deterministic child-plan rule

### 6.1 Authoritative child plan

Before any child can commit or any foreign owner can accept work, the interaction owner MUST have a reproducible authoritative child plan equivalent to:

```text
InteractionChildPlan {
    root_source_occurrence
    exact_semantic_revision_context
    ordered_child_occurrence_refs[]
    required_authority/precondition evidence
}
```

This is a semantic contract, not a storage schema.

### 6.2 Canonical collection/order

Eligible targets/edges MUST first be resolved authoritatively and then ordered by a declared semantic rule:

- explicit authored semantic order where order is meaningful; or
- a stable typed comparator over authoritative semantic keys where the set is otherwise unordered; or
- retained FND-03 accepted execution order only where the owning contract explicitly makes that accepted order semantic/replay evidence.

The implementation MUST NOT use:

- hash-map iteration;
- unordered set traversal;
- pointer order;
- thread/worker completion order;
- OS scheduler order;
- unspecified database row order.

The canonical order is part of replay evidence when order affects behavior.

### 6.3 Recovery after partial progress

Once any child has committed or any delegated owner has accepted work, recovery MUST reproduce the same accepted child set/order from retained authoritative evidence and/or the exact immutable bound content/state.

Recovery MUST NOT:

- re-enumerate against a newer mutable world and treat the result as the same root occurrence;
- drop a previously accepted sibling because it is no longer discoverable in current state;
- add a new sibling from changed state to the historical root;
- renumber siblings based on a new physical iteration order.

If the accepted child plan cannot be reconstructed safely, the root/affected children fail closed into explicit reconciliation rather than guessed re-execution.

## 7. Child lifecycle and exactly-once semantics

An implementation MAY choose a different internal representation, but it MUST preserve semantic states equivalent to:

```text
UNSTARTED
PENDING
COMMITTED
REJECTED
```

Rules:

- `UNSTARTED`: accepted child exists but no semantic commit/delegated operation acceptance has occurred; recovery may execute it once if current fences authorize.
- `PENDING`: final outcome cannot yet be proven; reconcile the same child and same accepted foreign operation if any.
- `COMMITTED`: semantic commit is proven exactly once; replay/retry never reapplies it.
- `REJECTED`: this logical child is terminal and cannot later be reinterpreted as a fresh attempt.

Different siblings MUST have different child refs. The same sibling delivered more than once MUST resolve to one lifecycle entry/outcome.

A child terminal result MAY be retained/reconstructed under bounded owner policy, but loss of a convenience payload MUST NOT re-enable semantic execution.

## 8. Deterministic RNG contract

For every child-owned authoritative random decision, identity MUST be equivalent to:

```text
InteractionRngDecisionRef = (
    InteractionChildOccurrenceRef,
    RngPurposeKey,
    DeterministicDrawOrdinal
)
```

SIM owns the actual algorithm/profile/seed derivation.

GAME-INTERACTION requirements:

1. same child + purpose + draw ordinal => same logical random decision on retry/replay/recovery;
2. runtime failover/generation change MUST NOT reroll;
3. stale/deferred result delivery MUST NOT reroll;
4. draw ordinal MUST follow semantic purpose order, not scheduling order;
5. adding an unrelated sibling/purpose MUST NOT accidentally perturb another purpose stream;
6. rejected work before authoritative acceptance consumes no authoritative gameplay RNG state unless the owning SIM mechanism explicitly defines and commits that occurrence;
7. secret seed/root material is never exposed merely to correlate interaction results.

## 9. Public/cross-owner outcome state

Every public/cross-component interaction result that can be affected by retry/ambiguity MUST expose one semantic outcome state:

```text
InteractionOutcomeState = COMMITTED | PENDING | REJECTED
```

### 9.1 `COMMITTED`

`COMMITTED` means the interaction's declared semantic commit point is proven complete exactly once.

For a named coupled workflow, only the workflow's final reconciliation owner/coordinator may establish whole-workflow `COMMITTED`. A participant-local commit is insufficient.

### 9.2 `PENDING`

`PENDING` means final semantic outcome is unresolved and another blind semantic attempt could duplicate effects/value.

While `PENDING`:

- same `InteractionChildOccurrenceRef` MUST be retained;
- same `OwnerOperationRef` MUST be used if a foreign owner accepted/may have accepted work and the owner contract can identify it;
- same client `CommandRef` remains the parent command occurrence when the root is client-originated;
- caller MUST reconcile/query/resume the same occurrence;
- caller MUST NOT issue a new `CommandRef` for the same semantic intent while the prior occurrence may still commit;
- transport reconnection/new `connection_generation` is not a new semantic occurrence;
- any FND-04-required new GameSession recovery does not by itself authorize replaying the old interaction as new;
- owner-specific recovery/retirement proof is required before a fresh semantic attempt is permitted.

### 9.3 `REJECTED`

`REJECTED` means the original logical occurrence is terminal and no accepted work from it may later commit.

If retry policy allows a fresh attempt:

- client-originated fresh attempt MUST use a new `CommandRef` under the currently valid GameSession, or a new valid session only if FND-04 requires it;
- non-client fresh attempt MUST use a new root source occurrence owned by that domain;
- replay of the old source occurrence returns/reconciles the old rejection and MUST NOT reevaluate it as new work.

## 10. Local mutation state for ambiguity

Where a `PENDING` cross-owner result can coexist with local participant mutation, the safe public/cross-component envelope MUST carry an owner-approved state equivalent to:

```text
LocalMutationState = NOT_COMMITTED | COMMITTED | UNKNOWN
```

Rules:

- `NOT_COMMITTED` may be asserted only when the owner can prove no local authoritative mutation from the occurrence committed;
- `COMMITTED` may be asserted only when the local commit is proven, but this does not imply whole coupled-workflow commit;
- `UNKNOWN` is required when recovery evidence cannot safely classify local mutation yet;
- absence of a response or timeout MUST NOT be interpreted as `NOT_COMMITTED`;
- a named coupled workflow may expose a richer owner-owned participant state, but it MUST map boundedly to these caller safety semantics.

Purely local `REJECTED` codes defined below require `NOT_COMMITTED`. Purely local `COMMITTED` is terminal and idempotent.

## 11. Mandatory correlation fields

A public/cross-component result MUST carry the applicable safe correlation required to reconcile without guessing:

- `RootSourceOccurrenceRef` or its externally legal parent command/event reference;
- `InteractionChildOccurrenceRef` or a protocol-safe exact representation/reference to it;
- semantic scope (`WorldId`, `ChannelId`, `InstanceId` as applicable; never generic mutable `GLOBAL`);
- exact bound semantic revision reference sufficient to reject incompatible replay;
- `InteractionOutcomeState`;
- stable machine category;
- contract-owned symbolic code;
- `OwnerOperationRef` when foreign work was accepted/may have been accepted and the owner contract exposes such a reference;
- `LocalMutationState` when partial/local mutation ambiguity exists;
- optional redacted diagnostic/correlation reference that is not itself authority.

The public envelope MUST NOT expose raw internal exception strings, credentials, secret RNG material, unrestricted DB identifiers, stack traces or other sensitive internals.

## 12. Retry authority vocabulary

GAME-INTERACTION uses these semantic retry authorities:

```text
RECONCILE_SAME_OCCURRENCE
NEW_OCCURRENCE_ALLOWED
OWNER_INTERVENTION_REQUIRED
NO_RETRY
```

Interpretation:

- `RECONCILE_SAME_OCCURRENCE`: transport/service calls may repeat idempotently, but semantic source/child/OwnerOperationRef does not change.
- `NEW_OCCURRENCE_ALLOWED`: the old occurrence is terminal; a new user/domain intent may create a new source occurrence/new CommandRef.
- `OWNER_INTERVENTION_REQUIRED`: automatic bounded reconciliation cannot establish a safe terminal state; owning operational/recovery procedure must resolve it before fresh semantic execution.
- `NO_RETRY`: security/terminal state forbids interaction-level retry; caller follows the owning session/security/domain contract.

This vocabulary is orthogonal to Foundation progression `RETRYABLE | TERMINAL | SECURITY_TERMINAL` and is included to remove caller ambiguity.

## 13. GAME-INTERACTION-owned public error codes

The codes in this section are stable symbolic contract codes owned by `GAME-INTERACTION-01`. This successor does **not** assign numeric wire values. Client-visible numeric registration/IDL is explicitly blocked on the future GAME-INTERACTION payload integration under `FND-02_PROTOCOL_OTERYN_V1_CONTRACT.md`.

### 13.1 Normative matrix

| Code | Machine category | Foundation progression | Outcome state | Retry authority | Same source / OwnerOperationRef | New CommandRef/source | Local mutation possible? | Caller terminal-state test | Final reconciliation owner |
|---|---|---|---|---|---|---|---|---|---|
| `GI_DEPENDENCY_UNAVAILABLE_REJECTED` | `DEPENDENCY_UNAVAILABLE` | `RETRYABLE` | `REJECTED` | `NEW_OCCURRENCE_ALLOWED` | same source only replays rejection; no foreign op exists | **required for a fresh semantic attempt** if still authorized | `NO`; code is legal only before foreign acceptance/local commit | `REJECTED` + this code proves old occurrence terminal | current interaction owner |
| `GI_DEPENDENCY_UNAVAILABLE_PENDING` | `DEPENDENCY_UNAVAILABLE` | `RETRYABLE` | `PENDING` | `RECONCILE_SAME_OCCURRENCE` | **same child and same OwnerOperationRef** where accepted/maybe accepted | **forbidden for same intent while pending** | `YES/UNKNOWN`; report `LocalMutationState` as required by owner/workflow | only later owner proof may produce `COMMITTED` or terminal `REJECTED` | delegated owner or named workflow coordinator; interaction maps result |
| `GI_TIMEOUT_REJECTED` | `TIMEOUT` | `RETRYABLE` | `REJECTED` | `NEW_OCCURRENCE_ALLOWED` | same source only replays rejection; no accepted foreign op | **required for fresh semantic attempt** | `NO`; timeout-before-acceptance must be proven | `REJECTED` proves old occurrence terminal | current interaction owner |
| `GI_TIMEOUT_PENDING` | `TIMEOUT` | `RETRYABLE` | `PENDING` | `RECONCILE_SAME_OCCURRENCE` | **same child/OwnerOperationRef** | **forbidden for same intent while pending** | `YES/UNKNOWN`; timeout is not proof of abort | owner proof of commit/cancel/reject decides terminal state | delegated owner or named workflow coordinator |
| `GI_CANCELLED_REJECTED` | `CANCELLED` | `TERMINAL` for this occurrence | `REJECTED` | `NEW_OCCURRENCE_ALLOWED` only for a later distinct intent | same source replays cancellation result | **new source required for later distinct intent** | `NO`; all accepted participants must be proven retired before semantic commit | cancellation-before-commit proof makes old occurrence terminal | interaction owner or workflow coordinator that proved retirement |
| `GI_CANCELLED_PENDING` | `CANCELLED` | `RETRYABLE` for reconciliation | `PENDING` | `RECONCILE_SAME_OCCURRENCE` | **same child/OwnerOperationRef** | **forbidden for same intent while pending** | `YES/UNKNOWN`; cancel request is not rollback proof | commit proof -> `COMMITTED`; cancel-before-commit proof -> terminal `REJECTED`; otherwise pending | delegated owner/workflow coordinator |
| `GI_STALE_FENCE_REJECTED` | `STALE_GENERATION` | `TERMINAL` for stale application attempt | `REJECTED` | `NEW_OCCURRENCE_ALLOWED` only after current authority resolves a genuinely new intent | old source remains terminal only when no underlying foreign op can still commit | new source only after terminal proof/current authorization | `NO` from the stale application itself | stale application was rejected before mutation; underlying op must be known absent/terminal | current authoritative runtime owner |
| `GI_DELEGATED_STALE_COMPLETION_PENDING` | `STALE_GENERATION` | `RETRYABLE` for reconciliation | `PENDING` | `RECONCILE_SAME_OCCURRENCE` | **same child and same delegated OwnerOperationRef** | **forbidden for same intent while pending** | underlying local/foreign mutation may be `COMMITTED` or `UNKNOWN`; stale completion itself mutates nothing | stale message rejection is **not** operation rejection; later current-owner reconciliation decides | underlying delegated owner + current interaction owner mapping |
| `GI_RECONCILIATION_REQUIRED` | `INTERNAL_UNAVAILABLE` | `RETRYABLE` bounded reconciliation | `PENDING` | `RECONCILE_SAME_OCCURRENCE`; may escalate to owner intervention under owning policy | same source/child/op | **forbidden until terminal retirement/proof** | `YES/UNKNOWN` as reported; never infer none | terminal only after authoritative reconciliation | owner named by underlying operation/workflow |
| `GI_COUPLED_WORKFLOW_RECONCILIATION_REQUIRED` | `INTERNAL_UNAVAILABLE` | `RETRYABLE` bounded reconciliation | `PENDING` | `RECONCILE_SAME_OCCURRENCE` | same child + same workflow/participant operation refs | **forbidden for same semantic workflow while pending** | participant-local mutation may be `COMMITTED`/`UNKNOWN`; whole workflow not committed yet | only named workflow coordinator can emit whole terminal classification | named coupled-workflow coordinator |

### 13.2 `DEPENDENCY_UNAVAILABLE`

#### Before acceptance

`GI_DEPENDENCY_UNAVAILABLE_REJECTED` MUST be used only if the interaction owner can prove:

- dependency was unavailable before any delegated owner accepted work;
- no local authoritative mutation committed;
- no operation from this occurrence can later commit.

A fresh attempt is a new source occurrence. For a client this means a new `CommandRef`. The old CommandRef remains terminal/replay-only.

#### After or ambiguously around acceptance

If work was accepted or acceptance cannot safely be disproven, `GI_DEPENDENCY_UNAVAILABLE_PENDING` MUST be used instead.

The caller MUST reconcile the same child/OwnerOperationRef. A dependency outage cannot be converted into a second semantic attempt while the first may still commit.

### 13.3 `TIMEOUT`

Timeout describes observation/deadline failure, not semantic rollback.

`GI_TIMEOUT_REJECTED` is legal only when the owner proves timeout occurred before any operation acceptance/mutation that might later commit.

Otherwise `GI_TIMEOUT_PENDING` is required and the same occurrence is reconciled.

No implementation may use `timeout => safe to retry with new CommandRef` as a general rule.

### 13.4 `CANCELLED`

A cancellation request is an intent, not proof of rollback.

`GI_CANCELLED_REJECTED` requires proof that the original occurrence can no longer commit.

If cancellation races with or follows possible acceptance, use `GI_CANCELLED_PENDING` until the owner/workflow coordinator proves one of:

- commit won -> `COMMITTED`;
- cancellation retired the operation before commit -> terminal `REJECTED`;
- still ambiguous -> remain `PENDING`.

A proven commit MUST NOT be rewritten as cancelled merely because the caller no longer wants it.

### 13.5 Stale/delegated completion ambiguity

Stale delivery and underlying operation outcome are separate facts.

A stale generation/revision completion MUST fail before mutation.

- if there was no accepted/maybe-accepted foreign operation and no local mutation, `GI_STALE_FENCE_REJECTED` may terminally reject that stale application attempt;
- if a delegated operation exists or may exist, use `GI_DELEGATED_STALE_COMPLETION_PENDING` for the interaction occurrence, preserve the same child/OwnerOperationRef, and reconcile through current authority.

The implementation MUST NOT infer `operation rejected` merely from `completion message stale`.

### 13.6 Coupled workflow pending/recovery

When a named coupled workflow has not reached a provable terminal semantic commit/reject state and no narrower category is more truthful, use `GI_COUPLED_WORKFLOW_RECONCILIATION_REQUIRED`.

Requirements:

- state remains `PENDING`;
- same workflow/participant operation identities remain authoritative;
- local participant `COMMITTED` does not imply whole workflow `COMMITTED`;
- new client CommandRef/source occurrence for the same workflow intent is forbidden while pending;
- bounded automatic recovery follows the named workflow contract;
- after that contract's bounded automatic recovery is exhausted, owner intervention may be required, but this candidate does not invent numeric retry counts;
- final whole-workflow classification belongs to the named coordinator.

If the known cause is specifically dependency outage, timeout or cancellation, use the corresponding more specific GAME-INTERACTION code rather than this fallback.

## 14. SECURITY_TERMINAL and session-owned failures

GAME-INTERACTION does not reinterpret authentication/session/security failures as ordinary retryable interaction failures.

When FND-02/FND-04/FND-04C owns the narrow code, its code and progression remain authoritative, including `SECURITY_TERMINAL` where specified.

Examples of required behavior:

- stale connection generation cannot submit/revive an interaction;
- authentication/binding/security-terminal session failure follows FND-04C reauthentication/recovery rules;
- GAME-INTERACTION MUST NOT tell the caller to reuse the same command/session when the owning Foundation contract requires a new authenticated issuance/session path;
- no interaction-level code downgrades `SECURITY_TERMINAL` to `RETRYABLE`;
- safe correlation is restricted to the owning Foundation contract's allowed fields.

Thus Foundation security/session codes remain **contract-owned by Foundation** rather than being duplicated under `GI_*` names.

## 15. Bounded internal-to-public mapping

Internal errors MUST map by semantic evidence, not exception type text.

### 15.1 Mapping classes

GAME-INTERACTION exposes only the bounded stable codes defined in section 13 for interaction-owned dependency/timeout/cancel/stale/reconciliation conditions, plus explicitly delegated owner codes/classes when the owning contract requires them.

Examples:

```text
many internal transport/service-unavailable causes
  -> GI_DEPENDENCY_UNAVAILABLE_REJECTED
     OR GI_DEPENDENCY_UNAVAILABLE_PENDING
     selected by acceptance/commit evidence

many deadline/internal timeout causes
  -> GI_TIMEOUT_REJECTED
     OR GI_TIMEOUT_PENDING
     selected by acceptance/commit evidence

many cancellation implementation details
  -> GI_CANCELLED_REJECTED
     OR GI_CANCELLED_PENDING
     selected by owner retirement/commit evidence
```

Raw driver/network/database/library strings MUST NOT cross the public boundary.

### 15.2 No lossy mapping across authority boundaries

When a foreign owner has a narrow code whose semantics affect legal retry, mutation or security disposition, GAME-INTERACTION MUST retain/map that owner-owned code/class according to the accepted adapter contract. It MUST NOT collapse distinct `SECURITY_TERMINAL`, `TERMINAL`, or same-attempt reconciliation requirements into generic `TEMPORARY_FAILURE`.

## 16. New CommandRef rules

For client-originated interactions the following rules are normative:

### 16.1 Same CommandRef

The same `CommandRef` is used for:

- duplicate replay/reconciliation of the same already-reserved client command;
- receiving/recovering the same eventual terminal result;
- preserving the parent identity of `PENDING` children across eligible same-GameSession reconnect.

It is **not** a mechanism to make a terminal command become a fresh attempt.

### 16.2 New CommandRef

A new `CommandRef` is required only when:

- prior occurrence is provably terminal `REJECTED` and policy permits a fresh semantic attempt; or
- prior occurrence is `COMMITTED` and the player intentionally issues a distinct subsequent action permitted by gameplay rules.

A new CommandRef is forbidden as a duplicate workaround while prior state is `PENDING`.

### 16.3 New GameSession

A new GameSession is Foundation-owned recovery/admission behavior, not interaction retry policy.

If FND-04 terminates the old session and establishes a new valid session, GAME-INTERACTION MUST still reconcile any durable/delegated operation that could have committed from the old occurrence before allowing a logically duplicate new interaction attempt.

A new GameSession namespace does not erase external/DUR-03 operation history.

## 17. Non-client root retry rules

For movement/timer/event/domain-owned roots:

- physical redelivery/recovery of the **same** root source occurrence MUST reuse the same child refs;
- a genuinely new committed movement/timer/event occurrence creates new child refs through its new root identity;
- current world state MUST NOT be used to relabel a historical root as a new occurrence merely because recovery happened;
- when root source identity cannot be reconstructed, fail closed/reconcile instead of allocating an ad hoc UUID.

## 18. Foreign-owner blocking dependencies

### 18.1 DUR-03 item/value

Owner: `docs/architecture/DUR-03_ITEM_TRANSACTION_AND_ANTI_DUPLICATION_CONTRACT.md`.

For interaction-driven item/value mutation:

- DUR-03 TransactionId/OperationId/cause is the foreign `OwnerOperationRef`;
- DUR-03 decides durable commit/abort/ambiguity;
- GAME-INTERACTION child identity correlates the trigger but does not become item value authority;
- ambiguous durable outcome remains `PENDING` until same DUR-03 transaction is reconciled;
- stale runtime completion cannot rematerialize or duplicate committed value.

### 18.2 GAME-ABILITY effect

Owner: accepted GAME-ABILITY-01 effect/whole-gate contract.

Current status at this successor base: draft PR #268 is unmerged/blocked and therefore noncanonical.

Implementation dependency:

> Any GAME-INTERACTION adapter that needs final GAME-ABILITY effect operation identity, narrow effect failure code or formula/effect commit semantics is `BLOCKED` until the Architecture Coordinator accepts the relevant GAME-ABILITY contract.

GAME-INTERACTION MUST NOT guess those codes or formulas.

### 18.3 Movement/relocation/handoff

Owner contract: `UNKNOWN / NOT YET ACCEPTED` by explicit predecessor boundary.

Implementation dependency:

> Any interaction that delegates teleport/movement/relocation/handoff is `BLOCKED` until a named accepted owner contract defines operation identity, current-authority fences, completion, timeout/cancellation, stale completion and recovery semantics.

This candidate does not choose that owner.

### 18.4 Durable writable text

Owner contract: `UNKNOWN / NOT YET ACCEPTED` by explicit predecessor boundary.

Implementation dependency:

> Any interaction requiring authoritative durable writable-text mutation is `BLOCKED` until a named accepted owner contract exists.

This candidate does not choose that owner.

### 18.5 Client protocol registration

Owner: `docs/architecture/FND-02_PROTOCOL_OTERYN_V1_CONTRACT.md` plus future registered GAME-INTERACTION typed payload schema.

Implementation dependency:

> Client-visible `InteractionChildOccurrenceRef` representation, `InteractionOutcomeState`, stable symbolic `GI_*` codes and correlation fields MUST be registered in the accepted FND-02 gameplay payload/registry path before runtime/client implementation is accepted. This successor does not allocate numeric message/error IDs or change FND-02.

## 19. Coupled workflow contract requirements

A mechanic that spans interaction plus another authoritative owner MUST have a named accepted workflow contract before implementation if partial success can matter.

That workflow MUST define:

- coordinator/final reconciliation owner;
- source occurrence and participant `OwnerOperationRef` identities;
- participant authority boundaries;
- exact bound semantic revision context;
- current generation/revision/fence checks;
- prepare/commit or equivalent semantic commit protocol;
- local/participant mutation states;
- idempotency and duplicate handling;
- timeout semantics;
- cancellation semantics;
- stale completion handling;
- crash/restart/failover recovery;
- compensation only when explicitly legal and owner-defined;
- bounded internal-to-public error mapping;
- when whole workflow becomes `COMMITTED`, `PENDING` or terminal `REJECTED`.

No implementation may infer those semantics from generic `InteractionOutcomeState` alone.

## 20. Final reconciliation ownership

| Case | Final authority | Required behavior |
|---|---|---|
| pure interaction-local child | current FND-03 authoritative runtime owner in exact semantic scope | validate current fences, dedup by child ref, emit terminal result once |
| DUR-03 item/value child | DUR-03 durable transaction owner/coordinator | same TransactionId/OperationId reconciliation; interaction maps result |
| GAME-ABILITY child | accepted GAME-ABILITY effect owner | same effect operation/cause as owner contract; interaction does not calculate/commit formula-owned result |
| movement/handoff child | `BLOCKED` pending named accepted owner | no guessed retry/completion semantics |
| coupled workflow | named accepted workflow coordinator | only coordinator declares whole semantic unit terminal |
| client CommandRef lifecycle | FND-02/FND-04 | same command replay/reconcile vs new command/session follows Foundation contract |

The interaction runtime is responsible for preserving the child/source correlation and refusing to overstate another owner's commit status.

## 21. Deterministic acceptance scenarios

### GI-SR-01 — movement fan-out, partial delivery, retry and recovery

**Given**

- committed authoritative movement occurrence `M`;
- bound semantic revision context `R`;
- authoritative contacts `A`, `B`, `C`;
- physical discovery order may vary;
- canonical semantics produce ordered children:
  - `C1 = (M, DefA, A, EdgeEnter, -, R)`;
  - `C2 = (M, DefB, B, EdgeContact, -, R)`;
  - `C3 = (M, DefC, C, EdgeEnter, -, R)`.

**Progress before failure**

1. `C1` commits.
2. `C2` delegates to owner operation `O2`, which is accepted, but final response is lost; child is `PENDING`.
3. process/runtime ownership changes before `C3` commits.
4. an old-generation completion for `C2` later arrives.

**Required recovery**

1. replacement owner reconstructs the same child plan under `R`;
2. `C1` is not applied again;
3. `C2` remains the same child and same `O2`; stale completion cannot mutate current owner, and current owner reconciles `O2`;
4. `C3` executes at most once under its original child ref if current fences authorize;
5. siblings never collapse into one dedup key;
6. physical hash/container order cannot change `C1/C2/C3` identity/order;
7. every child random decision uses the same `(Ci,purpose,draw)` identity and cannot reroll;
8. final state contains one terminal outcome per child exactly once;
9. replay reconstructs the same semantic child set/order/results under `R`.

**Acceptance verdict:** PASS only if all nine properties hold.

### GI-SR-01B — nested cascade path collision

**Given** two first-level children under root `M` both cascade into the same target/edge tuple.

**Required** the two nested children remain distinct because their `ParentSourceOccurrenceRef` values are distinct parent child refs. A runtime that truncates identity to `(M, final_target, final_edge)` fails acceptance.

### GI-SR-02 — dependency unavailable before acceptance

**Given** no foreign operation was accepted and no local mutation committed.

**Then** return:

```text
GI_DEPENDENCY_UNAVAILABLE_REJECTED
state = REJECTED
local_mutation = NOT_COMMITTED
```

Same CommandRef replay returns the same rejection. A later fresh client attempt uses a new CommandRef.

### GI-SR-03 — timeout after possible foreign acceptance

**Given** delegation may have been accepted when timeout occurs.

**Then** return:

```text
GI_TIMEOUT_PENDING
state = PENDING
same child
same OwnerOperationRef / same owner attempt identity
```

A new CommandRef for the same intent is forbidden until owner reconciliation proves terminal state.

### GI-SR-04 — cancellation races commit

**Given** cancellation request races a delegated commit.

**Then**:

- owner proves commit first -> `COMMITTED`;
- owner proves operation retired before commit -> `GI_CANCELLED_REJECTED` / `REJECTED`;
- neither proven -> `GI_CANCELLED_PENDING` / `PENDING`.

No path duplicates the operation and cancellation never rewrites a proven commit.

### GI-SR-05 — stale delegated completion after ownership change

**Given** a delegated operation exists and an old-generation completion arrives after runtime ownership moves.

**Then** stale completion mutates nothing, occurrence remains/re-enters `PENDING` as `GI_DELEGATED_STALE_COMPLETION_PENDING`, and current owner reconciles the same foreign operation. No new child, owner operation, CommandRef or RNG stream is created.

### GI-SR-06 — coupled workflow participant partial success

**Given** one participant has locally committed but another participant/final coordinator is unresolved.

**Then** whole workflow remains `PENDING`; `LocalMutationState` may be `COMMITTED` for the proven participant, but only the workflow coordinator may emit whole `COMMITTED` or terminal `REJECTED`. New duplicate CommandRef/source occurrence remains forbidden while pending.

### GI-SR-07 — terminal rejection followed by intentional fresh attempt

**Given** `GI_TIMEOUT_REJECTED` was proven before acceptance and the gameplay rule still permits retry.

**Then** old CommandRef remains terminal/replay-only and the player's fresh attempt uses a new CommandRef. The new root creates new child refs and, where randomness is semantically part of the new occurrence, may lawfully receive new RNG decisions because it is a new occurrence rather than a retry of the old one.

### GI-SR-08 — Foundation security-terminal failure

**Given** FND-04C classifies the session/admission condition `SECURITY_TERMINAL`.

**Then** GAME-INTERACTION does not wrap it as `GI_DEPENDENCY_UNAVAILABLE_*`, does not recommend same-command/session retry, and follows the owning Foundation reauthentication/recovery disposition. No interaction mutation is authorized by the failed/stale session evidence.

## 22. Failure-mode invariants

The following MUST hold under crash/restart/retry/failover:

1. one semantic sibling => at most one authoritative commit;
2. different siblings => different semantic refs unless an explicit owning join contract says otherwise;
3. same child retry => same semantic revisions and RNG purpose identity;
4. old ownership generation => no mutation authority;
5. stale completion rejection => no assumption about underlying operation outcome;
6. timeout => no assumption of abort;
7. cancellation request => no assumption of rollback;
8. `PENDING` => no blind new semantic attempt;
9. `REJECTED` => no pending operation may later commit;
10. `COMMITTED` => no retry/recovery may reapply;
11. new GameSession => does not erase durable/foreign operation reconciliation requirements;
12. scripts remain proposal-only;
13. foreign owner commit remains foreign-owned;
14. missing owner/narrow error contract => implementation blocked rather than guessed.

## 23. Decision timing

These decisions are required **now** before implementation because they define:

- dedup/equality semantics;
- deterministic RNG occurrence identity;
- failover/recovery behavior;
- client retry behavior;
- cross-owner adapter safety;
- public result contract.

Deferring them until runtime/DDL/protocol coding would risk persisting unstable identities or shipping ambiguous retry behavior that can duplicate effects/value.

This candidate intentionally does **not** decide physical storage, hashing, wire numeric codes, numeric limits, runtime topology or foreign-owner internals.

## 24. Explicit non-decisions

`DECISIONS_NOT_TAKEN`:

- no new global gate ID;
- no generic global `InteractionId`/UUID;
- no generic global owner `OperationId`;
- no generic mutable `GLOBAL` interaction scope;
- no teleport/movement/handoff owner decision;
- no writable-text owner decision;
- no GAME-ABILITY formulas/effect internals;
- no numeric cascade/resource/retry limits;
- no Rust/runtime/client/server implementation;
- no DDL/migration/schema decision;
- no Platform/external-repository decision;
- no production/deployment change;
- no coordinator-only global architecture overlay mutation.

## 25. Cross-domain findings

`CROSS_DOMAIN_FINDINGS: NONE NEW`.

Inherited explicit blockers are retained, not solved:

- GAME-ABILITY final whole-gate integration remains noncanonical while draft PR #268 is unmerged/blocked;
- movement/handoff owner contract remains unresolved;
- durable writable-text owner contract remains unresolved.

## 26. Implementation readiness conditions

Even if this candidate is accepted, runtime implementation remains `NOT_STARTED` and is permitted only after the relevant future implementation task verifies all required dependencies.

At minimum, implementation MUST be blocked until:

- Architecture Coordinator integrates/accepts the GAME-INTERACTION whole-gate contract including this successor;
- client-visible typed payload/error registration is accepted under FND-02 where needed;
- every used target/object family has a stable authoritative target discriminator;
- every used coupled workflow has a named accepted coordinator/error/recovery contract;
- every delegated owner supplies stable operation identity and narrow retry/commit semantics;
- GAME-ABILITY/movement/writable-text blockers are resolved for mechanics that depend on them;
- executable tests prove the scenarios/invariants above.

## 27. Acceptance evidence required from a future implementation task

Future executable acceptance MUST include, at minimum:

- property/golden tests that canonical child-plan order is independent of randomized container insertion order;
- duplicate/replay tests proving sibling uniqueness and same-sibling idempotency;
- crash/failover tests at every child lifecycle boundary;
- stale-generation/revision completion tests;
- deterministic RNG replay tests proving no retry reroll;
- dependency unavailable pre/post acceptance tests;
- timeout pre/post acceptance tests;
- cancellation race tests;
- FND-02 duplicate CommandRef/reconnect tests;
- DUR-03 ambiguous transaction integration tests where item/value is involved;
- coupled-workflow participant partial-success recovery tests;
- public error-schema tests proving bounded mapping and safe correlation;
- security-terminal tests proving no downgrade to ordinary retry.

Exact numeric limits and runtime mechanics belong to their implementation/owner tasks, not this paper-only candidate.

## 28. Governance terminal condition

This successor worker MUST stop after:

- successor task/analysis/candidate are committed;
- draft PR is created;
- full exact-head diff self-review is complete;
- ordinary exact-head repository CI is evaluated;
- any worker-owned material finding is repaired within this successor's bounded budget;
- final checkpoint evidence is recorded outside the frozen commit where necessary.

The worker MUST NOT:

- mark the PR ready;
- trigger Codex/OpenAI/owner-funded independent review;
- merge/auto-merge;
- close issue #274 or predecessor #262;
- close/archive predecessor PR #269;
- archive task/release ownership;
- update coordinator-only global architecture surfaces.

Required handoff:

`INTEGRATION_READY — DRAFT PR — COORDINATOR ACTION REQUIRED`

`NEXT_ACTION: ARCHITECTURE_COORDINATOR_AUDIT`

`MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`  
`IMPLEMENTATION_AUTHORITY: NONE`
