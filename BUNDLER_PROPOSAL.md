# Bundler System Proposal for wrkenv

## Overview

The bundler system in wrkenv will provide a generic, extensible framework for managing directory-based bundles. This will be used by both .agents (AI agent configurations) and .garnish (documentation bundles) systems.

## Core Architecture

### 1. Base Bundle Protocol/ABC

```python
# wrkenv/bundler/base.py

import attrs
from pathlib import Path
from typing import Protocol, List, Dict, Any, Optional
from abc import ABC, abstractmethod

@attrs.define
class BundleMetadata:
    """Common metadata for all bundles."""
    name: str
    version: str
    type: str  # "agents", "garnish", etc.
    description: Optional[str] = None
    tags: List[str] = attrs.field(factory=list)
    
class BundleProtocol(Protocol):
    """Protocol defining what a bundle must implement."""
    
    @property
    def path(self) -> Path:
        """Path to the bundle directory."""
        ...
    
    @property
    def metadata(self) -> BundleMetadata:
        """Bundle metadata."""
        ...
    
    def validate(self) -> bool:
        """Validate bundle structure and contents."""
        ...
    
    def load(self) -> None:
        """Load bundle contents."""
        ...

@attrs.define
class Bundle(ABC):
    """Base implementation of a bundle."""
    path: Path
    metadata: BundleMetadata = attrs.field(init=False)
    _loaded: bool = attrs.field(default=False, init=False)
    
    def __attrs_post_init__(self):
        """Initialize bundle after attrs creation."""
        if not self.path.exists():
            raise ValueError(f"Bundle path does not exist: {self.path}")
        self.metadata = self._load_metadata()
    
    @abstractmethod
    def _load_metadata(self) -> BundleMetadata:
        """Load metadata from bundle. Must be implemented by subclasses."""
        ...
    
    @abstractmethod
    def validate(self) -> bool:
        """Validate bundle structure."""
        ...
    
    def load(self) -> None:
        """Load bundle contents."""
        if not self._loaded:
            self._do_load()
            self._loaded = True
    
    @abstractmethod
    def _do_load(self) -> None:
        """Actually load the bundle contents."""
        ...
```

### 2. Bundle Discovery

```python
# wrkenv/bundler/discovery.py

@attrs.define
class BundleDiscovery:
    """Discovers bundles from filesystem."""
    
    search_paths: List[Path] = attrs.field(factory=list)
    bundle_suffix: str = attrs.field()  # e.g., ".agents", ".garnish"
    bundle_class: type[Bundle] = attrs.field()
    
    def discover(self, 
                 filter_tags: Optional[List[str]] = None,
                 filter_name: Optional[str] = None) -> List[Bundle]:
        """Discover all bundles matching criteria."""
        bundles = []
        
        for search_path in self.search_paths:
            if not search_path.exists():
                continue
                
            # Find all directories with the suffix
            for bundle_path in search_path.rglob(f"*{self.bundle_suffix}"):
                if bundle_path.is_dir():
                    try:
                        bundle = self.bundle_class(path=bundle_path)
                        if self._matches_filters(bundle, filter_tags, filter_name):
                            bundles.append(bundle)
                    except Exception as e:
                        logger.warning(f"Failed to load bundle at {bundle_path}: {e}")
        
        return bundles
    
    def _matches_filters(self, bundle: Bundle, 
                        filter_tags: Optional[List[str]], 
                        filter_name: Optional[str]) -> bool:
        """Check if bundle matches filters."""
        if filter_name and filter_name not in bundle.metadata.name:
            return False
        
        if filter_tags:
            bundle_tags = set(bundle.metadata.tags)
            filter_tags_set = set(filter_tags)
            if not bundle_tags.intersection(filter_tags_set):
                return False
        
        return True
```

### 3. Bundle Compiler

```python
# wrkenv/bundler/compiler.py

@attrs.define
class CompilationResult:
    """Result of bundle compilation."""
    content: str
    metadata: Dict[str, Any]
    warnings: List[str] = attrs.field(factory=list)

class BundleCompiler(Protocol):
    """Protocol for bundle compilers."""
    
    def compile(self, bundles: List[Bundle]) -> CompilationResult:
        """Compile bundles into output format."""
        ...

@attrs.define
class BaseCompiler(ABC):
    """Base implementation for compilers."""
    
    output_format: str = attrs.field(default="markdown")
    
    @abstractmethod
    def compile(self, bundles: List[Bundle]) -> CompilationResult:
        """Compile bundles."""
        ...
    
    def _merge_bundles(self, bundles: List[Bundle]) -> Dict[str, Bundle]:
        """Merge bundles by name, with later ones overriding."""
        merged = {}
        for bundle in bundles:
            merged[bundle.metadata.name] = bundle
        return merged
```

### 4. Template Support

```python
# wrkenv/bundler/templates.py

from jinja2 import Environment, FileSystemLoader
from typing import Dict, Callable, Any

@attrs.define
class TemplateEngine:
    """Jinja2-based template engine for bundles."""
    
    template_paths: List[Path] = attrs.field(factory=list)
    custom_functions: Dict[str, Callable] = attrs.field(factory=dict)
    
    def __attrs_post_init__(self):
        """Initialize Jinja2 environment."""
        self.env = Environment(
            loader=FileSystemLoader(self.template_paths),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        
        # Add custom functions
        for name, func in self.custom_functions.items():
            self.env.globals[name] = func
    
    def render(self, template_name: str, context: Dict[str, Any]) -> str:
        """Render a template with context."""
        template = self.env.get_template(template_name)
        return template.render(**context)
```

## Integration Examples

### 1. Agents Implementation

```python
# tofusoup/agents/models.py

from wrkenv.bundler import Bundle, BundleMetadata
import yaml

@attrs.define
class AgentBundle(Bundle):
    """Bundle for AI agent configurations."""
    
    # Agent-specific attributes
    context_files: List[Path] = attrs.field(factory=list, init=False)
    tools: Dict[str, Any] = attrs.field(factory=dict, init=False)
    examples: List[Dict[str, Any]] = attrs.field(factory=list, init=False)
    
    def _load_metadata(self) -> BundleMetadata:
        """Load metadata from agent.yaml."""
        agent_yaml = self.path / "agent.yaml"
        if not agent_yaml.exists():
            raise ValueError(f"No agent.yaml found in {self.path}")
        
        with open(agent_yaml) as f:
            data = yaml.safe_load(f)
        
        return BundleMetadata(
            name=data["name"],
            version=data.get("version", "1.0.0"),
            type="agents",
            description=data.get("description"),
            tags=data.get("tags", []),
        )
    
    def validate(self) -> bool:
        """Validate agent bundle structure."""
        required_dirs = ["context", "tools", "examples"]
        for dir_name in required_dirs:
            if not (self.path / dir_name).exists():
                return False
        return True
    
    def _do_load(self) -> None:
        """Load agent bundle contents."""
        # Load context files
        context_dir = self.path / "context"
        self.context_files = list(context_dir.glob("*.md"))
        
        # Load tools
        tools_file = self.path / "tools" / "tools.yaml"
        if tools_file.exists():
            with open(tools_file) as f:
                self.tools = yaml.safe_load(f)
        
        # Load examples
        examples_dir = self.path / "examples"
        for example_file in examples_dir.glob("*.yaml"):
            with open(example_file) as f:
                self.examples.append(yaml.safe_load(f))

# Usage in tofusoup
from wrkenv.bundler import BundleDiscovery

agent_discovery = BundleDiscovery(
    search_paths=[Path("~/.agents"), Path(".agents")],
    bundle_suffix=".agents",
    bundle_class=AgentBundle,
)

agents = agent_discovery.discover(filter_tags=["terraform"])
```

### 2. Garnish Implementation

```python
# tofusoup/garnish/models.py

from wrkenv.bundler import Bundle, BundleMetadata

@attrs.define
class GarnishBundle(Bundle):
    """Bundle for documentation."""
    
    # Garnish-specific attributes
    docs: List[Path] = attrs.field(factory=list, init=False)
    examples: List[Path] = attrs.field(factory=list, init=False)
    fixtures: List[Path] = attrs.field(factory=list, init=False)
    
    def _load_metadata(self) -> BundleMetadata:
        """Load metadata from bundle structure."""
        # Garnish bundles are named by directory
        name = self.path.stem  # Remove .garnish suffix
        
        # Check for metadata file
        meta_file = self.path / "meta.yaml"
        if meta_file.exists():
            with open(meta_file) as f:
                data = yaml.safe_load(f)
                return BundleMetadata(
                    name=name,
                    version=data.get("version", "1.0.0"),
                    type="garnish",
                    description=data.get("description"),
                    tags=data.get("tags", []),
                )
        
        # Default metadata
        return BundleMetadata(
            name=name,
            version="1.0.0",
            type="garnish",
        )
    
    def validate(self) -> bool:
        """Validate garnish bundle."""
        # At least one of these should exist
        return any([
            (self.path / "docs").exists(),
            (self.path / "examples").exists(),
            (self.path / "fixtures").exists(),
        ])
    
    def _do_load(self) -> None:
        """Load garnish contents."""
        if (self.path / "docs").exists():
            self.docs = list((self.path / "docs").glob("*.md"))
        
        if (self.path / "examples").exists():
            self.examples = list((self.path / "examples").glob("*"))
        
        if (self.path / "fixtures").exists():
            self.fixtures = list((self.path / "fixtures").glob("*"))
```

## Benefits of This Approach

1. **Shared Infrastructure**: Both .agents and .garnish use the same discovery, validation, and compilation infrastructure
2. **Type Safety**: Using attrs and protocols provides excellent type checking
3. **Extensibility**: New bundle types can be added by implementing the Bundle ABC
4. **Flexibility**: Each bundle type can have its own specific attributes and behavior
5. **Testing**: The protocol-based design makes it easy to create test doubles
6. **Performance**: Lazy loading of bundle contents only when needed

## Migration Path

1. **Phase 1**: Implement bundler system in wrkenv
2. **Phase 2**: Update garnish to use wrkenv.bundler as a base
3. **Phase 3**: Implement agents using wrkenv.bundler
4. **Phase 4**: Deprecate duplicate code in garnish

## API Design

```python
# High-level API for bundle users
from wrkenv.bundler import discover_bundles, compile_bundles

# Discover all agent bundles
agents = discover_bundles(
    bundle_type="agents",
    search_paths=["~/.agents", ".agents"],
    filter_tags=["terraform", "aws"]
)

# Compile to markdown
result = compile_bundles(
    bundles=agents,
    output_format="markdown",
    compiler_class=AgentCompiler,
)

# Write output
Path("AGENTS.md").write_text(result.content)
```

This design provides a clean, extensible foundation that both .agents and .garnish can build upon while maintaining their unique characteristics.