#!/usr/bin/env python3

import json
import sys
from math import comb, erfc, sqrt


ALPHA = 0.05


def exact_mcnemar(b, c):
    """
    Exact two-sided McNemar test.

    b = Pass -> Fail
    c = Fail -> Pass
    """

    n = b + c

    if n == 0:
        return 1.0

    k = min(b, c)

    # Under H0:
    # b ~ Binomial(n, 0.5)
    probability = sum(
        comb(n, i) * (0.5 ** n)
        for i in range(k + 1)
    )

    # Two-sided exact p-value
    return min(1.0, 2 * probability)

def corrected_mcnemar(b, c):
    """
    McNemar's test with continuity correction.

    chi-square = (|b-c| - 1)^2 / (b+c)
    """

    n = b + c

    if n == 0:
        return 0.0, 1.0

    chi_square = ((abs(b - c) - 1) ** 2) / n

    # Survival function for chi-square distribution
    # with 1 degree of freedom.
    p_value = erfc(sqrt(chi_square / 2))

    return chi_square, p_value


def load_data(path):
    """Load the JSON input file."""

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def main():

    if len(sys.argv) != 3:
        print(
            "Usage:\n"
            "    python mcnemar_test.py comparison.json output.json"
        )
        sys.exit(1)

    input_file = sys.argv[1]

    data = load_data(input_file)

    # ---------------------------------------------------------
    # Read summary
    # ---------------------------------------------------------

    try:
        summary = data["summary"]
    except KeyError:
        print("ERROR: 'summary' was not found in the JSON.")
        sys.exit(1)

    try:
        pass_to_pass = summary["pass_to_pass"]
        pass_to_fail = summary["pass_to_fail"]
        fail_to_pass = summary["fail_to_pass"]
        fail_to_fail = summary["fail_to_fail"]
        matched_tasks = summary["matched_tasks"]
    except KeyError as e:
        print(f"ERROR: Missing field in summary: {e}")
        sys.exit(1)

    # ---------------------------------------------------------
    # McNemar's test uses only discordant pairs
    # ---------------------------------------------------------

    b = pass_to_fail
    c = fail_to_pass

    discordant_pairs = b + c

    # ---------------------------------------------------------
    # Display contingency table
    # ---------------------------------------------------------

    print()
    print("=" * 70)
    print("McNEMAR TEST")
    print("=" * 70)

    print()
    print("2 × 2 CONTINGENCY TABLE")
    print("-" * 70)

    print(
        f"{'':25}"
        f"{'Watermarked PASS':20}"
        f"{'Watermarked FAIL':20}"
    )

    print(
        f"{'Unwatermarked PASS':25}"
        f"{pass_to_pass:<20}"
        f"{pass_to_fail:<20}"
    )

    print(
        f"{'Unwatermarked FAIL':25}"
        f"{fail_to_pass:<20}"
        f"{fail_to_fail:<20}"
    )

    # ---------------------------------------------------------
    # Display transitions
    # ---------------------------------------------------------

    print()
    print("TRANSITIONS")
    print("-" * 70)

    print(f"PASS → PASS : {pass_to_pass}")
    print(f"PASS → FAIL : {pass_to_fail}")
    print(f"FAIL → PASS : {fail_to_pass}")
    print(f"FAIL → FAIL : {fail_to_fail}")

    print()
    print(f"Matched tasks     : {matched_tasks}")
    print(f"Discordant pairs  : {discordant_pairs}")

    # ---------------------------------------------------------
    # Hypotheses
    # ---------------------------------------------------------

    print()
    print("HYPOTHESES")
    print("-" * 70)

    print(
        "H0: Watermarking does not affect the syntax pass/fail outcome."
    )

    print(
        "H1: Watermarking affects the syntax pass/fail outcome."
    )

    print(f"\nSignificance level (α): {ALPHA}")

    # ---------------------------------------------------------
    # Exact McNemar test
    # ---------------------------------------------------------

    exact_p = exact_mcnemar(b, c)

    print()
    print("EXACT McNEMAR TEST")
    print("-" * 70)

    print(f"Pass → Fail (b) : {b}")
    print(f"Fail → Pass (c) : {c}")
    print(f"p-value         : {exact_p:.6f}")

    if exact_p < ALPHA:
        print("Decision        : Reject H0")
        print(
            "Conclusion      : There is a statistically significant "
            "difference."
        )
    else:
        print("Decision        : Fail to reject H0")
        print(
            "Conclusion      : There is no statistically significant "
            "difference."
        )

    # ---------------------------------------------------------
    # Continuity-corrected McNemar test
    # ---------------------------------------------------------

    chi_square, corrected_p = corrected_mcnemar(b, c)

    print()
    print("McNEMAR TEST WITH CONTINUITY CORRECTION")
    print("-" * 70)

    print(f"Chi-square      : {chi_square:.6f}")
    print(f"p-value         : {corrected_p:.6f}")

    if corrected_p < ALPHA:
        print("Decision        : Reject H0")
        print(
            "Conclusion      : There is a statistically significant "
            "difference."
        )
    else:
        print("Decision        : Fail to reject H0")
        print(
            "Conclusion      : There is no statistically significant "
            "difference."
        )

    # ---------------------------------------------------------
    # Interpretation
    # ---------------------------------------------------------

    print()
    print("INTERPRETATION")
    print("-" * 70)

    difference = b - c

    if difference > 0:
        print(
            f"There are {difference} more regressions "
            f"(Pass → Fail) than improvements (Fail → Pass)."
        )
    elif difference < 0:
        print(
            f"There are {abs(difference)} more improvements "
            f"(Fail → Pass) than regressions (Pass → Fail)."
        )
    else:
        print(
            "The number of regressions and improvements is identical."
        )

    # ---------------------------------------------------------
    # Save result
    # ---------------------------------------------------------

    result = {
        "test": "McNemar",
        "alpha": ALPHA,
        "hypotheses": {
            "H0": "Watermarking does not affect the syntax pass/fail outcome.",
            "H1": "Watermarking affects the syntax pass/fail outcome."
        },
        "contingency_table": {
            "pass_to_pass": pass_to_pass,
            "pass_to_fail": pass_to_fail,
            "fail_to_pass": fail_to_pass,
            "fail_to_fail": fail_to_fail
        },
        "matched_tasks": matched_tasks,
        "discordant_pairs": discordant_pairs,
        "discordant_pairs_used_for_test": {
            "pass_to_fail": b,
            "fail_to_pass": c
        },
        "exact_test": {
            "p_value": exact_p,
            "significant": exact_p < ALPHA,
            "decision": (
                "reject H0"
                if exact_p < ALPHA
                else "fail to reject H0"
            )
        },
        "continuity_corrected_test": {
            "chi_square": chi_square,
            "p_value": corrected_p,
            "significant": corrected_p < ALPHA,
            "decision": (
                "reject H0"
                if corrected_p < ALPHA
                else "fail to reject H0"
            )
        }
    }

    output_file = sys.argv[2]

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print()
    print(f"Result saved to: {output_file}")
    print("=" * 70)


if __name__ == "__main__":
    main()
