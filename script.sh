#!/bin/sh

# Extract code from the provided source files.
python3 scripts/extractor.py --source outputs.unwatermarked.content -o sources/it01/unwatermarked sources/result-sanitized-mbpp-it-1.json
python3 scripts/extractor.py --source outputs.watermarked.content -o sources/it01/watermarked sources/result-sanitized-mbpp-it-1.json
python3 scripts/extractor.py --source outputs.unwatermarked.content -o sources/it02/unwatermarked sources/result-sanitized-mbpp-it-2.json
python3 scripts/extractor.py --source outputs.watermarked.content -o sources/it02/watermarked sources/result-sanitized-mbpp-it-2.json
python3 scripts/extractor.py --source outputs.unwatermarked.content -o sources/it03/unwatermarked sources/result-sanitized-mbpp-it-3.json
python3 scripts/extractor.py --source outputs.watermarked.content -o sources/it03/watermarked sources/result-sanitized-mbpp-it-3.json
python3 scripts/extractor.py --source outputs.unwatermarked.content -o sources/it04/unwatermarked sources/result-sanitized-mbpp-it-4.json
python3 scripts/extractor.py --source outputs.watermarked.content -o sources/it04/watermarked sources/result-sanitized-mbpp-it-4.json
python3 scripts/extractor.py --source outputs.unwatermarked.content -o sources/it05/unwatermarked sources/result-sanitized-mbpp-it-5.json
python3 scripts/extractor.py --source outputs.watermarked.content -o sources/it05/watermarked sources/result-sanitized-mbpp-it-5.json

# Install dependencies.
uv sync

# Run the orchestrator to generate report.
python3 main.py -o report_all.json

# Analyze the report.
