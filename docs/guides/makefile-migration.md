# Migrating from Makefile to `we` Tasks

Complete guide for replacing Makefiles with `wrknv.toml` task definitions across the provide.io ecosystem.

## Overview

The provide.io ecosystem currently uses canonical Makefiles (templated from provide-foundry) across ~16 projects. This guide shows how to migrate to the `we` task system while maintaining all functionality.

## Current State

### Makefile Distribution

**Projects with Makefiles:**
- provide-foundation
- provide-foundry
- provide-testkit
- pyvider
- pyvider-cty
- pyvider-hcl
- pyvider-rpcplugin
- pyvider-components
- flavorpack
- tofusoup
- plating
- supsrc
- wrknv
- terraform-provider-pyvider
- terraform-provider-tofusoup
- Workspace root

**Current Pattern:**
```makefile
# Python Library Makefile
# Source: provide-foundry/src/provide/foundry/config/Makefile.python.tmpl
# This file is maintained in provide-foundry and extracted to library projects
```

### Typical Makefile Targets (~35 targets)

**Testing:**
- test, test-parallel, test-verbose, test-unit, test-integration
- coverage, coverage-xml
- mutation-run, mutation-results, mutation-browse, mutation-clean

**Code Quality:**
- lint, lint-fix
- format, format-check
- typecheck
- quality, quality-all

**Development:**
- setup, dev-setup, dev-test, dev-check
- install, uninstall
- lock, version

**CI/CD:**
- ci-test, ci-quality, ci-all

**Documentation:**
- docs-setup, docs-build, docs-serve, docs-clean

**Build:**
- build, clean

## Migration Strategy

### Phase 1: Template Creation in provide-foundry

**1.1 Create wrknv.toml Template**

Create `provide-foundry/src/provide/foundry/config/wrknv.toml.tmpl`:

```toml
# wrknv.toml
# Canonical task configuration for Python library projects in provide.io
# This file is maintained in provide-foundry and extracted to library projects
#
# Source: provide-foundry/src/provide/foundry/config/wrknv.toml.tmpl
# To update: Extract from provide-foundry or run foundry sync

project_name = "{{ project_name }}"
version = "{{ version }}"

# ==============================================================================
# 🧪 Testing Tasks
# ==============================================================================

[tasks.test]
_default = "uv run pytest"
description = "Run all tests"

unit = "uv run pytest tests/unit/"
integration = "uv run pytest tests/integration/"
parallel = "uv run pytest -n auto"
verbose = "uv run pytest -v"

[tasks.test.coverage]
run = "uv run pytest --cov={{ package_name }} --cov-report=term-missing"
description = "Run tests with coverage"

xml = "uv run pytest --cov={{ package_name }} --cov-report=xml"

[tasks.test.mutation]
run = "uv run mutmut run"
description = "Run mutation testing"

results = "uv run mutmut results"
browse = "uv run mutmut html && open html/index.html"
clean = "rm -rf .mutmut-cache htmlcov/"

# ==============================================================================
# 🎨 Code Quality Tasks
# ==============================================================================

[tasks]
lint = "uv run ruff check src/ tests/"
format = "uv run ruff format src/ tests/"
typecheck = "uv run mypy src/"

[tasks.lint]
fix = "uv run ruff check --fix src/ tests/"
description = "Lint with auto-fix"

[tasks.format]
check = "uv run ruff format --check src/ tests/"
description = "Check formatting without changes"

# Composite quality tasks
[tasks.quality]
run = ["lint", "typecheck", "format.check"]
description = "Run all quality checks"

all = ["lint", "typecheck", "format.check", "test.coverage"]

# ==============================================================================
# 🔧 Setup & Development Tasks
# ==============================================================================

[tasks]
setup = "uv sync"

[tasks.dev]
setup = "uv sync --all-extras"
test = "uv run pytest -x"
check = "uv run pytest tests/unit/ -x"

# ==============================================================================
# 🚀 CI/CD Tasks
# ==============================================================================

[tasks.ci]
test = "uv run pytest -v"
quality = "we quality"
all = "we quality && we ci.test"
description = "Complete CI pipeline"

# ==============================================================================
# 📚 Documentation Tasks
# ==============================================================================

[tasks.docs]
_default = "mkdocs serve"
description = "Serve documentation locally"

setup = "uv sync --group docs"
build = "mkdocs build --strict"
serve = "mkdocs serve"
clean = "rm -rf site/"

# ==============================================================================
# 📦 Build & Distribution Tasks
# ==============================================================================

[tasks]
build = "uv build"
clean = "rm -rf dist/ build/ *.egg-info"

[tasks.build]
wheel = "uv build --wheel"
sdist = "uv build --sdist"

# ==============================================================================
# 🔐 Lock & Version Management
# ==============================================================================

[tasks]
lock = "uv lock"
version = "uv run hatch version"

[tasks.install]
run = "uv pip install -e ."
description = "Install in editable mode"

uninstall = "uv pip uninstall {{ package_name }}"
```

**1.2 Create Extraction Script**

Add to provide-foundry:

```python
# provide-foundry/src/provide/foundry/extract.py

from pathlib import Path
from jinja2 import Template

def extract_wrknv_toml(target_dir: Path, project_name: str, package_name: str, version: str):
    """Extract wrknv.toml template to target directory."""
    template_path = Path(__file__).parent / "config" / "wrknv.toml.tmpl"
    template = Template(template_path.read_text())

    output = template.render(
        project_name=project_name,
        package_name=package_name,
        version=version,
    )

    output_path = target_dir / "wrknv.toml"
    output_path.write_text(output)

    return output_path
```

### Phase 2: Project-by-Project Migration

**Migration Order** (low-risk to high-risk):

1. **Pilot: wrknv** (already has wrknv.toml)
2. **Foundation libraries:**
   - provide-foundation
   - provide-testkit
3. **Utility libraries:**
   - supsrc
   - tofusoup
   - flavorpack
4. **Pyvider ecosystem:**
   - pyvider-cty
   - pyvider-hcl
   - pyvider-rpcplugin
   - pyvider-components
   - pyvider
5. **Tools:**
   - plating
6. **Providers:**
   - terraform-provider-pyvider
   - terraform-provider-tofusoup
7. **Foundry:** provide-foundry (last, as it templates others)

**Per-Project Steps:**

1. Extract wrknv.toml from foundry template
2. Customize for project-specific tasks
3. Test all tasks work: `we tasks` and run each
4. Update CI workflows to use `we` commands
5. Add deprecation notice to Makefile
6. Document migration in project CHANGELOG

### Phase 3: Cross-Package Task Execution (Optional)

**For workspace-level orchestration:**

Enable Phase 2 features (package discovery):

```toml
# Workspace root wrknv.toml

[workspace]
discover = true  # Auto-discover sibling packages

[tasks.workspace]
test-all = "@all test"
quality-all = "@all quality"
build-all = "@all build"

[tasks.ci]
run = ["workspace.quality-all", "workspace.test-all"]
description = "CI across all packages"
```

This requires implementing Phase 2 (4-6 hours).

## Migration Examples

### Example 1: Simple Task

**Makefile:**
```makefile
test: ## Run all tests
	@echo 'Running tests...'
	uv run pytest
	@echo '✓ Tests complete'
```

**wrknv.toml:**
```toml
[tasks]
test = "uv run pytest"
```

Output formatting is handled by `we` automatically.

### Example 2: Nested Task Group

**Makefile:**
```makefile
test-unit: ## Run unit tests
	uv run pytest tests/unit/

test-integration: ## Run integration tests
	uv run pytest tests/integration/

test-parallel: ## Run tests in parallel
	uv run pytest -n auto
```

**wrknv.toml:**
```toml
[tasks.test]
unit = "uv run pytest tests/unit/"
integration = "uv run pytest tests/integration/"
parallel = "uv run pytest -n auto"
```

Usage: `we test unit`, `we test integration`, `we test parallel`

### Example 3: Composite Task

**Makefile:**
```makefile
quality: ## Run all quality checks
	$(MAKE) lint
	$(MAKE) typecheck
	$(MAKE) format-check
```

**wrknv.toml:**
```toml
[tasks.quality]
run = ["lint", "typecheck", "format.check"]
description = "Run all quality checks"
```

### Example 4: Task with Arguments

**Makefile:**
```makefile
test: ## Run tests
	uv run pytest $(ARGS)
```

**wrknv.toml:**
```toml
[tasks]
test = "uv run pytest"
```

Usage: `we test --verbose -x` (arguments passed automatically)

### Example 5: CI Pipeline

**Makefile:**
```makefile
ci-all: ## Complete CI pipeline
	$(MAKE) quality
	$(MAKE) test
	$(MAKE) build
```

**wrknv.toml:**
```toml
[tasks.ci]
run = ["quality", "test", "build"]
description = "Complete CI pipeline"
```

## Task Location Strategy

### Option 1: Each Package Owns Its Tasks (RECOMMENDED)

**Structure:**
```
provide-io/
├── pyvider/
│   └── wrknv.toml          # Pyvider-specific tasks
├── pyvider-cty/
│   └── wrknv.toml          # CTY-specific tasks
├── provide-foundation/
│   └── wrknv.toml          # Foundation-specific tasks
└── wrknv.toml              # Workspace-level orchestration only
```

**Pros:**
- ✅ Each package is self-contained
- ✅ Tasks travel with the package
- ✅ No cross-package dependencies
- ✅ Works immediately (no Phase 2 needed)
- ✅ Packages can be used independently

**Cons:**
- ❌ Some duplication across packages
- ❌ Need to run `we test` in each package

**Best for:** Current ecosystem structure

### Option 2: Centralized with Package References (FUTURE)

**Structure:**
```
provide-io/
├── wrknv.toml              # All workspace tasks + package refs
├── pyvider/
│   └── wrknv.toml          # Exports: test, lint, build
├── pyvider-cty/
│   └── wrknv.toml          # Exports: test, lint
└── provide-foundation/
    └── wrknv.toml          # Exports: test, lint, docs
```

**Workspace wrknv.toml:**
```toml
[workspace]
discover = true

[tasks.test]
pyvider = "@pyvider.test"
cty = "@pyvider-cty.test"
foundation = "@provide-foundation.test"
all = "@all test"  # Run test in all packages
```

**Pros:**
- ✅ Single entry point for all operations
- ✅ Consistent task names across packages
- ✅ Workspace-level orchestration

**Cons:**
- ❌ Requires Phase 2 implementation (4-6 hours)
- ❌ More complex mental model
- ❌ Packages less self-contained

**Best for:** After Phase 2, if workspace orchestration is priority

### Option 3: Hybrid (RECOMMENDED FOR MIGRATION)

**Each package has full tasks:**
```toml
# pyvider/wrknv.toml
[tasks]
test = "uv run pytest"
lint = "uv run ruff check ."
build = "uv build"

[export]
tasks = ["test", "lint", "build"]  # Mark for potential future import
```

**Workspace has orchestration:**
```toml
# /wrknv.toml (workspace root)
[tasks.all]
test = "for dir in */; do cd $dir && we test && cd ..; done"
quality = "for dir in */; do cd $dir && we quality && cd ..; done"
```

**Pros:**
- ✅ Works now without Phase 2
- ✅ Each package self-contained
- ✅ Workspace can orchestrate
- ✅ Ready for Phase 2 when implemented

**Cons:**
- ❌ Bash loops aren't as elegant as `@all test`

## CI/CD Integration

### GitHub Actions Example

**Before (Makefile):**
```yaml
- name: Run tests
  run: make test

- name: Quality checks
  run: make quality

- name: Build
  run: make build
```

**After (we tasks):**
```yaml
- name: Run tests
  run: we test

- name: Quality checks
  run: we quality

- name: Build
  run: we build
```

Or use the composite CI task:

```yaml
- name: CI Pipeline
  run: we ci
```

### Update All GitHub Workflows

**Script to update workflows:**
```bash
# In each project
find .github/workflows -name "*.yml" -o -name "*.yaml" | while read f; do
  sed -i '' 's/make test/we test/g' "$f"
  sed -i '' 's/make quality/we quality/g' "$f"
  sed -i '' 's/make build/we build/g' "$f"
  sed -i '' 's/make ci-all/we ci/g' "$f"
done
```

## Implementation Plan

### Timeline

**Phase 1: Template Creation** (2-3 hours)
- Create wrknv.toml.tmpl in provide-foundry
- Add extraction script
- Test extraction on one project

**Phase 2: Pilot Migration** (1 hour each x 3 projects)
- wrknv (already done)
- provide-foundation (low-risk)
- provide-testkit (low-risk)

**Phase 3: Bulk Migration** (0.5 hours each x 13 projects)
- Extract template
- Customize per-project
- Update CI workflows
- Test all tasks

**Phase 4: Deprecation** (1 hour)
- Add deprecation notices to Makefiles
- Update workspace documentation
- Communicate to team

**Total Time:** ~12-14 hours for complete migration

### Rollout Strategy

**Week 1:** Template + 3 pilots
**Week 2:** Foundation libraries (3 projects)
**Week 3:** Pyvider ecosystem (5 projects)
**Week 4:** Tools + providers (5 projects)
**Week 5:** Cleanup + deprecation

## Benefits After Migration

### Developer Experience

**Before:**
```bash
make test              # Makefile syntax
make test-unit         # Dash-separated
make ci-all            # Inconsistent naming
ARGS="--verbose" make test   # Awkward arg passing
```

**After:**
```bash
we test                # Clean, simple
we test unit           # Hierarchical
we ci                  # Consistent naming
we test --verbose      # Natural arg passing
we tasks               # Beautiful tree view
```

### Maintainability

**Before:**
- Makefiles scattered across 16 projects
- Template in provide-foundry must be extracted manually
- Bash script complexity for simple tasks
- Color codes and formatting duplication

**After:**
- Clean TOML configuration
- Template extraction automated
- Simple command strings
- Formatting handled by `we`

### Discoverability

**Before:**
```bash
make help              # Requires special target
# Output: grep magic on Makefile
```

**After:**
```bash
we tasks               # Built-in, beautiful
# Output:
# Available tasks:
#
# test
# ├── unit
# ├── integration
# └── coverage
#
# Flat tasks:
#   • lint
#   • format
```

## Backward Compatibility

### Transitional Period

Keep Makefiles but have them delegate to `we`:

```makefile
# Makefile (transitional)
# DEPRECATED: This Makefile is deprecated.
# Use `we TASK` directly instead of `make TASK`

test:
	@echo "DEPRECATED: Use 'we test' instead"
	we test

lint:
	@echo "DEPRECATED: Use 'we lint' instead"
	we lint

# ... etc
```

This allows gradual adoption while maintaining compatibility.

### Documentation Updates

Update all references:
- README files: `make test` → `we test`
- CONTRIBUTING guides
- CI/CD documentation
- Onboarding docs

## FAQ

### Q: Do we lose Make's dependency tracking?

**A:** We never used it. All Makefile targets are `.PHONY` (no actual files).

### Q: What about parallel execution?

**A:** Task system supports it via composite tasks. For true parallelism, use `test.parallel` task that calls `pytest -n auto`.

### Q: Can we still use Makefiles for non-task things?

**A:** Yes! Keep Makefiles for actual build artifacts (C extensions, compiled docs, etc.). Use `we` for command execution.

### Q: What if a project needs custom tasks?

**A:** Projects can extend the template. The template provides baseline, projects customize.

### Q: How do we handle workspace-level orchestration without Phase 2?

**A:** Use bash loops in workspace wrknv.toml, or implement Phase 2 (4-6 hours) for `@all` syntax.

## Next Steps

1. **Review this plan** - Discuss with team
2. **Create template** - Implement in provide-foundry
3. **Pilot on 3 projects** - Validate approach
4. **Decide on Phase 2** - Do we need `@all` workspace orchestration?
5. **Bulk migration** - Roll out to remaining projects
6. **Deprecate Makefiles** - Remove after transition period

## See Also

- [Task System Documentation](../features/task-system.md)
- [wrknv.toml Reference](../reference/wrknv-toml.md)
- [Examples](../../examples/)
