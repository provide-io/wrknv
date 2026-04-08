#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for memray.scaffold module."""

from __future__ import annotations

from provide.testkit import FoundationTestCase

from wrknv.memray.scaffold import (
    CONFTEST_TEMPLATE,
    EXAMPLE_STRESS_SCRIPT_TEMPLATE,
    EXAMPLE_TEST_TEMPLATE,
    GITIGNORE_ENTRY,
    INIT_TEMPLATE,
    PYPROJECT_MARKER_SNIPPET,
    WRKNV_TASKS_SNIPPET,
    scaffold_memray,
)


class TestScaffoldConstants(FoundationTestCase):
    """Tests for module-level constants."""

    def test_conftest_template_is_string(self) -> None:
        assert isinstance(CONFTEST_TEMPLATE, str)
        assert "wrknv.memray.fixtures" in CONFTEST_TEMPLATE

    def test_example_test_template_is_string(self) -> None:
        assert isinstance(EXAMPLE_TEST_TEMPLATE, str)
        assert "run_memray_stress" in EXAMPLE_TEST_TEMPLATE

    def test_example_stress_script_has_warmup_and_run_stress(self) -> None:
        assert "def warmup" in EXAMPLE_STRESS_SCRIPT_TEMPLATE
        assert "def run_stress" in EXAMPLE_STRESS_SCRIPT_TEMPLATE

    def test_init_template_is_string(self) -> None:
        assert isinstance(INIT_TEMPLATE, str)

    def test_wrknv_tasks_snippet_has_tasks_section(self) -> None:
        assert "[tasks.memray]" in WRKNV_TASKS_SNIPPET

    def test_pyproject_marker_snippet_has_memray(self) -> None:
        assert "memray" in PYPROJECT_MARKER_SNIPPET

    def test_gitignore_entry(self) -> None:
        assert "memray-output" in GITIGNORE_ENTRY


class TestScaffoldMemray(FoundationTestCase):
    """Tests for scaffold_memray function."""

    def test_creates_test_directory(self) -> None:
        tmp = self.create_temp_dir()
        actions = scaffold_memray(tmp)
        assert (tmp / "tests" / "memray").is_dir()
        assert len(actions) > 0

    def test_creates_init_py(self) -> None:
        tmp = self.create_temp_dir()
        scaffold_memray(tmp)
        assert (tmp / "tests" / "memray" / "__init__.py").exists()

    def test_creates_conftest(self) -> None:
        tmp = self.create_temp_dir()
        scaffold_memray(tmp)
        assert (tmp / "tests" / "memray" / "conftest.py").exists()

    def test_creates_baselines_json(self) -> None:
        tmp = self.create_temp_dir()
        scaffold_memray(tmp)
        baselines = tmp / "tests" / "memray" / "baselines.json"
        assert baselines.exists()
        assert baselines.read_text() == "{}\n"

    def test_creates_example_test(self) -> None:
        tmp = self.create_temp_dir()
        scaffold_memray(tmp)
        assert (tmp / "tests" / "memray" / "test_example_stress.py").exists()

    def test_creates_scripts_directory(self) -> None:
        tmp = self.create_temp_dir()
        scaffold_memray(tmp)
        assert (tmp / "scripts").is_dir()

    def test_creates_example_stress_script(self) -> None:
        tmp = self.create_temp_dir()
        scaffold_memray(tmp)
        assert (tmp / "scripts" / "memray_example_stress.py").exists()

    def test_creates_gitignore_when_missing(self) -> None:
        tmp = self.create_temp_dir()
        scaffold_memray(tmp)
        gitignore = tmp / ".gitignore"
        assert gitignore.exists()
        assert GITIGNORE_ENTRY in gitignore.read_text()

    def test_appends_to_existing_gitignore(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / ".gitignore").write_text("node_modules/\n")
        scaffold_memray(tmp)
        content = (tmp / ".gitignore").read_text()
        assert GITIGNORE_ENTRY in content
        assert "node_modules/" in content

    def test_skips_gitignore_entry_if_already_present(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / ".gitignore").write_text(f"{GITIGNORE_ENTRY}\n")
        actions = scaffold_memray(tmp)
        assert not any("Added" in a and "gitignore" in a.lower() for a in actions)

    def test_adds_memray_tasks_to_wrknv_toml(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "wrknv.toml").write_text('[project]\nname = "test"\n')
        scaffold_memray(tmp)
        content = (tmp / "wrknv.toml").read_text()
        assert "[tasks.memray]" in content

    def test_skips_wrknv_toml_when_missing(self) -> None:
        tmp = self.create_temp_dir()
        actions = scaffold_memray(tmp)
        assert any("Skipped wrknv.toml (file not found)" in a for a in actions)

    def test_skips_tasks_if_already_exist(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "wrknv.toml").write_text('[tasks.memray]\n_default = "pytest"\n')
        actions = scaffold_memray(tmp)
        assert any("already exist" in a for a in actions)

    def test_notes_missing_marker_in_pyproject(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_text("[tool.pytest.ini_options]\n")
        actions = scaffold_memray(tmp)
        assert any("memray marker" in a.lower() or "NOTE" in a for a in actions)

    def test_skips_marker_note_when_memray_already_in_pyproject(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_text('"memray: memory profiling"\n')
        actions = scaffold_memray(tmp)
        assert not any("Add memray marker" in a for a in actions)

    def test_skips_existing_conftest(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "tests" / "memray").mkdir(parents=True)
        existing_conftest = tmp / "tests" / "memray" / "conftest.py"
        existing_conftest.write_text("# custom conftest")
        actions = scaffold_memray(tmp)
        assert any("Skipped" in a and "conftest" in a for a in actions)
        # Content unchanged
        assert existing_conftest.read_text() == "# custom conftest"

    def test_returns_list_of_strings(self) -> None:
        tmp = self.create_temp_dir()
        actions = scaffold_memray(tmp)
        assert isinstance(actions, list)
        assert all(isinstance(a, str) for a in actions)

    def test_skips_existing_files(self) -> None:
        """Lines 141->146, 155->160, 161->166, 169->174: already-existing files are skipped."""
        tmp = self.create_temp_dir()
        # Create all files that scaffold would create
        memray_test_dir = tmp / "tests" / "memray"
        memray_test_dir.mkdir(parents=True, exist_ok=True)
        (memray_test_dir / "__init__.py").write_text("# existing")
        (memray_test_dir / "conftest.py").write_text("# existing")
        (memray_test_dir / "baselines.json").write_text("{}")
        (memray_test_dir / "test_example_stress.py").write_text("# existing")
        scripts_dir = tmp / "scripts"
        scripts_dir.mkdir(exist_ok=True)
        (scripts_dir / "memray_example_stress.py").write_text("# existing")

        actions = scaffold_memray(tmp)
        # conftest.py already exists → "Skipped" message expected
        assert any("Skipped" in a for a in actions)
        # init and other files should not be re-created
        assert (memray_test_dir / "__init__.py").read_text() == "# existing"


# 🧰🌍🔚
