#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""GitHub Releases API Client
===========================
Client for interacting with GitHub Releases API using provide-foundation transport."""

from __future__ import annotations

from collections.abc import Callable
import pathlib
import re
from types import TracebackType
from typing import Literal

from provide.foundation.hub import get_hub
from provide.foundation.logger import get_logger
from provide.foundation.transport import UniversalClient

from wrknv.managers.github.types import Asset, Release, Tag
from wrknv.wenv.resilience import get_circuit_breaker, get_retry_policy

logger = get_logger(__name__)
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg is not None:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


class GitHubReleasesClient:
    """GitHub Releases API client using foundation transport."""

    def xǁGitHubReleasesClientǁ__init____mutmut_orig(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_1(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = None
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_2(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = None

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_3(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = None

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_4(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "XXAcceptXX": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_5(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_6(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "ACCEPT": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_7(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "XXapplication/vnd.github+jsonXX",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_8(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "APPLICATION/VND.GITHUB+JSON",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_9(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "XXX-GitHub-Api-VersionXX": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_10(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "x-github-api-version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_11(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GITHUB-API-VERSION": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_12(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "XX2022-11-28XX",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_13(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = None

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_14(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["XXAuthorizationXX"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_15(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_16(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["AUTHORIZATION"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_17(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = None
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_18(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = None

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_19(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=None, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_20(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=None)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_21(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_22(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, )

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_23(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = None
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_24(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy(None)
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_25(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("XXgithubXX")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_26(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("GITHUB")
        self.circuit_breaker = get_circuit_breaker("github")

    def xǁGitHubReleasesClientǁ__init____mutmut_27(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = None

    def xǁGitHubReleasesClientǁ__init____mutmut_28(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker(None)

    def xǁGitHubReleasesClientǁ__init____mutmut_29(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("XXgithubXX")

    def xǁGitHubReleasesClientǁ__init____mutmut_30(self, repo: str, token: str | None = None) -> None:
        """Initialize GitHub client.

        Args:
            repo: Repository in format 'owner/name'
            token: Optional GitHub token for authentication
        """
        self.repo = repo
        self.token = token

        # Build headers
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # Get hub and create client
        hub = get_hub()
        self.client = UniversalClient(hub=hub, default_headers=headers)

        # Get resilience components
        self.retry_policy = get_retry_policy("github")
        self.circuit_breaker = get_circuit_breaker("GITHUB")
    
    xǁGitHubReleasesClientǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitHubReleasesClientǁ__init____mutmut_1': xǁGitHubReleasesClientǁ__init____mutmut_1, 
        'xǁGitHubReleasesClientǁ__init____mutmut_2': xǁGitHubReleasesClientǁ__init____mutmut_2, 
        'xǁGitHubReleasesClientǁ__init____mutmut_3': xǁGitHubReleasesClientǁ__init____mutmut_3, 
        'xǁGitHubReleasesClientǁ__init____mutmut_4': xǁGitHubReleasesClientǁ__init____mutmut_4, 
        'xǁGitHubReleasesClientǁ__init____mutmut_5': xǁGitHubReleasesClientǁ__init____mutmut_5, 
        'xǁGitHubReleasesClientǁ__init____mutmut_6': xǁGitHubReleasesClientǁ__init____mutmut_6, 
        'xǁGitHubReleasesClientǁ__init____mutmut_7': xǁGitHubReleasesClientǁ__init____mutmut_7, 
        'xǁGitHubReleasesClientǁ__init____mutmut_8': xǁGitHubReleasesClientǁ__init____mutmut_8, 
        'xǁGitHubReleasesClientǁ__init____mutmut_9': xǁGitHubReleasesClientǁ__init____mutmut_9, 
        'xǁGitHubReleasesClientǁ__init____mutmut_10': xǁGitHubReleasesClientǁ__init____mutmut_10, 
        'xǁGitHubReleasesClientǁ__init____mutmut_11': xǁGitHubReleasesClientǁ__init____mutmut_11, 
        'xǁGitHubReleasesClientǁ__init____mutmut_12': xǁGitHubReleasesClientǁ__init____mutmut_12, 
        'xǁGitHubReleasesClientǁ__init____mutmut_13': xǁGitHubReleasesClientǁ__init____mutmut_13, 
        'xǁGitHubReleasesClientǁ__init____mutmut_14': xǁGitHubReleasesClientǁ__init____mutmut_14, 
        'xǁGitHubReleasesClientǁ__init____mutmut_15': xǁGitHubReleasesClientǁ__init____mutmut_15, 
        'xǁGitHubReleasesClientǁ__init____mutmut_16': xǁGitHubReleasesClientǁ__init____mutmut_16, 
        'xǁGitHubReleasesClientǁ__init____mutmut_17': xǁGitHubReleasesClientǁ__init____mutmut_17, 
        'xǁGitHubReleasesClientǁ__init____mutmut_18': xǁGitHubReleasesClientǁ__init____mutmut_18, 
        'xǁGitHubReleasesClientǁ__init____mutmut_19': xǁGitHubReleasesClientǁ__init____mutmut_19, 
        'xǁGitHubReleasesClientǁ__init____mutmut_20': xǁGitHubReleasesClientǁ__init____mutmut_20, 
        'xǁGitHubReleasesClientǁ__init____mutmut_21': xǁGitHubReleasesClientǁ__init____mutmut_21, 
        'xǁGitHubReleasesClientǁ__init____mutmut_22': xǁGitHubReleasesClientǁ__init____mutmut_22, 
        'xǁGitHubReleasesClientǁ__init____mutmut_23': xǁGitHubReleasesClientǁ__init____mutmut_23, 
        'xǁGitHubReleasesClientǁ__init____mutmut_24': xǁGitHubReleasesClientǁ__init____mutmut_24, 
        'xǁGitHubReleasesClientǁ__init____mutmut_25': xǁGitHubReleasesClientǁ__init____mutmut_25, 
        'xǁGitHubReleasesClientǁ__init____mutmut_26': xǁGitHubReleasesClientǁ__init____mutmut_26, 
        'xǁGitHubReleasesClientǁ__init____mutmut_27': xǁGitHubReleasesClientǁ__init____mutmut_27, 
        'xǁGitHubReleasesClientǁ__init____mutmut_28': xǁGitHubReleasesClientǁ__init____mutmut_28, 
        'xǁGitHubReleasesClientǁ__init____mutmut_29': xǁGitHubReleasesClientǁ__init____mutmut_29, 
        'xǁGitHubReleasesClientǁ__init____mutmut_30': xǁGitHubReleasesClientǁ__init____mutmut_30
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitHubReleasesClientǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁGitHubReleasesClientǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁGitHubReleasesClientǁ__init____mutmut_orig)
    xǁGitHubReleasesClientǁ__init____mutmut_orig.__name__ = 'xǁGitHubReleasesClientǁ__init__'

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_orig(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_1(self, include_prereleases: bool = True, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_2(self, include_prereleases: bool = False, per_page: int = 101) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_3(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = None
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_4(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = None

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_5(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"XXper_pageXX": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_6(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"PER_PAGE": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_7(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(None, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_8(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, None)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_9(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_10(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, )}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_11(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 101)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_12(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(None)

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_13(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = None
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_14(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(None, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_15(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=None)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_16(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_17(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, )
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_18(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = None

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_19(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = None

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_20(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(None) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_21(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_22(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = None

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_23(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(releases)} releases")
        return releases

    async def xǁGitHubReleasesClientǁlist_releases__mutmut_24(self, include_prereleases: bool = False, per_page: int = 100) -> list[Release]:
        """List all releases from repository.

        Args:
            include_prereleases: Include prerelease versions
            per_page: Number of releases per page (max 100)

        Returns:
            List of Release objects
        """
        url = f"https://api.github.com/repos/{self.repo}/releases"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching releases from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        releases = [Release.from_api(r) for r in data]

        # Filter prereleases if needed
        if not include_prereleases:
            releases = [r for r in releases if not r.prerelease]

        if logger.is_debug_enabled():
            logger.debug(None)
        return releases
    
    xǁGitHubReleasesClientǁlist_releases__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitHubReleasesClientǁlist_releases__mutmut_1': xǁGitHubReleasesClientǁlist_releases__mutmut_1, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_2': xǁGitHubReleasesClientǁlist_releases__mutmut_2, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_3': xǁGitHubReleasesClientǁlist_releases__mutmut_3, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_4': xǁGitHubReleasesClientǁlist_releases__mutmut_4, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_5': xǁGitHubReleasesClientǁlist_releases__mutmut_5, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_6': xǁGitHubReleasesClientǁlist_releases__mutmut_6, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_7': xǁGitHubReleasesClientǁlist_releases__mutmut_7, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_8': xǁGitHubReleasesClientǁlist_releases__mutmut_8, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_9': xǁGitHubReleasesClientǁlist_releases__mutmut_9, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_10': xǁGitHubReleasesClientǁlist_releases__mutmut_10, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_11': xǁGitHubReleasesClientǁlist_releases__mutmut_11, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_12': xǁGitHubReleasesClientǁlist_releases__mutmut_12, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_13': xǁGitHubReleasesClientǁlist_releases__mutmut_13, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_14': xǁGitHubReleasesClientǁlist_releases__mutmut_14, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_15': xǁGitHubReleasesClientǁlist_releases__mutmut_15, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_16': xǁGitHubReleasesClientǁlist_releases__mutmut_16, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_17': xǁGitHubReleasesClientǁlist_releases__mutmut_17, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_18': xǁGitHubReleasesClientǁlist_releases__mutmut_18, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_19': xǁGitHubReleasesClientǁlist_releases__mutmut_19, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_20': xǁGitHubReleasesClientǁlist_releases__mutmut_20, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_21': xǁGitHubReleasesClientǁlist_releases__mutmut_21, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_22': xǁGitHubReleasesClientǁlist_releases__mutmut_22, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_23': xǁGitHubReleasesClientǁlist_releases__mutmut_23, 
        'xǁGitHubReleasesClientǁlist_releases__mutmut_24': xǁGitHubReleasesClientǁlist_releases__mutmut_24
    }
    
    def list_releases(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitHubReleasesClientǁlist_releases__mutmut_orig"), object.__getattribute__(self, "xǁGitHubReleasesClientǁlist_releases__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list_releases.__signature__ = _mutmut_signature(xǁGitHubReleasesClientǁlist_releases__mutmut_orig)
    xǁGitHubReleasesClientǁlist_releases__mutmut_orig.__name__ = 'xǁGitHubReleasesClientǁlist_releases'

    async def xǁGitHubReleasesClientǁget_latest_release__mutmut_orig(self) -> Release:
        """Get the latest non-prerelease, non-draft release.

        Returns:
            Latest Release object
        """
        url = f"https://api.github.com/repos/{self.repo}/releases/latest"

        if logger.is_debug_enabled():
            logger.debug(f"Fetching latest release from {self.repo}")

        response = await self.client.get(url)
        data = response.json()

        return Release.from_api(data)

    async def xǁGitHubReleasesClientǁget_latest_release__mutmut_1(self) -> Release:
        """Get the latest non-prerelease, non-draft release.

        Returns:
            Latest Release object
        """
        url = None

        if logger.is_debug_enabled():
            logger.debug(f"Fetching latest release from {self.repo}")

        response = await self.client.get(url)
        data = response.json()

        return Release.from_api(data)

    async def xǁGitHubReleasesClientǁget_latest_release__mutmut_2(self) -> Release:
        """Get the latest non-prerelease, non-draft release.

        Returns:
            Latest Release object
        """
        url = f"https://api.github.com/repos/{self.repo}/releases/latest"

        if logger.is_debug_enabled():
            logger.debug(None)

        response = await self.client.get(url)
        data = response.json()

        return Release.from_api(data)

    async def xǁGitHubReleasesClientǁget_latest_release__mutmut_3(self) -> Release:
        """Get the latest non-prerelease, non-draft release.

        Returns:
            Latest Release object
        """
        url = f"https://api.github.com/repos/{self.repo}/releases/latest"

        if logger.is_debug_enabled():
            logger.debug(f"Fetching latest release from {self.repo}")

        response = None
        data = response.json()

        return Release.from_api(data)

    async def xǁGitHubReleasesClientǁget_latest_release__mutmut_4(self) -> Release:
        """Get the latest non-prerelease, non-draft release.

        Returns:
            Latest Release object
        """
        url = f"https://api.github.com/repos/{self.repo}/releases/latest"

        if logger.is_debug_enabled():
            logger.debug(f"Fetching latest release from {self.repo}")

        response = await self.client.get(None)
        data = response.json()

        return Release.from_api(data)

    async def xǁGitHubReleasesClientǁget_latest_release__mutmut_5(self) -> Release:
        """Get the latest non-prerelease, non-draft release.

        Returns:
            Latest Release object
        """
        url = f"https://api.github.com/repos/{self.repo}/releases/latest"

        if logger.is_debug_enabled():
            logger.debug(f"Fetching latest release from {self.repo}")

        response = await self.client.get(url)
        data = None

        return Release.from_api(data)

    async def xǁGitHubReleasesClientǁget_latest_release__mutmut_6(self) -> Release:
        """Get the latest non-prerelease, non-draft release.

        Returns:
            Latest Release object
        """
        url = f"https://api.github.com/repos/{self.repo}/releases/latest"

        if logger.is_debug_enabled():
            logger.debug(f"Fetching latest release from {self.repo}")

        response = await self.client.get(url)
        data = response.json()

        return Release.from_api(None)
    
    xǁGitHubReleasesClientǁget_latest_release__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitHubReleasesClientǁget_latest_release__mutmut_1': xǁGitHubReleasesClientǁget_latest_release__mutmut_1, 
        'xǁGitHubReleasesClientǁget_latest_release__mutmut_2': xǁGitHubReleasesClientǁget_latest_release__mutmut_2, 
        'xǁGitHubReleasesClientǁget_latest_release__mutmut_3': xǁGitHubReleasesClientǁget_latest_release__mutmut_3, 
        'xǁGitHubReleasesClientǁget_latest_release__mutmut_4': xǁGitHubReleasesClientǁget_latest_release__mutmut_4, 
        'xǁGitHubReleasesClientǁget_latest_release__mutmut_5': xǁGitHubReleasesClientǁget_latest_release__mutmut_5, 
        'xǁGitHubReleasesClientǁget_latest_release__mutmut_6': xǁGitHubReleasesClientǁget_latest_release__mutmut_6
    }
    
    def get_latest_release(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitHubReleasesClientǁget_latest_release__mutmut_orig"), object.__getattribute__(self, "xǁGitHubReleasesClientǁget_latest_release__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_latest_release.__signature__ = _mutmut_signature(xǁGitHubReleasesClientǁget_latest_release__mutmut_orig)
    xǁGitHubReleasesClientǁget_latest_release__mutmut_orig.__name__ = 'xǁGitHubReleasesClientǁget_latest_release'

    async def xǁGitHubReleasesClientǁget_release_by_tag__mutmut_orig(self, tag: str) -> Release:
        """Get release by tag name.

        Args:
            tag: Tag name (with or without 'v' prefix)

        Returns:
            Release object
        """
        url = f"https://api.github.com/repos/{self.repo}/releases/tags/{tag}"

        if logger.is_debug_enabled():
            logger.debug(f"Fetching release {tag} from {self.repo}")

        response = await self.client.get(url)
        data = response.json()

        return Release.from_api(data)

    async def xǁGitHubReleasesClientǁget_release_by_tag__mutmut_1(self, tag: str) -> Release:
        """Get release by tag name.

        Args:
            tag: Tag name (with or without 'v' prefix)

        Returns:
            Release object
        """
        url = None

        if logger.is_debug_enabled():
            logger.debug(f"Fetching release {tag} from {self.repo}")

        response = await self.client.get(url)
        data = response.json()

        return Release.from_api(data)

    async def xǁGitHubReleasesClientǁget_release_by_tag__mutmut_2(self, tag: str) -> Release:
        """Get release by tag name.

        Args:
            tag: Tag name (with or without 'v' prefix)

        Returns:
            Release object
        """
        url = f"https://api.github.com/repos/{self.repo}/releases/tags/{tag}"

        if logger.is_debug_enabled():
            logger.debug(None)

        response = await self.client.get(url)
        data = response.json()

        return Release.from_api(data)

    async def xǁGitHubReleasesClientǁget_release_by_tag__mutmut_3(self, tag: str) -> Release:
        """Get release by tag name.

        Args:
            tag: Tag name (with or without 'v' prefix)

        Returns:
            Release object
        """
        url = f"https://api.github.com/repos/{self.repo}/releases/tags/{tag}"

        if logger.is_debug_enabled():
            logger.debug(f"Fetching release {tag} from {self.repo}")

        response = None
        data = response.json()

        return Release.from_api(data)

    async def xǁGitHubReleasesClientǁget_release_by_tag__mutmut_4(self, tag: str) -> Release:
        """Get release by tag name.

        Args:
            tag: Tag name (with or without 'v' prefix)

        Returns:
            Release object
        """
        url = f"https://api.github.com/repos/{self.repo}/releases/tags/{tag}"

        if logger.is_debug_enabled():
            logger.debug(f"Fetching release {tag} from {self.repo}")

        response = await self.client.get(None)
        data = response.json()

        return Release.from_api(data)

    async def xǁGitHubReleasesClientǁget_release_by_tag__mutmut_5(self, tag: str) -> Release:
        """Get release by tag name.

        Args:
            tag: Tag name (with or without 'v' prefix)

        Returns:
            Release object
        """
        url = f"https://api.github.com/repos/{self.repo}/releases/tags/{tag}"

        if logger.is_debug_enabled():
            logger.debug(f"Fetching release {tag} from {self.repo}")

        response = await self.client.get(url)
        data = None

        return Release.from_api(data)

    async def xǁGitHubReleasesClientǁget_release_by_tag__mutmut_6(self, tag: str) -> Release:
        """Get release by tag name.

        Args:
            tag: Tag name (with or without 'v' prefix)

        Returns:
            Release object
        """
        url = f"https://api.github.com/repos/{self.repo}/releases/tags/{tag}"

        if logger.is_debug_enabled():
            logger.debug(f"Fetching release {tag} from {self.repo}")

        response = await self.client.get(url)
        data = response.json()

        return Release.from_api(None)
    
    xǁGitHubReleasesClientǁget_release_by_tag__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitHubReleasesClientǁget_release_by_tag__mutmut_1': xǁGitHubReleasesClientǁget_release_by_tag__mutmut_1, 
        'xǁGitHubReleasesClientǁget_release_by_tag__mutmut_2': xǁGitHubReleasesClientǁget_release_by_tag__mutmut_2, 
        'xǁGitHubReleasesClientǁget_release_by_tag__mutmut_3': xǁGitHubReleasesClientǁget_release_by_tag__mutmut_3, 
        'xǁGitHubReleasesClientǁget_release_by_tag__mutmut_4': xǁGitHubReleasesClientǁget_release_by_tag__mutmut_4, 
        'xǁGitHubReleasesClientǁget_release_by_tag__mutmut_5': xǁGitHubReleasesClientǁget_release_by_tag__mutmut_5, 
        'xǁGitHubReleasesClientǁget_release_by_tag__mutmut_6': xǁGitHubReleasesClientǁget_release_by_tag__mutmut_6
    }
    
    def get_release_by_tag(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitHubReleasesClientǁget_release_by_tag__mutmut_orig"), object.__getattribute__(self, "xǁGitHubReleasesClientǁget_release_by_tag__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_release_by_tag.__signature__ = _mutmut_signature(xǁGitHubReleasesClientǁget_release_by_tag__mutmut_orig)
    xǁGitHubReleasesClientǁget_release_by_tag__mutmut_orig.__name__ = 'xǁGitHubReleasesClientǁget_release_by_tag'

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_orig(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_1(self, per_page: int = 101) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_2(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = None
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_3(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = None

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_4(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"XXper_pageXX": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_5(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"PER_PAGE": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_6(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(None, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_7(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(per_page, None)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_8(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_9(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(per_page, )}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_10(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(per_page, 101)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_11(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(None)

        response = await self.client.get(url, params=params)
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_12(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = None
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_13(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(None, params=params)
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_14(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, params=None)
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_15(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(params=params)
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_16(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, )
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_17(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, params=params)
        data = None

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_18(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        tags = None

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_19(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        tags = [Tag.from_api(None) for t in data]

        if logger.is_debug_enabled():
            logger.debug(f"Found {len(tags)} tags")
        return tags

    async def xǁGitHubReleasesClientǁlist_tags__mutmut_20(self, per_page: int = 100) -> list[Tag]:
        """List all tags from repository.

        Args:
            per_page: Number of tags per page (max 100)

        Returns:
            List of Tag objects
        """
        url = f"https://api.github.com/repos/{self.repo}/tags"
        params = {"per_page": min(per_page, 100)}

        if logger.is_debug_enabled():
            logger.debug(f"Fetching tags from {self.repo}")

        response = await self.client.get(url, params=params)
        data = response.json()

        tags = [Tag.from_api(t) for t in data]

        if logger.is_debug_enabled():
            logger.debug(None)
        return tags
    
    xǁGitHubReleasesClientǁlist_tags__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitHubReleasesClientǁlist_tags__mutmut_1': xǁGitHubReleasesClientǁlist_tags__mutmut_1, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_2': xǁGitHubReleasesClientǁlist_tags__mutmut_2, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_3': xǁGitHubReleasesClientǁlist_tags__mutmut_3, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_4': xǁGitHubReleasesClientǁlist_tags__mutmut_4, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_5': xǁGitHubReleasesClientǁlist_tags__mutmut_5, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_6': xǁGitHubReleasesClientǁlist_tags__mutmut_6, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_7': xǁGitHubReleasesClientǁlist_tags__mutmut_7, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_8': xǁGitHubReleasesClientǁlist_tags__mutmut_8, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_9': xǁGitHubReleasesClientǁlist_tags__mutmut_9, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_10': xǁGitHubReleasesClientǁlist_tags__mutmut_10, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_11': xǁGitHubReleasesClientǁlist_tags__mutmut_11, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_12': xǁGitHubReleasesClientǁlist_tags__mutmut_12, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_13': xǁGitHubReleasesClientǁlist_tags__mutmut_13, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_14': xǁGitHubReleasesClientǁlist_tags__mutmut_14, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_15': xǁGitHubReleasesClientǁlist_tags__mutmut_15, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_16': xǁGitHubReleasesClientǁlist_tags__mutmut_16, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_17': xǁGitHubReleasesClientǁlist_tags__mutmut_17, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_18': xǁGitHubReleasesClientǁlist_tags__mutmut_18, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_19': xǁGitHubReleasesClientǁlist_tags__mutmut_19, 
        'xǁGitHubReleasesClientǁlist_tags__mutmut_20': xǁGitHubReleasesClientǁlist_tags__mutmut_20
    }
    
    def list_tags(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitHubReleasesClientǁlist_tags__mutmut_orig"), object.__getattribute__(self, "xǁGitHubReleasesClientǁlist_tags__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list_tags.__signature__ = _mutmut_signature(xǁGitHubReleasesClientǁlist_tags__mutmut_orig)
    xǁGitHubReleasesClientǁlist_tags__mutmut_orig.__name__ = 'xǁGitHubReleasesClientǁlist_tags'

    async def xǁGitHubReleasesClientǁdownload_asset__mutmut_orig(
        self,
        asset: Asset,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download release asset to destination.

        Args:
            asset: Asset to download
            destination: Where to save the file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
        """
        await self._download_file(asset.browser_download_url, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_asset__mutmut_1(
        self,
        asset: Asset,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download release asset to destination.

        Args:
            asset: Asset to download
            destination: Where to save the file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
        """
        await self._download_file(None, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_asset__mutmut_2(
        self,
        asset: Asset,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download release asset to destination.

        Args:
            asset: Asset to download
            destination: Where to save the file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
        """
        await self._download_file(asset.browser_download_url, None, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_asset__mutmut_3(
        self,
        asset: Asset,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download release asset to destination.

        Args:
            asset: Asset to download
            destination: Where to save the file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
        """
        await self._download_file(asset.browser_download_url, destination, None)

    async def xǁGitHubReleasesClientǁdownload_asset__mutmut_4(
        self,
        asset: Asset,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download release asset to destination.

        Args:
            asset: Asset to download
            destination: Where to save the file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
        """
        await self._download_file(destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_asset__mutmut_5(
        self,
        asset: Asset,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download release asset to destination.

        Args:
            asset: Asset to download
            destination: Where to save the file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
        """
        await self._download_file(asset.browser_download_url, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_asset__mutmut_6(
        self,
        asset: Asset,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download release asset to destination.

        Args:
            asset: Asset to download
            destination: Where to save the file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
        """
        await self._download_file(asset.browser_download_url, destination, )
    
    xǁGitHubReleasesClientǁdownload_asset__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitHubReleasesClientǁdownload_asset__mutmut_1': xǁGitHubReleasesClientǁdownload_asset__mutmut_1, 
        'xǁGitHubReleasesClientǁdownload_asset__mutmut_2': xǁGitHubReleasesClientǁdownload_asset__mutmut_2, 
        'xǁGitHubReleasesClientǁdownload_asset__mutmut_3': xǁGitHubReleasesClientǁdownload_asset__mutmut_3, 
        'xǁGitHubReleasesClientǁdownload_asset__mutmut_4': xǁGitHubReleasesClientǁdownload_asset__mutmut_4, 
        'xǁGitHubReleasesClientǁdownload_asset__mutmut_5': xǁGitHubReleasesClientǁdownload_asset__mutmut_5, 
        'xǁGitHubReleasesClientǁdownload_asset__mutmut_6': xǁGitHubReleasesClientǁdownload_asset__mutmut_6
    }
    
    def download_asset(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitHubReleasesClientǁdownload_asset__mutmut_orig"), object.__getattribute__(self, "xǁGitHubReleasesClientǁdownload_asset__mutmut_mutants"), args, kwargs, self)
        return result 
    
    download_asset.__signature__ = _mutmut_signature(xǁGitHubReleasesClientǁdownload_asset__mutmut_orig)
    xǁGitHubReleasesClientǁdownload_asset__mutmut_orig.__name__ = 'xǁGitHubReleasesClientǁdownload_asset'

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_orig(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "zipball" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_1(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "XXzipballXX",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "zipball" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_2(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "ZIPBALL",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "zipball" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_3(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "XXheadsXX",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "zipball" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_4(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "HEADS",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "zipball" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_5(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = None
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_6(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "XXzipXX" if format == "zipball" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_7(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "ZIP" if format == "zipball" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_8(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format != "zipball" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_9(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "XXzipballXX" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_10(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "ZIPBALL" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_11(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "zipball" else "XXtar.gzXX"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_12(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "zipball" else "TAR.GZ"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_13(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "zipball" else "tar.gz"
        url = None

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_14(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "zipball" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(None)

        await self._download_file(url, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_15(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "zipball" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(None, destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_16(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "zipball" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, None, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_17(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "zipball" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, destination, None)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_18(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "zipball" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(destination, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_19(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "zipball" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, progress_callback)

    async def xǁGitHubReleasesClientǁdownload_archive__mutmut_20(
        self,
        ref: str,
        destination: pathlib.Path,
        format: Literal["zipball", "tarball"] = "zipball",
        ref_type: Literal["heads", "tags"] = "heads",
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download repository archive.

        Args:
            ref: Branch name, tag name, or commit SHA
            destination: Where to save archive
            format: Archive format - 'zipball' (.zip) or 'tarball' (.tar.gz)
            ref_type: Reference type - 'heads' (branch) or 'tags'
            progress_callback: Optional callback(downloaded_bytes, total_bytes)

        Examples:
            # Download main branch as zip
            await client.download_archive("main", "repo.zip", "zipball", "heads")

            # Download tag as tarball
            await client.download_archive("v1.0.0", "repo.tar.gz", "tarball", "tags")
        """
        ext = "zip" if format == "zipball" else "tar.gz"
        url = f"https://github.com/{self.repo}/archive/refs/{ref_type}/{ref}.{ext}"

        logger.info(f"Downloading archive from {url}")

        await self._download_file(url, destination, )
    
    xǁGitHubReleasesClientǁdownload_archive__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitHubReleasesClientǁdownload_archive__mutmut_1': xǁGitHubReleasesClientǁdownload_archive__mutmut_1, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_2': xǁGitHubReleasesClientǁdownload_archive__mutmut_2, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_3': xǁGitHubReleasesClientǁdownload_archive__mutmut_3, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_4': xǁGitHubReleasesClientǁdownload_archive__mutmut_4, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_5': xǁGitHubReleasesClientǁdownload_archive__mutmut_5, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_6': xǁGitHubReleasesClientǁdownload_archive__mutmut_6, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_7': xǁGitHubReleasesClientǁdownload_archive__mutmut_7, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_8': xǁGitHubReleasesClientǁdownload_archive__mutmut_8, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_9': xǁGitHubReleasesClientǁdownload_archive__mutmut_9, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_10': xǁGitHubReleasesClientǁdownload_archive__mutmut_10, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_11': xǁGitHubReleasesClientǁdownload_archive__mutmut_11, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_12': xǁGitHubReleasesClientǁdownload_archive__mutmut_12, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_13': xǁGitHubReleasesClientǁdownload_archive__mutmut_13, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_14': xǁGitHubReleasesClientǁdownload_archive__mutmut_14, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_15': xǁGitHubReleasesClientǁdownload_archive__mutmut_15, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_16': xǁGitHubReleasesClientǁdownload_archive__mutmut_16, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_17': xǁGitHubReleasesClientǁdownload_archive__mutmut_17, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_18': xǁGitHubReleasesClientǁdownload_archive__mutmut_18, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_19': xǁGitHubReleasesClientǁdownload_archive__mutmut_19, 
        'xǁGitHubReleasesClientǁdownload_archive__mutmut_20': xǁGitHubReleasesClientǁdownload_archive__mutmut_20
    }
    
    def download_archive(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitHubReleasesClientǁdownload_archive__mutmut_orig"), object.__getattribute__(self, "xǁGitHubReleasesClientǁdownload_archive__mutmut_mutants"), args, kwargs, self)
        return result 
    
    download_archive.__signature__ = _mutmut_signature(xǁGitHubReleasesClientǁdownload_archive__mutmut_orig)
    xǁGitHubReleasesClientǁdownload_archive__mutmut_orig.__name__ = 'xǁGitHubReleasesClientǁdownload_archive'

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_orig(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_1(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=None, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_2(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=None)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_3(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_4(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, )

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_5(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=False, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_6(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=False)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_7(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(None)

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_8(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = None
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_9(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 1
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_10(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = None

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_11(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 1

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_12(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = None
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_13(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(None)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_14(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "XXcontent-lengthXX" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_15(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "CONTENT-LENGTH" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_16(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" not in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_17(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = None
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_18(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(None)
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_19(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["XXcontent-lengthXX"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_20(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["CONTENT-LENGTH"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_21(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open(None) as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_22(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("XXwbXX") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_23(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("WB") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_24(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(None):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_25(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(None)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_26(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded = len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_27(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded -= len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_28(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(None, total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_29(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, None)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_30(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(total_size)

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_31(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, )

        logger.info(f"Successfully downloaded {destination.name} ({downloaded} bytes)")

    async def xǁGitHubReleasesClientǁ_download_file__mutmut_32(
        self,
        url: str,
        destination: pathlib.Path,
        progress_callback: Callable[[int, int], None] | None = None,
    ) -> None:
        """Download file using streaming.

        Args:
            url: URL to download
            destination: Where to save file
            progress_callback: Optional callback(downloaded_bytes, total_bytes)
                             total_bytes will be 0 if size is unknown
        """
        # Create parent directories
        destination.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Downloading {url} to {destination}")

        downloaded = 0
        total_size = 0

        # First get total size from HEAD request if possible
        try:
            head_response = await self.client.head(url)
            if "content-length" in head_response.headers:
                total_size = int(head_response.headers["content-length"])
        except Exception:
            pass  # nosec B110 - Size unknown, continue without it

        # Stream download
        async with self.client:
            with destination.open("wb") as f:
                async for chunk in self.client.stream(url):
                    f.write(chunk)
                    downloaded += len(chunk)

                    # Call progress callback even if total size is unknown (pass 0)
                    if progress_callback:
                        progress_callback(downloaded, total_size)

        logger.info(None)
    
    xǁGitHubReleasesClientǁ_download_file__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitHubReleasesClientǁ_download_file__mutmut_1': xǁGitHubReleasesClientǁ_download_file__mutmut_1, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_2': xǁGitHubReleasesClientǁ_download_file__mutmut_2, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_3': xǁGitHubReleasesClientǁ_download_file__mutmut_3, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_4': xǁGitHubReleasesClientǁ_download_file__mutmut_4, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_5': xǁGitHubReleasesClientǁ_download_file__mutmut_5, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_6': xǁGitHubReleasesClientǁ_download_file__mutmut_6, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_7': xǁGitHubReleasesClientǁ_download_file__mutmut_7, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_8': xǁGitHubReleasesClientǁ_download_file__mutmut_8, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_9': xǁGitHubReleasesClientǁ_download_file__mutmut_9, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_10': xǁGitHubReleasesClientǁ_download_file__mutmut_10, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_11': xǁGitHubReleasesClientǁ_download_file__mutmut_11, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_12': xǁGitHubReleasesClientǁ_download_file__mutmut_12, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_13': xǁGitHubReleasesClientǁ_download_file__mutmut_13, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_14': xǁGitHubReleasesClientǁ_download_file__mutmut_14, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_15': xǁGitHubReleasesClientǁ_download_file__mutmut_15, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_16': xǁGitHubReleasesClientǁ_download_file__mutmut_16, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_17': xǁGitHubReleasesClientǁ_download_file__mutmut_17, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_18': xǁGitHubReleasesClientǁ_download_file__mutmut_18, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_19': xǁGitHubReleasesClientǁ_download_file__mutmut_19, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_20': xǁGitHubReleasesClientǁ_download_file__mutmut_20, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_21': xǁGitHubReleasesClientǁ_download_file__mutmut_21, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_22': xǁGitHubReleasesClientǁ_download_file__mutmut_22, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_23': xǁGitHubReleasesClientǁ_download_file__mutmut_23, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_24': xǁGitHubReleasesClientǁ_download_file__mutmut_24, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_25': xǁGitHubReleasesClientǁ_download_file__mutmut_25, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_26': xǁGitHubReleasesClientǁ_download_file__mutmut_26, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_27': xǁGitHubReleasesClientǁ_download_file__mutmut_27, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_28': xǁGitHubReleasesClientǁ_download_file__mutmut_28, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_29': xǁGitHubReleasesClientǁ_download_file__mutmut_29, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_30': xǁGitHubReleasesClientǁ_download_file__mutmut_30, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_31': xǁGitHubReleasesClientǁ_download_file__mutmut_31, 
        'xǁGitHubReleasesClientǁ_download_file__mutmut_32': xǁGitHubReleasesClientǁ_download_file__mutmut_32
    }
    
    def _download_file(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitHubReleasesClientǁ_download_file__mutmut_orig"), object.__getattribute__(self, "xǁGitHubReleasesClientǁ_download_file__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _download_file.__signature__ = _mutmut_signature(xǁGitHubReleasesClientǁ_download_file__mutmut_orig)
    xǁGitHubReleasesClientǁ_download_file__mutmut_orig.__name__ = 'xǁGitHubReleasesClientǁ_download_file'

    async def xǁGitHubReleasesClientǁget_versions__mutmut_orig(self, include_prereleases: bool = False) -> list[str]:
        """Get list of version strings from releases.

        Args:
            include_prereleases: Include prerelease versions

        Returns:
            List of version strings (tag names with 'v' prefix stripped)
        """
        releases = await self.list_releases(include_prereleases=include_prereleases)
        versions = []

        for release in releases:
            version = release.tag_name
            # Strip leading 'v' if present
            if version.startswith("v"):
                version = version[1:]
            versions.append(version)

        return versions

    async def xǁGitHubReleasesClientǁget_versions__mutmut_1(self, include_prereleases: bool = True) -> list[str]:
        """Get list of version strings from releases.

        Args:
            include_prereleases: Include prerelease versions

        Returns:
            List of version strings (tag names with 'v' prefix stripped)
        """
        releases = await self.list_releases(include_prereleases=include_prereleases)
        versions = []

        for release in releases:
            version = release.tag_name
            # Strip leading 'v' if present
            if version.startswith("v"):
                version = version[1:]
            versions.append(version)

        return versions

    async def xǁGitHubReleasesClientǁget_versions__mutmut_2(self, include_prereleases: bool = False) -> list[str]:
        """Get list of version strings from releases.

        Args:
            include_prereleases: Include prerelease versions

        Returns:
            List of version strings (tag names with 'v' prefix stripped)
        """
        releases = None
        versions = []

        for release in releases:
            version = release.tag_name
            # Strip leading 'v' if present
            if version.startswith("v"):
                version = version[1:]
            versions.append(version)

        return versions

    async def xǁGitHubReleasesClientǁget_versions__mutmut_3(self, include_prereleases: bool = False) -> list[str]:
        """Get list of version strings from releases.

        Args:
            include_prereleases: Include prerelease versions

        Returns:
            List of version strings (tag names with 'v' prefix stripped)
        """
        releases = await self.list_releases(include_prereleases=None)
        versions = []

        for release in releases:
            version = release.tag_name
            # Strip leading 'v' if present
            if version.startswith("v"):
                version = version[1:]
            versions.append(version)

        return versions

    async def xǁGitHubReleasesClientǁget_versions__mutmut_4(self, include_prereleases: bool = False) -> list[str]:
        """Get list of version strings from releases.

        Args:
            include_prereleases: Include prerelease versions

        Returns:
            List of version strings (tag names with 'v' prefix stripped)
        """
        releases = await self.list_releases(include_prereleases=include_prereleases)
        versions = None

        for release in releases:
            version = release.tag_name
            # Strip leading 'v' if present
            if version.startswith("v"):
                version = version[1:]
            versions.append(version)

        return versions

    async def xǁGitHubReleasesClientǁget_versions__mutmut_5(self, include_prereleases: bool = False) -> list[str]:
        """Get list of version strings from releases.

        Args:
            include_prereleases: Include prerelease versions

        Returns:
            List of version strings (tag names with 'v' prefix stripped)
        """
        releases = await self.list_releases(include_prereleases=include_prereleases)
        versions = []

        for release in releases:
            version = None
            # Strip leading 'v' if present
            if version.startswith("v"):
                version = version[1:]
            versions.append(version)

        return versions

    async def xǁGitHubReleasesClientǁget_versions__mutmut_6(self, include_prereleases: bool = False) -> list[str]:
        """Get list of version strings from releases.

        Args:
            include_prereleases: Include prerelease versions

        Returns:
            List of version strings (tag names with 'v' prefix stripped)
        """
        releases = await self.list_releases(include_prereleases=include_prereleases)
        versions = []

        for release in releases:
            version = release.tag_name
            # Strip leading 'v' if present
            if version.startswith(None):
                version = version[1:]
            versions.append(version)

        return versions

    async def xǁGitHubReleasesClientǁget_versions__mutmut_7(self, include_prereleases: bool = False) -> list[str]:
        """Get list of version strings from releases.

        Args:
            include_prereleases: Include prerelease versions

        Returns:
            List of version strings (tag names with 'v' prefix stripped)
        """
        releases = await self.list_releases(include_prereleases=include_prereleases)
        versions = []

        for release in releases:
            version = release.tag_name
            # Strip leading 'v' if present
            if version.startswith("XXvXX"):
                version = version[1:]
            versions.append(version)

        return versions

    async def xǁGitHubReleasesClientǁget_versions__mutmut_8(self, include_prereleases: bool = False) -> list[str]:
        """Get list of version strings from releases.

        Args:
            include_prereleases: Include prerelease versions

        Returns:
            List of version strings (tag names with 'v' prefix stripped)
        """
        releases = await self.list_releases(include_prereleases=include_prereleases)
        versions = []

        for release in releases:
            version = release.tag_name
            # Strip leading 'v' if present
            if version.startswith("V"):
                version = version[1:]
            versions.append(version)

        return versions

    async def xǁGitHubReleasesClientǁget_versions__mutmut_9(self, include_prereleases: bool = False) -> list[str]:
        """Get list of version strings from releases.

        Args:
            include_prereleases: Include prerelease versions

        Returns:
            List of version strings (tag names with 'v' prefix stripped)
        """
        releases = await self.list_releases(include_prereleases=include_prereleases)
        versions = []

        for release in releases:
            version = release.tag_name
            # Strip leading 'v' if present
            if version.startswith("v"):
                version = None
            versions.append(version)

        return versions

    async def xǁGitHubReleasesClientǁget_versions__mutmut_10(self, include_prereleases: bool = False) -> list[str]:
        """Get list of version strings from releases.

        Args:
            include_prereleases: Include prerelease versions

        Returns:
            List of version strings (tag names with 'v' prefix stripped)
        """
        releases = await self.list_releases(include_prereleases=include_prereleases)
        versions = []

        for release in releases:
            version = release.tag_name
            # Strip leading 'v' if present
            if version.startswith("v"):
                version = version[2:]
            versions.append(version)

        return versions

    async def xǁGitHubReleasesClientǁget_versions__mutmut_11(self, include_prereleases: bool = False) -> list[str]:
        """Get list of version strings from releases.

        Args:
            include_prereleases: Include prerelease versions

        Returns:
            List of version strings (tag names with 'v' prefix stripped)
        """
        releases = await self.list_releases(include_prereleases=include_prereleases)
        versions = []

        for release in releases:
            version = release.tag_name
            # Strip leading 'v' if present
            if version.startswith("v"):
                version = version[1:]
            versions.append(None)

        return versions
    
    xǁGitHubReleasesClientǁget_versions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitHubReleasesClientǁget_versions__mutmut_1': xǁGitHubReleasesClientǁget_versions__mutmut_1, 
        'xǁGitHubReleasesClientǁget_versions__mutmut_2': xǁGitHubReleasesClientǁget_versions__mutmut_2, 
        'xǁGitHubReleasesClientǁget_versions__mutmut_3': xǁGitHubReleasesClientǁget_versions__mutmut_3, 
        'xǁGitHubReleasesClientǁget_versions__mutmut_4': xǁGitHubReleasesClientǁget_versions__mutmut_4, 
        'xǁGitHubReleasesClientǁget_versions__mutmut_5': xǁGitHubReleasesClientǁget_versions__mutmut_5, 
        'xǁGitHubReleasesClientǁget_versions__mutmut_6': xǁGitHubReleasesClientǁget_versions__mutmut_6, 
        'xǁGitHubReleasesClientǁget_versions__mutmut_7': xǁGitHubReleasesClientǁget_versions__mutmut_7, 
        'xǁGitHubReleasesClientǁget_versions__mutmut_8': xǁGitHubReleasesClientǁget_versions__mutmut_8, 
        'xǁGitHubReleasesClientǁget_versions__mutmut_9': xǁGitHubReleasesClientǁget_versions__mutmut_9, 
        'xǁGitHubReleasesClientǁget_versions__mutmut_10': xǁGitHubReleasesClientǁget_versions__mutmut_10, 
        'xǁGitHubReleasesClientǁget_versions__mutmut_11': xǁGitHubReleasesClientǁget_versions__mutmut_11
    }
    
    def get_versions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitHubReleasesClientǁget_versions__mutmut_orig"), object.__getattribute__(self, "xǁGitHubReleasesClientǁget_versions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_versions.__signature__ = _mutmut_signature(xǁGitHubReleasesClientǁget_versions__mutmut_orig)
    xǁGitHubReleasesClientǁget_versions__mutmut_orig.__name__ = 'xǁGitHubReleasesClientǁget_versions'

    def xǁGitHubReleasesClientǁfind_asset__mutmut_orig(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace("*", ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_1(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name != pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace("*", ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_2(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(None)
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace("*", ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_3(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = None

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_4(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace(None, ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_5(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace("*", None) if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_6(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace(".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_7(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace("*", ) if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_8(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(None, r"\.").replace("*", ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_9(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", None).replace("*", ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_10(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(r"\.").replace("*", ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_11(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", ).replace("*", ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_12(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace("XX.XX", r"\.").replace("*", ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_13(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"XX\.XX").replace("*", ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_14(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace("XX*XX", ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_15(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace("*", "XX.*XX") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_16(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace("*", ".*") if "XX*XX" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_17(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace("*", ".*") if "*" not in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_18(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace("*", ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(None, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_19(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace("*", ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, None):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_20(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace("*", ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_21(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace("*", ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, ):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_22(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace("*", ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(None)
                return asset

        if logger.is_debug_enabled():
            logger.debug(f"No asset found matching pattern: {pattern}")
        return None

    def xǁGitHubReleasesClientǁfind_asset__mutmut_23(self, release: Release, pattern: str) -> Asset | None:
        """Find asset in release matching pattern.

        Args:
            release: Release to search
            pattern: Regex pattern or simple glob-like pattern (*) to match

        Returns:
            First matching Asset or None
        """
        # First try exact match
        for asset in release.assets:
            if asset.name == pattern:
                if logger.is_debug_enabled():
                    logger.debug(f"Found exact matching asset: {asset.name}")
                return asset

        # Convert simple glob to regex
        regex_pattern = pattern.replace(".", r"\.").replace("*", ".*") if "*" in pattern else pattern

        # Try pattern match
        for asset in release.assets:
            if re.search(regex_pattern, asset.name):
                if logger.is_debug_enabled():
                    logger.debug(f"Found matching asset: {asset.name}")
                return asset

        if logger.is_debug_enabled():
            logger.debug(None)
        return None
    
    xǁGitHubReleasesClientǁfind_asset__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitHubReleasesClientǁfind_asset__mutmut_1': xǁGitHubReleasesClientǁfind_asset__mutmut_1, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_2': xǁGitHubReleasesClientǁfind_asset__mutmut_2, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_3': xǁGitHubReleasesClientǁfind_asset__mutmut_3, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_4': xǁGitHubReleasesClientǁfind_asset__mutmut_4, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_5': xǁGitHubReleasesClientǁfind_asset__mutmut_5, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_6': xǁGitHubReleasesClientǁfind_asset__mutmut_6, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_7': xǁGitHubReleasesClientǁfind_asset__mutmut_7, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_8': xǁGitHubReleasesClientǁfind_asset__mutmut_8, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_9': xǁGitHubReleasesClientǁfind_asset__mutmut_9, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_10': xǁGitHubReleasesClientǁfind_asset__mutmut_10, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_11': xǁGitHubReleasesClientǁfind_asset__mutmut_11, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_12': xǁGitHubReleasesClientǁfind_asset__mutmut_12, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_13': xǁGitHubReleasesClientǁfind_asset__mutmut_13, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_14': xǁGitHubReleasesClientǁfind_asset__mutmut_14, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_15': xǁGitHubReleasesClientǁfind_asset__mutmut_15, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_16': xǁGitHubReleasesClientǁfind_asset__mutmut_16, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_17': xǁGitHubReleasesClientǁfind_asset__mutmut_17, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_18': xǁGitHubReleasesClientǁfind_asset__mutmut_18, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_19': xǁGitHubReleasesClientǁfind_asset__mutmut_19, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_20': xǁGitHubReleasesClientǁfind_asset__mutmut_20, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_21': xǁGitHubReleasesClientǁfind_asset__mutmut_21, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_22': xǁGitHubReleasesClientǁfind_asset__mutmut_22, 
        'xǁGitHubReleasesClientǁfind_asset__mutmut_23': xǁGitHubReleasesClientǁfind_asset__mutmut_23
    }
    
    def find_asset(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitHubReleasesClientǁfind_asset__mutmut_orig"), object.__getattribute__(self, "xǁGitHubReleasesClientǁfind_asset__mutmut_mutants"), args, kwargs, self)
        return result 
    
    find_asset.__signature__ = _mutmut_signature(xǁGitHubReleasesClientǁfind_asset__mutmut_orig)
    xǁGitHubReleasesClientǁfind_asset__mutmut_orig.__name__ = 'xǁGitHubReleasesClientǁfind_asset'

    async def close(self) -> None:
        """Close the client and cleanup resources."""
        # UniversalClient will cleanup in __aexit__

    async def __aenter__(self) -> GitHubReleasesClient:
        """Context manager entry."""
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Context manager exit."""
        await self.close()


__all__ = [
    "GitHubReleasesClient",
]

# 🧰🌍🔚
