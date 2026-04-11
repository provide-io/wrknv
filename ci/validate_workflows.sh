#!/usr/bin/env bash
# Validate all GitHub Actions workflow YAML files
set -euo pipefail

echo "Validating workflow files..."
for file in .github/workflows/*.yml; do
    echo "Checking $file"
    python -c "import yaml; yaml.safe_load(open('$file'))" || exit 1
done
echo "All workflow files are valid!"
