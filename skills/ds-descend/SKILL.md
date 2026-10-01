---
name: descend
codename: DESCEND
internal: Pattern Audit & First-Principles Derivation v2.0
version: 2.0
tier: cognition
trigger:
  - "nothing works"
  - "tried everything"
  - "familiar solution feels wrong"
  - "experts would disagree"
  - "best practices conflict"
  - "novel problem with no template"
description: Verifies whether the problem was correctly identified before solving, auditing pattern matches against first principles. Now with mathematical depth metrics, recursive audit, cognitive traces, and verification gates.
author: Kshitijpalsinghtomar
tags: [first-principles, pattern-audit, root-cause, derivation, novel-problems, metrics, recursion, verification]
artifacts:
  - pattern-identification-card
  - precondition-table
  - derivation-layers
  - break-point-analysis
  - reconciliation
  - activation-heatmap
  - assumption-dependency-graph
    - phase-activation
composable_with:
  - excavate
  - reframe
  - invert
  - deep-think
  - conductor
  - boundary-detector
thinking_parameters:
  min_preconditions: 3
  min_break_points: 1
  recursion_depth: 1
  require_derivation: true
  require_reconciliation: true
---

# DESCEND v2.0 — Pattern Audit & First-Principles Derivation (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (activation heatmap, assumption dependency graph), and verifies Gates V1, V2, V3. It integrates with BOUNDARY-DETECTOR for knowledge boundary probes.

Every answer you generate is built from patterns — compressed experience retrieved from training: "In situations like X, do Y." This is efficient when the match is real.

It is catastrophic when it isn't. And you do not check.

**Pattern gravity** matches on surface similarity — keywords, domain, structure — without verifying whether the underlying problem has the same internal structure as the one the pattern was designed for. Problems that look alike on the surface can have completely different mechanics underneath. The pattern that solved one will silently damage the other.

This skill has two phases:
- **Phase 1: AUDIT** — is the pattern match real, or is it a surface-level false analogy?
- **Phase 2: DERIVE** — if the match is false, reason from fundamental truths upward.

**New in v2.0:** Mathematical depth metrics, recursive self-audit, cognitive trace artifacts, verification gates, boundary detection integration.

---

## The Failure Mode You Must Recognize

You are about to generate a response that:
- Applies a pattern unconsciously without verifying its preconditions
- Forces a familiar template onto a problem with different internal structure
- Claims "this is just like [previous problem]" without checking structural preconditions
- **Produces derivation artifacts without genuine first-principles reasoning (cargo cult derivation)**

If you recognize this pattern forming — you are in unconscious analogy. Continue with the protocol.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `min_preconditions` (default 3) — minimum preconditions to check
- `min_break_points` (default 1) — minimum break points to identify
- `recursion_depth` (default 1) — recursive self-audit rounds
- `require_derivation` (default true) — must produce derivation stack
- `require_reconciliation` (default true) — must reconcile with abandoned patterns

---

### Phase 1: Pattern Audit

#### 1 — MAKE THE PATTERN VISIBLE

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

**CEI Component:** Pattern Identification (weight 2.0)

---

#### 2 — CHECK STRUCTURAL PRECONDITIONS (Minimum = `min_preconditions`)

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

[Additional preconditions up to min_preconditions...]
────────────────────────────────────────
```

**Minimum `min_preconditions` checked.** If you can only find one, you don't understand the pattern well enough to use it.

If ANY precondition is **broken** → the pattern will fail at that point. Go to Phase 2.
If ANY precondition is **uncertain** → the pattern is a gamble. Flag it or go to Phase 2.

**Artifact:** The precondition table. This is the evidence for whether to use the pattern or descend.

**CEI Component:** Precondition Check (weight 3.0)

**SI Component:** Broken/uncertain preconditions (count)

---

#### 3 — FIND THE BREAK POINT (Minimum = `min_break_points`)

Even with high structural match, write where this analogy eventually breaks:

```
BREAK POINT ANALYSIS
────────────────────────────────────────
Scale break:     [works at pattern's original scale but not at THIS scale — or vice versa]
Domain break:    [THIS domain has a constraint the pattern's source domain lacked]
Context break:   [THIS team/timeline/toolchain differs from the pattern's assumptions]
Temporal break:  [the technology landscape changed since this pattern was established]
[Additional break points up to min_break_points...]
────────────────────────────────────────
```

If no break point found → pattern is safe to apply. Use it.
If break point found → use the pattern everywhere EXCEPT the break point. At the break point, Phase 2 applies.

**Artifact:** Break point analysis.

**CEI Component:** Break Point Analysis (weight 2.0)

**SI Component:** Boundary violations (break points found)

---

### Phase 2: First-Principles Derivation

Run when the pattern audit fails, when all templates feel forced, or when experts would disagree about the right approach.

#### 4 — WRITE THE FUNDAMENTAL QUANTITIES

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

**CEI Component:** Fundamental Quantities (weight 3.0)

---

#### 5 — STRIP TO ESSENTIAL FORM

Write the problem with all these removed:
- Technology choices (implementation, not the problem)
- "We have to" statements (constraints that may be false assumptions)
- "Everyone does it this way" reasoning (convention, not necessity)
- Time pressure (urgency is a constraint, not a fundamental)

**Write the essential problem in one sentence:** "[The irreducible thing that would still need solving with unlimited time, any technology, and zero conventions]."

**Artifact:** The essential problem statement. This is what Step 6 solves.

**CEI Component:** Essential Form (weight 2.0)

---

#### 6 — DERIVE UPWARD

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

**Artifact:** The derivation stack.

**CEI Component:** Derivation Stack (weight 5.0)

---

#### 7 — RECONCILE WITH ABANDONED PATTERNS

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

**Artifact:** The reconciliation.

**CEI Component:** Reconciliation (weight 3.0)

---

### 8 — METRICS: Compute and Output Depth Metrics

#### 8.1 Phase Activation (for ADS)

```json
{
  "phase": 1,
  "skill": "descend",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

#### 8.2 CEI Components

```json
{
  "cei_components": {
    "pattern_identification": 2.0,
    "precondition_check": 3.0,
    "break_point_analysis": 2.0,
    "fundamental_quantities": 3.0,
    "essential_form": 2.0,
    "derivation_stack": 5.0,
    "reconciliation": 3.0,
    "total_complexity_weight": 20.0,
    "output_tokens": N,
    "wall_time_seconds": T,
    "cei": 0.XX
  }
}
```

#### 8.3 SI Components

```json
{
  "si_components": {
    "c2_c3_count": 0,
    "contrarian_viable": false,
    "fatal_attacks": 0,
    "boundary_violations": N,
    "assumption_reversals": 0,
    "si_total": N
  }
}
```

#### 8.4 Cognitive Traces

**Activation Heatmap:**
```json
{
  "type": "activation_heatmap",
  "layers": [
    {"name": "Surface Patterns (0-20%)", "activation": 0.XX, "zone": "pattern_gravity"},
    {"name": "Assumption Layer (20-40%)", "activation": 0.XX, "zone": "excavation"},
    {"name": "Alternative Space (40-60%)", "activation": 0.XX, "zone": "divergence"},
    {"name": "Stress-Test Zone (60-80%)", "activation": 0.XX, "zone": "adversarial"},
    {"name": "Integrity Layer (80-100%)", "activation": 0.XX, "zone": "verification"}
  ],
  "overall_activation_depth": 0.XX,
  "target_for_task": 0.XX
}
```

**Assumption Dependency Graph:**
```json
{
  "type": "assumption_dependency_graph",
  "nodes": [
    {"id": "P1", "rating": "C2", "statement": "...", "match": "broken"},
    {"id": "P2", "rating": "C1", "statement": "...", "match": "confirmed"}
  ],
  "edges": [
    {"from": "P1", "to": "Pattern_Validity", "type": "foundational"}
  ],
  "critical_path": ["P1", "Pattern_Validity"],
  "ontological_risk": true
}
```

#### 8.5 Depth  Contribution

```json
{
  "skill": "descend",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": N, "ec": 0.XX},
  "gates_verified": {"V1": true, "V2": true, "V3": true},
  "limitations": ["..."]
}
```

---

### 9 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V1** | Assumption Coverage | Every claim in answer traces to a precondition or fundamental quantity (≥90%) |
| **V2** | Alternative Independence | If REFRAME/DIVERGE ran: CIM ≥ 0.5 (from interference) |
| **V3** | Opposition Authenticity | Break points reference specific pattern preconditions + external evidence |

**If any gate FAILS:** Return to relevant step and fix. Do not deliver.

---

### 10 — RECURSIVE SELF-AUDIT (if `recursion_depth` > 1)

If `recursion_depth` > 1, apply **this entire protocol** to your own output from Phases 1-2.

For each recursion level d = 2 to `recursion_depth`:
1. Treat your previous output as the "answer under review"
2. Run Phases 1-2 on it
3. Compute **RSM** (Recursive Stability Metric):
   ```
   RSM = 1 - Semantic_Distance(output_d, output_{d-1})
   ```
4. **Convergence Check:**
   - If RSM > 0.95 AND SI_d ≥ SI_{d-1} for 2 consecutive depths → **CONVERGED**, stop
   - If RSM < 0.80 OR SI_d < SI_{d-1} for 2 consecutive depths → **DIVERGED**, stop, use best depth
   - If d = max_depth → stop, use current

**Artifact:** `recursion_log` with RSM and SI at each depth.

**CEI Component:** Recursive Audit (weight 5.0 per level)

---

### 11 — INTERFERENCE: Receive and Provide

**Receive from prior skills:**

| From Skill | Interference | Use |
|------------|--------------|-----|
| BOUNDARY-DETECTOR | Knowledge gaps | Flag uncertain preconditions as "knowledge boundary" |
| DEEP-THINK | Assumptions from restatement | Seed pattern identification |

**Provide to later skills:**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| EXCAVATE | Broken preconditions → C2/C3 assumptions | +0.20 |
| REFRAME | Break points → lens selection | +0.15 |
| INVERT | Broken preconditions → inversion targets | +0.20 |
| ADVERSARY | Pattern audit failures → fatal attack targets | +0.20 |

**Artifact:** `interference_log` (received and provided).

---

## The Deeper Purpose

The model's output is built on pattern retrieval. This is efficient when patterns fit. When they don't, the model forces the closest match and hopes — producing answers that are correct for a different problem. This skill gives an alternative to force-fitting: verify the match explicitly; if it fails, derive from the domain's fundamental truths rather than from similar-looking solved problems. **Now it's quantified, verified, and traceable.** The most dangerous sentence in engineering is "this is just like the last one." This skill makes sure you know whether it is before you commit — and proves it.

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 1. It outputs:
```json
{
  "phase": 1,
  "skill": "descend",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: pattern_identification (2.0), precondition_check (3.0), break_point_analysis (2.0), fundamental_quantities (3.0), essential_form (2.0), derivation_stack (5.0), reconciliation (3.0)
- Total complexity weight: 20.0

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: [break points + broken preconditions count]
- Assumption reversals: 0

### Cognitive Traces Produced
- [x] Activation Heatmap
- [x] Assumption Dependency Graph
- [ ] Decision Landscape

### Gates Verified
- [x] V1  [x] V2  [x] V3  [ ] V4  [ ] V5  [ ] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From BOUNDARY-DETECTOR: Knowledge gaps → uncertain preconditions
- From DEEP-THINK: Assumptions → pattern identification seed