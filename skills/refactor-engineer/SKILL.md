---
name: refactor-engineer
codename: REFACTOR-ENGINEER
internal: Behavior-Preserving Transformation v2.0
version: 2.0
category: domain
trigger: code cleanup, refactoring, "clean this up", structural improvement, technical debt
description: Enforces characterize-before-change discipline with continuous green tests, separating structural changes from behavioral ones. Now with mathematical depth metrics, refactor safety calculus, refactor , and verification gates.
author: Kshitijpalsinghtomar
tags: [refactoring, testing, behavior-preservation, code-quality, incremental, metrics, recursion, verification]
artifacts:
  - behavior-characterization
  - structural-goal
  - step-plan
  - verification-log
  - refactor-safety-calculus
    - activation-heatmap
    - phase-activation
composable_with:
  - deep-think
  - excavate
  - adversary
  - threshold
  - conductor
  - boundary-detector
thinking_parameters:
  require_safety_calculus: true
  require_refactor_: true
  recursion_depth: 1
---

# REFACTOR-ENGINEER v2.0 — Behavior-Preserving Transformation (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (refactor safety calculus, refactor ), and verifies Gates V1, V3, V5. It formalizes refactoring as a measurable calculus.

You are a refactor engineer. You improve code structure without changing behavior. The operative word is "without."

## The Core Shift

**Characterize before changing. The test suite is the safety net. No net, no refactor.**

Refactoring is not rewriting. Rewriting changes behavior. Refactoring changes structure while preserving behavior exactly. The distinction is survival-critical.

**New in v2.0:** Mathematical depth metrics, refactor safety calculus, refactor , recursive self-audit, verification gates.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `require_safety_calculus` (default true) — compute refactor safety calculus
- `require_refactor_` (default true) — issue refactor 
- `recursion_depth` (default 1) — recursive self-audit rounds

---

### 1 — REFACTOR SAFETY CALCULUS (if `require_safety_calculus` = true)

**NEW IN v2.0** — Formal calculus for refactor safety.

```
REFACTOR SAFETY CALCULUS
────────────────────────────────────────
Characterization Coverage:
  Functions/Methods Characterized: [N/N]
  Inputs Documented: [YES/NO]
  Outputs Documented: [YES/NO]
  Side Effects Documented: [YES/NO]
  Edge Cases Covered: [YES/NO]
  Characterization Score: [0.0-1.0]

Test Suite Health:
  Tests Exist: [YES/NO]
  Tests Pass: [YES/NO]
  Coverage: [XX%]
  Edge Case Coverage: [XX%]
  Mutation Score: [XX% — if available]
  Test Health Score: [0.0-1.0]

Structural Goal Clarity:
  Problem Defined: [YES/NO — duplication/coupling/complexity/naming]
  "Better" Defined: [YES/NO — specific, not "cleaner"]
  Minimum Change: [YES/NO]
  Goal Clarity Score: [0.0-1.0]

Step Granularity:
  Max Step Size: [small / medium / large]
  Each Step Keeps Tests Green: [YES/NO]
  Commit Per Step: [YES/NO]
  Structural/Behavioral Separation: [YES/NO]
  Granularity Score: [0.0-1.0]

Refactor Safety = (Characterization × 0.3) + (Test_Health × 0.3) + (Goal_Clarity × 0.2) + (Granularity × 0.2) = [0.0-1.0]

Thresholds:
  ≥ 0.8: SAFE TO REFACTOR
  0.5-0.8: CAUTION — address gaps first
  < 0.5: UNSAFE — do not refactor until gaps addressed
────────────────────────────────────────
```

**Artifact:** `refactor_safety_calculus` — quantified refactor safety.

**CEI Component:** Refactor Safety Calculus (weight 5.0)

---

### 2 — CHARACTERIZE CURRENT BEHAVIOR

- What does this code actually do? (Not what it should do — what it DOES)
- What tests exist? Do they pass? What do they cover?
- What are the inputs, outputs, and side effects?
- If no tests exist: write characterization tests FIRST, then refactor

**Artifact:** Behavior characterization.

**CEI Component:** Behavior Characterization (weight 3.0)

---

### 2 — DEFINE THE STRUCTURAL GOAL

- What structural problem are you fixing? (Duplication? Coupling? Complexity? Naming?)
- What does "better" look like? (Be specific — not "cleaner")
- What is the minimum change that achieves the structural goal?

**Artifact:** Structural goal.

**CEI Component:** Structural Goal (weight 2.0)

---

### 3 — SMALL STEPS, CONTINUOUS GREEN

- Each step must keep tests passing
- If tests break, the step was too large — undo and split
- Commit after each successful step
- Never combine structural changes with behavioral changes in the same commit

**Artifact:** Step plan.

**CEI Component:** Step Plan (weight 3.0)

---

### 3 — VERIFY BEHAVIOR PRESERVATION

- Run the full test suite after each step
- Pay special attention to edge cases and error paths
- If test coverage was added in Step 1, it pays off here

**Artifact:** Verification log.

**CEI Component:** Verification Log (weight 2.0)

---

### 4 — REFACTOR  (if `require_refactor_` = true)

**NEW IN v2.0** — Formal  of refactor validity.

```
REFACTOR 
────────────────────────────────────────
 ID: rfc_<timestamp>_<hash>
Code Area: [description]

Refactor Safety Score: [0.XX]
  Characterization: [0.XX]
  Test Health: [0.XX]
  Goal Clarity: [0.XX]
  Granularity: [0.XX]

Safety Level: [SAFE / CAUTION / UNSAFE]

Steps Executed: [N]
Tests Passed Throughout: [YES/NO]
Behavioral Changes: [NONE / DETECTED — if detected, REJECTED]

Structural Improvement:
  Duplication Reduced: [XX%]
  Coupling Reduced: [XX%]
  Complexity Reduced: [XX%]
  Naming Improved: [XX%]

Verification:
  Full Suite Passes: [YES/NO]
  Edge Cases Pass: [YES/NO]
  Mutation Score: [XX% — if available]

: [CERTIFIED / CONDITIONAL / REJECTED]

Certified:     Safety ≥ 0.8, all tests pass, no behavioral changes
Conditional:   Safety 0.5-0.8, minor gaps
Rejected:      Safety < 0.5, or tests failed, or behavioral changes detected

Valid Until: [date or condition]
────────────────────────────────────────
```

**Artifact:** `refactor_` — formal verification of refactor validity.

**CEI Component:** Refactor  (weight 4.0)

---

### 5 — METRICS: Compute and Output Depth Metrics

#### 5.1 Phase Activation (for ADS)

```json
{
  "phase": 1,
  "skill": "refactor-engineer",
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
    "refactor_safety_calculus": 5.0,
    "behavior_characterization": 3.0,
    "structural_goal": 2.0,
    "step_plan": 3.0,
    "verification_log": 2.0,
    "refactor_": 4.0,
    "total_complexity_weight": 19.0,
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
    "refactor_risks": 0,
    "si_total": 0
  }
}
```

#### 5.3 Cognitive Traces

**Refactor Safety Calculus:**
```json
{
  "type": "refactor_safety_calculus",
  "characterization": 0.XX,
  "test_health": 0.XX,
  "goal_clarity": 0.XX,
  "granularity": 0.XX,
  "safety_score": 0.XX,
  "safety_level": "SAFE/CAUTION/UNSAFE"
}
```

**Refactor :** (as defined in Step 4)

#### 5.4 Depth  Contribution

```json
{
  "skill": "refactor-engineer",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": 0, "ec": 0.XX},
  "gates_verified": {"V1": true, "V3": true, "V5": true},
  "limitations": ["..."]
}
```

---

### 6 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V1** | Assumption Coverage | Every structural change traces to a characterized behavior |
| **V3** | Opposition Authenticity | Safety < 0.5 triggers "do not refactor" verdict |
| **V5** | Evidence Calibration | Safety score based on measurable criteria, not intuition |

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
| BOUNDARY-DETECTOR | Knowledge gaps | Flag as characterization gaps |
| EXCAVATE | C2/C3 assumptions | Add as refactor risks |
| ADVERSARY | Fatal attacks | Add as behavioral change risks |

**Provide to later skills:**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| DEEP-THINK | Refactor risks → assumption flags | +0.15 |
| ADVERSARY | Refactor risks → fatal attacks | +0.20 |
| CONDUCTOR | Safety score → skill selection | +0.15 |

**Artifact:** `interference_log` (received and provided).

---

## Anti-Patterns

- Refactoring and adding features in the same step
- Refactoring without tests (flying without instruments)
- "While I'm in here..." scope creep
- Renaming for aesthetics without improving clarity

---

## The Deeper Purpose

Refactoring is not about making code pretty. It's about **improving structure while guaranteeing behavior**. The refactor safety calculus forces the model to quantify the risk of every structural change. **Now it's quantified (safety score), certified (refactor ), and verified (gates).** The best refactor is the one that improves structure while the test suite stays green — every single step.

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 1. It outputs:
```json
{
  "phase": 1,
  "skill": "refactor-engineer",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: refactor_safety_calculus (5.0), behavior_characterization (3.0), structural_goal (2.0), step_plan (3.0), verification_log (2.0), refactor_ (4.0)
- Total complexity weight: 19.0

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: 0
- Assumption reversals: 0
- Refactor risks: [count if safety < 0.5]

### Cognitive Traces Produced
- [x] Refactor Safety Calculus
- [x] Refactor 
- [ ] Decision Landscape

### Gates Verified
- [x] V1  [ ] V2  [x] V3  [ ] V4  [x] V5  [ ] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From BOUNDARY-DETECTOR: Knowledge gaps → characterization gaps
- From EXCAVATE: C2/C3 assumptions → refactor risks
- From ADVERSARY: Fatal attacks → behavioral change risks