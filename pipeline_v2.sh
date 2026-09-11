#!/bin/bash

OUTPUT="reports/summary.json"

generate_report() {
    jq -n '
        reduce range(1; 6) as $i (
            {};
            . + {
                ("it" + ($i | tostring | if length == 1 then "0" + . else . end)): {}
            }
        )
    ' > "$OUTPUT"

    for i in {01..05}; do
        for type in unwatermarked watermarked; do

            syntax_file="reports/syntax/it${i}_syntax_result_${type}.json"
            assertion_file="reports/assertion/it${i}_assertion_result_${type}.json"

            result=$(jq -n \
                --slurpfile syntax "$syntax_file" \
                --slurpfile assertion "$assertion_file" '

                {
                    syntax: (
                        $syntax[0] | {
                            passed: [.[] | select(.passed == true)] | length,
                            failed: [.[] | select(.passed == false)] | length,
                            failed_task_ids: [
                                .[]
                                | select(.passed == false)
                                | .source
                                | capture("Task(?<task_id>[0-9]+)\\.py").task_id
                                | tonumber
                            ]
                        }
                    ),

                    assertion: (
                        $assertion[0] | {
                            passed: [.[] | select(.passed == true)] | length,
                            failed: [.[] | select(.passed == false)] | length,
                            failed_task_ids: [
                                .[]
                                | select(.passed == false)
                                | .task_id
                            ],
                            errors: (
                                [.[] | select(.passed == false)]
                                | group_by(.error.type)
                                | map({
                                    key: .[0].error.type,
                                    value: length
                                })
                                | from_entries
                            )
                        }
                    )
                }
            ')

            tmp=$(mktemp)

            jq \
                --arg iteration "it${i}" \
                --arg type "$type" \
                --argjson result "$result" \
                '.[$iteration][$type] = $result' \
                "$OUTPUT" > "$tmp"

            mv "$tmp" "$OUTPUT"

        done
    done

    jq '.' "$OUTPUT" > "${OUTPUT}.tmp"
    mv "${OUTPUT}.tmp" "$OUTPUT"

    echo "Report generated: $OUTPUT"
}

generate_report
