# depth-skills v2.x

> **Skills that change how AI thinks, not just what steps it follows — now with mathematical depth metrics, automatic orchestration, and verifiable cognitive depth.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 26](https://img.shields.io/badge/Skills-26-brightgreen.svg)](#skill-reference)
[![Version: 2.1](https://img.shields.io/badge/Version-2.1-orange.svg)](CHANGELOG.md)
[![Benchmark: +300%](https://img.shields.io/badge/Benchmark-%2B300%25-success.svg)](benchmark/report.md)

An open-source **cognitive architecture** for AI agents. 26 skills that force language models past surface-level reasoning into genuine, measurable depth — not by adding process steps, but by structurally changing how the model searches its knowledge before answering.

---

## 🛑 The Problem: Premature Closure

Language models experience **premature closure**. A query arrives, a statistically likely answer forms, and the model outputs it — not because it explored deeply, but because **convergence pressure** rewarded early stopping.

The deeper pathways — connections between distant concepts, non-obvious framings, solutions requiring cross-domain synthesis — rarely activate. The model settles at 60-75% activation solely because nothing forces it deeper.

### Why existing solutions fail to stop this:

| Approach | What It Does | What It Doesn't Do |
|---|---|---|
| **Process libraries** (e.g. Superpowers) | Add workflow/pipeline steps | Change how the AI thinks *within* each step |
| **Tool integrations** (e.g. Playwright, AWS) | Connect to external computational systems | Improve the AI's internal reasoning quality |
| **Depth-skills v1.x** | Force structural cognitive constraints | Require manual skill selection & sequencing |
| **Depth-skills v2.x (This Release)** | **Forces structural cognitive constraints + automatic orchestration + mathematical verification** | **Nothing — it's the complete cognitive architecture** |

A skill like `deep-think` doesn't just add a review step. It blocks the answer from forming until deeper semantic pathways have been activated. `descend` doesn't merely criticize an answer — it verifies whether the problem was properly identified before any answer was even generated. **`conductor v2.1` now does all of this automatically.**

---

## 📈 The Evidence: Why Cognitive Depth Matters

Internal testing on complex architectural prompts demonstrates a **massive non-linear jump in reasoning depth** when skills are stacked side-by-side.

By applying multiple cognitive restraints simultaneously, we stop the AI from generating baseline tutorial-level answers and force it into strategic, multi-horizon thinking.

<p align="center">
  <img src="https://img.shields.io/badge/Control_Run_Score-2%2F10-red?style=for-the-badge" alt="Control Run 2/10"/>
  <img src="https://img.shields.io/badge/3_Skills_Stacked-8%2F10-yellow?style=for-the-badge" alt="3 Skills 8/10"/>
  <img src="https://img.shields.io/badge/5_Skills_Stacked-10%2F10-success?style=for-the-badge" alt="5 Skills 10/10"/>
  <img src="https://img.shields.io/badge/Premium_v2.x-Auto_Orchestrated-brightgreen?style=for-the-badge" alt="Premium v2.x Auto Orchestrated"/>
</p>

| Setup | Cognitive Behavior | Depth Score |
|:---|:---|:---:|
| **Control (0 Skills)** | Yields to *pattern gravity* and jumps straight to the most common engineering tutorial answer. | **2/10** |
| **v1.x (3 Skills)** | Audits assumptions using `PROVENANCE`, attacks baseline using `ADVERSARY`. Acts like a **Senior Developer**. | **8/10** |
| **v1.x (5 Skills)** | Reframes problem using `DEEP-THINK`, discovers contrarian architectures using `DIVERGE`. Acts like a **Staff Architect**. | **10/10** |
| **v2.x Premium (Auto)** | **Auto-selects, sequences, validates interference, runs boundary detection, runs meta-learning, verifies with ungameable gates.** Acts like a **Principal Engineer + QA Team**. | **10/10 (Auto)** |

**v2.x Benchmark Results (Old v1.x vs Premium v2.x):**

| Metric | Old (v1.x) | Premium (v2.x) | Delta |
|:---|:---:|:---:|:---:|
| **ADS** (Activation Depth Score) | 0.23 | 1.41 | **+1.179 (+507%)** |
| **CEI** (Cognitive Effort Index) | 0.18 | 4.43 | **+4.25** |
| **SI** (Surprise Index) | 0.33 | 17.33 | **+17.0** |
| **EC** (Epistemic Calibration) | 0.35 | 0.70 | **+0.35** |
| **Composite Score** | 19.5 | 78.0 | **+58.5 (+300%)** |

**Qualitative Dimensions (0-2):**
| Dimension | Old | Premium | Delta |
|---|---:|---:|---:|
| Surface Coverage | 1.0 | 2.0 | +1.0 |
| Hidden Dimensions | 0.0 | 2.0 | **+2.0** |
| Assumption Quality | 0.0 | 2.0 | **+2.0** |
| Alternative Paths | 0.0 | 2.0 | **+2.0** |
| Evidence Calibration | 0.0 | 2.0 | **+2.0** |

→ Read the full scoring breakdown, prompts, and case studies in [tests/RESULTS.md](tests/RESULTS.md) and [benchmark/report.md](benchmark/report.md)

---

## 🚀 Quick Start

```bash
# Install all skills
git clone https://github.com/Kshitijpalsinghtomar/depth-skills
cd depth-skills

# Or copy individual skills into your agent
cp -r skills/ds-conductor ~/.claude/skills/
```

**Recommended:** Start with `ds-conductor` v2.1 — it **automatically** selects appropriate skills based on task complexity, runs boundary detection first, sequences skills with interference validation, runs meta-learning post-execution, and verifies with ungameable gates. This gives you proportional depth **automatically**.

**Try it now:** Add the `ds-conductor` skill and ask it questions of varying complexity. Compare the depth of response.

→ Full setup guide: [QUICKSTART.md](QUICKSTART.md)

---

## ⚙️ Compatibility

These skills work natively with any AI agent or tool that accepts markdown instructions:

| Tool | How to Use | Skill Path |
|---|---|---|
| **Claude Code** | Copy to `~/.claude/skills/` | `skills/<name>/SKILL.md` |
| **Cursor** | Add to `.cursor/rules/` or paste into system prompt | `skills/<name>/SKILL.md` |
| **Gemini CLI** | Copy to `~/.gemini/skills/` | `skills/<name>/SKILL.md` |
| **GitHub Copilot** | Add to `.github/copilot-instructions/` | `skills/<name>/SKILL.md` |
| **Any LLM** | Paste skill content into system prompt or context | `skills/<name>/SKILL.md` |

---

## 🏛️ The Architecture v2.x

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PREMIUM COGNITIVE STACK v2.x                      │
├─────────────────────────────────────────────────────────────────────────────┤
│  USER INTERFACE                                                              │
│  ├── Thinking Parameter Dashboard (depth, rigor, recursion presets)        │
│  ├── Cognitive Trace Viewer (heatmaps, graphs, landscapes)                 │
│  ├── Verification Gate Status (green/red per gate)                         │
│  └── Reproducibility Export (JSON + narrative)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  ORCHESTRATION LAYER                                                         │
│  ├── CONDUCTOR v2.1 (auto-select, auto-sequence, auto-validate, auto-stop) │
│  ├── META-LEARNING (pattern extraction → skill synthesis → policy learning) │
│  └── PARAMETER ENGINE (presets: quick/standard/deep/forensic)              │
├─────────────────────────────────────────────────────────────────────────────┤
│  COGNITIVE SKILLS (Enhanced v2.0)                                           │
│  ├── DEEP-THINK + METRICS + RECURSION + VISUALIZATION + GATES              │
│  ├── ADVERSARY + RECURSIVE_OPPOSITION + CONSTITUTIONAL + UNGAMEABLE        │
│  ├── DIVERGE + MCTS_EXPLORATION + CIM + TRANSFER_TEST                      │
│  ├── EXCAVATE + SENSITIVITY_SURFACE + COUNTERFACTUAL_WORLDS + BOUNDARY     │
│  ├── INVERT + SENSITIVITY_SURFACE + BELIEF_NETWORK + ROBUSTNESS_CERT       │
│  ├── REFRAME + CIM + INVARIANT_EXTRACTION + DECISION_LANDSCAPE             │
│  ├── NEGATIVE-SPACE + COMPLETENESS_PROOF + SECURITY_SCAN + FAILURE_TAXONOMY│
│  ├── CONTRADICT + CLAIM_GRAPH + COHERENCE_CERT + GATES                     │
│  ├── PROVENANCE + CALIBRATION_CURVES + AUDIT_TRAIL + INFLATION_DETECTION   │
│  ├── TEMPORAL + REGRET_SURFACE + OPTION_VALUE + TRANSITION_CERT            │
│  ├── THRESHOLD + REVERSAL_COST_FUNCTION + COMMITMENT_CERT + EWI            │
│  ├── BOUNDARY-DETECTOR (UnknownBench probes, void detection, gates all)    │
│  ├── META-LEARNING (pattern extraction, skill synthesis, policy learning)  │
│  └── VERIFICATION-GATES (V1-V6 + ungameable + red-team + Depth Report)     │
├─────────────────────────────────────────────────────────────────────────────┤
│  DOMAIN SKILLS (Enhanced v2.0)                                              │
│  ├── PRODUCT-ENGINEER (JTBD calculus, outcome verification)                │
│  ├── SYSTEM-ARCHITECT (architecture risk calculus, boundary integrity)     │
│  ├── COPY-ENGINEER (specificity calculus, conversion proof)                │
│  ├── API-DESIGNER (DX calculus, contract integrity)                        │
│  ├── MOBILE-ENGINEER (mobile fitness calculus, readiness cert)             │
│  ├── PERFORMANCE-ENGINEER (ROI calculus, optimization cert)                │
│  └── REFACTOR-ENGINEER (safety calculus, refactor cert)                    │
├─────────────────────────────────────────────────────────────────────────────┤
│  VERIFICATION ENGINE                                                         │
│  ├── Gates V1-V6 (machine-checkable)                                       │
│  ├── Ungameable Gates (human eval, held-out, ensemble critic)              │
│  ├── Red-Team Gate (active gaming detection)                               │
│  └── Depth Report Generator (cryptographically signed)                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  INFRASTRUCTURE                                                              │
│  ├── Plugin Registry v1 (frozen interface, versioned, sandboxed)           │
│  ├── Skill Runtime (tool registry, tool calls, execution traces)           │
│  ├── Benchmark Suite (standardized prompts, statistical testing)           │
│  └── SDK/API for programmatic orchestration                                │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🧰 Skill Reference v2.x

Every skill has a **codename** (what you invoke), an **internal name** (what it does), and a **version**.

### 1. Cognition — How to search deeper

| Codename | Internal Name | Version | Trigger |
|---|---|---|---|
| [`deep-think`](skills/ds-deep-think/SKILL.md) | The Depth Protocol | v2.0 | Complex problem, "go deeper", any task where the first answer is too easy |
| [`adversary`](skills/ds-adversary/SKILL.md) | Self-Opposition Engine | v2.0 | Any significant decision, any plan before execution |
| [`diverge`](skills/ds-diverge/SKILL.md) | Path Divergence | v2.0 | "What's the best way to", any architectural choice |
| [`descend`](skills/ds-descend/SKILL.md) | Pattern Audit & First-Principles Derivation | v2.0 | "Nothing works", familiar solution feels wrong, novel problems |
| [`clarify`](skills/ds-clarify/SKILL.md) | Ask/Answer Decision Engine | v2.0 | Ambiguous request, missing context, "should I ask or answer" |
| [`shallow`](skills/ds-shallow/SKILL.md) | Proportional Depth Protocol | v2.0 | Low-stakes task, "keep it simple", quick answer needed |
| [`teach`](skills/ds-teach/SKILL.md) | Feynman Gap Detection | v2.0 | "explain like I'm 5", test my understanding |

### 2. Excavation — What to dig for

| Codename | Internal Name | Version | Trigger |
|---|---|---|---|
| [`excavate`](skills/ds-excavate/SKILL.md) | Assumption Archaeology | v2.0 | "What am I assuming", high-stakes plans |
| [`invert`](skills/ds-invert/SKILL.md) | Constraint & Belief Inversion | v2.0 | "We have no choice", "are we sure", boxed-in tradeoffs |
| [`reframe`](skills/ds-reframe/SKILL.md) | Representation Multiplier | v2.0 | Stuck, "reframe this", same-looking solutions |
| [`negative-space`](skills/ds-negative-space/SKILL.md) | Absence Detector | v2.0 | "What am I missing", "is this complete" |

### 3. Integrity — How to trust the output

| Codename | Internal Name | Version | Trigger |
|---|---|---|---|
| [`contradict`](skills/ds-contradict/SKILL.md) | Coherence Auditor | v2.0 | Multi-part plans, long answers, design documents |
| [`provenance`](skills/ds-provenance/SKILL.md) | Evidence Tagger & Confidence Calibrator | v2.0 | "Is this true", "how sure are you" |
| [`fidelity`](skills/ds-fidelity/SKILL.md) | Compression Integrity Verifier | v2.0 | "Summarize", "TLDR", condensing complex analysis |

### 4. Governance & Systems

| Codename | Internal Name | Version | Trigger |
|---|---|---|---|
| [`anchor`](skills/ds-anchor/SKILL.md) | Objective Drift Detector | v2.0 | Long tasks, multi-step execution, scope creep |
| [`threshold`](skills/ds-threshold/SKILL.md) | Commitment Gateway | v2.0 | Irreversible decisions, schema changes, API contracts |
| [`emergence`](skills/ds-emergence/SKILL.md) | Interaction-Level Analyzer | v2.0 | Multi-component systems, integrations |
| [`temporal`](skills/ds-temporal/SKILL.md) | Cross-Time Reasoner | v2.0 | Architecture decisions, technology choices |

### 5. Meta — Orchestration & Premium

| Codename | Internal Name | Version | Trigger |
|---|---|---|---|
| [`conductor`](skills/ds-conductor/SKILL.md) | **Automatic** Skill Orchestration Layer | **v2.1** | **Any complex task — fully automatic** |
| [`boundary-detector`](skills/ds-boundary-detector/SKILL.md) | Knowledge Boundary Probe | v1.0 | "What do I not know", "am I hallucinating", high-stakes answers |
| [`meta-learning`](skills/ds-meta-learning/SKILL.md) | Cognitive Evolution Engine | v1.0 | "learn from this", "improve the skills", post-execution |
| [`verification-gates`](skills/ds-verification-gates/SKILL.md) | Depth Verification Engine | v1.0 | "verify this", "check gates", final validation |

### 6. Domain Skills (Enhanced v2.0)

| Codename | Internal Name | Version | Purpose |
|---|---|---|---|
| [`product-engineer`](skills/product-engineer/SKILL.md) | Job-to-be-Done Thinking | v2.0 | JTBD calculus, outcome verification |
| [`system-architect`](skills/system-architect/SKILL.md) | Data-First System Design | v2.0 | Architecture risk calculus, boundary integrity |
| [`copy-engineer`](skills/copy-engineer/SKILL.md) | Conversion-Oriented Writing | v2.0 | Specificity calculus, conversion proof |
| [`api-designer`](skills/api-designer/SKILL.md) | Developer-Experience-First Design | v2.0 | DX calculus, contract integrity |
| [`mobile-engineer`](skills/mobile-engineer/SKILL.md) | Mobile-First Development | v2.0 | Mobile fitness calculus, readiness cert |
| [`performance-engineer`](skills/performance-engineer/SKILL.md) | Measure-Before-Optimize | v2.0 | ROI calculus, optimization cert |
| [`refactor-engineer`](skills/refactor-engineer/SKILL.md) | Behavior-Preserving Transformation | v2.0 | Safety calculus, refactor cert |

---

## 🧩 How Skills Compose (v2.x)

**Automatic (via CONDUCTOR v2.1):**
Just invoke `conductor` — it handles everything automatically.

**Manual compositions (if needed):**

**Deep architectural decision:**
`conductor` → `deep-think` → `diverge` → `adversary` → `threshold`

**Stuck on a problem:**
`descend` → `reframe` → `invert` → `diverge`

**High-stakes delivery:**
`deep-think` → `adversary` → `contradict` → `provenance` → `fidelity`

**Before committing to something irreversible:**
`threshold` → `adversary` → `temporal` → full `conductor` sequence

**Novel domain / high uncertainty:**
`boundary-detector` → `conductor` (auto)

---

## 📖 The Core Vocabulary

| Term | Meaning |
|---|---|
| **Premature closure** | Settling on an answer before genuine exploration |
| **Convergence pressure** | The force pulling toward a quick, expected answer |
| **Pattern gravity** | The pull toward the most familiar template |
| **Lateral inhibition** | One strong activation suppressing adjacent, deeper pathways |
| **Activation depth** | How deep into the model's knowledge the search reaches |
| **Epistemic flattening** | Treating facts, inferences, and guesses with identical confidence |
| **ADS** | Activation Depth Score — weighted phase activation (0-1) |
| **CEI** | Cognitive Effort Index — complexity-weighted artifacts per token |
| **SI** | Surprise Index — C2/C3 assumptions + contrarian + fatal attacks + boundary violations |
| **EC** | Epistemic Calibration — (Facts + 0.5×Inferences) / Total claims |
| **OV** | Option Value — regret-weighted future flexibility |
| **CIM** | Compositional Independence Metric — path divergence (0-1) |
| **RSM** | Recursive Stability Metric — convergence of recursive self-audit |
| **CIM** | Compositional Independence Metric — path divergence (0-1) |

---

## 🛠️ Domain Skills

In addition to the 19 cognitive-mode skills + 4 premium skills above, this library includes **7 domain process skills** for specific engineering contexts — expert-level thinking for particular types of work.

These 7 domain skills are also located in the `skills/` directory alongside the core cognitive skills:
`product-engineer`, `system-architect`, `copy-engineer`, `api-designer`, `mobile-engineer`, `performance-engineer`, and `refactor-engineer`.

---

## 🔬 Contributing & The Protocol

Do these skills actually work on *your* specific problems? Test them yourself with the built-in evaluation protocol!

1. Pick a challenge from [`tests/test_prompts.json`](tests/test_prompts.json) (or write your own)
2. Run it **without** any skill loaded (control)
3. Run it **with** the target skill loaded (treatment)
4. Score both using the [depth scoring rubric](tests/eval.md) (0-10 scale)

**Want to Contribute?**
Read [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines. One test applies to every contribution:

**Does it change the cognitive mode, or does it just add steps?**
If it changes how the model thinks before generating — it belongs here. If it adds steps to an existing workflow — it belongs in a process library!

---

## 🗂️ Project Structure

```
depth-skills/
├── README.md              ← You are here
├── QUICKSTART.md          ← Setup guide
├── CHANGELOG.md           ← Version history
├── CONTRIBUTING.md        ← How to contribute
├── LICENSE                ← MIT License
├── benchmark/             ← Benchmarking framework (run.py, score.py, report.py)
├── tests/                 ← Built-in Evaluation Protocol + Results
│   ├── test_prompts.json
│   ├── eval.md
│   └── RESULTS.md
├── skills/                ← The Skill Library (19 Cognitive + 4 Premium + 7 Domain)
│   ├── ds-core/           ← Mathematical framework (MATHEMATICS.md)
│   ├── ds-deep-think/
│   ├── ds-adversary/
│   ├── ds-diverge/
│   ├── ds-descend/
│   ├── ds-excavate/
│   ├── ds-invert/
│   ├── ds-reframe/
│   ├── ds-negative-space/
│   ├── ds-contradict/
│   ├── ds-provenance/
│   ├── ds-fidelity/
│   ├── ds-anchor/
│   ├── ds-threshold/
│   ├── ds-emergence/
│   ├── ds-temporal/
│   ├── ds-conductor/
│   ├── ds-boundary-detector/
│   ├── ds-meta-learning/
│   ├── ds-verification-gates/
│   ├── ds-clarify/
│   ├── ds-shallow/
│   ├── ds-teach/
│   ├── product-engineer/
│   ├── system-architect/
│   ├── copy-engineer/
│   ├── api-designer/
│   ├── mobile-engineer/
│   ├── performance-engineer/
│   └── refactor-engineer/
└── benchmark/             ← Benchmarking framework
    ├── run.py
    ├── score.py
    ├── report.py
    ├── params_standard.json
    ├── params_deep.json
    ├── requirements.txt
    └── report.md
```

**Versioning Policy:** Each skill uses semantic versioning (`MAJOR.MINOR`). Major updates imply protocol rewrites, minor updates imply mechanism improvements. See [CHANGELOG.md](CHANGELOG.md) for history.

---

## 📄 License

[MIT](LICENSE) — use freely, modify freely, distribute freely.