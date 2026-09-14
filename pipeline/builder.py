from collections import deque
from dataclasses import dataclass, field
from typing import Any

from .model import NodeId, Pipeline


class PipelineBuildError(ValueError):
    """
    Raised when a pipeline build fails due to invalid graph structure.
    """

@dataclass
class PipelineExecutionContext:
    order: list[NodeId]
    pipeline: Pipeline
    results: dict[NodeId, Any] = field(default_factory=dict)
    def set_result(self, node_id: NodeId, result: Any):
        self.results[node_id] = result
    def get_result(self, node_id: NodeId) -> Any:
        return self.results[node_id]

class PipelineBuilder:
    def __init__(self, pipeline: Pipeline):
        self.pipeline = pipeline
    def build(self) -> PipelineExecutionContext:
        self._validate_pipeline()
        order = self._topological_sort()
        return PipelineExecutionContext(order=order, pipeline=self.pipeline)
    def _validate_pipeline(self):
        pipeline = self.pipeline

        node_ids = set(pipeline.nodes)
        for edge in pipeline.edges:
            if edge.source not in node_ids:
                raise PipelineBuildError(f"Edge source {edge.source} not found in pipeline nodes.")
            if edge.target not in node_ids:
                raise PipelineBuildError(f"Edge target {edge.target} not found in pipeline nodes.")
    def _topological_sort(self) -> list[NodeId]:
        """
        Use Kahn's algorithm to create a topological sort of the given pipeline graph.
        """

        pipeline = self.pipeline

        indegree = { node: 0 for node in pipeline.nodes}
        neighbors = { node: [] for node in pipeline.nodes}
        for edge in pipeline.edges:
            indegree[edge.target] += 1
            neighbors[edge.source].append(edge.target)
        q = deque()
        for node, indeg in indegree.items():
            if indeg == 0:
                q.append(node)
        result = []
        while q:
            node = q.popleft()
            result.append(node)
            for neighbor in neighbors[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        if len(result) != len(pipeline.nodes):
            raise PipelineBuildError("Cycle(s) detected during graph traversal.")
        return result
