# Quick Wins: Dead Code Cleanup

**Date:** 2026-03-22
**Effort:** #1 of 3 (tech debt series)
**Risk:** None — deletions only, no behavior changes

## Problem

Three categories of dead weight identified in the architectural review:

1. `logging/setup.py` and `logging/emojis.py` — two no-op functions called from `main()` on every invocation. The underlying Foundation module they depend on does not exist. The functions contain only commented-out code.
2. `config/sources.py` — `FileConfigSource`, `EnvironmentConfigSource`, and `ConfigSource` are defined but not used anywhere in the actual config loading path (`WorkenvConfig.load()`). They are exported from `config/__init__.py` but have no production callers.
3. `hub_cli.py` hardcoded version — `version="0.3.0"` is hardcoded in `create_cli()`, drifting from the real version tracked in the `VERSION` file and read via `wrknv.__version__` (currently `0.3.21`).

## Approach

Full delete. No stubs, no deprecation markers — these are clearly dead with no future use indicated.

## Changes

### 1. Delete `logging/` module

**Files to delete:**
- `src/wrknv/logging/setup.py`
- `src/wrknv/logging/emojis.py`
- `src/wrknv/logging/__init__.py`
- `tests/logging/__init__.py`
- `tests/logging/test_logging.py`

**Files to modify:**
- `src/wrknv/cli/hub_cli.py` — remove import of `setup_wrknv_logging` (line 273) and the call to it (line 275)
- `tests/cli/test_hub_cli.py` — remove `patch("wrknv.logging.setup.setup_wrknv_logging")` from `test_main_runs_cli_when_no_task` (line 410) and `test_main_returns_early_when_task_intercepted` (line 429)

### 2. Delete `config/sources.py`

**Files to delete:**
- `src/wrknv/config/sources.py`
- `tests/config/test_config_sources.py`
- `scripts/memray/memray_config_parsing_stress.py` — this script exercises `FileConfigSource` and `EnvironmentConfigSource` exclusively; it has no value once the sources module is gone

**Files to modify:**
- `src/wrknv/config/__init__.py` — remove imports and `__all__` entries for `ConfigSource`, `FileConfigSource`, `EnvironmentConfigSource`

### 3. Fix hardcoded version string

**Files to modify:**
- `src/wrknv/cli/hub_cli.py` — import `__version__` from `wrknv` and replace `version="0.3.0"` with `version=__version__`

### 4. Untrack `mutants/` directory

The `mutants/` directory is a generated mutmut artifact that was inadvertently committed. It contains stale copies of files being deleted and should not be tracked.

- Add `mutants/` to `.gitignore`
- Run `git rm -r --cached mutants/` to untrack it

## Acceptance Criteria

- All deleted files are gone with no remaining references (`grep -r "wrknv.logging\|config.sources\|FileConfigSource\|EnvironmentConfigSource" src/ tests/` returns zero results)
- `uv run python -m pytest tests/ -v` passes with no regressions
- `uv run ruff check src tests` passes clean
- `wrknv --version` outputs the correct version from the `VERSION` file (`0.3.21`)
- `mutants/` is absent from `git ls-files`
