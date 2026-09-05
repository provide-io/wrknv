#!/usr/bin/env bash
# Audit what this project depends on, and nothing else.
#
# The scanners used to be installed into the same virtualenv they then audited:
#
#     uv pip install -e ".[dev]"
#     uv pip install safety pip-audit
#     pip-audit --ignore-vuln CVE-2026-3219
#
# So every advisory against a scanner's own dependency was reported as this
# project's. The `--ignore-vuln` above is one of those, and its comment says so
# outright -- "in the scanner environment itself". It stopped being harmless
# when `safety` pulled in `nltk`, which drew an unpatched advisory
# (PYSEC-2026-3740) and turned the build red over a package this project has
# never depended on: nltk appears nowhere in `uv.lock`, dev groups included.
#
# Ignoring each one as it arrives makes the list grow and the audit mean less
# every time. Instead the audit reads the resolved lock, and the scanners run
# from `uvx`, which puts them in their own environment where their dependencies
# are nobody's problem.
set -euo pipefail

# A full template rather than `mktemp -t <prefix>`: GNU mktemp rejects a
# template with no trailing X's, which BSD mktemp accepts -- so the short
# form runs on macOS and fails on the runner.
REQUIREMENTS="$(mktemp "${TMPDIR:-/tmp}/wrknv-audit-requirements.XXXXXX")"
trap 'rm -f "${REQUIREMENTS}"' EXIT

# Everything the lock resolves, dev groups included: a vulnerable test-time
# dependency is still worth knowing about. The project itself is not a package
# to audit, so it is left out.
uv export --no-emit-project --format requirements-txt > "${REQUIREMENTS}"
echo "==> auditing $(grep -c '==' "${REQUIREMENTS}") locked packages"

# The export is fully pinned, so there is nothing to resolve. `--no-deps` says
# so, and `--disable-pip` keeps pip-audit from building a throwaway virtualenv
# to resolve with -- which it does even for a pinned file, and which fails on
# a host whose ensurepip cannot run.
uvx pip-audit --desc --no-deps --disable-pip --requirement "${REQUIREMENTS}"
