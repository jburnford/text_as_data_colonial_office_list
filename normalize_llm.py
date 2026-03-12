"""
LLM-Assisted Clustering for Stage 3 Normalization
===================================================

Uses Google Gemini API to cluster department names and position titles
that rule-based matching could not handle. Runs remotely — zero GPU
impact while Ollama extraction continues locally.

Expects GEMINI_API_KEY environment variable (or pass via --api-key).

Usage:
    # Cluster departments
    python normalize_llm.py departments --input taxonomy/department_unclustered.json

    # Cluster positions (batched automatically)
    python normalize_llm.py positions --input taxonomy/position_unclustered.json

    # Dry run — show prompts without calling API
    python normalize_llm.py departments --input taxonomy/department_unclustered.json --dry-run
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

try:
    from google import genai
except ImportError:
    print("ERROR: google-genai not installed. Run: pip install google-genai")
    sys.exit(1)


# =============================================================================
# CONFIGURATION
# =============================================================================

MODEL = "gemini-3.1-pro-preview"
MAX_ITEMS_PER_BATCH = 400  # positions batched to avoid output degradation
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds

REPO_DIR = Path(__file__).parent
TAXONOMY_DIR = REPO_DIR / "taxonomy"


# =============================================================================
# PROMPT TEMPLATES
# =============================================================================

DEPARTMENT_PROMPT = """You are a historian specializing in British colonial administration. Given the
following list of department/institution names extracted from Colonial Office
Lists (1867-1966), cluster them into groups where each group represents the
same type of institution appearing in different colonies or eras.

RULES:
1. Only group names when you are CONFIDENT they refer to the same institutional
   function. When in doubt, keep them separate.
2. "Medical Department" and "Medical and Sanitary Department" → same type.
3. "Provincial Administration" ≠ "Civil Establishment" — distinct institutional
   contexts.
4. Colony-specific qualifiers (e.g. "Sierra Leone Battalion, WAFF") → group by
   function (Military), not by colony name.
5. Use the most common variant as the canonical name.
6. Assign confidence: HIGH (obvious synonyms), MEDIUM (probable, needs reviewer
   confirmation), LOW (possible, needs scholar decision).
7. For each cluster, suggest a career_track from this list:
   Administrative, Legal, Medical, Financial, Engineering, Survey, Police,
   Ecclesiastical, Education, Military, Postal, Agricultural.
   Use null if the institution doesn't map cleanly to one track.

Previously clustered (HIGH confidence, do not re-cluster):
{pre_clustered_json}

Unclustered names to process (with instance counts):
{unclustered_names}

Return ONLY a JSON array (no markdown fencing, no commentary):
[{{"canonical_name": "...", "members": ["raw1", "raw2"], "confidence": "HIGH|MEDIUM|LOW", "career_track": "..." or null, "reasoning": "..."}}]"""

POSITION_PROMPT = """You are a historian specializing in British colonial administration. Given the
following position titles from Colonial Office Lists (1867-1966), group them
into clusters where each cluster represents the same functional role.

RULES:
1. "Colonial Surgeon" and "Col. Surgeon" → same. "Colonial Surgeon" and
   "Senior Medical Officer" → may NOT be same (different grades).
2. Graded positions: "Clerk", "2nd Clerk", "Chief Clerk" are DIFFERENT types.
3. "Clerks, 1st Class" and "1st Class Clerk" → same.
4. Department-qualified positions: "Clerk" in Treasury and "Clerk" in Post
   Office → same PositionType "Clerk" (department comes from the graph edge).
5. Assign each to one career_track from this list:
   Administrative, Legal, Medical, Financial, Engineering, Survey, Police,
   Ecclesiastical, Education, Military, Postal, Agricultural.
   Use null if the track depends on department context (e.g. "Clerk").
6. Assign confidence: HIGH (obvious synonyms), MEDIUM (probable), LOW (possible).
7. If a position has a clear grade level (e.g. "2nd Class" = grade 2), include
   grade_level as an integer. Otherwise use null.

Previously clustered (HIGH confidence, do not re-cluster):
{pre_clustered_json}

Unclustered position titles to process (with record counts):
{unclustered_names}

Return ONLY a JSON array (no markdown fencing, no commentary):
[{{"canonical_name": "...", "members": ["raw1", "raw2"], "confidence": "HIGH|MEDIUM|LOW", "career_track": "..." or null, "grade_level": int or null, "reasoning": "..."}}]"""


# =============================================================================
# API INTERACTION
# =============================================================================

def call_gemini(client, prompt: str, temperature: float = 0.1) -> str:
    """Call Gemini API with retry logic."""
    for attempt in range(MAX_RETRIES):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
                config={
                    "temperature": temperature,
                    "max_output_tokens": 65536,
                },
            )
            return response.text
        except Exception as e:
            if attempt < MAX_RETRIES - 1:
                print(f"  API error (attempt {attempt + 1}): {e}")
                time.sleep(RETRY_DELAY * (attempt + 1))
            else:
                raise


def parse_json_response(text: str) -> list[dict]:
    """Parse JSON from LLM response, handling markdown fencing."""
    text = text.strip()
    # Strip markdown code fences if present
    if text.startswith("```"):
        lines = text.split("\n")
        # Remove first and last lines (fences)
        lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines)

    return json.loads(text)


# =============================================================================
# CLUSTERING LOGIC
# =============================================================================

def format_pre_clustered(clusters: list[dict]) -> str:
    """Format pre-clustered items as compact JSON for the prompt."""
    summary = []
    for c in clusters:
        summary.append({
            "canonical_name": c["canonical_name"],
            "members": [m["raw"] for m in c["members"]],
        })
    return json.dumps(summary, indent=2)


def format_unclustered(items: list[dict]) -> str:
    """Format unclustered items for the prompt."""
    lines = []
    for item in items:
        raw = item.get("raw", "")
        count = item.get("count", 0)
        lines.append(f"- {raw} (count: {count})")
    return "\n".join(lines)


def cluster_departments_llm(client, unclustered: list[dict],
                            pre_clustered: list[dict],
                            dry_run: bool = False) -> list[dict]:
    """Cluster department names using Gemini."""
    pre_clustered_json = format_pre_clustered(pre_clustered)
    unclustered_names = format_unclustered(unclustered)

    prompt = DEPARTMENT_PROMPT.format(
        pre_clustered_json=pre_clustered_json,
        unclustered_names=unclustered_names,
    )

    print(f"  Department clustering: {len(unclustered)} items in 1 batch")
    print(f"  Prompt length: ~{len(prompt)} chars")

    if dry_run:
        print("\n--- PROMPT ---")
        print(prompt[:2000])
        print(f"... ({len(prompt)} chars total)")
        return []

    response_text = call_gemini(client, prompt)
    clusters = parse_json_response(response_text)

    # Tag method
    for cluster in clusters:
        cluster["method"] = "llm_assisted"

    print(f"  Got {len(clusters)} clusters from LLM")
    return clusters


def cluster_positions_llm(client, unclustered: list[dict],
                          pre_clustered: list[dict],
                          dry_run: bool = False) -> list[dict]:
    """Cluster position titles using Gemini, batched by frequency."""
    pre_clustered_json = format_pre_clustered(pre_clustered)

    # Sort by count descending, then batch
    sorted_items = sorted(unclustered, key=lambda x: x.get("count", 0), reverse=True)
    batches = []
    for i in range(0, len(sorted_items), MAX_ITEMS_PER_BATCH):
        batches.append(sorted_items[i:i + MAX_ITEMS_PER_BATCH])

    print(f"  Position clustering: {len(unclustered)} items in {len(batches)} batches")

    all_clusters = []
    for batch_idx, batch in enumerate(batches):
        unclustered_names = format_unclustered(batch)

        prompt = POSITION_PROMPT.format(
            pre_clustered_json=pre_clustered_json,
            unclustered_names=unclustered_names,
        )

        print(f"  Batch {batch_idx + 1}/{len(batches)}: {len(batch)} items, "
              f"~{len(prompt)} chars")

        if dry_run:
            if batch_idx == 0:
                print("\n--- PROMPT (batch 1) ---")
                print(prompt[:2000])
                print(f"... ({len(prompt)} chars total)")
            continue

        response_text = call_gemini(client, prompt)
        clusters = parse_json_response(response_text)

        for cluster in clusters:
            cluster["method"] = "llm_assisted"

        all_clusters.extend(clusters)
        print(f"    Got {len(clusters)} clusters")

        # Rate limiting between batches
        if batch_idx < len(batches) - 1:
            time.sleep(2)

    print(f"  Total: {len(all_clusters)} position clusters from LLM")
    return all_clusters


# =============================================================================
# FILE I/O
# =============================================================================

def load_unclustered(path: Path) -> tuple[list[dict], list[dict]]:
    """Load unclustered items from JSON file.

    Expected format: {"pre_clustered": [...], "unclustered": [...]}
    """
    with open(path) as f:
        data = json.load(f)
    return data.get("pre_clustered", []), data.get("unclustered", [])


def save_llm_clusters(clusters: list[dict], output_path: Path):
    """Save LLM clustering results."""
    with open(output_path, "w") as f:
        json.dump({
            "model": MODEL,
            "clusters": clusters,
            "count": len(clusters),
        }, f, indent=2)
    print(f"  Saved to {output_path}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="LLM-assisted clustering for Stage 3 normalization"
    )
    parser.add_argument("mode", choices=["departments", "positions"],
                        help="What to cluster")
    parser.add_argument("--input", required=True,
                        help="Path to unclustered JSON file")
    parser.add_argument("--output",
                        help="Output path (default: taxonomy/{mode}_llm_clusters.json)")
    parser.add_argument("--api-key",
                        help="Gemini API key (default: GEMINI_API_KEY env var)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show prompts without calling API")
    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("GEMINI_API_KEY")
    if not api_key and not args.dry_run:
        print("ERROR: No API key. Set GEMINI_API_KEY or use --api-key")
        sys.exit(1)

    print("=" * 60)
    print(f"LLM CLUSTERING: {args.mode.upper()}")
    print(f"Model: {MODEL}")
    print("=" * 60)

    # Load data
    input_path = Path(args.input)
    pre_clustered, unclustered = load_unclustered(input_path)
    print(f"Pre-clustered: {len(pre_clustered)} clusters")
    print(f"Unclustered: {len(unclustered)} items")

    if not unclustered:
        print("Nothing to cluster.")
        return

    # Initialize client
    client = None
    if not args.dry_run:
        client = genai.Client(api_key=api_key)

    # Cluster
    if args.mode == "departments":
        clusters = cluster_departments_llm(client, unclustered, pre_clustered,
                                           dry_run=args.dry_run)
    else:
        clusters = cluster_positions_llm(client, unclustered, pre_clustered,
                                         dry_run=args.dry_run)

    if args.dry_run:
        print("\n[DRY RUN] No API calls made.")
        return

    # Save
    output_path = Path(args.output) if args.output else (
        TAXONOMY_DIR / f"{args.mode}_llm_clusters.json"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    save_llm_clusters(clusters, output_path)

    # Summary
    high = sum(1 for c in clusters if c.get("confidence") == "HIGH")
    medium = sum(1 for c in clusters if c.get("confidence") == "MEDIUM")
    low = sum(1 for c in clusters if c.get("confidence") == "LOW")
    print(f"\nConfidence breakdown: {high} HIGH, {medium} MEDIUM, {low} LOW")


if __name__ == "__main__":
    main()
