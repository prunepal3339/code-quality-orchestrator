import argparse
import json

from pathlib import Path
from loader import SpecificationLoader
from resolver import SourceResolver

from gate import GateRegistry, QualityGate

from runtime.python import PythonSyntaxValidator, PythonUnitTestGate

parser = argparse.ArgumentParser(
    description="Run quality gate checks on test specifications."
)
parser.add_argument(
    "spec_path",
    type=str,
    help="Path to the test specifications file."
)
parser.add_argument(
    '--source-dir',
    type=str,
    default= Path(".").resolve(),
    help="Path to the source directory."
)
args = parser.parse_args()

registry = GateRegistry({
    "python": {
        "syntax": PythonSyntaxValidator(),
        "unit": PythonUnitTestGate(),
    }
})

loader = SpecificationLoader()
specs = loader.load(Path(args.spec_path))

results = []
for spec in specs:
    # resolved_source = SourceResolver(root_dir=Path(".").resolve()).resolve(spec.source)
    gate = registry.get(
        kind=spec.kind,
        language=spec.language
    )
    result = gate.run(spec)
    results.append(result)

print(json.dumps([r.to_dict() for r in results], indent=4))
