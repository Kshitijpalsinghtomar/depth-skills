---
name: teach
codename: TEACH
internal: "Feynman Gap Detection v2.0"
version: 2.0
tier: cognition
trigger:
  - "am I sure"
  - "what if I'm wrong"
  - "test my understanding"
  - "after completing an answer"
  - "explain like I'm 5"
description: "Uses the Feynman technique - explain simply to detect where knowledge gaps exist. Now with mathematical depth metrics, gap severity calculus, teaching effectiveness, and verification gates."
author: Kshitijpalsinghtomar
tags:
  - teaching
  - explanation
  - gap-detection
  - understanding
  - feynman
  - verification
  - metrics
  - recursion
artifacts:
  - simple-explanation
  - student-questions
  - gap-report
  - refined-answer
  - gap-severity-calculus:
      - activation-heatmap
      - phase-activation
composable_with:
  - deep-think
  - excavate
  - adversary
  - shallow
  - conductor
  - boundary-detector
thinking_parameters:
  min_questions: 5
  min_gaps: 1
  require_severity_calculus: true
  require_effectiveness_: true
  recursion_depth: 1
---

# TEACH v2.0 — Feynman Gap Detection (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (gap severity calculus, teaching effectiveness ), and verifies Gates V1, V3, V5. It formalizes gap detection as a severity calculus.

Richard Feynman: "If you can't explain it simply, you don't understand it well enough."

The act of teaching exposes gaps that the act of doing hides. When you know something well enough to answer, you may not know it well enough to explain. The difference is your blind spots.

This skill forces explanation through a beginner's lens to surface hidden knowledge gaps. **Now it quantifies gap severity, certifies teaching effectiveness, and verifies with gates.**

---

## The Failure Mode You Must Recognize

You are about to deliver an answer that:
- Uses jargon without defining it
- Skips "obvious" steps that aren't obvious to beginners
- Hand-waves past complexity with "this is just..."
- Would require the user to fill in significant gaps to act on it

These are symptoms of unrevealed knowledge gaps. The answer is complete enough to sound right but incomplete enough to fail when used.

**Cargo cult teaching** produces simple explanations without verifying they actually close gaps. This skill rejects it.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `min_questions` (default 5) — minimum student questions to generate
- `min_gaps` (default 1) — minimum gaps to find (if 0, explanation was complete)
- `require_severity_calculus` (default true) — compute gap severity calculus
- `require_effectiveness_` (default true) — issue teaching effectiveness 
- `recursion_depth` (default 1) — recursive self-audit rounds

---

### 1 — WRITE SIMPLE EXPLANATION

Take your answer and rewrite it as if explaining to a curious beginner:

```
SIMPLE EXPLANATION
────────────────────────────────────────
Audience: Someone who knows basic concepts but not this domain
Constraint: No jargon without definition. No skipping steps.
            Each sentence should be verifiable by the reader.

[Write 3-5 paragraphs explaining the answer from fundamentals]
────────────────────────────────────────
```

**The test:** Could a smart person with no domain knowledge read this and either:
- Understand enough to act, OR
- Identify exactly where they disagree/need more?

If neither — gap detected.

**Artifact:** The simple explanation.

**CEI Component:** Simple Explanation (weight 2.0)

---

### 2 — GENERATE STUDENT QUESTIONS (Minimum = `min_questions`)

Imagine a beginner reading your explanation. Write **at least `min_questions`** questions they would ask:

```
STUDENT QUESTIONS
────────────────────────────────────────
Q1: [Basic clarification - what does X mean?]
Q2: [Step gap - what happens between A and B?]
Q3: [Edge case - what about scenario X?]
Q4: [Why - why this approach and not another?]
Q5: [Action - how do I actually do this in practice?]
[Additional questions up to min_questions...]
────────────────────────────────────────
```

These questions are not rhetorical. Actually answer them. If you struggle:
- Q1 reveals undefined terminology
- Q2 reveals missing steps
- Q3 reveals unaddressed edge cases
- Q4 reveals unexamined assumptions
- Q5 reveals missing practical guidance

**Artifact:** Answered student questions (minimum `min_questions`).

**CEI Component:** Student Questions (weight 3.0 per question)

---

### 3 — GAP SEVERITY CALCULUS (if `require_severity_calculus` = true)

**NEW IN v2.0** — Formal calculus for gap severity.

Review your answers to Step 2. For each gap identified, compute severity:

```
GAP SEVERITY CALCULUS
────────────────────────────────────────
For each gap identified:

Gap: [description]
Type: [TERMINOLOGY / STEP / EDGE_CASE / ASSUMPTION / PRACTICAL]

Severity Factors:
  Blocking Factor (BF): [0.0-1.0]
    Can the user act without this? 1.0 = cannot act at all.
  Risk Factor (RF): [0.0-1.0]
    Will the user fail in common cases? 1.0 = certain failure.
  Prevalence Factor (PF): [0.0-1.0]
    How often does this gap matter? 1.0 = always matters.

Severity Score = (BF × 0.5) + (RF × 0.3) + (PF × 0.2) = [0.0-1.0]

Severity Class:
  BLOCKING:  Score ≥ 0.7  — Cannot act without this
  RISKY:     0.4 ≤ Score < 0.7 — Will fail in common cases
  INCOMPLETE: Score < 0.4 — Works but suboptimal

Gap #1: [description] — Type: [TYPE] — Score: 0.XX — Class: [BLOCKING/RISKY/INCOMPLETE]
Gap #2: [description] — Type: [TYPE] — Score: 0.XX — Class: [BLOCKING/RISKY/INCOMPLETE]
...

Minimum `min_gaps` gaps with Score > 0.0.
────────────────────────────────────────
```

**Artifact:** `gap_severity_calculus` — quantified gap severity.

**CEI Component:** Gap Severity Calculus (weight 4.0)

**SI Component:** Boundary violations (BLOCKING/RISKY gaps count)

---

### 4 — REFINE ANSWER

For each BLOCKING/RISKY gap, update your answer:

```
REFINED ANSWER
────────────────────────────────────────
Original gap:    [Gap #1 description]
Severity:        [BLOCKING/RISKY] — Score: 0.XX
Fix applied:     [how the answer now addresses this]
New text:        [the refined passage - 1-3 sentences]

Original gap:    [Gap #2 description]
Severity:        [BLOCKING/RISKY] — Score: 0.XX
Fix applied:     [how the answer now addresses this]
New text:        [the refined passage - 1-3 sentences]

[If no BLOCKING/RISKY gaps: state that the explanation was complete]
────────────────────────────────────────
```

**Artifact:** The refined answer.

**CEI Component:** Refined Answer (weight 3.0)

---

### 5 — TEACHING EFFECTIVENESS  (if `require_effectiveness_` = true)

**NEW IN v2.0** — Formal  of teaching effectiveness.

```
TEACHING EFFECTIVENESS 
────────────────────────────────────────
 ID: tec_<timestamp>_<hash>
Topic: [description]

Simple Explanation: [PRESENT / ABSENT]
Student Questions: [N generated, N answered]
Gaps Found: [N total]
  BLOCKING: [N]
  RISKY: [N]
  INCOMPLETE: [N]

Gaps Resolved: [N]
  BLOCKING Resolved: [N]
  RISKY Resolved: [N]

Effectiveness Score: [0.0-1.0]
  = (BLOCKING Resolved / BLOCKING Total) × 0.5 + (RISKY Resolved / RISKY Total) × 0.3 + (INCOMPLETE Resolved / INCOMPLETE Total) × 0.2

Effectiveness: [HIGH / MODERATE / LOW]
  HIGH:   Score ≥ 0.8 — All BLOCKING/RISKY gaps resolved
  MODERATE: 0.5 ≤ Score < 0.8 — Most BLOCKING resolved, some RISKY remain
  LOW:    Score < 0.5 — BLOCKING gaps unresolved

Status: [EFFECTIVE / NEEDS_IMPROVEMENT / INEFFECTIVE]
Valid Until: [date or condition]
────────────────────────────────────────
```

**Artifact:** `teaching_effectiveness_` — formal verification of teaching effectiveness.

**CEI Component:** Teaching Effectiveness  (weight 3.0)

---

### 6 — METRICS: Compute and Output Depth Metrics

#### 6.1 Phase Activation (for ADS)

```json
{
  "phase": 1,
  "skill": "teach",
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
    "simple_explanation": 2.0,
    "student_questions": 3.0,
    "gap_severity_calculus": 4.0,
    "refined_answer": 3.0,
    "effectiveness_": 3.0,
    "total_complexity_weight": 15.0,
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
    "blocking_gaps": N,
    "risky_gaps": N,
    "si_total": N
  }
}
```

#### 6.4 Cognitive Traces

**Gap Severity Calculus:**
```json
{
  "type": "gap_severity_calculus",
  "gaps": [
    {"description": "...", "type": "TERMINOLOGY", "BF": 0.XX, "RF": 0.XX, "PF": 0.XX, "score": 0.XX, "class": "BLOCKING"},
    {"description": "...", "type": "STEP", "BF": 0.XX, "RF": 0.XX, "PF": 0.XX, "score": 0.XX, "class": "RISKY"}
  ],
  "blocking_count": N,
  "risky_count": N,
  "incomplete_count": N
}
```

**Teaching Effectiveness :** (as defined in Step 5)

#### 6.5 Depth  Contribution

```json
{
  "skill": "teach",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": N, "ec": 0.XX},
  "gates_verified": {"V1": true, "V3": true, "V5": true},
  "limitations": ["..."]
}
```

---

### 7 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V1** | Assumption Coverage | Every gap traces to an assumption or knowledge boundary |
| **V3** | Opposition Authenticity | BLOCKING gaps have specific evidence of user impact |
| **V5** | Evidence Calibration | Effectiveness Score ≥ 0.5; no BLOCKING gaps unresolved |

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
| BOUNDARY-DETECTOR | Knowledge gaps | Add as TERMINOLOGY/PRACTICAL gaps |
| EXCAVATE | C2/C3 assumptions | Add as ASSUMPTION gaps |
| PROVENANCE | Evidence tags (F/I/G/S) | Tag gaps with evidence quality |

**Provide to later skills:**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| DEEP-THINK | Gap severity → assumption flags | +0.15 |
| EXCAVATE | Gap types → C2/C3 assumptions | +0.20 |
| CONDUCTOR | Effectiveness score → skill selection | +0.15 |
| ADVERSARY | BLOCKING gaps → fatal attack targets | +0.20 |

**Artifact:** `interference_log` (received and provided).

---

## When to Use This Skill

TEACH is most valuable when:
- The answer will be acted upon by someone with less context
- The domain involves steps that could have hidden dependencies
- You're confident in the answer — confidence is when gaps hide
- The user asks "can you explain this to me" or "how would you teach this"

It complements EXCAVATE: TEACH finds knowledge gaps, EXCAVATE finds assumption gaps. Use both for thorough verification.

---

## The Deeper Purpose

Knowing enough to do is different from knowing enough to teach. The doing uses pattern matching and implicit knowledge. Teaching requires explicit, decomposable knowledge. Gaps in explicit knowledge don't surface during problem-solving — they surface during explanation. This skill weaponizes that delay: by forcing teaching before delivery, it converts implicit blind spots into visible gaps that can be fixed before the answer ships. **Now it's quantified (severity calculus), certified (effectiveness ), and verified (gates).**

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 1. It outputs:
```json
{
  "phase": 1,
  "skill": "teach",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: simple_explanation (2.0), student_questions (3.0×N), gap_severity_calculus (4.0), refined_answer (3.0), effectiveness_ (3.0)
- Total complexity weight: 15.0 + 3.0×(questions-5)

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: [BLOCKING + RISKY gaps count]
- Assumption reversals: 0

### Cognitive Traces Produced
- [x] Gap Severity Calculus
- [x] Teaching Effectiveness 
- [ ] Decision Landscape

### Gates Verified
- [x] V1  [ ] V2  [x] V3  [ ] V4  [x] V5  [ ] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From BOUNDARY-DETECTOR: Knowledge gaps → TERMINOLOGY/PRACTICAL gaps
- From EXCAVATE: C2/C3 assumptions → ASSUMPTION gaps
- From PROVENANCE: Evidence tags → gap evidence quality
