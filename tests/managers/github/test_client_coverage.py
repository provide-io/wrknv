#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Coverage tests for wrknv.managers.github.client — uncovered branches."""

from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, patch

from provide.testkit import FoundationTestCase

from wrknv.managers.github.client import GitHubReleasesClient


def _make_client(repo: str = "owner/repo") -> GitHubReleasesClient:
    """Create a GitHubReleasesClient with mocked dependencies."""
    with (
        patch("wrknv.managers.github.client.get_hub"),
        patch("wrknv.managers.github.client.UniversalClient"),
        patch("wrknv.managers.github.client.get_retry_policy"),
        patch("wrknv.managers.github.client.get_circuit_breaker"),
    ):
        return GitHubReleasesClient(repo)


class TestDownloadFileHeadRequestFailure(FoundationTestCase):
    """Line 213-214: except Exception: pass in _download_file HEAD request."""

    def test_head_request_exception_is_silently_ignored(self) -> None:
        """Line 213-214: self.client.head() raises → pass, download continues."""
        client = _make_client()
        tmp = self.create_temp_dir()
        destination = tmp / "output.zip"

        mock_http_client = AsyncMock()
        mock_http_client.head = AsyncMock(side_effect=Exception("connection refused"))
        mock_http_client.__aenter__ = AsyncMock(return_value=mock_http_client)
        mock_http_client.__aexit__ = AsyncMock(return_value=False)

        chunk = b"hello"

        async def fake_stream(*args: object, **kwargs: object):  # type: ignore[misc]
            yield chunk

        mock_http_client.stream = fake_stream

        client.client = mock_http_client

        # Should not raise — HEAD failure is silently caught
        asyncio.run(client._download_file("https://example.com/file.zip", destination))

        assert destination.exists()
        assert destination.read_bytes() == chunk


# 🧰🌍🔚
