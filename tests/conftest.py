#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Pytest configuration and shared fixtures."""

from __future__ import annotations

import sys

from provide.testkit import reset_foundation_setup_for_testing as _reset_foundation
import pytest

# Initialize Foundation at conftest import time so that module-level loggers
# created during test collection are properly configured (not frozen as _nop).
# The Foundation initialization itself imports some provide.foundation modules
# before the logger is fully set up, leaving them with frozen BoundLoggerFilteringAtInfo
# (where log.debug = _nop). Patch those in-place so functions that reference
# their module's 'log' via __globals__ will use the proper lazy proxy.
import structlog as _structlog
import structlog._native as _sn  # private module; class naming convention tested against structlog>=21

_reset_foundation()

# Replace module-level frozen loggers (BoundLoggerFilteringAt* with _nop for debug) with
# lazy proxies that re-evaluate against the current structlog config on each call.
for _mod_name, _mod in list(sys.modules.items()):
    if _mod_name.startswith("provide.foundation") and hasattr(_mod, "log"):
        _logger = _mod.log
        if hasattr(_logger, "debug") and getattr(_logger.debug, "__name__", "") == "_nop":
            _mod.log = _structlog.get_logger(_mod_name)

# Some provide.foundation library code calls log.debug(key=value) without an event
# string. BoundLoggerFilteringAt* classes (used when log_cli_level=DEBUG or at INFO
# threshold) generate methods where event is required positionally. Patch all such
# classes to make event optional so these calls don't raise TypeError.


def _make_permissive(_orig_method):
    def _permissive(self, event="", *args, **kw):  # type: ignore[misc]
        return _orig_method(self, event, *args, **kw)

    return _permissive


for _cls_name in dir(_sn):
    if not _cls_name.startswith("BoundLoggerFilteringAt"):
        continue
    _cls = getattr(_sn, _cls_name)
    if not isinstance(_cls, type):
        continue
    for _level in ("debug", "info", "warning", "error", "critical", "trace", "exception"):
        _method = _cls.__dict__.get(_level)
        if _method is not None:
            setattr(_cls, _level, _make_permissive(_method))

del _reset_foundation, _structlog, _sn, _cls_name, _cls, _level, _method, _make_permissive

# Platform detection
IS_WINDOWS = sys.platform == "win32"
IS_UNIX = sys.platform in ("linux", "darwin")


def pytest_configure(config: pytest.Config) -> None:
    """Register custom markers."""
    config.addinivalue_line("markers", "unix_only: mark test to run only on Unix systems")
    config.addinivalue_line("markers", "windows_only: mark test to run only on Windows")


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """Skip tests based on platform markers."""
    skip_windows = pytest.mark.skip(reason="Test requires Unix (uses bash syntax or Unix paths)")
    skip_unix = pytest.mark.skip(reason="Test requires Windows")

    for item in items:
        if "unix_only" in item.keywords and IS_WINDOWS:
            item.add_marker(skip_windows)
        if "windows_only" in item.keywords and IS_UNIX:
            item.add_marker(skip_unix)


# Import all test utilities to make them available
from tests.utils.fixtures import (
    create_mock_builder,
    create_mock_exec,
    create_mock_lifecycle,
    create_mock_logs,
    create_mock_manager,
    create_mock_runtime,
    create_mock_storage,
    create_mock_volumes,
    create_test_config,
)


# Make fixtures available as pytest fixtures
@pytest.fixture
def test_config():
    """Create a test configuration."""
    return create_test_config()


@pytest.fixture
def mock_runtime():
    """Create a mock DockerRuntime."""
    return create_mock_runtime()


@pytest.fixture
def mock_manager():
    """Create a ContainerManager with mocked dependencies."""
    return create_mock_manager()


@pytest.fixture
def mock_lifecycle():
    """Create a mock ContainerLifecycle."""
    return create_mock_lifecycle()


@pytest.fixture
def mock_exec():
    """Create a mock ContainerExec."""
    return create_mock_exec()


@pytest.fixture
def mock_logs():
    """Create a mock ContainerLogs."""
    return create_mock_logs()


@pytest.fixture
def mock_builder():
    """Create a mock ContainerBuilder."""
    return create_mock_builder()


@pytest.fixture
def mock_volumes():
    """Create a mock VolumeManager."""
    return create_mock_volumes()


@pytest.fixture
def mock_storage():
    """Create a mock ContainerStorage."""
    return create_mock_storage()


# 🧰🌍🔚
