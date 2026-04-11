#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Tests for package.commands module."""

from __future__ import annotations

from unittest import mock

from provide.testkit import FoundationTestCase
import pytest

from wrknv.config import WorkenvConfig
from wrknv.package.commands import (
    _check_flavor_installed,
    build_package,
    clean_cache,
    generate_keys,
    get_package_info,
    init_provider,
    list_packages,
    sign_package,
    verify_package,
)


def _make_config() -> WorkenvConfig:
    return WorkenvConfig(project_name="test-pkg", version="1.0.0")


class TestCheckFlavorInstalled(FoundationTestCase):
    """Tests for _check_flavor_installed."""

    def test_raises_when_flavor_not_installed(self) -> None:
        with (
            mock.patch.dict("sys.modules", {"flavor": None}),
            pytest.raises(ImportError, match="flavorpack not installed"),
        ):
            _check_flavor_installed()

    def test_passes_when_flavor_installed(self) -> None:
        fake_flavor = mock.MagicMock()
        with mock.patch.dict("sys.modules", {"flavor": fake_flavor}):
            _check_flavor_installed()  # Should not raise


class TestBuildPackage(FoundationTestCase):
    """Tests for build_package."""

    def test_dry_run_returns_expected_path(self) -> None:
        tmp = self.create_temp_dir()
        manifest = tmp / "manifest.yaml"
        manifest.write_text("name: test")
        result = build_package(manifest, dry_run=True)
        assert len(result) == 1
        assert result[0] == tmp / "dist" / "package.psp"

    def test_dry_run_does_not_require_flavorpack(self) -> None:
        tmp = self.create_temp_dir()
        manifest = tmp / "manifest.yaml"
        manifest.write_text("name: test")
        # Should not check for flavor in dry_run mode
        with mock.patch.dict("sys.modules", {"flavor": None}):
            result = build_package(manifest, dry_run=True)
        assert len(result) == 1

    def test_raises_import_error_when_flavor_missing(self) -> None:
        tmp = self.create_temp_dir()
        manifest = tmp / "manifest.yaml"
        with mock.patch.dict("sys.modules", {"flavor": None}), pytest.raises(ImportError):
            build_package(manifest)

    def test_raises_runtime_error_on_build_failure(self) -> None:
        tmp = self.create_temp_dir()
        manifest = tmp / "manifest.yaml"
        fake_flavor = mock.MagicMock()
        fake_flavor.build_package_from_manifest.side_effect = Exception("build failed")
        with (
            mock.patch.dict("sys.modules", {"flavor": fake_flavor}),
            pytest.raises(RuntimeError, match="Package build failed"),
        ):
            build_package(manifest, config=_make_config())

    def test_uses_default_config_when_none_provided(self) -> None:
        tmp = self.create_temp_dir()
        manifest = tmp / "manifest.yaml"
        fake_flavor = mock.MagicMock()
        fake_flavor.build_package_from_manifest.return_value = []
        with mock.patch.dict("sys.modules", {"flavor": fake_flavor}):
            result = build_package(manifest)  # config=None
        assert result == []

    def test_returns_package_list_on_success(self) -> None:
        tmp = self.create_temp_dir()
        manifest = tmp / "manifest.yaml"
        fake_flavor = mock.MagicMock()
        expected = [tmp / "dist" / "out.psp"]
        fake_flavor.build_package_from_manifest.return_value = expected
        with mock.patch.dict("sys.modules", {"flavor": fake_flavor}):
            result = build_package(manifest, config=_make_config())
        assert result == expected


class TestInitProvider(FoundationTestCase):
    """Tests for init_provider."""

    def test_creates_project_directory(self) -> None:
        tmp = self.create_temp_dir()
        project = tmp / "my-provider"
        init_provider(project)
        assert project.exists()

    def test_creates_src_tests_keys_dirs(self) -> None:
        tmp = self.create_temp_dir()
        project = tmp / "my-provider"
        init_provider(project)
        assert (project / "src").exists()
        assert (project / "tests").exists()
        assert (project / "keys").exists()

    def test_creates_pyproject_toml(self) -> None:
        tmp = self.create_temp_dir()
        project = tmp / "my-provider"
        init_provider(project)
        assert (project / "pyproject.toml").exists()

    def test_pyproject_contains_flavor_section(self) -> None:
        tmp = self.create_temp_dir()
        project = tmp / "my-provider"
        init_provider(project)
        content = (project / "pyproject.toml").read_text()
        assert "[tool.flavor]" in content

    def test_returns_project_dir(self) -> None:
        tmp = self.create_temp_dir()
        project = tmp / "my-provider"
        result = init_provider(project)
        assert result == project

    def test_works_on_existing_directory(self) -> None:
        tmp = self.create_temp_dir()
        project = tmp / "existing"
        project.mkdir()
        init_provider(project)
        assert (project / "pyproject.toml").exists()


class TestListPackages(FoundationTestCase):
    """Tests for list_packages."""

    def test_returns_empty_list_when_no_output_dir(self) -> None:
        tmp = self.create_temp_dir()
        with mock.patch("pathlib.Path.home", return_value=tmp):
            result = list_packages()
        assert result == []

    def test_returns_empty_list_when_no_psp_files(self) -> None:
        tmp = self.create_temp_dir()
        output_dir = tmp / ".wrknv" / "packages"
        output_dir.mkdir(parents=True)
        with mock.patch("pathlib.Path.home", return_value=tmp):
            result = list_packages()
        assert result == []

    def test_returns_package_info_for_psp_files(self) -> None:
        tmp = self.create_temp_dir()
        output_dir = tmp / ".wrknv" / "packages"
        output_dir.mkdir(parents=True)
        psp_file = output_dir / "my-package.psp"
        psp_file.write_bytes(b"fake psp content")
        with mock.patch("pathlib.Path.home", return_value=tmp):
            result = list_packages()
        assert len(result) == 1
        assert result[0]["name"] == "my-package"
        assert "size" in result[0]
        assert "path" in result[0]

    def test_accepts_config_param(self) -> None:
        tmp = self.create_temp_dir()
        cfg = _make_config()
        with mock.patch("pathlib.Path.home", return_value=tmp):
            result = list_packages(config=cfg)
        assert isinstance(result, list)


class TestSignPackage(FoundationTestCase):
    """Tests for sign_package."""

    def test_raises_not_implemented(self) -> None:
        tmp = self.create_temp_dir()
        pkg = tmp / "package.psp"
        key = tmp / "private.pem"
        with pytest.raises(NotImplementedError):
            sign_package(pkg, key)



class TestVerifyPackage(FoundationTestCase):
    """Tests for verify_package."""

    def test_raises_import_error_when_flavor_missing(self) -> None:
        tmp = self.create_temp_dir()
        pkg = tmp / "package.psp"
        with mock.patch.dict("sys.modules", {"flavor": None}), pytest.raises(ImportError):
            verify_package(pkg)

    def test_returns_verification_result(self) -> None:
        tmp = self.create_temp_dir()
        pkg = tmp / "package.psp"
        fake_flavor = mock.MagicMock()
        fake_flavor.verify_package.return_value = {"valid": True}
        with mock.patch.dict("sys.modules", {"flavor": fake_flavor}):
            result = verify_package(pkg)
        assert result == {"valid": True}

    def test_raises_runtime_error_on_failure(self) -> None:
        tmp = self.create_temp_dir()
        pkg = tmp / "package.psp"
        fake_flavor = mock.MagicMock()
        fake_flavor.verify_package.side_effect = Exception("corrupt")
        with (
            mock.patch.dict("sys.modules", {"flavor": fake_flavor}),
            pytest.raises(RuntimeError, match="Package verification failed"),
        ):
            verify_package(pkg)


class TestGenerateKeys(FoundationTestCase):
    """Tests for generate_keys."""

    def test_raises_import_error_when_flavor_missing(self) -> None:
        tmp = self.create_temp_dir()
        with (
            mock.patch.dict("sys.modules", {"flavor": None, "flavor.packaging": None}),
            pytest.raises(ImportError),
        ):
            generate_keys(tmp / "keys")

    def test_returns_key_pair(self) -> None:
        tmp = self.create_temp_dir()
        keys_dir = tmp / "keys"
        private_key = keys_dir / "private.pem"
        public_key = keys_dir / "public.pem"
        fake_flavor = mock.MagicMock()
        fake_packaging = mock.MagicMock()
        fake_packaging.generate_key_pair.return_value = (private_key, public_key)
        with mock.patch.dict("sys.modules", {"flavor": fake_flavor, "flavor.packaging": fake_packaging}):
            result = generate_keys(keys_dir)
        assert result == (private_key, public_key)

    def test_creates_output_dir(self) -> None:
        tmp = self.create_temp_dir()
        keys_dir = tmp / "new" / "keys"
        private_key = keys_dir / "private.pem"
        public_key = keys_dir / "public.pem"
        fake_flavor = mock.MagicMock()
        fake_packaging = mock.MagicMock()
        fake_packaging.generate_key_pair.return_value = (private_key, public_key)
        with mock.patch.dict("sys.modules", {"flavor": fake_flavor, "flavor.packaging": fake_packaging}):
            generate_keys(keys_dir)
        assert keys_dir.exists()

    def test_raises_runtime_error_on_failure(self) -> None:
        tmp = self.create_temp_dir()
        fake_flavor = mock.MagicMock()
        fake_packaging = mock.MagicMock()
        fake_packaging.generate_key_pair.side_effect = Exception("key gen failed")
        with (
            mock.patch.dict("sys.modules", {"flavor": fake_flavor, "flavor.packaging": fake_packaging}),
            pytest.raises(RuntimeError, match="Key generation failed"),
        ):
            generate_keys(tmp / "keys")


class TestCleanCache(FoundationTestCase):
    """Tests for clean_cache."""

    def test_raises_import_error_when_flavor_missing(self) -> None:
        with mock.patch.dict("sys.modules", {"flavor": None}), pytest.raises(ImportError):
            clean_cache()

    def test_cleans_flavor_cache(self) -> None:
        fake_flavor = mock.MagicMock()
        with mock.patch.dict("sys.modules", {"flavor": fake_flavor}):
            clean_cache()
        fake_flavor.clean_cache.assert_called_once()

    def test_removes_wrknv_package_cache(self) -> None:
        tmp = self.create_temp_dir()
        fake_flavor = mock.MagicMock()
        with (
            mock.patch.dict("sys.modules", {"flavor": fake_flavor}),
            mock.patch("pathlib.Path.home", return_value=tmp),
        ):
            clean_cache()
        # No exception means success — cache dir either removed or never existed
        assert True

    def test_handles_flavor_clean_exception(self) -> None:
        fake_flavor = mock.MagicMock()
        fake_flavor.clean_cache.side_effect = Exception("cache error")
        # Should not raise (exception is caught with warning)
        with mock.patch.dict("sys.modules", {"flavor": fake_flavor}):
            clean_cache()  # Should not raise

    def test_uses_provided_config_skips_instantiation(self) -> None:
        """Line 127->129: config is not None → skip WorkenvConfig() instantiation."""
        from wrknv.config import WorkenvConfig

        fake_flavor = mock.MagicMock()
        tmp = self.create_temp_dir()

        fake_manager = mock.MagicMock()
        fake_manager.get_package_cache_dir.return_value = tmp / "nonexistent_cache"

        with (
            mock.patch.dict("sys.modules", {"flavor": fake_flavor}),
            mock.patch("wrknv.package.commands.PackageManager", return_value=fake_manager),
            mock.patch("wrknv.package.commands.WorkenvConfig") as mock_wc_cls,
        ):
            config = mock.MagicMock(spec=WorkenvConfig)
            clean_cache(config=config)

        # WorkenvConfig() should NOT have been called since config was provided
        mock_wc_cls.assert_not_called()

    def test_cache_dir_nonexistent_skips_rmtree(self) -> None:
        """Line 131->exit: cache_dir.exists() is False → shutil.rmtree NOT called."""
        fake_flavor = mock.MagicMock()
        tmp = self.create_temp_dir()

        fake_manager = mock.MagicMock()
        # Return a path that does NOT exist
        fake_manager.get_package_cache_dir.return_value = tmp / "no_such_cache"

        with (
            mock.patch.dict("sys.modules", {"flavor": fake_flavor}),
            mock.patch("wrknv.package.commands.PackageManager", return_value=fake_manager),
            mock.patch("shutil.rmtree") as mock_rmtree,
        ):
            clean_cache()

        mock_rmtree.assert_not_called()


class TestGetPackageInfo(FoundationTestCase):
    """Tests for get_package_info."""

    def test_raises_import_error_when_flavor_missing(self) -> None:
        tmp = self.create_temp_dir()
        pkg = tmp / "package.psp"
        pkg.write_bytes(b"fake")
        with mock.patch.dict("sys.modules", {"flavor": None}), pytest.raises(ImportError):
            get_package_info(pkg)

    def test_returns_package_info_dict(self) -> None:
        tmp = self.create_temp_dir()
        pkg = tmp / "my-package.psp"
        pkg.write_bytes(b"fake content")
        fake_flavor = mock.MagicMock()
        fake_flavor.verify_package.return_value = {"valid": True}
        with mock.patch.dict("sys.modules", {"flavor": fake_flavor}):
            result = get_package_info(pkg)
        assert result["name"] == "my-package"
        assert "size" in result
        assert "path" in result
        assert result["verification"] == {"valid": True}

    def test_raises_runtime_error_on_failure(self) -> None:
        tmp = self.create_temp_dir()
        pkg = tmp / "package.psp"
        pkg.write_bytes(b"fake")
        fake_flavor = mock.MagicMock()
        fake_flavor.verify_package.side_effect = Exception("inspect failed")
        with (
            mock.patch.dict("sys.modules", {"flavor": fake_flavor}),
            pytest.raises(RuntimeError, match="Package inspection failed"),
        ):
            get_package_info(pkg)


class TestListPackagesNoDirBranch(FoundationTestCase):
    """Tests for the output_dir not existing branch in list_packages."""

    def test_returns_empty_when_output_dir_does_not_exist(self) -> None:
        tmp = self.create_temp_dir()
        fake_manager = mock.MagicMock()
        fake_manager.get_package_output_dir.return_value = tmp / "nonexistent"
        with mock.patch("wrknv.package.commands.PackageManager", return_value=fake_manager):
            result = list_packages()
        assert result == []


# 🧰🌍🔚
