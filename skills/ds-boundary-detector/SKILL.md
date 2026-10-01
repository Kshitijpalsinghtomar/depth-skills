---
name: boundary-detector
codename: BOUNDARY-DETECTOR
internal: Knowledge Boundary Probe v1.0
version: 1.0
tier: excavation
trigger:
  - "what do I not know"
  - "am I hallucinating"
  - "knowledge boundary"
  - "unknown unknowns"
  - "any high-stakes answer where model confidence may be miscalibrated"
description: Probes the model's parametric knowledge boundaries using UnknownBench-style diagnostics. Detects when the model is confidently wrong about things outside its training data. Prevents epistemic hazard by flagging knowledge gaps before skills activate on voids.
author: Kshitijpalsinghtomar
tags: [boundary, knowledge, hallucination, calibration, unknownbench, epistemic-hazard, probe]
artifacts:
  - boundary-probe-results
  - knowledge-gap-map
  - confidence-calibration
  - void-detection-report
    - phase-activation
composable_with:
  - excavate
  - provenance
  - adversary
  - conductor
  - deep-think
thinking_parameters:
  probe_types: ["unknownbench", "retrieval_gap", "ensemble_disagreement", "self_consistency"]
  min_probes: 5
  confidence_threshold: 0.7
  require_void_detection: true
---

# BOUNDARY-DETECTOR — Knowledge Boundary Probe (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (knowledge gap map, void detection report), and verifies Gates V1, V3. It provides the critical "knowledge boundary" signal for the Depth .

> **Research Basis**: Liu et al. (2023) "Examining LLMs' Uncertainty Expression Towards Questions Outside Parametric Knowledge" (arXiv:2311.09731) — UnknownBench shows most LLMs fail to consistently refuse or express uncertainty towards questions outside their parametric knowledge, although instruction fine-tuning provides marginal enhancements.

Your model has parametric knowledge — a vast but finite training corpus. Outside that boundary lies the **void**: questions the model has never seen, concepts that don't exist, premises that are false. The model doesn't know where the boundary is. It generates confident answers in the void.

This skill **probes the boundary** before other skills activate. It runs diagnostic probes to detect:
1. **Non-existent concepts** — things that sound real but aren't in training data
2. **False premises** — premises that contradict established knowledge
3. **Retrieval gaps** — where external knowledge is needed but not accessed
4. **Ensemble disagreement** — where different reasoning paths diverge
5. **Self-consistency failures** — where the model contradicts itself on the same question

**If the boundary probe detects a void, other skills MUST NOT activate on that void.** They must flag, defer, or redesign.

---

## The Failure Mode You Must Recognize

You are about to run deep-think, adversary, diverge, etc. on a question that:
- Contains concepts not in your training data (but you don't know that)
- Assumes false premises (but you pattern-matched them as familiar)
- Requires knowledge you don't have (but you'll hallucinate anyway)

Your skills will produce **beautiful artifacts on empty ground**. The activation heatmap will show depth. The assumption list will be thorough. The adversary will mount sophisticated attacks. **But the foundation is void.**

This is **epistemic hazard**: skills that *feel* like they make the model smarter actually make it *more confidently wrong* on knowledge gaps.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `probe_types` (default: ["unknownbench", "retrieval_gap", "ensemble_disagreement", "self_consistency"]) — which probes to run
- `min_probes` (default 5) — minimum probes per type
- `confidence_threshold` (default 0.7) — confidence above which void detection triggers
- `require_void_detection` (default true) — must detect voids before other skills run

---

### 1 — UNKNOWN BENCH PROBES (Non-Existent Concepts)

**Based on Liu et al. (2023) UnknownBench methodology.**

Generate diagnostic questions containing **non-existent concepts** or **false premises** that are structurally similar to the task domain but guaranteed to be outside parametric knowledge.

```
UNKNOWN BENCH PROBES
────────────────────────────────────────
Task Domain: [e.g., "distributed systems architecture"]
Probe Strategy: [generate non-existent concepts in this domain]

Probe 1: [Question with non-existent concept]
  Concept: [name of fake concept — e.g., "Quantum Byzantine Consensus Protocol v3"]
  Structure: [how it mimics real concepts — e.g., "combines quantum crypto + Byzantine fault tolerance + versioning"]
  Expected Behavior: [REFUSE / UNCERTAIN / HALLUCINATE]
  Actual Response: [model's response]
  Confidence: [0.0-1.0 — model's expressed confidence]
  Void Detected: [YES/NO — if confidence > threshold AND concept is fake]

Probe 2: [Question with false premise]
  Premise: [false but plausible — e.g., "Since the CAP theorem was disproven in 2023..."]
  Expected Behavior: [CORRECT / REFUSE]
  Actual Response: [model's response]
  Confidence: [0.0-1.0]
  Void Detected: [YES/NO]

Probe 3: [Question with hallucinated citation]
  Citation: [fake paper — e.g., "Smith et al. 2024 'Neural Consensus in Async Networks'"]
  Expected Behavior: [REFUSE / "I don't know"]
  Actual Response: [model's response]
  Confidence: [0.0-1.0]
  Void Detected: [YES/NO]

[Minimum min_probes total across all probe types]
────────────────────────────────────────
```

**Void Detection Criteria:**
- Model expresses confidence > `confidence_threshold` on known-false content
- Model generates specific details about non-existent concepts
- Model fails to refuse or express uncertainty

**Artifact:** `unknownbench_probes` with results and void detections.

**CEI Component:** UnknownBench Probes (weight 4.0)

**SI Component:** Boundary violations (void detections count)

---

### 2 — RETRIEVAL GAP PROBES

Test whether the model recognizes when it needs external knowledge.

```
RETRIEVAL GAP PROBES
────────────────────────────────────────
For each domain-specific fact needed for the task:
  Fact: [specific fact — e.g., "current AWS Lambda cold start latency in us-east-1"]
  Parametric Knowledge: [YES/NO — is this in training data?]
  If NO:
    Probe: [ask model for the fact]
    Response: [model's answer]
    Behavior: [HALLUCINATE / REFUSE / UNCERTAIN / DEFER_TO_TOOL]
    Confidence: [0.0-1.0]
    Gap Detected: [YES if HALLUCINATE with confidence > threshold]

  If YES (in training data but may be outdated):
    Probe: [ask for current value]
    Response: [model's answer]
    Behavior: [CORRECT / OUTDATED / HALLUCINATE]
    Confidence: [0.0-1.0]
    Staleness Detected: [YES if OUTDATED with high confidence]
────────────────────────────────────────
```

**Artifact:** `retrieval_gap_probes` with gap/staleness detections.

**CEI Component:** Retrieval Gap Probes (weight 3.0)

---

### 3 — ENSEMBLE DISAGREEMENT PROBES

Run the same reasoning through multiple independent paths and measure disagreement.

```
ENSEMBLE DISAGREEMENT PROBES
────────────────────────────────────────
Question: [core question from task]
Paths: [N independent reasoning paths — different framings, abstractions, or random seeds]

Path 1: [framing] → Answer: [result] → Confidence: [0.0-1.0]
Path 2: [framing] → Answer: [result] → Confidence: [0.0-1.0]
Path 3: [framing] → Answer: [result] → Confidence: [0.0-1.0]
...

Disagreement Metrics:
  Pairwise Agreement: [fraction of pairs with same conclusion]
  Confidence Variance: [variance of confidence scores]
  Entropy: [Shannon entropy of answer distribution]
  Majority Confidence: [confidence of majority answer]

Void Detected: [YES if (Pairwise Agreement < 0.5) OR (Confidence Variance > 0.2) OR (Entropy > 1.0)]
  Interpretation: High disagreement on same question = knowledge boundary or ambiguity
────────────────────────────────────────
```

**Artifact:** `ensemble_disagreement_probes` with disagreement metrics.

**CEI Component:** Ensemble Disagreement (weight 3.0)

---

### 4 — SELF-CONSISTENCY PROBES

Test whether the model gives consistent answers to the same question under perturbation.

```
SELF-CONSISTENCY PROBES
────────────────────────────────────────
Question: [core question]
Perturbations: [N variations — rephrasing, added context, temperature changes]

Original: [answer] → Confidence: [0.0-1.0]
Perturbation 1: [variation] → Answer: [result] → Confidence: [0.0-1.0]
Perturbation 2: [variation] → Answer: [result] → Confidence: [0.0-1.0]
...

Consistency Metrics:
  Semantic Similarity: [average pairwise similarity of answers]
  Confidence Stability: [std dev of confidence scores]
  Contradiction Rate: [fraction of pairs with contradictory claims]

Void Detected: [YES if (Semantic Similarity < 0.7) OR (Contradiction Rate > 0.3)]
  Interpretation: Inconsistency on same question = knowledge boundary or instability
────────────────────────────────────────
```

**Artifact:** `self_consistency_probes` with consistency metrics.

**CEI Component:** Self-Consistency Probes (weight 3.0)

---

### 5 — KNOWLEDGE GAP MAP

Synthesize all probes into a map of knowledge boundaries for the task.

```
KNOWLEDGE GAP MAP
────────────────────────────────────────
Task: [description]
Domain: [domain]

Verified Knowledge (Safe for skills):
  [List concepts/facts confirmed in parametric knowledge]
  Confidence: [average confidence on verified items]

Knowledge Gaps (Void — skills MUST NOT activate here):
  Gap 1: [concept/area]
    Probe Type: [which probe detected it]
    Severity: [CRITICAL / HIGH / MEDIUM]
    Impact: [what skills would be affected if they ran on this]
    Action: [FLAG / DEFER / REDIRECT_TO_TOOL / REQUIRE_HUMAN]

  Gap 2: [concept/area]
    ...

Stale Knowledge (May be outdated):
  [List concepts where training data may be outdated]
  Action: [REQUIRE_RETRIEVAL / FLAG_AS_POTENTIALLY_STALE]

Ambiguous Zones (High disagreement/inconsistency):
  [List areas where ensemble/self-consistency probes flagged issues]
  Action: [REQUIRE_CLARIFICATION / MULTI_PATH_REASONING]

Overall Boundary Assessment:
  Void Coverage: [fraction of task domain in void — 0.0-1.0]
  Safe for Skills: [YES/NO — if void coverage < 0.2]
  Recommendation: [PROCEED / PROCEED_WITH_GAPS_FLAGGED / DEFER_UNTIL_RETRIEVAL / REQUIRE_HUMAN]
────────────────────────────────────────
```

**Artifact:** `knowledge_gap_map` — the go/no-go decision for skill activation.

---

### 6 — VOID DETECTION REPORT

Final report on whether the task contains voids that invalidate skill activation.

```
VOID DETECTION REPORT
────────────────────────────────────────
Task: [description]

Probe Summary:
  UnknownBench Probes: [N run, M voids detected]
  Retrieval Gap Probes: [N run, M gaps detected]
  Ensemble Disagreement: [N paths, agreement: 0.XX, void: YES/NO]
  Self-Consistency: [N perturbations, similarity: 0.XX, void: YES/NO]

Void Summary:
  Critical Voids: [N — areas where skills would hallucinate dangerously]
  High-Risk Voids: [N — areas where skills would likely be wrong]
  Medium Voids: [N — areas needing retrieval/human]

Skill Activation Decision:
  [PROCEED / PROCEED_WITH_GAPS_FLAGGED / DEFER_UNTIL_RETRIEVAL / REQUIRE_HUMAN]

If PROCEED_WITH_GAPS_FLAGGED:
  Gaps to Flag in Skill Outputs:
    - [Gap 1]: Flag in [which skills] as "ASSUMES [X] — UNVERIFIED"
    - [Gap 2]: Flag in [which skills] as "REQUIRES RETRIEVAL: [Y]"

If DEFER_UNTIL_RETRIEVAL:
  Required Retrieval: [specific facts/concepts to retrieve before skills run]

If REQUIRE_HUMAN:
  Human Needed For: [specific decisions/gaps]
────────────────────────────────────────
```

**Artifact:** `void_detection_report` — the gate for skill activation.

---

### 7 — METRICS: Compute and Output Depth Metrics

#### 7.1 Phase Activation (for ADS)

```json
{
  "phase": 1,
  "skill": "boundary-detector",
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
    "unknownbench_probes": 4.0,
    "retrieval_gap_probes": 3.0,
    "ensemble_disagreement": 3.0,
    "self_consistency": 3.0,
    "knowledge_gap_map": 2.0,
    "void_detection_report": 2.0,
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
    "boundary_violations": N,
    "assumption_reversals": 0,
    "si_total": N
  }
}
```

#### 7.4 Cognitive Traces

**Knowledge Gap Map:**
```json
{
  "type": "knowledge_gap_map",
  "verified_knowledge": ["concept1", "concept2"],
  "gaps": [
    {"area": "concept", "severity": "CRITICAL", "probe": "unknownbench", "action": "FLAG"},
    {"area": "concept", "severity": "HIGH", "probe": "retrieval_gap", "action": "REQUIRE_RETRIEVAL"}
  ],
  "stale_knowledge": ["concept"],
  "ambiguous_zones": ["concept"],
  "void_coverage": 0.XX,
  "safe_for_skills": true/false
}
```

**Void Detection Report:** (as defined in Step 6)

#### 7.5 Depth  Contribution

```json
{
  "skill": "boundary-detector",
  "version": "1.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": N, "ec": 0.XX},
  "gates_verified": {"V1": true, "V3": true},
  "limitations": ["..."]
}
```

---

### 8 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V1** | Assumption Coverage | Every assumption depending on parametric knowledge has boundary probe result |
| **V3** | Opposition Authenticity | Void detections are genuine (not false positives from probe design) |

**If any gate FAILS:** Return to relevant step and fix. Do not deliver.

---

### 9 — INTERFERENCE: Provide to Later Skills

**Critical Interference — This skill runs FIRST (Phase 1) and gates all subsequent skills.**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| DEEP-THINK | Knowledge gaps → assumption flags | +0.20 |
| EXCAVATE | Knowledge gaps → C2/C3 assumptions | +0.25 |
| ADVERSARY | Voids → fatal attack targets | +0.20 |
| DIVERGE | Gaps → contrarian path seeds | +0.15 |
| PROVENANCE | Gaps → G/S tagging for assumptions | +0.15 |
| CONDUCTOR | Void decision → skill activation gating | +0.30 |

**If Void Coverage > 0.2:** CONDUCTOR must **DEFER** skill activation until retrieval/human fills gaps.

**Artifact:** `interference_provided` — the gating signal for all downstream skills.

---

## The Deeper Purpose

**Skills are scaffolds. They reorganize search in parametric knowledge. They cannot create knowledge.** If the parametric knowledge has a gap, skills build elaborate structures on voids. The result is **confident hallucination with beautiful artifacts**.

This skill is the **grounding check**. It runs first. It probes the boundary. It says: "Here be dragons. Skills, do not enter." Or: "Safe to proceed, but flag these gaps." Or: "Stop. Retrieve first. Human needed."

Without this skill, the premium architecture is a **hallucination amplifier**. With it, it's a **grounded reasoning engine**.

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 1 (runs first). It outputs:
```json
{
  "phase": 1,
  "skill": "boundary-detector",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: unknownbench_probes (4.0), retrieval_gap_probes (3.0), ensemble_disagreement (3.0), self_consistency (3.0), knowledge_gap_map (2.0), void_detection_report (2.0)
- Total complexity weight: 17.0

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: [void detections count]
- Assumption reversals: 0

### Cognitive Traces Produced
- [x] Knowledge Gap Map
- [x] Void Detection Report
- [ ] Activation Heatmap
- [ ] Decision Landscape

### Gates Verified
- [x] V1  [ ] V2  [x] V3  [ ] V4  [ ] V5  [ ] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From DEEP-THINK: Task domain → probe generation
- From EXCAVATE: Assumptions → targeted probes