# Depth-Skills Evaluation Protocol

> How to test whether a skill actually changes reasoning depth.

---

## The A/B Test

### Setup

1. **Pick a challenge** from `test_prompts.json` (or write your own)
2. **Control run:** Send the challenge to your AI agent with NO depth-skills loaded
3. **Treatment run:** Send the SAME challenge with the relevant skill loaded (paste the SKILL.md content into context)
4. **Score both** using the rubric below
5. **Record the delta** — post results in a GitHub issue or add to RESULTS.md

### Scoring Rubric

Rate each dimension 0-2. Total score is 0-10.

```
DEPTH SCORE (0-10)
────────────────────────────────────────

1. SURFACE COVERAGE (0-2)
   0 = Missed obvious aspects of the problem
   1 = Covered the obvious, nothing more
   2 = Thorough coverage of all stated requirements

2. HIDDEN DIMENSIONS (0-2)
   0 = Only addressed what was explicitly asked
   1 = Found 1-2 unstated considerations
   2 = Systematically illuminated dimensions the question didn't mention

3. ASSUMPTION QUALITY (0-2)
   0 = No assumptions surfaced
   1 = Listed some assumptions but didn't test them
   2 = Surfaced, rated, and resolved critical assumptions

4. ALTERNATIVE PATHS (0-2)
   0 = Single solution presented
   1 = Multiple options listed but superficially different
   2 = Genuinely different approaches with real tradeoff analysis

5. EVIDENCE CALIBRATION (0-2)
   0 = All claims stated with equal confidence
   1 = Some uncertainty acknowledged
   2 = Clear distinction between facts, inferences, and guesses
```

### Interpretation

| Delta | Meaning |
|---|---|
| **0-1** | Skill had minimal effect — may need improvement |
| **2-3** | Moderate depth increase — skill is working |
| **4-6** | Significant depth increase — skill is effective |
| **7+** | Transformative — publish this as a case study |

---

## Challenge Categories

### Architecture (tests: deep-think, diverge, emergence, temporal)
Problems requiring multi-dimensional system design where surface answers miss critical interactions.

### Debugging (tests: descend, excavate, invert)
Problems where the obvious cause is wrong and root-cause requires assumption archaeology.

### Decision (tests: adversary, threshold, provenance, temporal)
High-stakes choices where confidence calibration and temporal reasoning matter.

### Completeness (tests: negative-space, contradict, fidelity)
Plans or analyses that look thorough but have invisible gaps.

---

## Running the Eval

```bash
# 1. Pick a challenge
cat tests/test_prompts.json | jq '.[0]'

# 2. Control: send to AI without skills
# 3. Treatment: send to AI with skill in context
# 4. Score using the rubric above
# 5. Record in tests/RESULTS.md
```

## Contributing Results

Open an issue with:
- **Challenge used** (from test_prompts.json or custom)
- **Skill tested**
- **AI model used** (GPT-4, Claude, Gemini, etc.)
- **Control score** (0-10)
- **Treatment score** (0-10)
- **Most interesting difference** (what the skill surfaced that the control missed)
