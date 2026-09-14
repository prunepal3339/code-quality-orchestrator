import json
from pathlib import Path
from typing import Any
from uuid import uuid4

from .model import SourceTaskSpecification, TaskSpecification


class ConfigurationError(Exception):
    ...

class TaskSpecificationLoader:

    @staticmethod
    def load(path: Path) -> list[TaskSpecification]:
        try:
            with open(path, 'r') as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise ConfigurationError(f"Failed to load task configuration from {path}: {e}")
        except json.JSONDecodeError as e:
            raise ConfigurationError(f"Task configuration is malformed: {e}")
        if not isinstance(data, dict):
            raise ConfigurationError(f"Expected valid JSON dictionary, got {type(data).__name__}")

        return TaskSpecificationLoader.from_dict(data)

    @staticmethod
    def from_dict(config: dict[str, Any]) -> list[TaskSpecification]:
        tasks = config.get('tasks')
        if not isinstance(tasks, dict):
            raise ConfigurationError("'tasks' must be an object")

        specs = tasks.get('specs')
        if not isinstance(specs, list):
            raise ConfigurationError("'specs' must be a list")

        return [
            TaskSpecificationLoader._load_spec(spec)
            for spec in specs
        ]
    @staticmethod
    def _load_spec(spec: dict[str, Any]) -> TaskSpecification:
        kind = spec.get("kind")
        if kind == "source":
            id = spec.get("id", uuid4()) # get the id from the task spec configuration if present otherwise, automatically assign a id to the task specification, it will be inherited by the task later on.
            return SourceTaskSpecification(
                id=f"Task#{id}",
                kind="source",
                source_type=spec.get("source_type", ""),
                value=spec.get("value")
            )
        raise ConfigurationError(f"Unidentified task specification: {kind}")
