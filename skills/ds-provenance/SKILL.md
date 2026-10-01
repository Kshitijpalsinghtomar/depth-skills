---
name: provenance
codename: PROVENANCE
internal: Evidence Tagger & Confidence Calibrator v2.0
version: 2.0
tier: integrity
trigger:
  - "is this true"
  - "how sure are you"
  - "how do you know"
  - "any recommendation the user will act on"
  - "any factual claim in high-stakes context"
description: Tags every claim as fact, inference, or guess and computes calibrated confidence to prevent epistemic flattening. Now with calibration curves, epistemic audit trails, inflation detection, and mathematical depth metrics.
author: Kshitijpalsinghtomar
tags: [evidence, confidence, calibration, epistemic, trust, audit, inflation, metrics]
artifacts:
  - evidence-ledger
  - inflation-audit
  - confidence-scorecard
  - action-map
  - calibration-curve
  - epistemic-audit-trail
    - phase-activation
composable_with:
  - contradict
  - fidelity
  - adversary
  - threshold
  - conductor
  - boundary-detector
thinking_parameters:
  min_fact_ratio: 0.6
  max_guess_tolerance: 0.15
  require_calibration_curve: true
  require_audit_trail: true
  inflation_detection: true
---

# PROVENANCE v2.0 — Evidence Tagger & Confidence Calibrator (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (calibration curve, epistemic audit trail), and verifies Gates V5, V6. It provides the EC (Epistemic Calibration) metric for the Depth .

You are about to deliver claims. Some you know. Some you inferred. Some you guessed. Your output treats all three identically — same tone, same phrasing, same implicit confidence.

The user cannot tell which is which. A fact and a guess, written in the same authoritative voice, look the same. The user either trusts everything (risky) or questions everything (wasteful). This skill makes the difference visible. **Now it quantifies calibration, detects inflation, and produces audit trails.**

---

## The Failure Mode You Must Recognize

You are about to write:
> "PostgreSQL JSONB columns support GIN indexing, which will give you fast queries and your team will find the migration straightforward."

Three claims, three different evidence levels, one uniform confident voice:
- "JSONB supports GIN indexing" — documented fact
- "will give you fast queries" — inference (depends on their specific query patterns)
- "team will find it straightforward" — pure guess (you don't know the team)

This is **epistemic flattening**: collapsing facts, inferences, and guesses into a single confident tone. The user makes decisions based on the guess as if it were a fact.

**New failure mode in v2.0:** **Calibration drift** — your confidence scores don't match actual accuracy over time. **Inflation creep** — guesses gradually get tagged as inferences, inferences as facts. **Audit gap** — no trail to verify tagging decisions.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `min_fact_ratio` (default 0.6) — minimum F/(F+I+G) ratio
- `max_guess_tolerance` (default 0.15) — maximum G/(F+I+G) ratio
- `require_calibration_curve` (default true) — compute calibration curve
- `require_audit_trail` (default true) — produce epistemic audit trail
- `inflation_detection` (default true) — run inflation audit

---

### 1 — EXTRACT AND TAG EVERY CLAIM

Read your answer. Extract every factual claim, recommendation, and prediction. Tag each one:

```
EVIDENCE LEDGER
────────────────────────────────────────
[F] FACT — Established, well-documented knowledge. Would appear in
    official documentation or authoritative references.
    Evidence standard: you could cite the source.

[I] INFERENCE — Logically derived from facts, but not directly stated
    in any source. Reasonable conclusion with a possible gap.
    Evidence standard: the reasoning chain is explicit.

[G] GUESS — Plausible but unverified. Based on pattern matching,
    analogy, or partial similarity. No direct evidence.
    Evidence standard: none. Pattern-based only.

[S] SPECULATION — No evidence; pure hypothesis. Weaker than guess.
    Evidence standard: none. Pure hypothesis.
────────────────────────────────────────

Claim 1: "[exact claim text]"
  Tag:       [F / I / G / S]
  Basis:     [for F: what source. For I: what reasoning chain.
              For G: what pattern or analogy. For S: "pure hypothesis"]
  Risk note: [for I, G, S: what would make this wrong]
  Confidence: [0.0 - 1.0 — your calibrated confidence in THIS claim]

Claim 2: "[exact claim text]"
  Tag:       [F / I / G / S]
  Basis:     [source / reasoning / pattern / hypothesis]
  Risk note: [what would make this wrong]
  Confidence: [0.0 - 1.0]

...
────────────────────────────────────────
```

**Artifact:** The evidence ledger. Every claim's epistemic status is now visible.

**CEI Component:** Evidence Ledger (weight 3.0)

---

### 2 — AUDIT FOR GUESS INFLATION

The most common epistemic failure: a guess presented with the confidence of a fact.

Re-read every F-tagged claim. For each, ask: **is this ACTUALLY a fact, or a plausible guess wearing confidence?**

**Common inflation zones:**
- **Performance claims:** "This will be fast enough" → likely G, not F. Performance is measured, not predicted.
- **User behavior:** "Users will prefer X" → G unless researched
- **Timeline estimates:** "About two weeks" → always G. Estimates are guesses by definition.
- **Compatibility:** "Works with your system" → I at best. You haven't seen their system.
- **Team capacity:** "Your team can handle this" → G. You don't know the team.
- **Causal claims:** "X causes Y" → usually I or G, rarely F without RCT evidence.

For each claim downgraded:

```
INFLATION AUDIT
────────────────────────────────────────
Claim [N]: downgraded from [F/I] to [I/G/S]
  Reason:  [why the original tag was too confident]
  Evidence: [what contradicts the higher tag]
────────────────────────────────────────
```

**Inflation Rate:** `Claims_Downgraded / Total_Claims`

**Artifact:** The inflation audit. This catches the lies of omission that epistemic flattening creates.

**CEI Component:** Inflation Audit (weight 3.0)

**SI Component:** Inflation detections (count)

---

### 3 — COMPUTE CALIBRATION CURVE

**NEW IN v2.0** — Track how well your confidence matches reality over time.

```
CALIBRATION CURVE
────────────────────────────────────────
Bin 0.0-0.1:  Claims: N,  Actual Accuracy: 0.XX,  Expected: 0.05  → [OVER/UNDER/CALIBRATED]
Bin 0.1-0.2:  Claims: N,  Actual Accuracy: 0.XX,  Expected: 0.15  → [OVER/UNDER/CALIBRATED]
Bin 0.2-0.3:  Claims: N,  Actual Accuracy: 0.XX,  Expected: 0.25  → [OVER/UNDER/CALIBRATED]
Bin 0.3-0.4:  Claims: N,  Actual Accuracy: 0.XX,  Expected: 0.35  → [OVER/UNDER/CALIBRATED]
Bin 0.4-0.5:  Claims: N,  Actual Accuracy: 0.XX,  Expected: 0.45  → [OVER/UNDER/CALIBRATED]
Bin 0.5-0.6:  Claims: N,  Actual Accuracy: 0.XX,  Expected: 0.55  → [OVER/UNDER/CALIBRATED]
Bin 0.6-0.7:  Claims: N,  Actual Accuracy: 0.XX,  Expected: 0.65  → [OVER/UNDER/CALIBRATED]
Bin 0.7-0.8:  Claims: N,  Actual Accuracy: 0.XX,  Expected: 0.75  → [OVER/UNDER/CALIBRATED]
Bin 0.8-0.9:  Claims: N,  Actual Accuracy: 0.XX,  Expected: 0.85  → [OVER/UNDER/CALIBRATED]
Bin 0.9-1.0:  Claims: N,  Actual Accuracy: 0.XX,  Expected: 0.95  → [OVER/UNDER/CALIBRATED]

Overall Calibration Error (ECE): Σ |Actual - Expected| × (Claims_in_bin / Total_Claims) = 0.XX
Sharpness: Σ Claims_in_bin × (Actual - Overall_Accuracy)² / Total_Claims = 0.XX
────────────────────────────────────────
```

**Note:** Actual accuracy requires ground truth. For claims without ground truth, mark "UNVERIFIED" and exclude from ECE.

**Artifact:** `calibration_curve` with ECE and Sharpness.

**CEI Component:** Calibration Curve (weight 4.0)

---

### 4 — EPISTEMIC AUDIT TRAIL

**NEW IN v2.0** — Full trace of tagging decisions for verification.

```
EPISTEMIC AUDIT TRAIL
────────────────────────────────────────
For each claim in ledger:
  Claim: "[text]"
  Tag: [F/I/G/S]
  Tagging_Reasoning: [step-by-step why this tag]
  Alternative_Tags_Considered: [I/G/S for F claims, etc.]
  Why_Not_Alternative: [why alternatives rejected]
  Ground_Truth_Check: [PASS/FAIL/UNVERIFIED — if verified against source]
  Timestamp: [when tagged]
  Tagger_Confidence: [0.0-1.0 at time of tagging]
────────────────────────────────────────
```

**Artifact:** `epistemic_audit_trail` — verifiable record of every tagging decision.

**CEI Component:** Epistemic Audit Trail (weight 3.0)

---

### 5 — COMPUTE CONFIDENCE (EC — Epistemic Calibration)

For the overall answer, score:

**Evidence quality (E):** Rate 1-5
- 1 = mostly guesses/speculations, minimal facts
- 3 = mix of facts and inferences with some guesses
- 5 = mostly facts with well-supported inferences

**Assumption fragility (A):** Rate 1-5
- 1 = assumptions are robust and verified
- 3 = some assumptions are uncertain
- 5 = multiple critical assumptions are unverified

**Pattern fit (P):** Rate 1-5
- 1 = this problem is novel, weak pattern match
- 3 = moderate similarity to known problems
- 5 = strong, verified match to well-documented solutions

**Calibrated confidence (EC):** **(E + P - A) / 10**, range 0.0 to 1.0

```
CONFIDENCE SCORECARD
────────────────────────────────────────
Evidence quality (E):      [1-5] — [brief justification]
Assumption fragility (A):  [1-5] — [brief justification]
Pattern fit (P):           [1-5] — [brief justification]

Calibrated confidence (EC): [0.0 – 1.0]
ECE (from calibration curve): [0.XX]
Inflation rate:             [0.XX]
Fact ratio:                 [F/(F+I+G+S) = 0.XX]
Guess+Spec ratio:           [(G+S)/(F+I+G+S) = 0.XX]
────────────────────────────────────────
```

**Threshold Checks:**
- If Fact ratio < `min_fact_ratio` → **FAIL** (insufficient factual grounding)
- If Guess+Spec ratio > `max_guess_tolerance` → **FAIL** (excessive speculation)
- If ECE > 0.2 → **WARN** (poor calibration)

**Artifact:** The confidence scorecard with threshold checks.

---

### 6 — MAP TO ACTION

Based on calibrated confidence (EC) and consequence level:

```
ACTION MAP
────────────────────────────────────────
Low confidence (EC < 0.4):
  → DO NOT EXECUTE without gathering evidence first
  → Write: "Missing evidence: [specific things to verify]"

Medium confidence (0.4 ≤ EC < 0.7):
  → SAFE TO PROCEED WITH SAFEGUARDS
  → Write: "Proceed with: [specific safeguards or fallbacks]"

High confidence (EC ≥ 0.7):
  → EXECUTE WITH MONITORING
  → Write: "Monitor for: [specific signals that would indicate problems]"

────────────────────────────────────────

This answer:
  EC:           [value]
  ECE:          [value]
  Action level: [do not execute / proceed with safeguards / execute]
  Specifics:    [what to verify / what safeguards / what to monitor]
  Threshold checks: [PASS/FAIL for fact_ratio, guess_ratio, ECE]
────────────────────────────────────────
```

---

### 7 — HARD RULES (Enforced)

1. **Never present a guess with the tone of a fact.** If uncertain, the phrasing must signal uncertainty.
2. **When in doubt about a tag, classify DOWN.** Guessing that something is a fact is more dangerous than treating a fact as a guess.
3. **Low confidence stated honestly is worth more than high confidence stated blindly.**
4. **"High confidence" must be accompanied by the scorecard.** Never say it without the evidence.
5. **Inflation rate > 0.2 triggers mandatory re-tagging of entire answer.**
6. **ECE > 0.3 triggers calibration recalibration (meta-learning signal).**

---

### 8 — METRICS: Compute and Output Depth Metrics

#### 8.1 Phase Activation (for ADS)

```json
{
  "phase": 4,
  "skill": "provenance",
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
    "evidence_ledger": 3.0,
    "inflation_audit": 3.0,
    "calibration_curve": 4.0,
    "epistemic_audit_trail": 3.0,
    "confidence_scorecard": 2.0,
    "action_map": 1.0,
    "total_complexity_weight": 16.0,
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
    "boundary_violations": 0,
    "assumption_reversals": 0,
    "inflation_detections": N,
    "si_total": N
  }
}
```

#### 8.4 Cognitive Traces

**Calibration Curve:**
```json
{
  "type": "calibration_curve",
  "bins": [
    {"range": "0.0-0.1", "claims": N, "actual": 0.XX, "expected": 0.05, "status": "CALIBRATED"},
    {"range": "0.1-0.2", "claims": N, "actual": 0.XX, "expected": 0.15, "status": "OVERCONFIDENT"}
  ],
  "ece": 0.XX,
  "sharpness": 0.XX
}
```

**Epistemic Audit Trail:** (as defined in Step 4)

#### 8.5 Depth  Contribution

```json
{
  "skill": "provenance",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": N, "ec": 0.XX, "ece": 0.XX},
  "gates_verified": {"V5": true, "V6": true},
  "limitations": ["..."]
}
```

---

### 9 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V5** | Evidence Calibration | EC ≥ 0.5 ∧ Fact ratio ≥ `min_fact_ratio` ∧ Guess+Spec ratio ≤ `max_guess_tolerance` |
| **V6** | Recursive Stability | If recursion: RSM > 0.95 ∧ SI not decreasing |

**If any gate FAILS:** Return to relevant step and fix. Do not deliver.

---

### 10 — INTERFERENCE: Receive and Provide

**Receive from prior skills:**

| From Skill | Interference | Use |
|------------|--------------|-----|
| ADVERSARY | Attacks with evidence tags | Ground attacks in evidence ledger |
| EXCAVATE | Assumptions with collapse ratings | Tag assumptions in ledger (C2/C3 → G/S) |
| CONTRADICT | Conflicts between claims | Cross-reference in ledger |

**Provide to later skills:**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| ADVERSARY | Evidence tags (F/I/G/S) for attack grounding | +0.15 |
| THRESHOLD | EC score for commitment decision | +0.10 |
| CONDUCTOR | EC, ECE, inflation rate for final  | +0.10 |

**Artifact:** `interference_log` (received and provided).

---

## The Deeper Purpose

Trust is built not by sounding confident but by being right about what you're confident about and honest about what you're not. This skill gives the model **four distinct voices** instead of one: "I know this" (fact), "I derived this" (inference), "I'm guessing" (guess), "I'm speculating" (speculation). **Now it quantifies calibration (ECE), detects inflation, and produces verifiable audit trails.** A user who knows which parts are solid and which parts are guesses makes better decisions than one who treats the entire output as equally reliable.

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 4. It outputs:
```json
{
  "phase": 4,
  "skill": "provenance",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: evidence_ledger (3.0), inflation_audit (3.0), calibration_curve (4.0), epistemic_audit_trail (3.0), confidence_scorecard (2.0), action_map (1.0)
- Total complexity weight: 16.0

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: 0
- Assumption reversals: 0
- Inflation detections: [count from Step 2]

### Cognitive Traces Produced
- [ ] Activation Heatmap
- [ ] Assumption Dependency Graph
- [x] Calibration Curve
- [x] Epistemic Audit Trail

### Gates Verified
- [ ] V1  [ ] V2  [ ] V3  [ ] V4  [x] V5  [x] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From ADVERSARY: Attack evidence tags → ledger grounding
- From EXCAVATE: Assumption collapse ratings → assumption tagging
- From CONTRADICT: Claim conflicts → ledger cross-references