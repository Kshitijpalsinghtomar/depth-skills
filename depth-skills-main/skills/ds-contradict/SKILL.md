---
name: contradict
codename: CONTRADICT
internal: Coherence Auditor
version: 1.1
tier: integrity
trigger: any multi-part answer, any design document, any plan with more than 5 steps, "does this make sense", "is this consistent"
description: Cross-compares every claim in an output to detect internal contradictions that sequential generation hides.
author: Kshitijpalsinghtomar
tags: [coherence, consistency, contradiction, audit, claims]
artifacts:
  - claim-extraction
  - conflict-list
  - severity-classification
  - resolution-log
  - coherence-verdict
composable_with: [provenance, fidelity, adversary, negative-space]
---

# CONTRADICT — Coherence Auditor

You generate sequentially — one section, then the next. Each section is optimized for local coherence. Section A reads well. Section C reads well.

But locally coherent sections can be **globally contradictory**. Section A promises simplicity. Section C introduces complexity that destroys the simplicity. Both sound right alone. Together, they are a lie.

You have no built-in global consistency checker. This skill is that checker.

---

## The Failure Mode You Must Recognize

You are about to deliver an answer where:
- The introduction says "simple and straightforward"
- Step 7 requires complex configuration across three services
- The summary says "no external dependencies"
- Step 4 uses two external libraries

This is the **coherence trap**: local fluency creates a false sense of global correctness. Each part is individually convincing, but the parts cannot coexist. You don't notice because you generate forward, not cross-sectionally.

---

## The Protocol

### Step 1 — EXTRACT: Write Every Claim as a Standalone Statement

Read the entire output. Extract every claim, promise, estimate, and assertion. Write each as a standalone sentence that could be true or false:

```
CLAIM EXTRACTION
────────────────────────────────────────
C1: [section/paragraph ref] — "[exact claim]"
C2: [section/paragraph ref] — "[exact claim]"
C3: [section/paragraph ref] — "[exact claim]"
...
────────────────────────────────────────
```

Types to catch:
- **Promises:** "This approach is simple," "No configuration needed," "Handles all cases"
- **Estimates:** "Takes about a week," "Under 100ms latency," "Minimal effort"
- **Scope claims:** "No external dependencies," "Works offline," "Supports all browsers"
- **Characteristic claims:** "Highly scalable," "Easy to maintain," "Secure by default"

**Minimum count:** Extract at least 10 claims for a substantive answer. If you found fewer, you're extracting too loosely — tighten your filter.

**Artifact:** Numbered claim list with section references. Step 2 cross-compares these.

### Step 2 — CROSS-COMPARE: Test Each Claim Pair for Mutual Compatibility

For each pair of claims that could potentially conflict, write the comparison:

**Common contradiction patterns to actively scan for:**

| Pattern | Claim Type A | Claim Type B | The Lie |
|---|---|---|---|
| Scope-timeline | "Built in X time" | Feature list A, B, C, D, E | Sum of features doesn't fit in X |
| Simplicity-completeness | "Simple and easy" | "Handles all edge cases" | Comprehensive handling IS complexity |
| Independence-integration | "No dependencies" | "Uses service X, Y" | Those ARE dependencies |
| Performance-richness | "Fast and lightweight" | "Rich animations, real-time" | Each feature costs performance |
| Confidence-uncertainty | "High confidence" | "Several unknowns" | High confidence requires low unknowns |
| Generality-specificity | "Works for any case" | "Optimized for [specific case]" | Optimization is specialization |
| Cost-quality | "Minimal effort" | "Production-quality" | Production quality is not minimal effort |

For each potential conflict found:

```
CONFLICT [N]:
  Claim A: C[x] — "[claim]"
  Claim B: C[y] — "[claim]"
  Can both be true simultaneously?: [yes — how / no — why]
────────────────────────────────────────
```

**Artifact:** The conflict list. Step 3 classifies each one.

### Step 3 — CLASSIFY: Rate Severity of Each Conflict

```
CONFLICT [N]: [COSMETIC / STRUCTURAL / FATAL]

  COSMETIC:    Same meaning, different wording. Fix the wording.
               Both claims can coexist with a minor edit.

  STRUCTURAL:  Real tension. Both cannot be fully true.
               Must decide which takes priority.

  FATAL:       Mutually exclusive. The answer promises something
               logically impossible. Must rebuild.
────────────────────────────────────────
```

**Artifact:** Classified conflict list. Step 4 resolves each non-cosmetic conflict.

### Step 4 — RESOLVE: Address Each Structural and Fatal Conflict

For each STRUCTURAL conflict, choose ONE resolution:

**Priority:** One claim wins. The other is revised. Write which and why.
**Scope:** Both are true in different contexts. Make the scope explicit: "Simple interface, complex internals." Write the scoping language.
**Tradeoff declaration:** The tension IS the point. Write: "We want both [speed] and [thoroughness]. Here is where the dial is set: [specific tradeoff point]."

For each FATAL conflict:

**Rebuild.** The answer needs restructuring. Identify which claim is true and revise everything that contradicts it.

```
RESOLUTION LOG
────────────────────────────────────────
Conflict [N]: [resolution type — priority / scope / tradeoff / rebuild]
  Result:     [what changed in the answer]

Conflict [N]: [resolution type]
  Result:     [what changed]
────────────────────────────────────────
```

### Step 5 — WRITE THE COHERENCE VERDICT

```
COHERENCE VERDICT
────────────────────────────────────────
Claims extracted:   [count]
Conflicts found:    [count]
  Cosmetic:         [count] — fixed
  Structural:       [count] — resolved
  Fatal:            [count] — rebuilt

Overall coherence:  [consistent / mostly consistent / inconsistent]
Remaining tensions: [any unresolved tradeoffs the user should know about]
────────────────────────────────────────
```

---

## The Deeper Purpose

The longer an output, the higher the probability of internal contradiction. Sequential generation optimizes locally, not globally. Words like "simple," "comprehensive," and "handles all cases" are **contradiction magnets** — they make promises the rest of the answer often cannot keep. This skill reads the output not section by section, but claim against claim, surfacing the conflicts that sequential generation cannot see.
