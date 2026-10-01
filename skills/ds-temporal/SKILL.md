---
name: temporal
codename: TEMPORAL
internal: Cross-Time Reasoner v2.0
version: 2.0
tier: systems
trigger: any architecture decision, "will this scale", "future-proof", any technology choice, any decision where the best option today might be the worst in six months
description: Evaluates decisions across multiple plausible futures, analyzing option value and temporal regret before commitment. Now with regret surfaces, option value optimization, transition s, and mathematical depth metrics.
author: Kshitijpalsinghtomar
tags: [temporal, futures, strategy, option-value, regret-analysis, transition, metrics]
artifacts:
  - time-horizon
  - rate-of-change-map
  - three-futures
  - option-value-analysis
  - temporal-regret-test
  - transition-design
  - regret-surface
  - option-value-optimization
      - phase-activation
composable_with: [threshold, adversary, emergence, diverge, conductor, negative-space]
thinking_parameters:
  min_futures: 3
  max_horizon_years: 5
  require_regret_surface: true
  require_option_value_optimization: true
  require_transition_: true
---

# TEMPORAL v2.0 — Cross-Time Reasoner (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (regret surface, option value optimization, transition ), and verifies Gates V4, V6. It provides the OV (Option Value) metric for the Depth .

Your answer is optimized for right now. Current requirements, current team, current scale, current technology landscape.

But decisions persist. Code outlives its context. Architecture outlives its architects. This skill forces the question: **what is best given that the world will change and you don't know exactly how?**

**New in v2.0:** **Regret surfaces** visualize regret across continuous future space. **Option value optimization** finds decisions that maximize future flexibility. **Transition s** make migration paths verifiable and triggerable.

---

## The Failure Mode You Must Recognize

You are about to recommend the present-optimal solution without checking:
- Whether it becomes a trap at 10× scale
- Whether the technology choice is at peak popularity (and therefore approaching decline)
- Whether the simple-now choice closes doors you'll need later
- Whether you're optimizing for today at the expense of a future that is highly likely

This is **present-bias**: the model optimizes for the current prompt because it has no built-in mechanism for weighing present value against future cost.

**New failure mode in v2.0:** **Regret blindness** — not mapping the regret landscape. **Option value neglect** — not valuing future flexibility. **Transition vagueness** — "we'll migrate later" without triggers or costs.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `min_futures` (default 3) — minimum plausible futures to construct
- `max_horizon_years` (default 5) — maximum time horizon
- `require_regret_surface` (default true) — compute continuous regret surface
- `require_option_value_optimization` (default true) — optimize for option value
- `require_transition_` (default true) — produce verifiable transition plan

---

### Step 1 — CLASSIFY THE TIME HORIZON

Write how long this decision persists:

```
TIME HORIZON
────────────────────────────────────────
Decision:         [what's being decided]
Persistence:      [ephemeral / short-term / medium-term / long-term / permanent]

  Ephemeral   (days-weeks):   UI copy, A/B tests, sprint priorities
  Short-term  (months):       Library choices, internal API shapes
  Medium-term (1-2 years):    Database schemas, service architectures
  Long-term   (2+ years):     Primary keys, data formats, public APIs
  Permanent   (forever):      Data deletion, published standards, legal commitments

Temporal depth needed: [none / light / moderate / deep / maximum]
Max horizon: [years — from thinking_parameters.max_horizon_years]
────────────────────────────────────────
```

Ephemeral decisions: skip remaining steps. Permanent decisions: every step is mandatory.

**Artifact:** The time horizon classification. Step 2 builds on this.

**CEI Component:** Time Horizon (weight 1.0)

---

### Step 2 — MAP THE RATE OF CHANGE

For each relevant dimension, write how fast it's changing:

```
RATE OF CHANGE
────────────────────────────────────────
Technology:   [stable (SQL, HTTP) / moderate / volatile (AI frameworks)]
              Specific: [which technologies are most relevant and their stability]
              Half-life: [estimated years until 50% obsolescence]

Requirements: [stable (banking) / moderate / volatile (startup)]
              Specific: [which requirements are most likely to change]
              Volatility Index: [0.0-1.0 — rate of requirement change]

Scale:        [linear growth / exponential / plateau / uncertain]
              Specific: [current volume and projected trajectory]
              Doubling Time: [months — if exponential]

Team:         [stable / growing / likely turnover]
              Specific: [what the team looks like in 12 months]
              Bus Factor: [how many people hold critical knowledge]

Competition:  [static / shifting]
              Specific: [what competitive changes could affect this]
              Disruption Probability: [0.0-1.0 per year]

Regulation:   [stable / evolving / uncertain]
              Specific: [what regulatory changes could affect this]
              Compliance Horizon: [years until next major change]

────────────────────────────────────────
```

High change rate → design for adaptability. Low change rate → design for efficiency.

**Artifact:** The rate of change map with quantified metrics.

**CEI Component:** Rate of Change Map (weight 2.0)

---

### Step 3 — CONSTRUCT PLAUSIBLE FUTURES (Minimum = `min_futures`)

Do not predict. Construct **at least `min_futures`** plausible futures:

```
FUTURE [N] — [NAME: Conservative / Growth / Disruption / Stagnation / Black Swan]
────────────────────────────────────────
Environment:       [specific changes from Step 2 — quantify where possible]
  Technology:      [specific changes]
  Requirements:    [specific changes]
  Scale:           [specific changes]
  Team:            [specific changes]
  Competition:     [specific changes]
  Regulation:      [specific changes]

This decision in [N]: [THRIVES / SURVIVES / DEGRADES / FAILS / CATASTROPHIC]
Why:               [specific reasoning with causal chain]

Probability:       [0.0-1.0 — subjective but reasoned]
Time to Manifest:  [months/years — when would we know?]
Early Indicators:  [observable signals this future is arriving]
────────────────────────────────────────
```

**Required Futures (minimum):**
1. **Conservative** — current trends continue
2. **Growth** — things go well (scale up, team grows, requirements expand)
3. **Disruption** — something fundamental changes (tech shift, market change, pivot)

**Additional Futures (for deeper analysis):**
4. **Stagnation** — growth stops, resources shrink
5. **Black Swan** — low-probability, high-impact event

**Artifact:** The futures with decision evaluation, probabilities, and early indicators.

**CEI Component:** Futures Construction (weight 3.0)

---

### Step 4 — REGRET SURFACE (if `require_regret_surface` = true)

**NEW IN v2.0** — Map regret across continuous future space, not just discrete futures.

```
REGRET SURFACE
────────────────────────────────────────
Decision Options: [list all options from DIVERGE interference]

For each option:
  Option: [name]
  Regret Function R(future) = Utility(best_in_future) - Utility(this_option_in_future)
  
  Regret across futures:
    Conservative:  [regret value]
    Growth:        [regret value]
    Disruption:    [regret value]
    Stagnation:    [regret value]
    Black Swan:    [regret value]
  
  Expected Regret: Σ P(future) × R(future) = [value]
  Max Regret:      max(R(future)) = [value] (worst-case)
  Regret Variance: Var(R(future)) = [value] (uncertainty)

Regret Surface Visualization:
  [For continuous future parameters, e.g., scale × time:
   Regret(option, scale, time) = ...]
────────────────────────────────────────
```

**Interpretation:**
- **Low Expected Regret** = good on average
- **Low Max Regret** = robust (minimax)
- **Low Regret Variance** = predictable

**Artifact:** `regret_surface` with regret functions, expected/max/variance, and visualization data.

**CEI Component:** Regret Surface (weight 5.0)

---

### Step 5 — OPTION VALUE OPTIMIZATION (if `require_option_value_optimization` = true)

**NEW IN v2.0** — Explicitly optimize for future flexibility.

```
OPTION VALUE OPTIMIZATION
────────────────────────────────────────
Decision Options: [list all options]

For each option:
  Option: [name]
  
  Opens (Future Options Enabled):
    [List specific future decisions this keeps open]
    Quantified: [Option Value = Σ P(future) × Value(enabled_option_in_future)]
  
  Closes (Future Options Foreclosed):
    [List specific future decisions this makes impossible/expensive]
    Quantified: [Option Cost = Σ P(future) × Cost(foreclosed_option_in_future)]
  
  Net Option Value: Opens - Closes = [value]
  Option Value Ratio: Opens / (Opens + Closes) = [0.0-1.0]

Option Value Advantage: [Option with highest Net Option Value]
  Because: [specific — which foreclosed option matters most]

Optimization Result:
  Present-Optimal Option: [name] — Net Option Value: [value]
  Future-Robust Option:   [name] — Net Option Value: [value]
  Recommendation: [Present-Optimal / Future-Robust / Hybrid with Transition]
────────────────────────────────────────
```

**Key Insight:** When the present-optimal closes more important options than an alternative, the alternative may be worth its present-moment cost — it preserves the ability to adapt.

**Artifact:** `option_value_optimization` with quantified opens/closes/net for each option.

**CEI Component:** Option Value Optimization (weight 5.0)

**OV Metric:** The Net Option Value of the recommended option becomes the **OV** for the Depth .

---

### Step 6 — TEMPORAL REGRET TEST

```
TEMPORAL REGRET TEST
────────────────────────────────────────
12 months from now, looking back:

Regret from present-optimal path:
  Scenario:   [in what future do you regret this?]
  Severity:   [how bad — minor / significant / catastrophic]
  Likelihood: [how likely is that future — from Step 3]

Regret from future-robust path:
  Scenario:   [what extra cost was paid now?]
  Severity:   [how bad]
  Likelihood: [certain — you pay the cost now regardless]

Worse regret: [which scenario — considering severity × likelihood]
Recommended:  [which path, given this analysis]
────────────────────────────────────────
```

**Artifact:** The temporal regret test.

**CEI Component:** Temporal Regret Test (weight 2.0)

---

### Step 7 — TRANSITION DESIGN (if present ≠ future optimal)

If the present-optimal and future-optimal are different:

```
TRANSITION DESIGN
────────────────────────────────────────
Start with:         [present-optimal — why it's OK for now]
Transition to:      [future-optimal — when it becomes necessary]
Trigger Condition:  [specific observable signal — NOT a calendar date]
  Primary Trigger:  [metric threshold, event, or milestone]
  Secondary Triggers: [backup signals]
  Monitoring Plan:  [how to detect triggers — dashboards, alerts, reviews]

Migration Cost:     [estimated effort, risk, downtime, data migration]
  Effort: [person-weeks]
  Risk: [LOW/MEDIUM/HIGH — what can go wrong]
  Downtime: [expected]
  Data Migration: [strategy, validation, rollback]

Escape Hatches:     [what to build NOW that makes migration cheaper later]
  1. [architectural decision — e.g., abstraction layer, interface segregation]
  2. [data decision — e.g., schema versioning, dual-write]
  3. [operational decision — e.g., canary deployment, feature flags]

Transition :
   ID: [unique]
  Valid Until: [date or condition]
  Review Cadence: [monthly/quarterly — when to reassess]
  Owner: [who owns the transition decision]
────────────────────────────────────────
```

**Artifact:** `transition_design` with trigger conditions, costs, escape hatches, and **transition **.

**CEI Component:** Transition Design (weight 4.0)

---

### Step 8 — TRANSITION  (if `require_transition_` = true)

**NEW IN v2.0** — Verifiable, triggerable transition commitment.

```
TRANSITION 
────────────────────────────────────────
 ID: tc_<timestamp>_<hash>
Decision: [what decision this covers]
Current State: [present-optimal choice]
Target State: [future-optimal choice]

Trigger Conditions (ALL must be met for auto-transition):
  1. [Metric] ≥ [Threshold] for [Duration]
  2. [Event] observed
  3. [Review] approval by [Role/Person]

Preconditions (must be true before transition):
  - [Escape hatch 1 implemented]
  - [Escape hatch 2 implemented]
  - [Migration tooling ready]
  - [Rollback tested]

Migration Plan:
  Phase 1: [steps, timeline, validation]
  Phase 2: [steps, timeline, validation]
  Phase 3: [steps, timeline, validation]
  Rollback: [steps, timeline, validation]

Monitoring:
  Dashboard: [URL/name]
  Alerts: [list of alert rules]
  Review Cadence: [monthly/quarterly]

Expiration: [date or "until triggered"]
Owner: [role/person responsible]
Sign-off: [required approvals]
────────────────────────────────────────
```

**Artifact:** `transition_` — a verifiable, executable transition commitment.

---

### 9 — METRICS: Compute and Output Depth Metrics

#### 9.1 Phase Activation (for ADS)

```json
{
  "phase": 3,
  "skill": "temporal",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

#### 9.2 CEI Components

```json
{
  "cei_components": {
    "time_horizon": 1.0,
    "rate_of_change_map": 2.0,
    "futures_construction": 3.0,
    "regret_surface": 5.0,
    "option_value_optimization": 5.0,
    "temporal_regret_test": 2.0,
    "transition_design": 4.0,
    "transition_": 3.0,
    "total_complexity_weight": 25.0,
    "output_tokens": N,
    "wall_time_seconds": T,
    "cei": 0.XX
  }
}
```

#### 9.3 SI Components

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

#### 9.4 Cognitive Traces

**Regret Surface:**
```json
{
  "type": "regret_surface",
  "options": ["Option A", "Option B", "Option C"],
  "futures": ["Conservative", "Growth", "Disruption", "Stagnation", "Black Swan"],
  "regret_matrix": [
    [0.1, 0.3, 0.8, 0.2, 0.9],  # Option A regret per future
    [0.2, 0.1, 0.3, 0.1, 0.4],  # Option B
    [0.5, 0.4, 0.1, 0.3, 0.2]   # Option C
  ],
  "probabilities": [0.4, 0.3, 0.2, 0.05, 0.05],
  "expected_regret": [0.32, 0.18, 0.28],
  "max_regret": [0.9, 0.4, 0.5],
  "recommended": "Option B"
}
```

**Option Value Optimization:**
```json
{
  "type": "option_value_optimization",
  "options": [
    {"name": "Option A", "opens": 0.6, "closes": 0.8, "net": -0.2, "ratio": 0.43},
    {"name": "Option B", "opens": 0.9, "closes": 0.2, "net": 0.7, "ratio": 0.82},
    {"name": "Option C", "opens": 0.7, "closes": 0.4, "net": 0.3, "ratio": 0.64}
  ],
  "recommended": "Option B",
  "transition_from": "Option A",
  "transition_to": "Option B"
}
```

**Transition :** (as defined in Step 8)

#### 9.5 Depth  Contribution

```json
{
  "skill": "temporal",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": 0, "ec": 0.XX, "ov": 0.XX},
  "gates_verified": {"V4": true, "V6": true},
  "limitations": ["..."]
}
```

---

### 10 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V4** | Temporal Consistency | Chosen path survives (not catastrophic) in ≥2/3 futures |
| **V6** | Recursive Stability | If recursion: RSM > 0.95 ∧ SI not decreasing |

**If any gate FAILS:** Return to relevant step and fix. Do not deliver.

---

### 11 — INTERFERENCE: Receive and Provide

**Receive from prior skills:**

| From Skill | Interference | Use |
|------------|--------------|-----|
| DIVERGE | Path profiles | Evaluate each path across futures |
| ADVERSARY | Fatal attacks | Add as "catastrophic" future outcomes |
| EXCAVATE | C2/C3 assumptions | Test assumption validity across futures |

**Provide to later skills:**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| DIVERGE | Future profiles for stress testing | +0.15 |
| THRESHOLD | Regret scenarios → reversal cost | +0.10 |
| NEGATIVE-SPACE | Regret scenarios → failure categories | +0.10 |
| CONDUCTOR | OV metric, transition  | +0.15 |

**Artifact:** `interference_log` (received and provided).

---

## The Deeper Purpose

The model generates optimal snapshots — perfect for the present moment. But decisions live in time. This skill forces temporal reasoning: evaluating decisions not just by present-moment optimality but by **regret surfaces across continuous future space**, **option value optimization**, and **verifiable transition s**. This activates the model's knowledge of strategy, option theory, and scenario planning — knowledge that exists but is rarely triggered because prompts ask about the present, not the future. **Now it's quantified, optimized, and certified.**

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 3. It outputs:
```json
{
  "phase": 3,
  "skill": "temporal",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: time_horizon (1.0), rate_of_change_map (2.0), futures_construction (3.0), regret_surface (5.0), option_value_optimization (5.0), temporal_regret_test (2.0), transition_design (4.0), transition_ (3.0)
- Total complexity weight: 25.0

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: 0
- Assumption reversals: 0

### Cognitive Traces Produced
- [ ] Activation Heatmap
- [ ] Assumption Dependency Graph
- [x] Regret Surface
- [x] Option Value Optimization
- [x] Transition 

### Gates Verified
- [ ] V1  [ ] V2  [ ] V3  [x] V4  [ ] V5  [x] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From DIVERGE: Path profiles → future evaluation
- From ADVERSARY: Fatal attacks → catastrophic futures
- From EXCAVATE: C2/C3 assumptions → assumption validity across futures