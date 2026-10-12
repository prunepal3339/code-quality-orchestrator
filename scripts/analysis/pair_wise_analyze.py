
import argparse
import json
from pathlib import Path
from scipy.stats import chi2


def classify_pairs(results):
    """
    Runs after merger.py merge_results.
    """
    unwatermarked = results["unwatermarked"]
    watermarked = results["watermarked"]

    concordant_both_pass = []
    concordant_both_fail = []
    discordant_u_pass_w_fail = []
    discordant_u_fail_w_pass = []
    missing_unwatermarked = []
    missing_watermarked = []

    all_ids = set(unwatermarked) | set(watermarked)

    for task_id in sorted(all_ids, key=str):
        u = unwatermarked.get(task_id)
        w = watermarked.get(task_id)

        if u is None:
            missing_unwatermarked.append(task_id)
            continue
        if w is None:
            missing_watermarked.append(task_id)
            continue

        u_pass = u.get("passed")
        w_pass = w.get("passed")

        if not isinstance(u_pass, bool) or not isinstance(w_pass, bool):
            continue

        pair = {
            "original_task_id": task_id,
            "unwatermarked": u_pass,
            "watermarked": w_pass,
            "unwatermarked_first_passing_iteration": u.get(
                "first_passing_iteration"
            ),
            "watermarked_first_passing_iteration": w.get(
                "first_passing_iteration"
            ),
        }

        if u_pass and w_pass:
            concordant_both_pass.append(pair)
        elif not u_pass and not w_pass:
            concordant_both_fail.append(pair)
        elif u_pass and not w_pass:
            discordant_u_pass_w_fail.append(pair)
        else:
            discordant_u_fail_w_pass.append(pair)

    b = len(discordant_u_pass_w_fail)
    c = len(discordant_u_fail_w_pass)


    mcnemar_ccv = ((abs(b - c) - 1) ** 2) / (b + c)
    mcnemar_p_value = chi2.sf(mcnemar_ccv, df=1)

    return {
        "concordant": {
            "both_pass": concordant_both_pass,
            "both_fail": concordant_both_fail,
            "count": (
                len(concordant_both_pass) + len(concordant_both_fail)
            ),
        },
        "discordant": {
            "unwatermarked_pass_watermarked_fail": discordant_u_pass_w_fail,
            "unwatermarked_fail_watermarked_pass": discordant_u_fail_w_pass,
            "count": b + c,
        },
        "mcnemar": {
            "b_unwatermarked_pass_watermarked_fail": b,
            "c_unwatermarked_fail_watermarked_pass": c,
            "discordant_pairs": b + c,
            "continuity_corrected_value": mcnemar_ccv,
            "p-value": mcnemar_p_value
        },
        "unmatched": {
            "missing_unwatermarked": missing_unwatermarked,
            "missing_watermarked": missing_watermarked,
        },
        "summary": {
            "matched_pairs": (
                len(concordant_both_pass)
                + len(concordant_both_fail)
                + b + c
            ),
            "unmatched_task_ids": (
                len(missing_unwatermarked) + len(missing_watermarked)
            ),
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description="Classify paired watermarked/unwatermarked outcomes."
    )
    parser.add_argument("input", help="Input summarized JSON file")
    parser.add_argument(
        "-o", "--output",
        default="-",
        help="Output JSON file (default: stdout)",
    )
    args = parser.parse_args()

    results = json.loads(Path(args.input).read_text())
    report = classify_pairs(results)
    output = json.dumps(report, indent=2)

    if args.output == "-":
        print(output)
    else:
        Path(args.output).write_text(output + "\n")


if __name__ == "__main__":
    main()
