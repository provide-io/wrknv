# 🧰🌍 wrkenv

Work Environment Tool - Manage development tools and versions across platforms.

## Overview

wrkenv provides a flexible, cross-platform solution for managing development tool versions. It supports Terraform, OpenTofu, Go, UV, and more, with a pluggable configuration system that can integrate with various tools.

## Features

- **Cross-platform Support**: Works on Linux, macOS, and Windows
- **Multiple Tools**: Manage Terraform, OpenTofu, Go, UV, and more
- **Flexible Configuration**: Support for multiple configuration sources
- **Environment Profiles**: Switch between different tool version sets
- **Version Matrix Testing**: Test against multiple tool version combinations
- **Easy Integration**: Clean API for integration with other tools

## Installation

```bash
pip install wrkenv
```

## Quick Start

### Standalone Usage

Create a `wrkenv.toml` file:

```toml
[workenv.tools]
terraform = "1.5.7"
tofu = "1.6.2"
go = "1.21.5"

[workenv.profiles.dev]
terraform = "1.6.0"
tofu = "1.7.0"

[workenv.settings]
verify_checksums = true
install_path = "~/.wrkenv/tools"
```

Install tools:

```bash
# Install specific tool version
wrkenv terraform 1.5.7

# Install from configuration
wrkenv install

# List installed versions
wrkenv status
```

### Environment Variables

wrkenv supports environment variable overrides:

```bash
export WRKENV_TERRAFORM_VERSION=1.7.0
export WRKENV_VERIFY_CHECKSUMS=false
```

### Integration with Other Tools

wrkenv provides a flexible API for integration:

```python
from wrkenv import WorkenvConfig, get_tool_manager

# Use default configuration
config = WorkenvConfig()

# Or create custom configuration
from wrkenv.workenv.config import FileConfigSource, EnvironmentConfigSource

sources = [
    EnvironmentConfigSource("MYAPP"),
    FileConfigSource(Path("myapp.toml"), section="tools"),
]
config = WorkenvConfig(sources=sources)

# Install a tool
manager = get_tool_manager("terraform", config)
manager.install_version("1.5.7")
```

## TofuSoup Integration

wrkenv was originally part of the TofuSoup project and maintains backward compatibility:

```python
from wrkenv.workenv.config import create_soup_config

# Create config that prioritizes soup.toml
config = create_soup_config()
```

This allows TofuSoup to use wrkenv while maintaining its existing configuration structure.

## Configuration

wrkenv supports multiple configuration sources with priority ordering:

1. Environment variables (`WRKENV_*`)
2. `wrkenv.toml` file
3. Backward compatibility with `soup.toml`
4. Built-in defaults

## Development

### Setup

```bash
git clone https://github.com/provide-io/wrkenv
cd wrkenv
pip install -e ".[dev]"
```

### Testing

```bash
pytest
```

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Originally developed as part of the TofuSoup project
- Inspired by tools like tfenv, pyenv, and rustup