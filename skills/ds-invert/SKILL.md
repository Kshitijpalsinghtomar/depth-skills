---
name: invert
codename: INVERT
internal: Constraint & Belief Inversion v2.0
version: 2.0
tier: excavation
trigger:
  - "we have no choice"
  - "given these constraints"
  - "boxed in"
  - "all options are bad"
  - "are we sure"
  - "what if we're wrong"
description: Flips constraints and beliefs to expose false walls and test plan robustness against inverted worldviews. Now with mathematical depth metrics, recursive audit, cognitive traces, and verification gates.
author: Kshitijpalsinghtomar
tags: [inversion, constraints, beliefs, robustness, counterfactual, metrics, recursion, verification]
artifacts:
  - constraint-map
  - inversion-table
  - load-bearing-beliefs
  - robustness-verdict
  - counterfactual-worlds
  - sensitivity-surface
  - activation-heatmap
  - belief-network-analysis
    - phase-activation
composable_with:
  - excavate
  - reframe
  - diverge
  - descend
  - conductor
  - boundary-detector
thinking_parameters:
  min_constraints: 5
  min_beliefs: 3
  recursion_depth: 1
  require_sensitivity_surface: true
  require_counterfactual_worlds: true
  require_belief_network: true
---

# INVERT v2.0 — Constraint & Belief Inversion (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (sensitivity surface, belief network analysis, counterfactual worlds), and verifies Gates V2, V3, V4. It integrates with EXCAVATE for C2/C3 assumption targeting.

Two forces trap answers in small spaces: **false constraints** (walls that aren't walls) and **untested beliefs** (foundations that might not be solid). Both feel real from inside. Both can collapse when tested.

This skill flips things. It inverts constraints to find which are real and which are habits. It inverts beliefs to find which are load-bearing and which are replaceable. Then it solves the problem from the opposite world — to discover what only becomes visible from the other side.

**New in v2.0:** Mathematical depth metrics, sensitivity surfaces, counterfactual worlds, belief network analysis, robustness s, recursive self-audit, verification gates.

---

## The Failure Mode You Must Recognize

You are about to generate a response that:
- Accepts constraints at face value without testing their hardness
- Holds beliefs without seeking evidence against them
- Solves only within the given frame, never from the opposite world
- **Produces inversion tables without measuring actual robustness impact (cargo cult inversion)**

If you recognize this pattern forming — you are in the constraint trap. Continue with the protocol.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `min_constraints` (default 5) — minimum constraints to map
- `min_beliefs` (default 3) — minimum load-bearing beliefs to test
- `recursion_depth` (default 1) — recursive self-audit rounds
- `require_sensitivity_surface` (default true) — compute sensitivity surface
- `require_counterfactual_worlds` (default true) — simulate counterfactuals
- `require_belief_network` (default true) — analyze belief interdependencies

---

## Part 1: Constraint Inversion

### Step 1 — WRITE THE CONSTRAINT MAP (Minimum = `min_constraints`)

List every constraint on THIS problem. For each, classify its type:

```
CONSTRAINT MAP
────────────────────────────────────────
C1: [constraint statement]
    Type:    [physical / legal / economic / policy / habit / assumption]
    Source:  [who stated this? user / me / industry convention / nobody-explicit]
    Hardness:[hard — cannot violate / soft — could be negotiated or removed]
    Sensitivity: [0.0-1.0 — how much solution changes if this constraint relaxes]

C2: [constraint statement]
    Type:    [type]
    Source:  [source]
    Hardness:[hard / soft]
    Sensitivity: [0.0-1.0]

...

Bottleneck constraint: C[N] — [this is the one most limiting the solution space]
────────────────────────────────────────
```

**Type definitions:**
1. **Physical** — speed of light, conservation laws. Cannot violate.
2. **Legal** — regulations, contracts, compliance. Cannot violate (but can sometimes work around).
3. **Economic** — money, resources, time. Can be traded.
4. **Policy** — internal rules, team decisions. Can be renegotiated.
5. **Habit** — "we always do it this way." Usually invertible without consequence.
6. **Assumption** — inherited from pattern matching. Unknown truth value. Most dangerous type.

**Key insight:** Constraints labeled "physical" are sometimes misclassified "policy" or "habit." If you cannot explain WHY this constraint cannot be violated in terms of physics or law — it's probably softer than you think.

**Artifact:** The constraint map with types, bottleneck, and sensitivity scores.

**CEI Component:** Constraint Map (weight 3.0)

**SI Component:** Boundary violations (assumption/habit constraints with high sensitivity)

---

### Step 2 — INVERT THE BOTTLENECK (and all assumption/habit constraints)

For the bottleneck constraint (and any "assumption" or "habit" type constraints), run three inversions:

```
INVERSION TABLE — CONSTRAINT C[N]
────────────────────────────────────────
Original: [the constraint as stated]

Full inversion:    [assume the exact opposite is true]
  Solution:        [what approach becomes possible?]
  Safety:          [upside if correct / downside if wrong]
  Sensitivity:     [how much answer quality changes — 0.0-1.0]

Partial inversion: [relax by 20-40%, not fully remove]
  Solution:        [what opens up?]
  Safety:          [upside / downside]
  Sensitivity:     [0.0-1.0]

Temporal inversion:[this holds now but not in 6 months, or vice versa]
  Solution:        [what does the transition path look like?]
  Safety:          [upside / downside]
  Sensitivity:     [0.0-1.0]
────────────────────────────────────────
```

**Hard rule:** Never invert physical or legal constraints. DO invert assumptions, habits, and policies — these are the source of most false boxes.

**Artifact:** The inversion table with sensitivity scores.

**CEI Component:** Inversion Tables (weight 4.0 per constraint)

**SI Component:** Boundary violations (inversions with high sensitivity that change answer)

---

### Step 3 — SENSITIVITY SURFACE (if `require_sensitivity_surface` = true)

**NEW IN v2.0** — Quantify how sensitive the solution is to each constraint.

```
SENSITIVITY SURFACE
────────────────────────────────────────
For each constraint:
  Constraint: [statement]
  Type: [type]
  Sensitivity Index: [0.0 - 1.0]
    Definition: |ΔSolution_Quality / ΔConstraint_Truth|
    Computed by: [counterfactual simulation / analytical / expert judgment]
  Critical Threshold: [constraint value below which solution fails]
  Interaction Effects: [other constraints that amplify/dampen this sensitivity]
  Mitigation: [what reduces sensitivity — e.g., fallback, monitoring, redesign]
────────────────────────────────────────
```

**Artifact:** `sensitivity_surface` — maps constraint space to solution robustness.

**CEI Component:** Sensitivity Surface (weight 4.0)

---

## Part 2: Belief Inversion

### Step 4 — WRITE THE LOAD-BEARING BELIEFS (Minimum = `min_beliefs`)

A belief is something held as true without significant doubt. Every plan rests on beliefs about reality:

Write the beliefs that, if wrong, would damage the plan most:

```
LOAD-BEARING BELIEFS
────────────────────────────────────────
B1: [belief statement — e.g., "Users want speed more than features"]
    Evidence for: [why you believe this — be specific]
    Evidence against: [genuine reasons the opposite could be true — not straw men]
    Confidence: [0.0-1.0]
    Centrality: [0.0-1.0 — how central to the plan]

B2: [belief statement]
    Evidence for: [specific]
    Evidence against: [genuine]
    Confidence: [0.0-1.0]
    Centrality: [0.0-1.0]

B3: [belief statement]
    Evidence for: [specific]
    Evidence against: [genuine]
    Confidence: [0.0-1.0]
    Centrality: [0.0-1.0]

[Additional beliefs up to min_beliefs...]
────────────────────────────────────────
```

**The "evidence against" step is the hardest and most important.** You must write real reasons the opposite could be true — not weak dismissable reasons. If you cannot find any evidence against a belief, you haven't looked hard enough.

**Artifact:** Beliefs with evidence both directions, confidence, centrality.

**CEI Component:** Load-Bearing Beliefs (weight 3.0)

---

### Step 5 — BELIEF NETWORK ANALYSIS (if `require_belief_network` = true)

**NEW IN v2.0** — Map how beliefs depend on each other.

```
BELIEF NETWORK ANALYSIS
────────────────────────────────────────
Nodes: [beliefs B1, B2, B3...]
Edges: [B1 → B2 means B2 depends on B1]

For each belief:
  Belief: [statement]
  Dependencies: [which other beliefs this depends on]
  Dependents: [which beliefs depend on this]
  Cascade Risk: [if this belief fails, how many others collapse? 0.0-1.0]

Critical Beliefs (Cascade Risk > 0.7):
  [List — these are single points of failure in the belief network]
────────────────────────────────────────
```

**Artifact:** `belief_network_analysis` — identifies belief cascade risks.

**CEI Component:** Belief Network Analysis (weight 4.0)

---

### Step 6 — SOLVE FROM THE OPPOSITE WORLD (Counterfactual Worlds)

For EACH belief, construct the opposite world and solve the problem there:

```
COUNTERFACTUAL WORLD [N]
────────────────────────────────────────
Original belief:           [from Step 4]
Inverted belief:           [the opposite]
If the opposite is true:   [what does the correct plan look like?]
Similarity to original plan:[high / moderate / low / orthogonal]
  If orthogonal → belief is FOUNDATIONAL (plan destroyed if wrong)
  If moderate → belief is STRUCTURAL (plan damaged if wrong)
  If high → belief is PERIPHERAL (plan survives if wrong)
Robustness Implication:    [what this counterfactual tells us about plan fragility]
────────────────────────────────────────
```

**Minimum:** One counterfactual world per belief.

**Artifact:** `counterfactual_worlds` — the plan's behavior across belief violations.

**CEI Component:** Counterfactual Worlds (weight 4.0 per belief)

**SI Component:** Boundary violations (counterfactuals with low similarity)

---

### Step 7 — ROBUSTNESS VERDICT & 

```
ROBUSTNESS VERDICT
────────────────────────────────────────
B1: if wrong → [plan survives / plan damaged / plan destroyed]
B2: if wrong → [plan survives / plan damaged / plan destroyed]
B3: if wrong → [plan survives / plan damaged / plan destroyed]

Overall:      [antifragile / robust / fragile / brittle]

For fragile/brittle plans:
  Verify:     [which beliefs to test before committing]
  Pivot:      [what triggers indicate a belief is wrong — early warning signals]
  Redesign:   [can the plan be restructured for belief-independence?]

ROBUSTNESS :
   ID: rc_<timestamp>_<hash>
  Plan: [description]
  Overall Robustness: [antifragile/robust/fragile/brittle]
  Critical Beliefs: [list with cascade risk]
  Verification Required: [list of beliefs to test]
  Early Warning Signals: [observable triggers]
  Valid Until: [date or condition]
────────────────────────────────────────
```

**Artifact:** Robustness verdict with .

**CEI Component:** Robustness Verdict (weight 3.0)

---

### 8 — METRICS: Compute and Output Depth Metrics

#### 8.1 Phase Activation (for ADS)

```json
{
  "phase": 2,
  "skill": "invert",
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
    "constraint_map": 3.0,
    "inversion_tables": 4.0,
    "sensitivity_surface": 4.0,
    "load_bearing_beliefs": 3.0,
    "belief_network_analysis": 4.0,
    "counterfactual_worlds": 4.0,
    "robustness_verdict": 3.0,
    "total_complexity_weight": 26.0,
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

**Sensitivity Surface:**
```json
{
  "type": "sensitivity_surface",
  "constraints": [
    {"id": "C1", "type": "assumption", "sensitivity": 0.XX, "threshold": 0.XX},
    {"id": "C2", "type": "habit", "sensitivity": 0.XX, "threshold": 0.XX}
  ],
  "interactions": [
    {"C1": "C1", "C2": "C2", "effect": "amplifying", "factor": 1.XX}
  ]
}
```

**Belief Network Analysis:**
```json
{
  "type": "belief_network_analysis",
  "nodes": [
    {"id": "B1", "statement": "...", "confidence": 0.XX, "centrality": 0.XX, "cascade_risk": 0.XX},
    {"id": "B2", "statement": "...", "confidence": 0.XX, "centrality": 0.XX, "cascade_risk": 0.XX}
  ],
  "edges": [
    {"from": "B1", "to": "B2", "type": "depends_on"}
  ],
  "critical_beliefs": ["B1"]
}
```

**Counterfactual Worlds:**
```json
{
  "type": "counterfactual_worlds",
  "worlds": [
    {"belief": "B1", "inverted": "...", "similarity": "orthogonal", "robustness": "destroyed"},
    {"belief": "B2", "inverted": "...", "similarity": "moderate", "robustness": "damaged"}
  ]
}
```

#### 8.5 Depth  Contribution

```json
{
  "skill": "invert",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": N, "ec": 0.XX},
  "gates_verified": {"V2": true, "V3": true, "V4": true},
  "limitations": ["..."]
}
```

---

### 9 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V2** | Alternative Independence | If REFRAME/DIVERGE ran: CIM ≥ 0.5 (from interference) |
| **V3** | Opposition Authenticity | Every inversion references specific constraint/belief + cites evidence |
| **V4** | Temporal Consistency | If TEMPORAL ran: chosen plan survives ≥2/3 futures (from TEMPORAL interference) |

**If any gate FAILS:** Return to relevant step and fix. Do not deliver.

---

### 10 — RECURSIVE SELF-AUDIT (if `recursion_depth` > 1)

If `recursion_depth` > 1, apply **this entire protocol** to your own output from Parts 1-2.

For each recursion level d = 2 to `recursion_depth`:
1. Treat your previous output as the "answer under review"
2. Run Parts 1-2 on it
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
| EXCAVATE | C2/C3 assumptions | Target as inversion constraints/beliefs |
| REFRAME | Invariants | Test as load-bearing beliefs |
| DESCEND | Broken preconditions | Invert as constraints |
| BOUNDARY-DETECTOR | Knowledge gaps | Flag as assumption-type constraints |

**Provide to later skills:**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| ADVERSARY | Inverted constraints/beliefs → fatal attacks | +0.20 |
| DIVERGE | Counterfactual solutions → contrarian paths | +0.15 |
| THRESHOLD | Robustness verdict → reversal cost function | +0.15 |
| CONDUCTOR | Sensitivity surface, belief network, robustness cert | +0.20 |

**Artifact:** `interference_log` (received and provided).

---

## The Deeper Purpose

The model selects one frame, one set of constraints, one set of beliefs — and optimizes within that space. The deeper knowledge (how the world looks from other frames) sits unused. This skill forces the model to use that knowledge: not think harder within one worldview, but genuinely construct alternative worldviews and report what changes. **Now it's quantified (sensitivity, cascade risk, similarity), verified (gates), and certified (robustness ).** Innovation is often constraint truth-maintenance. Robustness is often belief-testing before commitment. Both require inversion — and now they're measurable.

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 2. It outputs:
```json
{
  "phase": 2,
  "skill": "invert",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: constraint_map (3.0), inversion_tables (4.0×N), sensitivity_surface (4.0), load_bearing_beliefs (3.0), belief_network_analysis (4.0), counterfactual_worlds (4.0×N), robustness_verdict (3.0)
- Total complexity weight: 26.0 + 4.0×(constraints-5) + 4.0×(beliefs-3)

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: [inversions with high sensitivity + counterfactuals with low similarity]
- Assumption reversals: 0

### Cognitive Traces Produced
- [x] Sensitivity Surface
- [x] Belief Network Analysis
- [x] Counterfactual Worlds
- [ ] Decision Landscape

### Gates Verified
- [ ] V1  [x] V2  [x] V3  [x] V4  [ ] V5  [ ] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From EXCAVATE: C2/C3 assumptions → inversion targets
- From REFRAME: Invariants → belief inversion targets
- From DESCEND: Broken preconditions → constraint inversion
- From BOUNDARY-DETECTOR: Knowledge gaps → assumption-type constraints