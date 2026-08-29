from pathlib import Path
import json

from framework import (
    TestSpecification,
    SyntaxTestSpec,
    UnitTestSpec,
)

class SpecificationLoader:

    def load(
        self,
        path: Path,
    ) -> list[TestSpecification]:

        data = json.loads(
            path.read_text(
                encoding="utf-8"
            )
        )

        defaults = data.get("defaults", {})
        specs = data.get("specs", [])

        if not isinstance(specs, list):
            raise ValueError(
                "'specs' must be an array"
            )

        specifications = []

        for spec in specs:

            if not isinstance(spec, dict):
                raise ValueError(
                    "Every item in 'specs' must be an object"
                )

            spec_tests = spec.get("tests", [])

            if not isinstance(spec_tests, list):
                raise ValueError(
                    "'tests' must be an array"
                )

            for test in spec_tests:

                if not isinstance(test, dict):
                    raise ValueError(
                        "Every item in 'tests' must be an object"
                    )

                # ------------------------------------------------
                # Three-level precedence:
                #
                # defaults < spec < test
                # ------------------------------------------------

                kind = test.get(
                    "kind",
                    spec.get(
                        "kind",
                        defaults.get("kind"),
                    ),
                )

                language = test.get(
                    "language",
                    spec.get(
                        "language",
                        defaults.get("language"),
                    ),
                )

                if kind is None:
                    raise ValueError(
                        "Missing 'kind' in test specification"
                    )

                if language is None:
                    raise ValueError(
                        "Missing 'language' in test specification"
                    )

                # ------------------------------------------------
                # Build concrete specification
                # ------------------------------------------------

                if kind == "syntax":

                    expect = test.get(
                        "expect",
                        spec.get(
                            "expect",
                            defaults.get("expect"),
                        ),
                    )

                    source = test.get("source")

                    if source is None:
                        raise ValueError(
                            "Every syntax test must contain 'source'"
                        )

                    if expect is None:
                        raise ValueError(
                            "Missing 'expect' in syntax test"
                        )

                    specifications.append(
                        SyntaxTestSpec(
                            kind=kind,
                            language=language,
                            source=source,
                            expect=expect,
                        )
                    )

                elif kind == "unit":

                    source = test.get("source")

                    if source is None:
                        raise ValueError(
                            "Every unit test must contain 'source'"
                        )

                    target = test.get("target")

                    if target is None:
                        raise ValueError(
                            "Every unit test must contain 'target'"
                        )

                    assertions = test.get("assertions")

                    if assertions is None:
                        raise ValueError(
                            "Every unit test must contain 'assertions'"
                        )

                    if not isinstance(assertions, list):
                        raise ValueError(
                            "'assertions' must be an array"
                        )

                    specifications.append(
                        UnitTestSpec(
                            kind=kind,
                            language=language,
                            source=source,
                            target=target,
                            assertions=assertions,
                        )
                    )
                else:
                    raise ValueError(
                        f"Unsupported test kind: {kind}"
                    )

        return specifications
