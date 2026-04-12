# Contributing to Depth-Skills

Thank you for your interest in improving depth-skills. This library is a cognitive architecture — every change must earn its place through the FORGE quality standard.

---

## How to Contribute

### 1. Fork & Branch

```bash
git fork https://github.com/Kshitijpalsinghtomar/depth-skills
git checkout -b improve/skill-name
```

### 2. Understand What This Library Is

Depth-skills are **cognitive mode-shifting protocols**, not checklists.

Every skill must force the AI model to generate written artifacts that change the content of its context window — physically altering what it generates next. If a step says "consider X" instead of "write X," it's not a skill. It's a wish.

### 3. Types of Contributions

#### Improving an Existing Skill

1. Run the skill yourself. Identify where it fails to force genuine cognitive work.
2. Apply the FORGE five-test scorecard to the skill.
3. Make changes that address specific test failures.
4. Update the version in the skill's YAML frontmatter (e.g., `1.1` → `1.2`).
5. Add an entry to `CHANGELOG.md`.

#### Proposing a New Skill

Before writing a new skill, answer:

- **Non-redundancy:** Does this force a cognitive operation that NO existing skill covers?
- **Mechanism:** What specific written artifact does this skill force the model to generate?
- **Disruption:** Does this skill interrupt a default behavior, or does it just describe good practice?

If your answers are strong, write the skill following the standard format:

```yaml
---
codename: SKILL-NAME
internal: Full Internal Name
version: 1.0
tier: cognition | excavation | integrity | governance | systems | meta
trigger: when this skill activates
---
```

Every step must:
- Force **written output** (not "consider" — "write")
- Produce a **named artifact** referenced by subsequent steps
- Include **specificity anchors** ("for THIS problem")

#### Proposing a New Domain Skill

Domain skills go in `domain/`. These are context-specific process skills (e.g., `system-architect`, `api-designer`), not cognitive-mode skills.

### 4. Quality Gate

All contributions are evaluated against FORGE's five tests:

| Test | Requirement |
|---|---|
| **Cognitive Disruption** | Does the skill interrupt a default behavior? |
| **Anti-Fake** | Can the model fake compliance without doing the work? |
| **Operational Specificity** | Does every instruction produce observable output? |
| **Non-Redundancy** | Does this do something no other skill does? |
| **Honest Mechanism** | Does the description match what actually happens in the model? |

Contributions that score below 20/25 on the FORGE scorecard will be asked to revise.

### 5. Submit

```bash
git add -A
git commit -m "improve(skill-name): brief description of what changed"
git push origin improve/skill-name
```

Open a pull request with:
- **What changed** — specific improvements, not "made it better"
- **FORGE scores** — before and after, if improving an existing skill
- **Why** — what failure or gap motivated the change

---

## Commit Message Convention

```
improve(skill-name): description     # improving existing skill
add(skill-name): description         # new skill
fix(skill-name): description         # fixing a bug or typo
docs: description                    # documentation changes
```

---

## What We Don't Accept

- **Checklist inflation** — adding steps that don't force written output
- **Philosophy padding** — adding paragraphs that sound deep but don't activate specific knowledge
- **Redundant skills** — skills that cover the same cognitive operation as an existing skill
- **Generic instructions** — "think carefully" / "be thorough" / "consider all options"

Every word in this library must earn its place. Verbosity is not depth.

---

## Questions?

Open an issue. Describe what you're trying to improve and why the current version falls short. We'll discuss before you write code.
