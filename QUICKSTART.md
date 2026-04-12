# Quick Start — Your First 10 Minutes

## What Is This?

A library of **thinking skills** for AI agents. Not checklists. Not process steps. Cognitive modes that change how the model reasons before it generates output.

**The core idea:** AI models settle on answers too early. The first plausible response forms and ships — while deeper, better answers sit unused in the model's knowledge. These skills force the model past that surface layer into genuine depth.

---

## Install

### Option A: Full Library
```bash
git clone https://github.com/Kshitijpalsinghtomar/depth-skills
```

### Option B: Individual Skills
```bash
# Copy the skill you want into your agent's skill directory
cp -r depth-skills/skills/deep-think ~/.config/skills/
```

### Option C: Manual
Open any `SKILL.md` file and paste its contents into your AI agent's skill/instruction configuration.

---

## Try Your First Skill

Start with **`deep-think`** — the foundational skill.

### Without deep-think:
> "Design a user authentication system for my app"
>
> → You'll get a standard JWT + password hashing answer. Correct. Surface-level.

### With deep-think:
> The same question, but the model now runs the Depth Protocol:
> 1. Restates the problem (catches misunderstandings)
> 2. Surfaces hidden assumptions (are you sure you need auth, not just sessions?)
> 3. Generates three genuinely different approaches (not variations)
> 4. Steelmans the opposition (why might the chosen approach be wrong?)
> 5. Stress-tests edge cases (what about account recovery? Rate limiting? Token rotation?)
> 6. Compresses with caveats named
>
> → You'll get a deeper, more considered answer that names its assumptions and limitations.

**The difference is not more words. It's more thinking.**

---

## The Skill Map — Where to Go Next

After `deep-think`, add skills based on what you need:

```
"I want better decisions"
  → adversary (challenge your answer)
  → diverge (explore real alternatives)
  → threshold (match depth to consequence)

"I want to catch hidden problems"
  → excavate (find hidden assumptions)
  → negative-space (find what's missing)
  → emergence (find interaction bugs)

"I want to trust the output"
  → contradict (find internal inconsistencies)
  → provenance (tag evidence quality)
  → fidelity (don't lose truth when summarizing)

"I want to solve hard problems"
  → descend (go below patterns to first principles)
  → reframe (same problem, different lenses)
  → invert (flip constraints and beliefs)

"I want the system to self-organize"
  → conductor (selects the right skills automatically)
```

---

## How Skills Work Together

Skills compose. You can chain them for deeper analysis:

1. **Start broad:** `deep-think` expands the search space
2. **Challenge:** `adversary` attacks the best option
3. **Verify:** `contradict` checks internal consistency
4. **Calibrate:** `provenance` tags evidence quality
5. **Compress:** `fidelity` ensures the summary preserves truth

Or use `conductor` — it selects and sequences the right skills automatically based on the task's complexity and consequence level.

---

## Folder Structure

```
depth-skills/
├── README.md          ← Architecture guide
├── QUICKSTART.md      ← You are here
├── CHANGELOG.md       ← Version history
├── skills/            ← 16 cognitive-mode skills
   ├── ds-deep-think/
   ├── ds-adversary/
   ├── ds-diverge/
   ├── ds-descend/
   ├── ds-excavate/
   ├── ds-invert/
   ├── ds-reframe/
   ├── ds-negative-space/
   ├── ds-contradict/
   ├── ds-provenance/
   ├── ds-fidelity/
   ├── ds-anchor/
   ├── ds-threshold/
   ├── ds-emergence/
   ├── ds-temporal/
   ├── ds-conductor/
   ├── product-engineer/
   ├── system-architect/
   ├── copy-engineer/
   ├── api-designer/
   ├── mobile-engineer/
   ├── performance-engineer/
   └── refactor-engineer/
```

---

## FAQ

**Q: Do I need all 16 skills?**
No. Start with `deep-think` alone. Add others as you encounter specific needs. The [Skill Map](#the-skill-map--where-to-go-next) above tells you which to add when.

**Q: Do these work with any AI model?**
Yes. They're model-agnostic markdown instructions. Any model that reads skill/instruction files can use them.

**Q: What's the difference between the `skills/` and `domain/` folders?**
`skills/` contains cognitive-mode skills — they change HOW the model thinks, regardless of domain. `domain/` contains process skills — they provide expert knowledge for WHAT the model thinks about (APIs, mobile, performance, etc.). They compose: use `deep-think` + `system-architect` for deep architectural reasoning.

**Q: How are skills versioned?**
Each skill has a version in its frontmatter (e.g., `version: 1.0`). Check CHANGELOG.md for updates.
