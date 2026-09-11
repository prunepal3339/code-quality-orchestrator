#!/bin/bash
jq '
def aggregate($type; $stage):
    [range(1; 201)] as $all_tasks
    |
    [
        .it01[$type][$stage].failed_task_ids,
        .it02[$type][$stage].failed_task_ids,
        .it03[$type][$stage].failed_task_ids,
        .it04[$type][$stage].failed_task_ids,
        .it05[$type][$stage].failed_task_ids
    ] as $failed
    |
    {
        passed_at_least_once:
            [
                $all_tasks[]
                | select(
                    [
                        $failed[]
                        | index(.)
                    ]
                    | length < 5
                )
            ],
        failed_every_iteration:
            (
                $failed
                | add
                | group_by(.)
                | map(select(length == 5) | .[0])
            )
    };

{
    unwatermarked: {
        syntax: aggregate("unwatermarked"; "syntax"),
        assertion: aggregate("unwatermarked"; "assertion")
    },
    watermarked: {
        syntax: aggregate("watermarked"; "syntax"),
        assertion: aggregate("watermarked"; "assertion")
    }
}
' reports/summary.json
