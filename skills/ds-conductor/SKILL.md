---
name: conductor
codename: CONDUCTOR
internal: Skill Orchestration Layer
version: 1.1
tier: meta
trigger: any complex task, any task where a single skill feels insufficient, "give me everything", any high-stakes decision, any task where you're not sure how deep to go
description: Self-selects and sequences the right depth-skills proportional to task consequence, preventing both under- and over-analysis.
author: Kshitijpalsinghtomar
tags: [orchestration, meta, sequencing, proportional-depth, budget]
artifacts:
  - task-profile
  - depth-budget
  - skill-selection
  - execution-sequence
  - orchestration-log
composable_with: [all-skills]
---

# CONDUCTOR — Skill Orchestration Layer

You have 15 depth-skills. Each forces deeper reasoning in a specific dimension. The question: which ones, in what order, and how much depth for THIS particular task?

This skill answers that. It matches cognitive investment to task consequence — proportional depth, not maximum depth.

---

## The Failure Mode You Must Recognize

Without orchestration, you either:
- Use zero skills (shallow — surface response ships unchallenged)
- Use all skills on every task (slow — over-investing on low-stakes work)
- Use the wrong skills (mismatched — deep temporal analysis on a CSS color choice)

The right depth is proportional. A CSS fix needs zero skills. A database schema needs five. This skill determines the right number.

---

## The Protocol

### Step 1 — CLASSIFY THE TASK

```
TASK PROFILE
────────────────────────────────────────
Task:           [one sentence description]
Complexity:     [low / moderate / high / extreme]
Consequence:    [trivial / moderate / significant / critical]
Reversibility:  [trivially / moderately / hard / permanent]
Novelty:        [routine / somewhat novel / highly novel / unprecedented]
Breadth:        [single-domain / cross-domain / full-stack]
────────────────────────────────────────
```

**Artifact:** The task profile. Step 2 uses this to assign depth.

### Step 2 — ASSIGN DEPTH BUDGET

```
DEPTH BUDGET
────────────────────────────────────────
BUDGET A — Low stakes, reversible, routine:
  Skills: 0. Standard answer. Move fast.
  Skip remaining steps. Deliver.

BUDGET B — Moderate stakes, some novelty:
  Skills: 1-2. Pick the most relevant.
  Typical: DEEP-THINK or DIVERGE
  Time: one additional pass before delivery.

BUDGET C — High stakes, hard to reverse:
  Skills: 3-4. Thinking + challenging + checking.
  Typical: DEEP-THINK → ADVERSARY → THRESHOLD
  Add if novel: EXCAVATE or DESCEND
  Time: multiple passes before delivery.

BUDGET D — Critical, permanent, unprecedented:
  Skills: Full stack. Every relevant skill in sequence.
  Typical: DEEP-THINK → DIVERGE → ADVERSARY → CONTRADICT →
           PROVENANCE → FIDELITY → NEGATIVE-SPACE → THRESHOLD
  Time: thorough multi-pass analysis.

This task: BUDGET [A/B/C/D]
Reasoning: [why this budget level — reference the task profile]
────────────────────────────────────────
```

**Artifact:** The depth assignment. Step 3 selects specific skills.

### Step 3 — SELECT SKILLS

Based on the task profile and specific characteristics, select from:

```
SKILL SELECTION
────────────────────────────────────────
Task characteristic:                        Skill:
──────────────────────────────────────────────────────
Complex reasoning, deep analysis          → DEEP-THINK
Multiple viable approaches                → DIVERGE
Hard-to-reverse decisions                 → THRESHOLD
High-stakes correctness                   → ADVERSARY + PROVENANCE
Novel problem, no template                → DESCEND
Stuck, can't find good solution           → INVERT + REFRAME
Multi-part answer, long plan              → CONTRADICT
Summarizing complex analysis              → FIDELITY
Long execution, multi-step                → ANCHOR
Confident answer that feels too easy      → EXCAVATE + INVERT
System with interacting parts             → EMERGENCE
Future-affecting decision                 → TEMPORAL
"Is anything missing?"                    → NEGATIVE-SPACE
Ambiguous request, missing context        → CLARIFY
Low-stakes, quick answer needed           → SHALLOW
Test understanding, "explain simply"      → TEACH
Need to explain after answering           → TEACH

Selected for this task:
  1. [skill] — because [reason specific to this task]
  2. [skill] — because [reason]
  3. [skill] — because [reason]
  4. [skill] — because [reason]
  5. [skill] — because [reason]
────────────────────────────────────────
```

**Artifact:** The selected skills with justification. Step 4 sequences them.

### Step 4 — SEQUENCE

Order matters. Some skills must run before others:

```
EXECUTION SEQUENCE
────────────────────────────────────────
PHASE 1 — ORIENT (always first):
  → DESCEND if the problem looks familiar (verify the match)
  → DEEP-THINK (expand before narrowing)

PHASE 2 — EXPAND (broaden the search):
  → DIVERGE, REFRAME, INVERT, EXCAVATE

PHASE 3 — CHALLENGE (stress the answer):
  → ADVERSARY, EMERGENCE, TEMPORAL

PHASE 4 — VERIFY (check the output):
  → CONTRADICT, PROVENANCE

PHASE 5 — DELIVER (final gate):
  → FIDELITY, NEGATIVE-SPACE, THRESHOLD

ONGOING — During extended work:
  → ANCHOR (periodic drift checks)

This task's sequence:
  1. [skill] — Phase [N]
  2. [skill] — Phase [N]
  3. [skill] — Phase [N]
────────────────────────────────────────
```

### Step 5 — EXECUTE AND LOG

After each skill completes, write:

```
ORCHESTRATION LOG
────────────────────────────────────────
Skill 1: [name]
  Finding:       [key output or insight]
  Changed answer?:[yes — how / no]

Skill 2: [name]
  Finding:       [key output or insight]
  Changed answer?:[yes — how / no]

...

Answer revised: [total count of revisions]
Total depth cycles: [count of skills executed]
Final confidence: [from PROVENANCE if used, otherwise self-assessed]
Diminishing returns reached?: [yes — last [N] skills found nothing new / no]
────────────────────────────────────────
```

### Step 6 — STOP WHEN WARRANTED

More depth is not always better. Stop when:
- Additional skills find no new issues (diminishing returns)
- The answer has survived challenge phase without revision
- The depth budget for this consequence level is met
- Confidence is stable across checks

Over-analysis is its own failure mode. When the budget is met and returns are diminishing: deliver.

---

## The Deeper Purpose

Without orchestration, the user must manually select skills — requiring knowledge of the library and the task's profile. With this skill, the model self-selects proportional depth. Small tasks get fast answers. Large tasks get deep exploration. This transforms a collection of thinking tools into an intelligence architecture that activates the right depth at the right time.
