# 🧰🌍 wrkenv - Work Environment Tool

A flexible, cross-platform command-line tool for managing development tool versions and generating isolated, high-performance project environments. It is written in Python 3.11+ and uses `uv` for exceptional speed.

## Overview

`wrkenv` simplifies managing complex development toolchains (like Terraform, OpenTofu, Go, etc.) across different projects and platforms. Its primary output is a self-contained `env.sh` (or `env.ps1`) script that sets up a complete, isolated shell session without requiring `wrkenv` as a runtime dependency.

### Key Features

*   **Cross-Platform Support**: Generates environment scripts for Linux, macOS, and Windows.
*   **Multiple Tool Versions**: Manages versions for Terraform, OpenTofu, Go, `uv`, and more.
*   **High-Performance Environments**: Leverages `uv` to create and manage Python virtual environments with exceptional speed.
*   **Sibling Package Management**: Automatically discovers and installs local, editable packages from adjacent directories—ideal for monorepos.
*   **Containerized Development**: Includes commands to build, run, and manage Docker-based development containers.
*   **Provider Packaging**: Provides an interface for building and managing provider packages via the `flavor` tool.

## Quick Start

### 1. Installation

It is recommended to install `wrkenv` into a shared, central Python environment using `uv`.

```bash
# Example using a tools directory
uv venv ~/.tools/wrkenv
~/.tools/wrkenv/bin/uv pip install wrkenv
