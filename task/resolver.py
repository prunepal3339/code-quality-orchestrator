from pathlib import Path

from .model import (
    FileSourceOrigin,
    SourceTask,
    StringSourceOrigin,
    Task,
)

from .spec import TaskSpecification, SourceTaskSpecification

class TaskSpecificationResolver:
    @staticmethod
    def resolve(specs: list[TaskSpecification]) -> list[Task]:
        tasks = []
        for spec in specs:
            tasks.extend(TaskSpecificationResolver._resolve_spec(spec))
        return tasks

    @staticmethod
    def _resolve_spec(spec: TaskSpecification) -> list[Task]:
        if isinstance(spec, SourceTaskSpecification):
            return TaskSpecificationResolver._resolve_source_spec(spec)
        raise TypeError(f"Unidentified task specification, {type(spec).__name__}")

    @staticmethod
    def _resolve_source_spec(spec: SourceTaskSpecification) -> list[Task]:
        if spec.source_type == 'string':
            source = spec.value
            return [
                SourceTask(
                    id=spec.id,
                    source=source,
                    origin=StringSourceOrigin()
                )
            ]
        if spec.source_type == 'file':
            source = Path(spec.value).read_text(encoding='utf-8')
            return [
                SourceTask(
                    id=spec.id,
                    source=source,
                    origin=FileSourceOrigin(
                        path=Path(spec.value)
                    )
                )
            ]
        if spec.source_type == 'glob':
            files = Path('.').glob(spec.value)
            tasks = []
            for i, file in enumerate(files):
                source = Path(file).read_text(encoding='utf-8')
                tasks.append(
                    SourceTask(
                        id=f"{spec.id}_{i + 1}",
                        source=source,
                        origin=FileSourceOrigin(
                            path=Path(file)
                        )
                    )
                )
            return tasks
        raise ValueError(f'Unimplemented source type: {spec.source_type}')
