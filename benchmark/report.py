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
        f"- **Significant Improvement**: {'YES' if summary['significant_improvement'] else 'NO'}",
        "",
        "## Per-Category Results",
        "",
        "| Category | Count | ADS Delta | CEI Delta | SI Delta | EC Delta | OV Delta | Composite Delta |",
        "|----------|-------|-----------|-----------|----------|----------|----------|---------------|"
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
        "| Dimension | Control | Treatment | Delta |",
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
        f"{'Premium skills show significant improvement' if summary['significant_improvement'] else 'Improvement not statistically significant'}",
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
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    print(f"Report written to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--comparison", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    generate_report(args.comparison, args.output)