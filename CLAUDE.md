# CLAUDE.md - AI Assistant Context for wrkenv Development

## Project Overview

**wrkenv** (Work Environment) is a development environment management tool that generates optimized shell scripts (`env.sh` and `env.ps1`) for Python projects. It manages tool versions, virtual environments, and sibling package dependencies within the Provide.io ecosystem.

### Ecosystem Context
- **pyvider** - Python framework for building Terraform providers
- **tofusoup** - Testing/conformance suite for providers  
- **flavor** - Optional packaging system for binary distribution
- **wrkenv** - Development environment management (this project)
- **supsrc** - Automated Git commit/push utility (managed by wrkenv)

## Current State (August 2025)

### Recent Changes

1. **Python 3.11+ Support** (August 2025)
   - Updated all Provide.io projects to support Python 3.11+
   - Removed Python 3.12+ syntax from dependencies
   - Fixed pyvider-telemetry local file reference in pyproject.toml

2. **env.sh Generation Working**
   - Successfully generates env.sh with sibling package discovery
   - Hardcoded pyvider sibling patterns in env_generator.py
   - Tested in Docker containers with Python 3.11

3. **IBM Naming Convention** (December 2024)
   - HashiCorp Terraform is now referred to as "IBM Terraform" (IBM acquired HashiCorp)
   - Tool name changed: `terraform` → `ibmtf`
   - Manager renamed: `TerraformManager` → `IbmTfManager`
   - Config key: `terraform_flavor` → `tf_flavor` with values `"ibm"` or `"opentofu"`

### Key Concepts

**wrkenv is OPTIONAL** - Projects can function without it by using pre-generated `env.sh` scripts. wrkenv's value is in:
1. Managing complex tool version matrices during development
2. Testing tool combinations
3. Generating optimized `env.sh` scripts for production use

### Architecture

```
Development Time:
┌─────────────────┐
│     wrkenv      │ ← Manages versions, tests combinations
└────────┬────────┘
         │ generates
         ↓
┌─────────────────┐
│     env.sh      │ ← Optimized shell script (no Python needed)
└─────────────────┘

Runtime:
- Users just run: source env.sh
- No wrkenv dependency required
```

## Code Structure

```
src/wrkenv/
├── env/
│   ├── managers/
│   │   ├── base.py          # BaseToolManager abstract class
│   │   ├── tf_base.py       # TfVersionsBase for Tf tools
│   │   ├── ibm_tf.py        # IBM Terraform manager
│   │   ├── tofu.py          # OpenTofu manager
│   │   ├── go.py            # Go manager
│   │   ├── uv.py            # UV (Python) manager
│   │   └── factory.py       # Tool manager factory
│   ├── config.py            # Configuration handling
│   ├── cli.py               # CLI commands
│   ├── env_generator.py     # Generates env.sh scripts
│   └── visual.py            # Console output formatting
├── package/                 # Package management (unused)
├── container/              # Container support (0% coverage)
└── templates/
    └── env/
        ├── sh/             # Bash templates (modular)
        │   ├── base.sh.j2
        │   ├── sibling_packages.sh.j2
        │   └── ...
        └── pwsh/           # PowerShell templates
```

## Testing

Current test coverage: **34%** (needs improvement)

Key test files:
- `tests/test_tdd_config_integration.py` - Config system tests
- `tests/test_tdd_package_commands.py` - Package command tests
- `tests/workenv/test_tdd_cli_behavior.py` - CLI behavior tests
- `tests/workenv/test_tdd_workenv_contracts.py` - Contract tests

Run tests:
```bash
python -m pytest tests/ -v
python -m pytest tests/ -v --cov=src/wrkenv --cov-report=term-missing
```

## env.sh Generation

The generated `env.sh` script provides a complete development environment without requiring wrkenv at runtime:

### Features
1. **UV Installation** - Installs UV package manager if not present
2. **Virtual Environment** - Creates venv in `workenv/{project}_{os}_{arch}`
3. **Dependency Installation** - Runs `uv sync` to install all dependencies
4. **Sibling Discovery** - Automatically finds and installs sibling packages
5. **Tool Verification** - Checks for required tools (Python, UV, wrkenv, ibmtf, tofu)
6. **PYTHONPATH Configuration** - Sets up proper Python paths

### Sibling Package Configuration
Currently hardcoded in `env_generator.py`:
```python
elif project_name == "pyvider":
    extra_config["include_tool_verification"] = True
    extra_config["sibling_patterns"] = ["pyvider-*"]
    extra_config["special_siblings"] = [
        {"name": "tofusoup", "var_name": "tofusoup", "with_deps": False},
        {"name": "flavor", "var_name": "flavor", "with_deps": False},
        {"name": "wrkenv", "var_name": "wrkenv", "with_deps": False}
    ]
```

## Configuration

wrkenv uses multiple configuration sources (in precedence order):
1. Environment variables
2. `wrkenv.toml` file
3. Default values

Example `wrkenv.toml`:
```toml
[workenv]
tf_flavor = "ibm"  # or "opentofu"

[workenv.tools]
ibmtf = "1.8.5"
tofu = "1.10.5"
go = "1.21.5"

[workenv.settings]
verify_checksums = true
cache_downloads = true

# Future: sibling configuration
[workenv.env]
sibling_patterns = ["pyvider-*"]
special_siblings = ["tofusoup", "flavor"]
```

## TofuSoup Integration

TofuSoup can inject its configuration into wrkenv via `soup.toml`:

```toml
# soup.toml
[workenv]
tf_flavor = "opentofu"

[workenv.tools]
ibmtf = "1.8.5"
tofu = "1.10.5"

[workenv.matrix]
profiles = ["ibm-stable", "tofu-latest"]
parallel_jobs = 4
```

The integration is in `tofusoup/src/tofusoup/workenv_integration.py`.

## Current Tasks

1. **Improve Test Coverage** - Currently at 34%, critical functionality untested
2. **Dynamic Sibling Configuration** - Read sibling patterns from wrkenv.toml instead of hardcoding
3. **Better Error Handling** - UV installation failures in containers need graceful recovery
4. **Add Provider Shim Support** - For development without Flavor packaging
5. **Profile-Based Matrix Testing** - Instead of version combinations

## Development Workflow

1. **Setup Environment**
   ```bash
   source env.sh  # If available (generated by wrkenv)
   # OR manually activate the workenv virtual environment:
   source workenv/wrkenv_darwin_arm64/bin/activate  # Example for macOS ARM64
   # Format: workenv/{project}_{os}_{arch}/bin/activate
   pip install -e .
   ```

2. **Make Changes**
   - Follow existing patterns
   - Add tests for new functionality
   - Update this CLAUDE.md with significant changes

3. **Test**
   ```bash
   python -m pytest tests/ -v
   ```

4. **Common Commands**
   ```bash
   wrkenv generate-env           # Generate env.sh and env.ps1
   wrkenv generate-env --output custom.sh  # Custom output path
   wrkenv ibmtf install 1.8.5    # Install IBM Terraform
   wrkenv tofu install 1.10.5    # Install OpenTofu
   wrkenv list                   # List installed versions
   wrkenv status                 # Check tool versions
   ```

## Ecosystem Tools Summary

### Core Development Stack
1. **pyvider** - Write Terraform providers in Python
2. **tofusoup** - Test providers against real Tf implementations
3. **wrkenv** - Manage development environment and tools
4. **flavor** - Package providers as secure binaries (optional)

### Supporting Tools
- **supsrc** - Git automation (managed by wrkenv)
- **pyvider-cty** - Python implementation of Tf type system
- **pyvider-rpcplugin** - RPC framework for plugin communication
- **pyvider-telemetry** - Structured logging
- **pyvider-hcl** - HCL parsing/generation

### Typical Developer Flow
```
1. wrkenv sets up tools (IBM Tf, OpenTofu, etc.)
2. Developer writes provider with pyvider
3. tofusoup tests the provider
4. flavor packages for distribution (optional)
5. wrkenv generates env.sh for team/production
```

## Important Notes

- **env.sh Generation Works** - Tested with pyvider, installs sibling packages correctly
- **Container Verified** - env.sh works in Python 3.11 Docker containers
- **Sibling Patterns Hardcoded** - Currently in env_generator.py for pyvider project
- **Container module** (src/wrkenv/container/) has 0% coverage - consider removing
- **Download/Install operations** have only 11-14% coverage - critical for reliability
- **Tool managers** have 18-24% coverage - core functionality needs testing
- **Flavor is OPTIONAL** - It's for packaging, not required for development
- **IBM vs HashiCorp** - Use "IBM" when referring to HashiCorp Terraform

## Questions to Consider

1. Should wrkenv support generic tool management or focus on the Provide.io ecosystem?
2. How to make sibling pattern configuration dynamic (read from wrkenv.toml)?
3. Should the container module be removed if unused (0% coverage)?
4. What's the priority: test coverage or new features?
5. How to handle UV installation failures gracefully in restricted environments?

## Troubleshooting

### Common Issues

1. **UV Installation Fails in Container**
   ```bash
   # Manual UV installation
   curl -LsSf https://astral.sh/uv/install.sh | sh
   source ~/.local/bin/env
   ```

2. **Sibling Packages Not Found**
   - Check directory structure: siblings must be in parent directory
   - Verify patterns match: `ls -d ../pyvider-*`
   - Check generated env.sh has sibling installation section

3. **Wrong Virtual Environment Path**
   - Check `PYVIDER_PROFILE` environment variable
   - Default creates `workenv/pyvider_darwin_arm64`
   - Profile creates `workenv/{profile}_darwin_arm64`

4. **Import Errors After env.sh**
   - Ensure all siblings installed: `uv pip list | grep pyvider`
   - Check PYTHONPATH: `echo $PYTHONPATH`
   - Verify editable installs: look for `.egg-link` files

### Testing env.sh

```bash
# Basic test
source env.sh && pyvider --help

# Full test with pytest  
source env.sh && pytest -v

# Container test
docker run --rm -v $(pwd):/app python:3.11-slim bash env.sh
```

## Related Documentation

- `TOFUSOUP_INTEGRATION.md` - Details on TofuSoup integration
- `BFILES_INTEGRATION_ANALYSIS.md` - Analysis of potential bfiles integration
- Individual project READMEs in sibling directories

---

Last updated: August 2025
When updating, please preserve this structure and keep information current.