"""
COL ML Training (Phase 3)
==========================

Trains a GradientBoosting classifier on ground truth pairs to predict
whether two COL_Officials are the same person.

Key evaluation metric: CAREER RECOVERY RATE — for each known career in
the test set, does the model correctly predict at least one pair?

Input:  ml_data/feature_matrix.csv (from col_ml_features.py)
Output: ml_data/model.joblib, ml_data/training_report.txt

Usage:
    python col_ml_train.py              # train + evaluate
    python col_ml_train.py --cv-only    # cross-validation only, no model save

Requires:
    pip install scikit-learn pandas joblib
"""

import argparse
import json
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path

import numpy as np

try:
    import pandas as pd
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.metrics import (
        precision_recall_fscore_support,
        roc_auc_score, average_precision_score,
    )
    import joblib
except ImportError:
    print("ERROR: Install: pip install scikit-learn pandas joblib")
    sys.exit(1)

# =============================================================================
# CONFIGURATION
# =============================================================================

ML_DIR = Path(__file__).parent / "ml_data"
FEATURE_MATRIX_FILE = ML_DIR / "feature_matrix.csv"
KNOWN_CAREERS_FILE = ML_DIR / "known_careers.json"
MODEL_FILE = ML_DIR / "model.joblib"
REPORT_FILE = ML_DIR / "training_report.txt"

FEATURE_COLS = [
    "gap_years", "overlap_years", "time_decay",
    "a_editions", "b_editions",
    "same_colony",
    "name_specificity", "name_exact_match",
    "domain_match", "seniority_direction", "seniority_direction_no_acting",
    "honours_match", "honours_ratchet", "honours_upgrade",
    "is_acting_a", "is_acting_b", "acting_pair",
    "regional_proximity",
    "is_federal_pair",
]


# =============================================================================
# DATA LOADING
# =============================================================================

def load_data():
    """Load feature matrix and known careers."""
    df = pd.read_csv(FEATURE_MATRIX_FILE)
    with open(KNOWN_CAREERS_FILE) as f:
        careers = json.load(f)
    return df, careers


def build_career_index(careers):
    """Build mapping from career_id to set of official_ids.

    Only includes careers with 2+ officials (can generate pairs).
    """
    career_officials = {}
    for career in careers:
        cid = career["career_id"]
        off_ids = set()
        for off in career["officials"]:
            oid = off.get("official_id", off) if isinstance(off, dict) else off
            off_ids.add(oid)
        if len(off_ids) >= 2:
            career_officials[cid] = off_ids
    return career_officials


# =============================================================================
# CAREER RECOVERY EVALUATION
# =============================================================================

def evaluate_career_recovery(y_pred_proba, df_test, career_officials, threshold=0.5):
    """For each known career in the test set, check if the model finds it.

    A career is "recovered" if P(same_person) > threshold for at least
    one pair of officials in that career.
    """
    # Build pair → score lookup for test data
    pair_scores = {}
    for idx in range(len(df_test)):
        row = df_test.iloc[idx]
        key = frozenset({row["official_a"], row["official_b"]})
        pair_scores[key] = y_pred_proba[idx]

    recovered = []
    partial = []
    missed = []

    for career_id, officials in career_officials.items():
        career_pairs = list(combinations(officials, 2))
        scores = []
        for a, b in career_pairs:
            key = frozenset({a, b})
            if key in pair_scores:
                scores.append(pair_scores[key])

        if not scores:
            continue  # Not in this test fold

        above = sum(1 for s in scores if s > threshold)
        if above == len(scores):
            recovered.append(career_id)
        elif above > 0:
            partial.append(career_id)
        else:
            missed.append(career_id)

    total = len(recovered) + len(partial) + len(missed)
    return {
        "total": total,
        "recovered": len(recovered),
        "partial": len(partial),
        "missed": len(missed),
        "rate": (len(recovered) + len(partial)) / max(1, total),
        "full_rate": len(recovered) / max(1, total),
        "missed_ids": missed,
    }


# =============================================================================
# PER-SOURCE EVALUATION (anti-overfitting check)
# =============================================================================

def evaluate_per_source(y_test, y_pred, y_proba, df_test):
    """Break down metrics by source (gemini, wikidata, curated)."""
    results = {}
    for source in df_test["source"].unique():
        mask = df_test["source"].values == source
        if mask.sum() == 0:
            continue
        yt = y_test[mask]
        yp = y_pred[mask]
        ypr = y_proba[mask]
        n_pos = sum(yt == 1)
        n_neg = sum(yt == 0)
        if n_pos == 0 or n_neg == 0:
            results[source] = {"n": mask.sum(), "n_pos": n_pos, "n_neg": n_neg}
            continue
        p, r, f1, _ = precision_recall_fscore_support(yt, yp, average="binary",
                                                       zero_division=0)
        results[source] = {
            "n": mask.sum(), "n_pos": n_pos, "n_neg": n_neg,
            "precision": p, "recall": r, "f1": f1,
        }
    return results


# =============================================================================
# TRAINING
# =============================================================================

def train_and_evaluate(df, career_officials, n_splits=5):
    """Stratified k-fold CV with career recovery evaluation."""
    X = df[FEATURE_COLS].values.astype(float)
    y = df["label"].values.astype(int)

    fold_results = []
    fold_recovery = []
    fold_per_source = []
    all_importances = []

    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

    for fold_idx, (train_idx, test_idx) in enumerate(skf.split(X, y)):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        df_test = df.iloc[test_idx].reset_index(drop=True)

        # Class-balanced sample weights
        n_pos = sum(y_train == 1)
        n_neg = sum(y_train == 0)
        w_pos = len(y_train) / (2 * max(1, n_pos))
        w_neg = len(y_train) / (2 * max(1, n_neg))
        weights = np.where(y_train == 1, w_pos, w_neg)

        model = GradientBoostingClassifier(
            n_estimators=200,
            max_depth=4,
            learning_rate=0.1,
            min_samples_leaf=5,
            subsample=0.8,
            random_state=42 + fold_idx,
        )
        model.fit(X_train, y_train, sample_weight=weights)

        y_proba = model.predict_proba(X_test)[:, 1]
        y_pred = (y_proba > 0.5).astype(int)

        # Standard metrics
        p, r, f1, _ = precision_recall_fscore_support(y_test, y_pred,
                                                       average="binary", zero_division=0)
        try:
            auc = roc_auc_score(y_test, y_proba)
            ap = average_precision_score(y_test, y_proba)
        except ValueError:
            auc = ap = 0.0

        fold_results.append({
            "fold": fold_idx + 1,
            "precision": p, "recall": r, "f1": f1,
            "auc": auc, "ap": ap,
            "n_test": len(y_test),
        })

        # Career recovery
        recovery = evaluate_career_recovery(y_proba, df_test, career_officials)
        fold_recovery.append(recovery)

        # Per-source
        per_source = evaluate_per_source(y_test, y_pred, y_proba, df_test)
        fold_per_source.append(per_source)

        all_importances.append(model.feature_importances_)

        print(f"  Fold {fold_idx+1}: P={p:.3f} R={r:.3f} F1={f1:.3f} "
              f"AUC={auc:.3f} | "
              f"Recovery={recovery['rate']:.0%} "
              f"({recovery['recovered']+recovery['partial']}/{recovery['total']})")

    avg_importances = np.mean(all_importances, axis=0)
    importance_ranking = sorted(zip(FEATURE_COLS, avg_importances),
                                 key=lambda x: -x[1])

    return fold_results, fold_recovery, fold_per_source, importance_ranking


def train_final_model(df):
    """Train final model on all data."""
    X = df[FEATURE_COLS].values.astype(float)
    y = df["label"].values.astype(int)

    n_pos = sum(y == 1)
    n_neg = sum(y == 0)
    w_pos = len(y) / (2 * max(1, n_pos))
    w_neg = len(y) / (2 * max(1, n_neg))
    weights = np.where(y == 1, w_pos, w_neg)

    model = GradientBoostingClassifier(
        n_estimators=200,
        max_depth=4,
        learning_rate=0.1,
        min_samples_leaf=5,
        subsample=0.8,
        random_state=42,
    )
    model.fit(X, y, sample_weight=weights)
    return model


# =============================================================================
# REPORT
# =============================================================================

def write_report(fold_results, fold_recovery, fold_per_source,
                 importance_ranking, path):
    """Write training report."""
    lines = []
    lines.append("ML Training Report")
    lines.append("=" * 70)

    # Per-fold table
    lines.append("\nPER-FOLD RESULTS:")
    lines.append(f"{'Fold':>4}  {'P':>6}  {'R':>6}  {'F1':>6}  {'AUC':>6}  "
                 f"{'Recovery':>8}  {'Detail':>12}")
    lines.append("-" * 60)

    for fr, rec in zip(fold_results, fold_recovery):
        detail = f"{rec['recovered']}+{rec['partial']}/{rec['total']}"
        lines.append(
            f"{fr['fold']:>4}  {fr['precision']:>6.3f}  {fr['recall']:>6.3f}  "
            f"{fr['f1']:>6.3f}  {fr['auc']:>6.3f}  "
            f"{rec['rate']:>7.0%}  {detail:>12}")

    # Averages
    avg = lambda key: np.mean([r[key] for r in fold_results])
    avg_rec = np.mean([r["rate"] for r in fold_recovery])
    lines.append("-" * 60)
    lines.append(
        f" AVG  {avg('precision'):>6.3f}  {avg('recall'):>6.3f}  "
        f"{avg('f1'):>6.3f}  {avg('auc'):>6.3f}  {avg_rec:>7.0%}")

    # Feature importance
    lines.append("\n\nFEATURE IMPORTANCE:")
    lines.append(f"{'#':>2}  {'Feature':>35}  {'Imp':>7}")
    lines.append("-" * 50)
    for rank, (feat, imp) in enumerate(importance_ranking, 1):
        bar = "#" * int(imp * 200)
        lines.append(f"{rank:>2}  {feat:>35}  {imp:>7.4f}  {bar}")

    # Per-source breakdown
    lines.append("\n\nPER-SOURCE RECALL (anti-overfitting check):")
    all_sources = set()
    for ps in fold_per_source:
        all_sources.update(ps.keys())
    for source in sorted(all_sources):
        recalls = []
        for ps in fold_per_source:
            if source in ps and "recall" in ps[source]:
                recalls.append(ps[source]["recall"])
        if recalls:
            lines.append(f"  {source:>30}: recall={np.mean(recalls):.3f} "
                         f"(across {len(recalls)} folds)")

    # Missed careers
    lines.append("\n\nMISSED CAREERS:")
    all_missed = set()
    for rec in fold_recovery:
        all_missed.update(rec["missed_ids"])
    if all_missed:
        for m in sorted(all_missed):
            lines.append(f"  {m}")
    else:
        lines.append("  None!")

    text = "\n".join(lines)
    with open(path, "w") as f:
        f.write(text)
    return text


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Train ML career linker")
    parser.add_argument("--cv-only", action="store_true",
                        help="Cross-validation only")
    parser.add_argument("--folds", type=int, default=5,
                        help="CV folds (default: 5)")
    args = parser.parse_args()

    print("Loading data...")
    df, careers = load_data()
    career_officials = build_career_index(careers)
    n_pos = sum(df["label"] == 1)
    n_neg = sum(df["label"] == 0)
    print(f"  {len(df)} pairs ({n_pos} pos, {n_neg} neg)")
    print(f"  {len(career_officials)} multi-official careers for recovery eval")

    print(f"\n{args.folds}-fold stratified CV:")
    fold_results, fold_recovery, fold_per_source, importance_ranking = \
        train_and_evaluate(df, career_officials, n_splits=args.folds)

    report = write_report(fold_results, fold_recovery, fold_per_source,
                          importance_ranking, REPORT_FILE)
    print(f"\n{report}")

    if not args.cv_only:
        print("\nTraining final model on all data...")
        model = train_final_model(df)
        joblib.dump(model, MODEL_FILE)
        print(f"  Saved to {MODEL_FILE}")

        # Sanity check
        X = df[FEATURE_COLS].values.astype(float)
        y = df["label"].values.astype(int)
        train_acc = (model.predict(X) == y).mean()
        print(f"  Training accuracy: {train_acc:.3f}")

    print("\nDone!")


if __name__ == "__main__":
    main()
