# depth-skills

> **Skills that change how AI thinks, not just what steps it follows.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 16](https://img.shields.io/badge/Skills-16-brightgreen.svg)](#skill-reference)
[![Version: 1.1](https://img.shields.io/badge/Version-1.1-orange.svg)](CHANGELOG.md)

An open-source cognitive architecture for AI agents. 16 skills that force language models past surface-level reasoning into genuine depth — not by adding process steps, but by structurally changing how the model searches its knowledge before answering.

**Compatible with:** Claude Code · Cursor · Gemini CLI · GitHub Copilot · Antigravity · Windsurf · OpenCode · Any agent that reads markdown instructions.

---

## The Problem

Language models experience **premature closure**. A query arrives, a statistically likely answer forms, and the model outputs it — not because it explored deeply, but because **convergence pressure** rewarded early stopping. The deeper pathways — connections between distant concepts, non-obvious framings, solutions requiring cross-domain synthesis — never activate. Not because they don't exist. Because nothing forced the search to go there.

Most skill libraries add more steps. These skills change the **cognitive mode**.

---

## Quick Start

```bash
# Install all skills via skills.sh (recommended)
npx skills add Kshitijpalsinghtomar/depth-skills

# Or clone the full library
git clone https://github.com/Kshitijpalsinghtomar/depth-skills

# Or copy individual skills into your agent
cp -r depth-skills/skills/deep-think ~/.gemini/skills/
```

**Try it now:** Add the `deep-think` skill to your AI agent and ask it a question you've asked before. Compare the depth.

→ Full setup guide: [QUICKSTART.md](QUICKSTART.md)

---

## Compatibility

These skills work with any AI agent or tool that accepts markdown instructions:

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

## The Architecture

```
┌──────────────────────────────────────────────────────┐
│                    META                              │
│               ┌─────────┐                            │
│               │CONDUCTOR│ ← Selects & sequences      │
│               └────┬────┘   the right skills         │
│                    │                                 │
├────────────────────┼─────────────────────────────────┤
│              COGNITION                               │
│  ┌──────────┐ ┌─────────┐ ┌───────┐ ┌───────┐        │
│  │DEEP-THINK│ │ADVERSARY│ │DIVERGE│ │DESCEND│        │
│  └──────────┘ └─────────┘ └───────┘ └───────┘        │
│  How to search deeper                                │
│                                                      │
├──────────────────────────────────────────────────────┤
│              EXCAVATION                              │
│  ┌────────┐ ┌──────┐ ┌───────┐ ┌──────────────┐      │
│  │EXCAVATE│ │INVERT│ │REFRAME│ │NEGATIVE-SPACE│      │
│  └────────┘ └──────┘ └───────┘ └──────────────┘      │
│  What to dig for                                     │
│                                                      │
├──────────────────────────────────────────────────────┤
│              INTEGRITY                               │
│  ┌──────────┐ ┌──────────┐ ┌────────┐                │
│  │CONTRADICT│ │PROVENANCE│ │FIDELITY│                │
│  └──────────┘ └──────────┘ └────────┘                │
│  How to trust the output                             │
│                                                      │
├──────────────────────────────────────────────────────┤
│              GOVERNANCE                              │
│  ┌──────┐ ┌─────────┐                                │
│  │ANCHOR│ │THRESHOLD│                                │
│  └──────┘ └─────────┘                                │
│  How to control the process                          │
│                                                      │
├──────────────────────────────────────────────────────┤
│              SYSTEMS                                 │
│  ┌─────────┐ ┌────────┐                              │
│  │EMERGENCE│ │TEMPORAL│                              │
│  └─────────┘ └────────┘                              │
│  How to reason about wholes                          │
└──────────────────────────────────────────────────────┘
```

---

## Skill Reference

Every skill has a **codename** (what you invoke), an **internal name** (what it does), and a **version**.

### Cognition — How to search deeper

| Codename | Internal Name | Version | Trigger |
|---|---|---|---|
| [`deep-think`](skills/deep-think/SKILL.md) | The Depth Protocol | v1.1 | Complex problem, "go deeper", any task where the first answer is too easy |
| [`adversary`](skills/adversary/SKILL.md) | Self-Opposition Engine | v1.1 | Any significant decision, any plan before execution |
| [`diverge`](skills/diverge/SKILL.md) | Path Divergence | v1.1 | "What's the best way to", any architectural choice |
| [`descend`](skills/descend/SKILL.md) | Pattern Audit & First-Principles Derivation | v1.1 | "Nothing works", familiar solution feels wrong, novel problems |

### Excavation — What to dig for

| Codename | Internal Name | Version | Trigger |
|---|---|---|---|
| [`excavate`](skills/excavate/SKILL.md) | Assumption Archaeology | v1.1 | "What am I assuming", high-stakes plans |
| [`invert`](skills/invert/SKILL.md) | Constraint & Belief Inversion | v1.1 | "We have no choice", "are we sure", boxed-in tradeoffs |
| [`reframe`](skills/reframe/SKILL.md) | Representation Multiplier | v1.1 | Stuck, "reframe this", same-looking solutions |
| [`negative-space`](skills/negative-space/SKILL.md) | Absence Detector | v1.1 | "What am I missing", "is this complete" |

### Integrity — How to trust the output

| Codename | Internal Name | Version | Trigger |
|---|---|---|---|
| [`contradict`](skills/contradict/SKILL.md) | Coherence Auditor | v1.1 | Multi-part plans, long answers, design documents |
| [`provenance`](skills/provenance/SKILL.md) | Evidence Tagger & Confidence Calibrator | v1.1 | "Is this true", "how sure are you" |
| [`fidelity`](skills/fidelity/SKILL.md) | Compression Integrity Verifier | v1.1 | "Summarize", "TLDR", condensing complex analysis |

### Governance — How to control the process

| Codename | Internal Name | Version | Trigger |
|---|---|---|---|
| [`anchor`](skills/anchor/SKILL.md) | Objective Drift Detector | v1.1 | Long tasks, multi-step execution, scope creep |
| [`threshold`](skills/threshold/SKILL.md) | Commitment Gateway | v1.1 | Irreversible decisions, schema changes, API contracts |

### Systems — How to reason about wholes

| Codename | Internal Name | Version | Trigger |
|---|---|---|---|
| [`emergence`](skills/emergence/SKILL.md) | Interaction-Level Analyzer | v1.1 | Multi-component systems, integrations |
| [`temporal`](skills/temporal/SKILL.md) | Cross-Time Reasoner | v1.1 | Architecture decisions, technology choices |

### Meta — Orchestration

| Codename | Internal Name | Version | Trigger |
|---|---|---|---|
| [`conductor`](skills/conductor/SKILL.md) | Skill Orchestration Layer | v1.1 | Complex tasks, "give me everything" |

---

## How Skills Compose

Skills are designed to chain. Some common compositions:

**Deep architectural decision:**
`conductor` → `deep-think` → `diverge` → `adversary` → `threshold`

**Stuck on a problem:**
`descend` → `reframe` → `invert` → `diverge`

**High-stakes delivery:**
`deep-think` → `adversary` → `contradict` → `provenance` → `fidelity`

**"Is this complete?":**
`negative-space` → `excavate` → `emergence`

**Before committing to something irreversible:**
`threshold` → `adversary` → `temporal` → full `conductor` sequence

---

## The Core Vocabulary

These terms appear throughout the skills. Understanding them unlocks the system:

| Term | Meaning |
|---|---|
| **Premature closure** | Settling on an answer before genuine exploration |
| **Convergence pressure** | The force pulling toward a quick, expected answer |
| **Pattern gravity** | The pull toward the most familiar template |
| **Lateral inhibition** | One strong activation suppressing adjacent, deeper pathways |
| **Local optimum** | A good-enough answer that prevents finding the best answer |
| **Activation depth** | How deep into the model's knowledge the search reaches |
| **Coherence trap** | When sounding right prevents being right |
| **Cognitive inertia** | Resistance to changing direction once started |
| **Attentional blindspot** | The dimension space the model never illuminated |
| **Epistemic flattening** | Treating facts, inferences, and guesses with identical confidence |

---

## Domain Skills

In addition to the cognitive-mode skills above, this library includes **domain process skills** for specific engineering contexts — expert-level thinking for particular types of work.

→ See [domain/README.md](domain/README.md) for the full list (7 domain skills).

---

## What Makes These Different

| Approach | What It Does | What It Doesn't Do |
|---|---|---|
| Process libraries (Superpowers, GSD) | Add workflow steps | Change how the model thinks within each step |
| Tool integrations (Playwright, AWS) | Connect to external systems | Improve reasoning quality |
| **Depth-skills** | **Change the cognitive mode** | Replace process or tools |

A skill like `deep-think` doesn't add a review step. It prevents the answer from forming until deeper pathways have been activated. `negative-space` doesn't check what's there — it finds what's absent. `descend` doesn't criticize the answer — it verifies whether the problem was correctly identified before any answer was formed.

**These compose with process and tool libraries.** Use Superpowers for TDD discipline. Use depth-skills for the quality of thinking within each step.

---

## Project Structure

```
depth-skills/
├── README.md              ← You are here
├── QUICKSTART.md           ← Setup guide
├── CHANGELOG.md            ← Version history
├── CONTRIBUTING.md         ← How to contribute
├── LICENSE                 ← MIT License
├── .gitignore
├── skills/                 ← 16 cognitive-mode skills
│   ├── deep-think/
│   ├── adversary/
│   ├── diverge/
│   ├── descend/
│   ├── excavate/
│   ├── invert/
│   ├── reframe/
│   ├── negative-space/
│   ├── contradict/
│   ├── provenance/
│   ├── fidelity/
│   ├── anchor/
│   ├── threshold/
│   ├── emergence/
│   ├── temporal/
│   └── conductor/
└── domain/                 ← 7 domain-specific process skills
    ├── product-engineer/
    ├── system-architect/
    ├── copy-engineer/
    ├── api-designer/
    ├── mobile-engineer/
    ├── performance-engineer/
    └── refactor-engineer/

```

---

## Versioning

Each skill uses semantic versioning: `MAJOR.MINOR`
- **Major** (1.0 → 2.0): Protocol rewrite. Steps change.
- **Minor** (1.0 → 1.1): Improved mechanisms, tighter constraints. Core unchanged.

→ See [CHANGELOG.md](CHANGELOG.md) for version history.

---

## Testing & Evaluation

Do these skills actually work? Test them yourself with the built-in evaluation protocol:

1. Pick a challenge from [`tests/test_prompts.json`](tests/test_prompts.json) (20 real-world challenges)
2. Run it **without** any skill loaded (control)
3. Run it **with** the target skill loaded (treatment)
4. Score both using the [depth scoring rubric](tests/eval.md) (0-10 scale)
5. Compare the delta

→ Full protocol: [tests/eval.md](tests/eval.md) · Results: [tests/RESULTS.md](tests/RESULTS.md)

**Found a difference?** Open an issue or PR with your before/after results. Community evidence makes the library stronger.

---

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines. One test applies to every contribution:

**Does it change the cognitive mode, or does it just add steps?**

If it changes how the model thinks before generating — it belongs here.
If it adds steps to an existing workflow — it belongs in a process library.

---

## Philosophy

The standard of a great skill is not "does it add process." It is: **does reading this change how the model reasons about the problem?**

LLMs use a fraction of their knowledge depth because early answers are rewarded and users rarely push past them. The model settles at 60-75% activation because nothing forces it deeper. These skills are the forcing function. They create mandatory written artifacts that enter the context window and physically change what the model generates next.

Each skill targets a different dimension of premature closure:
- Closing before exploring alternatives → `diverge`, `reframe`
- Closing before checking foundations → `excavate`, `descend`
- Closing before challenging the answer → `adversary`, `invert`
- Closing before checking consistency → `contradict`
- Closing before checking for absences → `negative-space`
- Closing before calibrating confidence → `provenance`
- Closing before matching depth to consequence → `threshold`, `conductor`
- Closing before checking interactions → `emergence`
- Closing before reasoning across time → `temporal`
- Closing before ensuring fidelity → `fidelity`
- Closing before ensuring direction → `anchor`

The result is not "make the AI smarter." It is: **make the AI use more of what it already knows.**

---

## License

[MIT](LICENSE) — use freely, modify freely, distribute freely.
