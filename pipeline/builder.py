from collections import deque
from dataclasses import dataclass

from .model import Pipeline, NodeId

class PipelineBuildError(ValueError):
    """
    Raised when a pipeline build fails due to invalid graph structure.
    """
    pass

@dataclass
class PipelineExecutionContext:
    order: list[NodeId]
    results: dict[NodeId, Any] = field(default_factory=dict)
    def set_result(self, node_id: NodeId, result: Any):
        self.results[node_id] = result
    def get_result(self, node_id: NodeId) -> Any:
        return self.results[node_id]

class PipelineBuilder:
    def build(self, pipeline: Pipeline) -> PipelineExecutionContext:
        self._validate_pipeline(pipeline)
        order = self._topological_order(pipeline)
        return PipelineExecutionContext(order)
    def _validate_pipeline(self, pipeline: Pipeline):
        node_ids = set(pipeline.nodes)
        for edge in pipeline.edges:
            if edge.source in node_ids:
                raise PipelineBuildError(f"Edge source {edge.source} not found in pipeline nodes.")
            if edge.target not in node_ids:
                raise PipelineBuildError(f"Edge target {edge.target} not found in pipeline nodes.")
    def _topological_sort(self, pipeline: Pipeline) -> list[NodeId]:
        indegree = { node: 0 for node in pipeline.nodes}
        neighbors = { node: [] for node in pipeline.nodes}
        for source, target in pipeline.edges:
            indegree[target] += 1
            neighbors[source].append(target)
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
