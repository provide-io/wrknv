#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for managers.tf.utils module."""

from __future__ import annotations

from provide.testkit import FoundationTestCase

from wrknv.managers.tf.utils import calculate_file_hash, get_tool_version_key, version_sort_key


class TestCalculateFileHash(FoundationTestCase):
    """Tests for calculate_file_hash."""

    def test_sha256_default(self) -> None:
        tmp = self.create_temp_dir()
        f = tmp / "test.txt"
        f.write_text("hello")
        result = calculate_file_hash(f)
        assert len(result) == 64  # SHA256 hex digest length

    def test_sha256_explicit(self) -> None:
        tmp = self.create_temp_dir()
        f = tmp / "test.txt"
        f.write_text("hello")
        result = calculate_file_hash(f, algorithm="sha256")
        assert len(result) == 64

    def test_md5(self) -> None:
        tmp = self.create_temp_dir()
        f = tmp / "test.txt"
        f.write_text("hello")
        result = calculate_file_hash(f, algorithm="md5")
        assert len(result) == 32

    def test_same_content_same_hash(self) -> None:
        tmp = self.create_temp_dir()
        f1 = tmp / "a.txt"
        f2 = tmp / "b.txt"
        f1.write_bytes(b"same content")
        f2.write_bytes(b"same content")
        assert calculate_file_hash(f1) == calculate_file_hash(f2)

    def test_different_content_different_hash(self) -> None:
        tmp = self.create_temp_dir()
        f1 = tmp / "a.txt"
        f2 = tmp / "b.txt"
        f1.write_bytes(b"content A")
        f2.write_bytes(b"content B")
        assert calculate_file_hash(f1) != calculate_file_hash(f2)


class TestVersionSortKey(FoundationTestCase):
    """Tests for version_sort_key."""

    def test_standard_semver(self) -> None:
        key = version_sort_key("1.2.3")
        assert str(key) == "1.2.3"

    def test_two_part_version(self) -> None:
        key = version_sort_key("1.0")
        # Should pad to "1.0.0"
        assert key.major == 1
        assert key.minor == 0

    def test_one_part_version(self) -> None:
        key = version_sort_key("2")
        assert key.major == 2

    def test_invalid_version_returns_fallback(self) -> None:
        key = version_sort_key("not-a-version")
        assert str(key) == "0.0.0"

    def test_versions_sortable(self) -> None:
        versions = ["1.0.0", "2.0.0", "1.5.0"]
        keys = [(version_sort_key(v), v) for v in versions]
        sorted_keys = sorted(keys, reverse=True)
        assert [v for _, v in sorted_keys] == ["2.0.0", "1.5.0", "1.0.0"]


class TestGetToolVersionKey(FoundationTestCase):
    """Tests for get_tool_version_key."""

    def test_tofu_returns_opentofu_version(self) -> None:
        assert get_tool_version_key("tofu") == "opentofu_version"

    def test_terraform_returns_terraform_version(self) -> None:
        assert get_tool_version_key("terraform") == "terraform_version"

    def test_ibmtf_returns_ibmtf_version(self) -> None:
        assert get_tool_version_key("ibmtf") == "ibmtf_version"

    def test_other_tool_returns_tool_name_version(self) -> None:
        assert get_tool_version_key("mytool") == "mytool_version"


# 🧰🌍🔚
