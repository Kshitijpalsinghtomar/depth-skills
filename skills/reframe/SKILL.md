---
name: reframe
codename: REFRAME
internal: Representation Multiplier
version: 1.1
tier: excavation
trigger: stuck, "another way to think about this", "reframe", same-looking solutions, muddy tradeoffs, "I can't see a way forward"
description: Solves the same problem through multiple independent representations, then triangulates structural truth.
author: depth-skills
tags: [framing, representation, lenses, stuck, breakthrough]
artifacts:
  - current-frame-analysis
  - independent-lens-solutions
  - cross-frame-analysis
  - hybrid-recommendation
composable_with: [invert, diverge, descend, negative-space]
---

# REFRAME — Representation Multiplier

You are solving this problem in one representation — one mental model, one framing. That frame feels natural. It is also a **cognitive prison**: the search dynamics change with representation. A dead end in one frame is often trivially solvable in another.

Hard problems stay hard because the solver never changes the lens.

---

## The Failure Mode You Must Recognize

You are about to solve the problem the same way for the third time — using the same abstractions, the same vocabulary, the same decomposition. Each attempt produces slightly different results but no breakthrough. This is **single-frame reasoning**: the model is optimizing harder within one representation instead of switching to a representation where the answer is easier to find.

---

## The Protocol

### Step 1 — NAME THE CURRENT FRAME

Write down how you are currently framing this problem:

```
CURRENT FRAME
────────────────────────────────────────
Problem:                [one sentence]
Current representation: [how you're modeling it — e.g., as a data flow,
                         as a user story, as a code structure]
What this frame reveals:[what's easy to see in this frame]
What this frame hides:  [what's hard to see — be specific, not "some things"]
────────────────────────────────────────
```

**Artifact:** The current frame analysis. You cannot escape a frame you haven't named.

### Step 2 — CHOOSE THREE DIFFERENT LENSES

Select three from this set that are DIFFERENT from your current frame. No near-duplicates:

| Lens | What It Shows | Use When |
|---|---|---|
| **Constraint graph** | Nodes = decisions, edges = constraints. Reveals bottlenecks and dependencies. | You can't figure out what's blocking the solution |
| **State machine** | States the system can be in, valid transitions. Reveals illegal states and missing transitions. | The problem involves stateful behavior or workflows |
| **Cost function** | What you're minimizing/maximizing. Penalty surface shape. | You need to make an optimization tradeoff |
| **Queue & flow** | What enters, what exits, where things back up. | Performance, throughput, or capacity problems |
| **Risk matrix** | What can go wrong × how bad × how likely. | You need to prioritize what to worry about |
| **User journey** | The experience as a story: trigger → action → outcome → feeling. | The problem is about UX or human behavior |
| **Data model** | Entities, relationships, invariants (what must ALWAYS be true). | The problem is about correctness or consistency |
| **Decision tree** | Branching choices with outcomes at leaf nodes. | The problem involves sequential decisions |

### Step 3 — SOLVE INDEPENDENTLY IN EACH LENS

For EACH of the three chosen lenses, solve the problem from scratch within that lens. Do not translate your existing solution — generate a new one native to the lens.

For each lens, write:

```
LENS [N]: [name]
────────────────────────────────────────
Objective (in this lens's language):
  [what success looks like in this representation]

Key variables:
  [the important quantities in this frame — list 3-5]

Invariants:
  [what must stay true regardless of solution — list 2-3]

Solution candidate:
  [what the solution looks like from this angle]

Failure signature:
  [what failure looks like in this frame — how do you know it's broken?]
────────────────────────────────────────
```

**Anti-contamination rule:** Do not solve in Lens B by translating your Lens A solution. Start fresh. The value is in what each lens reveals independently. Contamination defeats the purpose.

**Artifact:** Three independent solutions. Step 4 compares them.

### Step 4 — EXTRACT CROSS-FRAME STRUCTURE

Compare the three solutions. Write:

```
CROSS-FRAME ANALYSIS
────────────────────────────────────────
INVARIANTS (true in all three lenses):
  I1: [statement] — this is a STRONG structural truth
  I2: [statement]

CONTRADICTIONS (Lens A says X, Lens B says opposite):
  T1: [Lens [A] recommends X] vs [Lens [B] recommends NOT X]
      This tension reveals: [what tradeoff this actually is]

UNIQUE INSIGHTS (visible in only one lens):
  Lens [N]: [insight not visible from other angles]
────────────────────────────────────────
```

**Invariants** survive reframing — they are the problem's real structure, not artifacts of your framing.

**Contradictions** are not bugs — they reveal the most important tradeoff in the problem. The contradiction IS the design decision.

**Unique insights** are the payoff. These are things invisible from your original frame.

**Artifact:** The cross-frame analysis. Step 5 builds the final recommendation from this.

### Step 5 — BUILD HYBRID RECOMMENDATION

Construct the final answer using:
- Invariants as the foundation (proven structural truths)
- One explicit tradeoff resolution for each contradiction (with reasoning)
- Unique insights incorporated where they improve the answer
- A fallback path if the primary invariant fails in practice

```
REFRAME OUTPUT
────────────────────────────────────────
Foundation (from invariants): [the core recommendation]
Tradeoff handled:             [which contradiction, which direction, why]
Insight incorporated:         [from which lens, what it added]
Fallback:                     [what to do if the foundation doesn't hold]
────────────────────────────────────────
```

---

## The Deeper Purpose

A problem is mathematically equivalent across representations, but search is not. The path to a solution that is invisible in one frame may be the obvious path in another. Three independent solutions from three different lenses reveal overlapping structural truths (invariants), hidden tradeoffs (contradictions), and invisible insights (unique findings). The hybrid exceeds what any single frame could produce — not by adding quantity, but by triangulating the problem's actual structure from multiple angles.
