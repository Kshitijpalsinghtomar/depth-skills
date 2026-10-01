# Contributing to Depth-Skills v2.x

Thank you for your interest in improving depth-skills. This library is a **cognitive architecture** — every change must earn its place through the FORGE quality standard and the new v2.x mathematical standards.

---

## How to Contribute

### 1. Fork & Branch

```bash
git fork https://github.com/Kshitijpalsinghtomar/depth-skills
git checkout -b improve/skill-name
```

### 2. Understand What This Library Is (v2.x)

Depth-skills are **cognitive mode-shifting protocols with mathematical verification**, not checklists.

Every skill must:
1. **Force the AI model to generate written artifacts** that change the content of its context window — physically altering what it generates next
2. **Produce measurable depth metrics** (ADS, CEI, SI, EC, OV, CIM, RSM)
3. **Pass verification gates** (V1-V6 machine-checkable + ungameable components)
4. **Support recursive self-audit** with RSM convergence detection
5. **Declare interference** (provides/receives with minimum ADS gains)
4. **Support thinking parameters** with presets (quick/standard/deep/forensic)

If a step says "consider X" instead of "write X," it's not a skill. It's a wish.

### 3. Types of Contributions

#### Improving an Existing Skill (v2.x Standards)

1. Run the skill yourself with the benchmark framework. Identify where it fails to force genuine cognitive work or produce measurable metrics.
2. Apply the **FORGE five-test scorecard** + **v2.x Mathematical Standards** to the skill.
3. Make changes that address specific test failures.
4. Update the version in the skill's YAML frontmatter (e.g., `2.0` → `2.1`).
5. Add an entry to `CHANGELOG.md`.

**v2.x Mathematical Standards Checklist:**
- [ ] Computes and outputs ADS phase activation
- [ ] Computes and outputs CEI components
- [ ] Computes and outputs SI components
- [ ] Computes and outputs EC (Epistemic Calibration)
- [ ] Computes and outputs OV (Option Value) where applicable
- [ ] Outputs cognitive traces (heatmaps, graphs, landscapes, certificates)
- [ ] Verifies Gates V1-V6 with machine-checkable criteria
- [ ] Supports recursive self-audit with RSM convergence detection
- [ ] Declares interference (provides/receives with minimum ADS gains)
- [ ] Supports thinking parameters with presets
- [ ] Includes MATHEMATICS COMPLIANCE section

#### Proposing a New Skill

Before writing a new skill, answer:

- **Non-redundancy:** Does this force a cognitive operation that NO existing skill covers?
- **Mechanism:** What specific written artifact does this skill force the model to generate?
- **Disruption:** Does this skill interrupt a default behavior, or does it just describe good practice?
- **Mathematical:** Does it produce measurable depth metrics (ADS, CEI, SI, EC, OV)?
- **Verifiable:** Does it pass Gates V1-V6 with machine-checkable criteria?
- **Recursive:** Does it support recursive self-audit with RSM?
- **Interference:** Does it declare what it provides/receives from other skills?
- **Parameters:** Does it support thinking parameters with presets?

If your answers are strong, write the skill following the v2.x standard format:

```yaml
---
name: skill-name
codename: SKILL-NAME
internal: Full Internal Name
version: 2.0
tier: cognition | excavation | integrity | governance | systems | meta
trigger: when this skill activates
author: Kshitijpalsinghtomar
tags: [orchestration, meta, sequencing, proportional-depth, budget, etc.]
artifacts:
  - artifact-name
  - activation-heatmap
  - assumption-dependency-graph
  - depth-certificate-contribution
  - phase-activation
composable_with: [all-skills]
thinking_parameters:
  param_name: default_value
  require_feature: true
---

# SKILL-NAME — Internal Name v2.0 (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (...), and verifies Gates V1-V6. It [what it does uniquely].

[Protocol with mathematical metrics, recursive audit, interference, gates, traces]

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
- Artifacts produced: [list with weights]
- Total complexity weight: X.X

### SI Components
- [components with counts]

### Cognitive Traces Produced
- [x] Activation Heatmap / [x] Assumption Dependency Graph / [x] Decision Landscape / [x] Other

### Gates Verified
- [x] V1  [x] V2  [x] V3  [x] V4  [x] V5  [x] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From [Skill A]: [what] → [use]
- From [Skill B]: [what] → [use]
```

#### Proposing a New Domain Skill

Domain skills go in `skills/` alongside cognitive skills. These are context-specific process skills (e.g., `system-architect`, `api-designer`), not cognitive-mode skills. They must still meet v2.x mathematical standards.

### 4. Quality Gate (FORGE + v2.x Mathematical Standards)

All contributions are evaluated against FORGE's five tests + v2.x mathematical standards:

| Test | Requirement |
|---|---|
| **Cognitive Disruption** | Does the skill interrupt a default behavior? |
| **Anti-Fake** | Can the model fake compliance without doing the work? |
| **Operational Specificity** | Does every instruction produce observable output? |
| **Non-Redundancy** | Does this do something no other skill does? |
| **Honest Mechanism** | Does the description match what actually happens in the model? |
| **Mathematical Depth** | Does it produce ADS, CEI, SI, EC, OV metrics? |
| **Verifiable Gates** | Does it pass V1-V6 with machine-checkable criteria? |
| **Recursive Audit** | Does it support recursive self-audit with RSM? |
| **Interference** | Does it declare provides/receives with min ADS gains? |
| **Parameters** | Does it support thinking parameters with presets? |

Contributions that score below 25/30 on the combined FORGE + Mathematical scorecard will be asked to revise.

### 5. Submit

```bash
git add -A
git commit -m "improve(skill-name): brief description of what changed"
git push origin improve/skill-name
```

Open a pull request with:
- **What changed** — specific improvements, not "made it better"
- **FORGE + Mathematical scores** — before and after, if improving an existing skill
- **Why** — what failure or gap motivated the change
- **Benchmark results** — if applicable, run `python benchmark/run.py` and include results

---

## Commit Message Convention

```
improve(skill-name): description     # improving existing skill
add(skill-name): description         # new skill
fix(skill-name): description         # fixing a bug or typo
docs: description                    # documentation changes
bench: description                   # benchmark improvements
```

---

## What We Don't Accept

- **Checklist inflation** — adding steps that don't force written output
- **Philosophy padding** — adding paragraphs that sound deep but don't activate specific knowledge
- **Redundant skills** — skills that cover the same cognitive operation as an existing skill
- **Generic instructions** — "think carefully" / "be thorough" / "consider all options"
- **Non-mathematical skills** — skills that don't produce measurable depth metrics
- **Non-verifiable skills** — skills that can't pass machine-checkable gates
- **Non-recursive skills** — skills that don't support recursive self-audit
- **Non-interfering skills** — skills that don't declare provides/receives

Every word in this library must earn its place. Verbosity is not depth. **Measurable, verifiable, recursive depth is.**

---

## Questions?

Open an issue. Describe what you're trying to improve and why the current version falls short. We'll discuss before you write code.