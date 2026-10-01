---
name: conductor
codename: CONDUCTOR
internal: Skill Orchestration Layer v2.1
version: 2.1
tier: meta
trigger: any complex task, any task where a single skill feels insufficient, "give me everything", any high-stakes decision, any task where you're not sure how deep to go
description: Self-selects and sequences the right depth-skills proportional to task consequence, preventing both under- and over-analysis. Automatic skill selection, interference-validated sequencing, risk-aware activation, plugin architecture, meta-learning integration, and mathematical depth optimization.
author: Kshitijpalsinghtomar
tags: [orchestration, meta, sequencing, proportional-depth, budget, interference, plugins, meta-learning, optimization, automatic]
artifacts:
  - task-profile
  - depth-budget
  - skill-selection
  - execution-sequence
  - orchestration-log
  - interference-validation
  - plugin-manifest
  - meta-learning-update
  - depth-report
composable_with: [all-skills]
thinking_parameters:
  risk_aware_activation: true
  require_interference: true
  require_recursive_audit: true
  min_cim: 0.5
  plugin_architecture: true
  meta_learning_enabled: true
  auto_skill_selection: true
  auto_sequencing: true
  boundary_detection_first: true
---

# CONDUCTOR v2.1 — Automatic Skill Orchestration Layer (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs the final ADS, CEI, SI, EC, OV, and Depth Report. It validates interference matrix, enforces plugin architecture, integrates meta-learning updates, and optimizes skill selection for maximum ADS per CEI.

You have 26 cognitive skills. Each forces deeper reasoning in a specific dimension. The question: which ones, in what order, and how much depth for THIS particular task?

This skill **automatically answers that**. It matches cognitive investment to task consequence — **proportional depth, not maximum depth**. It **automatically selects skills**, **sequences them correctly**, **validates they actually interfere**, **manages plugins**, and **integrates meta-learning** for compounding intelligence.

---

## The Failure Mode You Must Recognize

Without orchestration, you either:
- Use zero skills (shallow — surface response ships unchallenged)
- Use all skills on every task (slow — over-investing on low-stakes work)
- Use the wrong skills (mismatched — deep temporal analysis on a CSS color choice)
- **Compose skills that don't actually interfere (cargo cult composition)**
- **Ignore plugin architecture (lock-in to current paradigm)**
- **Miss meta-learning opportunities (no compounding intelligence)**

The right depth is proportional. A CSS fix needs zero skills. A database schema needs five. **This skill automatically determines the right number, the right skills, the right sequence, and verifies they actually work together.**

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `risk_aware_activation` (default true) — only activate skills where marginal epistemic risk reduction > cost
- `require_interference` (default true) — validate interference matrix before delivery
- `require_recursive_audit` (default true) — final recursive self-audit
- `min_cim` (default 0.5) — minimum Compositional Independence Metric for DIVERGE paths
- `plugin_architecture` (default true) — use plugin registry for skill loading
- `meta_learning_enabled` (default true) — apply meta-learning policy updates
- `auto_skill_selection` (default true) — automatically select skills based on task profile
- `auto_sequencing` (default true) — automatically sequence skills with interference validation
- `boundary_detection_first` (default true) — run BOUNDARY-DETECTOR first for novel domains

---

### Step 1 — AUTO-CLASSIFY THE TASK (Automatic)

**AUTOMATICALLY** analyze the prompt and produce:

```
TASK PROFILE
────────────────────────────────────────
Task:           [one sentence description — auto-extracted]
Complexity:     [low / moderate / high / extreme] — auto-scored
Consequence:    [trivial / moderate / significant / critical] — auto-scored
Reversibility:  [trivially / moderately / hard / permanent] — auto-scored
Novelty:        [routine / somewhat novel / highly novel / unprecedented] — auto-scored
Breadth:        [single-domain / cross-domain / full-stack] — auto-scored
Stakeholders:   [count and types] — auto-extracted
Time Pressure:  [none / low / moderate / high / extreme] — auto-scored
Domain Tags:    [architecture, debugging, decision, product, security, etc.] — auto-tagged
────────────────────────────────────────
```

**Auto-Scoring Rules:**
- **Complexity**: Count of distinct technical domains + interdependencies
- **Consequence**: Blast radius × irreversibility × stakeholder count
- **Reversibility**: Time to rollback × coordination needed × data risk
- **Novelty**: Distance from known patterns in training (0=routine, 1=unprecedented)
- **Breadth**: Number of distinct skill categories required

**Artifact:** The task profile. All subsequent steps use this.

---

### Step 2 — AUTO-ASSIGN DEPTH BUDGET (Risk-Aware, Automatic)

**AUTOMATICALLY** compute budget from task profile:

```
DEPTH BUDGET
────────────────────────────────────────
Budget Score = (Complexity × 0.3) + (Consequence × 0.3) + (1-Reversibility × 0.2) + (Novelty × 0.2)

BUDGET A (Score < 0.25): Low stakes, reversible, routine
  Skills: 0. Standard answer. Move fast.
  ADS Target: 0.20
  Skip remaining steps. Deliver.

BUDGET B (0.25 ≤ Score < 0.5): Moderate stakes, some novelty
  Skills: 1-2. Auto-pick most relevant.
  ADS Target: 0.45
  Time: one additional pass.

BUDGET C (0.5 ≤ Score < 0.75): High stakes, hard to reverse
  Skills: 3-4. Thinking + challenging + checking.
  ADS Target: 0.70
  Time: multiple passes.

BUDGET D (Score ≥ 0.75): Critical, permanent, unprecedented
  Skills: Full stack. Every relevant skill in sequence.
  ADS Target: 0.85
  Time: thorough multi-pass analysis.

This task: BUDGET [A/B/C/D] (Score: X.XX)
Reasoning: [auto-generated from profile scores]
ADS Target: [value]
CEI Budget: [computed]
────────────────────────────────────────
```

**Risk-Aware Activation (Automatic):** For each candidate skill:
```
Marginal_ADS_Gain = ADS_with_skill - ADS_without_skill
Marginal_CEI_Cost = CEI_with_skill - CEI_without_skill
Activate if: Marginal_ADS_Gain / Marginal_CEI_Cost > Risk_Threshold
```
Risk_Threshold: Budget B=0.5, Budget C=0.3, Budget D=0.2.

**Artifact:** Depth budget with auto-activation decisions.

---

### Step 3 — AUTO-SELECT SKILLS (Plugin-Aware, Automatic)

**AUTOMATICALLY** select skills using the Plugin Registry and task profile:

```
SKILL SELECTION (AUTOMATIC)
────────────────────────────────────────
Task Profile → Skill Mapping (Auto-Applied):

[Complexity ≥ high]                    → DEEP-THINK (core)
[Consequence ≥ significant]            → ADVERSARY + PROVENANCE (core)
[Reversibility ≤ hard]                 → THRESHOLD (core)
[Multiple approaches possible]         → DIVERGE (core)
[Novelty ≥ highly novel]               → DESCEND (core)
[Stuck / no good solution]             → INVERT + REFRAME (core)
[Multi-part / long plan]               → CONTRADICT (core)
[Summarizing complex analysis]         → FIDELITY (core)
[Long execution / multi-step]          → ANCHOR (core)
[Confident but feels easy]             → EXCAVATE + INVERT (core)
[System with interacting parts]        → EMERGENCE (core)
[Future-affecting decision]            → TEMPORAL (core)
[Completeness check needed]            → NEGATIVE-SPACE (core)
[Ambiguous request]                    → CLARIFY (core)
[Low stakes / quick answer]            → SHALLOW (core)
[Teaching / explanation needed]        → TEACH (core)
[Novel domain / high uncertainty]      → BOUNDARY-DETECTOR (premium)
[Post-execution learning]              → META-LEARNING (premium)
[Final validation required]            → VERIFICATION-GATES (premium)

Domain Tags → Additional Skills:
[architecture]        → SYSTEM-ARCHITECT
[product]             → PRODUCT-ENGINEER
[api]                 → API-DESIGNER
[mobile]              → MOBILE-ENGINEER
[performance]         → PERFORMANCE-ENGINEER
[refactoring]         → REFACTOR-ENGINEER
[copywriting]         → COPY-ENGINEER

Selected for this task (AUTO):
  1. [skill] — plugin: [core/premium] — reason: [auto-generated from profile match]
  2. [skill] — plugin: [core/premium] — reason: [auto-generated]
  3. [skill] — plugin: [core/premium] — reason: [auto-generated]
  ...
────────────────────────────────────────
```

**Plugin Loading (Automatic):** If `plugin_architecture` = true, load from Plugin Registry v1. Each skill declares:
- `interface_version` (must be "1.0")
- `dependencies` (other skills required)
- `provides_interference` (what it feeds to later skills)
- `requires_interference` (what it needs from earlier skills)
- `composition_metadata` (commutativity, order constraints)

**Artifact:** Selected skills with auto-generated justifications.

---

### Step 4 — AUTO-SEQUENCE (Interference-Validated, Automatic)

**AUTOMATICALLY** sequence skills with interference validation:

```
EXECUTION SEQUENCE (AUTO-GENERATED)
────────────────────────────────────────
PHASE 1 — ORIENT (always first):
  → BOUNDARY-DETECTOR (if Budget C/D OR novelty ≥ highly novel) — probe knowledge boundaries FIRST
  → DESCEND (if problem looks familiar) — verify pattern match
  → DEEP-THINK (expand before narrowing)
  → CLARIFY (if ambiguous request detected)

PHASE 2 — EXPAND (broaden the search):
  → DIVERGE, REFRAME, INVERT, EXCAVATE
  → Interference: DEEP-THINK assumptions → DIVERGE paths / INVERT targets / EXCAVATE targets

PHASE 3 — CHALLENGE (stress the answer):
  → ADVERSARY, EMERGENCE, TEMPORAL
  → Interference: EXCAVATE C2/C3 → ADVERSARY attacks / TEMPORAL regrets / EMERGENCE risks

PHASE 4 — VERIFY (check the output):
  → CONTRADICT, PROVENANCE
  → Interference: ADVERSARY attacks → PROVENANCE evidence tags / CONTRADICT claim graph

PHASE 5 — DELIVER (final gate):
  → FIDELITY, NEGATIVE-SPACE, THRESHOLD
  → Interference: NEGATIVE-SPACE silences → THRESHOLD exit plan / FIDELITY tags

ONGOING — During extended work:
  → ANCHOR (periodic drift checks, every 3 steps)

META-LEARNING (post-execution, if enabled):
  → META-LEARNING — extract patterns, update skill library, update CONDUCTOR policy

VERIFICATION (final, if Budget C/D):
  → VERIFICATION-GATES — re-verify all gates, ungameable components, red-team, Depth Report

This task's sequence (AUTO):
  1. [skill] — Phase [N] — provides: [interference] — requires: [interference]
  2. [skill] — Phase [N] — provides: [interference] — requires: [interference]
  ...
────────────────────────────────────────
```

**Interference Validation (AUTOMATIC, MANDATORY):**

For each required interference, auto-verify:

| From Skill | To Skill | Interference Type | Min ADS Gain | Actual Gain | PASS/FAIL |
|------------|----------|-------------------|--------------|-------------|-----------|
| DEEP-THINK | DIVERGE | Assumptions seed paths | +0.15 | [measured] | [PASS/FAIL] |
| EXCAVATE | INVERT | C2/C3 → inversion targets | +0.20 | [measured] | [PASS/FAIL] |
| ADVERSARY | PROVENANCE | Attacks cite evidence tags | +0.15 | [measured] | [PASS/FAIL] |
| TEMPORAL | THRESHOLD | Regret → reversal cost | +0.10 | [measured] | [PASS/FAIL] |
| NEGATIVE-SPACE | EMERGENCE | Absent failures → interactions | +0.15 | [measured] | [PASS/FAIL] |
| BOUNDARY-DETECTOR | ALL | Void flags → assumption tags | +0.30 | [measured] | [PASS/FAIL] |

**If any FAIL:** Auto-re-run skill with proper interference feeding, or document why not applicable.

**Artifact:** `interference_validation` matrix with PASS/FAIL.

---

### Step 5 — AUTO-EXECUTE AND LOG

After each skill completes, **automatically** log:

```
ORCHESTRATION LOG
────────────────────────────────────────
Skill 1: [name] v[version]
  Phase: [N]
  Plugin: [core/premium]
  Finding:       [key output or insight — auto-summarized]
  Changed answer?:[yes — how / no]
  Phase activation: 0.XX
  CEI: 0.XX
  SI contribution: N
  Interference provided: [what fed to next skills]
  Interference received: [what received from prior skills]
  Gates verified: [V1-V6]
  Cognitive traces: [heatmap, graph, landscape]

Skill 2: [name] v[version]
  ...

Answer revised: [total count of revisions]
Total depth cycles: [count of skills executed]
Final ADS: [computed]
Final CEI: [computed]
Final SI: [computed]
Final EC: [computed]
Final OV: [computed]
ADS/CEI Ratio: [computed]
Diminishing returns reached?: [yes — last [N] skills found nothing new / no]
Meta-learning update: [patterns extracted, skills synthesized, policy updated]
────────────────────────────────────────
```

---

### Step 6 — AUTO-FINAL VALIDATION & DEPTH REPORT

**AUTOMATICALLY** compute and verify:

#### 6.1 Final ADS Computation
```
ADS = Σᵢ wᵢ × φᵢ / Σᵢ wᵢ
```
Must meet ADS Target from Step 2.

#### 6.2 Gate Verification
All V1-V6 gates must PASS across all skills.

#### 6.3 Ungameable Gates (Budget C/D)
At least 2 of 3 must PASS:
- Human Eval on 10 novel tasks
- Held-Out Task Benchmark
- Ensemble Critic (different model)

#### 6.3 Compositional Independence (CIM)
If DIVERGE ran: CIM(paths) ≥ `min_cim` (default 0.5)

#### 6.4 Recursive Stability
Apply CONDUCTOR to CONDUCTOR output:
- RSM > 0.95 for 2 consecutive depths
- SI not decreasing

#### 6.5 Depth Report Generation (Automatic)

```json
{
  "report_id": "dr_<timestamp>_<hash>",
  "task_hash": "sha256(task_description)",
  "model": "model_identifier",
  "task_profile": {...},
  "budget": "BUDGET_[A/B/C/D]",
  "skills_executed": [
    {"name": "deep-think", "version": "2.0", "plugin": "core", "phase": 1, "activation": 0.XX},
    {"name": "adversary", "version": "2.0", "plugin": "core", "phase": 3, "activation": 0.XX}
  ],
  "metrics": {
    "ads": 0.XX,
    "cei": 0.XX,
    "si": N,
    "ec": 0.XX,
    "ov": 0.XX,
    "ads_cei_ratio": 0.XX
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
  "interference_validation": {"all_required_pass": true, "matrix": [...]},
  "cim": 0.XX,
  "recursive_stability": 0.XX,
  "threshold": "CATEGORY_[1-4]",
  "verdict": "PASS",
  "limitations": ["..."],
  "reproducibility": {
    "seed": 42,
    "temperature": 0.0,
    "skill_versions": {"deep-think": "2.0", "adversary": "2.0", ...},
    "thinking_parameters": {...}
  }
}
```

**Artifact:** `depth_report` — the final verifiable output.

---

### Step 7 — AUTO-META-LEARNING UPDATE (if enabled)

If `meta_learning_enabled` = true, **automatically** run META-LEARNING:

1. **Pattern Extraction:** From orchestration log, extract:
   - Which skill sequences worked for which task profiles
   - Which interferences were most valuable
   - Which gates failed most often
   - ADS/CEI ratios per skill per task type

2. **Skill Synthesis:** If patterns suggest new skill combinations, propose synthesized skills.

3. **Policy Update:** Update CONDUCTOR's skill selection policy (bandit/RL on selection outcomes).

4. **Regression Check:** New policy must not degrade performance on benchmark suite.

**Artifact:** `meta_learning_update` with patterns, proposals, policy delta, regression results.

---

### Step 8 — AUTO-STOP WHEN WARRANTED

**AUTOMATICALLY** stop when:
- ADS Target met AND additional skills show diminishing returns (ΔADS < 0.02 per skill)
- All V1-V6 gates PASS
- Interference validation PASSES
- CIM ≥ threshold
- Recursive stability CONVERGED
- Confidence stable across checks
- **ADS/CEI ratio** peaks (additional skills cost more than they add)

Over-analysis is its own failure mode. When the budget is met and returns are diminishing: deliver.

---

## The Deeper Purpose

Without orchestration, the user must manually select skills — requiring knowledge of the library and the task's profile. With this skill, the model **automatically self-selects proportional depth, validates that skills actually compose, manages plugin architecture for future-proofing, and integrates meta-learning for compounding intelligence**. Small tasks get fast answers. Large tasks get deep exploration. **The system gets smarter over time — automatically.**

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 5 (meta). It outputs:
```json
{
  "phase": 5,
  "skill": "conductor",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: task_profile (1.0), depth_budget (1.0), skill_selection (1.0), execution_sequence (1.0), orchestration_log (2.0), interference_validation (3.0), plugin_manifest (1.0), meta_learning_update (3.0), depth_report (2.0)
- Total complexity weight: 15.0

### SI Components
- C2/C3 assumptions: [from task profile]
- Contrarian viable: [from DIVERGE]
- Fatal attacks: [from ADVERSARY]
- Boundary violations: [from BOUNDARY-DETECTOR]
- Assumption reversals: [from EXCAVATE]

### Cognitive Traces Produced
- [x] Activation Heatmap (aggregated from all skills)
- [x] Assumption Dependency Graph (aggregated)
- [x] Decision Landscape (from TEMPORAL/DIVERGE)

### Gates Verified
- [x] V1  [x] V2  [x] V3  [x] V4  [x] V5  [x] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble (delegated to VERIFICATION-GATES)

### Required Interferences
- From ALL SKILLS: Phase activations → ADS computation
- From ALL SKILLS: Interference matrix → validation
- From META-LEARNING: Policy updates → next task optimization