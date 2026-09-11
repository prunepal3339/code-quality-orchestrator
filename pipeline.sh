#!/bin/bash

function aggregate_syntax_report() {
    for type in unwatermarked watermarked; do

        files=()

        for i in {01..05}; do
            files+=("reports/syntax/it${i}_syntax_result_${type}.json")
        done

        echo "=== ${type} ==="

        jq -s 'add | {
            passed: [.[] | select(.passed == true)] | length,
            failed: [.[] | select(.passed == false)] | length
        }' "${files[@]}"

    done

}

function per_iteration_syntax_report() {
    for i in {01..05}; do
        echo "===== Iteration $i ====="

        for type in unwatermarked watermarked; do
            file="reports/syntax/it${i}_syntax_result_${type}.json"

            result=$(jq '{
                passed: [.[] | select(.passed == true)] | length,
                failed: [.[] | select(.passed == false)] | length,
                failed_task_ids: [.[] | select(.passed == false) | .source | capture("Task(?<task_id>[0-9]+)\\.py").task_id | tonumber]
            }' "$file")

            echo "$type: $result"
        done
    done
}
function per_iteration_test_report() {
    for i in {01..05}; do
        for type in unwatermarked watermarked; do
            file="reports/assertion/it${i}_assertion_result_${type}.json"

            echo "===== Iteration $i - $type ====="

            jq '{
                passed: [.[] | select(.passed == true)] | length,
                failed: [.[] | select(.passed == false)] | length,
                error: (
                    [.[] | select(.passed == false)]
                    | group_by(.error.type)
                    | map({
                        key: .[0].error.type,
                        value: length
                    })
                    | from_entries
                )
            }' "$file"

            echo
        done
    done
}

per_iteration_syntax_report

# per_iteration_test_report
