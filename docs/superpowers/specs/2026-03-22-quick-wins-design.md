# Quick Wins: Dead Code Cleanup

**Date:** 2026-03-22
**Effort:** #1 of 3 (tech debt series)
**Risk:** None — deletions only, no behavior changes

## Problem

Three categories of dead weight identified in the architectural review:

1. `logging/setup.py` and `logging/emojis.py` — two no-op functions called from `main()` on every invocation. The underlying Foundation module they depend on does not exist. The functions contain only commented-out code.
2. `config/sources.py` — `FileConfigSource`, `EnvironmentConfigSource`, and `ConfigSource` are defined but not used anywhere in the actual config loading path (`WorkenvConfig.load()`). They are exported from `config/__init__.py` but have no callers outside their own test file.
3. `hub_cli.py` hardcoded version — `version="0.3.0"` is hardcoded in `create_cli()`, drifting from the real version tracked in the `VERSION` file and read via `wrknv.__version__`.

## Approach

Full delete. No stubs, no deprecation markers — these are clearly dead with no future use indicated.

## Changes

### 1. Delete `logging/` module

**Files to delete:**
- `src/wrknv/logging/setup.py`
- `src/wrknv/logging/emojis.py`
- `src/wrknv/logging/__init__.py`
- `tests/logging/test_logging.py`

**Files to modify:**
- `src/wrknv/cli/hub_cli.py` — remove import of `setup_wrknv_logging` (line 273) and the call to it (line 275)
- `tests/cli/test_hub_cli.py` — remove `patch("wrknv.logging.setup.setup_wrknv_logging")` from the two test methods that patch it (the underlying tested behavior is unaffected)

### 2. Delete `config/sources.py`

**Files to delete:**
- `src/wrknv/config/sources.py`
- `tests/config/test_config_sources.py`

**Files to modify:**
- `src/wrknv/config/__init__.py` — remove imports and `__all__` entries for `ConfigSource`, `FileConfigSource`, `EnvironmentConfigSource`

### 3. Fix hardcoded version string

**Files to modify:**
- `src/wrknv/cli/hub_cli.py` — import `__version__` from `wrknv` and replace `version="0.3.0"` with `version=__version__`

## Acceptance Criteria

- All deleted files are gone with no remaining references
- `uv run python -m pytest tests/ -v` passes with no regressions
- `uv run ruff check src tests` passes clean
- `wrknv --version` outputs the correct version from the `VERSION` file
