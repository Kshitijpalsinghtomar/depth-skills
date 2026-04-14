---
name: descend
codename: DESCEND
internal: Pattern Audit & First-Principles Derivation
version: 1.1
tier: cognition

trigger:
  - "nothing works"
  - "tried everything"
  - "familiar solution feels wrong"
  - "experts would disagree"
  - "best practices conflict"
  - "novel problem with no template"

description: Verifies whether the problem was correctly identified before solving, auditing pattern matches against first principles.

author: depth-skills

tags:
  - first-principles
  - pattern-audit
  - root-cause
  - derivation
  - novel-problems

artifacts:
  - pattern-identification-card
  - precondition-table
  - derivation-layers

composable_with:
  - excavate
  - reframe
  - invert
  - deep-think
---
# DESCEND — Pattern Audit & First-Principles Derivation

Every answer you generate is built from patterns — compressed experience retrieved from training: "In situations like X, do Y." This is efficient when the match is real.

It is catastrophic when it isn't. And you do not check.

**Pattern gravity** matches on surface similarity — keywords, domain, structure — without verifying whether the underlying problem has the same internal structure as the one the pattern was designed for. Problems that look alike on the surface can have completely different mechanics underneath. The pattern that solved one will silently damage the other.

This skill has two phases:
- **Phase 1: AUDIT** — is the pattern match real, or is it a surface-level false analogy?
- **Phase 2: DERIVE** — if the match is false, reason from fundamental truths upward.

---

## Phase 1: Pattern Audit

### Step 1 — MAKE THE PATTERN VISIBLE

Write down the pattern you are about to apply. Often you apply patterns unconsciously — the solution appears without explicit acknowledgment of its source.

```
PATTERN IDENTIFICATION
────────────────────────────────────────
Pattern I'm applying:  [name or description of the template/approach]
Source domain:         [what type of problem this pattern was designed for]
Surface trigger:       [what about THIS problem triggered this pattern match]
Conscious or auto:     [did I deliberately choose this, or did it appear unbidden?]
────────────────────────────────────────
```

If you cannot name the source pattern, you are operating on **unconscious analogy** — the most dangerous mode, because the match was never evaluated.

**Artifact:** The pattern identification card. Phase 1, Step 2 uses this directly.

### Step 2 — CHECK STRUCTURAL PRECONDITIONS

Every solution pattern has preconditions — things that must be true for it to work. List the preconditions of the pattern you identified, then check each against THIS problem:

```
PRECONDITION CHECK
────────────────────────────────────────
P1: [pattern requires X]
    This problem: [X is true / false / uncertain]
    Match: [confirmed / broken / uncertain]

P2: [pattern requires Y]
    This problem: [Y is true / false / uncertain]
    Match: [confirmed / broken / uncertain]

P3: [pattern requires Z]
    This problem: [Z is true / false / uncertain]
    Match: [confirmed / broken / uncertain]
────────────────────────────────────────
```

**Minimum three preconditions checked.** If you can only find one, you don't understand the pattern well enough to use it.

If ANY precondition is **broken** → the pattern will fail at that point. Go to Phase 2.
If ANY precondition is **uncertain** → the pattern is a gamble. Flag it or go to Phase 2.

**Artifact:** The precondition table. This is the evidence for whether to use the pattern or descend.

### Step 3 — FIND THE BREAK POINT

Even with high structural match, write where this analogy eventually breaks:

```
BREAK POINT ANALYSIS
────────────────────────────────────────
Scale break:     [works at pattern's original scale but not at THIS scale — or vice versa]
Domain break:    [THIS domain has a constraint the pattern's source domain lacked]
Context break:   [THIS team/timeline/toolchain differs from the pattern's assumptions]
Temporal break:  [the technology landscape changed since this pattern was established]
────────────────────────────────────────
```

If no break point found → pattern is safe to apply. Use it.
If break point found → use the pattern everywhere EXCEPT the break point. At the break point, Phase 2 applies.

---

## Phase 2: First-Principles Derivation

Run when the pattern audit fails, when all templates feel forced, or when experts would disagree about the right approach.

### Step 4 — WRITE THE FUNDAMENTAL QUANTITIES

Every domain has irreducible truths — the physics of the problem, not the conventions.

Write the fundamentals relevant to THIS problem. Some catalysts:

- **Software:** Data has location, size, and consistency requirements. Computation costs time proportional to input. Networks have latency, bandwidth, and failure probability. Humans have attention limits and error rates. State can be mutable or immutable, local or distributed.
- **Product:** Users have a job to accomplish. Attention is finite and competitive. Trust is earned incrementally and lost instantly. Value is determined by the user, not the creator.
- **Business:** Revenue must exceed cost. Growth compounds but so does complexity. Incentives drive behavior more reliably than policies.

```
FUNDAMENTAL QUANTITIES FOR THIS PROBLEM:
1. [quantity and its constraint]
2. [quantity and its constraint]
3. [quantity and its constraint]
```

**Artifact:** The fundamentals list. Step 5 and 6 build on this directly.

### Step 5 — STRIP TO ESSENTIAL FORM

Write the problem with all these removed:
- Technology choices (implementation, not the problem)
- "We have to" statements (constraints that may be false assumptions)
- "Everyone does it this way" reasoning (convention, not necessity)
- Time pressure (urgency is a constraint, not a fundamental)

**Write the essential problem in one sentence:** "[The irreducible thing that would still need solving with unlimited time, any technology, and zero conventions]."

**Artifact:** The essential problem statement. This is what Step 6 solves.

### Step 6 — DERIVE UPWARD

Starting from the fundamental quantities (Step 4) + essential problem (Step 5), derive:

```
DERIVATION STACK
────────────────────────────────────────
Layer 1 — Fundamental truth:
  [from Step 4 — the irreducible requirement]

Layer 2 — Required structure:
  [architecture implied by Layer 1 — what MUST the solution look like?]
  Justified by: [which fundamental truth requires this?]

Layer 3 — Implementation path:
  [technology choice implied by Layer 2]
  Justified by: [which structural requirement leads here?]

Layer 4 — Concrete plan:
  [specific steps implied by Layer 3]
  Justified by: [which implementation decision leads here?]
────────────────────────────────────────
```

**Justification check:** Each layer must be justified by the layer below it. If you cannot write the "Justified by:" line — the layer is a pattern injection, not a derivation. Remove it and re-derive from the layer below.

### Step 7 — RECONCILE WITH ABANDONED PATTERNS

Write a comparison between your first-principles solution and the pattern(s) that failed:

```
RECONCILIATION
────────────────────────────────────────
Agrees with [pattern]:       [where — the pattern was correct here]
Disagrees with [pattern]:    [where — this is WHY the pattern didn't fit]
Resembles [other pattern]:   [unexpected pattern match — name it if found]
────────────────────────────────────────
```

This often reveals that the correct pattern was a different one entirely — one you didn't initially consider because the surface similarity pointed elsewhere.

---

## The Deeper Purpose

The model's output is built on pattern retrieval. This is efficient when patterns fit. When they don't, the model forces the closest match and hopes — producing answers that are correct for a different problem. This skill gives an alternative to force-fitting: verify the match explicitly; if it fails, derive from the domain's fundamental truths rather than from similar-looking solved problems. The most dangerous sentence in engineering is "this is just like the last one." This skill makes sure you know whether it is before you commit.


