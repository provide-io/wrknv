# 🧰🌍 wrknv

**Work Environment** - The foundation for the provide.io ecosystem, generating standardized development environments across all projects.

## Requirements

- **Python 3.11 or later** - wrknv uses modern Python features including native type hints with pipe operators (`str | None`), native TOML support via `tomllib`, and other Python 3.11+ improvements.
- Git (for version control operations)
- curl or wget (for downloading tools)

## Overview

`wrknv` is THE central tool that generates all `env.sh` and `env.ps1` scripts for the provide.io ecosystem. Instead of maintaining hundreds of lines of duplicated shell scripts, each project uses wrknv to generate consistent, maintainable environment setup scripts.

## Features

-   **Environment Script Generation**: Creates standardized `env.sh` and `env.ps1` scripts from templates
-   **Tool Version Management**: Pin versions of Terraform, OpenTofu, Go, and `uv`
-   **Sibling Package Integration**: Automatically discover and install local, editable dependencies
-   **Python Version Safety**: Detects `pyproject.toml` Python requirements and manages virtual environments
-   **Containerized Development**: (Experimental) Manage Docker-based development environments
-   **Provider Packaging**: (Experimental) Interface for building `flavor`-based provider packages

## Quick Start

1.  **Install wrknv**:
    ```bash
    uv pip install wrknv
    ```

2.  **Create a `wrknv.toml` file**:

    ```toml
    # wrknv.toml
    
    [project]
    name = "my-project"
    
    [tools]
    uv = "latest"
    tofu = "1.7.0"
    go = "1.22.1"
    
    [siblings]
    patterns = ["pyvider-*", "tofusoup", "garnish"]
    ```

3.  **Generate Environment Scripts**:
    ```bash
    wrknv generate
    ```
    This creates `env.sh` and `env.ps1` in your project root.

4.  **Activate Your Environment**:
    ```bash
    source env.sh
    ```
    Your shell is now configured with the specified tool versions and all Python dependencies installed in `./workenv/`.

## Core Commands

-   `wrknv init`: Initialize a new wrknv.toml interactively
-   `wrknv generate`: Generate env.sh and env.ps1 scripts
-   `wrknv status`: Show the status and versions of all managed tools
-   `wrknv setup`: Complete setup (init + generate + activate instructions)
-   `wrknv test`: Run project tests
-   `wrknv build`: Build project artifacts

## Ecosystem Commands

-   `wrknv ecosystem setup`: Set up all provide.io projects
-   `wrknv ecosystem status`: Check health of all projects
-   `wrknv ecosystem test`: Run tests for all projects
-   `wrknv ecosystem build`: Build all project artifacts

## Project Configuration

Each project needs a simple `wrknv.toml`:

```toml
[project]
name = "flavorpack"
description = "Cross-language packaging system"

[tools]
uv = "latest"
go = "1.22.1"
rust = "1.75"

[siblings]
patterns = [
    "pyvider-*",      # All pyvider packages
    "tofusoup",       # Testing suite
    "garnish",        # Documentation generator
]

[settings]
python_version = ">=3.11"
verify_checksums = true
```

## Generated Files

wrknv generates:
- `env.sh` - Bash environment setup script
- `env.ps1` - PowerShell environment setup script  
- `Makefile` - Standard development commands (optional)
- `.vscode/` - VS Code settings and launch configs (optional)

## Why wrknv?

Before wrknv, every project had 300-400 lines of hand-written, duplicated `env.sh` scripts. This led to:
- Inconsistent setup experiences
- Maintenance burden
- Copy-paste errors
- Drift between projects

With wrknv:
- Single source of truth for environment setup
- Consistent experience across all projects
- Easy updates - change template once, regenerate everywhere
- Zero duplication

## License

MIT License - See LICENSE file for details.