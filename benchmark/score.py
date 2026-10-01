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