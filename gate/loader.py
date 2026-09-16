import json
from pathlib import Path
from typing import Any

from .model import GateSpecification, AssertionGateSpecification, AssertionSpecification

class ConfigurationError(Exception):
    ...

class GateSpecificationLoader:

    @staticmethod
    def load(path: Path) -> list[GateSpecification]:
        try:
            with open(path, "r") as f:
                data = json.load(f)

        except FileNotFoundError as e:
            raise ConfigurationError(
                f"Failed to load gate specification configuration "
                f"from {path}: {e}"
            )

        except json.JSONDecodeError as e:
            raise ConfigurationError(
                f"Gate specification configuration is malformed: {e}"
            )

        if not isinstance(data, dict):
            raise ConfigurationError(
                f"Expected valid JSON dictionary, "
                f"got {type(data).__name__}"
            )

        return GateSpecificationLoader.from_dict(data)

    @staticmethod
    def from_dict(
        config: dict[str, Any],
    ) -> list[GateSpecification]:

        specifications = config.get("specifications")

        if not isinstance(specifications, dict):
            raise ConfigurationError(
                "'specifications' must be an object"
            )

        return [
            GateSpecificationLoader._load_spec(
                spec_id,
                spec,
            )
            for spec_id, spec in specifications.items()
        ]

    @staticmethod
    def _load_spec(
        spec_id: str,
        spec: dict[str, Any],
    ) -> GateSpecification:
        if not isinstance(spec, dict):
            raise ConfigurationError(
                f"Specification '{spec_id}' must be an object"
            )
        kind = spec.get("kind")
        if kind == "assertion":
            return GateSpecificationLoader._load_assertion_spec(
                spec_id,
                spec,
            )
        raise ConfigurationError(
            f"Unidentified gate specification: {kind}"
        )

    @staticmethod
    def _load_assertion_spec(
        spec_id: str,
        spec: dict[str, Any],
    ) -> AssertionGateSpecification:
        assertions = spec.get("assertions")
        if not isinstance(assertions, list):
            raise ConfigurationError(
                f"'assertions' must be a list "
                f"in specification '{spec_id}'"
            )
        return AssertionGateSpecification(
            id=spec_id,
            kind="assertion",
            assertions=[
                GateSpecificationLoader._load_assertion(
                    assertion,
                    spec_id,
                )
                for assertion in assertions
            ],
        )

    @staticmethod
    def _load_assertion(
        assertion: dict[str, Any],
        spec_id: str,
    ) -> AssertionSpecification:
        if not isinstance(assertion, dict):
            raise ConfigurationError(
                f"Assertion in specification "
                f"'{spec_id}' must be an object"
            )
        source = assertion.get("source")
        if not isinstance(source, dict):
            raise ConfigurationError(
                f"'source' must be an object "
                f"in specification '{spec_id}'"
            )
        target = assertion.get("target")
        if not isinstance(target, dict):
            raise ConfigurationError(
                f"'target' must be an object "
                f"in specification '{spec_id}'"
            )
        target_kind = target.get("kind")
        target_name = target.get("name")

        if not isinstance(target_kind, str):
            raise ConfigurationError(
                f"Assertion target 'kind' must be a string "
                f"in specification '{spec_id}'"
            )

        if not isinstance(target_name, str):
            raise ConfigurationError(
                f"Assertion target 'name' must be a string "
                f"in specification '{spec_id}'"
            )

        rules = assertion.get("rules")

        if not isinstance(rules, list):
            raise ConfigurationError(
                f"'rules' must be a list "
                f"in specification '{spec_id}'"
            )

        return AssertionSpecification(
            source=source,
            target=AssertionTarget(
                kind=target_kind,
                name=target_name,
            ),
            rules=[
                GateSpecificationLoader._load_rule(
                    rule,
                    spec_id,
                )
                for rule in rules
            ],
        )

    @staticmethod
    def _load_rule(
        rule: dict[str, Any],
        spec_id: str,
    ) -> AssertionRule:

        if not isinstance(rule, dict):
            raise ConfigurationError(
                f"Assertion rule in specification "
                f"'{spec_id}' must be an object"
            )

        if "args" not in rule:
            raise ConfigurationError(
                f"Assertion rule is missing 'args' "
                f"in specification '{spec_id}'"
            )

        if "expected" not in rule:
            raise ConfigurationError(
                f"Assertion rule is missing 'expected' "
                f"in specification '{spec_id}'"
            )

        args = rule["args"]

        if not isinstance(args, list):
            raise ConfigurationError(
                f"'args' must be a list "
                f"in specification '{spec_id}'"
            )

        return AssertionRule(
            args=args,
            expected=rule["expected"],
        )
