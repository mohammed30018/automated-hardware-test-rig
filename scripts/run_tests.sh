#!/usr/bin/env bash
set -euo pipefail
mkdir -p reports
pytest -m "not hardware" --cov=hardware --cov-report=term-missing --junitxml=reports/junit.xml
