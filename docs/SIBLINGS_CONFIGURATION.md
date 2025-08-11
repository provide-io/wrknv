# Sibling Package Configuration

wrkenv supports automatic discovery and installation of sibling packages - related packages that live alongside your main project in the filesystem.

## Configuration

Sibling packages are configured in the `wrkenv.toml` file under the `[workenv.env]` section using the `siblings` array.

### Simple Pattern Matching

The simplest form is to use glob patterns as strings:

```toml
[workenv.env]
siblings = ["pyvider-*", "test-*"]
```

This will:
- Find all directories matching these patterns in the parent directory
- Install them with dependencies (default behavior)

### Advanced Configuration

For more control, use objects in the siblings array:

```toml
[workenv.env]
siblings = [
    # Pattern with options
    { pattern = "pyvider-*", with_deps = true },
    
    # Explicit package
    { name = "tofusoup", with_deps = false },
    
    # Custom variable name
    { name = "my-package", var_name = "my_pkg", with_deps = true }
]
```

### Mixed Configuration

You can mix simple strings and configured objects:

```toml
[workenv.env]
siblings = [
    "auto-*",                                    # Simple pattern (with deps)
    { pattern = "lib-*", with_deps = false },    # Pattern without deps
    { name = "special-tool", with_deps = true }  # Explicit package
]
```

## Configuration Options

### For Pattern-based Siblings

- `pattern` - Glob pattern to match directories (e.g., `"pyvider-*"`)
- `with_deps` - Whether to install dependencies (default: `true`)

### For Explicit Siblings

- `name` - Exact directory name of the sibling package
- `var_name` - Variable name used in the generated script (default: name with `-` replaced by `_`)
- `with_deps` - Whether to install dependencies (default: `true`)

## Default Behavior

- Simple string patterns install **with** dependencies
- The default for `with_deps` is `true` for all configurations
- Siblings are installed in editable mode (`-e` flag)
- Installation happens after the main project dependencies

## Example Use Cases

### Monorepo with Shared Libraries

```toml
[workenv.env]
siblings = [
    { pattern = "lib-*", with_deps = true },
    { pattern = "services-*", with_deps = false }
]
```

### Development with Optional Tools

```toml
[workenv.env]
siblings = [
    # Core dependencies
    { pattern = "core-*", with_deps = true },
    
    # Development tools (without their deps to avoid conflicts)
    { name = "dev-tools", with_deps = false },
    { name = "test-framework", with_deps = false }
]
```

### Custom Installation

```toml
[workenv.env]
siblings = [
    # Most packages use standard pattern
    "myproject-*",
    
    # Special handling for specific packages
    { name = "legacy-tool", var_name = "legacy", with_deps = false }
]
```

## Generated Script Behavior

The generated `env.sh` will:

1. Install main project dependencies first
2. For each sibling:
   - Check if the directory exists
   - Install with `uv pip install -e <path>` (with or without `--no-deps`)
   - Report success/failure
3. Continue even if individual siblings fail to install

## Migration from Legacy Format

If you're using the old format with `sibling_patterns` and `special_siblings`, it will continue to work:

```toml
# Old format (still supported)
[workenv.env]
sibling_patterns = ["pyvider-*"]
special_siblings = [
    { name = "tofusoup", var_name = "tofusoup", with_deps = true }
]
```

But we recommend migrating to the new unified format:

```toml
# New format (recommended)
[workenv.env]
siblings = [
    { pattern = "pyvider-*", with_deps = true },
    { name = "tofusoup", with_deps = true }
]
```

## Troubleshooting

### Siblings Not Found

- Check that sibling directories exist in the parent directory
- Verify the pattern matches: `ls -d ../pattern-*`
- Ensure the generated env.sh has the sibling section

### Dependency Conflicts

- Use `with_deps = false` for packages that might conflict
- Install order matters - main project dependencies are installed first
- Consider using version constraints in your pyproject.toml

### Performance

- Siblings with many dependencies can slow down environment setup
- Consider `with_deps = false` for development-only tools
- Use patterns wisely - `*` will match everything in the parent directory