#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for managers.subrosa.base - uncovered branches."""

from __future__ import annotations

import pathlib
import sys
from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.managers.base import ToolManagerError
from wrknv.managers.subrosa.bao import BaoVariant


def _make_subrosa(tmp_dir: pathlib.Path) -> BaoVariant:
    """Create a BaoVariant with all paths redirected to tmp_dir."""
    cfg = mock.MagicMock(spec=WorkenvConfig)
    cfg.get_setting.side_effect = lambda key, default=None: default
    cfg.get_tool_version.return_value = None
    cfg.install_path = str(tmp_dir / "tools")

    with (
        mock.patch("wrknv.managers.subrosa.base.get_workenv_bin_dir", return_value=tmp_dir / "bin"),
        mock.patch.object(pathlib.Path, "mkdir"),
    ):
        mgr = BaoVariant(config=cfg)

    mgr.install_path = tmp_dir / "subrosa"
    mgr.install_path.mkdir(parents=True, exist_ok=True)
    mgr.metadata_file = mgr.install_path / "metadata.json"
    mgr.metadata = {}
    mgr.cache_dir = tmp_dir / "cache"
    mgr.cache_dir.mkdir(parents=True, exist_ok=True)
    mgr.workenv_bin_dir = tmp_dir / "bin"
    (tmp_dir / "bin").mkdir(parents=True, exist_ok=True)
    return mgr


class TestGetInstalledVersionsSortFallback(FoundationTestCase):
    """Cover lines 112-113: packaging.version import failure falls back to string sort."""

    def test_sort_fallback_when_packaging_unavailable(self) -> None:
        """Lines 112-113: packaging.version not available → string sort in get_installed_versions."""
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        # Create some fake installed version binaries
        for v in ["2.1.0", "2.0.0", "1.9.0"]:
            (mgr.install_path / f"bao_{v}").write_text(f"binary {v}")

        real_packaging = sys.modules.get("packaging.version")
        sys.modules["packaging.version"] = None  # type: ignore[assignment]
        try:
            versions = mgr.get_installed_versions()
        finally:
            if real_packaging is not None:
                sys.modules["packaging.version"] = real_packaging
            elif "packaging.version" in sys.modules:
                del sys.modules["packaging.version"]
        assert isinstance(versions, list)
        assert len(versions) == 3


class TestRegenerateEnvScriptException(FoundationTestCase):
    """Cover line 168: exception in _regenerate_env_script is silently caught."""

    def test_exception_is_silenced(self) -> None:
        """Line 168: _regenerate_env_script silently catches exceptions."""
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        with mock.patch(
            "wrknv.managers.subrosa.base.pathlib.Path.cwd", side_effect=OSError("no cwd")
        ):
            mgr._regenerate_env_script()  # Should not raise


class TestInstallFromArchiveVerificationFails(FoundationTestCase):
    """Cover line 257: verify_installation returns False → ToolManagerError raised."""

    def test_verification_failure_raises(self) -> None:
        """Line 257: ToolManagerError raised when verify_installation returns False."""
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        archive = tmp / "bao.tar.gz"
        archive.touch()

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            (dst / "bao").write_text("binary")

        with (
            mock.patch.object(mgr, "extract_archive", side_effect=fake_extract),
            mock.patch("wrknv.managers.subrosa.base.safe_copy"),
            mock.patch.object(mgr, "make_executable"),
            mock.patch.object(mgr, "verify_installation", return_value=False),
            mock.patch("wrknv.managers.subrosa.base.safe_rmtree"),
            pytest.raises(ToolManagerError, match="installation verification failed"),
        ):
            mgr._install_from_archive(archive, "2.1.0")


class TestInstallFromArchiveLoopSkipsNonMatching(FoundationTestCase):
    """Cover line 236->235: loop iterates past files not named variant_name or variant_name.exe."""

    def test_loop_skips_non_matching_files(self) -> None:
        """Line 236->235: files like 'bao-something' are skipped; 'bao' is found."""
        tmp = self.create_temp_dir()
        mgr = _make_subrosa(tmp)
        archive = tmp / "bao.tar.gz"
        archive.touch()

        def fake_extract(src: pathlib.Path, dst: pathlib.Path) -> None:
            (dst / "bao-unarchiver").write_text("helper")  # matches rglob but not exact name
            (dst / "bao").write_text("binary")             # the real binary

        with (
            mock.patch.object(mgr, "extract_archive", side_effect=fake_extract),
            mock.patch("wrknv.managers.subrosa.base.safe_copy"),
            mock.patch.object(mgr, "make_executable"),
            mock.patch.object(mgr, "verify_installation", return_value=True),
            mock.patch("wrknv.managers.subrosa.base.safe_rmtree"),
        ):
            mgr._install_from_archive(archive, "2.1.0")


# 🧰🌍🔚
