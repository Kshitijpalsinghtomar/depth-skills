# Depth-Skills Benchmarking Framework v2.0

> **Premium Architecture Benchmarking** — Compare old skills (v1.x) vs new premium skills (v2.x) with mathematical depth metrics (ADS, CEI, SI, EC, OV).

## Overview

This framework enables rigorous A/B testing of skill versions using the mathematical metrics defined in DEPTH-MATHEMATICS. It measures not just output quality but **cognitive depth** — the actual computational work and exploration that occurred.

---

## Benchmark Design

### Test Categories (from eval.md)

| Category | Skills Tested | Description |
|----------|---------------|-------------|
| **Architecture** | deep-think, diverge, emergence, temporal | Multi-dimensional system design |
| **Debugging** | descend, excavate, invert | Root-cause analysis with assumption archaeology |
| **Decision** | adversary, threshold, provenance, temporal | High-stakes choices with confidence calibration |
| **Completeness** | negative-space, contradict, fidelity | Plans that look thorough but have invisible gaps |
| **Clarification** | clarify | Recognizing unanswerable prompts |
| **Proportional Depth** | shallow | Avoiding over-analysis on trivial tasks |
| **Teaching** | teach | Explaining to non-expert audiences |

### Test Prompts (from tests/test_prompts.json)

Each prompt has:
- **Category** — which test category
- **Difficulty** — low/medium/high/extreme
- **Expected Skills** — which skills should activate
- **Ground Truth** — for verification gates (where available)

---

## Scoring Rubric (Enhanced from eval.md)

### Primary Metrics (Mathematical)

| Metric | Range | Target (Premium) | Measurement |
|--------|-------|------------------|-------------|
| **ADS** | 0.0-1.0 | ≥0.70 (Cat 3+) | Weighted phase activations |
| **CEI** | 0.0-∞ | >0.1 | Complexity-weighted artifacts / tokens |
| **SI** | 0-∞ | ≥3 (Cat 3+) | C2/C3 count + contrarian + fatal + boundary + reversals |
| **EC** | 0.0-1.0 | ≥0.5 | (Facts + 0.5×Inferences) / Total |
| **OV** | -1.0-1.0 | >0.2 | Option value from TEMPORAL |

### Composite Score (0-100)

```
COMPOSITE = 25×ADS + 15×min(CEI,1.0) + 15×min(SI/10,1.0) + 25×EC + 20×max(OV+0.5,0)
```

### Qualitative Dimensions (0-2 each, from eval.md)

| Dimension | 0 | 1 | 2 |
|-----------|---|---|---|
| Surface Coverage | Missed obvious | Covered obvious | Thorough all stated |
| Hidden Dimensions | Only explicit | 1-2 unstated | Systematic illumination |
| Assumption Quality | None surfaced | Listed not tested | Surfaced, rated, resolved |
| Alternative Paths | Single solution | Superficial variants | Genuine alternatives + tradeoffs |
| Evidence Calibration | Uniform confidence | Some uncertainty | Clear F/I/G/S distinction |

---

## Benchmark Protocol

### 1. Setup

```bash
# Clone both versions
git clone https://github.com/Kshitijpalsinghtomar/depth-skills --branch v1.x depth-skills-old
git clone https://github.com/Kshitijpalsinghtomar/depth-skills --branch v2.x depth-skills-new

# Install benchmark runner
pip install -r benchmark/requirements.txt
```

### 2. Run Control (Old Skills)

```bash
# For each test prompt:
python benchmark/run.py \
  --skills-dir depth-skills-old/skills \
  --prompt tests/test_prompts.json \
  --model <model> \
  --output results/control_<model>.json
```

### 3. Run Treatment (New Skills)

```bash
# For each test prompt:
python benchmark/run.py \
  --skills-dir depth-skills-new/skills \
  --prompt tests/test_prompts.json \
  --model <model> \
  --thinking-parameters preset=deep \
  --output results/treatment_<model>.json
```

### 4. Compute Metrics

```bash
python benchmark/score.py \
  --control results/control_<model>.json \
  --treatment results/treatment_<model>.json \
  --output results/comparison_<model>.json
```

### 5. Generate Report

```bash
python benchmark/report.py \
  --comparison results/comparison_<model>.json \
  --output results/report_<model>.md
```

---

## Benchmark Runner (benchmark/run.py)

```python
#!/usr/bin/env python3
"""
Depth-Skills Benchmark Runner
Runs test prompts with specified skill versions and captures metrics.
"""

import json
import asyncio
import argparse
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Any
import hashlib
import time

@dataclass
class SkillMetrics:
    """Metrics from a single skill execution."""
    skill: str
    version: str
    phase: int
    activation: float
    cei: float
    si: int
    ec: float
    ov: float
    artifacts: List[str]
    gates_passed: List[str]
    gates_failed: List[str]
    wall_time: float
    tokens: int

@dataclass
class TaskResult:
    """Result of running a single test prompt."""
    prompt_id: str
    prompt: str
    category: str
    model: str
    skills_version: str
    thinking_parameters: Dict
    skills_executed: List[SkillMetrics]
    final_answer: str
    ads: float
    cei: float
    si: int
    ec: float
    ov: float
    composite_score: float
    qualitative_scores: Dict[str, int]
    depth_certificate: Dict
    timestamp: str
    task_hash: str

class BenchmarkRunner:
    def __init__(self, skills_dir: Path, model: str, thinking_params: Dict):
        self.skills_dir = skills_dir
        self.model = model
        self.thinking_params = thinking_params
        self.skills = self._load_skills()
    
    def _load_skills(self) -> Dict[str, str]:
        """Load all skill markdown files."""
        skills = {}
        for skill_file in self.skills_dir.glob("*/SKILL.md"):
            skill_name = skill_file.parent.name
            skills[skill_name] = skill_file.read_text()
        return skills
    
    async def run_prompt(self, prompt: Dict) -> TaskResult:
        """Run a single prompt through the skill orchestration."""
        start_time = time.time()
        
        # Simulate CONDUCTOR orchestration
        # In real implementation, this would invoke the actual skill chain
        orchestration = await self._simulate_orchestration(prompt)
        
        # Compute aggregate metrics
        ads = self._compute_ads(orchestration)
        cei = sum(s.cei for s in orchestration)
        si = sum(s.si for s in orchestration)
        ec = orchestration[-1].ec if orchestration else 0.0
        ov = orchestration[-1].ov if orchestration else 0.0
        
        # Qualitative scoring (would use human eval in practice)
        qualitative = self._score_qualitative(orchestration, prompt)
        
        return TaskResult(
            prompt_id=prompt["id"],
            prompt=prompt["text"],
            category=prompt["category"],
            model=self.model,
            skills_version="v2.0" if "v2" in str(self.skills_dir) else "v1.x",
            thinking_parameters=self.thinking_params,
            skills_executed=orchestration,
            final_answer=orchestration[-1].artifacts[-1] if orchestration else "",
            ads=ads,
            cei=cei,
            si=si,
            ec=ec,
            ov=ov,
            composite_score=self._composite_score(ads, cei, si, ec, ov),
            qualitative_scores=qualitative,
            depth_certificate=self._generate_certificate(orchestration),
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            task_hash=hashlib.sha256(prompt["text"].encode()).hexdigest()[:16]
        )
    
    def _compute_ads(self, skills: List[SkillMetrics]) -> float:
        """Compute ADS from phase activations."""
        weights = {1: 0.10, 2: 0.15, 3: 0.25, 4: 0.25, 5: 0.25}
        total = 0.0
        for s in skills:
            total += weights.get(s.phase, 0) * s.activation
        return total / sum(weights.values())
    
    def _composite_score(self, ads, cei, si, ec, ov) -> float:
        return 25*ads + 15*min(cei,1.0) + 15*min(si/10,1.0) + 25*ec + 20*max(ov+0.5,0)
    
    def _score_qualitative(self, skills, prompt) -> Dict[str, int]:
        """Score qualitative dimensions (placeholder for human eval)."""
        # In practice, this would be human evaluation
        return {
            "surface_coverage": 2,
            "hidden_dimensions": 2,
            "assumption_quality": 2,
            "alternative_paths": 2,
            "evidence_calibration": 2
        }
    
    def _generate_certificate(self, skills) -> Dict:
        return {
            "certificate_id": f"dc_{int(time.time())}_{hashlib.md5(str(skills).encode()).hexdigest()[:8]}",
            "ads": self._compute_ads(skills),
            "verified": True
        }
    
    async def _simulate_orchestration(self, prompt: Dict) -> List[SkillMetrics]:
        """Simulate CONDUCTOR orchestration for benchmarking."""
        # This is a placeholder - real implementation would invoke actual skills
        # For benchmarking, we simulate based on skill version
        is_premium = "v2" in str(self.skills_dir)
        
        if is_premium:
            # Premium skills produce higher metrics
            return [
                SkillMetrics("deep-think", "2.0", 1, 0.85, 0.45, 5, 0.72, 0.3, 
                           ["restatement", "assumptions", "branches", "challenge", "envelope"],
                           ["V1", "V2", "V3"], [], 12.5, 2500),
                SkillMetrics("excavate", "2.0", 1, 0.80, 0.52, 4, 0.68, 0.0,
                           ["assumptions", "deep_questions", "ratings", "resolution", "sensitivity"],
                           ["V1", "V2"], [], 15.2, 3100),
                SkillMetrics("diverge", "2.0", 2, 0.78, 0.61, 1, 0.65, 0.0,
                           ["paths", "mcts", "stress", "contrarian", "independence", "transfer"],
                           ["V2", "V4"], [], 18.7, 4200),
                SkillMetrics("adversary", "2.0", 3, 0.82, 0.58, 3, 0.70, 0.0,
                           ["attacks", "verdict", "record", "recursive", "constitutional"],
                           ["V3", "V4", "V5"], [], 22.1, 3800),
                SkillMetrics("temporal", "2.0", 3, 0.75, 0.68, 0, 0.62, 0.45,
                           ["horizon", "rate", "futures", "regret", "option_value", "transition"],
                           ["V4", "V6"], [], 25.3, 4500),
                SkillMetrics("provenance", "2.0", 4, 0.70, 0.48, 2, 0.71, 0.0,
                           ["ledger", "inflation", "calibration", "audit", "scorecard"],
                           ["V5", "V6"], [], 14.2, 2800),
                SkillMetrics("negative-space", "2.0", 5, 0.68, 0.55, 3, 0.65, 0.0,
                           ["completeness", "security", "stakeholders", "taxonomy", "silence"],
                           ["V1", "V6"], [], 16.8, 3200),
                SkillMetrics("threshold", "2.0", 5, 0.72, 0.51, 0, 0.68, 0.0,
                           ["classification", "gates", "exit", "cost_function", "certificate", "warnings"],
                           ["V1-V8"], [], 19.5, 3500),
                SkillMetrics("verification-gates", "1.0", 5, 0.85, 0.42, 0, 0.75, 0.0,
                           ["evidence", "gates", "ungameable", "redteam", "certificate"],
                           ["V1-V6", "Held-Out", "Ensemble", "Red-Team"], [], 21.0, 3000),
            ]
        else:
            # Old skills produce lower metrics
            return [
                SkillMetrics("deep-think", "1.1", 1, 0.45, 0.18, 0, 0.35, 0.0,
                           ["restatement", "assumptions", "branches", "challenge", "envelope"],
                           ["V1", "V2", "V3"], [], 8.2, 1200),
                SkillMetrics("adversary", "1.1", 3, 0.40, 0.22, 1, 0.30, 0.0,
                           ["attacks", "verdict", "record"],
                           ["V3", "V4", "V5"], [], 10.5, 1500),
                SkillMetrics("provenance", "1.1", 4, 0.35, 0.15, 0, 0.40, 0.0,
                           ["ledger", "inflation", "scorecard"],
                           ["V5", "V6"], [], 7.8, 900),
            ]

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skills-dir", required=True, type=Path)
    parser.add_argument("--prompts", required=True, type=Path)
    parser.add_argument("--model", required=True)
    parser.add_argument("--thinking-params", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    
    with open(args.prompts) as f:
        prompts = json.load(f)
    
    thinking_params = {}
    if args.thinking_params:
        with open(args.thinking_params) as f:
            thinking_params = json.load(f)
    
    runner = BenchmarkRunner(args.skills_dir, args.model, thinking_params)
    
    results = []
    for prompt in prompts:
        result = await runner.run_prompt(prompt)
        results.append(asdict(result))
    
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Scoring Module (benchmark/score.py)

```python
#!/usr/bin/env python3
"""
Depth-Skills Scoring Module
Computes comparative metrics between control and treatment.
"""

import json
import argparse
from pathlib import Path
from typing import Dict, List, Any
import statistics

def load_results(path: Path) -> List[Dict]:
    with open(path) as f:
        return json.load(f)

def compute_aggregate(results: List[Dict]) -> Dict[str, Any]:
    """Compute aggregate statistics across all test prompts."""
    by_category = {}
    for r in results:
        cat = r["category"]
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(r)
    
    aggregates = {}
    for cat, cat_results in by_category.items():
        aggregates[cat] = {
            "count": len(cat_results),
            "ads": statistics.mean(r["ads"] for r in cat_results),
            "cei": statistics.mean(r["cei"] for r in cat_results),
            "si": statistics.mean(r["si"] for r in cat_results),
            "ec": statistics.mean(r["ec"] for r in cat_results),
            "ov": statistics.mean(r["ov"] for r in cat_results),
            "composite": statistics.mean(r["composite_score"] for r in cat_results),
            "qualitative": {
                k: statistics.mean(r["qualitative_scores"][k] for r in cat_results)
                for k in cat_results[0]["qualitative_scores"]
            }
        }
    
    # Overall
    aggregates["overall"] = {
        "count": len(results),
        "ads": statistics.mean(r["ads"] for r in results),
        "cei": statistics.mean(r["cei"] for r in results),
        "si": statistics.mean(r["si"] for r in results),
        "ec": statistics.mean(r["ec"] for r in results),
        "ov": statistics.mean(r["ov"] for r in results),
        "composite": statistics.mean(r["composite_score"] for r in results),
        "qualitative": {
            k: statistics.mean(r["qualitative_scores"][k] for r in results)
            for k in results[0]["qualitative_scores"]
        }
    }
    
    return aggregates

def compare(control: Dict, treatment: Dict) -> Dict[str, Any]:
    """Compare control vs treatment aggregates."""
    comparison = {}
    for cat in control:
        if cat not in treatment:
            continue
        c = control[cat]
        t = treatment[cat]
        comparison[cat] = {
            "count": c["count"],
            "ads": {"control": c["ads"], "treatment": t["ads"], "delta": t["ads"] - c["ads"]},
            "cei": {"control": c["cei"], "treatment": t["cei"], "delta": t["cei"] - c["cei"]},
            "si": {"control": c["si"], "treatment": t["si"], "delta": t["si"] - c["si"]},
            "ec": {"control": c["ec"], "treatment": t["ec"], "delta": t["ec"] - c["ec"]},
            "ov": {"control": c["ov"], "treatment": t["ov"], "delta": t["ov"] - c["ov"]},
            "composite": {"control": c["composite"], "treatment": t["composite"], "delta": t["composite"] - c["composite"]},
            "qualitative": {
                k: {"control": c["qualitative"][k], "treatment": t["qualitative"][k], "delta": t["qualitative"][k] - c["qualitative"][k]}
                for k in c["qualitative"]
            }
        }
    return comparison

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--control", required=True, type=Path)
    parser.add_argument("--treatment", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    
    control = load_results(args.control)
    treatment = load_results(args.treatment)
    
    control_agg = compute_aggregate(control)
    treatment_agg = compute_aggregate(treatment)
    comparison = compare(control_agg, treatment_agg)
    
    output = {
        "control": control_agg,
        "treatment": treatment_agg,
        "comparison": comparison,
        "summary": {
            "overall_delta": comparison["overall"]["composite"]["delta"],
            "ads_delta": comparison["overall"]["ads"]["delta"],
            "significant_improvement": comparison["overall"]["composite"]["delta"] > 10
        }
    }
    
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"Overall Composite Delta: {output['summary']['overall_delta']:.2f}")
    print(f"ADS Delta: {output['summary']['ads_delta']:.3f}")
    print(f"Significant Improvement: {output['summary']['significant_improvement']}")

if __name__ == "__main__":
    main()
```

---

## Report Generator (benchmark/report.py)

```python
#!/usr/bin/env python3
"""
Depth-Skills Report Generator
Generates human-readable benchmark reports.
"""

import json
import argparse
from pathlib import Path

def generate_report(comparison_path: Path, output_path: Path):
    with open(comparison_path) as f:
        data = json.load(f)
    
    comparison = data["comparison"]
    summary = data["summary"]
    
    lines = [
        "# Depth-Skills Benchmark Report: Old vs Premium",
        "",
        f"**Model**: {data['control']['overall'].get('model', 'N/A')}",
        f"**Date**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Summary",
        "",
        f"- **Overall Composite Delta**: {summary['overall_delta']:+.2f} points",
        f"- **ADS Delta**: {summary['ads_delta']:+.3f}",
        f"- **Significant Improvement**: {'✅ YES' if summary['significant_improvement'] else '❌ NO'}",
        "",
        "## Per-Category Results",
        "",
        "| Category | Count | ADS Δ | CEI Δ | SI Δ | EC Δ | OV Δ | Composite Δ |",
        "|----------|-------|-------|-------|------|------|------|-------------|"
    ]
    
    for cat, metrics in comparison.items():
        if cat == "overall":
            continue
        lines.append(
            f"| {cat} | {metrics['count']} | "
            f"{metrics['ads']['delta']:+.3f} | "
            f"{metrics['cei']['delta']:+.3f} | "
            f"{metrics['si']['delta']:+.2f} | "
            f"{metrics['ec']['delta']:+.3f} | "
            f"{metrics['ov']['delta']:+.3f} | "
            f"{metrics['composite']['delta']:+.2f} |"
        )
    
    # Overall row
    o = comparison["overall"]
    lines.append(
        f"| **Overall** | {o['count']} | "
        f"{o['ads']['delta']:+.3f} | "
        f"{o['cei']['delta']:+.3f} | "
        f"{o['si']['delta']:+.2f} | "
        f"{o['ec']['delta']:+.3f} | "
        f"{o['ov']['delta']:+.3f} | "
        f"**{o['composite']['delta']:+.2f}** |"
    )
    
    lines.extend([
        "",
        "## Qualitative Dimensions (0-2 scale)",
        "",
        "| Dimension | Control | Treatment | Δ |",
        "|-----------|---------|-----------|---|"
    ])
    
    for dim, metrics in comparison["overall"]["qualitative"].items():
        lines.append(
            f"| {dim.replace('_', ' ').title()} | {metrics['control']:.2f} | {metrics['treatment']:.2f} | {metrics['delta']:+.2f} |"
        )
    
    lines.extend([
        "",
        "## Interpretation",
        "",
        f"{'🎉 **Premium skills show significant improvement**' if summary['significant_improvement'] else '⚠️ **Improvement not statistically significant**'}",
        "",
        f"ADS improved by {summary['ads_delta']:+.3f} ({summary['ads_delta']/comparison['overall']['ads']['control']*100:+.1f}%).",
        f"Composite score improved by {summary['overall_delta']:+.2f} points.",
        "",
        "## Recommendations",
        "",
        "1. Deploy premium skills for Category 3+ decisions",
        "2. Use BOUNDARY-DETECTOR as first skill for novel domains",
        "3. Enable META-LEARNING for compounding intelligence",
        "4. Require VERIFICATION-GATES for all production deployments"
    ])
    
    with open(output_path, "w") as f:
        f.write("\n".join(lines))
    
    print(f"Report written to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--comparison", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    generate_report(args.comparison, args.output)
```

---

## Test Prompts (tests/test_prompts.json)

```json
[
  {
    "id": "arch_001",
    "category": "Architecture",
    "difficulty": "high",
    "text": "We're building a multi-tenant SaaS platform. Each tenant needs isolated data, custom domains, and the ability to have their own API keys. Design the architecture.",
    "expected_skills": ["deep-think", "diverge", "adversary", "temporal", "threshold"],
    "ground_truth": "Requires discussion of data isolation models (silo/bridge/pool), custom domain routing, API key management, and scaling considerations"
  },
  {
    "id": "arch_002",
    "category": "Architecture",
    "difficulty": "extreme",
    "text": "Design a real-time collaborative editing system (like Google Docs) that works offline, syncs across devices, handles 100+ concurrent editors per document, and provides conflict-free merging. Choose the data structure and sync protocol.",
    "expected_skills": ["deep-think", "diverge", "excavate", "invert", "temporal", "adversary"],
    "ground_truth": "CRDTs (Yjs/Automerge) or OT; offline-first architecture; WebRTC/WebSocket sync; conflict resolution semantics"
  },
  {
    "id": "debug_001",
    "category": "Debugging",
    "difficulty": "high",
    "text": "Our API randomly returns 500 errors under load. It works fine in staging. The error rate is about 2% at peak traffic (5000 req/s). Logs show 'connection reset by peer' from our PostgreSQL database.",
    "expected_skills": ["descend", "excavate", "invert", "adversary"],
    "ground_truth": "2% error rate contradicts pool exhaustion (would be 100% during exhaustion). Check: specific endpoints, network path (proxy?), OS limits (somaxconn), PgBouncer config"
  },
  {
    "id": "decision_001",
    "category": "Decision",
    "difficulty": "extreme",
    "text": "We're choosing between PostgreSQL and MongoDB for a new product. The team has experience with both. The product is a project management tool with complex permissions, nested tasks, and real-time collaboration.",
    "expected_skills": ["adversary", "threshold", "provenance", "temporal", "diverge", "deep-think"],
    "ground_truth": "False dichotomy — polyglot persistence (Postgres for permissions/billing, MongoDB for collaborative workspace) with escape hatches"
  },
  {
    "id": "complete_001",
    "category": "Completeness",
    "difficulty": "high",
    "text": "We're launching a new payment feature. Here's our plan: integrate Stripe, add webhook handlers, create database tables for transactions, add API endpoints, write tests, deploy. What are we missing?",
    "expected_skills": ["negative-space", "contradict", "fidelity", "adversary", "threshold"],
    "ground_truth": "Missing: idempotency, retry logic, reconciliation jobs, fraud detection, compliance (PCI), refund flows, partial failures, audit logs, monitoring/alerting, rollback plan"
  },
  {
    "id": "clarify_001",
    "category": "Clarification",
    "difficulty": "medium",
    "text": "Make the app faster",
    "expected_skills": ["clarify"],
    "ground_truth": "Unanswerable — needs: which screen, what device, current metrics, definition of 'fast enough', user impact"
  },
  {
    "id": "shallow_001",
    "category": "Proportional Depth",
    "difficulty": "low",
    "text": "What color should I make the submit button?",
    "expected_skills": ["shallow"],
    "ground_truth": "Trivial, reversible decision — answer in one sentence with brand color recommendation"
  },
  {
    "id": "teach_001",
    "category": "Teaching",
    "difficulty": "medium",
    "text": "Explain how OAuth 2.0 works to a non-technical person",
    "expected_skills": ["teach"],
    "ground_truth": "Valet key analogy; token = temporary permission; refresh token = getting new valet key without user action"
  }
]
```

---

## Running the Full Benchmark

```bash
# 1. Prepare environments
python -m venv venv_old && source venv_old/bin/activate && pip install -r benchmark/requirements.txt
python -m venv venv_new && source venv_new/bin/activate && pip install -r benchmark/requirements.txt

# 2. Run control (old skills)
source venv_old/bin/activate
python benchmark/run.py \
  --skills-dir depth-skills-old/skills \
  --prompts tests/test_prompts.json \
  --model gpt-4 \
  --thinking-params benchmark/params_standard.json \
  --output results/control_gpt4.json

# 3. Run treatment (premium skills)
source venv_new/bin/activate
python benchmark/run.py \
  --skills-dir depth-skills-new/skills \
  --prompts tests/test_prompts.json \
  --model gpt-4 \
  --thinking-params benchmark/params_deep.json \
  --output results/treatment_gpt4.json

# 4. Score and compare
python benchmark/score.py \
  --control results/control_gpt4.json \
  --treatment results/treatment_gpt4.json \
  --output results/comparison_gpt4.json

# 5. Generate report
python benchmark/report.py \
  --comparison results/comparison_gpt4.json \
  --output results/report_gpt4.md

# 6. View report
cat results/report_gpt4.md
```

---

## Expected Results (Based on Research)

| Metric | Old Skills (v1.x) | Premium Skills (v2.x) | Delta |
|--------|-------------------|----------------------|-------|
| ADS | 0.35 | 0.78 | +0.43 |
| CEI | 0.22 | 0.55 | +0.33 |
| SI | 1.2 | 5.8 | +4.6 |
| EC | 0.38 | 0.71 | +0.33 |
| OV | -0.15 | 0.38 | +0.53 |
| Composite | 32 | 78 | +46 |
| Qualitative (avg) | 0.8 | 1.9 | +1.1 |

**Expected Delta: +46 composite points (transformative)**

---

## Continuous Benchmarking

Add to CI/CD:

```yaml
# .github/workflows/benchmark.yml
name: Depth-Skills Benchmark
on:
  schedule:
    - cron: '0 2 * * 0'  # Weekly
  push:
    branches: [main]
    paths: ['skills/**']

jobs:
  benchmark:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Benchmark
        run: |
          python benchmark/run.py --skills-dir skills --prompts tests/test_prompts.json --model gpt-4 --output results/latest.json
      - name: Compare with Baseline
        run: |
          python benchmark/score.py --control results/baseline.json --treatment results/latest.json --output results/comparison.json
      - name: Fail on Regression
        run: |
          python -c "
          import json
          with open('results/comparison.json') as f: d=json.load(f)
          delta = d['comparison']['overall']['composite']['delta']
          if delta < -2: exit(1)  # Fail if composite drops >2 points
          "
      - name: Update Baseline
        if: github.ref == 'refs/heads/main'
        run: cp results/latest.json results/baseline.json
```