# Manager Hierarchy Consolidation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Delete the dead `wenv/managers/` tool manager hierarchy and its tests, update all references to point at the active `managers/` hierarchy, and add one targeted test to reach 100% coverage on `managers/tf/base.py`.

**Architecture:** All production code already imports from `src/wrknv/managers/` — `wenv/managers/` has zero production callers and is being deleted entirely. Four prose/config files contain stale references that need mechanical text updates. One coverage gap in `managers/tf/base.py` requires a new test exercising the multi-file `rglob` branch.

**Tech Stack:** Python 3.11+, pytest, uv, provide.testkit (FoundationTestCase + patch/MagicMock)

---

## File Map

**Deleted (source):**
- `src/wrknv/wenv/managers/__init__.py`
- `src/wrknv/wenv/managers/base.py`
- `src/wrknv/wenv/managers/factory.py`
- `src/wrknv/wenv/managers/tf_base.py`
- `src/wrknv/wenv/managers/ibm_tf.py`
- `src/wrknv/wenv/managers/tofu.py`
- `src/wrknv/wenv/managers/uv.py`
- `src/wrknv/wenv/managers/go.py`

**Deleted (tests):**
- `tests/wenv/test_managers_base.py`
- `tests/wenv/test_managers_base_coverage.py`
- `tests/wenv/test_managers_base_install.py`
- `tests/wenv/test_managers_factory.py`
- `tests/wenv/test_managers_go.py`
- `tests/wenv/test_managers_go_extended.py`
- `tests/wenv/test_managers_ibm_tf.py`
- `tests/wenv/test_managers_tf_base.py`
- `tests/wenv/test_managers_tf_base_coverage.py`
- `tests/wenv/test_managers_tf_base_extended.py`
- `tests/wenv/test_managers_tf_base_meta.py`
- `tests/wenv/test_managers_tofu.py`
- `tests/wenv/test_managers_uv.py`

**Modified:**
- `src/wrknv/wenv/__init__.py` — remove stale comment line and `"managers"` from `__all__`
- `CLAUDE.md` — update Tool Managers path (~line 55)
- `pyproject.toml` — remove `"wrknv.wenv.managers.*"` mypy override entry (~line 169)
- `CONTRIBUTING.md` — 4 stale references in "Adding New Tool Managers" section
- `docs/getting-started/installation.md` — 3 stale code examples (~lines 272–296)
- `tests/managers/test_managers.py` — add one new test for the `rglob` multi-file branch

---

### Task 1: Delete `src/wrknv/wenv/managers/` source files

**Files:**
- Delete: `src/wrknv/wenv/managers/__init__.py`
- Delete: `src/wrknv/wenv/managers/base.py`
- Delete: `src/wrknv/wenv/managers/factory.py`
- Delete: `src/wrknv/wenv/managers/tf_base.py`
- Delete: `src/wrknv/wenv/managers/ibm_tf.py`
- Delete: `src/wrknv/wenv/managers/tofu.py`
- Delete: `src/wrknv/wenv/managers/uv.py`
- Delete: `src/wrknv/wenv/managers/go.py`

- [ ] **Step 1: Delete all 8 source files**

```bash
git rm src/wrknv/wenv/managers/__init__.py \
       src/wrknv/wenv/managers/base.py \
       src/wrknv/wenv/managers/factory.py \
       src/wrknv/wenv/managers/tf_base.py \
       src/wrknv/wenv/managers/ibm_tf.py \
       src/wrknv/wenv/managers/tofu.py \
       src/wrknv/wenv/managers/uv.py \
       src/wrknv/wenv/managers/go.py
```

- [ ] **Step 2: Confirm directory is empty**

```bash
ls src/wrknv/wenv/managers/
```

Expected: No such file or directory (or empty listing — the directory itself can remain; git won't track empty dirs).

- [ ] **Step 3: Verify test suite still collects**

```bash
uv run python -m pytest tests/ --collect-only -q 2>&1 | tail -5
```

Expected: Collection succeeds (some errors from `tests/wenv/` are fine — those tests will be deleted next).

- [ ] **Step 4: Commit**

```bash
git commit -m "refactor: delete dead wenv/managers source hierarchy"
```

---

### Task 2: Delete `tests/wenv/test_managers_*.py` test files

**Files:**
- Delete: all 13 `tests/wenv/test_managers_*.py` files

- [ ] **Step 1: Delete all 13 test files**

```bash
git rm tests/wenv/test_managers_base.py \
       tests/wenv/test_managers_base_coverage.py \
       tests/wenv/test_managers_base_install.py \
       tests/wenv/test_managers_factory.py \
       tests/wenv/test_managers_go.py \
       tests/wenv/test_managers_go_extended.py \
       tests/wenv/test_managers_ibm_tf.py \
       tests/wenv/test_managers_tf_base.py \
       tests/wenv/test_managers_tf_base_coverage.py \
       tests/wenv/test_managers_tf_base_extended.py \
       tests/wenv/test_managers_tf_base_meta.py \
       tests/wenv/test_managers_tofu.py \
       tests/wenv/test_managers_uv.py
```

- [ ] **Step 2: Run full test suite — confirm no regressions**

```bash
uv run python -m pytest tests/ -q 2>&1 | tail -10
```

Expected: All tests pass. The deleted tests no longer appear. Zero failures.

- [ ] **Step 3: Commit**

```bash
git commit -m "test: delete dead wenv/managers test files"
```

---

### Task 3: Update `src/wrknv/wenv/__init__.py`

**Files:**
- Modify: `src/wrknv/wenv/__init__.py`

The file currently reads (lines 20–23):
```python
# Submodules are available but not imported to avoid circular imports
# Use explicit imports: from wrknv.wenv import config, managers, etc.

__all__ = ["config", "managers", "operations"]
```

- [ ] **Step 1: Remove stale comment line and `"managers"` from `__all__`**

Replace lines 20–23 with:
```python
# Submodules are available but not imported to avoid circular imports

__all__ = ["config", "operations"]
```

- [ ] **Step 2: Run tests**

```bash
uv run python -m pytest tests/ -q 2>&1 | tail -5
```

Expected: All pass.

- [ ] **Step 3: Commit**

```bash
git add src/wrknv/wenv/__init__.py
git commit -m "refactor: remove managers from wenv __all__"
```

---

### Task 4: Update `CLAUDE.md`, `pyproject.toml`, and `CONTRIBUTING.md`

**Files:**
- Modify: `CLAUDE.md` (~line 55)
- Modify: `pyproject.toml` (~line 169)
- Modify: `CONTRIBUTING.md` (~lines 82, 91–112, 210)

These are all mechanical text replacements with no logic.

- [ ] **Step 1: Update `CLAUDE.md` line ~55**

Change:
```
**Tool Managers (`src/wrknv/wenv/managers/`)**: Abstract base class pattern for tool installation/management. Implementations for UV, Terraform, OpenTofu, Go, etc. Each manager handles platform-specific download URLs and verification.
```

To:
```
**Tool Managers (`src/wrknv/managers/`)**: Abstract base class pattern for tool installation/management. Implementations for UV, Terraform, OpenTofu, Go, Bao, Vault, etc. Each manager handles platform-specific download URLs and verification.
```

- [ ] **Step 2: Update `pyproject.toml` — remove dead mypy override**

Remove the line `"wrknv.wenv.managers.*",` from the `[[tool.mypy.overrides]]` block around line 169. The block before:
```toml
module = [
    "wrknv.wenv.schema",
    "wrknv.wenv.env_generator",
    "wrknv.wenv.managers.*",
    "wrknv.wenv.operations.*",
    "wrknv.wenv.doctor",
]
```

After:
```toml
module = [
    "wrknv.wenv.schema",
    "wrknv.wenv.env_generator",
    "wrknv.wenv.operations.*",
    "wrknv.wenv.doctor",
]
```

- [ ] **Step 3: Update `CONTRIBUTING.md` — 4 changes**

**Change 1** — line 82, update path:
```
# Before
1. **Create a manager class**: Inherit from `BaseToolManager` in `src/wrknv/wenv/managers/`
# After
1. **Create a manager class**: Inherit from `BaseToolManager` in `src/wrknv/managers/`
```

**Change 2** — line 91, update import:
```python
# Before
from wrknv.wenv.managers.base import BaseToolManager
# After
from wrknv.managers.base import BaseToolManager
```

**Change 3** — remove line 92 (`from wrknv.wenv.managers.types import ToolInfo`) and the entire `get_tool_info` method (lines 105–112). The code example after all changes should be:
```python
from wrknv.managers.base import BaseToolManager

class NewToolManager(BaseToolManager):
    """Manager for NewTool installation and management."""

    def get_download_url(self, version: str, platform: str, arch: str) -> str:
        """Get download URL for specified version and platform."""
        return f"https://releases.newtool.com/v{version}/newtool_{platform}_{arch}.zip"

    def get_executable_name(self, platform: str) -> str:
        """Get executable name for the platform."""
        return "newtool.exe" if platform == "windows" else "newtool"
```

**Change 4** — line 210, update file path:
```
# Before
vim src/wrknv/wenv/managers/newtool.py
# After
vim src/wrknv/managers/newtool.py
```

- [ ] **Step 4: Verify the grep returns zero**

```bash
grep -r "wenv\.managers\|wenv/managers" src/ tests/ CONTRIBUTING.md CLAUDE.md pyproject.toml
```

Expected: No output (zero matches).

- [ ] **Step 5: Run tests and ruff**

```bash
uv run python -m pytest tests/ -q 2>&1 | tail -5
uv run ruff check src tests
```

Expected: All pass, ruff clean.

- [ ] **Step 6: Commit**

```bash
git add CLAUDE.md pyproject.toml CONTRIBUTING.md
git commit -m "docs: update wenv/managers references to managers/"
```

---

### Task 5: Update `docs/getting-started/installation.md`

**Files:**
- Modify: `docs/getting-started/installation.md` (~lines 270–296)

The file has three stale code examples. Current content around lines 270–296:

```python
# Example 1 (~line 272):
from wrknv.wenv.managers.uv import UVManager
manager = UVManager()
await manager.ensure_installed(version="0.5.11")

# Example 2 (~line 281):
from wrknv.wenv.managers.terraform import TerraformManager
manager = TerraformManager()
await manager.ensure_installed(version="1.9.8")

# Example 3 (~line 289–295):
Extend `ToolManager` base class for custom tools:
from wrknv.wenv.managers.base import ToolManager
class CustomToolManager(ToolManager):
    async def get_download_url(self, version: str, platform: str) -> str:
```

- [ ] **Step 1: Update all three examples**

Replace with `managers/` equivalents:

```python
# Example 1:
from wrknv.managers.uv import UvManager
manager = UvManager(config)
await manager.ensure_installed(version="0.5.11")

# Example 2:
from wrknv.managers.tf.ibm import IbmTfVariant
manager = IbmTfVariant(config)
await manager.ensure_installed(version="1.9.8")

# Example 3:
Extend `BaseToolManager` base class for custom tools:
from wrknv.managers.base import BaseToolManager
class CustomToolManager(BaseToolManager):
    def get_download_url(self, version: str) -> str:
```

Also update the surrounding prose: `Extend \`ToolManager\` base class` → `Extend \`BaseToolManager\` base class`.

- [ ] **Step 2: Verify grep returns zero on docs/ too (spot-check)**

```bash
grep -r "wenv\.managers\|wenv/managers" docs/getting-started/
```

Expected: No output.

- [ ] **Step 3: Commit**

```bash
git add docs/getting-started/installation.md
git commit -m "docs: update installation.md manager examples to managers/"
```

---

### Task 6: Add coverage test for `managers/tf/base.py` rglob multi-file branch

**Files:**
- Modify: `tests/managers/test_managers.py`

**Background:** `managers/tf/base.py` lines 184–191 have an uncovered branch (`186->185`). The `for` loop over `extract_dir.rglob(...)` only ever iterates once in existing tests (the first file matches). The uncovered branch is the loop body executing a second time — i.e., the first file doesn't match the binary name check, but a later file does.

```python
# src/wrknv/managers/tf/base.py lines 184-191
binary_path = None
for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
    if file_path.is_file() and file_path.name in [
        archive_binary_name,
        f"{archive_binary_name}.exe",
    ]:
        binary_path = file_path
        break
```

The test must mock `extract_dir.rglob()` to return **two** paths: a non-matching file first (e.g., `terraform.sig`), then the correct binary (`terraform`). It must verify the correct one is selected.

**Important:** Look at the existing tests in `tests/managers/test_managers.py` and in the `tests/managers/` directory to understand the `TfBaseToolManager` test fixture pattern before writing this test. Read `src/wrknv/managers/tf/base.py` lines 140–210 to understand `_install_from_archive()`.

- [ ] **Step 1: Read the existing tf manager tests to understand the pattern**

```bash
# Find existing tf-related tests
grep -n "TfBase\|_install_from_archive\|rglob" tests/managers/ -r
```

Then read the relevant test file.

- [ ] **Step 2: Read `src/wrknv/managers/tf/base.py` lines 130–210**

Understand what `_install_from_archive` needs mocked: `zipfile.ZipFile` or `tarfile.open`, `extract_dir.rglob`, `file_path.is_file()`, `file_path.name`, `safe_copy`, `os.chmod`.

- [ ] **Step 3: Add the new test to `tests/managers/test_managers.py`**

**How `_install_from_archive` works (already read):**

```python
# src/wrknv/managers/tf/base.py lines 165-222
def _install_from_archive(self, archive_path: pathlib.Path, version: str) -> None:
    extract_dir = self.cache_dir / f"{self.tool_prefix}_{version}_extract"
    extract_dir.mkdir(exist_ok=True)
    try:
        self.extract_archive(archive_path, extract_dir)   # delegate to base class
        # ... determine archive_binary_name ...
        for file_path in extract_dir.rglob(f"{archive_binary_name}*"):
            if file_path.is_file() and file_path.name in [...]:
                binary_path = file_path
                break
        safe_copy(binary_path, target_path, overwrite=True)  # from provide.foundation.file
        self.make_executable(target_path)
        binary_hash = calculate_file_hash(target_path)       # from wrknv.managers.tf.utils
        self._update_install_metadata(version, archive_path, binary_hash)
        self._update_recent_file()
        if not self.verify_installation(version):
            raise ToolManagerError(...)
    finally:
        safe_rmtree(extract_dir, missing_ok=True)
```

**Key insight:** `extract_dir` comes from `self.cache_dir / "..."`. To control `extract_dir.rglob()`, mock `manager.cache_dir` itself so the `/` operator returns a controllable mock. There is no `zipfile`, `tempfile`, or `Path` symbol to patch in `tf/base.py`.

**Correct patch targets:**
- `wrknv.managers.tf.base.safe_copy` — imported directly in tf/base.py
- `wrknv.managers.tf.base.calculate_file_hash` — imported directly in tf/base.py
- `wrknv.managers.tf.base.safe_rmtree` — imported directly in tf/base.py
- Instance methods via attribute assignment: `manager.extract_archive`, `manager.make_executable`, `manager._update_install_metadata`, `manager._update_recent_file`, `manager.verify_installation`, `manager.get_binary_path`

Add the following test class to `tests/managers/test_managers.py`. Add the necessary import at the top of the file: `from wrknv.managers.tf.ibm import IbmTfVariant`

```python
class TestTfBaseInstallFromArchiveMultiFile(FoundationTestCase):
    """Test _install_from_archive selects the correct binary when rglob returns multiple files.

    Covers branch 186->185: the for loop iterates past a non-matching file
    before finding the correct binary.
    """

    @patch("wrknv.managers.tf.base.safe_rmtree")
    @patch("wrknv.managers.tf.base.calculate_file_hash", return_value="abc123")
    @patch("wrknv.managers.tf.base.safe_copy")
    def test_rglob_skips_non_matching_file_and_finds_binary(
        self, mock_safe_copy, mock_hash, mock_rmtree
    ) -> None:
        # Arrange
        config = WorkenvConfig()
        manager = IbmTfVariant(config)

        # Two files returned by rglob: a non-matching sig file first, then the real binary
        non_matching = MagicMock(spec=Path)
        non_matching.name = "terraform.sig"
        non_matching.is_file.return_value = True

        correct_binary = MagicMock(spec=Path)
        correct_binary.name = "terraform"
        correct_binary.is_file.return_value = True

        # mock_extract_dir controls extract_dir = self.cache_dir / "..."
        mock_extract_dir = MagicMock()
        mock_extract_dir.rglob.return_value = iter([non_matching, correct_binary])

        manager.cache_dir = MagicMock()
        manager.cache_dir.__truediv__ = MagicMock(return_value=mock_extract_dir)

        # Stub out all methods that run after the rglob loop
        mock_binary_path = MagicMock()
        manager.get_binary_path = MagicMock(return_value=mock_binary_path)
        manager.extract_archive = MagicMock()
        manager.make_executable = MagicMock()
        manager._update_install_metadata = MagicMock()
        manager._update_recent_file = MagicMock()
        manager.verify_installation = MagicMock(return_value=True)

        # Act
        manager._install_from_archive(Path("/fake/archive.zip"), "1.9.8")

        # Assert: safe_copy was called with the correct binary (not the .sig file)
        mock_safe_copy.assert_called_once()
        first_arg = mock_safe_copy.call_args[0][0]
        assert first_arg == correct_binary
```

- [ ] **Step 4: Run the new test in isolation**

```bash
uv run python -m pytest tests/managers/test_managers.py::TestTfBaseInstallFromArchiveMultiFile -xvs
```

Expected: PASS.

- [ ] **Step 5: Run coverage check**

```bash
uv run python -m pytest tests/managers/ --cov=src/wrknv/managers --cov-report=term-missing -q
```

Expected: 100% coverage for all `managers/` modules, including `managers/tf/base.py` with no missing lines.

- [ ] **Step 6: Run full test suite**

```bash
uv run python -m pytest tests/ -q 2>&1 | tail -10
```

Expected: All pass.

- [ ] **Step 7: Commit**

```bash
git add tests/managers/test_managers.py
git commit -m "test: cover rglob multi-file branch in managers/tf/base.py"
```

---

### Task 7: Final verification

**Files:** None modified.

- [ ] **Step 1: Verify zero stale references**

```bash
grep -r "wenv\.managers\|wenv/managers" src/ tests/ CONTRIBUTING.md CLAUDE.md pyproject.toml
```

Expected: No output.

- [ ] **Step 2: Full test suite passes**

```bash
uv run python -m pytest tests/ -q 2>&1 | tail -10
```

Expected: All pass, no failures.

- [ ] **Step 3: 100% coverage on managers/**

```bash
uv run python -m pytest tests/managers/ --cov=src/wrknv/managers --cov-report=term-missing -q
```

Expected: 100% coverage, no missing lines.

- [ ] **Step 4: Ruff clean**

```bash
uv run ruff check src tests
```

Expected: No issues.
