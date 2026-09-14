import json
from pathlib import Path

from .model import NodeId, Pipeline, PipelineEdge, PipelineNode


class PipelineConfigError(Exception):
    """
    Raised when a pipeline configuration cannot be loaded.
    """

class PipelineLoader:
    @staticmethod
    def load(path: Path) -> Pipeline:
        """
        Loads a pipeline configuration from a file path.
        Args:
            path (Path): The path to the pipeline configuration file.
        Returns:
            Pipeline: The loaded pipeline configuration.
        Raises:
            PipelineConfigError: If the pipeline configuration cannot be loaded.
        """
        try:
            with open(path, 'r') as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise PipelineConfigError(f"Failed to load pipeline configuration from {path}: {e}")
        except json.JSONDecodeError as e:
            raise PipelineConfigError(f"Pipeline configuration is malformed: {e}")
        if not isinstance(data, dict):
            raise PipelineConfigError(f"Expected valid JSON dictionary, got {type(data).__name__}")
        return PipelineLoader.from_dict(data)

    @staticmethod
    def from_dict(data: dict) -> Pipeline:
        pipeline_data = data.get('pipeline', {})

        name = pipeline_data.get('name')
        if not isinstance(name, str) or not name:
            raise PipelineConfigError(
                "Pipeline 'name' must be a non-empty string"
            )
        nodes = PipelineLoader.load_nodes(
            pipeline_data.get('nodes', [])
        )
        edges = PipelineLoader.load_edges(
            pipeline_data.get('edges', [])
        )
        config = pipeline_data.get('config', {})
        if not isinstance(config, dict):
            raise PipelineConfigError(
                "Pipeline 'config' must be an object"
            )

        return Pipeline(
            name=name,
            nodes=nodes,
            edges=edges,
            config=config,
        )

    @staticmethod
    def load_nodes(node_config: list[dict]) -> dict:
        nodes: dict[NodeId, PipelineNode] = {}
        for node in node_config:
            node_name = node.get('id')
            if not isinstance(node_name, str) or not node_name:
                raise PipelineConfigError(
                    "Node 'id' must be a non-empty string"
                )
            nodes[node_name] = PipelineNode(
                **node
            )
        return nodes

    @staticmethod
    def load_edges(edge_config: list[dict]) -> list[PipelineEdge]:
        edges: list[PipelineEdge] = []
        for edge in edge_config:
            edge_from = edge.get('from')
            edge_to = edge.get('to')
            if not isinstance(edge_from, str) or not edge_from:
                raise PipelineConfigError(
                    "Edge 'from' must be a non-empty string"
                )
            if not isinstance(edge_to, str) or not edge_to:
                raise PipelineConfigError(
                    "Edge 'to' must be a non-empty string"
                )
            edges.append(PipelineEdge(
                source=edge_from,
                target=edge_to,
            ))
        return edges
