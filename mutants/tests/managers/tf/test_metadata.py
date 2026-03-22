#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for managers.tf.metadata module."""

from __future__ import annotations

import json

from provide.testkit import FoundationTestCase

from wrknv.managers.tf.metadata import TfMetadataManager


class TestTfMetadataManagerInit(FoundationTestCase):
    """Tests for TfMetadataManager.__init__."""

    def test_init_stores_fields(self) -> None:
        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "tofu")
        assert mgr.install_path == tmp
        assert mgr.tool_name == "tofu"
        assert mgr.metadata_file == tmp / "metadata.json"

    def test_init_empty_metadata(self) -> None:
        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "tofu")
        assert mgr.metadata == {}


class TestLoadMetadata(FoundationTestCase):
    """Tests for load_metadata."""

    def test_empty_when_no_file(self) -> None:
        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.load_metadata()
        assert mgr.metadata == {}

    def test_loads_existing_file(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "metadata.json").write_text('{"key": "val"}')
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.load_metadata()
        assert mgr.metadata["key"] == "val"

    def test_handles_invalid_json(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "metadata.json").write_text("not json{{{")
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.load_metadata()
        assert mgr.metadata == {}

    def test_migrates_active_tofu_key(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "metadata.json").write_text('{"active_tofu": "1.5.0"}')
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.load_metadata()
        assert "active_tofu" not in mgr.metadata
        assert mgr.metadata["workenv"]["default"]["opentofu_version"] == "1.5.0"

    def test_migrates_active_terraform_key(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "metadata.json").write_text('{"active_terraform": "1.7.0"}')
        mgr = TfMetadataManager(tmp, "terraform")
        mgr.load_metadata()
        assert "active_terraform" not in mgr.metadata
        assert mgr.metadata["workenv"]["default"]["terraform_version"] == "1.7.0"


class TestSaveMetadata(FoundationTestCase):
    """Tests for save_metadata."""

    def test_writes_json_file(self) -> None:
        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.metadata = {"version": "1.0"}
        mgr.save_metadata()
        data = json.loads((tmp / "metadata.json").read_text())
        assert data["version"] == "1.0"


class TestUpdateRecentFile(FoundationTestCase):
    """Tests for update_recent_file."""

    def test_creates_recent_file(self) -> None:
        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.update_recent_file(["1.5.0", "1.4.0"])
        recent = json.loads((tmp / "RECENT").read_text())
        assert "opentofu" in recent

    def test_tofu_uses_opentofu_key(self) -> None:
        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.update_recent_file(["1.5.0"])
        recent = json.loads((tmp / "RECENT").read_text())
        assert recent["opentofu"] == ["1.5.0"]

    def test_terraform_uses_terraform_key(self) -> None:
        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "terraform")
        mgr.update_recent_file(["1.7.0"])
        recent = json.loads((tmp / "RECENT").read_text())
        assert recent["terraform"] == ["1.7.0"]

    def test_keeps_only_five_versions(self) -> None:
        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.update_recent_file(["1.5.0", "1.4.0", "1.3.0", "1.2.0", "1.1.0", "1.0.0"])
        recent = json.loads((tmp / "RECENT").read_text())
        assert len(recent["opentofu"]) == 5

    def test_removes_tool_when_no_versions(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "RECENT").write_text('{"opentofu": ["1.5.0"]}')
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.update_recent_file([])
        recent = json.loads((tmp / "RECENT").read_text())
        assert "opentofu" not in recent

    def test_reads_existing_recent_file(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "RECENT").write_text('{"terraform": ["1.7.0"]}')
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.update_recent_file(["1.5.0"])
        recent = json.loads((tmp / "RECENT").read_text())
        assert "terraform" in recent
        assert "opentofu" in recent

    def test_handles_corrupt_recent_file(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "RECENT").write_text("not json{")
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.update_recent_file(["1.5.0"])
        recent = json.loads((tmp / "RECENT").read_text())
        assert "opentofu" in recent


class TestUpdateRecentFileWithActive(FoundationTestCase):
    """Tests for update_recent_file_with_active."""

    def test_active_version_is_first(self) -> None:
        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.update_recent_file_with_active("1.5.0", ["1.5.0", "1.4.0", "1.3.0"])
        recent = json.loads((tmp / "RECENT").read_text())
        assert recent["opentofu"][0] == "1.5.0"

    def test_other_versions_follow(self) -> None:
        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.update_recent_file_with_active("1.5.0", ["1.5.0", "1.4.0", "1.3.0"])
        recent = json.loads((tmp / "RECENT").read_text())
        assert "1.4.0" in recent["opentofu"]
        assert "1.3.0" in recent["opentofu"]

    def test_no_duplicate_active_version(self) -> None:
        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.update_recent_file_with_active("1.5.0", ["1.5.0", "1.4.0"])
        recent = json.loads((tmp / "RECENT").read_text())
        assert recent["opentofu"].count("1.5.0") == 1

    def test_caps_at_five_versions(self) -> None:
        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "tofu")
        versions = ["1.5.0", "1.4.0", "1.3.0", "1.2.0", "1.1.0", "1.0.0"]
        mgr.update_recent_file_with_active("1.5.0", versions)
        recent = json.loads((tmp / "RECENT").read_text())
        assert len(recent["opentofu"]) == 5

    def test_corrupt_recent_file_is_reset(self) -> None:
        """Lines 112-116: corrupt RECENT file in update_recent_file_with_active is silently reset."""
        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "tofu")
        (tmp / "RECENT").write_text("{ not json }")
        mgr.update_recent_file_with_active("1.6.0", ["1.5.0"])
        recent = json.loads((tmp / "RECENT").read_text())
        assert recent["opentofu"][0] == "1.6.0"

    def test_write_recent_with_active_exception_is_silenced(self) -> None:
        """Line 133: write exception in update_recent_file_with_active is silently caught."""
        import pathlib
        from unittest.mock import patch

        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "tofu")
        with patch.object(pathlib.Path, "open", side_effect=OSError("disk full")):
            mgr.update_recent_file_with_active("1.6.0", [])  # Should not raise

    def test_write_recent_exception_is_silenced(self) -> None:
        """Line 102: write exception in update_recent_file is silently caught."""
        import pathlib
        from unittest.mock import patch

        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "tofu")
        with patch.object(pathlib.Path, "open", side_effect=OSError("disk full")):
            mgr.update_recent_file(["1.6.0"])  # Should not raise

    def test_save_metadata_exception_is_silenced(self) -> None:
        """Line 72: write exception in save_metadata is silently caught."""
        import pathlib
        from unittest.mock import patch

        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.metadata = {"key": "value"}
        with patch.object(pathlib.Path, "open", side_effect=OSError("disk full")):
            mgr.save_metadata()  # Should not raise


class TestMigrateMetadataFormat(FoundationTestCase):
    """Tests for _migrate_metadata_format branches."""

    def test_migrates_active_tofu_with_no_workenv_key(self) -> None:
        """Lines 52->54: workenv key is created when missing."""
        tmp = self.create_temp_dir()
        metadata_file = tmp / "metadata.json"
        metadata_file.write_text(json.dumps({"active_tofu": "1.6.0"}))
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.load_metadata()
        assert mgr.metadata.get("workenv", {}).get("default", {}).get("opentofu_version") == "1.6.0"
        assert "active_tofu" not in mgr.metadata

    def test_migrates_active_tofu_with_existing_workenv_no_default(self) -> None:
        """Line 54 True: 'default' key created when workenv exists but default doesn't."""
        tmp = self.create_temp_dir()
        metadata_file = tmp / "metadata.json"
        metadata_file.write_text(json.dumps({"active_tofu": "1.6.0", "workenv": {}}))
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.load_metadata()
        assert mgr.metadata["workenv"]["default"]["opentofu_version"] == "1.6.0"

    def test_migrates_active_tofu_with_existing_workenv_and_default(self) -> None:
        """Line 54->59: skips creating 'default' when workenv and default both exist."""
        tmp = self.create_temp_dir()
        metadata_file = tmp / "metadata.json"
        existing = {"active_tofu": "1.6.0", "workenv": {"default": {"other": "val"}}}
        metadata_file.write_text(json.dumps(existing))
        mgr = TfMetadataManager(tmp, "tofu")
        mgr.load_metadata()
        assert mgr.metadata["workenv"]["default"]["opentofu_version"] == "1.6.0"


class TestUpdateRecentFileBranches(FoundationTestCase):
    """Cover remaining branches in update_recent_file."""

    def test_empty_versions_and_key_not_in_recent(self) -> None:
        """Line 94->99: installed_versions empty and tool_key absent → skip elif body."""
        tmp = self.create_temp_dir()
        mgr = TfMetadataManager(tmp, "tofu")
        # No RECENT file, no versions → key won't be in recent_data, elif is False
        mgr.update_recent_file([])  # should not raise and should write an empty dict


# 🧰🌍🔚
