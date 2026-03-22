# Manager Hierarchy Consolidation

**Date:** 2026-03-22
**Effort:** #2 of 3 (tech debt series)
**Risk:** Low — deleting dead code with zero production callers

## Problem

Two parallel tool manager hierarchies exist in the codebase:

- `src/wrknv/wenv/managers/` — original implementation (synchronous, direct urllib, 4 tools: ibmtf, tofu, uv, go)
- `src/wrknv/managers/` — active production implementation (async-capable, GitHubReleasesClient, resilience, 6 tools: ibmtf, tofu, bao, vault, uv, go)

All production code (CLI commands, lockfile, public API) already imports exclusively from `managers/`. The `wenv/managers/` hierarchy has zero production callers — it exists only for its own tests, which test dead code. The newer `managers/` hierarchy is a strict superset: every capability of `wenv/managers/` exists in `managers/`, plus async support, resilience, secret tool management, and dedicated GitHub release handling.

Additionally, `managers/tf/base.py` has one uncovered branch (line `186->185`) that needs a targeted test to reach 100% coverage.

## Approach

Full delete of `wenv/managers/` and its tests. Add one test to cover the missed branch in `managers/tf/base.py`. No migration is needed — `managers/` is already complete and in production.

`wenv/operations/` is **not deleted** — it is actively imported by `managers/base.py`.

## What Is Deleted

### Source files

All 8 files in `src/wrknv/wenv/managers/`:
- `__init__.py`
- `base.py`
- `factory.py`
- `tf_base.py`
- `ibm_tf.py`
- `tofu.py`
- `uv.py`
- `go.py`

### Test files

13 files in `tests/wenv/`:
- `test_managers_base.py`
- `test_managers_base_coverage.py`
- `test_managers_base_install.py`
- `test_managers_factory.py`
- `test_managers_go.py`
- `test_managers_go_extended.py`
- `test_managers_ibm_tf.py`
- `test_managers_tf_base.py`
- `test_managers_tf_base_coverage.py`
- `test_managers_tf_base_extended.py`
- `test_managers_tf_base_meta.py`
- `test_managers_tofu.py`
- `test_managers_uv.py`

## What Changes

### `src/wrknv/wenv/__init__.py`

Remove the stale comment on line 21 and remove `"managers"` from `__all__` on line 23:

Before:
```python
# Submodules are available but not imported to avoid circular imports
# Use explicit imports: from wrknv.wenv import config, managers, etc.

__all__ = ["config", "managers", "operations"]
```

After:
```python
# Submodules are available but not imported to avoid circular imports

__all__ = ["config", "operations"]
```

### `docs/getting-started/installation.md`

Three code examples reference deleted module paths. Update to use `managers/` equivalents:

| Old | New |
|---|---|
| `from wrknv.wenv.managers.uv import UVManager` | `from wrknv.managers.uv import UvManager` |
| `from wrknv.wenv.managers.terraform import TerraformManager` | `from wrknv.managers.tf.ibm import IbmTfVariant` (or `TofuTfVariant`) |
| `from wrknv.wenv.managers.base import ToolManager` | `from wrknv.managers.base import BaseToolManager` |

Also update class names in the examples accordingly (`UVManager` → `UvManager`, `TerraformManager` → `IbmTfVariant`, `ToolManager` → `BaseToolManager`).

### `CONTRIBUTING.md`

Four changes in the "Adding New Tool Managers" section:

1. Line ~82: update path `src/wrknv/wenv/managers/` → `src/wrknv/managers/`
2. Line ~91: update import `from wrknv.wenv.managers.base import BaseToolManager` → `from wrknv.managers.base import BaseToolManager`
3. Line ~92: remove `from wrknv.wenv.managers.types import ToolInfo` — no `types.py` exists and there is no `ToolInfo` equivalent in `managers/`. Also remove the `get_tool_info` method body (lines ~105–110) that uses `ToolInfo`, keeping only the two required method stubs (`get_download_url` and `get_executable_name`).
4. Line ~210: update `vim src/wrknv/wenv/managers/newtool.py` → `vim src/wrknv/managers/newtool.py`

### `CLAUDE.md` (project root)

Line ~55 describes Tool Managers as living in `src/wrknv/wenv/managers/`. Update to `src/wrknv/managers/`.

### `pyproject.toml`

Remove the dead mypy override entry `"wrknv.wenv.managers.*",` from the `[[tool.mypy.overrides]]` block for wenv modules (the block around line 169).

### `tests/managers/test_managers.py`

Add one test to cover the `186->185` branch miss in `managers/tf/base.py`.

The uncovered branch is in `_install_from_archive()` — the `for file_path in extract_dir.rglob(...)` loop. The loop currently only iterates once in tests (the first file matches). The branch miss is the loop body executing more than once before breaking — i.e., the case where `rglob` returns multiple files and the first one does not match, but a later one does.

New test: mock `extract_dir.rglob()` to return two file paths — a non-matching file first, then the correct binary — and verify the correct one is selected.

## What Is Preserved

- `src/wrknv/wenv/operations/` — untouched, actively used by `managers/base.py`
- `src/wrknv/managers/` — untouched
- `tests/managers/` — unchanged except for the new test

## Acceptance Criteria

- All 8 `src/wrknv/wenv/managers/` source files are deleted with no remaining references
- All 13 `tests/wenv/test_managers_*.py` files are deleted
- `grep -r "wenv\.managers\|wenv/managers" src/ tests/ CONTRIBUTING.md CLAUDE.md pyproject.toml` returns zero results (`.egg-info/SOURCES.txt` is not searched and will be regenerated on next build; `docs/` is excluded because this spec file itself contains the old paths for documentation purposes)
- `uv run python -m pytest tests/ -q` passes with no regressions
- `uv run python -m pytest tests/managers/ --cov=src/wrknv/managers --cov-report=term-missing` shows 100% coverage for all `managers/` modules
- `uv run ruff check src tests` passes clean
