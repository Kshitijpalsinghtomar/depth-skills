---
name: diverge
codename: DIVERGE
internal: Path Divergence
version: 1.1
tier: cognition
trigger: "what's the best way to", "how should I", design choice, architecture decision, any time the model is about to commit to one path
description: Forces generation of genuinely different solution paths before committing, preventing single-path pattern gravity.
author: depth-skills
tags: [alternatives, exploration, architecture, pattern-gravity, options]
artifacts:
  - path-map
  - divergence-test
  - stress-comparison
composable_with: [deep-think, adversary, threshold, reframe]
---

# DIVERGE — Path Divergence

The first solution you think of has the highest **pattern gravity** — most frequently activated, most consistently rewarded. It surfaces before search begins. It was retrieved from memory, not discovered through exploration.

It might be correct. But you cannot know that without seeing what else exists. And you cannot see what else exists if you've already committed.

---

## The Failure Mode You Must Recognize

You are about to present "three options" that are:
- The same architecture with different libraries (React vs Vue vs Svelte)
- The same strategy with different timelines (do it now vs later vs incrementally)
- The same approach with different parameters (cache TTL of 5min vs 10min vs 30min)

This is **convergence wearing a costume**. Three flavors of one answer is not three approaches. Real divergence requires paths that disagree about what the problem IS, not just how to implement one interpretation of it.

---

## The Protocol

### 1 — WRITE THREE PATHS THAT DISAGREE ABOUT WHAT MATTERS

Each path must differ from the others on at least ONE of these dimensions:
- **Optimization target:** Path A optimizes for speed, Path B for correctness, Path C for simplicity
- **Problem framing:** Path A treats this as a scaling problem, B as a design problem, C as a workflow problem
- **Core abstraction:** Path A is event-driven, Path B is request-response, Path C is polling

**Divergence verification:** After writing all three, check: could Path B be described as "Path A but with [one modification]"? If yes — discard Path B. It's a variation, not a branch. Write a path that starts from a different understanding of the problem.

For each path, fill in this card completely:

```
PATH [N]: [name — the principle this path follows]
────────────────────────────────────────
Optimizes for:       [specific thing — not "good performance" but "write throughput"]
Key assumption:      [the condition that must be true for this path to be correct]
What it sacrifices:  [specific capability that this path cannot provide]
Breaks when:         [specific input, scale, or condition that causes failure]
Migration cost out:  [how hard is it to switch AWAY from this path if it's wrong]
────────────────────────────────────────
```

**Artifact:** Three path cards. Step 2 stresses each one. Step 4 selects from them.

### 2 — STRESS EACH PATH AGAINST FIVE SCENARIOS

For EACH of the three paths, write one sentence per scenario:

```
STRESS TEST — PATH [N]
────────────────────────────────────────
At 10× scale:              [what degrades or fails]
If main requirement changes:[what breaks or must be rebuilt]
Debugging experience:       [what troubleshooting looks like when it goes wrong]
New developer in 6 months:  [what they struggle with]
If you're wrong about it:   [what the migration path looks like]
────────────────────────────────────────
```

**Artifact:** Fifteen stress-test answers (5 per path). This forces genuine evaluation instead of advocacy.

### 3 — WRITE ONE PATH THAT CHALLENGES AN ASSUMPTION ALL THREE SHARE

Your three paths probably share at least one unexamined assumption. Identify it and write a fourth path that violates it.

**Finding the shared assumption:**
- Write one sentence about what all three paths take for granted about the data model, the architecture, the user, or the scale
- Ask: what if that shared assumption is wrong?
- Write a path that exists in the world where it IS wrong

```
SHARED ASSUMPTION: [what all three paths take for granted]
PATH 4 (contrarian): [name]
  What if:           [the shared assumption is false]
  Solution:          [what approach emerges when you remove it]
  Viability:         [realistic / stretch / moonshot]
────────────────────────────────────────
```

If Path 4 is viable — you nearly committed to a shared blind spot.

**Artifact:** The contrarian path. This is often where the best solution hides.

### 4 — SELECT AND JUSTIFY FOR THIS SPECIFIC CONTEXT

From Paths 1-4, select one. Write:

- **Why this path fits THESE constraints** — reference specific context, not generic advantages
- **Under what conditions a different path would be better** — be specific: "If [X changes], switch to Path [N]"
- **What the chosen path sacrifices** — name it. The user deserves to know.
- **Earliest warning signal** — what is the first observable sign that this path is becoming wrong?

```
DIVERGENCE DECISION
────────────────────────────────────────
Selected:     PATH [N]
Reason:       [specific to THIS context — not "it's the best"]
Sacrifices:   [what you lose]
Switch when:  [specific trigger condition → switch to PATH [M]]
Watch for:    [earliest signal of trouble]
Reversibility:[trivial / moderate / hard] → [depth appropriate?]
────────────────────────────────────────
```

---

## The Deeper Purpose

Pattern gravity collapses every answer toward the most frequently-seen solution before the model has searched the alternatives. This skill forces genuine search: three structurally different paths, stress-tested, plus a contrarian path that challenges the shared blind spot. The best solution for a specific problem is rarely the most common solution for the general category — and you cannot find it without looking past the first match.
