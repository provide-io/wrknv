# Soup-Specific Changes Needed for Wrkenv

## Current Soup-Specific Dependencies

### 1. Import Paths
- All imports use `from tofusoup.workenv.*` which need to change to `from workenv.*`
- Tests import from `tofusoup.workenv.*` as well

### 2. Configuration File
- Currently reads from `soup.toml` with `[workenv]` section
- Options:
  a. Keep soup.toml support for backward compatibility
  b. Also support standalone `wrkenv.toml` 
  c. Support both with precedence: wrkenv.toml > soup.toml

### 3. Environment Variables
- Currently uses `TOFUSOUP_WORKENV_*` prefix
- Should probably change to `WRKENV_*` prefix
- Could support both for compatibility

### 4. Default Paths
- Default installation path: `~/.tofusoup/tools`
- Should change to: `~/.wrkenv/tools`

### 5. Documentation and Comments
- Many references to "TofuSoup workenv" in docstrings
- CLI help text mentions "TofuSoup testing environment"

### 6. Project Metadata
- No pyproject.toml exists - needs to be created
- Package name should be `wrkenv`
- Entry point for CLI needs to be defined

## Recommendation

I recommend making wrkenv support both standalone and soup-integrated modes:

1. **Configuration**: Support both `wrkenv.toml` and `soup.toml`
2. **Environment Variables**: Support both `WRKENV_*` and `TOFUSOUP_WORKENV_*`  
3. **Paths**: Use `~/.wrkenv/tools` by default, but allow `~/.tofusoup/tools` for backward compatibility
4. **Integration**: Keep the ability to be imported by tofusoup if needed

This allows wrkenv to be:
- A standalone tool for general terraform/tofu version management
- Still integrate seamlessly with tofusoup when needed

## Emojis for Wrkenv

Suggested emojis: 🧰🌍

- 🧰 (toolbox) - Represents tool management
- 🌍 (globe) - Represents work environments

Alternative options:
- 🔧🏗️ (wrench + construction)
- 🛠️📦 (hammer/wrench + package)
- 🧰🔄 (toolbox + refresh)