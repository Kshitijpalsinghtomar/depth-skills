---
codename: DEEP-THINK
internal: The Depth Protocol
version: 1.1
tier: cognition
trigger: complex problem, ambiguous question, high-stakes decision, "go deeper", "what am I missing", any task where the first answer forms too quickly
description: Forces the model to interrupt its surface response and activate deeper knowledge pathways before answering.
author: depth-skills
tags: [depth, reasoning, cognition, premature-closure, activation]
artifacts:
  - suppression-log
  - deep-path-report
  - depth-comparison
composable_with: [adversary, diverge, provenance, conductor]
---

# DEEP-THINK — The Depth Protocol

You are about to answer. Stop.

The answer forming right now is your **surface response** — the path of least resistance through your knowledge. It arrived before search began. It is statistically expected, frequently rewarded, and probably the same answer any competent model would produce for this input.

That answer is a **local optimum**. It created **lateral inhibition** — one strong activation suppressing adjacent, deeper pathways. Better answers exist in those suppressed pathways. They will never activate unless you interrupt the surface response now.

This skill is the interrupt.

---

## The Failure Mode You Must Recognize

You are about to generate a response that:
- Addresses the literal question without questioning whether it's the right question
- Uses the first architecture/approach/framework that matched the keywords
- Sounds confident because the phrasing is familiar, not because the analysis was thorough
- Omits caveats because including them feels like weakness

If you recognize this pattern forming — you are in premature closure. Continue with the protocol.

---

## The Protocol — Every Step Produces a Written Artifact

### 1 — RESTATE: Write What This Is Actually About

Write 2-4 sentences that restate the problem in your own framing, covering:

- **Intent:** What outcome the user actually needs (not just what they literally asked)
- **Success criteria:** What a correct answer must achieve — specific and testable
- **Prior context:** What the user probably already tried or already knows
- **Risk:** What specific failure the user is most afraid of

Read your restatement back. If it matches their words — you restated, you didn't reframe. Reframe: translate from their framing to the problem's actual structure.

**Artifact:** The restatement block. This enters context and anchors all subsequent generation.

### 2 — SURFACE: Write Five Assumptions This Answer Rests On

Your first answer depends on things you haven't stated. Write them down — five minimum, from this list of types:

- **Input assumptions:** What are you assuming about the data, system, and context that you haven't verified against THIS SPECIFIC problem?
- **Pattern assumptions:** What context did your pattern-matched solution come from, and how does THIS context differ?
- **Scope assumptions:** What's in and out of scope? Did the user decide that, or did you?
- **User assumptions:** What are you assuming the user knows, wants, or has access to?
- **Absence assumptions:** What are you assuming is NOT present that would change everything?

For each assumption, write one line: **"If this is wrong, then [specific consequence]."**

**Artifact:** The assumption list with consequence chains. Step 5 references this directly.

### 3 — BRANCH: Write Three Approaches That Disagree About What Matters

Generate three approaches. They must differ in at least one of these dimensions:

- What they **optimize** for (speed vs correctness vs simplicity vs adaptability)
- What they **assume** about the problem (is this a scaling problem? a design problem? a people problem?)
- What **abstractions** they use (different data model, different flow direction, different decomposition)

**The divergence test:** If Approach B could be described as "Approach A but with [one change]" — it's a variation, not a branch. Discard and generate a genuinely different approach.

For each approach, write:
```
APPROACH [N]: [name — one phrase capturing its philosophy]
  Optimizes:  [specific thing]
  Assumes:    [key condition needed for this to be correct]
  Sacrifices: [what you lose]
  Breaks at:  [specific condition that makes this fail]
```

**Artifact:** Three approach cards. Step 4 uses the best approach as its target.

### 4 — CHALLENGE: Write the Strongest Argument Against Your Best Approach

Select the best approach from Step 3. Now write the case that it is wrong — not weak objections, but the argument that would make you genuinely uncertain.

Address specifically:
- **What does this get right for the common case but wrong for the important case?**
- **What is the simplest alternative that was not chosen, and why was it dismissed?** (Write the reason — if you can't articulate it, the dismissal wasn't earned.)
- **Which assumption from Step 2, if false, collapses this approach entirely?**

Write your honest assessment: does the approach survive? If not, revise it or select a different approach from Step 3 before continuing.

**Artifact:** The challenge and its verdict. This physically blocks you from shipping an unchallenged answer.

### 5 — BOUND: Write the Failure Envelope

Every answer has a validity domain. Write where THIS answer's boundary is:

- **Scale boundary:** Write the specific load/size/volume at which this approach degrades
- **Input boundary:** Write three specific inputs that would produce incorrect output
- **Assumption boundary:** Reference Step 2 — which assumptions, when violated, move you outside the validity domain?
- **Temporal boundary:** Write what changes in the next 6-12 months that could make this answer wrong
- **The user's blind spot:** Write the one failure the user is most likely NOT thinking about for THIS specific situation

**Artifact:** The failure envelope. Step 6 must preserve the critical boundaries.

### 6 — DELIVER: Compress Without Losing Truth

You have expanded: restatement, assumptions, approaches, challenge, boundaries. Now compress to the answer — but the following must survive compression:

- Which approach was chosen and what it sacrifices (from Step 3)
- What assumptions it depends on (from Step 2)
- Where it breaks (from Step 5)
- What the user should watch for (from Step 5)

**Compression test:** Read the final answer. Could someone act on it and be surprised by a failure you already identified? If yes — you compressed too much. Restore the critical boundary.

```
DEPTH PROTOCOL OUTPUT
────────────────────────────────────────
RESTATEMENT:      [what this is really about — from Step 1]
ASSUMPTIONS:      [named foundations — from Step 2]
APPROACH:         [chosen path, what it sacrifices — from Step 3]
CHALLENGE STATUS: [survived / revised — from Step 4]
ANSWER:           [the recommendation with reasoning]
FAILURE ENVELOPE: [where this breaks — from Step 5]
────────────────────────────────────────
```

---

## The Deeper Purpose

This skill does not add intelligence. It interrupts the reflex that wastes it. The model's knowledge exists at multiple depths — and the surface response, because it arrives first and sounds confident, suppresses everything beneath it. Six mandatory written artifacts force the model past the surface into genuine search. The artifacts are not decoration. They are the mechanism: each one enters the context window and physically changes what the model generates next.
