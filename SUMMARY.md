# 🧰🌍 wrkenv - Work Environment Tool

## Summary

Successfully extracted workenv functionality from tofusoup into a standalone package.

### What We Did

1. **Created wrkenv Repository**
   - Standalone package at `provide-io/wrkenv`
   - Clean separation of concerns
   - Proper 4-emoji footer: 🧰🌍🖥️🪄

2. **Extracted Core Functionality**
   - Tool managers (Terraform, OpenTofu, Go, UV)
   - Configuration system (multi-source with priorities)
   - CLI commands (tf, terraform, status, sync, profile, config, matrix-test)
   - Platform-specific work environments

3. **Fixed Directory Structure**
   - Source code: `/src/wrkenv/env/` (was workenv)
   - Work environments: `/workenv/` (git-ignored)
   - Clean imports: `from wrkenv.env import ...`

4. **Implemented Features**
   - ✅ Flexible configuration (env vars, wrkenv.toml, soup.toml)
   - ✅ Tool version management
   - ✅ Profile support
   - ✅ Dry-run mode
   - ✅ Matrix testing framework
   - ✅ TofuSoup compatibility

5. **Testing**
   - 31 tests passing (CLI behavior, config integration)
   - Core functionality fully tested
   - Backward compatibility maintained

### Next Steps for TofuSoup Integration

1. Add wrkenv as a dependency to tofusoup
2. Update tofusoup CLI to use wrkenv commands
3. Remove old workenv code from tofusoup
4. Test integration

### Usage

```bash
# Install wrkenv
pip install -e .

# Use CLI
wrkenv tf 1.6.2              # Install OpenTofu
wrkenv terraform 1.5.7       # Install Terraform  
wrkenv status                # Show tool status
wrkenv sync                  # Install from config
wrkenv profile save dev      # Save profile
wrkenv config show           # Show configuration
```

### Configuration

Supports multiple config sources (in priority order):
1. Environment variables (`WRKENV_*`)
2. `wrkenv.toml` file
3. `soup.toml` file (for backward compatibility)

Example `wrkenv.toml`:
```toml
[workenv.tools]
terraform = "1.5.7"
tofu = "1.6.2"
go = "1.21.5"
uv = "0.4.15"

[workenv.profiles.dev]
terraform = "1.5.7"
tofu = "1.6.2"

[workenv.settings]
verify_checksums = true
cache_downloads = true
```