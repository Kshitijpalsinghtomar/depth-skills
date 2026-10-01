---
name: clarify
codename: CLARIFY
internal: Ask/Answer Decision Engine v2.0
version: 2.0
tier: cognition
trigger: ambiguous request, missing context, "should I ask or answer", user says "what do you need to answer this"
description: Decides whether to ask clarifying questions or proceed with an answer, optimizing for information value vs. delay cost. Now with mathematical depth metrics, question value calculus, answer readiness , and verification gates.
author: Kshitijpalsinghtomar
tags: [questions, clarification, intent, information-gathering, decision, metrics, recursion, verification]
artifacts:
  - intent-assessment
  - question-value-score
  - answer-readiness-verdict
  - clarification-calculus
    - activation-heatmap
    - phase-activation
composable_with:
  - deep-think
  - excavate
  - shallow
  - conductor
  - boundary-detector
thinking_parameters:
  min_questions: 1
  value_threshold: 3
  require_calculus: true
  require_readiness_: true
  recursion_depth: 1
---

# CLARIFY v2.0 — Ask/Answer Decision Engine (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (clarification calculus, readiness ), and verifies Gates V1, V3. It formalizes the ask/answer decision as a value calculus.

Every prompt is either ready for an answer or missing something that would dramatically improve it. You must decide: ask now, or answer now and refine later?

The wrong choice costs:
- **Asking when you could answer:** Wastes user's time, breaks flow, signals incompetence
- **Answering when you should ask:** Delivers wrong thing, requires revision cycles, erodes trust

This skill decides. **Now it quantifies the decision.**

---

## The Failure Mode You Must Recognize

You are about to either:
- Ask a question the user already answered (implicitly or in prior context)
- Answer a question that will require 3 follow-up messages to converge

Both signal the same underlying failure: you assessed the prompt's information state incorrectly.

**Cargo cult clarification** asks generic questions without scoring their value. This skill rejects it.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `min_questions` (default 1) — minimum questions to generate if asking
- `value_threshold` (default 3) — minimum total value score to ask
- `require_calculus` (default true) — compute clarification calculus
- `require_readiness_` (default true) — issue answer readiness 
- `recursion_depth` (default 1) — recursive self-audit rounds

---

### 1 — ASSESS INTENT READINESS

Write your assessment of the incoming prompt:

```
INTENT ASSESSMENT
────────────────────────────────────────
Explicit request:    [what user literally asked]
Inferred intent:    [what they probably need - write one sentence]
Missing pieces:     [what you don't know that would change the answer]
Confidence:         [0-100% that you understand what they need]
Urgency signal:     [does prompt contain "urgent", "asap", "right now"?]
Prior context:      [relevant conversation history - yes/no]
Information State:  [COMPLETE / PARTIAL / FRAGMENTED / UNKNOWN]
────────────────────────────────────────
```

**Artifact:** Intent assessment.

**CEI Component:** Intent Assessment (weight 1.0)

---

### 2 — CLARIFICATION CALCULUS (if `require_calculus` = true)

**NEW IN v2.0** — Formal value calculus for each potential question.

For each potential question, calculate its value:

```
QUESTION VALUE CALCULUS
────────────────────────────────────────
Question: [write the question]

Information Impact (II):
  If I knew the answer, how much would my response change?
    - Substantially (different approach): II = 2.0
    - Moderately (refinement): II = 1.0
    - Minimally (same answer either way): II = 0.0

User Cooperation Likelihood (UCL):
  How likely will the user answer this?
    - High (obvious gap, easy to answer): UCL = 1.0
    - Medium (reasonable to ask): UCL = 0.5
    - Low (intrusive, unclear): UCL = 0.0

Delay Cost (DC):
  What is the delay cost?
    - Low (quick answer): DC = 1.0
    - Medium (some back-and-forth): DC = 0.5
    - High (derails conversation): DC = 0.0

Prior Answer Probability (PAP):
  How likely is the user to have already answered this implicitly?
    - Low (genuinely unknown): PAP = 1.0
    - Medium (might be in context): PAP = 0.5
    - High (likely answered): PAP = 0.0

TOTAL VALUE = II × UCL × PAP + DC
  [0.0 - 3.0]

Decision Threshold: [value_threshold, default 3.0 scaled]
  If TOTAL VALUE ≥ threshold → ASK
  If TOTAL VALUE < threshold → ANSWER (with caveats if 1-2)
────────────────────────────────────────
```

**Minimum `min_questions` questions evaluated.**

**Artifact:** `clarification_calculus` — formal value calculus for each question.

**CEI Component:** Clarification Calculus (weight 3.0)

---

### 3 — DELIVER VERDICT

Write your final decision and reasoning:

```
ASK/ANSWER VERDICT
────────────────────────────────────────
Decision:          [ASK / ANSWER / ANSWER-WITH-CAVEATS]
Primary question:  [if asking - write it]
Reasoning:         [2-3 sentences why this is the right call, referencing calculus]
What happens next: [if asking - wait for response]
                     [if answering - deliver and note what I'd ask if I could]
────────────────────────────────────────
```

**Artifact:** Ask/Answer verdict.

**CEI Component:** Verdict (weight 1.0)

---

### 4 — ANSWER READINESS  (if `require_readiness_` = true)

**NEW IN v2.0** — Formal  of answer readiness.

```
ANSWER READINESS 
────────────────────────────────────────
 ID: arc_<timestamp>_<hash>
Prompt: [description]
Information State: [COMPLETE / PARTIAL / FRAGMENTED / UNKNOWN]

Questions Evaluated: [N]
Questions to Ask: [N]
Total Value Score: [0.0-3.0]
Threshold: [value_threshold]

Readiness: [READY / NOT_READY / CONDITIONAL]

If NOT_READY:
  Missing Information: [list]
  Questions to Ask: [list]
  Expected Value Gain: [value]

If CONDITIONAL:
  Caveats: [list]
  Questions to Ask if Time Permits: [list]

Validity: [date or condition]
────────────────────────────────────────
```

**Artifact:** `readiness_` — formal verification of answer readiness.

**CEI Component:** Readiness  (weight 2.0)

---

### 5 — METRICS: Compute and Output Depth Metrics

#### 5.1 Phase Activation (for ADS)

```json
{
  "phase": 1,
  "skill": "clarify",
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
    "intent_assessment": 1.0,
    "clarification_calculus": 3.0,
    "verdict": 1.0,
    "readiness_": 2.0,
    "total_complexity_weight": 7.0,
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
    "si_total": 0
  }
}
```

#### 5.4 Cognitive Traces

**Clarification Calculus:**
```json
{
  "type": "clarification_calculus",
  "questions": [
    {"question": "...", "II": 2.0, "UCL": 1.0, "DC": 1.0, "PAP": 1.0, "total": 3.0, "decision": "ASK"},
    {"question": "...", "II": 1.0, "UCL": 0.5, "DC": 0.5, "PAP": 0.5, "total": 0.625, "decision": "ANSWER"}
  ],
  "threshold": 3.0,
  "questions_to_ask": N
}
```

**Readiness :** (as defined in Step 4)

#### 5.5 Depth  Contribution

```json
{
  "skill": "clarify",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": 0, "ec": 0.XX},
  "gates_verified": {"V1": true, "V3": true},
  "limitations": ["..."]
}
```

---

### 6 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V1** | Assumption Coverage | Every missing piece in intent assessment traces to a question or caveat |
| **V3** | Opposition Authenticity | If ANSWER: calculus shows why asking would be lower value |

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
| BOUNDARY-DETECTOR | Knowledge gaps | Add as missing pieces in intent assessment |
| DEEP-THINK | Assumptions from restatement | Inform missing pieces |
| EXCAVATE | C2/C3 assumptions | Add as missing pieces |

**Provide to later skills:**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| DEEP-THINK | Missing pieces → assumption flags | +0.15 |
| EXCAVATE | Missing pieces → C2/C3 assumptions | +0.20 |
| CONDUCTOR | Readiness  → skill selection | +0.15 |
| SHALLOW | Readiness → depth budget | +0.10 |

**Artifact:** `interference_log` (received and provided).

---

## The Deeper Purpose

The model defaults to answering — it's what it's built to do. But sometimes the highest-value action is to slow down and ask. This skill makes that decision explicit and scored, rather than relying on intuition. **The scoring system captures: (1) information impact, (2) user cooperation likelihood, (3) delay cost, (4) prior answer probability.** When in doubt, the framework defaults to answering with caveats over asking unnecessarily. **Now it's a formal calculus with s.**

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 1. It outputs:
```json
{
  "phase": 1,
  "skill": "clarify",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: intent_assessment (1.0), clarification_calculus (3.0), verdict (1.0), readiness_ (2.0)
- Total complexity weight: 7.0

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: 0
- Assumption reversals: 0

### Cognitive Traces Produced
- [x] Clarification Calculus
- [x] Readiness 
- [ ] Decision Landscape

### Gates Verified
- [x] V1  [ ] V2  [x] V3  [ ] V4  [ ] V5  [ ] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From BOUNDARY-DETECTOR: Knowledge gaps → missing pieces
- From DEEP-THINK: Assumptions → missing pieces
- From EXCAVATE: C2/C3 assumptions → missing pieces