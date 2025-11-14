#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2025 provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Pytest configuration and shared fixtures."""

from __future__ import annotations

import warnings

import pytest

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


def pytest_configure(config):
    """Configure pytest - suppress benchmark warnings when using xdist."""
    # Suppress pytest-benchmark warnings when xdist is active
    try:
        from pytest_benchmark.logger import PytestBenchmarkWarning

        warnings.filterwarnings("ignore", category=PytestBenchmarkWarning)
    except ImportError:
        pass


# Re-apply in sessionstart for worker processes
def pytest_sessionstart(session):
    """Session start hook - suppress warnings in each xdist worker."""
    try:
        from pytest_benchmark.logger import PytestBenchmarkWarning

        warnings.filterwarnings("ignore", category=PytestBenchmarkWarning)
    except ImportError:
        pass


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
