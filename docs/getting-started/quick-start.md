# Quick Start Guide

Get your first wrknv environment running in 5 minutes.

## Prerequisites

- Python 3.11 or higher
- pip or uv package manager

## Installation

Install wrknv from PyPI:

```console
$ pip install wrknv
# or using uv
$ uv pip install wrknv
```

Verify installation:

```console
$ wrknv --version
wrknv, version 0.1.0
```

## Your First Environment

### Step 1: Initialize a Project

For this quickstart, let's use an existing Python project or create a simple one:

```console
$ mkdir my-project
$ cd my-project
```

Create a minimal `pyproject.toml`:

```toml
[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.11"

[tool.wrknv.tools]
uv = "0.5.1"
```

### Step 2: Generate Environment Scripts

Generate the environment scripts:

```console
$ wrknv generate
✓ Generated env.sh
✓ Generated env.ps1
✓ Environment scripts created
```

This creates two files:
- `env.sh` - Bash script for Linux/macOS
- `env.ps1` - PowerShell script for Windows

### Step 3: Activate the Environment

#### On Linux/macOS:

```bash
$ source env.sh
🚀 Setting up development environment...
✓ Python 3.11.12 detected
✓ Installing UV 0.5.1...
✓ Creating virtual environment at workenv/
✓ Installing dependencies...
✓ Environment ready!

(my-project) $
```

#### On Windows:

```powershell
PS> .\env.ps1
🚀 Setting up development environment...
✓ Python 3.11.12 detected
✓ Installing UV 0.5.1...
✓ Creating virtual environment at workenv/
✓ Installing dependencies...
✓ Environment ready!

(my-project) PS>
```

### Step 4: Verify the Environment

Check that UV is installed and available:

```console
$ uv --version
uv 0.5.1

$ which uv  # or 'where uv' on Windows
/path/to/my-project/workenv/bin/uv
```

## What Just Happened?

When you ran `source env.sh`, wrknv:

1. **Detected your Python version** from `pyproject.toml`
2. **Downloaded and installed UV** (specified in `[tool.wrknv.tools]`)
3. **Created a virtual environment** in `workenv/` (not `.venv/`)
4. **Installed project dependencies** using UV
5. **Activated the environment** automatically

## Next Steps

### Add More Tools

You can manage multiple tools in your environment. Edit `pyproject.toml`:

```toml
[tool.wrknv.tools]
uv = "0.5.1"
terraform = "1.9.0"
go = "1.22.0"
```

Regenerate and reactivate:

```console
$ wrknv generate
$ source env.sh  # or .\env.ps1 on Windows
```

Now Terraform and Go will be installed automatically!

### Work with Sibling Packages

If you're developing multiple related packages (like in a monorepo), wrknv can discover and install them automatically.

In `pyproject.toml`:

```toml
[tool.wrknv.siblings]
discover_patterns = ["../*/pyproject.toml"]
install_as_editable = true
```

wrknv will find sibling projects and install them in editable mode.

### Check Environment Health

Use the doctor command to verify your environment:

```console
$ wrknv doctor
✓ Python version: 3.11.12 (matches requirement >=3.11)
✓ UV installed: 0.5.1
✓ Terraform installed: 1.9.0
✓ Virtual environment: workenv/ (active)
✓ All dependencies installed
✓ Environment is healthy!
```

### View Configuration

See your current wrknv configuration:

```console
$ wrknv config show
[tool.wrknv.tools]
uv = "0.5.1"
terraform = "1.9.0"
go = "1.22.0"

[tool.wrknv.siblings]
discover_patterns = ["../*/pyproject.toml"]
install_as_editable = true
```

## Common Tasks

### Lock Tool Versions

Create a lockfile to ensure consistent tool versions across your team:

```console
$ wrknv lock
✓ Created wrknv.lock
```

This locks the exact versions of all tools being used.

### Update wrknv Configuration

To add or change tool versions:

1. Edit `pyproject.toml`
2. Run `wrknv generate` to update scripts
3. Run `source env.sh` (or `.\env.ps1`) to apply changes

### Clean Up

Deactivate the environment:

```console
$ deactivate
```

Remove the work environment:

```console
$ rm -rf workenv/
```

## What's in the Generated Scripts?

The `env.sh` and `env.ps1` scripts contain:

- **Platform detection** - Automatically detects OS and architecture
- **Python version validation** - Ensures Python meets requirements
- **Tool installation** - Downloads and installs specified tools
- **Virtual environment setup** - Creates and activates workenv/
- **Dependency installation** - Installs Python dependencies via UV
- **Sibling discovery** - Finds and installs related packages
- **Path management** - Adds tools to PATH
- **Colorful output** - Beautiful terminal feedback

You can inspect the scripts to see exactly what they do.

## Troubleshooting

### "Python version not found"

Ensure Python 3.11+ is installed and in your PATH:

```console
$ python --version
Python 3.11.12
```

### "Permission denied" when running env.sh

Make the script executable:

```console
$ chmod +x env.sh
$ source env.sh
```

### "UV installation failed"

Check your internet connection and try again. UV is downloaded from GitHub releases.

### Environment activation doesn't work

Make sure you're using `source env.sh` (not just `./env.sh`):

```console
# Wrong:
$ ./env.sh

# Right:
$ source env.sh
```

On Windows, use:

```powershell
PS> .\env.ps1
```

## Learn More

- **[Complete Installation Guide](installation.md)** - Detailed installation and configuration
- **[Core Concepts](concepts.md)** - Understanding wrknv architecture
- **[API Reference](../reference/)** - Python API documentation

## Summary

You've now:

✓ Installed wrknv
✓ Generated environment scripts
✓ Activated your first wrknv environment
✓ Learned basic wrknv commands
✓ Understood what wrknv does

Ready to dive deeper? Check out the [Complete Installation Guide](installation.md) or explore [Core Concepts](concepts.md).
