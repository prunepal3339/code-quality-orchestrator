import json
from pathlib import Path

class MBPPAssertionMapper:
    def __init__(self, source: Path | str):
        if isinstance(source, str):
            source = Path(source)
        self.source = source
    def map(self, args: dict) -> dict | list:
        field = args.get('field')
        source = self.source.read_text(encoding="utf-8")
        source_dict = json.loads(source)
        assertions = []
        for item in source_dict:
            assertions.append(
                {
                    "task_id": item["task_id"],
                    "rules": item[field]
                }
            )
        return assertions
