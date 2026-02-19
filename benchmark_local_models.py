"""
Benchmark Local Models Against Gold Standard
=============================================

Runs each Ollama model against the Sierra Leone 1896 test data,
evaluates against gold_standard.json, and produces a comparison table.

IMPORTANT: Stops each model before loading the next to avoid OOM.

Usage:
    python benchmark_local_models.py
    python benchmark_local_models.py --models gpt-oss:120b qwen3-coder-next:q4_K_M
    python benchmark_local_models.py --json-mode   # test JSON extraction mode too

Output:
    benchmark_results.json  (detailed results)
    prints comparison table to stdout
"""

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field, asdict

# Import extraction and evaluation functions
sys.path.insert(0, str(Path(__file__).parent))
from extraction_ollama import extract_codegen, extract_json_mode, run_generated_code
from extraction_regex import (
    Official, load_gold_standard, compare_name
)


# =============================================================================
# CONFIGURATION
# =============================================================================

DEFAULT_MODELS = [
    "gpt-oss:120b",
    "qwen3-coder-next:q4_K_M",
    # "llama4:scout",  # Uncomment if you have enough VRAM headroom
]

SCRIPT_DIR = Path(__file__).parent
TEST_INPUT = SCRIPT_DIR / "test_data" / "sierra_leone_1896_test.txt"
GOLD_FILE = SCRIPT_DIR / "test_data" / "gold_standard.json"
OUTPUT_DIR = SCRIPT_DIR / "generated"


# =============================================================================
# MODEL MANAGEMENT
# =============================================================================

def ollama_stop(model: str):
    """Stop a running Ollama model to free VRAM."""
    print(f"  Stopping model: {model}")
    try:
        subprocess.run(
            ["ollama", "stop", model],
            capture_output=True, text=True, timeout=30
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    # Give the GPU a moment to release memory
    time.sleep(2)


def ollama_list_running() -> list[str]:
    """List currently running Ollama models."""
    try:
        result = subprocess.run(
            ["ollama", "ps"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            return []
        lines = result.stdout.strip().split("\n")[1:]  # skip header
        return [line.split()[0] for line in lines if line.strip()]
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return []


def stop_all_models():
    """Stop all running Ollama models."""
    running = ollama_list_running()
    for model in running:
        ollama_stop(model)


# =============================================================================
# EVALUATION (adapted from extraction_regex.py)
# =============================================================================

def evaluate_against_gold(extracted_officials: list[dict], gold: list[dict]) -> dict:
    """Evaluate extracted officials against gold standard.

    Args:
        extracted_officials: List of dicts with keys matching gold standard format
        gold: Gold standard officials from gold_standard.json

    Returns:
        Evaluation metrics dict
    """
    results = {
        "total_gold": len(gold),
        "total_extracted": len(extracted_officials),
        "matched": 0,
        "precision": 0.0,
        "recall": 0.0,
        "field_accuracy": {
            "name": {"correct": 0, "total": 0},
            "position": {"correct": 0, "total": 0},
            "department": {"correct": 0, "total": 0},
            "salary_min": {"correct": 0, "total": 0},
            "salary_max": {"correct": 0, "total": 0},
            "honors": {"correct": 0, "total": 0},
            "qualifications": {"correct": 0, "total": 0},
            "location": {"correct": 0, "total": 0},
            "military_rank": {"correct": 0, "total": 0},
        },
        "matches": [],
        "missed": [],
        "extra": [],
    }

    used = set()

    for g in gold:
        best_idx = None
        best_score = 0

        g_canonical = g.get("canonical_name", g.get("name", ""))
        if not g_canonical:
            continue

        for i, e in enumerate(extracted_officials):
            if i in used:
                continue

            e_canonical = e.get("canonical_name", e.get("name", ""))
            if not e_canonical:
                continue
            if compare_name(e_canonical, g_canonical):
                score = 1.0
                if score > best_score:
                    best_score = score
                    best_idx = i

        if best_idx is not None:
            used.add(best_idx)
            results["matched"] += 1
            e = extracted_officials[best_idx]

            # Name
            results["field_accuracy"]["name"]["total"] += 1
            if compare_name(
                e.get("canonical_name", e.get("name", "")),
                g.get("canonical_name", g.get("name", ""))
            ):
                results["field_accuracy"]["name"]["correct"] += 1

            # Position
            results["field_accuracy"]["position"]["total"] += 1
            e_pos = (e.get("position") or "").lower()
            g_pos = (g.get("position") or "").lower()
            if e_pos and g_pos and (e_pos in g_pos or g_pos in e_pos):
                results["field_accuracy"]["position"]["correct"] += 1

            # Department
            results["field_accuracy"]["department"]["total"] += 1
            e_dept = (e.get("department") or "").lower().replace(" - sierra leone", "")
            g_dept = (g.get("department") or "").lower()
            if e_dept and g_dept and (e_dept in g_dept or g_dept in e_dept):
                results["field_accuracy"]["department"]["correct"] += 1

            # Salary
            results["field_accuracy"]["salary_min"]["total"] += 1
            if e.get("salary_min") == g.get("salary_min"):
                results["field_accuracy"]["salary_min"]["correct"] += 1

            results["field_accuracy"]["salary_max"]["total"] += 1
            if e.get("salary_max") == g.get("salary_max"):
                results["field_accuracy"]["salary_max"]["correct"] += 1

            # Honors
            if g.get("honors"):
                results["field_accuracy"]["honors"]["total"] += 1
                if set(e.get("honors", [])) == set(g["honors"]):
                    results["field_accuracy"]["honors"]["correct"] += 1

            # Qualifications
            if g.get("qualifications"):
                results["field_accuracy"]["qualifications"]["total"] += 1
                if set(e.get("qualifications", [])) == set(g["qualifications"]):
                    results["field_accuracy"]["qualifications"]["correct"] += 1

            # Location
            if g.get("location"):
                results["field_accuracy"]["location"]["total"] += 1
                if e.get("location") and e["location"].lower() == g["location"].lower():
                    results["field_accuracy"]["location"]["correct"] += 1

            # Military rank
            if g.get("military_rank"):
                results["field_accuracy"]["military_rank"]["total"] += 1
                if e.get("military_rank") and e["military_rank"] == g["military_rank"]:
                    results["field_accuracy"]["military_rank"]["correct"] += 1

            results["matches"].append({
                "gold": g.get("name"),
                "extracted": e.get("name"),
            })
        else:
            results["missed"].append(g.get("name", "?"))

    # Extra (false positives)
    for i, e in enumerate(extracted_officials):
        if i not in used:
            results["extra"].append(e.get("name", "?"))

    # Metrics
    if results["total_extracted"] > 0:
        results["precision"] = results["matched"] / results["total_extracted"]
    if results["total_gold"] > 0:
        results["recall"] = results["matched"] / results["total_gold"]

    # Field accuracy percentages
    for field_name, counts in results["field_accuracy"].items():
        if counts["total"] > 0:
            counts["accuracy"] = counts["correct"] / counts["total"]
        else:
            counts["accuracy"] = None

    return results


# =============================================================================
# BENCHMARK RUNNER
# =============================================================================

def run_benchmark(model: str, source_text: str, gold: list[dict],
                  timeout: int = 600, json_mode: bool = False) -> dict:
    """Run a single model benchmark."""
    result = {
        "model": model,
        "mode": "json" if json_mode else "codegen",
        "timestamp": datetime.now().isoformat(),
        "generation_time": None,
        "code_valid": None,
        "extraction": None,
        "evaluation": None,
        "error": None,
    }

    start = time.time()

    try:
        if json_mode:
            data = extract_json_mode(
                source_text, model, "Sierra Leone", 1896,
                timeout=timeout
            )
            elapsed = time.time() - start
            result["generation_time"] = round(elapsed, 1)

            if data is None:
                result["error"] = "Invalid JSON output"
                return result

            result["code_valid"] = True
            officials = data.get("officials", [])

        else:
            code = extract_codegen(
                source_text, model, "Sierra Leone", 1896,
                str(TEST_INPUT), timeout=timeout
            )
            elapsed = time.time() - start
            result["generation_time"] = round(elapsed, 1)

            # Save generated code
            OUTPUT_DIR.mkdir(exist_ok=True)
            model_slug = model.replace(":", "_").replace("/", "_")
            code_file = OUTPUT_DIR / f"sierra_leone_1896_extraction_{model_slug}.py"
            with open(code_file, "w") as f:
                f.write(code)

            # Try running
            data = run_generated_code(code_file)
            if data is None:
                result["code_valid"] = False
                result["error"] = "Generated code failed to run or produce valid JSON"
                return result

            result["code_valid"] = True
            officials = data.get("officials", [])

        result["extraction"] = {
            "total": len(officials),
            "officials": officials,
        }

        # Evaluate
        evaluation = evaluate_against_gold(officials, gold)
        result["evaluation"] = evaluation

    except Exception as e:
        result["error"] = str(e)
        result["generation_time"] = round(time.time() - start, 1)

    return result


# =============================================================================
# REPORTING
# =============================================================================

def print_comparison_table(all_results: list[dict]):
    """Print a formatted comparison table."""
    print("\n" + "=" * 90)
    print("BENCHMARK COMPARISON TABLE")
    print("=" * 90)

    # Header
    print(f"\n{'Model':<30} {'Mode':<8} {'Recall':>8} {'Precision':>10} "
          f"{'Position':>10} {'Salary':>8} {'Time':>8} {'Valid':>6}")
    print("-" * 90)

    for r in all_results:
        model = r["model"][:28]
        mode = r["mode"]
        ev = r.get("evaluation")

        if r.get("error") and not ev:
            print(f"{model:<30} {mode:<8} {'ERROR':>8} {r['error'][:40]}")
            continue

        recall = f"{ev['recall']:.0%}" if ev else "N/A"
        precision = f"{ev['precision']:.0%}" if ev else "N/A"

        pos_acc = "N/A"
        sal_acc = "N/A"
        if ev:
            pa = ev["field_accuracy"]["position"]["accuracy"]
            pos_acc = f"{pa:.0%}" if pa is not None else "N/A"
            sa = ev["field_accuracy"]["salary_min"]["accuracy"]
            sal_acc = f"{sa:.0%}" if sa is not None else "N/A"

        gen_time = f"{r['generation_time']}s" if r["generation_time"] else "N/A"
        valid = "Yes" if r.get("code_valid") else "No"

        print(f"{model:<30} {mode:<8} {recall:>8} {precision:>10} "
              f"{pos_acc:>10} {sal_acc:>8} {gen_time:>8} {valid:>6}")

    # Gemini reference row
    print("-" * 90)
    print(f"{'Gemini 2.0 Flash (reference)':<30} {'codegen':<8} {'100%':>8} {'100%':>10} "
          f"{'100%':>10} {'100%':>8} {'~10s':>8} {'Yes':>6}")
    print(f"{'Regex (reference)':<30} {'regex':<8} {'100%':>8} {'95%':>10} "
          f"{'43%':>10} {'98%':>8} {'<1s':>8} {'N/A':>6}")

    print("\n" + "=" * 90)

    # Detail per model: missed entries
    for r in all_results:
        ev = r.get("evaluation")
        if ev and ev.get("missed"):
            print(f"\n{r['model']} ({r['mode']}) — Missed ({len(ev['missed'])}):")
            for name in ev["missed"]:
                print(f"  - {name}")
        if ev and ev.get("extra"):
            print(f"\n{r['model']} ({r['mode']}) — Extra ({len(ev['extra'])}):")
            for name in ev["extra"][:10]:
                print(f"  - {name}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Benchmark local Ollama models")
    parser.add_argument("--models", nargs="+", default=DEFAULT_MODELS,
                        help="Models to benchmark")
    parser.add_argument("--json-mode", action="store_true",
                        help="Also test JSON extraction mode")
    parser.add_argument("--timeout", type=int, default=600,
                        help="Timeout per model in seconds (default: 600)")
    parser.add_argument("--output", default="benchmark_results.json",
                        help="Output file for detailed results")
    args = parser.parse_args()

    print("=" * 60)
    print("LOCAL MODEL BENCHMARK")
    print("=" * 60)
    print(f"Models: {', '.join(args.models)}")
    print(f"Test input: {TEST_INPUT}")
    print(f"Gold standard: {GOLD_FILE} (44 officials)")
    print(f"Modes: codegen" + (" + json" if args.json_mode else ""))
    print()

    # Load test data
    with open(TEST_INPUT, "r") as f:
        source_text = f.read()

    gold = load_gold_standard(GOLD_FILE)
    print(f"Gold standard loaded: {len(gold)} officials\n")

    all_results = []

    for i, model in enumerate(args.models):
        print(f"\n{'=' * 60}")
        print(f"MODEL {i+1}/{len(args.models)}: {model}")
        print(f"{'=' * 60}")

        # Stop any running models first
        stop_all_models()

        # Code generation mode
        print(f"\n--- Code Generation Mode ---")
        result = run_benchmark(model, source_text, gold, timeout=args.timeout)
        all_results.append(result)

        if result.get("evaluation"):
            ev = result["evaluation"]
            print(f"  Recall: {ev['recall']:.0%}, Precision: {ev['precision']:.0%}")
            print(f"  Matched: {ev['matched']}/{ev['total_gold']}")
        elif result.get("error"):
            print(f"  ERROR: {result['error']}")

        # JSON mode (optional)
        if args.json_mode:
            print(f"\n--- JSON Mode ---")
            result_json = run_benchmark(
                model, source_text, gold,
                timeout=args.timeout, json_mode=True
            )
            all_results.append(result_json)

            if result_json.get("evaluation"):
                ev = result_json["evaluation"]
                print(f"  Recall: {ev['recall']:.0%}, Precision: {ev['precision']:.0%}")
            elif result_json.get("error"):
                print(f"  ERROR: {result_json['error']}")

    # Stop final model
    stop_all_models()

    # Print comparison
    print_comparison_table(all_results)

    # Save detailed results
    output_path = SCRIPT_DIR / args.output
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nDetailed results saved to: {output_path}")


if __name__ == "__main__":
    main()
