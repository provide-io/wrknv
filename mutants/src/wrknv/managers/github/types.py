#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""GitHub API Types
================
Type definitions for GitHub API responses."""

from __future__ import annotations

from attrs import define, field
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


@define
class Asset:
    """GitHub release asset."""

    name: str
    browser_download_url: str
    size: int
    content_type: str
    id: int = 0
    state: str = "uploaded"
    created_at: str = ""
    updated_at: str = ""

    @classmethod
    def from_api(cls, data: dict) -> Asset:
        """Create Asset from GitHub API response."""
        return cls(
            name=data["name"],
            browser_download_url=data["browser_download_url"],
            size=data["size"],
            content_type=data["content_type"],
            id=data.get("id", 0),
            state=data.get("state", "uploaded"),
            created_at=data.get("created_at", ""),
            updated_at=data.get("updated_at", ""),
        )


@define
class Release:
    """GitHub release."""

    tag_name: str
    name: str
    prerelease: bool
    draft: bool
    assets: list[Asset] = field(factory=list)
    body: str = ""
    published_at: str = ""
    created_at: str = ""
    id: int = 0
    html_url: str = ""

    @classmethod
    def from_api(cls, data: dict) -> Release:
        """Create Release from GitHub API response."""
        assets = [Asset.from_api(asset) for asset in data.get("assets", [])]

        return cls(
            tag_name=data["tag_name"],
            name=data.get("name", ""),
            prerelease=data.get("prerelease", False),
            draft=data.get("draft", False),
            assets=assets,
            body=data.get("body", ""),
            published_at=data.get("published_at", ""),
            created_at=data.get("created_at", ""),
            id=data.get("id", 0),
            html_url=data.get("html_url", ""),
        )


@define
class Tag:
    """GitHub tag."""

    name: str
    commit_sha: str
    zipball_url: str = ""
    tarball_url: str = ""

    @classmethod
    def from_api(cls, data: dict) -> Tag:
        """Create Tag from GitHub API response."""
        return cls(
            name=data["name"],
            commit_sha=data["commit"]["sha"],
            zipball_url=data.get("zipball_url", ""),
            tarball_url=data.get("tarball_url", ""),
        )


__all__ = [
    "Asset",
    "Release",
    "Tag",
]

# 🧰🌍🔚
