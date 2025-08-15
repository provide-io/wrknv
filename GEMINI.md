# GEMINI.md: Your AI Assistant for the `wrkenv` Project

This document provides context and instructions for interacting with the `wrkenv` project. It is intended to be used by the Gemini AI assistant to help you with your development tasks.

## Project Overview

`wrkenv` is a command-line tool for managing development tool versions across different platforms. It is written in Python and uses the `click` library for its command-line interface. The project is configured using `pyproject.toml` and `wrkenv.toml` files.

The main features of `wrkenv` include:

*   **Cross-platform Support**: Works on Linux, macOS, and Windows.
*   **Multiple Tools**: Manage Terraform, OpenTofu, Go, UV, and more.
*   **Flexible Configuration**: Support for multiple configuration sources.
*   **Environment Profiles**: Switch between different tool version sets.
*   **Easy Integration**: Clean API for integration with other tools.

## Building and Running

The project is built and managed using `setuptools` and `pip`. The following commands are used for building, testing, and running the project:

*   **Installation**: `pip install -e .[dev]`
*   **Testing**: `pytest`
*   **Running**: `wrkenv`

The `wrkenv` command-line interface provides several commands for managing tools and environments. The main commands are:

*   `wrkenv setup`: Set up the `wrkenv` environment and integrations.
*   `wrkenv tf`: Install or manage Terraform/OpenTofu versions.
*   `wrkenv status`: Show the status of all managed tools.
*   `wrkenv sync`: Install all tools defined in the configuration.
*   `wrkenv generate-env`: Generate an optimized environment setup script.
*   `wrkenv container`: Manage development containers.
*   `wrkenv profile`: Manage `wrkenv` profiles.
*   `wrkenv config`: Manage `wrkenv` configuration.
*   `wrkenv package`: Manage provider packages.

## Development Conventions

The project follows standard Python development conventions. The code is formatted with `black` and linted with `ruff`. The project uses `pytest` for testing and `mypy` for type checking.

The project's dependencies are managed in the `pyproject.toml` file. The `wrkenv.toml` file is used for configuring the tools and their versions.
