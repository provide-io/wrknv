# 🧰🌍 wrkenv

**Work Environment Tool** - A flexible, cross-platform solution for managing development tool versions and Python environments, specialized for the Pyvider ecosystem.

## Requirements

- **Python 3.11 or later** - wrkenv uses modern Python features including native type hints with pipe operators (`str | None`), native TOML support via `tomllib`, and other Python 3.11+ improvements.
- Git (for version control operations)
- curl or wget (for downloading tools)

## Overview

`wrkenv` manages development tools like Terraform, OpenTofu, Go, and `uv`. Its primary purpose is to generate optimized, standalone shell scripts (`env.sh`, `env.ps1`) that configure a development session without requiring `wrkenv` at runtime.

## Features

-   **Tool Version Management**: Pin versions of Terraform, OpenTofu, Go, and `uv`.
-   **Automated Environment Scripts**: Generate `env.sh` and `env.ps1` for reproducible setups.
-   **Sibling Package Integration**: Automatically discover and install local, editable dependencies.
-   **Python Version Safety**: Detects `pyproject.toml` Python requirements and recreates virtual environments if they are incompatible.
-   **Containerized Development**: (Experimental) Manage a Docker-based development environment.
-   **Provider Packaging**: (Experimental) Interface for building `flavor`-based provider packages.

## Quick Start

1.  **Install `wrkenv`**:
    ```bash
    uv pip install wrkenv
    ```

2.  **Create a `wrkenv.toml` file**:

    ```toml
    # wrkenv.toml

    [workenv.tools]
    tofu = "1.7.0"
    go = "1.22.1"

    [workenv.settings]
    verify_checksums = true

    # See "Sibling Packages" section for details
    [workenv.env]
    siblings = [
        "pyvider-*",
        { name = "tofusoup", with_deps = false }
    ]
    ```

3.  **Generate Environment Scripts**:
    ```bash
    wrkenv generate-env
    ```
    This creates `env.sh` and `env.ps1` in your project root.

4.  **Activate Your Environment**:
    ```bash
    source env.sh
    ```
    Your shell is now configured with the specified tool versions and all Python dependencies (including local siblings) installed in an isolated virtual environment at `./workenv/`.

## Core Commands

-   `wrkenv generate-env`: Generate the `env.sh` and `env.ps1` scripts.
-   `wrkenv status`: Show the status and versions of all managed tools.
-   `wrkenv sync`: Install all tools defined in the configuration.
-   `wrkenv tofu install <version>`: Install a specific OpenTofu version.
-   `wrkenv go install <version>`: Install a specific Go version.

## Sibling Package Configuration

`wrkenv` excels at managing monorepos with local package dependencies. Configure them in `wrkenv.toml`:

```toml
[workenv.env]
siblings = [
    # Simple pattern matching, installs with dependencies by default
    "pyvider-*",
    "internal-lib-*",

    # Advanced configuration using a table
    { name = "tofusoup", with_deps = false }, # Install without its dependencies
    { pattern = "utils-*", with_deps = true }
]
