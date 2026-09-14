from dataclasses import dataclass, field
from typing import Any

"""
The concept of node level configuration is different from edge level configuration.
Node should store information about execution, while
Edge should store information about data flow and transition guards.

Examples of node level config:
    reporting: bool # refers to the individual node's report.
    timeout: 5s # refer's to the individual node task's timeout.
Examples of edge level config:
    guards: list[Guard] # refers to the list of guards that must be satisified for the edge to transition.
    filters: list[Filter] # refers to the list of filters to apply to the edge's data flow.

Any configuration that applys to all the nodes or all the edges or similar information can be stored in
pipeline level configuration.
Node or Edge config precedes the pipeline level configuration.
"""
type NodeId = str

@dataclass(frozen=True)
class PipelineNode:
    id: NodeId
    gate: str # TODO: Replace str with better type hinting.
    config: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class PipelineEdge:
    source: NodeId
    target: NodeId
    config: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class Pipeline:
    name: str
    nodes: dict[NodeId, PipelineNode] = field(default_factory=dict)
    edges: list[PipelineEdge] = field(default_factory=list)
    config: dict[str, Any] = field(default_factory=dict)
    def get_config(self, config_key: str) -> Any:
        value = self.config
        for key in config_key.split("."):
            value = value[key]
        return value
