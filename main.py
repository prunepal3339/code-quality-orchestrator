import argparse
from pathlib import Path

from gate import GateExecutor, GateRegistry, GateSpecRegistry
from gate.loader import GateSpecificationLoader
from pipeline import PipelineBuilder, PipelineExecutor, PipelineLoader
from pipeline.strategy import (
    PipelineStrategyRegistry,
    StagedExecutionStrategy,
    TaskExecutionStrategy,
)
from reporter import Reporter
from runtime.python import PythonAssertionGate, PythonExecutionGate, PythonSyntaxGate
from runtime.python.python_assertion_executor import SpecAssertionExecutor
from task.loader import TaskSpecificationLoader
from task.resolver import TaskSpecificationResolver


def run_orchestator(reporting_file: str):
    gate_registry = GateRegistry(
        {
            "python": {
                "syntax": PythonSyntaxGate(),
                "execution": PythonExecutionGate(),
                "assertion": PythonAssertionGate(SpecAssertionExecutor()),
            }
        }
    )
    strategy_registry = PipelineStrategyRegistry(
        {"staged": StagedExecutionStrategy(), "task": TaskExecutionStrategy()}
    )

    gate_specs, bindings = GateSpecificationLoader.load(Path("config/specs.json"))
    gate_spec_registry = GateSpecRegistry(bindings, gate_specs)

    specs = TaskSpecificationLoader.load(Path("config/tasks.json"))
    tasks = TaskSpecificationResolver.resolve(specs)

    conduit = PipelineLoader.load(Path("config/pipeline.json"))
    context = PipelineBuilder(conduit).build()
    
    gate_executor = GateExecutor()
    results = PipelineExecutor(context, strategy_registry).execute(tasks, gate_registry, gate_spec_registry, gate_executor)

    r = Reporter({})

    report = r.generate(results)
    with open(reporting_file, "w") as f:
        f.write(report)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run quality gate checks on test specifications."
    )
    parser.add_argument(
        "--output-file",
        "-o",
        type=str,
        default="report.json",
        help="Path to file where report needs to be persisted.",
    )
    args = parser.parse_args()

    run_orchestator(reporting_file=args.output_file)
