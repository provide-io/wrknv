#!/usr/bin/env python3
"""Memray stress test for task registry hot paths.

Profiles TaskRegistry.from_repo() — TOML parsing, recursive task building,
and TaskNamespace resolution. These are called on every `we run` invocation.
"""

import os

os.environ.setdefault("LOG_LEVEL", "ERROR")

import tempfile
from pathlib import Path

from wrknv.tasks.registry import TaskRegistry
from wrknv.tasks.schema import TaskNamespace

# ---------------------------------------------------------------------------
# Build a realistic wrknv.toml for stress testing
# ---------------------------------------------------------------------------
TOML_CONTENT = """\
project_name = "stress-project"
version = "1.0.0"

[tasks]
build = "make build"
lint = "ruff check ."
format = "ruff format ."
typecheck = "mypy src/"

[tasks.test]
_default = "pytest"
unit = "pytest -m unit"
integration = "pytest -m integration"
fast = "pytest -x"
parallel = "pytest -n auto"
verbose = "pytest -vvv"

[tasks.test.coverage]
run = "pytest --cov=src"
description = "Run tests with coverage"
_default = "pytest --cov=src --cov-report=html"

[tasks.quality]
run = ["lint", "typecheck"]
parallel = true
description = "Run all quality checks"

[tasks.ci]
run = ["quality", "test"]
description = "Full CI pipeline"

[tasks.setup]
_default = "uv sync"
dev = "uv sync --dev"

[tasks.docs]
_default = "mkdocs serve"
build = "mkdocs build"
clean = "rm -rf site"

[tasks.docs.links]
_default = "lychee docs/"
check = "lychee --offline docs/"

[tasks.clean]
run = "rm -rf build/ dist/ *.egg-info"

[tasks.security]
_default = "bandit -r src/"
scan = "trufflehog git file://."
"""

WARMUP_CYCLES = 10
STRESS_CYCLES = 1000


def main() -> None:
    # Create a temp directory with wrknv.toml
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir)
        config_file = repo_path / "wrknv.toml"
        config_file.write_text(TOML_CONTENT)

        # Warmup — let caches settle
        for _ in range(WARMUP_CYCLES):
            registry = TaskRegistry.from_repo(repo_path)
            registry.resolve_task("test.unit")

        # Stress: registry loading (TOML parse + recursive task build)
        for _ in range(STRESS_CYCLES):
            registry = TaskRegistry.from_repo(repo_path)

        # Stress: task resolution with namespace fallback
        registry = TaskRegistry.from_repo(repo_path)
        for _ in range(STRESS_CYCLES):
            registry.resolve_task("test")
            registry.resolve_task("test.unit")
            registry.resolve_task("test.coverage")
            registry.resolve_task("docs.links.check")

        # Stress: TaskNamespace parsing
        names = [
            "test", "test.unit", "test.coverage._default",
            "docs.links.check", "quality", "ci",
        ]
        for _ in range(STRESS_CYCLES):
            for name in names:
                ns = TaskNamespace.parse(name)
                _ = ns.full_name
                _ = ns.depth
                _ = ns.parent()

    print(f"Task registry stress complete: {STRESS_CYCLES} cycles")


if __name__ == "__main__":
    main()
