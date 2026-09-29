import json
from dataclasses import asdict

from task.model import TaskResult


class Reporter:
    def __init__(self, config: dict):
        self.config = config

    def generate(self, task_results: list[TaskResult]):
        data = [
            asdict(task_result)
            for task_result in task_results
        ]
        return json.dumps(data)
