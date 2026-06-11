# depth-skills

> **Skills that change how AI thinks, not just what steps it follows.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 19](https://img.shields.io/badge/Skills-19-brightgreen.svg)](#skill-reference)
[![Version: 1.2](https://img.shields.io/badge/Version-1.2-orange.svg)](CHANGELOG.md)

An open-source cognitive architecture for AI agents. 19 skills that force language models past surface-level reasoning into genuine depth — not by adding process steps, but by structurally changing how the model searches its knowledge before answering.

---

## 🛑 The Problem: Premature Closure

Language models experience **premature closure**. A query arrives, a statistically likely answer forms, and the model outputs it — not because it explored deeply, but because **convergence pressure** rewarded early stopping. 

The deeper pathways — connections between distant concepts, non-obvious framings, solutions requiring cross-domain synthesis — rarely activate. The model settles at 60-75% activation solely because nothing forces it deeper. 

### Why existing solutions fail to stop this:
| Approach | What It Does | What It Doesn't Do |
|---|---|---|
| **Process libraries** (e.g. Superpowers) | Add workflow/pipeline steps | Change how the AI thinks *within* each step |
| **Tool integrations** (e.g. Playwright, AWS) | Connect to external computational systems | Improve the AI's internal reasoning quality |
| **Depth-skills (This Library)** | **Forces structural cognitive constraint** | Compete with process or tools (they compose perfectly) |

A skill like `deep-think` doesn't just add a review step. It blocks the answer from forming until deeper semantic pathways have been activated. `descend` doesn't merely criticize an answer — it verifies whether the problem was properly identified before any answer was even generated.

---

## 📈 The Evidence: Why Cognitive Depth Matters

Internal testing on complex architectural prompts demonstrates a **massive non-linear jump in reasoning depth** when skills are stacked side-by-side. 

By applying multiple cognitive restraints simultaneously, we stop the AI from generating baseline tutorial-level answers and force it into strategic, multi-horizon thinking.

<p align="center">
  <img src="https://img.shields.io/badge/Control_Run_Score-2%2F10-red?style=for-the-badge" alt="Control Run 2/10"/>
  <img src="https://img.shields.io/badge/3_Skills_Stacked-8%2F10-yellow?style=for-the-badge" alt="3 Skills 8/10"/>
  <img src="https://img.shields.io/badge/5_Skills_Stacked-10%2F10-success?style=for-the-badge" alt="5 Skills 10/10"/>
</p>

| Setup | Cognitive Behavior | Depth Score |
|:---|:---|:---:|
| **Control (0 Skills)** | Yields to *pattern gravity* and jumps straight to the most common engineering tutorial answer. | **2/10** |
| **Treatment (3 Skills)** | Audits its own assumptions using `PROVENANCE`, attacks its baseline answer using `ADVERSARY`. Acts like a **Senior Developer**. | **8/10** |
| **Treatment (5 Skills)** | Reframes the actual problem using `DEEP-THINK` and discovers contrarian architectures using `DIVERGE`. Acts like a **Staff Architect**. | **10/10** |

→ Read the full scoring breakdown, prompts, and case studies in [tests/RESULTS.md](tests/RESULTS.md)

---

## 🚀 Quick Start

```bash
# Install all skills via skills.sh (recommended)
npx skills add Kshitijpalsinghtomar/depth-skills

# Or clone the full library
git clone https://github.com/Kshitijpalsinghtomar/Depth-skills

# Or copy individual skills into your agent
cp -r depth-skills/skills/ds-conductor ~/.claude/skills/
```

**Recommended:** Start with `ds-conductor` — it automatically selects appropriate skills based on task complexity. This gives you proportional depth without manually choosing skills.

**Try it now:** Add the `ds-conductor` skill and ask it questions of varying complexity. Compare the depth of response.

→ Full setup guide: [QUICKSTART.md](QUICKSTART.md)

---

## ⚙️ Compatibility

These skills work natively with any AI agent or tool that accepts markdown instructions. (Just paste them in your system context!):

| Tool | How to Use | Skill Path |
|---|---|---|
| **Claude Code** | Copy to `~/.claude/skills/` | `skills/<name>/SKILL.md` |
| **Cursor** | Add to `.cursor/rules/` or paste into system prompt | `skills/<name>/SKILL.md` |
| **Gemini CLI** | Copy to `~/.gemini/skills/` | `skills/<name>/SKILL.md` |
| **GitHub Copilot** | Add to `.github/copilot-instructions/` | `skills/<name>/SKILL.md` |
| **Antigravity** | Copy to `~/.gemini/skills/` | `skills/<name>/SKILL.md` |
| **Windsurf** | Add to `.windsurf/rules/` | `skills/<name>/SKILL.md` |
| **Any LLM** | Paste skill content into system prompt or context | `skills/<name>/SKILL.md` |

---

## 🏛️ The Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                        META                                  │
│                   ┌─────────────┐                            │
│                   │  CONDUCTOR  │ ← Selects & sequences      │
│                   └──────┬──────┘   the right skills         │
│                          │                                   │
├──────────────────────────┼───────────────────────────────────┤
│                      COGNITION                               │
│  ┌──────────┐ ┌─────────┐ ┌───────┐ ┌───────┐ ┌─────────┐    │
│  │DEEP-THINK│ │ADVERSARY│ │DIVERGE│ │DESCEND│ │ CLARIFY │    │
│  └──────────┘ └─────────┘ └───────┘ └───────┘ └─────────┘    │
│  ┌─────────┐ ┌─────────┐                                     │
│  │ SHALLOW │ │  TEACH  │                                     │
│  └─────────┘ └─────────┘                                     │
│  How to search deeper / proportional depth                   │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│              EXCAVATION                                      │
│  ┌────────┐ ┌──────┐ ┌───────┐ ┌──────────────┐              │
│  │EXCAVATE│ │INVERT│ │REFRAME│ │NEGATIVE-SPACE│              │
│  └────────┘ └──────┘ └───────┘ └──────────────┘              │
│  What to dig for                                             │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│              INTEGRITY                                       │
│  ┌──────────┐ ┌──────────┐ ┌────────┐ ┌───────┐              │
│  │CONTRADICT│ │PROVENANCE│ │FIDELITY│ │ TEACH │              │
│  └──────────┘ └──────────┘ └────────┘ └───────┘              │
│  How to trust the output                                     │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│              GOVERNANCE                                      │
│  ┌──────┐ ┌─────────┐                                        │
│  │ANCHOR│ │THRESHOLD│                                        │
│  └──────┘ └─────────┘                                        │
│  How to control the process                                  │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│              SYSTEMS                                         │
│  ┌─────────┐ ┌────────┐                                      │
│  │EMERGENCE│ │TEMPORAL│                                      │
│  └─────────┘ └────────┘                                      │
│  How to reason about wholes                                  │
└──────────────────────────────────────────────────────────────┘
```

---

## 🧰 Skill Reference

Every skill has a **codename** (what you invoke), an **internal name** (what it does), and a **version**.

### 1. Cognition — How to search deeper

| Codename | Internal Name | Version | Trigger |
|---|---|---|---|
| [`deep-think`](skills/ds-deep-think/SKILL.md) | The Depth Protocol | v1.1 | Complex problem, "go deeper", any task where the first answer is too easy |
| [`adversary`](skills/ds-adversary/SKILL.md) | Self-Opposition Engine | v1.1 | Any significant decision, any plan before execution |
| [`diverge`](skills/ds-diverge/SKILL.md) | Path Divergence | v1.1 | "What's the best way to", any architectural choice |
| [`descend`](skills/ds-descend/SKILL.md) | Pattern Audit & First-Principles Derivation | v1.1 | "Nothing works", familiar solution feels wrong, novel problems |
| [`clarify`](skills/ds-clarify/SKILL.md) | Ask/Answer Decision Engine | v1.1 | Ambiguous request, missing context, "should I ask or answer" |
| [`shallow`](skills/ds-shallow/SKILL.md) | Proportional Depth Protocol | v1.1 | Low-stakes task, "keep it simple", quick answer needed |
| [`teach`](skills/ds-teach/SKILL.md) | Feynman Gap Detection | v1.1 | "explain like I'm 5", test my understanding |

### 2. Excavation — What to dig for

| Codename | Internal Name | Version | Trigger |
|---|---|---|---|
| [`excavate`](skills/ds-excavate/SKILL.md) | Assumption Archaeology | v1.1 | "What am I assuming", high-stakes plans |
| [`invert`](skills/ds-invert/SKILL.md) | Constraint & Belief Inversion | v1.1 | "We have no choice", "are we sure", boxed-in tradeoffs |
| [`reframe`](skills/ds-reframe/SKILL.md) | Representation Multiplier | v1.1 | Stuck, "reframe this", same-looking solutions |
| [`negative-space`](skills/ds-negative-space/SKILL.md) | Absence Detector | v1.1 | "What am I missing", "is this complete" |

### 3. Integrity — How to trust the output

| Codename | Internal Name | Version | Trigger |
|---|---|---|---|
| [`contradict`](skills/ds-contradict/SKILL.md) | Coherence Auditor | v1.1 | Multi-part plans, long answers, design documents |
| [`provenance`](skills/ds-provenance/SKILL.md) | Evidence Tagger & Confidence Calibrator | v1.1 | "Is this true", "how sure are you" |
| [`fidelity`](skills/ds-fidelity/SKILL.md) | Compression Integrity Verifier | v1.1 | "Summarize", "TLDR", condensing complex analysis |

### 4. Governance & Systems

| Codename | Internal Name | Version | Trigger |
|---|---|---|---|
| [`anchor`](skills/ds-anchor/SKILL.md) | Objective Drift Detector | v1.1 | Long tasks, multi-step execution, scope creep |
| [`threshold`](skills/ds-threshold/SKILL.md) | Commitment Gateway | v1.1 | Irreversible decisions, schema changes, API contracts |
| [`emergence`](skills/ds-emergence/SKILL.md) | Interaction-Level Analyzer | v1.1 | Multi-component systems, integrations |
| [`temporal`](skills/ds-temporal/SKILL.md) | Cross-Time Reasoner | v1.1 | Architecture decisions, technology choices |

### 5. Meta — Orchestration

| Codename | Internal Name | Version | Trigger |
|---|---|---|---|
| [`conductor`](skills/ds-conductor/SKILL.md) | Skill Orchestration Layer | v1.1 | Complex tasks, "give me everything" |

---

## 🧩 How Skills Compose

Skills are designed to chain seamlessly. Some common compositions:

**Deep architectural decision:**
`conductor` → `deep-think` → `diverge` → `adversary` → `threshold`

**Stuck on a problem:**
`descend` → `reframe` → `invert` → `diverge`

**High-stakes delivery:**
`deep-think` → `adversary` → `contradict` → `provenance` → `fidelity`

**Before committing to something irreversible:**
`threshold` → `adversary` → `temporal` → full `conductor` sequence

---

## 📖 The Core Vocabulary

These terms appear throughout the skills. Understanding them unlocks the system:

| Term | Meaning |
|---|---|
| **Premature closure** | Settling on an answer before genuine exploration |
| **Convergence pressure** | The force pulling toward a quick, expected answer |
| **Pattern gravity** | The pull toward the most familiar template |
| **Lateral inhibition** | One strong activation suppressing adjacent, deeper pathways |
| **Activation depth** | How deep into the model's knowledge the search reaches |
| **Epistemic flattening** | Treating facts, inferences, and guesses with identical confidence |

---

## 🛠️ Domain Skills

In addition to the cognitive-mode skills above, this library includes **domain process skills** for specific engineering contexts — expert-level thinking for particular types of work.

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
├── QUICKSTART.md           ← Setup guide
├── CHANGELOG.md            ← Version history
├── CONTRIBUTING.md         ← How to contribute
├── LICENSE                 ← MIT License
├── tests/                  ← Built-in Evaluation Protocol + Results
└── skills/                 ← The Skill Library (19 Cognitive + 7 Domain)
```

**Versioning Policy:** Each skill uses semantic versioning (`MAJOR.MINOR`). Major updates imply protocol rewrites, minor updates imply mechanism improvements. See [CHANGELOG.md](CHANGELOG.md) for history.

---

## 📄 License
[MIT](LICENSE) — use freely, modify freely, distribute freely.
