# Quick Start — Your First 10 Minutes (v2.x)

## What Is This?

A library of **thinking skills** for AI agents. Not checklists. Not process steps. Cognitive modes that change how the model reasons before it generates output.

**The core idea:** AI models settle on answers too early. The first plausible response forms and ships — while deeper, better answers sit unused in the model's knowledge. These skills force the model past that surface layer into genuine depth.

**New in v2.x:** Mathematical depth metrics (ADS, CEI, SI, EC, OV), automatic orchestration via CONDUCTOR v2.1, boundary detection, meta-learning, and verifiable depth reports.

---

## Install

### Option A: Full Library (Recommended)
```bash
git clone https://github.com/Kshitijpalsinghtomar/depth-skills
cd depth-skills
```

### Option B: Individual Skills
```bash
# Copy the skill you want into your agent's skill directory
cp -r skills/ds-conductor ~/.claude/skills/
```

### Option C: Manual
Open any `SKILL.md` file and paste its contents into your AI agent's skill/instruction configuration.

---

## Try Your First Skill

Start with **`ds-conductor` v2.1** — the fully automatic orchestrator.

### Without any skills:
> "Design a user authentication system for my app"
>
> → You'll get a standard JWT + password hashing answer. Correct. Surface-level.

### With `ds-conductor` v2.1:
> The same question, but CONDUCTOR v2.1 automatically:
> 1. **Classifies the task** — extracts complexity, consequence, reversibility, novelty
> 2. **Runs BOUNDARY-DETECTOR first** — probes knowledge boundaries, detects voids
> 3. **Auto-selects skills** — DEEP-THINK → DIVERGE → ADVERSARY → TEMPORAL → THRESHOLD
> 4. **Sequences with interference validation** — verifies each skill feeds the next
> 5. **Runs meta-learning post-execution** — extracts patterns, updates policy
> 6. **Verifies with ungameable gates** — held-out tasks, ensemble critic, red-team
> 7. **Auto-stops** — when ADS target met, diminishing returns, ADS/CEI peaks
> 8. **Outputs Depth Report** — cryptographically signed, reproducible
>
> → You get a **Principal Engineer-level answer** with **Depth Report** (ADS=0.73, CEI=4.8, SI=18, EC=0.73, OV=0.42) — **automatically**.

**The difference is not more words. It's measurable, verified, automatic depth.**

---

## The Skill Map — Where to Go Next

After `ds-conductor` (which does everything automatically), you can also use skills manually:

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

"I want to solve novel problems safely"
  → boundary-detector (probe knowledge boundaries first)

"I want the system to self-improve"
  → meta-learning (extract patterns, synthesize skills, update policy)

"I want final verification"
  → verification-gates (ungameable gates, red-team, depth report)
```

---

## How Skills Work Together

**Automatic (recommended):** Just use `ds-conductor` v2.1 — it handles everything.

**Manual chaining (if needed):**
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
├── README.md              ← Architecture guide (this file)
├── QUICKSTART.md          ← You are here
├── CHANGELOG.md           ← Version history
├── CONTRIBUTING.md        ← How to contribute
├── LICENSE                ← MIT License
├── benchmark/             ← Benchmarking framework
│   ├── run.py
│   ├── score.py
│   ├── report.py
│   ├── params_standard.json
│   ├── params_deep.json
│   ├── requirements.txt
│   └── report.md
├── tests/                 ← Built-in Evaluation Protocol + Results
│   ├── test_prompts.json
│   ├── eval.md
│   └── RESULTS.md
└── skills/                ← The Skill Library (19 Cognitive + 4 Premium + 7 Domain)
   ├── ds-core/            ← Mathematical framework (MATHEMATICS.md)
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
   ├── ds-boundary-detector/
   ├── ds-meta-learning/
   ├── ds-verification-gates/
   ├── ds-clarify/
   ├── ds-shallow/
   ├── ds-teach/
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

**Q: Do I need all 26 skills?**
No. Start with `ds-conductor` alone — it automatically selects and runs the right skills. Add others manually only if you need fine-grained control.

**Q: Do these work with any AI model?**
Yes. They're model-agnostic markdown instructions. Any model that reads skill/instruction files can use them.

**Q: What's the difference between cognitive skills and domain skills?**
`skills/ds-*` contains cognitive-mode skills — they change HOW the model thinks, regardless of domain. `skills/product-engineer` etc. are domain skills — they provide expert knowledge for WHAT the model thinks about (APIs, mobile, performance, etc.). They compose: use `deep-think` + `system-architect` for deep architectural reasoning.

**Q: What's new in v2.x vs v1.x?**
| Feature | v1.x | v2.x |
|---|---|---|
| Orchestration | Manual | **Automatic (CONDUCTOR v2.1)** |
| Boundary Detection | None | **BOUNDARY-DETECTOR (UnknownBench probes)** |
| Meta-Learning | None | **META-LEARNING (pattern extraction, skill synthesis)** |
| Verification | Self-reported | **Ungameable gates (held-out, ensemble, red-team)** |
| Metrics | Qualitative | **Mathematical (ADS, CEI, SI, EC, OV, CIM, RSM)** |
| Stopping | Manual | **Auto-stop (ADS target, diminishing returns, ADS/CEI peak)** |
| Depth Report | None | **Cryptographically signed Depth Report** |

**Q: How are skills versioned?**
Each skill has a version in its frontmatter (e.g., `version: 2.0`). Check CHANGELOG.md for updates.

---

## Run Benchmarks

```bash
# Install dependencies
pip install -r benchmark/requirements.txt

# Run control (old skills)
python benchmark/run.py --skills-dir skills_old --prompts tests/test_prompts.json --model gpt-4 --skills-version v1.x --thinking-params benchmark/params_standard.json --output benchmark/results_control.json

# Run treatment (premium skills)
python benchmark/run.py --skills-dir skills --prompts tests/test_prompts.json --model gpt-4 --skills-version v2.x --thinking-params benchmark/params_deep.json --output benchmark/results_treatment.json

# Score and compare
python benchmark/score.py --control benchmark/results_control.json --treatment benchmark/results_treatment.json --output benchmark/comparison.json

# Generate report
python benchmark/report.py --comparison benchmark/comparison.json --output benchmark/report.md
```