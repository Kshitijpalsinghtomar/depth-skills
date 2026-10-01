---
name: depth-mathematics
codename: DEPTH-MATH
internal: Mathematical Formalization of Cognitive Depth
version: 1.0
tier: foundation
description: Formal mathematical definitions for measuring, verifying, and optimizing cognitive depth in AI reasoning. Provides computable metrics (ADS, CEI, SI, EC, OV) that transform qualitative "thinking deeper" into quantitative, verifiable, optimizable objectives.
author: Kshitijpalsinghtomar
tags: [mathematics, metrics, verification, optimization, depth-quantification]
artifacts:
  - activation-depth-score
  - cognitive-effort-index
  - surprise-index
  - epistemic-calibration
  - option-value
  - depth-certificate
composable_with: [all-skills]
---

# DEPTH-MATHEMATICS — Formal Quantification of Cognitive Depth

## The Core Problem

"Thinking deeper" is currently a qualitative claim. This module makes it **quantitative, verifiable, and optimizable**. Every skill in the premium architecture must compute and report these metrics. The metrics are not decorative — they are the **objective function** that the meta-learning loop optimizes.

---

## 1. ACTIVATION DEPTH SCORE (ADS)

Measures how deeply the model's knowledge pathways were activated during reasoning.

### Definition

```
ADS = Σᵢ₌₁⁵ wᵢ × φᵢ / Σᵢ₌₁⁵ wᵢ
```

Where:
- **w** = Phase weights: [0.10, 0.15, 0.25, 0.25, 0.25] for Phases 1-5
- **φᵢ** = Phase activation ∈ [0, 1] computed as:

```
φᵢ = (Artifact_Completenessᵢ × Gate_Pass_Rateᵢ × External_Validityᵢ × Human_Evalᵢ)^(1/4)
```

### Phase Definitions

| Phase | Skills | Weight | Activation Components |
|-------|--------|--------|----------------------|
| 1 ORIENT | DESCEND, DEEP-THINK | 0.10 | Restatement quality, assumption coverage, problem framing |
| 2 EXPAND | DIVERGE, REFRAME, INVERT, EXCAVATE | 0.15 | Branch independence, lens diversity, inversion validity, assumption depth |
| 3 CHALLENGE | ADVERSARY, EMERGENCE, TEMPORAL | 0.25 | Attack specificity, emergence detection, future coverage |
| 4 VERIFY | CONTRADICT, PROVENANCE | 0.25 | Conflict detection, evidence calibration, inflation audit |
| 5 DELIVER | FIDELITY, NEGATIVE-SPACE, THRESHOLD | 0.25 | Compression integrity, silence report, commitment gates |

### Computation Protocol

Each skill **must** output a `phase_activation` object:

```json
{
  "phase": 3,
  "skill": "adversary",
  "artifact_completeness": 0.95,
  "gate_pass_rate": 0.80,
  "external_validity": 0.70,
  "human_eval": 0.85,
  "phase_activation": 0.82
}
```

### Thresholds

| ADS Range | Interpretation | Action |
|-----------|----------------|--------|
| < 0.30 | Surface only | Reject — insufficient depth |
| 0.30 - 0.50 | Shallow | Accept with warnings |
| 0.50 - 0.70 | Moderate | Accept for routine tasks |
| 0.70 - 0.85 | Deep | Required for Category 3+ decisions |
| > 0.85 | Forensic | Required for Category 4 decisions |

---

## 2. COGNITIVE EFFORT INDEX (CEI)

Measures the **computational work** expended per unit of output. Prevents "cargo cult depth" (verbose but shallow).

### Definition

```
CEI = (Σ Artifacts × Complexity_Weight) / (Output_Tokens × Wall_Time_Seconds)
```

### Complexity Weights

| Artifact Type | Weight | Rationale |
|---------------|--------|-----------|
| Restatement | 1.0 | Baseline |
| Assumption List | 2.0 | Requires active search |
| Branch/Path Cards | 3.0 | Requires genuine alternatives |
| Attack/Challenge | 4.0 | Requires opposition generation |
| Cross-Frame Analysis | 5.0 | Requires representation switching |
| Verification Gates | 3.0 | Requires systematic checking |
| Cognitive Traces | 2.0 | Requires meta-representation |
| Failure Envelopes | 3.0 | Requires boundary reasoning |

### Interpretation

- **CEI < 0.1**: Performative (many tokens, little cognitive work)
- **CEI 0.1 - 0.5**: Standard
- **CEI 0.5 - 1.0**: High effort
- **CEI > 1.0**: Intensive (expected for forensic depth)

---

## 3. SURPRISE INDEX (SI)

Measures **how much the reasoning changed** from initial surface response. High SI = genuine exploration occurred.

### Definition

```
SI = C2_C3_Count + Contrarian_Viable + Fatal_Attacks + Boundary_Violations + Assumption_Reversals
```

Where:
- **C2_C3_Count**: Number of assumptions rated C2 (Foundation) or C3 (Ontological)
- **Contrarian_Viable**: 1 if PATH 4 (contrarian) is viable, 0 otherwise
- **Fatal_Attacks**: Number of FATAL attacks from ADVERSARY that required rebuild
- **Boundary_Violations**: Number of failure envelope boundaries that changed the answer
- **Assumption_Reversals**: Number of assumptions where verification changed the rating

### Thresholds

| SI | Interpretation |
|----|----------------|
| 0 | No surprise — pure pattern match |
| 1-2 | Minor surprises |
| 3-5 | Significant exploration |
| 6-10 | Deep restructuring |
| >10 | Fundamental reframing |

---

## 4. EPISTEMIC CALIBRATION (EC)

Measures **honesty about uncertainty**. From PROVENANCE ledger.

### Definition

```
EC = (Facts + 0.5 × Inferences) / (Facts + Inferences + Guesses + Speculations)
```

### Tag Definitions (Strict)

| Tag | Definition | Weight |
|-----|------------|--------|
| **F** (Fact) | Verifiable in authoritative source; citation provided | 1.0 |
| **I** (Inference) | Logical derivation from facts; reasoning chain explicit | 0.5 |
| **G** (Guess) | Plausible but unverified; pattern-based only | 0.0 |
| **S** (Speculation) | No evidence; pure hypothesis | 0.0 |

### Inflation Penalty

If inflation audit detects downgrades:
```
EC_adjusted = EC × (1 - Inflation_Rate)
Inflation_Rate = Claims_Downgraded / Total_Claims
```

### Thresholds

| EC | Interpretation |
|----|----------------|
| < 0.3 | Epistemic hazard — mostly guesses presented as facts |
| 0.3 - 0.5 | Poor calibration |
| 0.5 - 0.7 | Acceptable |
| 0.7 - 0.85 | Well-calibrated |
| > 0.85 | Exceptional honesty |

---

## 5. OPTION VALUE (OV)

Measures **future robustness** of the decision. From TEMPORAL analysis.

### Definition

```
OV = Σ_f P(f) × [V(decision, f) - V(baseline, f)]
```

Where:
- **f** ∈ {Conservative, Growth, Disruption, Stagnation, Black_Swan}
- **P(f)** = Subjective probability of future f (from TEMPORAL Step 2)
- **V(decision, f)** = Value of chosen decision in future f
- **V(baseline, f)** = Value of present-optimal baseline in future f

### Value Function

```
V(decision, f) = Utility(decision, f) - Switching_Cost(decision, f)
```

Where Utility ∈ [-1, 1] (catastrophic failure to optimal) and Switching_Cost ≥ 0.

### Interpretation

| OV | Interpretation |
|----|----------------|
| < -0.2 | Present-optimal destroys future options |
| -0.2 to 0.2 | Neutral |
| 0.2 to 0.5 | Moderate option value |
| > 0.5 | High option value — future-robust |

---

## 6. DEPTH CERTIFICATE (Composite)

Single verifiable artifact combining all metrics.

### Structure

```json
{
  "certificate_id": "dc_<timestamp>_<hash>",
  "task_hash": "sha256(task_description)",
  "model": "model_identifier",
  "skills_executed": ["deep-think", "adversary", "diverge", ...],
  "metrics": {
    "ads": 0.78,
    "cei": 0.62,
    "si": 7,
    "ec": 0.71,
    "ov": 0.34
  },
  "gates": {
    "v1_assumption_coverage": true,
    "v2_alternative_independence": true,
    "v3_opposition_authenticity": true,
    "v4_temporal_consistency": true,
    "v5_evidence_calibration": true,
    "v6_recursive_stability": true,
    "ungameable_human_eval": true,
    "ungameable_held_out": true,
    "ungameable_ensemble": true
  },
  "threshold": "CATEGORY_3",
  "verdict": "PASS",
  "limitations": ["Assumption A3 flagged", "Gate V3 passed with ensemble only"],
  "reproducibility": {
    "seed": 42,
    "temperature": 0.0,
    "skill_versions": {"deep-think": "2.0", "adversary": "2.0", ...}
  }
}
```

### Verification

A Depth Certificate is **valid** iff:
1. All executed skills report phase_activation
2. ADS ≥ threshold for task category
3. All V1-V6 gates PASS
4. At least 2 ungameable gates PASS
5. EC ≥ 0.5
6. Certificate signed by VERIFICATION-GATES skill

---

## 7. RECURSIVE STABILITY METRIC (RSM)

For skills with recursive self-application.

### Definition

```
RSM = 1 - (Semantic_Distance(output_d, output_{d-1}) / Max_Distance)
```

Where:
- **d** = recursion depth
- **Semantic_Distance** = 1 - cosine_similarity(embedding(output_d), embedding(output_{d-1}))
- **Max_Distance** = 1.0 (orthogonal)

### Convergence Criteria

Recursion **converges** when:
- RSM > 0.95 for 2 consecutive depths, AND
- SI_d > SI_{d-1} (still discovering new issues), AND
- d ≤ max_depth (default 3)

### Divergence Detection

Recursion **diverges** when:
- RSM < 0.80 (oscillating), OR
- SI_d < SI_{d-1} for 2 consecutive depths (diminishing returns), OR
- d > max_depth

---

## 8. COMPOSITIONAL INDEPENDENCE METRIC (CIM)

For DIVERGE paths and skill interference.

### Definition

For a set of n paths/skills:
```
CIM = 1 - (2 / (n(n-1))) × Σ_{i<j} Cosine_Similarity(embedding(path_i), embedding(path_j))
```

### Thresholds

| CIM | Interpretation |
|-----|----------------|
| < 0.3 | Paths are variations, not branches |
| 0.3 - 0.5 | Moderate independence |
| 0.5 - 0.7 | Good independence |
| > 0.7 | Strong structural divergence |

---

## 9. INTERFERENCE MATRIX (Skill Composition)

Quantifies how skills affect each other when composed.

### Definition

For skills A → B (A runs before B):
```
Interference(A→B) = Quality(B_with_A) - Quality(B_alone)
```

Where Quality = ADS of B's output.

### Required Interferences (Must Be Positive)

| Skill A | Skill B | Minimum Interference |
|---------|---------|---------------------|
| DEEP-THINK | DIVERGE | +0.15 (assumptions seed paths) |
| EXCAVATE | INVERT | +0.20 (C2/C3 assumptions become inversion targets) |
| ADVERSARY | PROVENANCE | +0.15 (attacks cite evidence tags) |
| TEMPORAL | THRESHOLD | +0.10 (regret informs reversal cost) |
| NEGATIVE-SPACE | EMERGENCE | +0.15 (absent failures map to interactions) |

### Validation

CONDUCTOR must verify all required interferences > minimum before allowing delivery.

---

## 10. THINKING PARAMETERS (User-Configurable)

Standardized parameters that control depth/rigor.

```json
{
  "thinking_parameters": {
    "depth": {
      "min_assumptions": 10,
      "min_branches": 3,
      "min_attacks": 5,
      "min_lenses": 3,
      "min_futures": 3
    },
    "rigor": {
      "collapse_threshold": "C2",
      "attack_severity_floor": "SIGNIFICANT",
      "contradiction_severity_floor": "STRUCTURAL",
      "min_fact_ratio": 0.6,
      "max_guess_tolerance": 0.15
    },
    "recursion": {
      "max_depth": 3,
      "convergence_threshold": 0.95,
      "require_external_grounding": true
    },
    "integration": {
      "require_interference": true,
      "require_recursive_audit": true,
      "min_cim": 0.5
    },
    "verification": {
      "require_human_eval": false,
      "require_held_out": true,
      "require_ensemble": true
    }
  },
  "presets": {
    "quick": {"depth": {"min_assumptions": 5, "min_branches": 2}, "recursion": {"max_depth": 1}},
    "standard": {"depth": {"min_assumptions": 10, "min_branches": 3}, "recursion": {"max_depth": 1}},
    "deep": {"depth": {"min_assumptions": 15, "min_branches": 4}, "recursion": {"max_depth": 2}, "integration": {"require_interference": true}},
    "forensic": {"depth": {"min_assumptions": 20, "min_branches": 5}, "recursion": {"max_depth": 3}, "integration": {"require_interference": true, "require_recursive_audit": true}, "verification": {"require_human_eval": true}}
  }
}
```

---

## 11. COGNITIVE TRACE ARTIFACTS (Standardized Visualizations)

Every skill must produce these machine-readable traces.

### 11.1 Activation Heatmap

```json
{
  "type": "activation_heatmap",
  "layers": [
    {"name": "Surface Patterns (0-20%)", "activation": 0.40, "zone": "pattern_gravity"},
    {"name": "Assumption Layer (20-40%)", "activation": 0.50, "zone": "excavation"},
    {"name": "Alternative Space (40-60%)", "activation": 0.40, "zone": "divergence"},
    {"name": "Stress-Test Zone (60-80%)", "activation": 0.30, "zone": "adversarial"},
    {"name": "Integrity Layer (80-100%)", "activation": 0.20, "zone": "verification"}
  ],
  "overall_activation_depth": 0.36,
  "target_for_task": 0.70
}
```

### 11.2 Assumption Dependency Graph

```json
{
  "type": "assumption_dependency_graph",
  "nodes": [
    {"id": "A1", "rating": "C3", "statement": "AGI-likeness decomposes into modules"},
    {"id": "A2", "rating": "C2", "statement": "Current architecture supports meta-learning"},
    {"id": "A3", "rating": "C1", "statement": "Skills compose associatively"}
  ],
  "edges": [
    {"from": "A1", "to": "Answer_Core", "type": "ontological"},
    {"from": "A2", "to": "Approach_B", "type": "foundation"},
    {"from": "A3", "to": "CONDUCTOR", "type": "structural"}
  ],
  "critical_path": ["A1", "Answer_Core"],
  "ontological_risk": true
}
```

### 11.3 Decision Landscape Topology

```json
{
  "type": "decision_landscape",
  "paths": [
    {"id": "A", "name": "Present-Optimal", "profile": [0.9, 0.8, 0.3, 0.1], "peaks": ["now"], "cliffs": ["12mo"]},
    {"id": "B", "name": "Robust", "profile": [0.6, 0.7, 0.8, 0.8], "peaks": ["24mo"], "cliffs": []},
    {"id": "C", "name": "Contrarian", "profile": [0.3, 0.4, 0.9, 0.7], "peaks": ["disruption"], "cliffs": ["conservative"]},
    {"id": "D", "name": "Hybrid", "profile": [0.7, 0.8, 0.8, 0.8], "peaks": ["all"], "cliffs": []}
  ],
  "dimensions": ["Present", "Growth", "Disruption", "Long-term"],
  "recommended": "D",
  "escape_hatches": ["Trigger: model_benchmark_delta < 0.1", "Migrate to: B"]
}
```

---

## 12. VERIFICATION GATES (Machine-Checkable)

### Gate V1: Assumption Coverage
```
Input: Problem statement + Answer + Assumption list
Check: ∀ claim ∈ Answer: ∃ assumption ∈ Assumptions supporting claim
Pass: Coverage ≥ 90%
```

### Gate V2: Alternative Independence
```
Input: DIVERGE paths
Check: CIM(paths) ≥ 0.5
Pass: True
```

### Gate V3: Opposition Authenticity
```
Input: ADVERSARY attacks
Check: ∀ attack: references_specific_answer_text ∧ cites_external_evidence
Pass: 100% compliance
```

### Gate V4: Temporal Consistency
```
Input: TEMPORAL futures + chosen path
Check: Chosen path survives (not catastrophic) in ≥ 2/3 futures
Pass: True
```

### Gate V5: Evidence Calibration
```
Input: PROVENANCE ledger
Check: EC ≥ 0.5 ∧ No G-tagged claims without uncertainty markers
Pass: True
```

### Gate V6: Recursive Stability
```
Input: Skill outputs at depth d and d-1
Check: RSM > 0.95 ∧ SI_d ≥ SI_{d-1}
Pass: True
```

### Ungameable Gates (Require External Resources)

| Gate | Requirement | Implementation |
|------|-------------|----------------|
| **Human Eval** | Human rates depth on 10 novel tasks | Separate human evaluation pipeline |
| **Held-Out Tasks** | Skill improves performance on unseen task class | Benchmark suite with held-out split |
| **Ensemble Critic** | Different model runs ADVERSARY/CONTRADICT | Multi-model orchestration |

---

## 13. IMPLEMENTATION REQUIREMENTS

Every premium skill **must**:

1. **Accept** `thinking_parameters` as input
2. **Output** `phase_activation` for ADS computation
3. **Output** `cognitive_trace` (heatmap, dependency graph, or landscape)
4. **Output** `depth_certificate` contribution
5. **Verify** required interferences with prior skills
6. **Support** recursive self-application with RSM tracking
7. **Report** CEI components (artifact counts, complexity weights)
8. **Tag** every claim in output with PROVENANCE tags
9. **Compute** and report SI components
10. **Pass** V1-V6 gates before delivery

---

## 14. MATHEMATICAL NOTATION REFERENCE

| Symbol | Meaning |
|--------|---------|
| Σ | Summation |
| ∀ | For all |
| ∃ | There exists |
| ∈ | Element of |
| ∧ | Logical AND |
| ∨ | Logical OR |
| ¬ | Logical NOT |
| ⇒ | Implies |
| ⇔ | If and only if |
| |x| | Absolute value / cardinality |
| ||x|| | Norm |
| ⟨x, y⟩ | Inner product |
| cos(θ) | Cosine similarity |
| H(x) | Entropy |
| KL(p||q) | KL divergence |
| 𝔼[X] | Expectation |
| P(A|B) | Conditional probability |

---

## 15. USAGE IN SKILLS

Each skill's SKILL.md must include a **MATHEMATICS COMPLIANCE** section:

```markdown
## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase [N]. It outputs:
```json
{
  "phase": N,
  "skill": "skill-name",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: [list with complexity weights]
- Total complexity weight: X.X

### SI Components
- C2/C3 assumptions: N
- Contrarian viable: Y/N
- Fatal attacks: N
- Boundary violations: N
- Assumption reversals: N

### Cognitive Traces Produced
- [ ] Activation Heatmap
- [ ] Assumption Dependency Graph
- [ ] Decision Landscape
- [ ] Other: _______

### Gates Verified
- [ ] V1  [ ] V2  [ ] V3  [ ] V4  [ ] V5  [ ] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From [Skill A]: [specific interference]
- From [Skill B]: [specific interference]
```

---

*This mathematical framework is the backbone of the premium architecture. Skills that don't compute these metrics are not "premium" — they're the old version.*