# Changelog

All notable changes to depth-skills are documented here.

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
