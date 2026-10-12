import json
from dataclasses import asdict
from pathlib import Path

from task.model import TaskResult


class Reporter:
    def __init__(self, config: dict):
        self.config = config

    def generate(self, task_results: list[TaskResult]):
        data = [
            asdict(task_result)
            for task_result in task_results
        ]
        return json.dumps(data, indent=4, default=custom_object_encoder)
    

def custom_object_encoder(obj):
    if isinstance(obj, BaseException):
        msg = str(obj)
        return {
            "kind": type(obj).__name__,
            "message": msg if msg else repr(obj),
        }
    else:
        return str(obj)
