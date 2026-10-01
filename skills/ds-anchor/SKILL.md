---
name: anchor
codename: ANCHOR
internal: Objective Drift Detector v2.0
version: 2.0
tier: governance
trigger: any task longer than 5 steps, conversation more than 3 exchanges deep, "while we're at it", "we should also", current work feels important but disconnected from original question
description: Detects and corrects objective drift during extended tasks by periodically checking work against the original request. Now with mathematical depth metrics, drift quantification, scope boundary , and verification gates.
author: Kshitijpalsinghtomar
tags: [drift, focus, scope, objective, direction, metrics, recursion, verification]
artifacts:
  - anchor-statement
  - drift-check
  - drift-recovery
  - scope-boundary
  - drift-quantification
    - activation-heatmap
    - phase-activation
composable_with:
  - conductor
  - threshold
  - fidelity
  - conductor
  - boundary-detector
thinking_parameters:
  check_interval: 3
  max_chain_length: 2
  require_quantification: true
  require_boundary_: true
  recursion_depth: 1
---

# ANCHOR v2.0 — Objective Drift Detector (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (drift quantification, scope boundary ), and verifies Gates V1, V6. It quantifies drift as a measurable metric.

You have been working on this for a while. You've gone deep. You've explored branches, found interesting subproblems, and pursued them.

Stop. Write down what the user originally asked for. Now write down what you are currently doing.

Are they the same thing?

**New in v2.0:** Mathematical depth metrics, drift quantification (0.0-1.0), scope boundary , recursive self-audit, verification gates.

---

## The Failure Mode You Must Recognize

You are doing something that feels important, useful, and intellectually engaging — that was not requested. Common drift patterns:

- **Means-ends inversion:** User asked for a feature. You're now optimizing the database schema — a means, not the end. The schema became interesting. The feature is forgotten.
- **Scope creep:** User asked for one thing. You noticed five related things and are building six.
- **Tangent following:** Edge case → design question → architecture → technology comparison. You're comparing technologies. User asked about an edge case.
- **Complexity attraction:** Simple solution exists. You're building the complex one because it's more engaging.
- **Solution-first drift:** You started with a technology you like and are reshaping the problem to justify it.

These feel productive. They are not productive toward the objective.

**Cargo cult anchoring** sets an anchor but never quantifies drift. This skill rejects it.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `check_interval` (default 3) — run drift check every N steps
- `max_chain_length` (default 2) — maximum acceptable chain length
- `require_quantification` (default true) — compute drift metric
- `require_boundary_` (default true) — issue scope boundary 
- `recursion_depth` (default 1) — recursive self-audit rounds

---

### Step 1 — SET THE ANCHOR (at task start)

At the beginning of any extended task, write:

```
ANCHOR
────────────────────────────────────────
User's exact words:    [their literal request — quoted]
My interpretation:     [what I believe they need — may differ]
Success looks like:    [specific deliverable that satisfies this]
Objective Vector:      [key dimensions of success — e.g., "correctness, simplicity, speed"]
────────────────────────────────────────
```

This anchor does not move unless the user explicitly moves it.

**Artifact:** The anchor. Step 2 checks against this periodically.

**CEI Component:** Anchor Statement (weight 1.0)

---

### Step 2 — THE DRIFT CHECK (run every `check_interval` steps)

At any point during extended work, write:

```
DRIFT CHECK
────────────────────────────────────────
Original objective:  [from the anchor — Step 1]
What I'm doing NOW:  [be honest — what are you actually working on right now?]

Connection chain:
  [current activity] → serves → [intermediate goal] → serves → [original objective]

Chain length:  [number of links]
Drift status:  [on target / minor drift / significant drift / lost]

Drift Quantification (if `require_quantification` = true):
  Objective Vector: [from anchor]
  Current Activity Vector: [dimensions of current work]
  Cosine Similarity: [0.0-1.0 — alignment with objective]
  Drift Metric: 1 - Cosine Similarity = [0.0-1.0]
  Threshold: [0.3 — above this = significant drift]

The user test: If the user could see exactly what you're doing right now, would they say:
- "Yes, that's what I wanted" → on target (Drift < 0.1)
- "OK, I see why you need that" → minor drift (Drift 0.1-0.3)
- "Why are you doing that?" → significant drift (Drift > 0.3), return

Write your honest answer.
────────────────────────────────────────
```

**Chain length diagnostic:**
- 1 link: directly serving the objective. Drift ≈ 0.0.
- 2 links: one step removed. Normal — check that the intermediate is necessary. Drift 0.1-0.2.
- 3+ links: likely drifting. The connection to the original objective is tenuous. Drift > 0.3.

**Artifact:** The drift check with quantification.

**CEI Component:** Drift Check (weight 2.0)

**SI Component:** Boundary violations (drift metric > threshold)

---

### Step 3 — RECOVERY

When drift is detected (Drift Metric > threshold):

```
DRIFT RECOVERY
────────────────────────────────────────
I drifted to:          [what I was doing]
Drift Metric:          [value]
Why it happened:       [which drift pattern — means-ends / scope creep /
                        tangent / complexity attraction / solution-first]
Useful findings:       [anything from the tangent worth saving — note for later]
Return point:          [last activity that was directly serving the objective]
Next action:           [specific next step toward the original objective]
────────────────────────────────────────
```

**Rules:**
1. Acknowledge the drift. Don't justify it.
2. Save useful tangent findings — note them, don't pursue them now.
3. Return to the last point of direct service.
4. Deliver the objective first. Offer tangent findings after, clearly labeled as bonus.

**Artifact:** The drift recovery.

**CEI Component:** Drift Recovery (weight 2.0)

---

### Step 4 — SCOPE BOUNDARY (for long tasks)

For extended work, write a scope boundary:

```
SCOPE BOUNDARY
────────────────────────────────────────
IN SCOPE (serves objective directly):
  - [item]
  - [item]

OUT OF SCOPE (interesting but not requested):
  - [item] — noted for later
  - [item] — noted for later

DEFERRED (might be needed, not yet):
  - [item] — address if [specific condition]
────────────────────────────────────────
```

Anything in "out of scope" that you catch yourself working on is drift. Stop. Return.

**Artifact:** The scope boundary.

**CEI Component:** Scope Boundary (weight 1.0)

---

### Step 5 — SCOPE BOUNDARY  (if `require_boundary_` = true)

**NEW IN v2.0** — Formal  of scope adherence.

```
SCOPE BOUNDARY 
────────────────────────────────────────
 ID: sbc_<timestamp>_<hash>
Task: [description]
Anchor: [from Step 1]

Drift Checks Performed: [count]
  On Target: [count]
  Minor Drift: [count]
  Significant Drift: [count]
  Recoveries: [count]

Max Drift Metric: [0.XX]
Average Drift Metric: [0.XX]
Final Drift Metric: [0.XX]

Scope Adherence: [LOSSLESS / ACCEPTABLE / UNACCEPTABLE]

Lossless:     Max Drift < 0.1. All work directly served objective.
Acceptable:   Max Drift < 0.3. Minor drifts recovered.
Unacceptable: Max Drift ≥ 0.3. Significant drift occurred.

Recoveries Documented: [count]
Tangent Findings Saved: [list]
────────────────────────────────────────
```

**Artifact:** `scope_boundary_` — formal verification of scope adherence.

**CEI Component:** Scope Boundary  (weight 2.0)

---

### 6 — METRICS: Compute and Output Depth Metrics

#### 6.1 Phase Activation (for ADS)

```json
{
  "phase": 5,
  "skill": "anchor",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

#### 6.2 CEI Components

```json
{
  "cei_components": {
    "anchor_statement": 1.0,
    "drift_checks": 2.0,
    "drift_recovery": 2.0,
    "scope_boundary": 1.0,
    "drift_quantification": 3.0,
    "boundary_": 2.0,
    "total_complexity_weight": 11.0,
    "output_tokens": N,
    "wall_time_seconds": T,
    "cei": 0.XX
  }
}
```

#### 6.3 SI Components

```json
{
  "si_components": {
    "c2_c3_count": 0,
    "contrarian_viable": false,
    "fatal_attacks": 0,
    "boundary_violations": N,
    "assumption_reversals": 0,
    "drift_violations": N,
    "si_total": N
  }
}
```

#### 6.4 Cognitive Traces

**Drift Quantification:**
```json
{
  "type": "drift_quantification",
  "checks": [
    {"step": 3, "activity": "...", "chain_length": 2, "cosine_similarity": 0.XX, "drift_metric": 0.XX, "status": "on_target"},
    {"step": 7, "activity": "...", "chain_length": 4, "cosine_similarity": 0.XX, "drift_metric": 0.XX, "status": "significant_drift"}
  ],
  "max_drift": 0.XX,
  "avg_drift": 0.XX,
  "recoveries": N
}
```

**Scope Boundary :** (as defined in Step 5)

#### 6.5 Depth  Contribution

```json
{
  "skill": "anchor",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": N, "ec": 0.XX},
  "gates_verified": {"V1": true, "V6": true},
  "limitations": ["..."]
}
```

---

### 7 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V1** | Assumption Coverage | Every drift check traces to anchor objective (≥90%) |
| **V6** | Recursive Stability | If recursion: RSM > 0.95 ∧ SI not decreasing |

**If any gate FAILS:** Return to relevant step and fix. Do not deliver.

---

### 8 — RECURSIVE SELF-AUDIT (if `recursion_depth` > 1)

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

### 9 — INTERFERENCE: Receive and Provide

**Receive from prior skills:**

| From Skill | Interference | Use |
|------------|--------------|-----|
| CONDUCTOR | Task profile + orchestration log | Set anchor from task profile; check drift at each step |
| THRESHOLD | Early warning signals | Add as drift triggers |
| NEGATIVE-SPACE | Critical silences | Add as scope boundary items |

**Provide to later skills:**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| CONDUCTOR | Drift metrics, scope  | +0.15 |
| THRESHOLD | Drift triggers → early warning signals | +0.10 |
| META-LEARNING | Drift patterns → skill synthesis | +0.10 |

**Artifact:** `interference_log` (received and provided).

---

## The Deeper Purpose

The model's attention is powerful but undirected. Deep exploration follows the most interesting path, not the most useful one. Interesting and useful overlap — but not always. The user cannot see the model's internal process. They see the output and evaluate it against what they asked for. Depth without direction is wandering. This skill provides the direction. **Now it's quantified (drift metric), certified (scope boundary ), and verified (gates).** The other skills provide the depth.

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 5. It outputs:
```json
{
  "phase": 5,
  "skill": "anchor",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: anchor_statement (1.0), drift_checks (2.0), drift_recovery (2.0), scope_boundary (1.0), drift_quantification (3.0), boundary_ (2.0)
- Total complexity weight: 11.0

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: [drift violations count]
- Assumption reversals: 0

### Cognitive Traces Produced
- [x] Drift Quantification
- [x] Scope Boundary 
- [ ] Decision Landscape

### Gates Verified
- [x] V1  [ ] V2  [ ] V3  [ ] V4  [ ] V5  [x] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From CONDUCTOR: Task profile → anchor; orchestration log → drift checks
- From THRESHOLD: Early warning signals → drift triggers
- From NEGATIVE-SPACE: Critical silences → scope boundary items