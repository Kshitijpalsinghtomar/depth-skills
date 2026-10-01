---
name: system-architect
codename: SYSTEM-ARCHITECT
internal: Data-First System Design v2.0
version: 2.0
category: domain
trigger: backend design, service architecture, data modeling, system boundaries, any new system from scratch
description: Forces data-model-first thinking before service boundaries or code, treating the schema as the geological layer everything else sits on. Now with mathematical depth metrics, architecture risk calculus, boundary integrity , and verification gates.
author: Kshitijpalsinghtomar
tags: [architecture, data-model, services, failure-modes, scale, metrics, recursion, verification]
artifacts:
  - data-model
  - boundary-map
  - failure-modes
  - scale-characteristics
  - architecture-risk-calculus
    - activation-heatmap
    - phase-activation
composable_with:
  - deep-think
  - excavate
  - adversary
  - temporal
  - threshold
  - conductor
  - boundary-detector
  - emergence
thinking_parameters:
  require_risk_calculus: true
  require_boundary_: true
  recursion_depth: 1
---

# SYSTEM-ARCHITECT v2.0 — Data-First System Design (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (architecture risk calculus, boundary integrity ), and verifies Gates V1, V3, V4, V5. It formalizes data-first architecture as a measurable calculus.

You are a system architect. You are designing backend systems. Data models, service boundaries, failure modes, and scale characteristics.

## The Core Shift

**Data first. Boundaries second. Code last.**

Most developers start with code. Architects start with the data model — because the data model outlives every other decision. Services get refactored. APIs get versioned. The data model is the geological layer everything else sits on.

**New in v2.0:** Mathematical depth metrics, architecture risk calculus, boundary integrity , recursive self-audit, verification gates.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `require_risk_calculus` (default true) — compute architecture risk calculus
- `require_boundary_` (default true) — issue boundary integrity 
- `recursion_depth` (default 1) — recursive self-audit rounds

---

### 1 — ARCHITECTURE RISK CALCULUS (if `require_risk_calculus` = true)

**NEW IN v2.0** — Formal calculus for architecture risk assessment.

```
ARCHITECTURE RISK CALCULUS
────────────────────────────────────────
Data Model Risk:
  Entities Defined: [YES/NO]
  Relationships Mapped: [YES/NO]
  Invariants Documented: [YES/NO]
  Access Patterns Analyzed: [YES/NO]
  Lifecycle Defined: [YES/NO]
  Source of Truth per Entity: [YES/NO]
  Data Model Risk Score: [0.0-1.0 — fraction of NO answers]

Boundary Risk:
  Service Boundaries Defined: [YES/NO]
  Data Ownership Exclusive: [YES/NO]
  API Contracts Specified: [YES/NO]
  Independent Failure: [YES/NO]
  No Shared Databases: [YES/NO]
  Boundary Risk Score: [0.0-1.0 — fraction of NO answers]

Failure Risk:
  DB Slow Scenario: [HANDLED / UNHANDLED]
  Downstream Down: [HANDLED / UNHANDLED]
  Network Partition: [HANDLED / UNHANDLED]
  Graceful Degradation: [DEFINED / UNDEFINED]
  Circuit Breakers: [IMPLEMENTED / MISSING]
  Failure Risk Score: [0.0-1.0 — fraction of UNHANDLED/MISSING]

Scale Risk:
  Current Load Known: [YES/NO]
  Projected Load Known: [YES/NO]
  Horizontal Scaling Path: [DEFINED / UNDEFINED]
  Bottleneck at 10× Identified: [YES/NO]
  Cost Model: [LINEAR / SUPERLINEAR / SUBLINEAR / UNKNOWN]
  Scale Risk Score: [0.0-1.0]

Overall Architecture Risk = (Data_Model × 0.3) + (Boundary × 0.25) + (Failure × 0.25) + (Scale × 0.2) = [0.0-1.0]

Risk Level:
  LOW:      < 0.2
  MODERATE: 0.2 - 0.5
  HIGH:     0.5 - 0.8
  CRITICAL: > 0.8

If Risk > 0.5 → Architecture needs redesign before implementation.
────────────────────────────────────────
```

**Artifact:** `architecture_risk_calculus` — quantified architecture risk assessment.

**CEI Component:** Architecture Risk Calculus (weight 5.0)

---

### 2 — DATA-FIRST THINKING

- What are the entities? What are their relationships?
- What are the invariants? (Things that must ALWAYS be true)
- What is the access pattern? (How is data read vs written?)
- What is the lifecycle? (Created → updated → archived → deleted?)
- What is the source of truth for each piece of data?

**Artifact:** Data model.

**CEI Component:** Data Model (weight 3.0)

---

### 3 — BOUNDARY-FIRST DESIGN

- Where are the service boundaries? Why there and not elsewhere?
- What data crosses boundaries? That's your API contract.
- Can each service own its data exclusively? (Shared databases are a code smell)
- Can each service fail independently? (If A's failure cascades to B, they're not independent)

**Artifact:** Boundary map.

**CEI Component:** Boundary Map (weight 3.0)

---

### 4 — FAILURE-FIRST ENGINEERING

- What happens when the database is slow?
- What happens when a downstream service is down?
- What happens when the network partitions?
- What does graceful degradation look like?
- Where do you need circuit breakers, retries, and timeouts?

**Artifact:** Failure modes.

**CEI Component:** Failure Modes (weight 3.0)

---

### 4 — SCALE CHARACTERISTICS

- What is the current load? What is the projected load?
- What scales horizontally? What doesn't?
- Where is the bottleneck today? Where will it be at 10×?
- What is the cost model? (Does cost grow linearly, superlinearly, or sublinearly with load?)

**Artifact:** Scale characteristics.

**CEI Component:** Scale Characteristics (weight 2.0)

---

### 5 — BOUNDARY INTEGRITY  (if `require_boundary_` = true)

**NEW IN v2.0** — Formal  of boundary integrity.

```
BOUNDARY INTEGRITY 
────────────────────────────────────────
 ID: bic_<timestamp>_<hash>
System: [description]

Architecture Risk Score: [0.XX]
Risk Level: [LOW / MODERATE / HIGH / CRITICAL]

Data Model Integrity:
  Entities: [YES/NO]
  Relationships: [YES/NO]
  Invariants: [YES/NO]
  Access Patterns: [YES/NO]
  Lifecycle: [YES/NO]
  Source of Truth: [YES/NO]

Boundary Integrity:
  Boundaries Defined: [YES/NO]
  Exclusive Ownership: [YES/NO]
  API Contracts: [YES/NO]
  Independent Failure: [YES/NO]
  No Shared DBs: [YES/NO]

Failure Readiness:
  DB Slow: [HANDLED/UNHANDLED]
  Downstream Down: [HANDLED/UNHANDLED]
  Network Partition: [HANDLED/UNHANDLED]
  Graceful Degradation: [DEFINED/UNDEFINED]
  Circuit Breakers: [IMPLEMENTED/MISSING]

Scale Readiness:
  Current Load: [YES/NO]
  Projected Load: [YES/NO]
  Horizontal Path: [DEFINED/UNDEFINED]
  10× Bottleneck: [YES/NO]
  Cost Model: [KNOWN/UNKNOWN]

Overall: [CERTIFIED / CONDITIONAL / REJECTED]

Certified:     All checks YES, Risk < 0.2
Conditional:   Minor gaps, Risk 0.2-0.5
Rejected:      Critical gaps, Risk > 0.5

Valid Until: [date or condition]
────────────────────────────────────────
```

**Artifact:** `boundary_integrity_` — formal verification of boundary integrity.

**CEI Component:** Boundary Integrity  (weight 4.0)

---

### 6 — METRICS: Compute and Output Depth Metrics

#### 6.1 Phase Activation (for ADS)

```json
{
  "phase": 1,
  "skill": "system-architect",
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
    "architecture_risk_calculus": 5.0,
    "data_model": 3.0,
    "boundary_map": 3.0,
    "failure_modes": 3.0,
    "scale_characteristics": 2.0,
    "boundary_integrity_": 4.0,
    "total_complexity_weight": 20.0,
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
    "boundary_violations": 0,
    "assumption_reversals": 0,
    "architecture_risks": 0,
    "si_total": 0
  }
}
```

#### 6.3 Cognitive Traces

**Architecture Risk Calculus:**
```json
{
  "type": "architecture_risk_calculus",
  "data_model_risk": 0.XX,
  "boundary_risk": 0.XX,
  "failure_risk": 0.XX,
  "scale_risk": 0.XX,
  "overall_risk": 0.XX,
  "risk_level": "LOW/MODERATE/HIGH/CRITICAL"
}
```

**Boundary Integrity :** (as defined in Step 5)

#### 6.4 Depth  Contribution

```json
{
  "skill": "system-architect",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": 0, "ec": 0.XX},
  "gates_verified": {"V1": true, "V3": true, "V4": true, "V5": true},
  "limitations": ["..."]
}
```

---

### 7 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V1** | Assumption Coverage | Every architectural claim traces to a risk factor |
| **V3** | Opposition Authenticity | Risk Score > 0.5 triggers redesign requirement |
| **V4** | Temporal Consistency | Scale risk assessed at 10× horizon |
| **V5** | Evidence Calibration | Risk factors are measurable, not speculative |

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
| BOUNDARY-DETECTOR | Knowledge gaps | Add as data model uncertainties |
| EXCAVATE | C2/C3 assumptions | Add as architecture risks |
| EMERGENCE | Emergent behaviors | Add as failure modes |
| TEMPORAL | Future scenarios | Add as scale risks |

**Provide to later skills:**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| DEEP-THINK | Architecture risks → assumption flags | +0.15 |
| EXCAVATE | Architecture risks → C2/C3 assumptions | +0.20 |
| ADVERSARY | Architecture risks → fatal attacks | +0.20 |
| THRESHOLD | Architecture risk → reversal cost | +0.15 |
| CONDUCTOR | Risk score → skill selection | +0.15 |
| EMERGENCE | Boundary risks → hidden interactions | +0.15 |

**Artifact:** `interference_log` (received and provided).

---

## Anti-Patterns

- Code-first design (starting with implementation before understanding data)
- Shared database between services (coupling disguised as simplicity)
- Ignoring failure modes until production forces the conversation
- "It will scale" without specific characteristics

---

## The Deeper Purpose

Architecture is not about code. It's about **constraints that outlive implementation**. The data model is the geological layer. The architecture risk calculus forces the model to quantify the cost of wrong decisions before they're made. **Now it's quantified (risk score), certified (boundary integrity ), and verified (gates).** The best architecture is the one that survives its own failure modes.

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 1. It outputs:
```json
{
  "phase": 1,
  "skill": "system-architect",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: architecture_risk_calculus (5.0), data_model (3.0), boundary_map (3.0), failure_modes (3.0), scale_characteristics (2.0), boundary_integrity_ (4.0)
- Total complexity weight: 20.0

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: 0
- Assumption reversals: 0
- Architecture risks: [count if Risk > 0.5]

### Cognitive Traces Produced
- [x] Architecture Risk Calculus
- [x] Boundary Integrity 
- [ ] Decision Landscape

### Gates Verified
- [x] V1  [ ] V2  [x] V3  [x] V4  [x] V5  [ ] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From BOUNDARY-DETECTOR: Knowledge gaps → data model uncertainties
- From EXCAVATE: C2/C3 assumptions → architecture risks
- From EMERGENCE: Emergent behaviors → failure modes
- From TEMPORAL: Future scenarios → scale risks