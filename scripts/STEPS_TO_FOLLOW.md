Look for code blocks pattern in extractor.py to modify if it doesn't follow the same rule.
Run the following scripts to extract the python codes from the json result obtained via LLM generation.
```sh
python3 scripts/extractor.py --source outputs.unwatermarked.content -o sources/it01/unwatermarked sources/result-sanitized-mbpp-it-1.json
python3 scripts/extractor.py --source outputs.watermarked.content -o sources/it01/watermarked sources/result-sanitized-mbpp-it-1.json
python3 scripts/extractor.py --source outputs.unwatermarked.content -o sources/it02/unwatermarked sources/result-sanitized-mbpp-it-2.json
python3 scripts/extractor.py --source outputs.watermarked.content -o sources/it02/watermarked sources/result-sanitized-mbpp-it-2.json
python3 scripts/extractor.py --source outputs.unwatermarked.content -o sources/it03/unwatermarked sources/result-sanitized-mbpp-it-3.json
python3 scripts/extractor.py --source outputs.watermarked.content -o sources/it03/watermarked sources/result-sanitized-mbpp-it-3.json
python3 scripts/extractor.py --source outputs.unwatermarked.content -o sources/it04/unwatermarked sources/result-sanitized-mbpp-it-4.json
python3 scripts/extractor.py --source outputs.watermarked.content -o sources/it04/watermarked sources/result-sanitized-mbpp-it-4.json
python3 scripts/extractor.py --source outputs.unwatermarked.content -o sources/it05/unwatermarked sources/result-sanitized-mbpp-it-5.json
python3 scripts/extractor.py --source outputs.watermarked.content -o sources/it05/watermarked sources/result-sanitized-mbpp-it-5.json
```
Update config/tasks.json to consider the list of source files.
We can add specification for all tasks (considering all iterations at once) or simply by single task spec at once.
For example (All task specifications at once):
```json
{
  "tasks": {
      "specs": [
        { "id": "it01u", "kind": "source", "source_type": "glob", "value": "sources/it01/unwatermarked/*.py" },
        { "id": "it01w", "kind": "source", "source_type": "glob", "value": "sources/it01/watermarked/*.py" },
        { "id": "it02u", "kind": "source", "source_type": "glob", "value": "sources/it02/unwatermarked/*.py" },
        { "id": "it02w", "kind": "source", "source_type": "glob", "value": "sources/it02/watermarked/*.py" },
        { "id": "it03u", "kind": "source", "source_type": "glob", "value": "sources/it03/unwatermarked/*.py" },
        { "id": "it03w", "kind": "source", "source_type": "glob", "value": "sources/it03/watermarked/*.py" },
        { "id": "it04u", "kind": "source", "source_type": "glob", "value": "sources/it04/unwatermarked/*.py" },
        { "id": "it04w", "kind": "source", "source_type": "glob", "value": "sources/it04/watermarked/*.py" },
        { "id": "it05u", "kind": "source", "source_type": "glob", "value": "sources/it05/unwatermarked/*.py" },
        { "id": "it05w", "kind": "source", "source_type": "glob", "value": "sources/it05/watermarked/*.py" }
      ],
  }
}
```
Given task specification/configuration will be loaded into python `task/spec.py` via task loader `task/loader.py` and gets resolved into individual task models `task/model.py` via the task resolution process `task/resolver.py`.

