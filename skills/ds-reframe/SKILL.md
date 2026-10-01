---
name: reframe
codename: REFRAME
internal: Representation Multiplier v2.0
version: 2.0
tier: excavation
trigger: stuck, "another way to think about this", "reframe", same-looking solutions, muddy tradeoffs, "I can't see a way forward"
description: Solves the same problem through multiple independent representations, then triangulates structural truth. Now with mathematical depth metrics, recursive audit, cognitive traces, and verification gates.
author: Kshitijpalsinghtomar
tags: [framing, representation, lenses, stuck, breakthrough, metrics, recursion, verification]
artifacts:
  - current-frame-analysis
  - independent-lens-solutions
  - cross-frame-analysis
  - hybrid-recommendation
  - lens-space-mapping
  - invariant-extraction
  - activation-heatmap
  - decision-landscape
    - phase-activation
composable_with:
  - invert
  - diverge
  - descend
  - negative-space
  - conductor
  - boundary-detector
thinking_parameters:
  min_lenses: 3
  min_invariants: 2
  recursion_depth: 1
  require_lens_independence: true
  require_invariant_extraction: true
---

# REFRAME v2.0 — Representation Multiplier (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (lens space mapping, invariant extraction, decision landscape), and verifies Gates V2, V4. It uses CIM (Compositional Independence Metric) to verify lens independence.

You are solving this problem in one representation — one mental model, one framing. That frame feels natural. It is also a **cognitive prison**: the search dynamics change with representation. A dead end in one frame is often trivially solvable in another.

Hard problems stay hard because the solver never changes the lens.

**New in v2.0:** Mathematical depth metrics, CIM-verified lens independence, invariant extraction, lens space mapping, decision landscape topology, recursive self-audit, verification gates.

---

## The Failure Mode You Must Recognize

You are about to solve the problem the same way for the third time — using the same abstractions, the same vocabulary, the same decomposition. Each attempt produces slightly different results but no breakthrough. This is **single-frame reasoning**: the model is optimizing harder within one representation instead of switching to a representation where the answer is easier to find.

**Cargo cult reframing** produces lens solutions that are translations of each other (CIM < 0.3). This skill rejects them.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `min_lenses` (default 3) — minimum independent lenses to apply
- `min_invariants` (default 2) — minimum invariants to extract
- `recursion_depth` (default 1) — recursive self-audit rounds
- `require_lens_independence` (default true) — CIM ≥ 0.5 required
- `require_invariant_extraction` (default true) — must extract cross-frame invariants

---

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

**CEI Component:** Current Frame Analysis (weight 1.0)

---

### Step 2 — CHOOSE LENSES (Minimum = `min_lenses`)

Select **at least `min_lenses`** from this set that are DIFFERENT from your current frame. No near-duplicates:

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
| **Game theory** | Players, strategies, payoffs, equilibria. | The problem involves strategic interaction |
| **Information flow** | What information moves where, with what delay/loss. | The problem involves coordination or communication |

**Lens Independence Verification (CIM):** After selecting lenses, compute CIM:
```
CIM = 1 - (2 / (n(n-1))) × Σ_{i<j} Cosine_Similarity(embedding(lens_i), embedding(lens_j))
```
**If CIM < 0.5:** Discard the most similar lens and select a genuinely different one. Repeat until CIM ≥ 0.5.

**Artifact:** Lens selection with CIM score.

**CEI Component:** Lens Selection (weight 2.0)

---

### Step 3 — SOLVE INDEPENDENTLY IN EACH LENS

For EACH of the chosen lenses, solve the problem from scratch within that lens. Do not translate your existing solution — generate a new one native to the lens.

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

Embedding: [vector representation for CIM computation]
────────────────────────────────────────
```

**Anti-contamination rule:** Do not solve in Lens B by translating your Lens A solution. Start fresh. The value is in what each lens reveals independently. Contamination defeats the purpose.

**Artifact:** Independent lens solutions (minimum `min_lenses`, CIM ≥ 0.5).

**CEI Component:** Lens Solutions (weight 4.0 each)

---

### Step 4 — EXTRACT CROSS-FRAME STRUCTURE

Compare the solutions. Write:

```
CROSS-FRAME ANALYSIS
────────────────────────────────────────
INVARIANTS (true in all lenses — minimum min_invariants):
  I1: [statement] — this is a STRONG structural truth
  I2: [statement]
  ...

CONTRADICTIONS (Lens A says X, Lens B says opposite):
  T1: [Lens [A] recommends X] vs [Lens [B] recommends NOT X]
      This tension reveals: [what tradeoff this actually is]
  ...

UNIQUE INSIGHTS (visible in only one lens):
  Lens [N]: [insight not visible from other angles]
  ...

LENS SPACE MAPPING:
  [Map each lens to its region in the problem space — what it illuminates vs. hides]
────────────────────────────────────────
```

**Invariants** survive reframing — they are the problem's real structure, not artifacts of your framing.

**Contradictions** are not bugs — they reveal the most important tradeoff in the problem. The contradiction IS the design decision.

**Unique insights** are the payoff. These are things invisible from your original frame.

**Artifact:** Cross-frame analysis with invariants, contradictions, unique insights, lens space mapping.

**CEI Component:** Cross-Frame Analysis (weight 5.0)

**SI Component:** Contradictions found (count)

---

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
Lens Space Coverage:          [what fraction of problem space the lenses cover]
────────────────────────────────────────
```

**Artifact:** Hybrid recommendation.

**CEI Component:** Hybrid Recommendation (weight 3.0)

---

### Step 6 — DECISION LANDSCAPE TOPOLOGY

**NEW IN v2.0** — Visualize the decision space across lenses and futures.

```
DECISION LANDSCAPE
────────────────────────────────────────
Lenses: [list all lenses with names]
Dimensions: [Present, Growth, Disruption, Long-term] (from TEMPORAL interference)
Profiles:
  Lens A: [0.9, 0.6, 0.2, 0.1]  # peaks now, cliffs at disruption
  Lens B: [0.6, 0.8, 0.7, 0.8]  # robust across futures
  Lens C: [0.3, 0.4, 0.9, 0.7]  # contrarian, wins in disruption
  Hybrid: [0.7, 0.8, 0.8, 0.8]  # best option value

Recommended: [Hybrid]
Escape Hatches: [trigger conditions for switching]
────────────────────────────────────────
```

**Artifact:** `decision_landscape` — for cognitive trace.

---

### 7 — METRICS: Compute and Output Depth Metrics

#### 7.1 Phase Activation (for ADS)

```json
{
  "phase": 2,
  "skill": "reframe",
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
    "current_frame_analysis": 1.0,
    "lens_selection": 2.0,
    "lens_solutions": 4.0,
    "cross_frame_analysis": 5.0,
    "hybrid_recommendation": 3.0,
    "decision_landscape": 2.0,
    "total_complexity_weight": 21.0,
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
    "c2_c3_count": 0,
    "contrarian_viable": false,
    "fatal_attacks": 0,
    "boundary_violations": 0,
    "assumption_reversals": 0,
    "contradictions_found": N,
    "si_total": N
  }
}
```

#### 7.4 Cognitive Traces

**Lens Space Mapping:**
```json
{
  "type": "lens_space_mapping",
  "lenses": [
    {"name": "Constraint Graph", "coverage": 0.XX, "overlap_with_others": 0.XX},
    {"name": "State Machine", "coverage": 0.XX, "overlap_with_others": 0.XX},
    {"name": "Cost Function", "coverage": 0.XX, "overlap_with_others": 0.XX}
  ],
  "cim": 0.XX,
  "invariant_coverage": 0.XX
}
```

**Invariant Extraction:**
```json
{
  "type": "invariant_extraction",
  "invariants": [
    {"statement": "...", "supporting_lenses": ["A", "B", "C"], "strength": 0.XX},
    {"statement": "...", "supporting_lenses": ["A", "B"], "strength": 0.XX}
  ],
  "contradictions": [
    {"lens_a": "A", "lens_b": "B", "tradeoff": "...", "resolution": "..."}
  ]
}
```

**Decision Landscape:** (as defined in Step 6)

#### 7.5 Depth  Contribution

```json
{
  "skill": "reframe",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": N, "ec": 0.XX},
  "gates_verified": {"V2": true, "V4": true},
  "limitations": ["..."]
}
```

---

### 8 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V2** | Alternative Independence | CIM(lenses) ≥ 0.5 |
| **V4** | Temporal Consistency | If TEMPORAL ran: chosen hybrid survives ≥2/3 futures (from TEMPORAL interference) |

**If any gate FAILS:** Return to relevant step and fix. Do not deliver.

---

### 9 — RECURSIVE SELF-AUDIT (if `recursion_depth` > 1)

If `recursion_depth` > 1, apply **this entire protocol** to your own output from Steps 1-5.

For each recursion level d = 2 to `recursion_depth`:
1. Treat your previous output as the "answer under review"
2. Run Steps 1-5 on it
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

### 10 — INTERFERENCE: Receive and Provide

**Receive from prior skills:**

| From Skill | Interference | Use |
|------------|--------------|-----|
| DESCEND | Break points | Select lenses that address break points |
| EXCAVATE | C2/C3 assumptions | Challenge assumptions in each lens |
| DIVERGE | Path profiles | Map to lens space |
| TEMPORAL | Future scenarios | Test invariants across futures |

**Provide to later skills:**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| INVERT | Invariants → belief inversion targets | +0.15 |
| DIVERGE | Lens space mapping → path independence | +0.15 |
| ADVERSARY | Contradictions → attack targets | +0.15 |
| CONDUCTOR | Invariants, CIM, lens space coverage | +0.20 |

**Artifact:** `interference_log` (received and provided).

---

## The Deeper Purpose

A problem is mathematically equivalent across representations, but search is not. The path to a solution that is invisible in one frame may be the obvious path in another. **Three independent solutions from three different lenses reveal overlapping structural truths (invariants), hidden tradeoffs (contradictions), and invisible insights (unique findings).** The hybrid exceeds what any single frame could produce — not by adding quantity, but by triangulating the problem's actual structure from multiple angles. **Now it's quantified (CIM), verified (gates), and traceable (traces).**

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 2. It outputs:
```json
{
  "phase": 2,
  "skill": "reframe",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: current_frame_analysis (1.0), lens_selection (2.0), lens_solutions (4.0×N), cross_frame_analysis (5.0), hybrid_recommendation (3.0), decision_landscape (2.0)
- Total complexity weight: 21.0 + 4.0×(lenses-3)

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: 0
- Assumption reversals: 0
- Contradictions found: [count from Step 4]

### Cognitive Traces Produced
- [ ] Activation Heatmap
- [ ] Assumption Dependency Graph
- [x] Lens Space Mapping
- [x] Invariant Extraction
- [x] Decision Landscape

### Gates Verified
- [ ] V1  [x] V2  [ ] V3  [x] V4  [ ] V5  [ ] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From DESCEND: Break points → lens selection
- From EXCAVATE: C2/C3 assumptions → challenge in each lens
- From DIVERGE: Path profiles → lens space mapping
- From TEMPORAL: Future scenarios → invariant testing