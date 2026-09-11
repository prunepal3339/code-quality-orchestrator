#!/bin/bash
function per_iteration_syntax_comparison() {
    mkdir -p reports/comparison

    for i in {01..05}; do
        unwatermarked="reports/syntax/it${i}_syntax_result_unwatermarked.json"
        watermarked="reports/syntax/it${i}_syntax_result_watermarked.json"
        output="reports/comparison/it${i}_syntax_comparison.json"

        echo "===== Iteration $i ====="
        echo "Unwatermarked: $unwatermarked"
        echo "Watermarked:   $watermarked"
        echo "Output:        $output"

        python reporter.py \
            "$unwatermarked" \
            "$watermarked" \
            "$output"

        echo
    done
}

# per_iteration_syntax_comparison

function per_iteration_assertion_comparison() {
    mkdir -p reports/comparison

    for i in {01..05}; do
        unwatermarked="reports/assertion/it${i}_assertion_result_unwatermarked.json"
        watermarked="reports/assertion/it${i}_assertion_result_watermarked.json"
        output="reports/comparison/it${i}_assertion_comparison.json"

        echo "===== Iteration $i ====="

        if [[ ! -f "$unwatermarked" ]]; then
            echo "ERROR: Missing $unwatermarked"
            continue
        fi

        if [[ ! -f "$watermarked" ]]; then
            echo "ERROR: Missing $watermarked"
            continue
        fi

        python reporter_v2.py \
            "$unwatermarked" \
            "$watermarked" \
            "$output"

        if [[ $? -eq 0 ]]; then
            echo "Comparison saved to: $output"
        else
            echo "ERROR: Comparison failed for iteration $i"
        fi
        echo
    done
}

# per_iteration_assertion_comparison

function per_iteration_mcnemar() {
    mkdir -p reports/mcnemar

    for i in {01..05}; do
        echo "===== Iteration $i ====="

        # Syntax
        syntax_input="reports/comparison/it${i}_syntax_comparison.json"
        syntax_output="reports/mcnemar/it${i}_syntax_mcnemar.json"

        if [[ -f "$syntax_input" ]]; then
            python3 mcnemar_test.py \
                "$syntax_input" \
                "$syntax_output"

            if [[ $? -eq 0 ]]; then
                echo "Syntax McNemar saved to: $syntax_output"
            else
                echo "ERROR: Syntax McNemar failed for iteration $i"
            fi
        else
            echo "ERROR: Missing $syntax_input"
        fi

        # Assertion
        assertion_input="reports/comparison/it${i}_assertion_comparison.json"
        assertion_output="reports/mcnemar/it${i}_assertion_mcnemar.json"

        if [[ -f "$assertion_input" ]]; then
            python3 mcnemar_test.py \
                "$assertion_input" \
                "$assertion_output"

            if [[ $? -eq 0 ]]; then
                echo "Assertion McNemar saved to: $assertion_output"
            else
                echo "ERROR: Assertion McNemar failed for iteration $i"
            fi
        else
            echo "ERROR: Missing $assertion_input"
        fi

        echo
    done
}


per_iteration_mcnemar
