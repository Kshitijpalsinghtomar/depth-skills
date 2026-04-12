# Evaluation Results

> Community-tested evidence that depth-skills change reasoning quality.

## How to Contribute

Run the [eval protocol](eval.md) and add your results below.

---

## Results Log

### Test 1
- **Challenge:** #6 — API randomly returns 500 errors under load (2% at 5000 req/s, "connection reset by peer" from PostgreSQL)
- **Skills:** DESCEND + EXCAVATE
- **Model:** Gemini (self-eval)
- **Control score:** 2/10
- **Treatment score:** 10/10
- **Delta:** +8
- **Key finding:** The control immediately pattern-matched to "connection pool exhaustion" and prescribed standard fixes (increase pool, add PgBouncer). The skills caught a **critical anomaly the control completely ignored**: the 2% failure rate *contradicts* pool exhaustion (which creates bursts of 100% failure, not steady 2%). DESCEND's pattern audit revealed 1 broken and 3 uncertain preconditions. EXCAVATE surfaced the invisible architecture assumption — the possibility of a proxy/PgBouncer layer the team never mentioned, which changes the entire diagnosis.

| Dimension | Control | Treatment |
|---|---|---|
| Surface coverage | 2 | 2 |
| Hidden dimensions | 0 | 2 |
| Assumption quality | 0 | 2 |
| Alternative paths | 0 | 2 |
| Evidence calibration | 0 | 2 |
| **Total** | **2/10** | **10/10** |

**Without skills:** "Increase your connection pool." (Standard answer, possibly wrong.)
**With skills:** "The 2% rate tells us this ISN'T pool exhaustion. Here's what to actually investigate." (Correct diagnostic approach.)

---

*Add your own results — open a PR or issue with your before/after comparison.*
