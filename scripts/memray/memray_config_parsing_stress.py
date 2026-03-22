#!/usr/bin/env python3
"""Memray stress test for config parsing hot paths.

Profiles WorkenvConfig loading, TOML file source parsing, and
environment variable config resolution. These paths run on every
`we` CLI invocation during config discovery.
"""

import os

os.environ.setdefault("LOG_LEVEL", "ERROR")

import tempfile
from pathlib import Path

from wrknv.config.sources import EnvironmentConfigSource, FileConfigSource

# ---------------------------------------------------------------------------
# Build a realistic wrknv.toml for config stress testing
# ---------------------------------------------------------------------------
TOML_CONTENT = """\
project_name = "stress-project"
version = "2.0.0"
description = "A project for stress testing config parsing"

[tools]
terraform = ["1.11.x", "1.13.x"]
tofu = ["1.9.x", "1.10.x"]

[tools.bao]
version = "2.1.0"

[tools.kubectl]
version = "1.30.0"

[tools.helm]
version = "3.15.0"

[profiles.dev]
terraform = ["1.11.x"]
tofu = ["1.9.x"]
bao = "2.1.0"

[profiles.prod]
terraform = ["1.13.x"]
tofu = ["1.10.x"]
bao = "2.1.0"

[profiles.staging]
terraform = ["1.12.x"]

[workenv]
auto_install = true
use_cache = true
cache_ttl = "7d"
log_level = "WARNING"
container_runtime = "docker"
container_registry = "ghcr.io"

[workenv.env]
APP_ENV = "development"
LOG_FORMAT = "json"

[tasks]
build = "make build"
test = "pytest"
lint = "ruff check ."

[gitignore]
extend = [".venv/", "build/", "dist/"]
"""

WARMUP_CYCLES = 10
STRESS_CYCLES = 1000


def main() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / "wrknv.toml"
        config_path.write_text(TOML_CONTENT)

        # Warmup
        for _ in range(WARMUP_CYCLES):
            source = FileConfigSource(config_path, section="workenv")
            source.get_all_tools()

        # Stress: FileConfigSource loading (TOML parse + attribute access)
        for _ in range(STRESS_CYCLES):
            source = FileConfigSource(config_path, section="workenv")

        # Stress: tool version lookups
        source = FileConfigSource(config_path, section="workenv")
        tools = ["terraform", "tofu", "bao", "kubectl", "helm", "nonexistent"]
        for _ in range(STRESS_CYCLES):
            for tool in tools:
                source.get_tool_version(tool)
            source.get_all_tools()

        # Stress: profile lookups
        for _ in range(STRESS_CYCLES):
            source.get_profile("dev")
            source.get_profile("prod")
            source.get_profile("staging")
            source.get_profile("nonexistent")

        # Stress: setting lookups (dot-notation traversal)
        for _ in range(STRESS_CYCLES):
            source.get_setting("project_name")
            source.get_setting("version")
            source.get_setting("workenv.auto_install")
            source.get_setting("workenv.log_level")
            source.get_setting("deep.nested.missing", default="fallback")

        # Stress: EnvironmentConfigSource
        env_source = EnvironmentConfigSource(prefix="WRKNV")
        for _ in range(STRESS_CYCLES):
            env_source.get_tool_version("terraform")
            env_source.get_all_tools()
            env_source.get_setting("LOG_LEVEL", default="WARNING")

    print(f"Config parsing stress complete: {STRESS_CYCLES} cycles")


if __name__ == "__main__":
    main()
