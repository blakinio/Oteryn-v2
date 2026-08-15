# GAME-INTERACTION-01 successor analysis — child occurrence identity and retry semantics

- Status: `PROPOSED / NONCANONICAL`
- Gate: `GAME-INTERACTION-01` (unchanged)
- Successor task: `OTV2-20260815-game-interaction-successor-r1`
- Successor issue: #274
- Predecessor issue: #262
- Predecessor draft PR: #269
- Predecessor reviewed head: `71253a8d5805ed37ec451e40e2c7200c38031a52`
- Base: `main@cb98fd32a2bb71fce83234ebf8bf69bdd1a1970e`
- Mode: `PAPER-ONLY / CONTRACT`
- Merge authority: `ARCHITECTURE_COORDINATOR_ONLY`
- Implementation authority: `NONE`

## 1. Why this is a successor rather than predecessor repair

The predecessor task on #269 truthfully records `repair_cycles_for_current_gate: 3`. The final coordinator reconciliation found two remaining architecture gaps only after that repair budget had been exhausted. Repository execution-budget policy forbids silently continuing as a fourth repair cycle.

This document therefore belongs to a new bounded successor task while retaining the same semantic gate, `GAME-INTERACTION-01`. It does not rewrite the predecessor's task, candidate or lifecycle; it does not create a new global gate ID.

The successor addresses only:

1. fan-out/cascade child-occurrence identity; and
2. cross-owner/client error, retry, ambiguity and reconciliation semantics.

Every predecessor invariant not directly involved in those findings remains inherited.

## 2. Trusted facts and constraints

### 2.1 PROVEN — FND-02 command identity is already the client-command idempotency boundary

`docs/architecture/FND-02_PROTOCOL_OTERYN_V1_CONTRACT.md` defines:

```text
CommandRef = (GameSessionId, CommandId)
```

A reserved CommandId advances once. A lower already-reserved ID is never executed a second time; a pending duplicate remains the same operation and a retained terminal result is replayed. Eligible same-GameSession reconnect preserves pending and terminal command identity.

Therefore GAME-INTERACTION must not create a competing client-command identity. A child occurrence is a semantic sub-occurrence beneath an already accepted root source occurrence, not a replacement for `CommandRef`.

### 2.2 PROVEN — SIM requires retry-stable semantic RNG identity

`SIM-DETERMINISM-01_AUTHORITATIVE_SIMULATION_CONTRACT.md` requires gameplay RNG identity to derive from stable semantic occurrence identity and stable purpose paths. It expressly forbids thread, worker, pointer, NodeId, unordered-container position or transient generation as semantic RNG identity, and says an idempotently retried logical occurrence must not reroll merely because runtime ownership moved.

Therefore child fan-out needs a stable sibling discriminator before deterministic RNG can be correct.

### 2.3 PROVEN — DUR-03 already demonstrates the required ambiguity discipline

`DUR-03_ITEM_TRANSACTION_AND_ANTI_DUPLICATION_CONTRACT.md` treats a mixed runtime/durable operation as one stable transaction/operation. Known commit is finalized, known abort may release/retry, ambiguous completion remains reserved until the same transaction is reconciled, and a stale completion cannot mutate a newer runtime owner.

GAME-INTERACTION should reuse that semantic discipline rather than invent blind retry.

### 2.4 PROVEN — public errors require more than a category name

`docs/contracts/FOUNDATION_ERROR_VOCABULARY.md` requires a public or cross-component failure to have:

- stable machine category;
- contract-owned code;
- `RETRYABLE`, `TERMINAL` or `SECURITY_TERMINAL` progression;
- explicit retry authority, including same/new command/session or owner intervention;
- safe correlation;
- idempotency and partial-mutation outcome;
- bounded internal-to-public mapping.

`FND-04C_ERROR_DIAGNOSTICS_FAILURE_COMPATIBILITY_CONTRACT.md` provides an accepted pattern: ambiguous issuance/recovery uses the same attempt reference; stale candidates fail closed; public classes are bounded; a new authority attempt is not created until the prior ambiguous attempt is retired or reconciled.

## 3. Finding 1 — why a root occurrence is insufficient

A root source occurrence can legitimately fan out to multiple independent semantic children.

Example:

```text
one committed movement occurrence M
  -> pressure plate A / ON_ENTER
  -> hazard B / ON_CONTACT
  -> scripted trigger C / ON_ENTER
```

If deduplication uses only `M`, all siblings collapse into one key. If the implementation instead appends whichever index happened to be produced by a hash map or worker completion order, replay can assign different keys and deterministic RNG streams after restart. If it generates fresh UUIDs on each dispatch, retry cannot prove that a re-delivered child is the same semantic occurrence.

The missing identity must therefore distinguish siblings while remaining reproducible from authoritative source semantics.

## 4. Proposed child-occurrence identity

The proposed value is `InteractionChildOccurrenceRef`:

```text
InteractionChildOccurrenceRef = (
    RootSourceOccurrenceRef,
    InteractionDefinitionRef,
    AuthoritativeTargetDiscriminator,
    TypedEdgeOrCapabilityDiscriminator,
    OptionalCanonicalChildOrdinal,
    SemanticRevisionContext
)
```

This is a composite semantic value, not a globally allocated UUID and not a new root operation namespace.

### 4.1 `RootSourceOccurrenceRef`

This is exactly the accepted source occurrence already owned by the relevant upstream domain, for example:

- client interaction command -> `CommandRef`;
- movement-derived interaction -> committed authoritative movement occurrence reference;
- timer-derived interaction -> stable timer occurrence identity;
- delegated/coupled workflow -> accepted owner operation/transaction/cause reference;
- event-derived interaction -> accepted event occurrence identity.

The child never upgrades a client hint, visual selection, pointer or local callback into authority.

### 4.2 `InteractionDefinitionRef`

A stable authored/compiled interaction-definition or interaction-object semantic identity from the exact bound content artifact/revision.

It identifies the behavior definition being executed, not a process object address or loader slot.

### 4.3 `AuthoritativeTargetDiscriminator`

A deterministic discriminator for the authoritative target/object resolved by the server in the applicable World/Channel/Instance scope.

It may be a strong semantic object/entity identity or a canonical typed world-object key accepted by the owning contract. It must not be:

- a client-supplied target hint;
- pointer/address identity;
- hash bucket;
- container/vector discovery position;
- transient stack slot whose numbering can change after recovery;
- an ordering index standing in for real target identity.

If the domain cannot name a stable authoritative target discriminator, that interaction family is not implementation-ready.

### 4.4 `TypedEdgeOrCapabilityDiscriminator`

The same target may expose multiple distinct semantic edges/capabilities, such as `ON_ENTER`, `ON_LEAVE`, `ON_CONTACT`, `USE`, or a versioned authored edge key.

This discriminator is a stable typed semantic key. It prevents two distinct edges on one object from collapsing into one child.

### 4.5 `OptionalCanonicalChildOrdinal`

The ordinal is **absent by default**.

It is allowed only where the accepted interaction definition intentionally permits multiple semantically distinct children that would otherwise have identical tuple fields. In that case:

- the multiplicity must be explicit in authored/compiled semantics;
- ordinal assignment must follow an explicit authored order or a canonical comparator over stable semantic fields;
- the same content revision must reproduce the same ordinal;
- runtime enumeration, hash-map iteration, DB row order without `ORDER BY`, thread scheduling or worker completion order must not assign it.

If two configured children are accidentally indistinguishable and no semantic multiplicity is declared, validation should reject the interaction definition rather than inventing an ordinal at runtime.

An ordinal is therefore a semantic discriminator of last resort, never a patch over unstable enumeration.

### 4.6 `SemanticRevisionContext`

The identity binds the behavior-affecting immutable semantic revision context required to interpret the child, such as applicable:

- exact World Bundle/content artifact identity;
- interaction-definition revision;
- ruleset/world-policy revision;
- SIM profile revision;
- script artifact/profile revision when a proposal-only script participates;
- other accepted behavior-affecting revision owned by the delegated domain.

A retry/replay continues under the exact bound semantic context for that logical occurrence or fails through an explicit compatibility/reconciliation rule. It never silently reinterprets an old child against the newest content.

### 4.7 Why ownership generation is not part of logical child equality

Runtime ownership generation and relevant state/domain revisions remain mandatory **fences**, but transient ownership generation must not make the same logical child become a different child after failover.

Otherwise:

```text
child under generation 7 != child under generation 8
```

would incorrectly authorize duplicate execution after ownership moves.

The correct separation is:

```text
logical child identity = stable semantic occurrence tuple
application authority = current generation/revision/fence validation
```

A stale-generation completion is rejected before mutation. The replacement owner then reconciles the same logical child/owner operation under current authority.

State/domain revisions that are behavior-affecting immutable semantic inputs belong in the bound semantic context; mutable observed revisions used only for optimistic/fencing checks remain preconditions/evidence rather than identity components.

## 5. Equality, representation and storage consequences

`InteractionChildOccurrenceRef` equality is tuple equality over the defined semantic fields.

A later implementation may encode or derive a compact digest for transport/storage efficiency, but:

- the digest is a representation of the tuple, not a new semantic UUID;
- collision handling must preserve tuple semantics;
- this successor does not select a hash algorithm, binary layout, database schema or retention count;
- opaque diagnostic correlation IDs are never idempotency authority.

The architecture needs the semantic identity now; physical representation remains deliberately deferred.

## 6. Deterministic child-plan/manifest rule

A stable key alone is insufficient if recovery re-enumerates children from changed mutable state. The root occurrence therefore needs a deterministic child plan at the point at which child execution becomes authoritative.

Conceptually:

```text
InteractionChildPlan {
    root_source_occurrence
    exact_semantic_revision_context
    ordered_child_occurrence_refs[]
    required precondition/fence evidence
}
```

The implementation shape/storage is not frozen. The semantic rules are:

1. server resolves eligible targets/edges authoritatively;
2. collection is canonicalized by accepted stable semantics before child acceptance;
3. every child reference is derived deterministically;
4. once any child can commit or a foreign owner can accept delegated work, recovery must reproduce the same accepted child set/order from retained authoritative evidence or immutable bound content/state; it must not rediscover siblings against a newer mutable world and treat them as the original occurrence;
5. stale generation/revision/fence fails closed before applying a child/completion;
6. each child is reconciled independently.

A runtime may internally track states equivalent to:

```text
UNSTARTED | PENDING | COMMITTED | REJECTED
```

without this document choosing a physical ledger.

## 7. Child-level exactly-once and retry rules

For one `InteractionChildOccurrenceRef`:

- `COMMITTED` -> never apply again; replay returns/reconstructs the same semantic outcome;
- `PENDING` -> reconcile the same delegated/coupled owner operation; do not create a second operation;
- `REJECTED` -> the occurrence is terminal; replay does not reevaluate it as the same occurrence;
- `UNSTARTED` after recoverable interruption -> evaluate/execute once using the already bound child identity and semantic context, provided current fences authorize progress.

Different siblings have different `InteractionChildOccurrenceRef` values and therefore cannot collapse into one dedup entry.

## 8. RNG binding

For an authoritative random decision owned by a child, the stable semantic anchor is equivalent to:

```text
RngDecisionRef = (
    InteractionChildOccurrenceRef,
    RngPurposeKey,
    DeterministicDrawOrdinal
)
```

The exact SIM-approved algorithm remains SIM-owned.

Rules:

- retry/replay/recovery uses the same child and same purpose/draw identity;
- a failed/stale delivery does not obtain a fresh random draw;
- draw order is semantic, not physical scheduling order;
- adding a sibling or unrelated purpose does not perturb another child's purpose stream unless the owning accepted mechanics explicitly define such coupling;
- seed/root evidence remains server-controlled and may be security-sensitive.

## 9. Finding 2 — caller-visible operation state must be explicit

A public/cross-owner result needs an orthogonal semantic state:

```text
COMMITTED | PENDING | REJECTED
```

### 9.1 `COMMITTED`

The required semantic commit point for this interaction occurrence is proven complete exactly once.

For a named coupled workflow, `COMMITTED` is legal only when that workflow's coordinator/owner contract proves the entire declared atomic semantic unit committed. A local participant cannot advertise global `COMMITTED` merely because its local mutation succeeded.

### 9.2 `PENDING`

Final outcome is not yet safely classifiable. The caller receives enough safe correlation to reconcile the **same** occurrence/owner operation.

`PENDING` means:

- no blind fresh retry of the same semantic intent;
- no new client `CommandRef` for the same intent while the old command/child may still commit;
- same `InteractionChildOccurrenceRef` remains the idempotency identity;
- same delegated `OwnerOperationRef`/TransactionId/attempt ref is reused when one exists;
- local mutation state is explicitly reported as `NOT_COMMITTED`, `COMMITTED`, or `UNKNOWN` where cross-owner ambiguity makes that distinction relevant;
- final authority remains with the named operation/workflow owner.

A reconnect may use a new transport generation and, where FND-04 requires, a different session recovery path. That transport/session action does **not** create a second semantic child operation.

### 9.3 `REJECTED`

The original occurrence is terminal and no pending foreign operation can still commit it.

A safe fresh user/domain attempt, when policy permits, is a **new root source occurrence**. For a client command this means a new `CommandRef` in the current valid GameSession (or a new valid GameSession only when FND-04 requires it). Reusing the old `CommandRef` only reconciles/replays the old terminal result; it never becomes a new attempt.

## 10. Correlation envelope

A cross-owner/client-visible interaction result needs, as applicable and safe:

```text
RootSourceOccurrenceRef
InteractionChildOccurrenceRef
semantic scope identity (WorldId / ChannelId / InstanceId as applicable)
exact bound semantic revision reference
InteractionOutcomeState = COMMITTED | PENDING | REJECTED
stable error category
contract-owned symbolic error code
OwnerOperationRef?   // only when a foreign owner accepted work
LocalMutationState?  // NOT_COMMITTED | COMMITTED | UNKNOWN when relevant
safe diagnostic/correlation reference?
```

`OwnerOperationRef` is a typed reference to an identity owned by the delegated contract (for example DUR-03 TransactionId/OperationId). GAME-INTERACTION does not create a new generic global `OperationId` definition.

Raw internal exceptions, credentials, seed material, row keys or security-sensitive evidence are not public correlation.

## 11. Proposed GAME-INTERACTION public error semantics

The successor owns stable symbolic GAME-INTERACTION codes for conditions it can classify. Numeric protocol registration remains future FND-02/gameplay-schema work.

### 11.1 Dependency unavailable before acceptance

`GI_DEPENDENCY_UNAVAILABLE_REJECTED`

- category: `DEPENDENCY_UNAVAILABLE`;
- progression: `RETRYABLE` for a **fresh attempt**, but the original occurrence is terminal `REJECTED`;
- legal only when no foreign owner operation was accepted and no local authoritative mutation committed;
- same source/CommandRef only replays the rejection;
- new user/domain attempt requires a new root occurrence/new `CommandRef` if still authorized;
- final reconciliation owner: interaction runtime, because no foreign operation exists.

### 11.2 Dependency unavailable after acceptance or with acceptance ambiguity

`GI_DEPENDENCY_UNAVAILABLE_PENDING`

- category: `DEPENDENCY_UNAVAILABLE`;
- progression: `RETRYABLE` **for reconciliation of the same occurrence only**;
- state: `PENDING`;
- retain same child + same `OwnerOperationRef`;
- no new `CommandRef` for the same semantic intent until final outcome is proven;
- local mutation may be `NOT_COMMITTED`, `COMMITTED`, or `UNKNOWN` only as the named workflow contract permits and reports;
- final reconciliation owner: the accepted foreign operation owner or named coupled-workflow coordinator; interaction runtime maps the result.

### 11.3 Timeout before any accepted/committed work

`GI_TIMEOUT_REJECTED`

- category: `TIMEOUT`;
- progression: `RETRYABLE` as a fresh occurrence;
- state: `REJECTED`;
- legal only when timeout is proven to have occurred before any operation acceptance or authoritative mutation that could later commit;
- same old CommandRef cannot be reused as a new attempt;
- fresh attempt uses new root occurrence/new CommandRef.

### 11.4 Timeout after possible acceptance/commit

`GI_TIMEOUT_PENDING`

- category: `TIMEOUT`;
- progression: `RETRYABLE` for same-occurrence reconciliation;
- state: `PENDING`;
- same child + same foreign operation identity;
- no new CommandRef for the same intent while pending;
- local mutation may already have committed; caller sees explicit local mutation state where relevant;
- final owner is the delegated operation/workflow owner.

### 11.5 Cancellation proven before commit

`GI_CANCELLED_REJECTED`

- category: `CANCELLED`;
- progression: `TERMINAL` for the original occurrence;
- state: `REJECTED`;
- legal only when accepted participants are either absent or have all proven cancellation/retirement before the semantic commit point;
- no mutation remains able to commit;
- a later user action is a new intent/new root occurrence/new CommandRef.

### 11.6 Cancellation race/ack ambiguity

`GI_CANCELLED_PENDING`

- category: `CANCELLED`;
- progression: `RETRYABLE` for same-occurrence reconciliation;
- state: `PENDING`;
- cancellation request is not proof of cancellation;
- if the owner later proves prior commit, final state is `COMMITTED`;
- if it proves cancel-before-commit, final state is `REJECTED` with cancellation;
- if neither is yet proven, remain `PENDING`;
- same child/foreign operation identity is retained; no fresh command for the same intent.

### 11.7 Stale delegated completion

`GI_STALE_COMPLETION_REJECTED`

- category: `STALE_GENERATION`;
- progression: `TERMINAL` for the stale completion message/application attempt;
- stale completion performs no mutation under the newer owner;
- this code does **not** by itself prove that the underlying foreign operation rejected or failed;
- if the underlying operation's final outcome is uncertain, the interaction occurrence remains `PENDING` under its same child/OwnerOperationRef and reconciliation continues with the current owner;
- if the current owner already knows the underlying terminal result, it surfaces that terminal result rather than guessing from the stale message.

This separation prevents stale-delivery rejection from being mistaken for semantic operation rollback.

### 11.8 Generic reconciliation unavailable

`GI_RECONCILIATION_REQUIRED`

- category: `INTERNAL_UNAVAILABLE`;
- progression: `RETRYABLE` for bounded reconciliation of the same occurrence;
- state: `PENDING`;
- used only when no narrower truthful public category owns the current wait condition;
- same child/foreign operation reference is retained;
- no new semantic attempt until the old occurrence is classified terminal;
- owner intervention becomes permissible only after the owning contract's bounded automatic reconciliation policy is exhausted; this successor does not invent numeric retry counts.

## 12. Narrow foreign codes remain foreign-owned

GAME-INTERACTION must not flatten every foreign failure into a guessed local code.

### DUR-03 item/value workflows

`docs/architecture/DUR-03_ITEM_TRANSACTION_AND_ANTI_DUPLICATION_CONTRACT.md` owns TransactionId/OperationId, value linearization and durable reconciliation. Interaction maps DUR-03 outcomes into its bounded public state/category without redefining item transaction codes or commit authority.

### GAME-ABILITY effects

GAME-ABILITY owns effect legality/formulas/effect operation semantics. The current whole-gate candidate PR #268 is unmerged/blocked at this analysis baseline. Ability-trigger integration that needs final narrow effect codes/operation references is implementation-blocked until the Architecture Coordinator accepts the relevant GAME-ABILITY contract. This successor does not adopt PR #268 as canonical truth.

### Movement/relocation/handoff

The final movement/teleport/handoff owner is deliberately unresolved by this task. Any interaction requiring a cross-owner relocation operation is implementation-blocked until a named accepted movement/handoff contract defines its operation identity, completion and narrow errors.

### Durable writable text

The durable writable-text owner remains deliberately unresolved. Interactions requiring that durable authority remain implementation-blocked until a named accepted owner contract exists.

### Session/admission/transport failures

FND-02/FND-04/FND-04C own session/generation/admission/recovery codes. GAME-INTERACTION must propagate/map them boundedly without inventing replacement session authority or retry semantics.

## 13. Coupled workflows

The predecessor rule remains: no generic cross-domain multi-owner transaction abstraction is authorized merely because interactions can touch several domains.

Each accepted coupled workflow must name:

- workflow coordinator/final reconciliation owner;
- stable workflow/owner operation reference(s);
- participants and exact authority boundaries;
- current generation/revision/fence evidence;
- semantic commit point or accepted prepare/commit equivalent;
- timeout handling;
- cancellation semantics;
- ambiguity reconciliation;
- crash/recovery behavior;
- idempotency and compensation only where the owning contract explicitly permits compensation;
- bounded public error mapping.

Until such a workflow contract exists for a mechanic, that mechanic is implementation-blocked. The caller never guesses whether local success means whole-workflow success.

## 14. Reconciliation owner matrix

| Interaction family | Final semantic/reconciliation owner | GAME-INTERACTION responsibility |
|---|---|---|
| interaction-local state only | current authoritative FND-03 runtime owner in the exact World/Channel/Instance scope | child dedup, fences, result state/code |
| DUR-03 item/value | DUR-03 transaction owner/coordinator | preserve child/source correlation; boundedly map durable result |
| GAME-ABILITY effect | accepted GAME-ABILITY effect owner | preserve trigger child/source correlation; do not own formulas/effect commit |
| movement/relocation/handoff | **BLOCKED** until named owner contract exists | do not infer owner; keep delegation boundary |
| named coupled workflow | workflow's explicitly accepted coordinator | never claim whole `COMMITTED` from one participant's local success |
| client command/result identity | FND-02 session command stream | map child outcomes into the already-reserved CommandRef; never create competing command identity |

## 15. Deterministic acceptance scenarios

### GI-SR-01 — one movement occurrence, N contacts, partial delivery and recovery

Given:

- committed authoritative movement occurrence `M`;
- exact semantic revision context `R`;
- authoritative contacted objects `A`, `B`, `C` discovered in an arbitrary physical container order;
- canonical semantics order them as `A`, `B`, `C` and derive distinct child refs `C1`, `C2`, `C3`;
- every random child decision uses `(Ci, purpose, draw_ordinal)`.

Execution:

1. `C1` commits locally.
2. `C2` is accepted by a delegated owner as operation `O2` and becomes `PENDING`.
3. runtime fails before `C3` commits.
4. replacement owner recovers under a newer ownership generation.
5. stale completion from old generation for `C2` arrives.

Required outcome:

- stale completion cannot mutate replacement authority;
- `C1` is recognized as already committed and is not applied twice;
- `C2` remains the same child and reconciles the same `O2`; it is not redispatched as a fresh owner operation;
- `C3` executes at most once under its already-derived child identity if current fences authorize progress;
- the full child set/order remains `C1,C2,C3`, independent of hash/container/worker order;
- retries/replay use the same RNG purpose identities and cannot reroll any child;
- after reconciliation each child has one terminal result, exactly once;
- replay under `R` reproduces the same semantic child plan and outcomes.

### GI-SR-02 — dependency unavailable before owner acceptance

If a dependency is proven unavailable before any delegated owner accepts work and before local mutation, return `GI_DEPENDENCY_UNAVAILABLE_REJECTED`. The original CommandRef is terminal. A future fresh user attempt, if permitted, uses a new CommandRef; replaying the old one returns the same rejection.

### GI-SR-03 — timeout after possible owner acceptance

If a delegated request may have been accepted when timeout occurs, return `GI_TIMEOUT_PENDING`, retain the same child and `OwnerOperationRef`, and reconcile. Issuing a fresh CommandRef for the same semantic intent while the old operation could still commit is invalid.

### GI-SR-04 — cancel race with commit

A cancellation request races with a delegated commit:

- proof commit won -> `COMMITTED`;
- proof cancellation retired the operation before commit -> `GI_CANCELLED_REJECTED`;
- neither provable yet -> `GI_CANCELLED_PENDING`.

Cancellation never retroactively rewrites a proven commit and ambiguity never authorizes blind re-execution.

### GI-SR-05 — stale delegated completion

A completion produced under stale ownership generation is rejected before mutation. The underlying same owner operation is then reconciled through current authority. Stale-message rejection does not create a new child, new owner operation or new RNG stream.

### GI-SR-06 — coupled workflow pending

A named coupled workflow has one participant committed locally and another unresolved. Caller-visible whole-workflow state remains `PENDING`; only the named workflow coordinator may eventually classify the semantic unit `COMMITTED` or terminally `REJECTED` according to that workflow's accepted contract.

## 16. Decision-timing test

### Must decide now? YES

Child identity and cross-owner retry/result semantics block safe implementation of interaction fan-out, deterministic replay, idempotent recovery and client/cross-component result handling.

### Concrete downstream work blocked

- child-level dedup/ledger design;
- deterministic child RNG binding;
- recovery/failover replay of movement/contact cascades;
- public gameplay command result schemas;
- delegated owner adapters;
- named coupled workflow implementation.

### What becomes harder or impossible if deferred

If runtime starts with root-only dedup or unstable sibling indices, later repair risks changing persisted/replayed semantic identities and can expose double application/reroll behavior. If callers ship without committed/pending/rejected and same-vs-new attempt rules, retry behavior becomes API folklore and can duplicate value/effects.

### What evidence would justify superseding this decision

A later accepted architecture may supersede the tuple shape only if it proves equivalent or stronger sibling uniqueness, retry/replay stability, deterministic RNG identity and foreign-owner reconciliation without global mutable identity drift.

### Deliberately undecided

- physical digest/hash/serialization;
- database/storage schema and retention counts;
- numeric protocol error values;
- numeric queue/retry/resource ceilings;
- movement/handoff owner;
- writable-text owner;
- GAME-ABILITY formulas/effect internals;
- runtime/service/crate topology.

## 17. Preserved predecessor invariants

This successor does not reopen:

- server-authoritative target resolution;
- typed/versioned state machines;
- explicit scope/lifetime/reset/recovery;
- GAME-ITEM + DUR-03 item/value authority;
- GAME-ABILITY effect authority;
- movement/handoff delegation;
- named coupled workflows instead of a generic distributed transaction;
- bounded deterministic cascades;
- DUR-04 proposal-only scripts;
- exact deterministic semantic revisions/order/RNG;
- prohibition on generic process-global mutable interaction scope.

## 18. Cross-domain findings

`NONE NEW`.

Inherited dependencies remain explicit:

- GAME-ABILITY final whole-gate integration is not canonical while #268 is unmerged/blocked;
- movement/handoff owner remains an explicit future blocker for relocation mechanics;
- durable writable-text owner remains an explicit future blocker for durable text mechanics.

This successor reports those boundaries but does not resolve them.

## 19. Recommended contract disposition

**RECOMMENDATION:** accept the successor candidate only if coordinator audit confirms that:

1. child tuple identity is source-derived, deterministic and independent of transient runtime enumeration/generation;
2. exact semantic revisions remain bound while mutable generation/revisions remain fail-closed fences;
3. every ambiguous cross-owner case stays `PENDING` and reconciles the same semantic attempt;
4. a new `CommandRef` is created only for a genuinely new attempt after the prior occurrence is terminal;
5. foreign owners remain foreign-owned and missing narrow contracts block implementation rather than inviting inference.

`NEXT_ACTION: ARCHITECTURE_COORDINATOR_AUDIT`
