# ADR-0015: GameNode implementation shape is not yet frozen

- Status: Accepted clarification
- Date: 2026-08-11
- Decision ID: `GAMENODE-SHAPE-01`
- Supersedes: only the **binding interpretation** of (a) `ARCHITECTURE_REVIEW_REFINEMENTS_2026-08-10.md` statements that the first GameNode "should be a domain-modular monolith" and that the programme should "build a modular-monolith GameNode", and (b) `FOUNDATION_PROGRAMME_CURRENT_STATUS.md` Section 3 wording that the first GameNode implementation "should remain a domain-modular monolith until real deployment/security/data/failure boundaries justify separation". In all three locations the modular-monolith shape is a **nonbinding preferred starting hypothesis**, not frozen process/service topology.
- Preserves: FND-03 authoritative runtime ownership, domain/transport/persistence separation, bounded queues, one logical authoritative writer per scope, and the rule against speculative empty services/crates.
- Does not authorize: runtime implementation, microservice decomposition, Kubernetes, process topology, deployment changes, or production activation.

## Problem

The 2026-08-10 architecture review and current-status overlay correctly identify a modular monolith as the most conservative **working hypothesis** for the first GameNode, but their wording can be read as a binding topology decision.

That would freeze a process/service shape before the implementation programme has measured real scaling, failure-isolation, security-boundary and data-ownership pressures. Oteryn needs to preserve the recommendation without turning it into premature architecture authority.

## Constraints

Any future GameNode implementation-shape decision must preserve:

- gameplay/domain logic independent from Tokio sockets, Protobuf wire layout, PostgreSQL adapters and client UI/renderer state;
- one logical authoritative mutation owner per ChannelRuntime/InstanceRuntime scope;
- explicit world-shared authority instead of process-global mutable caches;
- bounded queues, bounded auxiliary work and stale-result rejection;
- no speculative empty services or crates merely to mirror diagrams;
- deployment/process separation only when justified by a real ownership, security, scaling or failure boundary.

## Options considered

### Option A — Freeze a domain-modular monolith now

Benefits:

- simplest initial deployment and debugging model;
- lowest distributed-systems overhead;
- aligns with the current small vertical-slice delivery strategy.

Risks:

- prematurely turns a reasonable implementation hypothesis into architecture authority;
- may later resist a justified security/data/failure boundary;
- lacks measured evidence from an actual native GameNode.

Disposition: **not accepted as a binding decision yet**.

### Option B — Freeze a multi-service GameNode architecture now

Benefits:

- explicit process isolation and independent scaling from day one.

Risks:

- introduces distributed coordination, deployment and observability cost before evidence;
- increases failure modes and operational surface;
- risks creating empty service boundaries without real independent ownership.

Disposition: **rejected for the current stage**.

### Option C — Keep topology open; retain modular monolith as the preferred starting hypothesis

Benefits:

- preserves the simplest likely implementation path without freezing it;
- lets vertical-slice evidence drive process/service separation;
- keeps domain boundaries independent from deployment topology;
- avoids both premature microservices and premature topology lock-in.

Costs:

- implementation planning must carry one explicit later decision gate;
- some deployment details remain intentionally unresolved.

Disposition: **selected**.

## Decision

The GameNode **process/service topology is not yet frozen**.

The current programme recommendation is:

> Start implementation discovery from a domain-modular monolith unless evidence demonstrates a stronger boundary.

This recommendation is **NONBINDING**. It must not be treated as accepted runtime topology merely because either the 2026-08-10 refinement or the canonical current-status overlay uses prescriptive wording.

Before any implementation task freezes GameNode process/service shape, its owning decision must explicitly answer:

1. Why must topology be decided at that point rather than remaining internal implementation detail?
2. Which concrete downstream work is blocked without the decision?
3. Which alternatives were compared, at minimum single-process modular monolith versus one or more separately deployed services?
4. Which security, data-ownership, independent-scaling, failure-domain or operational boundaries justify separation?
5. What measured evidence exists for CPU, memory, latency, noisy-neighbor and failure-recovery behavior?
6. What evidence would supersede the selected shape later?

## Current implementation guidance

Until that later gate exists:

- implementation tasks may use a modular-monolith spike or vertical slice as the default exploration path;
- they may not claim that topology as globally frozen architecture;
- a new crate or service still requires an immediate consumer and a real boundary;
- gameplay/domain semantics remain topology-independent.

## Decision timing

- **Must topology be decided now?** NO.
- **What must be decided now?** Only that the prior modular-monolith wording is a nonbinding recommendation rather than accepted topology authority.
- **Blocked downstream work:** a task that wants to freeze production GameNode process/service decomposition.
- **Evidence to supersede/open the later gate:** representative vertical-slice and load/failure/security evidence showing where process boundaries materially improve correctness, isolation or operations.

## Consequence

`ARCHITECTURE_REVIEW_REFINEMENTS_2026-08-10.md` and `FOUNDATION_PROGRAMME_CURRENT_STATUS.md` remain useful programme/status guidance, but for GameNode process/service topology this ADR takes precedence over their prescriptive modular-monolith wording: **modular monolith is the preferred starting hypothesis, not a frozen architecture requirement**.
