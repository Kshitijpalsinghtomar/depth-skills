---
name: deep-think
codename: DEEP-THINK
internal: The Depth Protocol v2.0
version: 2.0
tier: cognition
trigger: complex problem, ambiguous question, high-stakes decision, "go deeper", "what am I missing", any task where the first answer forms too quickly
description: Forces the model to interrupt its surface response and activate deeper knowledge pathways before answering. Now with mathematical depth metrics (ADS, CEI, SI), recursive self-audit, cognitive trace artifacts, and verification gates.
author: Kshitijpalsinghtomar
tags: [depth, reasoning, cognition, premature-closure, activation, metrics, recursion, verification]
artifacts:
  - suppression-log
  - deep-path-report
  - depth-comparison
  - activation-heatmap
  - assumption-dependency-graph
    - phase-activation
composable_with: [adversary, diverge, provenance, conductor, excavate, invert, reframe]
thinking_parameters:
  min_assumptions: 10
  min_branches: 3
  recursion_depth: 1
  collapse_threshold: "C2"
  require_interference: true
---

# DEEP-THINK v2.0 — The Depth Protocol (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (activation heatmap, assumption dependency graph), and verifies Gates V1, V2, V3.

You are about to answer. Stop.

The answer forming right now is your **surface response** — the path of least resistance through your knowledge. It arrived before search began. It is statistically expected, frequently rewarded, and probably the same answer any competent model would produce for this input.

That answer is a **local optimum**. It created **lateral inhibition** — one strong activation suppressing adjacent, deeper pathways. Better answers exist in those suppressed pathways. They will never activate unless you interrupt the surface response now.

This skill is the interrupt. **It now measures the interrupt.**

---

## The Failure Mode You Must Recognize

You are about to generate a response that:
- Addresses the literal question without questioning whether it's the right question
- Uses the first architecture/approach/framework that matched the keywords
- Sounds confident because the phrasing is familiar, not because the analysis was thorough
- Omits caveats because including them feels like weakness
- **Produces artifacts without genuine cognitive work (cargo cult depth)**

If you recognize this pattern forming — you are in premature closure. Continue with the protocol.

---

## The Protocol — Every Step Produces a Measured Artifact

### 0 — PARAMETERIZE: Read Thinking Parameters

Before starting, read the `thinking_parameters` from context (or use preset). These control:
- `min_assumptions` (default 10) — minimum assumptions in Step 2
- `min_branches` (default 3) — minimum approaches in Step 3
- `recursion_depth` (default 1) — recursive self-audit rounds
- `collapse_threshold` (default "C2") — minimum collapse rating requiring resolution
- `require_interference` (default true) — must receive interference from prior skills

**Artifact:** `parameter_acknowledgment` — confirm parameters read and will be enforced.

---

### 1 — RESTATE: Write What This Is Actually About

Write 2-4 sentences that restate the problem in your own framing, covering:

- **Intent:** What outcome the user actually needs (not just what they literally asked)
- **Success criteria:** What a correct answer must achieve — specific and testable
- **Prior context:** What the user probably already tried or already knows
- **Risk:** What specific failure the user is most afraid of

Read your restatement back. If it matches their words — you restated, you didn't reframe. Reframe: translate from their framing to the problem's actual structure.

**Artifact:** The restatement block. This enters context and anchors all subsequent generation.

**CEI Component:** Restatement (weight 1.0)

---

### 2 — SURFACE: Write Assumptions (Minimum = `min_assumptions`)

Your first answer depends on things you haven't stated. Write them down — **at least `min_assumptions`**, from these types:

- **Input assumptions:** What are you assuming about the data, system, and context that you haven't verified against THIS SPECIFIC problem?
- **Pattern assumptions:** What context did your pattern-matched solution come from, and how does THIS context differ?
- **Scope assumptions:** What's in and out of scope? Did the user decide that, or did you?
- **User assumptions:** What are you assuming the user knows, wants, or has access to?
- **Absence assumptions:** What are you assuming is NOT present that would change everything?

For each assumption, write one line: **"If this is wrong, then [specific consequence]."**

**Artifact:** Numbered assumption list with consequence chains. Step 5 references this directly.

**CEI Component:** Assumption List (weight 2.0)

**SI Component:** Count of C2/C3 assumptions (after Step 3 rating)

---

### 3 — BRANCH: Write Approaches That Disagree (Minimum = `min_branches`)

Generate **at least `min_branches`** approaches. They must differ in at least one of these dimensions:

- What they **optimize** for (speed vs correctness vs simplicity vs adaptability)
- What they **assume** about the problem (is this a scaling problem? a design problem? a people problem?)
- What **abstractions** they use (different data model, different flow direction, different decomposition)

**The divergence test:** If Approach B could be described as "Approach A but with [one change]" — it's a variation, not a branch. Discard and generate a genuinely different approach.

**Note:** This BRANCH step is for problem exploration. For deeper solution comparison with stress-testing, use DIVERGE as a follow-up skill.

For each approach, write:

```
APPROACH [N]: [name — one phrase capturing its philosophy]
  Optimizes:  [specific thing]
  Assumes:    [key condition needed for this to be correct]
  Sacrifices: [what you lose]
  Breaks at:  [specific condition that makes this fail]
```

**Artifact:** Approach cards (minimum `min_branches`).

**CEI Component:** Branch Cards (weight 3.0 each)

**CIM Requirement:** Cosine similarity between approach embeddings < 0.5 (verified by CONDUCTOR)

---

### 4 — CHALLENGE: Write the Strongest Argument Against Your Best Approach

Select the best approach from Step 3. Now write the case that it is wrong — not weak objections, but the argument that would make you genuinely uncertain.

Address specifically:
- **What does this get right for the common case but wrong for the important case?**
- **What is the simplest alternative that was not chosen, and why was it dismissed?** (Write the reason — if you can't articulate it, the dismissal wasn't earned.)
- **Which assumption from Step 2, if false, collapses this approach entirely?**

Write your honest assessment: does the approach survive? If not, revise it or select a different approach from Step 3 before continuing.

**Artifact:** The challenge and its verdict. This physically blocks you from shipping an unchallenged answer.

**CEI Component:** Challenge (weight 4.0)

**SI Component:** Fatal attacks that required rebuild (count)

---

### 5 — BOUND: Write the Failure Envelope

Every answer has a validity domain. Write where THIS answer's boundary is:

- **Scale boundary:** Write the specific load/size/volume at which this approach degrades
- **Input boundary:** Write three specific inputs that would produce incorrect output
- **Assumption boundary:** Reference Step 2 — which assumptions, when violated, move you outside the validity domain?
- **Temporal boundary:** Write what changes in the next 6-12 months that could make this answer wrong
- **The user's blind spot:** Write the one failure the user is most likely NOT thinking about for THIS specific situation

**Artifact:** The failure envelope. Step 6 must preserve the critical boundaries.

**CEI Component:** Failure Envelope (weight 3.0)

**SI Component:** Boundary violations that changed the answer (count)

---

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

**CEI Component:** Final Answer (weight 1.0)

---

### 7 — METRICS: Compute and Output Depth Metrics

**MANDATORY** — Compute and output:

#### 7.1 Phase Activation (for ADS)

```json
{
  "phase": 1,
  "skill": "deep-think",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

#### 7.2 CEI Components

```json
{
  "cei_components": {
    "restatement": 1.0,
    "assumption_list": 2.0,
    "branch_cards": 3.0,
    "challenge": 4.0,
    "failure_envelope": 3.0,
    "final_answer": 1.0,
    "total_complexity_weight": 14.0,
    "output_tokens": N,
    "wall_time_seconds": T,
    "cei": 0.XX
  }
}
```

#### 7.3 SI Components

```json
{
  "si_components": {
    "c2_c3_count": N,
    "contrarian_viable": false,
    "fatal_attacks": N,
    "boundary_violations": N,
    "assumption_reversals": N,
    "si_total": N
  }
}
```

#### 7.4 Cognitive Traces

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
    {"id": "A1", "rating": "C3", "statement": "..."},
    {"id": "A2", "rating": "C2", "statement": "..."}
  ],
  "edges": [
    {"from": "A1", "to": "Answer_Core", "type": "ontological"}
  ],
  "critical_path": ["A1", "Answer_Core"],
  "ontological_risk": true
}
```

#### 7.5 Depth  Contribution

```json
{
  "skill": "deep-think",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": N, "ec": 0.XX},
  "gates_verified": {"V1": true, "V2": true, "V3": true},
  "limitations": ["..."]
}
```

---

### 8 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V1** | Assumption Coverage | Every claim in answer traces to an assumption in Step 2 (≥90%) |
| **V2** | Alternative Independence | CIM(approaches) ≥ 0.5 |
| **V3** | Opposition Authenticity | Challenge (Step 4) references specific answer text + external evidence |

**If any gate FAILS:** Return to the relevant step and fix. Do not deliver.

---

### 9 — RECURSIVE SELF-AUDIT (if `recursion_depth` > 1)

If `recursion_depth` > 1, apply **this entire protocol** to your own output from Steps 1-8.

For each recursion level d = 2 to `recursion_depth`:

1. Treat your previous output as the "answer under review"
2. Run Steps 1-8 on it
3. Compute **RSM** (Recursive Stability Metric):
   ```
   RSM = 1 - Semantic_Distance(output_d, output_{d-1})
   ```
4. Compute **SI_d** (Surprise Index at depth d)
5. **Convergence Check:**
   - If RSM > 0.95 AND SI_d ≥ SI_{d-1} for 2 consecutive depths → **CONVERGED**, stop
   - If RSM < 0.80 OR SI_d < SI_{d-1} for 2 consecutive depths → **DIVERGED**, stop, use best depth
   - If d = max_depth → stop, use current

**Artifact:** `recursion_log` with RSM and SI at each depth.

**CEI Component:** Recursive Audit (weight 5.0 per level)

---

### 10 — INTERFERENCE: Receive from Prior Skills

If `require_interference` = true, CONDUCTOR will have fed you interference from prior skills. You must:

1. **Acknowledge** each interference received
2. **Show** how it changed your output (or why it didn't)
3. **Verify** minimum interference thresholds met

| From Skill | Required Interference | Minimum | Your Received |
|------------|----------------------|---------|---------------|
| (none for Phase 1) | — | — | — |

**Artifact:** `interference_log`

---

## The Deeper Purpose

This skill does not add intelligence. It interrupts the reflex that wastes it. The model's knowledge exists at multiple depths — and the surface response, because it arrives first and sounds confident, suppresses everything beneath it. **Six mandatory written artifacts + mathematical metrics + recursive audit + verification gates** force the model past the surface into genuine search. The metrics are not decoration. They are the mechanism: each one enters the context window and physically changes what the model generates next. The recursion forces the model to audit its own audit. The gates prevent cargo cult compliance.

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 1. It outputs:
```json
{
  "phase": 1,
  "skill": "deep-think",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: restatement (1.0), assumption_list (2.0), branch_cards (3.0×N), challenge (4.0), failure_envelope (3.0), final_answer (1.0), recursive_audit (5.0×depth)
- Total complexity weight: 14.0 + 3.0×(branches-3) + 5.0×recursion_depth

### SI Components
- C2/C3 assumptions: [count from Step 3 rating]
- Contrarian viable: [true/false from DIVERGE interference]
- Fatal attacks: [count from Step 4]
- Boundary violations: [count from Step 5]
- Assumption reversals: [count from EXCAVATE interference]

### Cognitive Traces Produced
- [x] Activation Heatmap
- [x] Assumption Dependency Graph
- [ ] Decision Landscape (produced by DIVERGE/TEMPORAL)

### Gates Verified
- [x] V1  [x] V2  [x] V3  [ ] V4  [ ] V5  [ ] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From EXCAVATE: C2/C3 assumptions → inversion targets (INVERT)
- From DIVERGE: Contrarian path viability → SI component
- From ADVERSARY: Fatal attacks → challenge revision