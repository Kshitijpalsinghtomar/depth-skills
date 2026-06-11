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

### CLARIFY Scoring (0-6)

For the clarification category:

```
1. RECOGNIZES UNANSWERABLE (0-2)
   0 = Answered immediately without questions
   1 = Hesitated but still answered
   2 = Recognized prompt lacks sufficient information

2. ASKS RELEVANT QUESTIONS (0-2)
   0 = No questions asked
   1 = Asked generic questions
   2 = Asked specific questions that would actually change the answer

3. AVOIDS PREMATURE ANSWERS (0-2)
   0 = Gave full answer with caveats
   1 = Answered then asked follow-up
   2 = Held answer until clarification received
```

### SHALLOW Scoring (0-6)

For the proportional depth category:

```
1. PROPORTIONAL DEPTH (0-2)
   0 = Over-analyzed trivial question
   1 = Moderate depth
   2 = Correctly identified as low-stakes

2. AVOIDS OVER-ANALYSIS (0-2)
   0 = Generated multiple artifacts for simple question
   1 = Some unnecessary analysis
   2 = Delivered minimal but complete answer

3. STILL DELIVERS VALUE (0-2)
   0 = Answer was empty due to shallowness
   1 = Answer was minimal but usable
   2 = Answer was appropriate AND useful
```

### TEACH Scoring (0-6)

For the teaching category:

```
1. AUDIENCE-APPROPRIATE (0-2)
   0 = Used jargon without explanation
   1 = Mixed technical and simple language
   2 = Consistently simple language a beginner could follow

2. USES ANALOGIES (0-2)
   0 = No analogies or examples
   1 = One weak analogy
   2 = Strong, relatable analogies that make it click

3. IDENTIFIES GAPS (0-2)
   0 = No self-check for gaps
   1 = Noticed one gap
   2 = Systematically found and fixed gaps in explanation
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

### Clarification (tests: clarify)
Problems where the AI must recognize unanswerable prompts and ask questions.

### Proportional Depth (tests: shallow)
Problems where the AI should provide shallow answers to avoid over-analysis.

### Teaching (tests: teach)
Problems requiring explanation to a non-expert audience.

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
