# GAME-CHAR-01 — Stage B B1-B3 Evidence Acquisition

- Status: **EVIDENCE ACQUISITION / NONBINDING / NOT ACCEPTED**
- Date: 2026-08-11
- Gate: `GAME-CHAR-01` Stage B
- Reference target: Global Tibia production-observable behavior after the 2026-07-28 server-save/maintenance change boundary
- Scope: B1 naming, B2 deletion/quota, B3 creation/starter only
- Trusted repository base: `blakinio/Oteryn-v2@1411994c70abbf065273c0502c88413b61ca5ca0`
- Does not authorize: Stage-B acceptance, overall GAME-CHAR acceptance, runtime/client/protocol/persistence/content implementation, physical schema or intentional Reference differences

## 1. Executive result

This evidence pass reduces **B1 naming** and **B3 creation/starter** uncertainty but does not close either blocker completely. **B2 deletion/quota remains materially unresolved for the July-28 target** beyond the already strong 25-active-character continuity evidence.

No owner decision is required yet.

### Result by blocker

- **B1 naming:** partial progress. Tibia-wide name uniqueness is historically explicit and rename-history/search retention for six months has strong before/after primary continuity. Exact July-28 normalization, 29-character limit continuity, full permitted repertoire and deleted-name recycling remain unresolved.
- **B2 deletion/quota:** little progress beyond the active limit. Current official manual clearly states 60-day reversible deletion, maximum 30 active+scheduled characters and at-least-six-month deleted-name hold, but this pass did not locate reliable target-era primary continuity for those exact values. They remain `UNKNOWN` for the target.
- **B3 creation/starter:** meaningful chronology established. Newhaven and vocation-selection flow are primary-evidenced before the target; Targuna replaced the post-Newhaven Thais/Blue Valley route before July 28. Exact starter stats/items/home-state and exact target-era skip-tutorial starting state remain unresolved.

## 2. Evidence-method rule

This report follows the accepted first-Reference evidence model:

- `PROVEN`
- `OBSERVED`
- `DERIVED`
- `UNKNOWN`
- `CONFLICT`
- `DECLARED_DIFFERENCE`

Current official documentation is primary **current** evidence, not automatic July-28 historical proof. Historical official announcements can establish dated rules or changes. A before/after match with no known contradiction may support `DERIVED` continuity, but absence of a discovered change notice is never enough by itself.

The available search pass also attempted to locate archived/historical copies of the official account manual around July 28. It did not yield a provenance-clear target-era snapshot for the B2 numeric rules. That negative result is recorded as an evidence limitation, not evidence that the current values differed or matched.

## 3. B1 — naming evidence

### 3.1 Tibia-wide uniqueness

Official April 2, 2008 news explicitly described Tibia's policy as one in which every character across all then-existing game worlds had a unique name, contrasting it with games where uniqueness existed only per server.

Primary source:

- `https://www.tibia.com/news/?id=708&subtopic=latestnews` — **Tibia Character Names - Now and in the Future**, 2008-04-02.

Current official character creation/name-change surfaces continue to require a new name to be available before creation/rename succeeds.

### Classification

**`DERIVED` strong continuity candidate:** character-name uniqueness is game-wide/Tibia-wide rather than per-world.

### What this is sufficient to constrain

Character Authority should not design July-28 Reference naming as a per-WorldId namespace merely because Oteryn has explicit worlds/channels. The Reference-facing namespace needs to preserve the evidence of global uniqueness unless later target evidence proves a scoped exception.

### What remains open

The exact machine-level uniqueness implementation is not yet proven, including:

- normalization before uniqueness comparison;
- case folding;
- whitespace folding/trimming;
- locale/Unicode handling;
- historical alias reservation interactions;
- whether any reserved/system namespace is evaluated before or after canonicalization.

Therefore the final database unique-index expression remains **not freeze-ready**.

## 4. B1 — technical name format

Official April 8, 2008 patch notes state that new technical limits prohibited:

- names with more than three words;
- names containing special characters such as a hyphen.

Primary source:

- `https://www.tibia.com/news/?id=716&subtopic=newsarchive` — **Minor Patch Released - New Tibia Rules Valid Now!**, 2008-04-08.

Current official creation documentation states additional/current constraints including:

- maximum 29 letters;
- no numbers;
- no special characters;
- some words/letter combinations disallowed;
- Tibia Rules still apply.

### Classification

- three-word/special-character historical restriction family: **`DERIVED` continuity support**, not an exact July-28 parser specification;
- exact `29` maximum at July 28: **`UNKNOWN` target continuity**;
- exact valid character repertoire/canonicalization: **`UNKNOWN`**;
- exact reserved-word/restricted-pattern revision: **`UNKNOWN`**.

The 2008 rules show that technical format constraints are long-lived product semantics, but they are not sufficient to reconstruct the 2026 validator byte-for-byte.

## 5. B1 — rename history and aliases

Official February 19, 2010 introduction of Character Name Change states that after a rename:

- the old character name is listed on the character page for six months;
- the character remains findable by the old name for six months.

Primary source:

- `https://www.tibia.com/news/?id=1240&subtopic=newsarchive` — **Release of New Extra Services**, 2010-02-19.

Current official Store/product manual still states that the old name remains usable for six months in the Lost Account Interface or Characters search after a rename.

Current source:

- `https://www.tibia.com/gameguides/?section=products&subtopic=manual` — Character Name Change section.

### Classification

**`DERIVED` strong continuity candidate:** six-month old-name lookup/history after rename.

### Architecture consequence

Name history/alias projection is semantically distinct from current authoritative name reservation. CharacterId remains stable through rename under Stage A. A former name may remain a searchable alias even though it is no longer the current display name.

The exact storage/index/expiry mechanism remains DUR-02 work after target semantics are accepted.

## 6. B1 — deleted-name reuse is not the same rule

The current account manual states that names of deleted characters cannot be chosen for new characters for **at least six months**.

Current official support material also warns that a deleted character's former name may remain unavailable for several months or even years depending on multiple factors.

This is semantically different from the fixed six-month **rename-history/search** rule introduced in 2010.

### Classification

- current deleted-name hold minimum `>= 6 months`: `PROVEN` current behavior/documentation;
- exact July-28 continuity: `UNKNOWN`;
- exact release algorithm/timing after permanent deletion: `UNKNOWN`;
- treating deleted-name release as exactly six months: **rejected** by current primary evidence.

### Architecture consequence

Do not model deleted-name recycling as `retired_at + 6 months = available` merely by analogy with rename history.

## 7. B1 result

B1 is **reduced but not closed**.

Strong candidates now exist for:

1. Tibia-wide/global name uniqueness;
2. long-lived technical-format restrictions as a rule family;
3. six-month old-name lookup/history after rename.

Still blocked:

- exact July-28 29-letter continuity;
- canonical normalization/case/space rules;
- exact permitted repertoire;
- restricted/reserved pattern authority;
- deleted-name release timing/algorithm;
- exact rename collision/history mechanics beyond the six-month lookup fact.

## 8. B2 — active-character quota

Official February 24, 2025 Monk product-management material announced that the character limit for all accounts would increase from 20 to 25. Official March 2025 live changes then stated that the limit had been increased from 20 to 25.

Primary sources include:

- `https://www.tibia.com/news/?id=8260&subtopic=latestnews` — **Monk: Product Management Insight Part 2**, 2025-02-24;
- `https://www.tibia.com/news/?id=8307&subtopic=newsarchive` — live Monk/balancing changes confirming the increase.

The current official account/creation manuals still state 25 active characters.

### Classification

**`DERIVED` strong continuity candidate:** maximum 25 active characters at the July-28 target.

This remains stronger than current-only evidence because the change is explicitly dated before the target and the same value is documented after the target.

## 9. B2 — current deletion/undelete contract

Current official account manual states:

- manual character deletion is not final for 60 days / two months;
- during that period the deletion can be cancelled through Undelete Character;
- after final deletion the character cannot be recovered;
- deletion-scheduled characters do not count as active;
- active characters may not exceed 25;
- active + scheduled-for-deletion characters may not exceed 30;
- undelete may fail until another active character is scheduled for deletion when the 25-active limit would otherwise be exceeded;
- deleted names cannot be chosen for new characters for at least six months.

Current source:

- `https://www.tibia.com/gameguides/?section=accounts&subtopic=manual`.

### Historical-target search result

The targeted official-news/search pass did not locate a dated primary introduction/change record for:

- `60 days` / two-month manual deletion grace;
- total `30` active+scheduled limit;
- exact undelete/quota interaction;
- deleted-name minimum hold.

Attempts to locate provenance-clear archived snapshots of the official account manual around July 28 through available web search also did not produce a target-era snapshot.

### Classification

For the July-28 target:

- deletion grace = 60 days: `UNKNOWN` continuity;
- scheduled deletion excluded from active quota: `UNKNOWN` continuity;
- total 30: `UNKNOWN` continuity;
- undelete active-quota interaction: `UNKNOWN` continuity;
- final deletion irreversible: likely consistent with Stage-A semantics but exact target public workflow remains `UNKNOWN` from this evidence pass;
- deleted-name minimum hold: `UNKNOWN` continuity.

### Important negative conclusion

This task **does not** infer continuity merely because no contrary patch note was found.

## 10. B2 interaction with Stage A

The evidence gap does not threaten the accepted baseline-neutral lifecycle:

```text
ACTIVE
-> DELETION_SCHEDULED
-> RETIRED
```

Stage A already safely captures:

- reversible nonterminal deletion intent;
- terminal retirement distinct from temporary scheduling;
- no CharacterId reuse after retirement;
- privacy erasure as a separate data-lifecycle concern.

B2 therefore blocks **numeric/product-policy parameters and exact Reference workflow**, not the safe semantic lifecycle boundary.

## 11. B2 result

B2 remains **open**.

Freeze-ready/strong candidate:

- 25 active characters: `DERIVED` strong continuity.

Still target-`UNKNOWN`:

- 60-day grace;
- total 30;
- exact undelete constraints;
- exact deleted-name hold/release.

No owner preference is useful yet; this remains a historical-evidence problem.

## 12. B3 — Newhaven and vocation-selection anchor

Official October 2025 Newhaven rollout material provides a strong pre-target creation/early-game anchor.

Official October 15, 2025 teaser states that:

- a redesigned tutorial begins the new-player flow;
- after finishing it, the player may teleport to Rookgaard or take the portal to Newhaven;
- in Newhaven the player selects a vocation through a new pop-up;
- Newhaven contains the early progression services/areas;
- the western exit requires level 8 and account email confirmation.

Primary source:

- `https://www.tibia.com/news/?id=8543&subtopic=newsarchive` — **A New Helping Hand II**, 2025-10-15.

Official October 8, 2025 material also states that players can no longer change vocation after their initial choice or return to Newhaven after leaving it.

Primary source:

- `https://www.tibia.com/news/?id=8541&subtopic=newsarchive` — **A New Helping Hand**, 2025-10-08.

Official October 21, 2025 release states Newhaven opened as Tibia's new entry point and Dawnport was retired.

Primary source:

- `https://www.tibia.com/news/?id=8553&subtopic=newsarchive`.

### Classification

- Newhaven as entry/progression area before July 28: `PROVEN`;
- tutorial → Rookgaard-or-Newhaven fork: `PROVEN` pre-target release semantics;
- vocation selection in Newhaven: `PROVEN` pre-target release semantics;
- no vocation change after initial choice / no return to Newhaven after leaving: `PROVEN` pre-target release semantics unless later target evidence supersedes it; no superseding evidence was established in this pass.

For exact July-28 continuity, these are strong pre-target anchors and are additionally corroborated by target-era Character Bazaar `Newhaven` quest-line state.

## 13. B3 — Targuna changed the level-8+ continuation before target

Official March 17, 2026 news states that from level 8 onward characters would no longer travel directly from Newhaven to Thais Peninsula; all characters, including monks, would instead continue to Targuna.

Primary source:

- `https://www.tibia.com/news/?id=8733&subtopic=newsarchive` — **Greater Lessons for Young Tibians**, 2026-03-17.

Follow-up March/April 2026 live-fix chronology refers to Targuna/Newhaven production behavior, showing the flow was live months before July 28.

The currently indexed official Quick Start still says Newhaven exits to Thais Peninsula and monks to Blue Valley.

Current source:

- `https://www.tibia.com/gameguides/?subtopic=quickstart`.

### Classification

- Targuna as post-Newhaven level-8+ continuation before target: `PROVEN` dated chronology;
- current Quick Start Thais/Blue Valley wording: `CONFLICT / stale official documentation` for July-28 route;
- target architecture must follow the dated production chronology, not the stale current paragraph.

## 14. B3 — current skip-tutorial starting state

Current official starting manual states that players who already have a character on the main continent may skip the tutorial and that those characters start at **level 2 in Newhaven**, ready to select a vocation.

Current source:

- `https://www.tibia.com/gameguides/?section=starting&subtopic=manual`.

### Historical search result

The targeted official-news search did not locate a dated 2025/2026 primary release note explicitly specifying the same `skip tutorial -> level 2 in Newhaven` value.

The 2025 Newhaven release material proves the tutorial/Newhaven/vocation architecture, but not this exact skip-start level.

### Classification

- current skip-tutorial level-2 rule: `PROVEN` current;
- exact July-28 continuity: `UNKNOWN`.

## 15. B3 — exact starter template remains unresolved

Historical official material proves that tutorials provide early equipment and that Newhaven is the vocation-selection/early-progression area, but this evidence pass does not establish a complete July-28 starter template including:

- exact initial level for every creation path;
- exact initial HP/mana/capacity/skill values;
- exact starter inventory/equipment/containers;
- exact home town/citizenship state;
- exact position/temple/respawn state;
- exact Rookgaard/Newhaven selection eligibility for every account state;
- exact retry/idempotency visible behavior of web/client creation;
- exact account-confirmation constraints at each transition.

These remain `UNKNOWN` for Stage B.

## 16. B3 — Character Bazaar corroboration

Official Character Bazaar pages indexed in 2026 include the `Newhaven` completed quest line on multiple characters, including entries whose character-title data was updated before the July-28 target.

This corroborates that Newhaven progression state was present in target-era durable/public character data.

It does **not** define which part of that quest/progression belongs in the core Character aggregate versus content/quest authority.

Stage A remains binding: public display on a character page does not transfer semantic ownership into Character.

## 17. B3 result

B3 is **reduced but not closed**.

Strong pre-target/target-aligned facts:

1. Newhaven replaced Dawnport as the new entry point before target;
2. redesigned tutorial feeds into a Rookgaard-or-Newhaven choice;
3. vocation selection occurs in Newhaven;
4. vocation cannot be casually changed after the initial Newhaven choice under the 2025 release model;
5. post-Newhaven level-8+ continuation was changed to Targuna before July 28;
6. stale current Quick Start content must not override dated production chronology.

Still unresolved:

- exact target-era skip-tutorial level 2 continuity;
- exact creation web/client input validation at target;
- full starter stats/items/template;
- exact home/citizenship/respawn fields;
- exact account-state eligibility and error semantics.

## 18. Revised B1-B3 blocker state

### B1 naming

**PARTIALLY REDUCED**

Strong candidates:

- global/Tibia-wide uniqueness;
- long-lived technical format-restriction family;
- six-month old-name lookup/history after rename.

Still blocked:

- exact normalization/case/space/repertoire;
- exact 29-character target continuity;
- reserved/restricted pattern revision;
- deleted-name recycling algorithm/timing.

### B2 deletion/quota

**LARGELY UNCHANGED**

Strong candidate:

- 25 active characters.

Still blocked:

- 60-day deletion continuity;
- total 30 continuity;
- undelete interaction;
- deleted-name hold/release.

### B3 creation/starter

**PARTIALLY REDUCED**

Strong anchors:

- Newhaven entry and vocation selection;
- no casual re-vocation/return-to-Newhaven under release model;
- Targuna continuation before target.

Still blocked:

- exact starter template;
- skip-tutorial level-2 target continuity;
- exact creation validation/error semantics;
- home/citizenship/respawn details.

## 19. Architecture consequences

This evidence pass reinforces several already accepted constraints without creating new binding architecture:

- Character Authority needs a game-wide Reference name namespace, not silently per-world uniqueness;
- current name, old-name searchable alias/history and deleted-name reservation are distinct concepts;
- B2 numeric deletion policies belong in a versioned Reference/product policy, not in the semantic lifecycle enum itself;
- starter state must remain a versioned ruleset/content template, not hard-coded Character constructor defaults;
- early-game route/quest content belongs to content/quest authority even when it affects character progression;
- final naming indexes, deletion timers and starter-state physical fields must not be frozen by DUR-02 until target semantics are accepted.

## 20. Evidence-acquisition stopping rule for B1-B3

This bounded pass made meaningful progress but reached diminishing returns for primary web evidence.

The next B1-B3 evidence improvement should come from one of:

1. provenance-clear archived official manual snapshots near July 28;
2. owner-provided historical official captures;
3. a rule-specific official change notice newly discovered through a narrower chronology;
4. controlled current observation only when continuity to July 28 can be independently evidenced.

Repeated general web search for the same 60/30/skip-level-2 phrases should not continue without a new hypothesis.

## 21. Owner decision result

**No owner decision required.**

This pass does not produce a complete target-accurate B1/B2/B3 owner package. Asking the owner to choose values that should be determined by Reference evidence would be premature.

If historical evidence remains unavailable later, the owner may need to choose an explicit Reference fallback/difference policy, for example adopting a current documented rule as a declared approximation. That decision is **not required yet**.

## 22. Next programme evidence work

Proceed autonomously to the next Stage-B blockers with high downstream leverage:

1. **B4 progression formulas / authoritative-vs-derived mapping**;
2. **B5 promotion continuity and entitlement boundary**;
3. then B6/B7 death-edge and offline-effectiveness evidence;
4. B8 modern build-state ownership in conjunction with GAME-ITEM/ability/content boundaries.

B1-B3 remain registered as open evidence gaps and should be revisited only when new primary historical evidence becomes available.

Until Stage B receives an owner-accepted complete evidence-backed contract, overall `GAME-CHAR-01` remains **PROPOSED / PLANNED / NOT_STARTED** and runtime/schema authority remains **NONE**.
