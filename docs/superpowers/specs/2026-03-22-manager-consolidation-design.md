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

Remove the stale comment on line 21:
```python
# Use explicit imports: from wrknv.wenv import config, managers, etc.
```

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
- `grep -r "wenv\.managers\|wenv/managers" src/ tests/` returns zero results (excluding `wenv/operations/` which is unrelated)
- `uv run python -m pytest tests/ -q` passes with no regressions
- `uv run python -m pytest tests/managers/ --cov=src/wrknv/managers --cov-report=term-missing` shows 100% coverage for all `managers/` modules
- `uv run ruff check src tests` passes clean
