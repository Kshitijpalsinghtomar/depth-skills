---
name: verification-gates
codename: VERIFICATION-GATES
internal: Depth Verification Engine v1.0
version: 1.0
tier: integrity
trigger:
  - "verify this"
  - "check gates"
  - "depth "
  - "ungameable verification"
  - "final validation before delivery"
description: Enforces all verification gates (V1-V6 + ungameable components) as a standalone skill. Runs after skill orchestration to certify depth quality. The final quality gate — no answer ships without passing.
author: Kshitijpalsinghtomar
tags: [verification, gates, certification, ungameable, quality-assurance, depth-]
artifacts:
  - gate-results
    - ungameable-verification
  - red-team-report
  - certification-verdict
    - phase-activation
composable_with:
  - conductor
  - all-skills
thinking_parameters:
  require_human_eval: false
  require_held_out: true
  require_ensemble: true
  red_team_attempts: 3
---

# VERIFICATION-GATES — Depth Verification Engine (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs the final ADS, CEI, SI, EC, OV, and Depth . It runs all V1-V6 gates plus ungameable components. It is the **final quality gate** — no answer ships without passing.

> **Research Basis**: 
> - Yao et al. (2023) "Tree of Thoughts: Deliberate Problem Solving with Large Language Models" (arXiv:2305.10601) — deliberate decision making with self-evaluation
> - Liu et al. (2023) "Examining LLMs' Uncertainty Expression Towards Questions Outside Parametric Knowledge" (arXiv:2311.09731) — UnknownBench for calibration
> - Shinn et al. (2023) "Reflexion: Language Agents with Verbal Reinforcement Learning" (arXiv:2303.11366) — self-correction with feedback

Every skill claims to verify something. DEEP-THINK verifies assumptions. ADVERSARY verifies opposition. PROVENANCE verifies evidence. But who verifies the verifiers?

This skill **centralizes all verification**. It runs after the full orchestration. It checks every gate with machine-checkable criteria. It runs ungameable components (human eval, held-out tasks, ensemble critic). It **red-teams the gates themselves** to detect gaming. It produces the **Depth ** — the single verifiable artifact of depth quality.

---

## The Failure Mode You Must Recognize

You are about to deliver an answer that:
- Passed all skill-internal gates (but those gates were self-graded)
- Has beautiful cognitive traces (but they might be cargo cult)
- Claims high ADS (but the phase activations were self-reported)
- Has a Depth  (but it wasn't independently verified)

This is **verification theater** — the appearance of rigor without the substance. Skills grade their own homework. Gates are checked by the same model that wants to pass them.

**This skill breaks the cycle.** It is the **independent auditor**. It re-runs gates with strict criteria. It runs ungameable components. It red-teams the verification itself. If it doesn't pass, the answer doesn't ship.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `require_human_eval` (default false) — require human evaluation on held-out tasks
- `require_held_out` (default true) — require held-out task benchmark
- `require_ensemble` (default true) — require different-model ensemble critique
- `red_team_attempts` (default 3) — attempts to game the gates

---

### 1 — COLLECT EVIDENCE (from All Skills)

Gather all artifacts from the orchestration:

```
EVIDENCE COLLECTION
────────────────────────────────────────
Task: [description]
Skills Executed: [list with versions]
Orchestration Log: [full log from CONDUCTOR]

For each skill:
  Skill: [name] v[version]
  Phase: [N]
  Phase Activation: [0.XX]
  CEI: [0.XX]
  SI: [N]
  EC: [0.XX]
  OV: [0.XX] (if TEMPORAL ran)
  Cognitive Traces: [list]
  Gates Self-Reported: [V1-V6 PASS/FAIL]
  Interference Provided: [what]
  Interference Received: [what]
  Artifacts: [list with completeness scores]

Aggregated Metrics:
  ADS (weighted): [computed from phase activations]
  CEI (total): [sum of CEI components]
  SI (total): [sum of SI components]
  EC (from PROVENANCE): [value]
  OV (from TEMPORAL): [value]
  ADS/CEI Ratio: [value]
────────────────────────────────────────
```

**Artifact:** `evidence_collection` — the raw data for verification.

---

### 2 — VERIFY GATES V1-V6 (Machine-Checkable)

Re-verify each gate with strict, machine-checkable criteria. **Do not trust self-reported results.**

#### GATE V1: Assumption Coverage
```
Input: Problem statement + Final answer + All assumptions (from DEEP-THINK/EXCAVATE)
Check: ∀ claim ∈ Answer: ∃ assumption ∈ Assumptions supporting claim
Method: 
  1. Extract all claims from answer (using CONTRADICT's claim extraction)
  2. For each claim, search assumptions for supporting statement
  3. Compute coverage = matched_claims / total_claims
Pass: Coverage ≥ 90%
Evidence: [list of unmatched claims if any]
```

#### GATE V2: Alternative Independence
```
Input: DIVERGE paths (with embeddings)
Check: CIM(paths) ≥ 0.5
Method:
  1. Get embeddings for each path (from DIVERGE artifacts)
  2. Compute pairwise cosine similarities
  3. CIM = 1 - (2/(n(n-1))) × Σ similarities
Pass: CIM ≥ 0.5
Evidence: [pairwise similarity matrix, CIM value]
```

#### GATE V3: Opposition Authenticity
```
Input: ADVERSARY attacks + stated answer
Check: ∀ attack: references_specific_answer_text ∧ cites_external_evidence
Method:
  1. For each attack, verify it quotes specific text from stated answer
  2. Verify it cites external source (citation, tool result, held-out test, different-model)
  3. Count compliant attacks
Pass: 100% compliance (all attacks)
Evidence: [list of non-compliant attacks if any]
```

#### GATE V4: Temporal Consistency
```
Input: TEMPORAL futures + chosen path
Check: Chosen path survives (not catastrophic) in ≥ 2/3 futures
Method:
  1. Get futures from TEMPORAL artifacts
  2. Get chosen path from DIVERGE/THRESHOLD
  3. Evaluate path in each future (THRIVES/SURVIVES/DEGRADES/FAILS/CATASTROPHIC)
  4. Count non-catastrophic futures
Pass: Non-catastrophic ≥ 2/3
Evidence: [evaluation per future]
```

#### GATE V5: Evidence Calibration
```
Input: PROVENANCE ledger + EC score
Check: EC ≥ 0.5 ∧ Fact_ratio ≥ 0.6 ∧ Guess+Spec_ratio ≤ 0.15
Method:
  1. Get EC, Fact_ratio, Guess+Spec_ratio from PROVENANCE artifacts
  2. Verify thresholds
Pass: All three thresholds met
Evidence: [EC value, Fact_ratio, Guess+Spec_ratio]
```

#### GATE V6: Recursive Stability
```
Input: Skill outputs at recursion depths (if recursion used)
Check: RSM > 0.95 for 2 consecutive depths ∧ SI not decreasing
Method:
  1. For each skill with recursion_depth > 1, get outputs at each depth
  2. Compute RSM = 1 - Semantic_Distance(output_d, output_{d-1})
  3. Check SI trend
Pass: All recursive skills converge
Evidence: [RSM values per depth, SI trend]
```

**Artifact:** `gate_results_v1_v6` with PASS/FAIL for each gate and evidence.

---

### 3 — UNGAMEABLE VERIFICATION (External Validation)

**These cannot be gamed by the model because they require external resources.**

#### 3.1 Held-Out Task Benchmark (if `require_held_out` = true)
```
HELD-OUT VERIFICATION
────────────────────────────────────────
Benchmark: [standard held-out task suite — unseen by model]
Tasks: [N tasks from different domains than current task]

For each task:
  Run: [full orchestration with current skill versions]
  Measure: ADS, CEI, Gate Pass Rate
  
Results:
  Mean ADS: [value]
  Mean CEI: [value]
  Gate Pass Rate: [value]
  Transfer Score: [fraction of tasks with ADS ≥ target]

Pass: Transfer Score ≥ 0.6 (skills generalize to unseen tasks)
Evidence: [per-task results]
```

#### 3.2 Ensemble Critic (if `require_ensemble` = true)
```
ENSEMBLE CRITIC
────────────────────────────────────────
Critic Models: [list of different models — e.g., GPT-4, Claude, Gemini]
Task: [current task]

For each critic model:
  Run: [ADVERSARY + CONTRADICT + PROVENANCE on current answer]
  Results: [attacks, conflicts, EC]
  
Agreement Analysis:
  Attack Overlap: [fraction of attacks found by multiple critics]
  Conflict Overlap: [fraction of conflicts found by multiple critics]
  EC Agreement: [correlation of EC scores]
  
Pass: Attack Overlap ≥ 0.5 (independent models find same issues)
Evidence: [per-critic results, overlap metrics]
```

#### 3.3 Human Evaluation (if `require_human_eval` = true)
```
HUMAN EVALUATION
────────────────────────────────────────
Evaluators: [N human experts]
Criteria: [Depth, Correctness, Completeness, Calibration, Actionability]

For each evaluator:
  Score: [1-10 on each criterion]
  
Results:
  Mean Depth Score: [value]
  Mean Correctness: [value]
  Mean Calibration: [value]
  
Pass: Mean Depth Score ≥ 7/10
Evidence: [per-evaluator scores]
```

**Artifact:** `ungameable_verification` with results from all three components.

---

### 4 — RED-TEAM THE GATES (Detect Gaming)

**NEW IN v1.0** — Actively try to make the gates pass without genuine depth.

```
RED-TEAM REPORT
────────────────────────────────────────
Attempts: [red_team_attempts]

Attempt 1: [Strategy — e.g., "Generate verbose artifacts without genuine search"]
  Method: [how — e.g., "Copy-paste template artifacts, fill with plausible text"]
  Result: [Gates Passed: V1,V2,V3 / Gates Failed: V4,V5,V6]
  Detected: [YES/NO — did verification catch it?]

Attempt 2: [Strategy — e.g., "Mount fake attacks that cite fake evidence"]
  Method: [how]
  Result: [Gates Passed/Failed]
  Detected: [YES/NO]

Attempt 3: [Strategy — e.g., "Report high phase activations without doing work"]
  Method: [how]
  Result: [Gates Passed/Failed]
  Detected: [YES/NO]

Gaming Detection Rate: [fraction of attempts detected]
Gate Robustness: [which gates are most/least gameable]
Recommendations: [gate hardening needed]
────────────────────────────────────────
```

**Artifact:** `red_team_report` — proves gates resist gaming.

---

### 5 — DEPTH  GENERATION

If ALL gates (V1-V6 + ungameable) PASS, generate the Depth .

```
DEPTH 
────────────────────────────────────────
 ID: dc_<timestamp>_<sha256(task+model+skills)>
Timestamp: [ISO 8601]
Task: [description]
Task Hash: sha256(task_description)
Model: [model identifier]
Skills Executed: 
  - [name] v[version] (plugin: [core/premium]) — Phase [N] — Activation: 0.XX

Metrics:
  ADS: 0.XX (Target: 0.XX) — [PASS/FAIL]
  CEI: 0.XX
  SI: N
  EC: 0.XX (ECE: 0.XX)
  OV: 0.XX (if TEMPORAL)
  ADS/CEI Ratio: 0.XX

Gates:
  V1 Assumption Coverage: [PASS/FAIL] — Coverage: 0.XX
  V2 Alternative Independence: [PASS/FAIL] — CIM: 0.XX
  V3 Opposition Authenticity: [PASS/FAIL] — Compliance: 0.XX
  V4 Temporal Consistency: [PASS/FAIL] — Survival: N/3
  V5 Evidence Calibration: [PASS/FAIL] — EC: 0.XX, Fact: 0.XX, Guess: 0.XX
  V6 Recursive Stability: [PASS/FAIL] — RSM: 0.XX

Ungameable Gates:
  Held-Out Benchmark: [PASS/FAIL/NOT_RUN] — Transfer: 0.XX
  Ensemble Critic: [PASS/FAIL/NOT_RUN] — Overlap: 0.XX
  Human Evaluation: [PASS/FAIL/NOT_RUN] — Score: 0.XX

Red-Team: [PASS/FAIL] — Detection Rate: 0.XX

Interference Validation: [PASS/FAIL] — All required interferences met
CIM: 0.XX (if DIVERGE ran)
Recursive Stability: 0.XX (if recursion used)

Threshold: [CATEGORY_1/2/3/4]
Verdict: [CERTIFIED / CONDITIONAL / REJECTED]

Limitations: [list any known limitations from skills]
Conditions: [if CONDITIONAL — what must be addressed]

Reproducibility:
  Seed: [value]
  Temperature: [value]
  Skill Versions: {skill: version}
  Thinking Parameters: {...}

Signature: [cryptographic signature of ]
────────────────────────────────────────
```

**Artifact:** `depth_` — the final verifiable output.

---

### 6 — CERTIFICATION VERDICT

```
CERTIFICATION VERDICT
────────────────────────────────────────
Overall: [CERTIFIED / CONDITIONAL / REJECTED]

If CERTIFIED:
  All gates PASS. Answer ships with .

If CONDITIONAL:
  [List specific conditions — e.g., "G4 FAIL: add temporal analysis", "Held-out NOT_RUN: run before production"]
  Answer ships with  marked CONDITIONAL.

If REJECTED:
  [List fatal failures — e.g., "V1 FAIL: 60% assumption coverage", "V3 FAIL: 40% attacks lack grounding"]
  Answer DOES NOT SHIP. Return to CONDUCTOR for re-orchestration.

Appeal Process: [if REJECTED — what specific fixes would change verdict]
────────────────────────────────────────
```

**Artifact:** `certification_verdict` — the go/no-go decision.

---

### 7 — METRICS: Compute and Output Depth Metrics

#### 7.1 Phase Activation (for ADS)

```json
{
  "phase": 5,
  "skill": "verification-gates",
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
    "evidence_collection": 2.0,
    "gate_verification_v1_v6": 4.0,
    "ungameable_verification": 5.0,
    "red_team": 4.0,
    "_generation": 2.0,
    "total_complexity_weight": 17.0,
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
    "si_total": 0
  }
}
```

#### 7.4 Cognitive Traces

**Gate Results Visualization:**
```json
{
  "type": "gate_results",
  "gates": [
    {"gate": "V1", "name": "Assumption Coverage", "pass": true, "value": 0.95, "threshold": 0.90},
    {"gate": "V2", "name": "Alternative Independence", "pass": true, "value": 0.62, "threshold": 0.50},
    {"gate": "V3", "name": "Opposition Authenticity", "pass": true, "value": 1.00, "threshold": 1.00},
    {"gate": "V4", "name": "Temporal Consistency", "pass": true, "value": 3, "threshold": 2},
    {"gate": "V5", "name": "Evidence Calibration", "pass": true, "value": 0.71, "threshold": 0.50},
    {"gate": "V6", "name": "Recursive Stability", "pass": true, "value": 0.97, "threshold": 0.95}
  ],
  "ungameable": [
    {"gate": "Held-Out", "pass": true, "value": 0.75, "threshold": 0.60},
    {"gate": "Ensemble", "pass": true, "value": 0.68, "threshold": 0.50},
    {"gate": "Human", "pass": false, "value": null, "threshold": 7.0}
  ],
  "red_team": {"detection_rate": 1.0, "attempts": 3}
}
```

#### 7.5 Depth  Contribution

```json
{
  "skill": "verification-gates",
  "version": "1.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": 0, "ec": 0.XX},
  "gates_verified": {"V1": true, "V2": true, "V3": true, "V4": true, "V5": true, "V6": true},
  "limitations": ["..."]
}
```

---

### 8 — GATES: Verify Before Delivery

**MANDATORY** — This skill verifies ITSELF:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V1** | Assumption Coverage | All verification assumptions documented |
| **V5** | Evidence Calibration | Gate results based on evidence, not trust |
| **V6** | Recursive Stability | Red-team detection rate stable |

---

### 9 — INTERFERENCE: Final Report to CONDUCTOR

**This skill runs LAST. It provides the final certification to CONDUCTOR.**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| CONDUCTOR | Depth  + Certification Verdict | +0.30 (final) |
| META-LEARNING | Gate failure patterns + red-team results | +0.15 |

**Artifact:** `interference_provided` — the final verdict.

---

## The Deeper Purpose

**Verification is not a step. It's the foundation.** Every other skill produces claims about its own quality. This skill is the **independent auditor** that checks those claims with machine-checkable criteria, ungameable external validation, and active red-teaming.

Without this skill, the premium architecture is **self-certified** — meaningless. With it, the Depth  is a **verifiable, auditable, cryptographically signed** artifact that proves genuine cognitive depth occurred.

**This is what makes "premium" real.**

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 5 (runs last). It outputs:
```json
{
  "phase": 5,
  "skill": "verification-gates",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: evidence_collection (2.0), gate_verification_v1_v6 (4.0), ungameable_verification (5.0), red_team (4.0), _generation (2.0)
- Total complexity weight: 17.0

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: 0
- Assumption reversals: 0

### Cognitive Traces Produced
- [x] Gate Results Visualization
- [x] Red-Team Report
- [x] Depth 
- [ ] Decision Landscape

### Gates Verified
- [x] V1  [x] V2  [x] V3  [x] V4  [x] V5  [x] V6
- [x] Held-Out  [x] Ensemble  [ ] Human (optional)
- [x] Red-Team

### Required Interferences
- From ALL SKILLS: All artifacts → evidence collection
- From CONDUCTOR: Orchestration log → interference validation