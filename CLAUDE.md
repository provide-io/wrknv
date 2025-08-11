# CLAUDE.md - AI Assistant Context for wrkenv Development

## Project Overview

**wrkenv** is a development toolkit for managing tool versions and generating optimized environment setup scripts. It's part of the Provide.io ecosystem that includes:

- **pyvider** - Python framework for building Terraform providers
- **tofusoup** - Testing/conformance suite for providers
- **flavor** - Optional packaging system for binary distribution
- **wrkenv** - Development environment management (this project)

## Current State (December 2024)

### Recent Changes

1. **IBM Naming Convention**
   - HashiCorp Terraform is now referred to as "IBM Terraform" (IBM acquired HashiCorp)
   - Tool name changed: `terraform` → `ibmtf`
   - Manager renamed: `TerraformManager` → `IbmTfManager`
   - Config key: `terraform_flavor` → `tf_flavor` with values `"ibm"` or `"opentofu"`

2. **Architecture Refactoring**
   - Base class renamed: `TerraformVersionsBase` → `TfVersionsBase`
   - File renamed: `tf_versions_base.py` → `tf_base.py`
   - "Terraform" is now "Tf" as the generic term for both implementations

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
│   └── env_generator.py     # Generates env.sh scripts
├── package/                 # Package management (for pyvider packages)
└── container/              # Container support (unused, consider removing)
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
2. **Implement env.sh Generation** - Core feature for making wrkenv optional
3. **Add Provider Shim Support** - For development without Flavor packaging
4. **Profile-Based Matrix Testing** - Instead of version combinations

## Development Workflow

1. **Setup Environment**
   ```bash
   source env.sh  # If available
   # OR
   python -m venv venv
   source venv/bin/activate
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
   wrkenv ibmtf install 1.8.5    # Install IBM Terraform
   wrkenv tofu install 1.10.5    # Install OpenTofu
   wrkenv list                   # List installed versions
   wrkenv generate-env           # Generate env.sh (TODO)
   ```

## Important Notes

- **Container module** (src/wrkenv/container/) has 0% coverage - consider removing
- **Download/Install operations** have only 11-14% coverage - critical for reliability
- **Tool managers** have 18-24% coverage - core functionality needs testing
- **Flavor is OPTIONAL** - It's for packaging, not required for development
- **IBM vs HashiCorp** - Use "IBM" when referring to HashiCorp Terraform

## Questions to Consider

1. Should wrkenv support generic tool management or focus on the Provide.io ecosystem?
2. How to handle the transition from HashiCorp to IBM naming for existing users?
3. Should the container module be removed if unused?
4. What's the priority: test coverage or new features?

## Related Documentation

- `TOFUSOUP_INTEGRATION.md` - Details on TofuSoup integration
- `BFILES_INTEGRATION_ANALYSIS.md` - Analysis of potential bfiles integration
- Individual project READMEs in sibling directories

---

Last updated: December 2024
When updating, please preserve this structure and keep information current.