# WrkNv Documentation

Welcome to WrkNv - Work environment management and toolchain automation for modern development workflows.

## Features

WrkNv provides:

- **Environment Management**: Automated setup and management of development environments
- **Toolchain Automation**: Orchestration of development tools and dependencies
- **Container Integration**: Seamless Docker and container workflow support
- **Package Management**: Unified package management across languages and platforms
- **Configuration Management**: Environment-specific configuration handling
- **Git Integration**: Advanced Git workflow automation and management

## Quick Start

```python
from wrknv import Environment, Container

# Create and manage development environment
env = Environment("myproject")
env.setup()

# Work with containers
container = Container("python:3.11")
container.run("pip install -r requirements.txt")
```

## API Reference

For complete API documentation, see the [API Reference](api/index.md).

## Core Components

- **Environment**: Development environment orchestration
- **Container**: Container and Docker integration
- **Package**: Package management and dependency resolution
- **Config**: Configuration management utilities
- **CLI**: Command-line interface tools