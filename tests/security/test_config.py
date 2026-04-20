#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for security.config module."""

from __future__ import annotations

from provide.testkit import FoundationTestCase

from wrknv.security.config import SecurityConfig, load_security_config


class TestSecurityConfig(FoundationTestCase):
    """Tests for SecurityConfig attrs class."""

    def test_default_description(self) -> None:
        cfg = SecurityConfig()
        assert cfg.description == "Allowlisted paths for secret scanning"

    def test_default_allowed_paths_empty(self) -> None:
        cfg = SecurityConfig()
        assert cfg.allowed_paths == []

    def test_custom_description(self) -> None:
        cfg = SecurityConfig(description="My project")
        assert cfg.description == "My project"

    def test_custom_allowed_paths(self) -> None:
        cfg = SecurityConfig(allowed_paths=["path/to/secret"])
        assert cfg.allowed_paths == ["path/to/secret"]


class TestLoadSecurityConfig(FoundationTestCase):
    """Tests for load_security_config."""

    def test_returns_none_when_no_config_files(self) -> None:
        tmp = self.create_temp_dir()
        result = load_security_config(project_dir=tmp)
        assert result is None

    def test_loads_from_pyproject_tool_security(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_bytes(
            b'[tool.security]\ndescription = "My security"\nallowed_paths = ["secrets/"]\n'
        )
        result = load_security_config(project_dir=tmp)
        assert result is not None
        assert result.description == "My security"
        assert result.allowed_paths == ["secrets/"]

    def test_pyproject_without_tool_security_returns_none(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_bytes(b"[tool.other]\nfoo = 1\n")
        result = load_security_config(project_dir=tmp)
        assert result is None

    def test_loads_from_wrknv_toml(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "wrknv.toml").write_bytes(
            b'[security]\ndescription = "wrknv security"\nallowed_paths = ["creds/"]\n'
        )
        result = load_security_config(project_dir=tmp)
        assert result is not None
        assert result.description == "wrknv security"
        assert result.allowed_paths == ["creds/"]

    def test_loads_from_hidden_wrknv_toml(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / ".wrknv.toml").write_bytes(b'[security]\nallowed_paths = ["hidden/"]\n')
        result = load_security_config(project_dir=tmp)
        assert result is not None
        assert result.allowed_paths == ["hidden/"]

    def test_pyproject_takes_priority_over_wrknv(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_bytes(b'[tool.security]\ndescription = "from pyproject"\n')
        (tmp / "wrknv.toml").write_bytes(b'[security]\ndescription = "from wrknv"\n')
        result = load_security_config(project_dir=tmp)
        assert result is not None
        assert result.description == "from pyproject"

    def test_wrknv_takes_priority_over_hidden_wrknv(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "wrknv.toml").write_bytes(b'[security]\ndescription = "from wrknv"\n')
        (tmp / ".wrknv.toml").write_bytes(b'[security]\ndescription = "from hidden"\n')
        result = load_security_config(project_dir=tmp)
        assert result is not None
        assert result.description == "from wrknv"

    def test_explicit_pyproject_path(self) -> None:
        tmp = self.create_temp_dir()
        custom = tmp / "custom.toml"
        custom.write_bytes(b'[tool.security]\nallowed_paths = ["x/"]\n')
        result = load_security_config(pyproject_path=custom)
        assert result is not None
        assert result.allowed_paths == ["x/"]

    def test_explicit_wrknv_path(self) -> None:
        tmp = self.create_temp_dir()
        custom = tmp / "custom_wrknv.toml"
        custom.write_bytes(b'[security]\nallowed_paths = ["y/"]\n')
        result = load_security_config(project_dir=tmp, wrknv_path=custom)
        assert result is not None
        assert result.allowed_paths == ["y/"]

    def test_returns_none_on_invalid_toml_in_pyproject(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_bytes(b"not valid toml {{{\n")
        result = load_security_config(project_dir=tmp)
        assert result is None

    def test_returns_none_on_invalid_toml_in_wrknv(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "wrknv.toml").write_bytes(b"not valid toml {{{\n")
        result = load_security_config(project_dir=tmp)
        assert result is None

    def test_uses_cwd_when_no_project_dir(self) -> None:
        # Just verify it doesn't error; cwd likely has no security config
        result = load_security_config()
        # May or may not return a config depending on the actual cwd
        assert result is None or isinstance(result, SecurityConfig)

    def test_default_allowed_paths_from_toml(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "pyproject.toml").write_bytes(b"[tool.security]\n")
        # empty security section returns None since security_data is empty/falsy
        result = load_security_config(project_dir=tmp)
        assert result is None

    def test_wrknv_without_security_section_returns_none(self) -> None:
        tmp = self.create_temp_dir()
        (tmp / "wrknv.toml").write_bytes(b'[tasks]\nfoo = "bar"\n')
        result = load_security_config(project_dir=tmp)
        assert result is None


# 🧰🌍🔚
