# 🐝📁 bfiles Integration with wrkenv

## What is bfiles?

bfiles (invoked as `bf`) is a file bundling utility that:
- **Bundles multiple source files into a single text file** with clear delimiters and metadata
- **Primary use case**: Providing context to LLMs by concatenating relevant files
- **Key features**: 
  - Respects .gitignore patterns
  - Supports custom include/exclude patterns
  - Detects duplicates by content hash
  - Can chunk large files for LLM token limits
  - Rich terminal output
  - Includes metadata (path, size, MIME type) for each file

## How bfiles Could Use wrkenv's Bundler System

### 1. bfiles as a Bundle Type

bfiles output files (`.bf.txt` or `*bfiles*.txt`) could be treated as bundles themselves:

```python
# wrkenv/bundler/bfiles.py

from wrkenv.bundler import Bundle, BundleMetadata
import re

@attrs.define
class BfileBundle(Bundle):
    """A bundle representing a bfiles output."""
    
    # Pattern to parse bfile headers
    FILE_HEADER_PATTERN = re.compile(r"### FILE (\d+): (.+?) \| (.+?) ###")
    
    entries: List[Dict[str, Any]] = attrs.field(factory=list, init=False)
    
    def _load_metadata(self) -> BundleMetadata:
        """Extract metadata from bfile."""
        # bfiles includes a summary at the end
        with open(self.path) as f:
            content = f.read()
            
        # Extract bundle summary info
        if "Bundle Summary:" in content:
            # Parse the summary section
            name = self.path.stem
            return BundleMetadata(
                name=name,
                version="1.0.0",
                type="bfile",
                description=f"bfiles bundle: {name}",
                tags=["bfile", "bundled-code"]
            )
        
        return BundleMetadata(
            name=self.path.stem,
            version="1.0.0",
            type="bfile"
        )
    
    def validate(self) -> bool:
        """Check if this is a valid bfile."""
        with open(self.path) as f:
            first_line = f.readline()
            return first_line.startswith("### FILE")
    
    def _do_load(self) -> None:
        """Parse bfile entries."""
        with open(self.path) as f:
            content = f.read()
        
        # Parse each file entry
        for match in self.FILE_HEADER_PATTERN.finditer(content):
            file_num = int(match.group(1))
            file_path = match.group(2)
            metadata = match.group(3)
            
            self.entries.append({
                "number": file_num,
                "path": file_path,
                "metadata": metadata,
                # Extract content between headers...
            })
```

### 2. bfiles Configuration via wrkenv

bfiles could use wrkenv's configuration system for its settings:

```python
# In bfiles/config.py, integrate with wrkenv

from wrkenv import WorkenvConfig
from wrkenv.workenv.config import ConfigSource

class BfilesConfigSource(ConfigSource):
    """Configuration source for bfiles settings."""
    
    def __init__(self, config: BfilesConfig):
        self.config = config
    
    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get bfiles-specific settings."""
        settings_map = {
            "bfiles_encoding": self.config.encoding,
            "bfiles_use_gitignore": self.config.use_gitignore,
            "bfiles_follow_symlinks": self.config.follow_symlinks,
            "bfiles_chunk_size": self.config.chunk_size,
            "bfiles_exclude_patterns": self.config.exclude_patterns,
        }
        return settings_map.get(key, default)

# Usage in bfiles
def create_bfiles_config_with_workenv():
    """Create bfiles config that integrates with workenv."""
    # Get workenv config
    workenv_config = WorkenvConfig()
    
    # Create bfiles config with workenv overrides
    encoding = workenv_config.get_setting("bfiles_encoding", DEFAULT_ENCODING)
    use_gitignore = workenv_config.get_setting("bfiles_use_gitignore", True)
    
    return BfilesConfig(
        encoding=encoding,
        use_gitignore=use_gitignore,
        # ... other settings from workenv
    )
```

### 3. bfiles as a Tool Managed by wrkenv

wrkenv could manage bfiles installations:

```python
# wrkenv/workenv/managers/bfiles.py

from wrkenv.workenv.managers.base import BaseToolManager

@attrs.define
class BfilesManager(BaseToolManager):
    """Manage bfiles installations."""
    
    tool_name = "bfiles"
    executable_name = "bf"
    
    def get_available_versions(self) -> List[str]:
        """Get available bfiles versions from PyPI."""
        # Query PyPI API for bfiles versions
        ...
    
    def get_download_url(self, version: str) -> str:
        """Get wheel download URL."""
        return f"https://pypi.org/packages/bfiles/{version}/bfiles-{version}-py3-none-any.whl"
    
    def install_version(self, version: str) -> None:
        """Install bfiles via pip in isolated environment."""
        install_dir = self.get_install_dir(version)
        
        # Create virtual environment
        venv_path = install_dir / "venv"
        subprocess.run([sys.executable, "-m", "venv", str(venv_path)])
        
        # Install bfiles
        pip_path = venv_path / "bin" / "pip"
        subprocess.run([str(pip_path), "install", f"bfiles=={version}"])
        
        # Create wrapper script
        self.create_wrapper_script(version)
```

### 4. Integration Use Cases

#### A. Project Bundle Management

```bash
# Use wrkenv to manage different bfiles versions
wrkenv bfiles 1.2.0

# Create a project bundle
bf --include "*.py" -o myproject.bf.txt

# Register bundle with wrkenv
wrkenv bundle register myproject.bf.txt --type bfile
```

#### B. LLM Context Preparation

```python
# Combine multiple bundle types for LLM context
from wrkenv.bundler import discover_bundles, BundleCompiler

# Find all bundles
agent_bundles = discover_bundles(bundle_type="agents")
doc_bundles = discover_bundles(bundle_type="garnish")
code_bundles = discover_bundles(bundle_type="bfile")

# Custom compiler that combines all bundle types
class LLMContextCompiler(BundleCompiler):
    def compile(self, bundles: List[Bundle]) -> CompilationResult:
        sections = []
        
        # Add agent configurations
        sections.append("# AI Agent Configurations")
        for bundle in agent_bundles:
            sections.append(self._format_agent_bundle(bundle))
        
        # Add documentation
        sections.append("# Documentation")
        for bundle in doc_bundles:
            sections.append(self._format_doc_bundle(bundle))
        
        # Add code context
        sections.append("# Code Context")
        for bundle in code_bundles:
            sections.append(self._format_bfile_bundle(bundle))
        
        return CompilationResult(
            content="\n\n".join(sections),
            metadata={"total_bundles": len(bundles)}
        )
```

#### C. Configuration Integration

```toml
# wrkenv.toml
[workenv.tools]
bfiles = "1.2.0"

[workenv.settings.bfiles]
encoding = "utf-8"
use_gitignore = true
chunk_size = 8000  # For LLM context windows
default_exclude_patterns = [
    "*.pyc",
    "__pycache__/",
    ".git/",
    "*.bf.txt"  # Don't bundle other bundles
]

[bundles.bfile]
search_paths = [".", "~/bundles"]
auto_discover = true
```

## Benefits of Integration

1. **Unified Tool Management**: wrkenv manages bfiles versions alongside other tools
2. **Configuration Consistency**: Single configuration source for all tools
3. **Bundle Ecosystem**: bfiles outputs become first-class bundles that can be discovered and processed
4. **LLM Workflow Integration**: Combine agent configs, docs, and code bundles for complete context
5. **Extensibility**: bfiles can leverage wrkenv's plugin system for custom processors

## Implementation Priority

1. **Phase 1**: Add bfiles as a managed tool in wrkenv
2. **Phase 2**: Create BfileBundle type for discovering/reading bfile outputs
3. **Phase 3**: Configuration integration for bfiles settings
4. **Phase 4**: LLM context compilation combining multiple bundle types

This integration would make bfiles a key component in the developer workflow, especially for LLM-assisted development where providing the right context is crucial.