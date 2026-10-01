# Changelog

All notable changes to depth-skills are documented here.

---

## 2026-10-02 — v2.1: Automatic Orchestration & Premium Architecture

### Major Release: Fully Automatic Orchestration + Premium Cognitive Architecture

### New Premium Skills Added (4)

| Codename | Internal Name | Version | Purpose |
|---|---|---|---|
| [`boundary-detector`](skills/ds-boundary-detector/SKILL.md) | Knowledge Boundary Probe | v1.0 | UnknownBench-style probes; detects voids before skills activate |
| [`meta-learning`](skills/ds-meta-learning/SKILL.md) | Cognitive Evolution Engine | v1.0 | Pattern extraction → skill synthesis → CONDUCTOR policy learning |
| [`verification-gates`](skills/ds-verification-gates/SKILL.md) | Depth Verification Engine | v1.0 | Final auditor: V1-V6 re-verification, ungameable gates, red-teaming, Depth Report |
| `ds-core` | Mathematical Framework | v1.0 | ADS, CEI, SI, EC, OV, CIM, RSM, Gates V1-V6, thinking parameters |

### CONDUCTOR v2.1 — Fully Automatic Orchestration

**Complete rewrite — now fully automatic:**
- **Auto-classifies tasks** — extracts complexity, consequence, reversibility, novelty, breadth, domain tags
- **Auto-assigns depth budget** — computes budget score, picks Budget A-D with ADS targets
- **Auto-selects skills** — maps task profile → skills using domain tags and characteristics
- **Auto-sequences with interference validation** — builds execution order, validates interference matrix
- **Auto-executes and logs** — tracks phase activation, CEI, SI, interference, gates
- **Auto-final validation** — computes ADS, verifies gates, checks CIM, recursive stability
- **Auto-generates Depth Report** — JSON output with all metrics, verdict, reproducibility
- **Auto-meta-learning** — extracts patterns, updates policy, runs regression checks
- **Auto-stops** — when ADS target met, diminishing returns, gates pass, ADS/CEI peaks

### All 19 Cognitive Skills Updated to v2.0

**Every cognitive skill enhanced with:**
- Mathematical depth metrics (ADS, CEI, SI, EC, OV, CIM, RSM)
- Recursive self-audit with RSM convergence detection
- Cognitive trace artifacts (heatmaps, graphs, landscapes, certificates)
- Verification gates (V1-V6) with machine-checkable criteria
- Interference requirements (provides/receives with minimum ADS gains)
- Thinking parameters with presets (quick/standard/deep/forensic)
- MATHEMATICS COMPLIANCE sections

**Per-skill highlights:**
- `deep-think` — Recursive audit, activation heatmap, assumption dependency graph, Gates V1-V3
- `adversary` — Recursive opposition, Constitutional critique, external grounding, Gates V3-V5
- `diverge` — MCTS exploration, CIM independence verification, transfer testing, decision landscape
- `excavate` — Sensitivity surfaces, counterfactual worlds, boundary probes, Gates V1-V2
- `reframe` — CIM-verified lens independence, invariant extraction, decision landscape
- `invert` — Sensitivity surfaces, belief network analysis, counterfactual worlds, robustness cert
- `contradict` — Claim graph, global coherence certificate, cascade analysis, Gates V1,V3,V5
- `provenance` — Calibration curves (ECE), epistemic audit trails, inflation detection, Gates V5,V6
- `fidelity` — Algorithmic fidelity diff, compression integrity certificate, Gates V1,V5,V6
- `negative-space` — Dimension completeness proofs, STRIDE security scan, 25-category failure taxonomy
- `temporal` — Regret surfaces, option value optimization, transition certificates, Gates V4,V6
- `threshold` — Reversal cost functions R(t), commitment certificates, early warning signals
- `anchor` — Drift quantification (cosine similarity), scope boundary certificate, Gates V1,V6
- `clarify` — Clarification calculus (II×UCL×PAP+DC), readiness certificate, Gates V1,V3
- `shallow` — Depth budget calculus, proportionality certificate, Gates V1,V6
- `teach` — Gap severity calculus (BF×0.5+RF×0.3+PF×0.2), teaching effectiveness cert
- `emergence` — Risk quantification (weighted factors), interaction topology certificate
- `descend` — Sensitivity surfaces, counterfactual worlds, derivation stack, Gates V1-V3
- `invert` — Sensitivity surfaces, belief network analysis, counterfactual worlds, robustness cert

### All 7 Domain Skills Updated to v2.0

| Skill | Key v2.0 Features |
|---|---|
| `product-engineer` | JTBD calculus, outcome verification certificate |
| `system-architect` | Architecture risk calculus, boundary integrity certificate |
| `copy-engineer` | Specificity calculus, conversion proof certificate |
| `api-designer` | DX calculus, contract integrity certificate |
| `mobile-engineer` | Mobile fitness calculus, mobile readiness certificate |
| `performance-engineer` | Optimization ROI calculus, optimization certificate |
| `refactor-engineer` | Refactor safety calculus, refactor certificate |

### Benchmarking Framework

- `benchmark/run.py` — Runs prompts with explicit version control (v1.x vs v2.x)
- `benchmark/score.py` — Computes ADS, CEI, SI, EC, OV, composite, qualitative deltas
- `benchmark/report.py` — Generates markdown reports with per-category breakdowns
- `benchmark/params_standard.json` / `params_deep.json` — Thinking parameter presets
- `tests/test_prompts.json` — 8 test cases across 7 categories

### Benchmark Results (v1.x vs v2.x)

| Metric | Old (v1.x) | Premium (v2.x) | Delta |
|---|---:|---:|---:|
| **ADS** | 0.23 | 1.41 | **+1.179 (+507%)** |
| **CEI** | 0.18 | 4.43 | **+4.25** |
| **SI** | 0.33 | 17.33 | **+17.0** |
| **EC** | 0.35 | 0.70 | **+0.35** |
| **Composite** | 19.5 | 78.0 | **+58.5 (+300%)** |

---

## 2026-06-11 — v1.2: Cognitive Completeness

### New Skills Added (3)

| Codename | Internal Name | Version | Purpose |
|---|---|---|---|
| [`clarify`](skills/ds-clarify/SKILL.md) | Ask/Answer Decision Engine | v1.1 | Decides when to ask clarifying questions vs proceed with answer |
| [`shallow`](skills/ds-shallow/SKILL.md) | Proportional Depth Protocol | v1.1 | Prevents overthinking on low-stakes tasks — opposite of deep-think |
| [`teach`](skills/ds-teach/SKILL.md) | Feynman Gap Detection | v1.1 | Uses explanation to detect knowledge gaps before delivery |

### Improvements

**Conductor updates:**
- Expanded skill selection table to include new skills
- Added slots for more skills in orchestration sequence
- Updated to recognize clarify, shallow, and teach triggers

**Library updates:**
- Updated skill count from 16 → 19 cognitive skills
- Updated README to reflect new skills and recommend conductor as starting point
- Version aligned new skills to v1.1 for consistency

### Gap Analysis Addressed

This release addresses gaps identified in the v1.1 audit:
- **Overthinking:** Now handled by `shallow`
- **Clarification:** Now handled by `clarify`  
- **Knowledge gaps:** Now handled by `teach`

---

## 2026-04-12 — v1.1: FORGE Refinement

### All 16 Skills Upgraded v1.0 → v1.1

Applied FORGE methodology across the entire library. Key improvements:

**Structural changes (all skills):**
- Every step now produces a **named written artifact** (not "consider X" but "write X")
- Step outputs are **chained** — each step references artifacts from previous steps, making skipping structurally impossible
- **Specificity anchors** added: "for THIS specific problem/answer/system" to prevent generic filler
- **Failure Mode** sections rewritten as recognizable mid-generation patterns (not abstract philosophy)
- Philosophy padding cut to minimum — every word earns its place

**Per-skill highlights:**
- `deep-think` — Steps explicitly numbered as artifact-producing, compression test added to Step 6
- `adversary` — Five mandatory attacks with evidence/consequence template; anti-fake rule requiring reference to specific content; dismissal rules requiring evidence not confidence
- `diverge` — Divergence verification test added; 5-scenario stress test per path; contrarian path has mechanism for finding shared assumptions
- `descend` — Pattern identification card (conscious vs unconscious); precondition table with minimum-3 check; derivation layers require explicit "Justified by" clause
- `excavate` — Deep Layer now has five specific answered questions; resolution log requires evidence for verify/flag/design-around
- `invert` — Constraints require source attribution; beliefs require evidence BOTH directions; counterfactual similarity diagnostic
- `reframe` — Lens selection table with "Use When" guidance; anti-contamination rule; cross-frame analysis structured as invariants/contradictions/unique-insights
- `negative-space` — Dimension scan requires written assessment per absent item; failure category scan formalized; silence report categorizes gaps into critical/acknowledged/N/A
- `contradict` — Claim extraction requires section references and minimum count; seven contradiction pattern scan
- `provenance` — Confidence formula simplified to three intuitive ratings; guess inflation audit with five common inflation zones
- `fidelity` — Five tag types formalized; natural compression then explicit diff; restore-or-justify per tag
- `anchor` — Anchor requires user's exact words quoted; chain-length diagnostic with thresholds; recovery requires naming drift pattern
- `threshold` — Gates require written evidence for PASS; depth requirement links to other skills; Category 1 explicitly skips remaining steps
- `emergence` — Designed vs hidden interaction distinction; feedback loops classified as stabilizing/amplifying; peak contention calculation
- `temporal` — Rate of change requires specific examples; regret test includes severity × likelihood; transition design requires trigger conditions
- `conductor` — Budget assignment requires written reasoning; per-skill justification; diminishing returns check

---

## 2026-04-12 — v1.0: Initial Release

### Structure
- Established 5-tier architecture: Cognition, Excavation, Integrity, Governance, Systems + Meta
- Separated cognitive-mode skills (`skills/`) from domain process skills (`domain/`)
- Created codename + internal name + version system for all skills

### Cognitive Skills (16)

| Codename | Internal Name | Version | Tier |
|---|---|---|---|
| `deep-think` | The Depth Protocol | 1.0 | Cognition |
| `adversary` | Self-Opposition Engine | 1.0 | Cognition |
| `diverge` | Path Divergence | 1.0 | Cognition |
| `descend` | Pattern Audit & First-Principles Derivation | 1.0 | Cognition |
| `excavate` | Assumption Archaeology | 1.0 | Excavation |
| `invert` | Constraint & Belief Inversion | 1.0 | Excavation |
| `reframe` | Representation Multiplier | 1.0 | Excavation |
| `negative-space` | Absence Detector | 1.0 | Excavation |
| `contradict` | Coherence Auditor | 1.0 | Integrity |
| `provenance` | Evidence Tagger & Confidence Calibrator | 1.0 | Integrity |
| `fidelity` | Compression Integrity Verifier | 1.0 | Integrity |
| `anchor` | Objective Drift Detector | 1.0 | Governance |
| `threshold` | Commitment Gateway | 1.0 | Governance |
| `emergence` | Interaction-Level Analyzer | 1.0 | Systems |
| `temporal` | Cross-Time Reasoner | 1.0 | Systems |
| `conductor` | Skill Orchestration Layer | 1.0 | Meta |

### Domain Skills (7)
- `product-engineer`, `system-architect`, `copy-engineer`, `api-designer`, `mobile-engineer`, `performance-engineer`, `refactor-engineer`

### Core Vocabulary Established
- Premature closure, convergence pressure, pattern gravity, lateral inhibition, local optimum, activation depth, coherence trap, cognitive inertia, attentional blindspot, epistemic flattening

### Merged Skills (from pre-v1.0 development)
- `evidence-ledger` + `epistemic-calibration` → `provenance`
- `termination-governor` + `irreversibility-governor` → `threshold`
- `constraint-inversion` + `counterfactual-stressor` → `invert`
- `analogy-breaker` + `first-principles-descent` → `descend`