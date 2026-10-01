---
name: shallow
codename: SHALLOW
internal: Proportional Depth Protocol v2.0
version: 2.0
tier: cognition
trigger: low-stakes task, reversible decision, "keep it simple", "don't overthink", quick answer needed
description: Prevents overthinking by matching cognitive investment to consequence - the intentional opposite of DEEP-THINK. Now with mathematical depth metrics, depth budget calculus, proportionality , and verification gates.
author: Kshitijpalsinghtomar
tags: [proportionality, efficiency, overthinking, quick-answer, depth-calibration, metrics, recursion, verification]
artifacts:
  - depth-assessment
  - budget-allocation
  - shallow-delivery-verdict
  - depth-budget-calculus
    - activation-heatmap
    - phase-activation
composable_with:
  - deep-think
  - threshold
  - conductor
  - boundary-detector
thinking_parameters:
  require_calculus: true
  require_proportionality_: true
  recursion_depth: 1
---

# SHALLOW v2.0 — Proportional Depth Protocol (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (depth budget calculus, proportionality ), and verifies Gates V1, V6. It formalizes proportional depth as a budget calculus.

DEEP-THINK is essential. But not every task deserves it. Sometimes the deepest answer is a short one.

The failure mode of depth-skills is **depth bias**: the model reaches for sophisticated analysis on problems that don't warrant it. A CSS color choice gets 6-step reasoning. A routine email gets threat-modeled. This skill is the brake.

**New in v2.0:** Mathematical depth metrics, depth budget calculus, proportionality , recursive self-audit, verification gates.

---

## The Failure Mode You Must Recognize

You are about to:
- Generate six artifacts for a question that could be answered in one sentence
- Add caveats to a decision that is easily reversed
- Apply THRESHOLD analysis to a temporary workaround
- Treat a first-pass response as if it were a permanent architecture decision

If the cost of being wrong is low and the fix is easy — this is a SHALLOW task.

**Cargo cult shallowness** gives short answers without justifying why depth isn't needed. This skill rejects it.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `require_calculus` (default true) — compute depth budget calculus
- `require_proportionality_` (default true) — issue proportionality 
- `recursion_depth` (default 1) — recursive self-audit rounds

---

### 1 — DEPTH BUDGET CALCULUS (if `require_calculus` = true)

**NEW IN v2.0** — Formal calculus for depth appropriateness.

Evaluate the task against depth criteria:

```
DEPTH BUDGET CALCULUS
────────────────────────────────────────
Reversibility:    [Trivial / Moderate / Hard / Permanent]
  Weight: [1.0 / 0.5 / 0.2 / 0.0] → Score: [value]

Consequence:      [Trivial / Moderate / Significant / Critical]
  Weight: [1.0 / 0.5 / 0.2 / 0.0] → Score: [value]

Complexity:       [Simple / Moderate / Complex / Intricate]
  Weight: [1.0 / 0.5 / 0.2 / 0.0] → Score: [value]

Pattern match:    [Routine / Variation / Novel / Unprecedented]
  Weight: [1.0 / 0.5 / 0.2 / 0.0] → Score: [value]

Stakeholders:     [One / Few / Many / All-hands]
  Weight: [1.0 / 0.5 / 0.2 / 0.0] → Score: [value]

Urgency:          [Can wait / Within hour / Within minute / Now]
  Weight: [1.0 / 0.5 / 0.2 / 0.0] → Score: [value]

────────────────────────────────────────
TOTAL SHALLOW SCORE: Σ Scores / 6 = [0.0-1.0]
  (1.0 = fully shallow, 0.0 = fully deep)

Depth Budget:
  SHALLOW SCORE ≥ 0.67 → MINIMAL (no artifacts, one sentence)
  0.33 ≤ SHALLOW SCORE < 0.67 → LIGHT (one artifact, one assumption, one alternative)
  SHALLOW SCORE < 0.33 → MODERATE (restatement + approach, skip challenge)
────────────────────────────────────────
```

**Artifact:** `depth_budget_calculus` — formal justification for depth level.

**CEI Component:** Depth Budget Calculus (weight 3.0)

---

### 2 — ALLOCATE COGNITIVE BUDGET

Based on the calculus, allocate:

```
BUDGET ALLOCATION
────────────────────────────────────────
Shallow Score: [0.XX]
Depth Budget:  [MINIMAL / LIGHT / MODERATE]

MINIMAL (Score ≥ 0.67):
  - No artifacts required
  - One sentence answer
  - Skip caveats
  - Skip alternatives
  - Skip "it depends"
  - ADS Target: 0.15

LIGHT (0.33 ≤ Score < 0.67):
  - One artifact: answer with ONE assumption stated
  - One alternative mentioned in 1 sentence
  - One caveat if genuinely important
  - ADS Target: 0.30

MODERATE (Score < 0.33):
  - Two artifacts: restatement + chosen approach
  - Skip challenge phase
  - Minimal boundary check
  - ADS Target: 0.45
────────────────────────────────────────
```

**Artifact:** Budget allocation with ADS targets.

**CEI Component:** Budget Allocation (weight 2.0)

---

### 3 — DELIVER WITHIN BUDGET

Execute the answer within allocated depth:

```
SHALLOW DELIVERY
────────────────────────────────────────
Budget level:   [MINIMAL / LIGHT / MODERATE]
Answer:         [deliver within budget constraints]

If MINIMAL:
  Answer only. No preamble. No caveats.
  
If LIGHT:
  State ONE assumption. Mention ONE alternative.
  One sentence each, inline.
  
If MODERATE:
  Restate in one sentence.
  Give the answer.
  One-line boundary: "works for [common case], not [edge case]."
────────────────────────────────────────
```

**Artifact:** The shallow delivery.

**CEI Component:** Shallow Delivery (weight 1.0)

---

### 4 — PROPORTIONALITY  (if `require_proportionality_` = true)

**NEW IN v2.0** — Formal  of proportional depth.

```
PROPORTIONALITY 
────────────────────────────────────────
 ID: pc_<timestamp>_<hash>
Task: [description]

Depth Budget Calculus:
  Reversibility: [level] → [score]
  Consequence: [level] → [score]
  Complexity: [level] → [score]
  Pattern Match: [level] → [score]
  Stakeholders: [level] → [score]
  Urgency: [level] → [score]
  Total Shallow Score: [0.XX]

Depth Budget: [MINIMAL / LIGHT / MODERATE]
ADS Target: [0.XX]
Actual ADS: [0.XX] (from CONDUCTOR)

Proportionality: [PROPORTIONAL / OVER-DEEP / UNDER-DEEP]

Proportional:     Actual ADS within ±0.1 of target
Over-Deep:        Actual ADS > target + 0.1 (wasted cognitive effort)
Under-Deep:       Actual ADS < target - 0.1 (insufficient analysis)

Status: [PROPORTIONAL / OVER-DEEP / UNDER-DEEP]
Valid Until: [date or condition]
────────────────────────────────────────
```

**Artifact:** `proportionality_` — formal verification of proportional depth.

**CEI Component:** Proportionality  (weight 2.0)

---

### 5 — METRICS: Compute and Output Depth Metrics

#### 5.1 Phase Activation (for ADS)

```json
{
  "phase": 1,
  "skill": "shallow",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

#### 5.2 CEI Components

```json
{
  "cei_components": {
    "depth_budget_calculus": 3.0,
    "budget_allocation": 2.0,
    "shallow_delivery": 1.0,
    "proportionality_": 2.0,
    "total_complexity_weight": 8.0,
    "output_tokens": N,
    "wall_time_seconds": T,
    "cei": 0.XX
  }
}
```

#### 5.3 SI Components

```json
{
  "si_components": {
    "c2_c3_count": 0,
    "contrarian_viable": false,
    "fatal_attacks": 0,
    "boundary_violations": 0,
    "assumption_reversals": 0,
    "proportionality_violations": 0,
    "si_total": 0
  }
}
```

#### 5.4 Cognitive Traces

**Depth Budget Calculus:**
```json
{
  "type": "depth_budget_calculus",
  "dimensions": [
    {"dimension": "Reversibility", "level": "...", "score": 0.XX},
    {"dimension": "Consequence", "level": "...", "score": 0.XX},
    {"dimension": "Complexity", "level": "...", "score": 0.XX},
    {"dimension": "Pattern Match", "level": "...", "score": 0.XX},
    {"dimension": "Stakeholders", "level": "...", "score": 0.XX},
    {"dimension": "Urgency", "level": "...", "score": 0.XX}
  ],
  "total_shallow_score": 0.XX,
  "depth_budget": "MINIMAL/LIGHT/MODERATE",
  "ads_target": 0.XX
}
```

**Proportionality :** (as defined in Step 4)

#### 5.5 Depth  Contribution

```json
{
  "skill": "shallow",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": 0, "ec": 0.XX},
  "gates_verified": {"V1": true, "V6": true},
  "limitations": ["..."]
}
```

---

### 6 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V1** | Assumption Coverage | If MODERATE budget: every claim traces to assumption |
| **V6** | Recursive Stability | If recursion: RSM > 0.95 ∧ SI not decreasing |

**If any gate FAILS:** Return to relevant step and fix. Do not deliver.

---

### 7 — RECURSIVE SELF-AUDIT (if `recursion_depth` > 1)

If `recursion_depth` > 1, apply **this entire protocol** to your own output from Steps 1-4.

For each recursion level d = 2 to `recursion_depth`:
1. Treat your previous output as the "answer under review"
2. Run Steps 1-4 on it
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

### 8 — INTERFERENCE: Receive and Provide

**Receive from prior skills:**

| From Skill | Interference | Use |
|------------|--------------|-----|
| CLARIFY | Readiness  | If NOT_READY → force MINIMAL budget |
| CONDUCTOR | Task profile | Auto-populate calculus dimensions |
| THRESHOLD | Reversal cost | If Category 1 → force MINIMAL |

**Provide to later skills:**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| DEEP-THINK | Shallow score → skip if ≥ 0.67 | +0.15 |
| CONDUCTOR | Depth budget → skill selection | +0.15 |
| THRESHOLD | Reversibility → category | +0.10 |

**Artifact:** `interference_log` (received and provided).

---

## When NOT to Use This Skill

SHALLOW should NOT activate when:
- The user explicitly asks for deep analysis
- The task involves security, safety, or financial consequences
- The decision is hard to reverse (architecture, contract, data model)
- The user has expressed confusion or uncertainty
- This is iteration N>2 on the same problem (depth may finally be warranted)

**The default should still be appropriate depth.** SHALLOW is a targeted counter to depth bias — not a replacement for sound judgment.

---

## The Deeper Purpose

The depth-skills library is optimized for depth. But cognitive investment should match consequence. SHALLOW provides the calibration: a **formal calculus** that routes low-stakes tasks to fast answers. It's not anti-thinking — it's proportional-thinking. **Now it's quantified (shallow score), certified (proportionality ), and verified (gates).** The skill exists because the library's other skills make over-analysis easy. SHALLOW makes under-analysis acceptable — when it's appropriate.

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 1. It outputs:
```json
{
  "phase": 1,
  "skill": "shallow",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: depth_budget_calculus (3.0), budget_allocation (2.0), shallow_delivery (1.0), proportionality_ (2.0)
- Total complexity weight: 8.0

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: 0
- Assumption reversals: 0
- Proportionality violations: [count if actual ADS deviates from target]

### Cognitive Traces Produced
- [x] Depth Budget Calculus
- [x] Proportionality 
- [ ] Decision Landscape

### Gates Verified
- [x] V1  [ ] V2  [ ] V3  [ ] V4  [ ] V5  [x] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From CLARIFY: Readiness  → if NOT_READY force MINIMAL
- From CONDUCTOR: Task profile → auto-populate calculus
- From THRESHOLD: Reversal cost → if Category 1 force MINIMAL