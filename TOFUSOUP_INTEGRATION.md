# TofuSoup Integration with wrkenv

This document describes how TofuSoup should integrate with wrkenv now that all TofuSoup-specific code has been removed from wrkenv.

## Overview

wrkenv is now a standalone tool for managing development environment tools. TofuSoup can extend wrkenv's functionality through its flexible configuration system without requiring any modifications to wrkenv itself.

## What TofuSoup Needs to Implement

### 1. Configuration Integration

TofuSoup should use wrkenv's custom configuration sources to maintain backward compatibility:

```python
from wrkenv.env.config import WorkenvConfig, FileConfigSource, EnvironmentConfigSource
from pathlib import Path

def create_soup_config() -> WorkenvConfig:
    """Create a WorkenvConfig that prioritizes soup.toml."""
    sources = [
        # Support legacy TOFUSOUP_WORKENV_ environment variables
        EnvironmentConfigSource("TOFUSOUP_WORKENV"),
        # Also check standard WRKENV_ variables
        EnvironmentConfigSource("WRKENV"),
    ]
    
    # Look for soup.toml first
    soup_toml = Path.cwd() / "soup.toml"
    if soup_toml.exists():
        sources.append(FileConfigSource(soup_toml, "workenv"))
    
    # Also check wrkenv.toml
    wrkenv_toml = Path.cwd() / "wrkenv.toml"
    if wrkenv_toml.exists():
        sources.append(FileConfigSource(wrkenv_toml, "workenv"))
    
    return WorkenvConfig(sources)
```

### 2. Matrix Testing Implementation

TofuSoup should implement the matrix testing functionality for `soup stir`:

```python
# In tofusoup/testing/matrix.py
import asyncio
import itertools
from dataclasses import dataclass
from typing import Dict, List, Any

from wrkenv import WorkenvConfig, get_tool_manager

@dataclass
class MatrixCombination:
    """Represents a specific combination of tool versions."""
    tools: Dict[str, str]

class VersionMatrix:
    """Manages version matrix testing for TofuSoup."""
    
    def __init__(self, base_tools: Dict[str, str], config: WorkenvConfig):
        self.config = config
        self.base_tools = base_tools
        # Get matrix configuration from soup.toml
        self.matrix_config = config.get_setting("matrix", {})
    
    def generate_combinations(self) -> List[MatrixCombination]:
        """Generate all combinations for matrix testing."""
        # Implementation here
        pass
    
    async def run_conformance_tests(self) -> Dict[str, Any]:
        """Run conformance tests across all matrix combinations."""
        # Implementation here
        pass
```

### 3. Package Scaffolding

TofuSoup should implement provider scaffolding:

```python
# In tofusoup/scaffolding/generator.py
from pathlib import Path

def scaffold_new_provider(project_dir: Path) -> Path:
    """Scaffold a new Terraform provider project."""
    project_dir.mkdir(parents=True, exist_ok=True)
    
    # Create TofuSoup-specific project structure
    # Add templates, examples, etc.
    
    return project_dir
```

### 4. CLI Integration

TofuSoup should integrate wrkenv commands into its CLI:

```python
# In tofusoup's CLI
import click
from wrkenv.env.cli import workenv_cli

@soup_cli.group(name="workenv")
def workenv_group():
    """Manage development environment tools."""
    pass

# Add wrkenv commands to soup CLI
for name, cmd in workenv_cli.commands.items():
    workenv_group.add_command(cmd, name=name)
```

### 5. Terraform Wrapper Enhancement

If TofuSoup needs special terraform wrapper behavior, it can provide its own wrapper that reads from soup.toml:

```python
# In tofusoup/bin/terraform-wrapper.py
def get_terraform_flavor():
    """Get terraform flavor from soup.toml."""
    # Check soup.toml for terraform_flavor setting
    # Default to terraform or opentofu as needed
    pass
```

## Benefits of This Approach

1. **Clean Separation**: wrkenv remains a standalone tool with no TofuSoup dependencies
2. **Flexibility**: TofuSoup can extend wrkenv without modifying its code
3. **Backward Compatibility**: TofuSoup can maintain support for soup.toml and legacy environment variables
4. **Maintainability**: Each project can evolve independently
5. **Reusability**: Other projects can use wrkenv without TofuSoup baggage

## Migration Path for TofuSoup Users

1. Install wrkenv as a dependency: `pip install wrkenv`
2. Use TofuSoup's `create_soup_config()` for backward compatibility
3. Existing soup.toml files will continue to work
4. Legacy TOFUSOUP_WORKENV_ environment variables will be supported by TofuSoup's integration layer

## Example Usage in TofuSoup

```python
# In TofuSoup code
from wrkenv import get_tool_manager

# Use TofuSoup's config that includes soup.toml support
config = create_soup_config()

# Install tools
terraform_manager = get_tool_manager("terraform", config)
terraform_manager.install_version("1.5.7")

# Matrix testing for soup stir
matrix = VersionMatrix({"terraform": "1.5.7", "tofu": "1.6.2"}, config)
results = await matrix.run_conformance_tests()
```

This approach allows TofuSoup to leverage all of wrkenv's functionality while maintaining its own unique features and configuration preferences.