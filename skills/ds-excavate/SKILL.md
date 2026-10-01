---
name: excavate
codename: EXCAVATE
internal: Assumption Archaeology v2.0
version: 2.0
tier: excavation
trigger:
  - "what am I assuming"
  - "is this safe"
  - "high-stakes plan"
  - "any answer that feels solid but hasn't been tested at its roots"
description: Digs beneath logic to inspect unchecked premises, rating each assumption by collapse severity. Now with sensitivity surfaces, counterfactual worlds, boundary detection integration, and mathematical depth metrics.
author: Kshitijpalsinghtomar
tags: [assumptions, foundations, premises, risk, validation, sensitivity, counterfactual, metrics]
artifacts:
  - assumption-list
  - deep-layer-questions
  - collapse-ratings
  - resolution-log
  - sensitivity-surface
  - counterfactual-worlds
    - phase-activation
composable_with:
  - invert
  - negative-space
  - threshold
  - adversary
  - conductor
  - boundary-detector
thinking_parameters:
  min_assumptions: 10
  min_deep_questions: 5
  collapse_threshold: "C2"
  require_sensitivity_surface: true
  require_counterfactual_worlds: true
  require_boundary_probes: true
---

# EXCAVATE v2.0 — Assumption Archaeology (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (sensitivity surface, assumption dependency graph), and verifies Gates V1, V2. It integrates with BOUNDARY-DETECTOR for knowledge boundary probes.

Every answer stands on ground you haven't inspected. The logic is flawless. The conclusion follows from the premises. No one checked the premises.

"Valid" means "correct IF the premises are true." You never verified that they are. The premises were absorbed — from the problem description, from pattern matching, from your model of the user's situation. Each is a silent **load-bearing wall**. Remove one, and everything above it collapses.

This skill digs beneath the logic to inspect the ground. **Now it maps the sensitivity surface and simulates counterfactual worlds.**

---

## The Failure Mode You Must Recognize

You are about to deliver an answer that:
- Lists assumptions you already know are true (safe, performative)
- Skips assumptions you absorbed from pattern matching without noticing
- Conflates "I haven't seen evidence against this" with "this is true"
- Never checks whether the problem itself is correctly framed
- **Produces assumption lists without measuring their actual impact (sensitivity)**

Surface assumptions are not the threat. The threat is the assumptions you don't know you're making. **The threat is assumptions whose collapse you haven't simulated.**

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `min_assumptions` (default 10) — minimum assumptions in Step 1
- `min_deep_questions` (default 5) — minimum deep questions in Step 2
- `collapse_threshold` (default "C2") — minimum rating requiring resolution
- `require_sensitivity_surface` (default true) — compute sensitivity surface
- `require_counterfactual_worlds` (default true) — simulate counterfactuals
- `require_boundary_probes` (default true) — probe knowledge boundaries

---

### 1 — WRITE THE SURFACE LAYER: Assumptions (Minimum = `min_assumptions`)

List everything this answer takes as given. Write each one as a clear, falsifiable statement.

**Categories to scan — write at least two per category:**

**Input assumptions** (about the data, system, and context):
- "The user's [system/data/environment] can [support/handle/provide] [X]."

**Pattern assumptions** (inherited from your pattern match):
- "This is the same type of problem as [source domain], therefore [Y applies]."

**Scope assumptions** (what's in and out — who decided?):
- "The scope includes [A] and excludes [B]."

**User assumptions** (about what they know, want, and have):
- "The user [has access to / understands / is willing to] [Z]."

**Absence assumptions** (what you assume is NOT present):
- "There is no [existing system / constraint / stakeholder / requirement] that would affect this."

**Minimum `min_assumptions`.** Fewer than `min_assumptions` means you stopped at the surface. The dangerous assumptions are always below the comfortable ones.

**Artifact:** Numbered assumption list. Step 2 and 3 reference these by number.

**CEI Component:** Assumption List (weight 2.0)

---

### 2 — WRITE THE DEEP LAYER: Questions You Haven't Asked (Minimum = `min_deep_questions`)

These are harder. They challenge the framing of the problem itself, not just the solution.

Write your honest answer to each:

```
DEEP LAYER QUESTIONS
────────────────────────────────────────
Q1: Am I solving the right problem, or is the user describing
    a symptom of a different problem?
    My answer: [write it — don't skip]

Q2: Which of my assumptions from Step 1 did I
    add from pattern matching, not from the actual problem statement?
    Candidates: [list assumption numbers from Step 1]

Q3: What context am I filling in that the user
    never actually stated? Write the specifics.
    I'm assuming: [list specific filled-in context]

Q4: What factor might exist that wasn't mentioned in the problem
    and would change my entire approach?
    Candidate factors: [list at least two]

Q5: If I showed my assumption list (Step 1) to the user and they
    said "actually, #[N] is wrong" — which number would
    most surprise me and most damage my answer?
    Most surprising wrong: Assumption #[N] — because [why]

[Additional questions up to min_deep_questions...]
────────────────────────────────────────
```

**Artifact:** Answered deep questions. These surface the unconscious assumptions the surface layer misses.

**CEI Component:** Deep Questions (weight 3.0)

---

### 3 — RANK: Write the Collapse Rating for Every Assumption

For each assumption from Steps 1 and 2, assign a collapse rating:

```
COLLAPSE RATINGS
────────────────────────────────────────
C0 — Cosmetic:     If wrong, answer needs minor rewording. Core survives.
C1 — Structural:   If wrong, significant parts must change. Core might survive.
C2 — Foundation:   If wrong, entire answer must be rebuilt from scratch.
C3 — Ontological:  If wrong, the PROBLEM was wrong. Wrong category entirely.
────────────────────────────────────────

Assumption #1:  [statement] — C[rating]
Assumption #2:  [statement] — C[rating]
...
Assumption #N:  [statement] — C[rating]

C2/C3 assumptions requiring resolution:
  #[N]: [statement]
  #[N]: [statement]
────────────────────────────────────────
```

**Artifact:** Full assumption list with collapse ratings. Step 4 processes every C2 and C3.

**CEI Component:** Collapse Ratings (weight 2.0)

**SI Component:** C2/C3 count

---

### 4 — RESOLVE: Process Every C2 and C3

For each C2/C3 assumption, choose one resolution strategy and execute it:

**Verify** — Find evidence it's true. Not "probably true." Actual evidence: a documented fact, a stated requirement, a known constraint. Write the evidence.

**Flag** — Cannot verify? Write this sentence in your output: "This answer assumes [X]. If [X] is false, the answer changes to [Y]." The user now knows the dependency.

**Design around** — Cannot verify AND highly critical? Redesign the answer so it does not depend on this assumption. Most expensive strategy, most robust result.

```
RESOLUTION LOG
────────────────────────────────────────
Assumption #[N] (C2): [statement]
  Strategy: [verify / flag / design-around]
  Result:   [evidence found / flagged in output / redesigned to avoid]
  Evidence: [specific citation / tool result / "none — flagged"]

Assumption #[N] (C3): [statement]
  Strategy: [verify / flag / design-around]
  Result:   [evidence found / flagged in output / redesigned to avoid]
  Evidence: [specific citation / tool result / "none — flagged"]
────────────────────────────────────────
```

**Artifact:** The resolution log. This proves every critical assumption was explicitly addressed — not left to hope.

**CEI Component:** Resolution Log (weight 3.0)

**SI Component:** Assumption reversals (where verification changed rating)

---

### 5 — SENSITIVITY SURFACE (if `require_sensitivity_surface` = true)

**NEW IN v2.0** — Quantify how sensitive the answer is to each assumption.

For each C2/C3 assumption, compute:

```
SENSITIVITY SURFACE
────────────────────────────────────────
Assumption #[N]: [statement]
  Collapse Rating: C[N]
  Sensitivity Index: [0.0 - 1.0]
    Definition: |ΔAnswer_Quality / ΔAssumption_Truth|
    Computed by: [counterfactual simulation / analytical / expert judgment]
  Critical Threshold: [assumption truth value below which answer fails]
  Interaction Effects: [other assumptions that amplify/dampen this sensitivity]
  Mitigation: [what reduces sensitivity — e.g., fallback, monitoring, redesign]
────────────────────────────────────────
```

**Sensitivity Index Computation:**
- **Counterfactual Simulation** (preferred): Flip assumption, re-run reasoning, measure answer quality delta
- **Analytical**: Derive mathematically from answer structure
- **Expert Judgment**: Calibrated estimate (flag as such)

**Artifact:** `sensitivity_surface` — maps assumption space to answer robustness.

**CEI Component:** Sensitivity Surface (weight 4.0)

---

### 6 — COUNTERFACTUAL WORLDS (if `require_counterfactual_worlds` = true)

**NEW IN v2.0** — Simulate worlds where key assumptions are false.

For each C2/C3 assumption, construct:

```
COUNTERFACTUAL WORLD [N]
────────────────────────────────────────
Assumption: [statement]
Inverted:   [negation of assumption]
World Description:
  [Describe the world where this assumption is false.
   Be specific: what changes in the environment, data, constraints?]

Answer in This World:
  [What does the correct answer look like in this world?
   Not "it would be different" — write the actual alternative approach.]

Similarity to Original Answer: [high / moderate / low / orthogonal]
  If orthogonal → assumption is FOUNDATIONAL (C3 confirmed)
  If moderate → assumption is STRUCTURAL (C2 confirmed)

Robustness Implication:
  [What does this counterfactual tell us about the answer's fragility?]
────────────────────────────────────────
```

**Minimum:** One counterfactual world per C2/C3 assumption.

**Artifact:** `counterfactual_worlds` — the answer's behavior across assumption violations.

**CEI Component:** Counterfactual Worlds (weight 4.0)

---

### 7 — BOUNDARY PROBES (if `require_boundary_probes` = true)

**NEW IN v2.0** — Integrate with BOUNDARY-DETECTOR to probe knowledge boundaries.

For each assumption that depends on model parametric knowledge:

```
BOUNDARY PROBE [N]
────────────────────────────────────────
Assumption: [statement]
Knowledge Dependency: [what parametric knowledge this assumes]
Probe Type: [UnknownBench-style / retrieval_gap / ensemble_disagreement]
Probe Result: [PASS / FAIL / UNCERTAIN]
  PASS: Knowledge confirmed present
  FAIL: Knowledge gap detected — assumption UNVERIFIED
  UNCERTAIN: Cannot determine

Implication: [If FAIL → assumption must be FLAGGED or DESIGNED AROUND]
────────────────────────────────────────
```

**Artifact:** `boundary_probes` — links assumptions to knowledge boundaries.

**CEI Component:** Boundary Probes (weight 3.0)

---

### 8 — METRICS: Compute and Output Depth Metrics

#### 8.1 Phase Activation (for ADS)

```json
{
  "phase": 1,
  "skill": "excavate",
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
    "assumption_list": 2.0,
    "deep_questions": 3.0,
    "collapse_ratings": 2.0,
    "resolution_log": 3.0,
    "sensitivity_surface": 4.0,
    "counterfactual_worlds": 4.0,
    "boundary_probes": 3.0,
    "total_complexity_weight": 21.0,
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
    "c2_c3_count": N,
    "contrarian_viable": false,
    "fatal_attacks": 0,
    "boundary_violations": N,
    "assumption_reversals": N,
    "si_total": N
  }
}
```

#### 8.4 Cognitive Traces

**Assumption Dependency Graph:**
```json
{
  "type": "assumption_dependency_graph",
  "nodes": [
    {"id": "A1", "rating": "C3", "statement": "...", "sensitivity": 0.XX},
    {"id": "A2", "rating": "C2", "statement": "...", "sensitivity": 0.XX}
  ],
  "edges": [
    {"from": "A1", "to": "Answer_Core", "type": "ontological", "sensitivity": 0.XX}
  ],
  "critical_path": ["A1", "Answer_Core"],
  "ontological_risk": true,
  "sensitivity_surface": {...}
}
```

**Sensitivity Surface Visualization:**
```json
{
  "type": "sensitivity_surface",
  "assumptions": [
    {"id": "A1", "rating": "C3", "sensitivity": 0.95, "threshold": 0.5},
    {"id": "A2", "rating": "C2", "sensitivity": 0.70, "threshold": 0.3}
  ],
  "interactions": [
    {"A1": "A1", "A2": "A2", "effect": "amplifying", "factor": 1.5}
  ]
}
```

#### 8.5 Depth  Contribution

```json
{
  "skill": "excavate",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": N, "ec": 0.XX},
  "gates_verified": {"V1": true, "V2": true},
  "limitations": ["..."]
}
```

---

### 9 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V1** | Assumption Coverage | Every claim in answer traces to an assumption (≥90%) |
| **V2** | Alternative Independence | If DIVERGE ran: CIM(paths) ≥ 0.5 (from DIVERGE interference) |

**If any gate FAILS:** Return to relevant step and fix. Do not deliver.

---

### 10 — INTERFERENCE: Provide to Later Skills

You must provide interference to:

| To Skill | Interference Type | Minimum ADS Gain | Your Output |
|----------|-------------------|------------------|-------------|
| INVERT | C2/C3 assumptions become inversion targets | +0.20 | List of C2/C3 assumptions with statements |
| ADVERSARY | Collapse ratings guide attack severity | +0.20 | C3→FATAL, C2→SIGNIFICANT mapping |
| BOUNDARY-DETECTOR | Knowledge-dependent assumptions for probing | +0.15 | Assumptions with knowledge dependencies |
| NEGATIVE-SPACE | Absent dimensions from assumption gaps | +0.10 | Dimensions not covered by assumptions |

**Artifact:** `interference_provided` log.

---

## The Deeper Purpose

Most wrong answers are not wrong in their logic. They are wrong in their foundations — flawless reasoning built on unchecked premises. The model assembles correct chains of reasoning on top of assumptions it absorbed unconsciously during pattern matching. The logic looks right. The conclusion is valid. And it fails in production because premise #3 was never true. **This skill forces the premises into the open where they can be inspected, rated, simulated, and addressed before the answer ships. The sensitivity surface and counterfactual worlds make the cost of each assumption visible and quantifiable.**

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 1. It outputs:
```json
{
  "phase": 1,
  "skill": "excavate",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: assumption_list (2.0), deep_questions (3.0), collapse_ratings (2.0), resolution_log (3.0), sensitivity_surface (4.0), counterfactual_worlds (4.0), boundary_probes (3.0)
- Total complexity weight: 21.0

### SI Components
- C2/C3 assumptions: [count from Step 3]
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: [count from Step 7]
- Assumption reversals: [count from Step 4]

### Cognitive Traces Produced
- [x] Assumption Dependency Graph (with sensitivity)
- [x] Sensitivity Surface
- [ ] Decision Landscape

### Gates Verified
- [x] V1  [x] V2  [ ] V3  [ ] V4  [ ] V5  [ ] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From DEEP-THINK: Assumptions from restatement → seed excavation
- From BOUNDARY-DETECTOR: Probe results → resolution strategy