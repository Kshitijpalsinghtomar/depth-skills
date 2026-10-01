---
name: contradict
codename: CONTRADICT
internal: Coherence Auditor v2.0
version: 2.0
tier: integrity
trigger: any multi-part answer, any design document, any plan with more than 5 steps, "does this make sense", "is this consistent"
description: Cross-compares every claim in an output to detect internal contradictions that sequential generation hides. Now with mathematical depth metrics, claim graph analysis, global coherence , and verification gates.
author: Kshitijpalsinghtomar
tags: [coherence, consistency, contradiction, audit, claims, metrics, recursion, verification]
artifacts:
  - claim-extraction
  - conflict-list
  - severity-classification
  - resolution-log
  - coherence-verdict
  - claim-graph
    - activation-heatmap
    - phase-activation
composable_with:
  - provenance
  - fidelity
  - adversary
  - negative-space
  - conductor
  - boundary-detector
thinking_parameters:
  min_claims: 10
  min_conflicts: 1
  recursion_depth: 1
  require_claim_graph: true
  require_coherence_: true
---

# CONTRADICT v2.0 — Coherence Auditor (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (claim graph, global coherence ), and verifies Gates V1, V3, V5. It builds a formal claim dependency graph for contradiction detection.

You generate sequentially — one section, then the next. Each section is optimized for local coherence. Section A reads well. Section C reads well.

But locally coherent sections can be **globally contradictory**. Section A promises simplicity. Section C introduces complexity that destroys the simplicity. Both sound right alone. Together, they are a lie.

You have no built-in global consistency checker. This skill is that checker.

**New in v2.0:** Mathematical depth metrics, formal claim graph, global coherence , recursive self-audit, verification gates.

---

## The Failure Mode You Must Recognize

You are about to deliver an answer where:
- The introduction says "simple and straightforward"
- Step 7 requires complex configuration across three services
- The summary says "no external dependencies"
- Step 4 uses two external libraries

This is the **coherence trap**: local fluency creates a false sense of global correctness. Each part is individually convincing, but the parts cannot coexist. You don't notice because you generate forward, not cross-sectionally.

**Cargo cult coherence** produces claim lists without building a claim graph. This skill rejects them.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `min_claims` (default 10) — minimum claims to extract
- `min_conflicts` (default 1) — minimum conflicts to find (if 0, answer is trivial)
- `recursion_depth` (default 1) — recursive self-audit rounds
- `require_claim_graph` (default true) — build formal claim dependency graph
- `require_coherence_` (default true) — issue coherence 

---

### Step 1 — EXTRACT: Write Every Claim as a Standalone Statement

Read the entire output. Extract every claim, promise, estimate, and assertion. Write each as a standalone sentence that could be true or false:

```
CLAIM EXTRACTION
────────────────────────────────────────
C1: [section/paragraph ref] — "[exact claim]"
C2: [section/paragraph ref] — "[exact claim]"
C3: [section/paragraph ref] — "[exact claim]"
...
────────────────────────────────────────
```

Types to catch:
- **Promises:** "This approach is simple," "No configuration needed," "Handles all cases"
- **Estimates:** "Takes about a week," "Under 100ms latency," "Minimal effort"
- **Scope claims:** "No external dependencies," "Works offline," "Supports all browsers"
- **Characteristic claims:** "Highly scalable," "Easy to maintain," "Secure by default"
- **Causal claims:** "X causes Y," "A leads to B"

**Minimum `min_claims`.** If you found fewer, you're extracting too loosely — tighten your filter.

**Artifact:** Numbered claim list with section references.

**CEI Component:** Claim Extraction (weight 2.0)

---

### Step 2 — BUILD CLAIM GRAPH (if `require_claim_graph` = true)

**NEW IN v2.0** — Build a formal dependency graph of claims.

```
CLAIM GRAPH
────────────────────────────────────────
Nodes: [claims C1, C2, C3...]
Edges: [C1 → C2 means C2 depends on C1 being true]

For each claim:
  Claim: [statement]
  Type: [promise / estimate / scope / characteristic / causal]
  Dependencies: [which other claims this requires]
  Dependents: [which claims require this]
  If False Impact: [what breaks if this claim is false — cascade analysis]
  Confidence: [0.0-1.0 — from PROVENANCE interference]

Critical Claims (high cascade risk):
  [Claims whose falsity would collapse many others]
────────────────────────────────────────
```

**Artifact:** `claim_graph` — formal dependency structure for contradiction detection.

**CEI Component:** Claim Graph (weight 4.0)

---

### Step 3 — CROSS-COMPARE: Test Each Claim Pair for Mutual Compatibility

For each pair of claims that could potentially conflict, write the comparison:

**Common contradiction patterns to actively scan for:**

| Pattern | Claim Type A | Claim Type B | The Lie |
|---|---|---|---|
| Scope-timeline | "Built in X time" | Feature list A, B, C, D, E | Sum of features doesn't fit in X |
| Simplicity-completeness | "Simple and easy" | "Handles all edge cases" | Comprehensive handling IS complexity |
| Independence-integration | "No dependencies" | "Uses service X, Y" | Those ARE dependencies |
| Performance-richness | "Fast and lightweight" | "Rich animations, real-time" | Each feature costs performance |
| Confidence-uncertainty | "High confidence" | "Several unknowns" | High confidence requires low unknowns |
| Generality-specificity | "Works for any case" | "Optimized for [specific case]" | Optimization is specialization |
| Cost-quality | "Minimal effort" | "Production-quality" | Production quality is not minimal effort |
| Causality-timeline | "X causes Y" | "Y happens before X" | Temporal impossibility |

For each potential conflict found:

```
CONFLICT [N]:
  Claim A: C[x] — "[claim]"
  Claim B: C[y] — "[claim]"
  Can both be true simultaneously?: [yes — how / no — why]
  Graph Path: [dependency path between claims in claim graph]
  Severity: [COSMETIC / STRUCTURAL / FATAL]
────────────────────────────────────────
```

**Artifact:** The conflict list with graph paths and severity.

**CEI Component:** Conflict Detection (weight 4.0)

**SI Component:** Fatal/Structural conflicts (count)

---

### Step 4 — CLASSIFY: Rate Severity of Each Conflict

```
CONFLICT [N]: [COSMETIC / STRUCTURAL / FATAL]

  COSMETIC:    Same meaning, different wording. Fix the wording.
               Both claims can coexist with a minor edit.

  STRUCTURAL:  Real tension. Both cannot be fully true.
               Must decide which takes priority.

  FATAL:       Mutually exclusive. The answer promises something
               logically impossible. Must rebuild.
────────────────────────────────────────
```

**Artifact:** Classified conflict list.

---

### Step 5 — RESOLVE: Address Each Structural and Fatal Conflict

For each STRUCTURAL conflict, choose ONE resolution:

**Priority:** One claim wins. The other is revised. Write which and why.
**Scope:** Both are true in different contexts. Make the scope explicit: "Simple interface, complex internals." Write the scoping language.
**Tradeoff declaration:** The tension IS the point. Write: "We want both [speed] and [thoroughness]. Here is where the dial is set: [specific tradeoff point]."

For each FATAL conflict:

**Rebuild.** The answer needs restructuring. Identify which claim is true and revise everything that contradicts it.

```
RESOLUTION LOG
────────────────────────────────────────
Conflict [N]: [resolution type — priority / scope / tradeoff / rebuild]
  Result:     [what changed in the answer]
  Graph Update: [how claim graph changed]

Conflict [N]: [resolution type]
  Result:     [what changed]
  Graph Update: [how claim graph changed]
────────────────────────────────────────
```

**Artifact:** Resolution log with graph updates.

**CEI Component:** Resolution Log (weight 3.0)

---

### Step 6 — GLOBAL COHERENCE  (if `require_coherence_` = true)

**NEW IN v2.0** — Formal  of coherence.

```
GLOBAL COHERENCE 
────────────────────────────────────────
 ID: gc_<timestamp>_<hash>
Claims Extracted: [count]
Conflicts Found: [count]
  Cosmetic: [count] — fixed
  Structural: [count] — resolved
  Fatal: [count] — rebuilt

Claim Graph:
  Nodes: [count]
  Edges: [count]
  Critical Nodes: [count]
  Max Cascade Depth: [count]

Overall Coherence: [consistent / mostly consistent / inconsistent]
Remaining Tensions: [any unresolved tradeoffs the user should know about]

Coherence Score: [0.0-1.0 — fraction of claims in consistent subgraph]
Valid Until: [date or condition]
────────────────────────────────────────
```

**Artifact:** `global_coherence_` — formal verification of coherence.

**CEI Component:** Coherence  (weight 3.0)

---

### Step 7 — WRITE THE COHERENCE VERDICT

```
COHERENCE VERDICT
────────────────────────────────────────
Claims extracted:   [count]
Conflicts found:    [count]
  Cosmetic:         [count] — fixed
  Structural:       [count] — resolved
  Fatal:            [count] — rebuilt

Claim Graph:
  Nodes: [count]
  Edges: [count]
  Critical Nodes: [count]
  Max Cascade Depth: [count]

Overall coherence:  [consistent / mostly consistent / inconsistent]
Remaining tensions: [any unresolved tradeoffs the user should know about]
Coherence Score:    [0.0-1.0]
────────────────────────────────────────
```

**Artifact:** The coherence verdict.

**CEI Component:** Coherence Verdict (weight 2.0)

---

### 8 — METRICS: Compute and Output Depth Metrics

#### 8.1 Phase Activation (for ADS)

```json
{
  "phase": 4,
  "skill": "contradict",
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
    "claim_extraction": 2.0,
    "claim_graph": 4.0,
    "conflict_detection": 4.0,
    "resolution_log": 3.0,
    "coherence_": 3.0,
    "coherence_verdict": 2.0,
    "total_complexity_weight": 18.0,
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
    "fatal_conflicts": N,
    "structural_conflicts": N,
    "si_total": N
  }
}
```

#### 8.4 Cognitive Traces

**Claim Graph:**
```json
{
  "type": "claim_graph",
  "nodes": [
    {"id": "C1", "claim": "...", "type": "promise", "confidence": 0.XX, "cascade_risk": 0.XX},
    {"id": "C2", "claim": "...", "type": "estimate", "confidence": 0.XX, "cascade_risk": 0.XX}
  ],
  "edges": [
    {"from": "C1", "to": "C2", "type": "depends_on"}
  ],
  "critical_nodes": ["C1"],
  "max_cascade_depth": 3
}
```

**Global Coherence :** (as defined in Step 6)

#### 8.5 Depth  Contribution

```json
{
  "skill": "contradict",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": N, "ec": 0.XX},
  "gates_verified": {"V1": true, "V3": true, "V5": true},
  "limitations": ["..."]
}
```

---

### 9 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V1** | Assumption Coverage | Every claim traces to an assumption (≥90%) — from DEEP-THINK/EXCAVATE |
| **V3** | Opposition Authenticity | Conflicts reference specific claims + cite evidence |
| **V5** | Evidence Calibration | EC ≥ 0.5 (from PROVENANCE); claim confidences match PROVENANCE tags |

**If any gate FAILS:** Return to relevant step and fix. Do not deliver.

---

### 10 — RECURSIVE SELF-AUDIT (if `recursion_depth` > 1)

If `recursion_depth` > 1, apply **this entire protocol** to your own output from Steps 1-6.

For each recursion level d = 2 to `recursion_depth`:
1. Treat your previous output as the "answer under review"
2. Run Steps 1-6 on it
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

### 11 — INTERFERENCE: Receive and Provide

**Receive from prior skills:**

| From Skill | Interference | Use |
|------------|--------------|-----|
| PROVENANCE | Evidence tags (F/I/G/S) + EC | Tag claims with evidence quality; calibrate confidences |
| ADVERSARY | Fatal attacks | Convert to claim conflicts |
| NEGATIVE-SPACE | Critical silences | Add as missing claims |
| BOUNDARY-DETECTOR | Knowledge gaps | Flag claims depending on void knowledge |

**Provide to later skills:**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| FIDELITY | Resolved conflicts → tags that must survive compression | +0.15 |
| THRESHOLD | Fatal conflicts → reversal triggers | +0.15 |
| CONDUCTOR | Coherence score, claim graph,  | +0.20 |
| META-LEARNING | Conflict patterns → skill synthesis targets | +0.10 |

**Artifact:** `interference_log` (received and provided).

---

## The Deeper Purpose

The longer an output, the higher the probability of internal contradiction. Sequential generation optimizes locally, not globally. Words like "simple," "comprehensive," and "handles all cases" are **contradiction magnets** — they make promises the rest of the answer often cannot keep. This skill reads the output not section by section, but claim against claim, surfacing the conflicts that sequential generation cannot see. **Now it's formalized (claim graph), certified (coherence ), and verified (gates).**

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 4. It outputs:
```json
{
  "phase": 4,
  "skill": "contradict",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: claim_extraction (2.0), claim_graph (4.0), conflict_detection (4.0), resolution_log (3.0), coherence_ (3.0), coherence_verdict (2.0)
- Total complexity weight: 18.0

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: 0
- Assumption reversals: 0
- Fatal conflicts: [count]
- Structural conflicts: [count]

### Cognitive Traces Produced
- [x] Claim Graph
- [x] Global Coherence 
- [ ] Decision Landscape

### Gates Verified
- [x] V1  [ ] V2  [x] V3  [ ] V4  [x] V5  [ ] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From PROVENANCE: Evidence tags + EC → claim tagging + confidence calibration
- From ADVERSARY: Fatal attacks → claim conflicts
- From NEGATIVE-SPACE: Critical silences → missing claims
- From BOUNDARY-DETECTOR: Knowledge gaps → void-dependent claims