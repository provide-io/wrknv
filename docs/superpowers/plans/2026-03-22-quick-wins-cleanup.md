# Quick Wins: Dead Code Cleanup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove three categories of dead code — a no-op logging module, an unused config sources module, and a hardcoded version string — and untrack a stale generated directory.

**Architecture:** Pure deletion with minimal modification. No new code is introduced. Each task is independent and can be committed separately. The order below minimizes the chance of a broken intermediate state.

**Tech Stack:** Python 3.11+, pytest, ruff, git

**Spec:** `docs/superpowers/specs/2026-03-22-quick-wins-design.md`

---

### Task 1: Untrack `mutants/` directory

The `mutants/` directory is a mutmut-generated artifact that was accidentally committed. It contains stale copies of source files and should not be in version control.

**Files:**
- Modify: `.gitignore`
- Remove from index: `mutants/` (all tracked files)

- [ ] **Step 1: Add `mutants/` to `.gitignore`**

Open `.gitignore` and add the following line in the "Build artifacts" section (near `bfiles-*.txt`):

```
# mutmut mutation testing output (generated, not tracked)
mutants/
```

- [ ] **Step 2: Untrack the directory from git**

```bash
git rm -r --cached mutants/
```

Expected output: a long list of `rm 'mutants/...'` lines, one per tracked file.

- [ ] **Step 3: Verify `mutants/` is no longer tracked**

```bash
git ls-files mutants/
```

Expected output: empty (no lines).

- [ ] **Step 4: Commit**

```bash
git add .gitignore
git commit -m "chore: untrack mutants/ directory from git"
```

---

### Task 2: Delete the `logging/` module

The `wrknv.logging` module contains two no-op functions (`setup_wrknv_logging`, `setup_wrknv_config_logging`) that are called on every CLI invocation but do nothing. The Foundation module they were intended to call does not exist. The emoji constants file exists only to support them.

**Files:**
- Delete: `src/wrknv/logging/setup.py`
- Delete: `src/wrknv/logging/emojis.py`
- Delete: `src/wrknv/logging/__init__.py`
- Delete: `tests/logging/test_logging.py`
- Delete: `tests/logging/__init__.py`
- Modify: `src/wrknv/cli/hub_cli.py` (lines 272–275)
- Modify: `tests/cli/test_hub_cli.py` (lines 410, 429)

- [ ] **Step 1: Delete the logging source files**

```bash
git rm src/wrknv/logging/setup.py src/wrknv/logging/emojis.py src/wrknv/logging/__init__.py
```

- [ ] **Step 2: Delete the logging test files**

```bash
git rm tests/logging/test_logging.py tests/logging/__init__.py
```

- [ ] **Step 3: Remove the import and call from `hub_cli.py`**

In `src/wrknv/cli/hub_cli.py`, remove these 3 lines (currently lines 272–275):

```python
    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

```

The surrounding context before the change:
```python
    hub.initialize_foundation(telemetry_config)

    # Set up wrknv-specific logging (emoji hierarchy)
    from wrknv.logging.setup import setup_wrknv_logging

    setup_wrknv_logging()

    # Set initial process title
    set_process_title("we")
```

The surrounding context after the change:
```python
    hub.initialize_foundation(telemetry_config)

    # Set initial process title
    set_process_title("we")
```

- [ ] **Step 4: Remove the patches from `test_hub_cli.py`**

In `tests/cli/test_hub_cli.py`, remove the patch line `patch("wrknv.logging.setup.setup_wrknv_logging"),` from **two** places:

First occurrence (currently around line 410) — inside `test_main_runs_cli_when_no_task`:
```python
        with (
            patch("wrknv.config.WorkenvConfig.from_env", return_value=mock_cfg),
            patch("wrknv.cli.hub_cli.get_hub"),
            patch("wrknv.cli.hub_cli.create_cli", return_value=mock_cli),
            patch("wrknv.cli.hub_cli.intercept_task_command", return_value=False),
            patch("wrknv.logging.setup.setup_wrknv_logging"),   # <-- remove this line
            patch("attrs.evolve", side_effect=lambda x, **kw: x),
```

Second occurrence (currently around line 429) — inside `test_main_returns_early_when_task_intercepted`:
```python
        with (
            patch("wrknv.config.WorkenvConfig.from_env", return_value=mock_cfg),
            patch("wrknv.cli.hub_cli.get_hub"),
            patch("wrknv.cli.hub_cli.create_cli") as mock_create_cli,
            patch("wrknv.cli.hub_cli.intercept_task_command", return_value=True),
            patch("wrknv.logging.setup.setup_wrknv_logging"),   # <-- remove this line
            patch("attrs.evolve", side_effect=lambda x, **kw: x),
```

- [ ] **Step 5: Run the affected tests to verify they pass**

```bash
uv run python -m pytest tests/cli/test_hub_cli.py -v
```

Expected: all tests in this file pass.

- [ ] **Step 6: Verify no remaining references to `wrknv.logging`**

```bash
grep -r "wrknv.logging\|setup_wrknv_logging" src/ tests/
```

Expected output: empty (no lines).

- [ ] **Step 7: Commit**

```bash
git add src/wrknv/cli/hub_cli.py tests/cli/test_hub_cli.py
git commit -m "chore: delete dead logging module and no-op setup calls"
```

---

### Task 3: Delete `config/sources.py` and related files

`FileConfigSource`, `EnvironmentConfigSource`, and `ConfigSource` are defined in `src/wrknv/config/sources.py` and exported from `config/__init__.py`, but they are not used anywhere in the real config loading path (`WorkenvConfig.load()`). The memray stress script that exercises them is also dead weight.

**Files:**
- Delete: `src/wrknv/config/sources.py`
- Delete: `tests/config/test_config_sources.py`
- Delete: `scripts/memray/memray_config_parsing_stress.py`
- Modify: `src/wrknv/config/__init__.py`

- [ ] **Step 1: Delete the source and test files**

```bash
git rm src/wrknv/config/sources.py tests/config/test_config_sources.py scripts/memray/memray_config_parsing_stress.py
```

- [ ] **Step 2: Remove exports from `config/__init__.py`**

In `src/wrknv/config/__init__.py`, remove these lines:

```python
from .sources import (
    ConfigSource,
    EnvironmentConfigSource,
    FileConfigSource,
)
```

And remove these three entries from `__all__`:

```python
    "ConfigSource",
    "EnvironmentConfigSource",
    "FileConfigSource",
```

After the change, `config/__init__.py` should look like:

```python
from __future__ import annotations

from .core import (
    WorkenvConfig,
    WorkenvConfigError,
    WorkenvSettings,
    WorkenvToolConfig,
)
from .display import WorkenvConfigDisplay
from .persistence import WorkenvConfigPersistence
from .validation import WorkenvConfigValidator

__all__ = [
    "WorkenvConfig",
    "WorkenvConfigDisplay",
    "WorkenvConfigError",
    "WorkenvConfigPersistence",
    "WorkenvConfigValidator",
    "WorkenvSettings",
    "WorkenvToolConfig",
]

# 🧰🌍🔚
```

- [ ] **Step 3: Run the config tests to verify they pass**

```bash
uv run python -m pytest tests/config/ -v
```

Expected: all tests pass (the deleted test file is gone, remaining config tests unaffected).

- [ ] **Step 4: Verify no remaining references**

```bash
grep -r "config\.sources\|FileConfigSource\|EnvironmentConfigSource\|ConfigSource" src/ tests/ scripts/
```

Expected output: empty (no lines). Note: `provide.foundation.config.types` also exports a `ConfigSource` — that is unrelated and will not appear in this grep since it lives outside `src/wrknv`.

- [ ] **Step 5: Commit**

```bash
git add src/wrknv/config/__init__.py
git commit -m "chore: delete unused config sources module and memray stress script"
```

---

### Task 4: Fix hardcoded version string in `hub_cli.py`

`create_cli()` passes `version="0.3.0"` to the hub, but the real version is `0.3.21` and is already available as `wrknv.__version__`. This will drift on every release.

**Files:**
- Modify: `src/wrknv/cli/hub_cli.py`

- [ ] **Step 1: Add `__version__` import to `hub_cli.py`**

At the top of `src/wrknv/cli/hub_cli.py`, find the existing imports block. Add one line importing `__version__`:

```python
from wrknv import __version__
```

Place it with the other `wrknv` imports (near the bottom of the import block, alongside `from wrknv.config import ...`).

- [ ] **Step 2: Replace the hardcoded version**

Find line 104 in `src/wrknv/cli/hub_cli.py`:

```python
        version="0.3.0",
```

Replace with:

```python
        version=__version__,
```

- [ ] **Step 3: Verify the version is correct at runtime**

```bash
uv run wrknv --version
```

Expected output: `wrknv, version 0.3.21` (or whatever the current `VERSION` file contains).

- [ ] **Step 4: Run the hub CLI tests**

```bash
uv run python -m pytest tests/cli/test_hub_cli.py -v
```

Expected: all tests pass.

- [ ] **Step 5: Commit**

```bash
git add src/wrknv/cli/hub_cli.py
git commit -m "fix: use __version__ instead of hardcoded version string in CLI"
```

---

### Task 5: Final verification

- [ ] **Step 1: Run the full test suite**

```bash
uv run python -m pytest tests/ -v --cov=src/wrknv --cov-report=term-missing
```

Expected: all tests pass, coverage at or above previous baseline (~97%).

- [ ] **Step 2: Run ruff**

```bash
uv run ruff check src tests
```

Expected: no errors.

- [ ] **Step 3: Full reference check**

```bash
grep -r "wrknv\.logging\|setup_wrknv_logging\|config\.sources\|FileConfigSource\|EnvironmentConfigSource" src/ tests/ scripts/
```

Expected output: empty.

- [ ] **Step 4: Confirm `mutants/` not tracked**

```bash
git ls-files mutants/
```

Expected output: empty.

- [ ] **Step 5: Confirm version**

```bash
uv run wrknv --version
```

Expected: version matches content of `VERSION` file.
