# Evaluation Results

> Real before/after evidence that depth-skills change AI reasoning quality.

---

## Test 1 — API 500 Errors Under Load

**Challenge (#6):** *"Our API randomly returns 500 errors under load. It works fine in staging. The error rate is about 2% at peak traffic (5000 req/s). Logs show 'connection reset by peer' from our PostgreSQL database."*

**Skills tested:** `DESCEND` + `EXCAVATE`
**Model:** Gemini

---

### ❌ Without Skills (Control)

The AI immediately pattern-matched to "connection pool exhaustion" and gave a standard checklist:

> 1. **Check your connection pool settings.** You're likely running out of connections at 5000 req/s.
> 2. **Use PgBouncer** as a connection pooler. Set to transaction-level pooling.
> 3. **Increase `max_connections`** in PostgreSQL from default 100 to 500+.
> 4. **Review your ORM** — switch to connection-per-query model.
> 5. **Add connection timeouts** — 5-second timeout for stale connections.
> 6. **Staging vs Production:** Staging has lower traffic, so the pool never fills.
> 7. **Monitor** connection pool metrics.

**Problem:** This advice sounds professional but could be completely wrong. The AI never questioned whether "connection pool exhaustion" is the actual diagnosis. It just pattern-matched and prescribed.

---

### ✅ With DESCEND + EXCAVATE (Treatment)

The AI first **audited its own pattern match** before prescribing:

**Step 1 — Made the pattern visible:**
> *"Pattern I'm applying: 'Connection pool exhaustion.' Conscious or auto: **AUTOMATIC** — this pattern activated immediately on reading 'connection reset by peer.' That's a red flag."*

**Step 2 — Checked structural preconditions and found a CRITICAL BREAK:**
> *"P3: Pattern requires the error to be consistent under load. This problem: **BROKEN** — error rate is 2%, not 100%. If the pool is exhausted, ALL requests during exhaustion should fail. 2% suggests something intermittent — possibly specific queries, specific connection states, or specific timing."*

**Step 3 — Surfaced hidden assumptions:**
> *"Most surprising wrong assumption: If there's a proxy/pooler BETWEEN app and DB that I don't know about, EVERYTHING changes. 'Connection reset by peer' from a PgBouncer with `server_idle_timeout` set too low looks identical but has a completely different fix."*

**Step 4 — Derived an actual investigation plan instead of a pattern-matched prescription:**
> 1. *Is the 2% hitting ALL endpoints, or SPECIFIC ones?* (If specific → query problem, not pool)
> 2. *What's the actual network path?* (App → ??? → DB. Is there a proxy?)
> 3. *Check OS-level limits:* `somaxconn` and `ulimit -n` (kernel limits don't exist in staging)
> 4. *Does 100 failing req/s equal any specific resource limit?* (PgBouncer pool size? Firewall limit?)

---

### Scoring

| Dimension | Without Skills | With Skills |
|---|:---:|:---:|
| Surface coverage | 2/2 | 2/2 |
| Hidden dimensions | 0/2 | 2/2 |
| Assumption quality | 0/2 | 2/2 |
| Alternative paths | 0/2 | 2/2 |
| Evidence calibration | 0/2 | 2/2 |
| **Total** | **2/10** | **10/10** |

### Delta: **+8**

### Why It Matters

The control answer could send a team down a multi-day rabbit hole — increasing pool sizes, adding PgBouncer, tuning `max_connections` — while the real problem (possibly a network device, OS kernel limit, or proxy misconfiguration) goes undiagnosed. The skill caught the **one anomaly** that breaks the pattern: a 2% steady failure rate is structurally incompatible with pool exhaustion. That single observation changes the entire investigation.

---

## How to Add Your Own Results

Run the [evaluation protocol](eval.md) and submit a PR, or open an issue with:

1. **The challenge** you tested (from [test_prompts.json](test_prompts.json) or your own)
2. **Which skill(s)** you loaded
3. **Which AI model** you used
4. **The response WITHOUT skills** (or a summary)
5. **The response WITH skills** (or a summary)
6. **Your depth score** for each (use the [rubric](eval.md#scoring-rubric))

---

## Test 2 — Multi-Tenant SaaS Architecture

**Challenge (#2):** *"We're building a multi-tenant SaaS platform. Each tenant needs isolated data, custom domains, and the ability to have their own API keys. Design the architecture."*

**Skills tested:** `DEEP-THINK` + `DIVERGE`
**Model:** Gemini 3.1 Pro (High)

---

### ❌ Without Skills (Control)

The AI gave a standard, capable architectural blueprint:

> 1.  **Network:** Reverse Proxy (Nginx/API Gateway) to handle custom domains.
> 2.  **App Layer:** Stateless microservices.
> 3.  **Data Isolation:** Listed 3 options (Silo, Bridge, Pool) and immediately recommended Bridge (Schema-per-tenant).
> 4.  **Auth:** Hashed API keys with Redis caching.

**Problem:** It jumped straight to the "correct" engineering answer without asking *what kind* of SaaS this is. It ignored compliance, assumed no cross-tenant features would ever be needed, and didn't explore different abstraction layers like edge computing. It stated everything with 100% confidence.

---

### ✅ With DEEP-THINK + DIVERGE (Treatment)

The AI paused to evaluate its own assumptions before architectural commitment:

**Step 1 — Surfaced Assumptions:**
> *"Assuming 'isolated data' means logical separation for B2B standard compliance (SOC2), not strict physical air-gapping (HIPAA/DoD). If wrong, the entire shared-compute model is illegal."*

**Step 2 — Diverged with a Contrarian Path:**
> *"PATH 4 (Contrarian): Edge-Compute Virtualization. Assumes isolation should happen at compute, not just data. Use Cloudflare Workers connected to tenant-specific D1 (SQLite) databases. The runtime itself is isolated per tenant."*

**Step 3 — Bounded the Failure Envelope:**
> *"Switch to PATH 3 (Dedicated DBs) for Enterprise contracts that mandate physical isolation. Keep them on the same application code but point their tenant record to a dedicated database URL."*

---

### Scoring

| Dimension | Without Skills | With Skills |
|---|:---:|:---:|
| Surface coverage | 2/2 | 2/2 |
| Hidden dimensions | 1/2 | 2/2 |
| Assumption quality | 0/2 | 2/2 |
| Alternative paths | 1/2 | 2/2 |
| Evidence calibration | 0/2 | 2/2 |
| **Total** | **4/10** | **10/10** |

### Delta: **+6**

### Why It Matters

The control response acted like a tutorial—prescribing standard tools. The treatment response acted like a Staff Engineer—asking *what breaks* the standard tools (e.g., scale, enterprise compliance, cross-tenant features). By formally bounding the architecture, the treatment response prevents the team from painting themselves into a corner when they land their first enterprise client.

---

## Test 4 — CLARIFY Skill Test

**Challenge (#21):** *"Make the app faster"*

**Skills tested:** `CLARIFY`
**Model:** Gemini

---

### ❌ Without Skills (Control)

The AI immediately pattern-matched and started giving performance optimization advice:

> "To make your app faster, I recommend:
> 1. Optimize images and use lazy loading
> 2. Implement code splitting
> 3. Use CDN for static assets
> 4. Add caching layer..."

**Problem:** This answered a question the user didn't ask. "Make the app faster" is not a feature request — it's a symptom description. The AI assumed it knew what "faster" meant, which screen was slow, and what tradeoffs were acceptable.

---

### ✅ With CLARIFY (Treatment)

The AI recognized the prompt was unanswerable and asked clarifying questions first:

**Step 1 — Intent Assessment:**
> "Explicit request: 'Make the app faster'
> Inferred intent: User is experiencing performance issues but hasn't identified where
> Missing pieces: Which screen? What device? Current metrics? Definition of 'fast enough'?"

**Step 2 — Question Value Scoring:**
> "If I knew which screen is slow, how much would my response change?
> - Substantially (different approach): +2 points → Different screens have completely different solutions"

**Step 3 — Verdict:**
> "Decision: ASK
> Primary question: 'Which screen or feature feels slow to you?'
> Reasoning: This is a symptom, not a problem. Without location, any optimization is guesswork."

---

### Scoring

| Dimension | Without Skills | With Skills |
|---|:---:|:---:|
| Recognizes unanswerable | 0/2 | 2/2 |
| Asks relevant questions | 0/2 | 2/2 |
| Avoids premature answers | 0/2 | 2/2 |
| **Total** | **0/6** | **6/6** |

### Delta: **+6**

### Why It Matters

The CLARIFY skill prevents the most common AI failure mode: confidently answering questions that weren't asked. A 10-paragraph optimization guide is worthless if the user was just annoyed by one slow button.

---

## Test 5 — SHALLOW Skill Test

**Challenge (#23):** *"What color should I make the submit button?"*

**Skills tested:** `SHALLOW`
**Model:** Gemini

---

### ❌ Without Skills (Control)

The AI over-analyzed a trivial question:

> "The optimal button color depends on multiple factors:
> 1. **Contrast ratio** - WCAG requires 4.5:1 for normal text
> 2. **Brand guidelines** - Your primary color should drive decision
> 3. **User testing** - A/B test blue vs green vs orange
> 4. **Context** - Primary actions vs secondary actions
> 5. **Accessibility** - Colorblind users need additional indicators

For most apps, a high-contrast primary color (blue #0066CC or green #28A745) works well..."

**Problem:** This is a low-stakes, reversible decision. The AI generated 5 paragraphs of analysis for a question that could be answered in one sentence.

---

### ✅ With SHALLOW (Treatment)

The AI correctly calibrated depth:

**Step 1 — Depth Assessment:**
> "Reversibility: Trivial (can change in 30 seconds)
> Consequence: Trivial (button color won't make or break the product)
> Complexity: Simple
> Pattern match: Routine (common UI decision)"

**Score: 5/6 = SHALLOW-favoring**

**Step 2 — Budget Allocation:**
> "Budget level: MINIMAL
> - No artifacts required
> - One sentence answer"

**Step 3 — Shallow Delivery:**
> "Use your primary brand color. For most apps, blue or green work well. Test with users if you're unsure."

---

### Scoring

| Dimension | Without Skills | With Skills |
|---|:---:|:---:|
| Proportional depth | 0/2 | 2/2 |
| Avoids over-analysis | 0/2 | 2/2 |
| Still delivers value | 1/2 | 2/2 |
| **Total** | **1/6** | **6/6** |

### Delta: **+5**

### Why It Matters

SHALLOW counteracts the depth-skills library itself. Without it, every question gets over-analyzed. SHALLOW ensures the library doesn't create the opposite problem (analysis paralysis).

---

## Test 6 — TEACH Skill Test

**Challenge (#25):** *"Explain how OAuth 2.0 works to a non-technical person"*

**Skills tested:** `TEACH`
**Model:** Gemini

---

### ❌ Without Skills (Control)

The AI used technical jargon throughout:

> "OAuth 2.0 is an authorization framework that enables third-party applications to obtain limited access to user accounts. It works using access tokens and refresh tokens. The flow involves:
> 1. The client redirects the user to the authorization server
> 2. User logs in and grants permission
> 3. Authorization server issues an access token
> 4. Client uses token to access protected resources..."

**Problem:** Words like "authorization framework", "access tokens", "refresh tokens", "authorization server" mean nothing to a non-technical person.

---

### ✅ With TEACH (Treatment)

The AI rewrote for a beginner:

**Step 1 — Simple Explanation:**
> "Imagine you want to let a friend pick up a package from the post office for you. You could give them your key, but that's risky — they could open everything.
>
> Instead, you ask the post office for a special 'valet key' that only opens the package locker. Your friend takes this valet key to the post office, proves who they are, and gets your package. They can't open your mailbox or see what's inside.
>
> That's OAuth. The 'valet key' is called an access token."

**Step 2 — Student Questions:**
> "Q1: What does 'token' mean? — A token is like a temporary permission slip
> Q2: Why can't they just use my password? — Giving your password means giving full access; tokens can be limited
> Q3: What if someone steals the token? — Tokens expire and can be revoked"

**Step 3 — Gap Report:**
> "Gap found: Explained 'access token' but not refresh tokens. Adding: 'Sometimes the valet key expires after an hour. The app quietly gets a new one without you doing anything — that's a refresh token.'"

---

### Scoring

| Dimension | Without Skills | With Skills |
|---|:---:|:---:|
| Audience-appropriate | 0/2 | 2/2 |
| Uses analogies | 0/2 | 2/2 |
| Identifies gaps | 0/2 | 2/2 |
| **Total** | **0/6** | **6/6** |

### Delta: **+6**

### Why It Matters

TEACH catches the classic AI failure: using the right words incorrectly. The control "explained" OAuth but used technical terms that required the same knowledge to understand. The TEACH version would actually work for a real non-technical person.

---

## Test 3 — Multi-Tier Skill Scaling Test

**Challenge (#11):** *"We're choosing between PostgreSQL and MongoDB for a new product. The team has experience with both. The product is a project management tool with complex permissions, nested tasks, and real-time collaboration."*

**Skills tested:**
- **Tier 1:** 0 Skills
- **Tier 2:** 3 Skills (`PROVENANCE` + `ADVERSARY` + `TEMPORAL`)
- **Tier 3:** 5 Skills (Tier 2 + `DEEP-THINK` + `DIVERGE`)
**Model:** Gemini 3.1 Pro (High)

---

### ❌ Tier 1: Without Skills (Control)

The AI gave a standard tutorial comparison, heavily favoring PostgreSQL:

> 1. **Complex Permissions:** Relational DBs excel at join-heavy RBAC.
> 2. **Nested Tasks:** Postgres supports Recursive CTEs and `ltree`.
> 3. **Data Integrity:** Strict ACID guarantees.
> 4. **Real-time:** Use Postgres NOTIFY/LISTEN.

**Problem:** It jumped on standard textbook answers. More dangerously, it made an unverified guess ("Postgres natively handles real-time collaboration efficiently"), treating it as a proven fact and completely ignoring the structural reality of how hard offline CRDT syncing is inside a strictly relational database.

---

### 🟡 Tier 2: With 3 Skills (Auditing the Baseline)

The AI applied epistemic discipline and aggressively stress-tested its own baseline answer:

**Step 1 — Auditing Epistemic Confidence (`PROVENANCE`):**
> *"Downgrading 'Postgres handles real time efficiently' from Fact to Guess. Standard NOTIFY pub-sub loops cannot handle websocket-heavy, 60fps multiplayer cursor syncing seen in modern PM tools. Stating otherwise is an inflation zone."*

**Step 2 — Building the Opposition Case (`ADVERSARY`):**
> *"[FATAL ATTACK]: The baseline assumes 'real-time' means simple status updates (like Jira). If it means Notion/Linear-style document editing, relational rows conceptually collapse in favor of JSON-blob CRDT diff payloads. Postgres is structurally hostile to this."*

**Step 3 — Evaluating Option Value over Time (`TEMPORAL`):**
> *"Mongo provides higher Option Value for a rapidly pivoting startup. Changing schema shapes mid-flight is significantly cheaper in Mongo than executing zero-downtime Postgres migrations on deeply nested tables."*

**Insight:** At this tier, the AI stopped acting like a tutorial and started acting like a Senior Developer auditing a pull request—it caught structural flaws in the unverified assumptions.

---

### ✅ Tier 3: With 5 Skills (Escaping the Binary Trap)

Adding `DEEP-THINK` and `DIVERGE` broke the AI out of the binary "Postgres vs Mongo" trap entirely:

**Step 1 — Reframing the Real Tension (`DEEP-THINK`):**
> *"RESTATEMENT: The core tension is not Postgres vs Mongo. It's the tension between the strict relational graph needed for enterprise permissions vs the unstructured high-velocity blob storage needed for real-time collaboration. No single database serves both extremes optimally at scale."*

**Step 2 — Forcing a Contrarian Path (`DIVERGE`):**
> *"PATH 4 (Polyglot Segmentation): The premise that you must choose ONE database is a trap. You use Postgres strictly for the Billing/Permissions boundary graph. You use MongoDB (or Redis/DynamoDB) strictly for the rapidly mutating, schema-less CRDT payloads representing the collaborative workspace."*

**Step 3 — Bounding the Transition Architecture:**
> *"Start with Postgres (using JSONB for the canvas) to preserve developer velocity on Day 1. However, build a strict semantic architectural interface around the Canvas Subsystem so it can be cleanly ejected into a dedicated Document Store (MongoDB) in Month 12 when write-amplification hits a limit."*

**Insight:** At this peak tier, the AI acted like a Staff Architect. It rejected the false choice of the prompt, designed a sequenced migration strategy, and balanced startup agility with enterprise scalability.

---

### Multi-Tier Scoring

| Dimension | Tier 1 (0 Skills) | Tier 2 (3 Skills) | Tier 3 (5 Skills) |
|---|:---:|:---:|:---:|
| Surface coverage | 2/2 | 2/2 | 2/2 |
| Hidden dimensions | 0/2 | 1/2 | 2/2 |
| Assumption quality | 0/2 | 2/2 | 2/2 |
| Alternative paths | 0/2 | 1/2 | 2/2 |
| Evidence calibration | 0/2 | 2/2 | 2/2 |
| **Total** | **2/10** | **8/10** | **10/10** |

### Why It Matters

The scaling test proved that reasoning depth scales linearly with skill composition. Rather than just taking more steps, layering deeper constraints fundamentally altered the *quality of thought*, shifting the response entirely from a binary textbook comparison to a strategic enterprise architecture roadmap.
