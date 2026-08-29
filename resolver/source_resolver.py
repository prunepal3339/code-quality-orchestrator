from pathlib import Path
from typing import Any

class SourceResolver:
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir.resolve()

    def resolve(
        self,
        source: dict[str, Any]
    ) -> str:
        source_kind = source.get("kind")

        if source_kind == "string":
            if not source.get("content"):
                raise ValueError("content is required for string source")
            return source.get("content")

        if source_kind == "file":
            if not source.get("path"):
                raise ValueError("path is required for file source")

            relative_path = source.get("path")
            file_path =  (self.root_dir / relative_path).resolve()
            if not file_path.is_file():
                raise ValueError(f"file not found: {file_path}")
            with open(file_path, "r") as f:
                return f.read()
