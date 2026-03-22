#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Gitignore File Builder
======================
Constructs gitignore files with proper formatting and sections."""

from __future__ import annotations

from pathlib import Path

from provide.foundation import logger
from provide.foundation.time import provide_now

# Pattern dictionaries for ecosystem-specific sections
WRKNV_PATTERNS: dict[str, list[str]] = {
    "Work environment directories": [
        "workenv/",
        "wrknv_*/",
    ],
    "wrknv configuration and cache": [
        ".wrknv/",
        "*.wrknv.bak",
    ],
    "Container volumes": [
        ".wrknv_*/",
    ],
}

PROVIDE_PATTERNS: dict[str, list[str]] = {
    "Generated outputs and artifacts": [
        ".provide/output/",
        ".provide/shared/",
        ".provide/logs/",
        ".provide/cache/",
    ],
    "Log files": [
        "*.log",
        "*.log.*",
        "logs/",
    ],
    "Local/temporary files": [
        "*.local",
        "*.local.*",
        ".*.local",
        "*.bak",
        "*.tmp",
    ],
}
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


class GitignoreBuilder:
    """Builds gitignore files with proper sections and formatting."""

    def xǁGitignoreBuilderǁ__init____mutmut_orig(self) -> None:
        """Initialize the builder."""
        self.sections: list[tuple[str, str]] = []
        self.custom_rules: list[str] = []
        logger.debug("GitignoreBuilder initialized")

    def xǁGitignoreBuilderǁ__init____mutmut_1(self) -> None:
        """Initialize the builder."""
        self.sections: list[tuple[str, str]] = None
        self.custom_rules: list[str] = []
        logger.debug("GitignoreBuilder initialized")

    def xǁGitignoreBuilderǁ__init____mutmut_2(self) -> None:
        """Initialize the builder."""
        self.sections: list[tuple[str, str]] = []
        self.custom_rules: list[str] = None
        logger.debug("GitignoreBuilder initialized")

    def xǁGitignoreBuilderǁ__init____mutmut_3(self) -> None:
        """Initialize the builder."""
        self.sections: list[tuple[str, str]] = []
        self.custom_rules: list[str] = []
        logger.debug(None)

    def xǁGitignoreBuilderǁ__init____mutmut_4(self) -> None:
        """Initialize the builder."""
        self.sections: list[tuple[str, str]] = []
        self.custom_rules: list[str] = []
        logger.debug("XXGitignoreBuilder initializedXX")

    def xǁGitignoreBuilderǁ__init____mutmut_5(self) -> None:
        """Initialize the builder."""
        self.sections: list[tuple[str, str]] = []
        self.custom_rules: list[str] = []
        logger.debug("gitignorebuilder initialized")

    def xǁGitignoreBuilderǁ__init____mutmut_6(self) -> None:
        """Initialize the builder."""
        self.sections: list[tuple[str, str]] = []
        self.custom_rules: list[str] = []
        logger.debug("GITIGNOREBUILDER INITIALIZED")
    
    xǁGitignoreBuilderǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreBuilderǁ__init____mutmut_1': xǁGitignoreBuilderǁ__init____mutmut_1, 
        'xǁGitignoreBuilderǁ__init____mutmut_2': xǁGitignoreBuilderǁ__init____mutmut_2, 
        'xǁGitignoreBuilderǁ__init____mutmut_3': xǁGitignoreBuilderǁ__init____mutmut_3, 
        'xǁGitignoreBuilderǁ__init____mutmut_4': xǁGitignoreBuilderǁ__init____mutmut_4, 
        'xǁGitignoreBuilderǁ__init____mutmut_5': xǁGitignoreBuilderǁ__init____mutmut_5, 
        'xǁGitignoreBuilderǁ__init____mutmut_6': xǁGitignoreBuilderǁ__init____mutmut_6
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreBuilderǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁGitignoreBuilderǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁGitignoreBuilderǁ__init____mutmut_orig)
    xǁGitignoreBuilderǁ__init____mutmut_orig.__name__ = 'xǁGitignoreBuilderǁ__init__'

    def xǁGitignoreBuilderǁadd_header__mutmut_orig(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_1(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = None

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_2(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "XX# ========================XX",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_3(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "XX# Generated by wrknvXX",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_4(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_5(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# GENERATED BY WRKNV",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_6(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime(None)}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_7(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('XX%Y-%m-%d %H:%M:%SXX')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_8(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%y-%m-%d %h:%m:%s')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_9(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%M-%D %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_10(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(None)

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_11(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            None
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_12(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "XX# ========================XX",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_13(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "XXXX",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_14(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "XX# This file is auto-generated. Custom rules should be addedXX",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_15(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# this file is auto-generated. custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_16(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# THIS FILE IS AUTO-GENERATED. CUSTOM RULES SHOULD BE ADDED",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_17(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "XX# in the 'Custom Rules' section at the bottom to preserve themXX",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_18(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'custom rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_19(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# IN THE 'CUSTOM RULES' SECTION AT THE BOTTOM TO PRESERVE THEM",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_20(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "XX# during regeneration.XX",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_21(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# DURING REGENERATION.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_22(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "XXXX",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_23(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(None, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_24(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, None)
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_25(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_26(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, )
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_27(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(1, ("header", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_28(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("XXheaderXX", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_29(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("HEADER", "\n".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_30(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(None)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_31(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "XX\nXX".join(header_lines)))
        logger.debug(f"Added header for project: {project_name}")

    def xǁGitignoreBuilderǁadd_header__mutmut_32(self, project_name: str | None = None) -> None:
        """
        Add a header section to the gitignore.

        Args:
            project_name: Optional project name for the header
        """
        header_lines = [
            "# ========================",
            "# Generated by wrknv",
            f"# Date: {provide_now().strftime('%Y-%m-%d %H:%M:%S')}",
        ]

        if project_name:
            header_lines.append(f"# Project: {project_name}")

        header_lines.extend(
            [
                "# ========================",
                "",
                "# This file is auto-generated. Custom rules should be added",
                "# in the 'Custom Rules' section at the bottom to preserve them",
                "# during regeneration.",
                "",
            ]
        )

        self.sections.insert(0, ("header", "\n".join(header_lines)))
        logger.debug(None)
    
    xǁGitignoreBuilderǁadd_header__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreBuilderǁadd_header__mutmut_1': xǁGitignoreBuilderǁadd_header__mutmut_1, 
        'xǁGitignoreBuilderǁadd_header__mutmut_2': xǁGitignoreBuilderǁadd_header__mutmut_2, 
        'xǁGitignoreBuilderǁadd_header__mutmut_3': xǁGitignoreBuilderǁadd_header__mutmut_3, 
        'xǁGitignoreBuilderǁadd_header__mutmut_4': xǁGitignoreBuilderǁadd_header__mutmut_4, 
        'xǁGitignoreBuilderǁadd_header__mutmut_5': xǁGitignoreBuilderǁadd_header__mutmut_5, 
        'xǁGitignoreBuilderǁadd_header__mutmut_6': xǁGitignoreBuilderǁadd_header__mutmut_6, 
        'xǁGitignoreBuilderǁadd_header__mutmut_7': xǁGitignoreBuilderǁadd_header__mutmut_7, 
        'xǁGitignoreBuilderǁadd_header__mutmut_8': xǁGitignoreBuilderǁadd_header__mutmut_8, 
        'xǁGitignoreBuilderǁadd_header__mutmut_9': xǁGitignoreBuilderǁadd_header__mutmut_9, 
        'xǁGitignoreBuilderǁadd_header__mutmut_10': xǁGitignoreBuilderǁadd_header__mutmut_10, 
        'xǁGitignoreBuilderǁadd_header__mutmut_11': xǁGitignoreBuilderǁadd_header__mutmut_11, 
        'xǁGitignoreBuilderǁadd_header__mutmut_12': xǁGitignoreBuilderǁadd_header__mutmut_12, 
        'xǁGitignoreBuilderǁadd_header__mutmut_13': xǁGitignoreBuilderǁadd_header__mutmut_13, 
        'xǁGitignoreBuilderǁadd_header__mutmut_14': xǁGitignoreBuilderǁadd_header__mutmut_14, 
        'xǁGitignoreBuilderǁadd_header__mutmut_15': xǁGitignoreBuilderǁadd_header__mutmut_15, 
        'xǁGitignoreBuilderǁadd_header__mutmut_16': xǁGitignoreBuilderǁadd_header__mutmut_16, 
        'xǁGitignoreBuilderǁadd_header__mutmut_17': xǁGitignoreBuilderǁadd_header__mutmut_17, 
        'xǁGitignoreBuilderǁadd_header__mutmut_18': xǁGitignoreBuilderǁadd_header__mutmut_18, 
        'xǁGitignoreBuilderǁadd_header__mutmut_19': xǁGitignoreBuilderǁadd_header__mutmut_19, 
        'xǁGitignoreBuilderǁadd_header__mutmut_20': xǁGitignoreBuilderǁadd_header__mutmut_20, 
        'xǁGitignoreBuilderǁadd_header__mutmut_21': xǁGitignoreBuilderǁadd_header__mutmut_21, 
        'xǁGitignoreBuilderǁadd_header__mutmut_22': xǁGitignoreBuilderǁadd_header__mutmut_22, 
        'xǁGitignoreBuilderǁadd_header__mutmut_23': xǁGitignoreBuilderǁadd_header__mutmut_23, 
        'xǁGitignoreBuilderǁadd_header__mutmut_24': xǁGitignoreBuilderǁadd_header__mutmut_24, 
        'xǁGitignoreBuilderǁadd_header__mutmut_25': xǁGitignoreBuilderǁadd_header__mutmut_25, 
        'xǁGitignoreBuilderǁadd_header__mutmut_26': xǁGitignoreBuilderǁadd_header__mutmut_26, 
        'xǁGitignoreBuilderǁadd_header__mutmut_27': xǁGitignoreBuilderǁadd_header__mutmut_27, 
        'xǁGitignoreBuilderǁadd_header__mutmut_28': xǁGitignoreBuilderǁadd_header__mutmut_28, 
        'xǁGitignoreBuilderǁadd_header__mutmut_29': xǁGitignoreBuilderǁadd_header__mutmut_29, 
        'xǁGitignoreBuilderǁadd_header__mutmut_30': xǁGitignoreBuilderǁadd_header__mutmut_30, 
        'xǁGitignoreBuilderǁadd_header__mutmut_31': xǁGitignoreBuilderǁadd_header__mutmut_31, 
        'xǁGitignoreBuilderǁadd_header__mutmut_32': xǁGitignoreBuilderǁadd_header__mutmut_32
    }
    
    def add_header(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreBuilderǁadd_header__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreBuilderǁadd_header__mutmut_mutants"), args, kwargs, self)
        return result 
    
    add_header.__signature__ = _mutmut_signature(xǁGitignoreBuilderǁadd_header__mutmut_orig)
    xǁGitignoreBuilderǁadd_header__mutmut_orig.__name__ = 'xǁGitignoreBuilderǁadd_header'

    def xǁGitignoreBuilderǁadd_template_section__mutmut_orig(self, name: str, content: str) -> None:
        """
        Add a template section.

        Args:
            name: Template name
            content: Template content
        """
        if not content:
            logger.warning(f"Empty content for template: {name}")
            return

        section_header = f"\n# === {name} ===\n"
        section_content = content.strip()

        self.sections.append((name, section_header + section_content))
        logger.debug(f"Added template section: {name}")

    def xǁGitignoreBuilderǁadd_template_section__mutmut_1(self, name: str, content: str) -> None:
        """
        Add a template section.

        Args:
            name: Template name
            content: Template content
        """
        if content:
            logger.warning(f"Empty content for template: {name}")
            return

        section_header = f"\n# === {name} ===\n"
        section_content = content.strip()

        self.sections.append((name, section_header + section_content))
        logger.debug(f"Added template section: {name}")

    def xǁGitignoreBuilderǁadd_template_section__mutmut_2(self, name: str, content: str) -> None:
        """
        Add a template section.

        Args:
            name: Template name
            content: Template content
        """
        if not content:
            logger.warning(None)
            return

        section_header = f"\n# === {name} ===\n"
        section_content = content.strip()

        self.sections.append((name, section_header + section_content))
        logger.debug(f"Added template section: {name}")

    def xǁGitignoreBuilderǁadd_template_section__mutmut_3(self, name: str, content: str) -> None:
        """
        Add a template section.

        Args:
            name: Template name
            content: Template content
        """
        if not content:
            logger.warning(f"Empty content for template: {name}")
            return

        section_header = None
        section_content = content.strip()

        self.sections.append((name, section_header + section_content))
        logger.debug(f"Added template section: {name}")

    def xǁGitignoreBuilderǁadd_template_section__mutmut_4(self, name: str, content: str) -> None:
        """
        Add a template section.

        Args:
            name: Template name
            content: Template content
        """
        if not content:
            logger.warning(f"Empty content for template: {name}")
            return

        section_header = f"\n# === {name} ===\n"
        section_content = None

        self.sections.append((name, section_header + section_content))
        logger.debug(f"Added template section: {name}")

    def xǁGitignoreBuilderǁadd_template_section__mutmut_5(self, name: str, content: str) -> None:
        """
        Add a template section.

        Args:
            name: Template name
            content: Template content
        """
        if not content:
            logger.warning(f"Empty content for template: {name}")
            return

        section_header = f"\n# === {name} ===\n"
        section_content = content.strip()

        self.sections.append(None)
        logger.debug(f"Added template section: {name}")

    def xǁGitignoreBuilderǁadd_template_section__mutmut_6(self, name: str, content: str) -> None:
        """
        Add a template section.

        Args:
            name: Template name
            content: Template content
        """
        if not content:
            logger.warning(f"Empty content for template: {name}")
            return

        section_header = f"\n# === {name} ===\n"
        section_content = content.strip()

        self.sections.append((name, section_header - section_content))
        logger.debug(f"Added template section: {name}")

    def xǁGitignoreBuilderǁadd_template_section__mutmut_7(self, name: str, content: str) -> None:
        """
        Add a template section.

        Args:
            name: Template name
            content: Template content
        """
        if not content:
            logger.warning(f"Empty content for template: {name}")
            return

        section_header = f"\n# === {name} ===\n"
        section_content = content.strip()

        self.sections.append((name, section_header + section_content))
        logger.debug(None)
    
    xǁGitignoreBuilderǁadd_template_section__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreBuilderǁadd_template_section__mutmut_1': xǁGitignoreBuilderǁadd_template_section__mutmut_1, 
        'xǁGitignoreBuilderǁadd_template_section__mutmut_2': xǁGitignoreBuilderǁadd_template_section__mutmut_2, 
        'xǁGitignoreBuilderǁadd_template_section__mutmut_3': xǁGitignoreBuilderǁadd_template_section__mutmut_3, 
        'xǁGitignoreBuilderǁadd_template_section__mutmut_4': xǁGitignoreBuilderǁadd_template_section__mutmut_4, 
        'xǁGitignoreBuilderǁadd_template_section__mutmut_5': xǁGitignoreBuilderǁadd_template_section__mutmut_5, 
        'xǁGitignoreBuilderǁadd_template_section__mutmut_6': xǁGitignoreBuilderǁadd_template_section__mutmut_6, 
        'xǁGitignoreBuilderǁadd_template_section__mutmut_7': xǁGitignoreBuilderǁadd_template_section__mutmut_7
    }
    
    def add_template_section(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreBuilderǁadd_template_section__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreBuilderǁadd_template_section__mutmut_mutants"), args, kwargs, self)
        return result 
    
    add_template_section.__signature__ = _mutmut_signature(xǁGitignoreBuilderǁadd_template_section__mutmut_orig)
    xǁGitignoreBuilderǁadd_template_section__mutmut_orig.__name__ = 'xǁGitignoreBuilderǁadd_template_section'

    def xǁGitignoreBuilderǁ_build_section_content__mutmut_orig(self, section_name: str, patterns: dict[str, list[str]]) -> str:
        """Build section content from pattern dictionary.

        Args:
            section_name: Name of the section (e.g., "wrknv", "Provide Ecosystem")
            patterns: Dictionary mapping category names to lists of patterns

        Returns:
            Formatted section content string
        """
        lines = ["", f"# === {section_name} ==="]
        for category, items in patterns.items():
            lines.append(f"# {category}")
            lines.extend(items)
            lines.append("")
        return "\n".join(lines)

    def xǁGitignoreBuilderǁ_build_section_content__mutmut_1(self, section_name: str, patterns: dict[str, list[str]]) -> str:
        """Build section content from pattern dictionary.

        Args:
            section_name: Name of the section (e.g., "wrknv", "Provide Ecosystem")
            patterns: Dictionary mapping category names to lists of patterns

        Returns:
            Formatted section content string
        """
        lines = None
        for category, items in patterns.items():
            lines.append(f"# {category}")
            lines.extend(items)
            lines.append("")
        return "\n".join(lines)

    def xǁGitignoreBuilderǁ_build_section_content__mutmut_2(self, section_name: str, patterns: dict[str, list[str]]) -> str:
        """Build section content from pattern dictionary.

        Args:
            section_name: Name of the section (e.g., "wrknv", "Provide Ecosystem")
            patterns: Dictionary mapping category names to lists of patterns

        Returns:
            Formatted section content string
        """
        lines = ["XXXX", f"# === {section_name} ==="]
        for category, items in patterns.items():
            lines.append(f"# {category}")
            lines.extend(items)
            lines.append("")
        return "\n".join(lines)

    def xǁGitignoreBuilderǁ_build_section_content__mutmut_3(self, section_name: str, patterns: dict[str, list[str]]) -> str:
        """Build section content from pattern dictionary.

        Args:
            section_name: Name of the section (e.g., "wrknv", "Provide Ecosystem")
            patterns: Dictionary mapping category names to lists of patterns

        Returns:
            Formatted section content string
        """
        lines = ["", f"# === {section_name} ==="]
        for category, items in patterns.items():
            lines.append(None)
            lines.extend(items)
            lines.append("")
        return "\n".join(lines)

    def xǁGitignoreBuilderǁ_build_section_content__mutmut_4(self, section_name: str, patterns: dict[str, list[str]]) -> str:
        """Build section content from pattern dictionary.

        Args:
            section_name: Name of the section (e.g., "wrknv", "Provide Ecosystem")
            patterns: Dictionary mapping category names to lists of patterns

        Returns:
            Formatted section content string
        """
        lines = ["", f"# === {section_name} ==="]
        for category, items in patterns.items():
            lines.append(f"# {category}")
            lines.extend(None)
            lines.append("")
        return "\n".join(lines)

    def xǁGitignoreBuilderǁ_build_section_content__mutmut_5(self, section_name: str, patterns: dict[str, list[str]]) -> str:
        """Build section content from pattern dictionary.

        Args:
            section_name: Name of the section (e.g., "wrknv", "Provide Ecosystem")
            patterns: Dictionary mapping category names to lists of patterns

        Returns:
            Formatted section content string
        """
        lines = ["", f"# === {section_name} ==="]
        for category, items in patterns.items():
            lines.append(f"# {category}")
            lines.extend(items)
            lines.append(None)
        return "\n".join(lines)

    def xǁGitignoreBuilderǁ_build_section_content__mutmut_6(self, section_name: str, patterns: dict[str, list[str]]) -> str:
        """Build section content from pattern dictionary.

        Args:
            section_name: Name of the section (e.g., "wrknv", "Provide Ecosystem")
            patterns: Dictionary mapping category names to lists of patterns

        Returns:
            Formatted section content string
        """
        lines = ["", f"# === {section_name} ==="]
        for category, items in patterns.items():
            lines.append(f"# {category}")
            lines.extend(items)
            lines.append("XXXX")
        return "\n".join(lines)

    def xǁGitignoreBuilderǁ_build_section_content__mutmut_7(self, section_name: str, patterns: dict[str, list[str]]) -> str:
        """Build section content from pattern dictionary.

        Args:
            section_name: Name of the section (e.g., "wrknv", "Provide Ecosystem")
            patterns: Dictionary mapping category names to lists of patterns

        Returns:
            Formatted section content string
        """
        lines = ["", f"# === {section_name} ==="]
        for category, items in patterns.items():
            lines.append(f"# {category}")
            lines.extend(items)
            lines.append("")
        return "\n".join(None)

    def xǁGitignoreBuilderǁ_build_section_content__mutmut_8(self, section_name: str, patterns: dict[str, list[str]]) -> str:
        """Build section content from pattern dictionary.

        Args:
            section_name: Name of the section (e.g., "wrknv", "Provide Ecosystem")
            patterns: Dictionary mapping category names to lists of patterns

        Returns:
            Formatted section content string
        """
        lines = ["", f"# === {section_name} ==="]
        for category, items in patterns.items():
            lines.append(f"# {category}")
            lines.extend(items)
            lines.append("")
        return "XX\nXX".join(lines)
    
    xǁGitignoreBuilderǁ_build_section_content__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreBuilderǁ_build_section_content__mutmut_1': xǁGitignoreBuilderǁ_build_section_content__mutmut_1, 
        'xǁGitignoreBuilderǁ_build_section_content__mutmut_2': xǁGitignoreBuilderǁ_build_section_content__mutmut_2, 
        'xǁGitignoreBuilderǁ_build_section_content__mutmut_3': xǁGitignoreBuilderǁ_build_section_content__mutmut_3, 
        'xǁGitignoreBuilderǁ_build_section_content__mutmut_4': xǁGitignoreBuilderǁ_build_section_content__mutmut_4, 
        'xǁGitignoreBuilderǁ_build_section_content__mutmut_5': xǁGitignoreBuilderǁ_build_section_content__mutmut_5, 
        'xǁGitignoreBuilderǁ_build_section_content__mutmut_6': xǁGitignoreBuilderǁ_build_section_content__mutmut_6, 
        'xǁGitignoreBuilderǁ_build_section_content__mutmut_7': xǁGitignoreBuilderǁ_build_section_content__mutmut_7, 
        'xǁGitignoreBuilderǁ_build_section_content__mutmut_8': xǁGitignoreBuilderǁ_build_section_content__mutmut_8
    }
    
    def _build_section_content(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreBuilderǁ_build_section_content__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreBuilderǁ_build_section_content__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _build_section_content.__signature__ = _mutmut_signature(xǁGitignoreBuilderǁ_build_section_content__mutmut_orig)
    xǁGitignoreBuilderǁ_build_section_content__mutmut_orig.__name__ = 'xǁGitignoreBuilderǁ_build_section_content'

    def xǁGitignoreBuilderǁadd_wrknv_section__mutmut_orig(self) -> None:
        """Add wrknv-specific ignore patterns."""
        content = self._build_section_content("wrknv", WRKNV_PATTERNS)
        self.sections.append(("wrknv", content))
        logger.debug("Added wrknv-specific patterns")

    def xǁGitignoreBuilderǁadd_wrknv_section__mutmut_1(self) -> None:
        """Add wrknv-specific ignore patterns."""
        content = None
        self.sections.append(("wrknv", content))
        logger.debug("Added wrknv-specific patterns")

    def xǁGitignoreBuilderǁadd_wrknv_section__mutmut_2(self) -> None:
        """Add wrknv-specific ignore patterns."""
        content = self._build_section_content(None, WRKNV_PATTERNS)
        self.sections.append(("wrknv", content))
        logger.debug("Added wrknv-specific patterns")

    def xǁGitignoreBuilderǁadd_wrknv_section__mutmut_3(self) -> None:
        """Add wrknv-specific ignore patterns."""
        content = self._build_section_content("wrknv", None)
        self.sections.append(("wrknv", content))
        logger.debug("Added wrknv-specific patterns")

    def xǁGitignoreBuilderǁadd_wrknv_section__mutmut_4(self) -> None:
        """Add wrknv-specific ignore patterns."""
        content = self._build_section_content(WRKNV_PATTERNS)
        self.sections.append(("wrknv", content))
        logger.debug("Added wrknv-specific patterns")

    def xǁGitignoreBuilderǁadd_wrknv_section__mutmut_5(self) -> None:
        """Add wrknv-specific ignore patterns."""
        content = self._build_section_content("wrknv", )
        self.sections.append(("wrknv", content))
        logger.debug("Added wrknv-specific patterns")

    def xǁGitignoreBuilderǁadd_wrknv_section__mutmut_6(self) -> None:
        """Add wrknv-specific ignore patterns."""
        content = self._build_section_content("XXwrknvXX", WRKNV_PATTERNS)
        self.sections.append(("wrknv", content))
        logger.debug("Added wrknv-specific patterns")

    def xǁGitignoreBuilderǁadd_wrknv_section__mutmut_7(self) -> None:
        """Add wrknv-specific ignore patterns."""
        content = self._build_section_content("WRKNV", WRKNV_PATTERNS)
        self.sections.append(("wrknv", content))
        logger.debug("Added wrknv-specific patterns")

    def xǁGitignoreBuilderǁadd_wrknv_section__mutmut_8(self) -> None:
        """Add wrknv-specific ignore patterns."""
        content = self._build_section_content("wrknv", WRKNV_PATTERNS)
        self.sections.append(None)
        logger.debug("Added wrknv-specific patterns")

    def xǁGitignoreBuilderǁadd_wrknv_section__mutmut_9(self) -> None:
        """Add wrknv-specific ignore patterns."""
        content = self._build_section_content("wrknv", WRKNV_PATTERNS)
        self.sections.append(("XXwrknvXX", content))
        logger.debug("Added wrknv-specific patterns")

    def xǁGitignoreBuilderǁadd_wrknv_section__mutmut_10(self) -> None:
        """Add wrknv-specific ignore patterns."""
        content = self._build_section_content("wrknv", WRKNV_PATTERNS)
        self.sections.append(("WRKNV", content))
        logger.debug("Added wrknv-specific patterns")

    def xǁGitignoreBuilderǁadd_wrknv_section__mutmut_11(self) -> None:
        """Add wrknv-specific ignore patterns."""
        content = self._build_section_content("wrknv", WRKNV_PATTERNS)
        self.sections.append(("wrknv", content))
        logger.debug(None)

    def xǁGitignoreBuilderǁadd_wrknv_section__mutmut_12(self) -> None:
        """Add wrknv-specific ignore patterns."""
        content = self._build_section_content("wrknv", WRKNV_PATTERNS)
        self.sections.append(("wrknv", content))
        logger.debug("XXAdded wrknv-specific patternsXX")

    def xǁGitignoreBuilderǁadd_wrknv_section__mutmut_13(self) -> None:
        """Add wrknv-specific ignore patterns."""
        content = self._build_section_content("wrknv", WRKNV_PATTERNS)
        self.sections.append(("wrknv", content))
        logger.debug("added wrknv-specific patterns")

    def xǁGitignoreBuilderǁadd_wrknv_section__mutmut_14(self) -> None:
        """Add wrknv-specific ignore patterns."""
        content = self._build_section_content("wrknv", WRKNV_PATTERNS)
        self.sections.append(("wrknv", content))
        logger.debug("ADDED WRKNV-SPECIFIC PATTERNS")
    
    xǁGitignoreBuilderǁadd_wrknv_section__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreBuilderǁadd_wrknv_section__mutmut_1': xǁGitignoreBuilderǁadd_wrknv_section__mutmut_1, 
        'xǁGitignoreBuilderǁadd_wrknv_section__mutmut_2': xǁGitignoreBuilderǁadd_wrknv_section__mutmut_2, 
        'xǁGitignoreBuilderǁadd_wrknv_section__mutmut_3': xǁGitignoreBuilderǁadd_wrknv_section__mutmut_3, 
        'xǁGitignoreBuilderǁadd_wrknv_section__mutmut_4': xǁGitignoreBuilderǁadd_wrknv_section__mutmut_4, 
        'xǁGitignoreBuilderǁadd_wrknv_section__mutmut_5': xǁGitignoreBuilderǁadd_wrknv_section__mutmut_5, 
        'xǁGitignoreBuilderǁadd_wrknv_section__mutmut_6': xǁGitignoreBuilderǁadd_wrknv_section__mutmut_6, 
        'xǁGitignoreBuilderǁadd_wrknv_section__mutmut_7': xǁGitignoreBuilderǁadd_wrknv_section__mutmut_7, 
        'xǁGitignoreBuilderǁadd_wrknv_section__mutmut_8': xǁGitignoreBuilderǁadd_wrknv_section__mutmut_8, 
        'xǁGitignoreBuilderǁadd_wrknv_section__mutmut_9': xǁGitignoreBuilderǁadd_wrknv_section__mutmut_9, 
        'xǁGitignoreBuilderǁadd_wrknv_section__mutmut_10': xǁGitignoreBuilderǁadd_wrknv_section__mutmut_10, 
        'xǁGitignoreBuilderǁadd_wrknv_section__mutmut_11': xǁGitignoreBuilderǁadd_wrknv_section__mutmut_11, 
        'xǁGitignoreBuilderǁadd_wrknv_section__mutmut_12': xǁGitignoreBuilderǁadd_wrknv_section__mutmut_12, 
        'xǁGitignoreBuilderǁadd_wrknv_section__mutmut_13': xǁGitignoreBuilderǁadd_wrknv_section__mutmut_13, 
        'xǁGitignoreBuilderǁadd_wrknv_section__mutmut_14': xǁGitignoreBuilderǁadd_wrknv_section__mutmut_14
    }
    
    def add_wrknv_section(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreBuilderǁadd_wrknv_section__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreBuilderǁadd_wrknv_section__mutmut_mutants"), args, kwargs, self)
        return result 
    
    add_wrknv_section.__signature__ = _mutmut_signature(xǁGitignoreBuilderǁadd_wrknv_section__mutmut_orig)
    xǁGitignoreBuilderǁadd_wrknv_section__mutmut_orig.__name__ = 'xǁGitignoreBuilderǁadd_wrknv_section'

    def xǁGitignoreBuilderǁadd_provide_section__mutmut_orig(self) -> None:
        """Add provide ecosystem ignore patterns."""
        content = self._build_section_content("Provide Ecosystem", PROVIDE_PATTERNS)
        self.sections.append(("provide", content))
        logger.debug("Added provide ecosystem patterns")

    def xǁGitignoreBuilderǁadd_provide_section__mutmut_1(self) -> None:
        """Add provide ecosystem ignore patterns."""
        content = None
        self.sections.append(("provide", content))
        logger.debug("Added provide ecosystem patterns")

    def xǁGitignoreBuilderǁadd_provide_section__mutmut_2(self) -> None:
        """Add provide ecosystem ignore patterns."""
        content = self._build_section_content(None, PROVIDE_PATTERNS)
        self.sections.append(("provide", content))
        logger.debug("Added provide ecosystem patterns")

    def xǁGitignoreBuilderǁadd_provide_section__mutmut_3(self) -> None:
        """Add provide ecosystem ignore patterns."""
        content = self._build_section_content("Provide Ecosystem", None)
        self.sections.append(("provide", content))
        logger.debug("Added provide ecosystem patterns")

    def xǁGitignoreBuilderǁadd_provide_section__mutmut_4(self) -> None:
        """Add provide ecosystem ignore patterns."""
        content = self._build_section_content(PROVIDE_PATTERNS)
        self.sections.append(("provide", content))
        logger.debug("Added provide ecosystem patterns")

    def xǁGitignoreBuilderǁadd_provide_section__mutmut_5(self) -> None:
        """Add provide ecosystem ignore patterns."""
        content = self._build_section_content("Provide Ecosystem", )
        self.sections.append(("provide", content))
        logger.debug("Added provide ecosystem patterns")

    def xǁGitignoreBuilderǁadd_provide_section__mutmut_6(self) -> None:
        """Add provide ecosystem ignore patterns."""
        content = self._build_section_content("XXProvide EcosystemXX", PROVIDE_PATTERNS)
        self.sections.append(("provide", content))
        logger.debug("Added provide ecosystem patterns")

    def xǁGitignoreBuilderǁadd_provide_section__mutmut_7(self) -> None:
        """Add provide ecosystem ignore patterns."""
        content = self._build_section_content("provide ecosystem", PROVIDE_PATTERNS)
        self.sections.append(("provide", content))
        logger.debug("Added provide ecosystem patterns")

    def xǁGitignoreBuilderǁadd_provide_section__mutmut_8(self) -> None:
        """Add provide ecosystem ignore patterns."""
        content = self._build_section_content("PROVIDE ECOSYSTEM", PROVIDE_PATTERNS)
        self.sections.append(("provide", content))
        logger.debug("Added provide ecosystem patterns")

    def xǁGitignoreBuilderǁadd_provide_section__mutmut_9(self) -> None:
        """Add provide ecosystem ignore patterns."""
        content = self._build_section_content("Provide Ecosystem", PROVIDE_PATTERNS)
        self.sections.append(None)
        logger.debug("Added provide ecosystem patterns")

    def xǁGitignoreBuilderǁadd_provide_section__mutmut_10(self) -> None:
        """Add provide ecosystem ignore patterns."""
        content = self._build_section_content("Provide Ecosystem", PROVIDE_PATTERNS)
        self.sections.append(("XXprovideXX", content))
        logger.debug("Added provide ecosystem patterns")

    def xǁGitignoreBuilderǁadd_provide_section__mutmut_11(self) -> None:
        """Add provide ecosystem ignore patterns."""
        content = self._build_section_content("Provide Ecosystem", PROVIDE_PATTERNS)
        self.sections.append(("PROVIDE", content))
        logger.debug("Added provide ecosystem patterns")

    def xǁGitignoreBuilderǁadd_provide_section__mutmut_12(self) -> None:
        """Add provide ecosystem ignore patterns."""
        content = self._build_section_content("Provide Ecosystem", PROVIDE_PATTERNS)
        self.sections.append(("provide", content))
        logger.debug(None)

    def xǁGitignoreBuilderǁadd_provide_section__mutmut_13(self) -> None:
        """Add provide ecosystem ignore patterns."""
        content = self._build_section_content("Provide Ecosystem", PROVIDE_PATTERNS)
        self.sections.append(("provide", content))
        logger.debug("XXAdded provide ecosystem patternsXX")

    def xǁGitignoreBuilderǁadd_provide_section__mutmut_14(self) -> None:
        """Add provide ecosystem ignore patterns."""
        content = self._build_section_content("Provide Ecosystem", PROVIDE_PATTERNS)
        self.sections.append(("provide", content))
        logger.debug("added provide ecosystem patterns")

    def xǁGitignoreBuilderǁadd_provide_section__mutmut_15(self) -> None:
        """Add provide ecosystem ignore patterns."""
        content = self._build_section_content("Provide Ecosystem", PROVIDE_PATTERNS)
        self.sections.append(("provide", content))
        logger.debug("ADDED PROVIDE ECOSYSTEM PATTERNS")
    
    xǁGitignoreBuilderǁadd_provide_section__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreBuilderǁadd_provide_section__mutmut_1': xǁGitignoreBuilderǁadd_provide_section__mutmut_1, 
        'xǁGitignoreBuilderǁadd_provide_section__mutmut_2': xǁGitignoreBuilderǁadd_provide_section__mutmut_2, 
        'xǁGitignoreBuilderǁadd_provide_section__mutmut_3': xǁGitignoreBuilderǁadd_provide_section__mutmut_3, 
        'xǁGitignoreBuilderǁadd_provide_section__mutmut_4': xǁGitignoreBuilderǁadd_provide_section__mutmut_4, 
        'xǁGitignoreBuilderǁadd_provide_section__mutmut_5': xǁGitignoreBuilderǁadd_provide_section__mutmut_5, 
        'xǁGitignoreBuilderǁadd_provide_section__mutmut_6': xǁGitignoreBuilderǁadd_provide_section__mutmut_6, 
        'xǁGitignoreBuilderǁadd_provide_section__mutmut_7': xǁGitignoreBuilderǁadd_provide_section__mutmut_7, 
        'xǁGitignoreBuilderǁadd_provide_section__mutmut_8': xǁGitignoreBuilderǁadd_provide_section__mutmut_8, 
        'xǁGitignoreBuilderǁadd_provide_section__mutmut_9': xǁGitignoreBuilderǁadd_provide_section__mutmut_9, 
        'xǁGitignoreBuilderǁadd_provide_section__mutmut_10': xǁGitignoreBuilderǁadd_provide_section__mutmut_10, 
        'xǁGitignoreBuilderǁadd_provide_section__mutmut_11': xǁGitignoreBuilderǁadd_provide_section__mutmut_11, 
        'xǁGitignoreBuilderǁadd_provide_section__mutmut_12': xǁGitignoreBuilderǁadd_provide_section__mutmut_12, 
        'xǁGitignoreBuilderǁadd_provide_section__mutmut_13': xǁGitignoreBuilderǁadd_provide_section__mutmut_13, 
        'xǁGitignoreBuilderǁadd_provide_section__mutmut_14': xǁGitignoreBuilderǁadd_provide_section__mutmut_14, 
        'xǁGitignoreBuilderǁadd_provide_section__mutmut_15': xǁGitignoreBuilderǁadd_provide_section__mutmut_15
    }
    
    def add_provide_section(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreBuilderǁadd_provide_section__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreBuilderǁadd_provide_section__mutmut_mutants"), args, kwargs, self)
        return result 
    
    add_provide_section.__signature__ = _mutmut_signature(xǁGitignoreBuilderǁadd_provide_section__mutmut_orig)
    xǁGitignoreBuilderǁadd_provide_section__mutmut_orig.__name__ = 'xǁGitignoreBuilderǁadd_provide_section'

    def xǁGitignoreBuilderǁadd_custom_rules__mutmut_orig(self, rules: list[str]) -> None:
        """
        Add custom rules.

        Args:
            rules: List of custom ignore patterns
        """
        if not rules:
            return

        self.custom_rules.extend(rules)
        logger.debug(f"Added {len(rules)} custom rules")

    def xǁGitignoreBuilderǁadd_custom_rules__mutmut_1(self, rules: list[str]) -> None:
        """
        Add custom rules.

        Args:
            rules: List of custom ignore patterns
        """
        if rules:
            return

        self.custom_rules.extend(rules)
        logger.debug(f"Added {len(rules)} custom rules")

    def xǁGitignoreBuilderǁadd_custom_rules__mutmut_2(self, rules: list[str]) -> None:
        """
        Add custom rules.

        Args:
            rules: List of custom ignore patterns
        """
        if not rules:
            return

        self.custom_rules.extend(None)
        logger.debug(f"Added {len(rules)} custom rules")

    def xǁGitignoreBuilderǁadd_custom_rules__mutmut_3(self, rules: list[str]) -> None:
        """
        Add custom rules.

        Args:
            rules: List of custom ignore patterns
        """
        if not rules:
            return

        self.custom_rules.extend(rules)
        logger.debug(None)
    
    xǁGitignoreBuilderǁadd_custom_rules__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreBuilderǁadd_custom_rules__mutmut_1': xǁGitignoreBuilderǁadd_custom_rules__mutmut_1, 
        'xǁGitignoreBuilderǁadd_custom_rules__mutmut_2': xǁGitignoreBuilderǁadd_custom_rules__mutmut_2, 
        'xǁGitignoreBuilderǁadd_custom_rules__mutmut_3': xǁGitignoreBuilderǁadd_custom_rules__mutmut_3
    }
    
    def add_custom_rules(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreBuilderǁadd_custom_rules__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreBuilderǁadd_custom_rules__mutmut_mutants"), args, kwargs, self)
        return result 
    
    add_custom_rules.__signature__ = _mutmut_signature(xǁGitignoreBuilderǁadd_custom_rules__mutmut_orig)
    xǁGitignoreBuilderǁadd_custom_rules__mutmut_orig.__name__ = 'xǁGitignoreBuilderǁadd_custom_rules'

    def xǁGitignoreBuilderǁbuild__mutmut_orig(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_1(self, merge_duplicates: bool = False) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_2(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info(None)

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_3(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("XXBuilding gitignore fileXX")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_4(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_5(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("BUILDING GITIGNORE FILE")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_6(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = None
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_7(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = None

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_8(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates or section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_9(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name == "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_10(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "XXheaderXX":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_11(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "HEADER":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_12(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = None
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_13(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split(None):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_14(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("XX\nXX"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_15(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = None
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_16(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped or not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_17(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_18(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith(None):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_19(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("XX#XX"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_20(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_21(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(None)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_22(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(None)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_23(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(None)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_24(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append(None)
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_25(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(None))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_26(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("XX\nXX".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_27(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(None)
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_28(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(None)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_29(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(None)

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_30(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = None

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_31(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "XXXX",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_32(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "XX# === Custom Rules ===XX",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_33(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === custom rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_34(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === CUSTOM RULES ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_35(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "XX# Add your project-specific patterns hereXX",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_36(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_37(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# ADD YOUR PROJECT-SPECIFIC PATTERNS HERE",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_38(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates and rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_39(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_40(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_41(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(None)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_42(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() or not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_43(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates or rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_44(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_45(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith(None):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_46(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("XX#XX"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_47(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(None)

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_48(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append(None)
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_49(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(None))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_50(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("XX\nXX".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_51(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(None)

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_52(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = None

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_53(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(None)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_54(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "XX\n\nXX".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_55(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if result.endswith("\n"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_56(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith(None):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_57(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("XX\nXX"):
            result += "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_58(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result = "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_59(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result -= "\n"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_60(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "XX\nXX"

        logger.info(f"Built gitignore with {len(seen_patterns)} unique patterns")
        return result

    def xǁGitignoreBuilderǁbuild__mutmut_61(self, merge_duplicates: bool = True) -> str:
        """
        Build the final gitignore content.

        Args:
            merge_duplicates: Whether to remove duplicate patterns

        Returns:
            Complete gitignore file content
        """
        logger.info("Building gitignore file")

        all_lines = []
        seen_patterns = set()

        # Process all sections
        for section_name, section_content in self.sections:
            if merge_duplicates and section_name != "header":
                # Filter out duplicate patterns
                filtered_lines = []
                for line in section_content.split("\n"):
                    # Skip empty lines and comments for deduplication
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        if stripped not in seen_patterns:
                            seen_patterns.add(stripped)
                            filtered_lines.append(line)
                    else:
                        filtered_lines.append(line)

                if filtered_lines:
                    all_lines.append("\n".join(filtered_lines))
                    logger.debug(f"Added section {section_name} with {len(filtered_lines)} lines")
            else:
                all_lines.append(section_content)
                logger.debug(f"Added section {section_name} without deduplication")

        # Add custom rules section if we have any
        if self.custom_rules:
            custom_section = [
                "",
                "# === Custom Rules ===",
                "# Add your project-specific patterns here",
            ]

            for rule in self.custom_rules:
                # Check for duplicates in custom rules too
                if not merge_duplicates or rule.strip() not in seen_patterns:
                    custom_section.append(rule)
                    if merge_duplicates and rule.strip() and not rule.strip().startswith("#"):
                        seen_patterns.add(rule.strip())

            all_lines.append("\n".join(custom_section))
            logger.debug(f"Added {len(self.custom_rules)} custom rules")

        # Join all sections with double newlines
        result = "\n\n".join(all_lines)

        # Ensure file ends with newline
        if not result.endswith("\n"):
            result += "\n"

        logger.info(None)
        return result
    
    xǁGitignoreBuilderǁbuild__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreBuilderǁbuild__mutmut_1': xǁGitignoreBuilderǁbuild__mutmut_1, 
        'xǁGitignoreBuilderǁbuild__mutmut_2': xǁGitignoreBuilderǁbuild__mutmut_2, 
        'xǁGitignoreBuilderǁbuild__mutmut_3': xǁGitignoreBuilderǁbuild__mutmut_3, 
        'xǁGitignoreBuilderǁbuild__mutmut_4': xǁGitignoreBuilderǁbuild__mutmut_4, 
        'xǁGitignoreBuilderǁbuild__mutmut_5': xǁGitignoreBuilderǁbuild__mutmut_5, 
        'xǁGitignoreBuilderǁbuild__mutmut_6': xǁGitignoreBuilderǁbuild__mutmut_6, 
        'xǁGitignoreBuilderǁbuild__mutmut_7': xǁGitignoreBuilderǁbuild__mutmut_7, 
        'xǁGitignoreBuilderǁbuild__mutmut_8': xǁGitignoreBuilderǁbuild__mutmut_8, 
        'xǁGitignoreBuilderǁbuild__mutmut_9': xǁGitignoreBuilderǁbuild__mutmut_9, 
        'xǁGitignoreBuilderǁbuild__mutmut_10': xǁGitignoreBuilderǁbuild__mutmut_10, 
        'xǁGitignoreBuilderǁbuild__mutmut_11': xǁGitignoreBuilderǁbuild__mutmut_11, 
        'xǁGitignoreBuilderǁbuild__mutmut_12': xǁGitignoreBuilderǁbuild__mutmut_12, 
        'xǁGitignoreBuilderǁbuild__mutmut_13': xǁGitignoreBuilderǁbuild__mutmut_13, 
        'xǁGitignoreBuilderǁbuild__mutmut_14': xǁGitignoreBuilderǁbuild__mutmut_14, 
        'xǁGitignoreBuilderǁbuild__mutmut_15': xǁGitignoreBuilderǁbuild__mutmut_15, 
        'xǁGitignoreBuilderǁbuild__mutmut_16': xǁGitignoreBuilderǁbuild__mutmut_16, 
        'xǁGitignoreBuilderǁbuild__mutmut_17': xǁGitignoreBuilderǁbuild__mutmut_17, 
        'xǁGitignoreBuilderǁbuild__mutmut_18': xǁGitignoreBuilderǁbuild__mutmut_18, 
        'xǁGitignoreBuilderǁbuild__mutmut_19': xǁGitignoreBuilderǁbuild__mutmut_19, 
        'xǁGitignoreBuilderǁbuild__mutmut_20': xǁGitignoreBuilderǁbuild__mutmut_20, 
        'xǁGitignoreBuilderǁbuild__mutmut_21': xǁGitignoreBuilderǁbuild__mutmut_21, 
        'xǁGitignoreBuilderǁbuild__mutmut_22': xǁGitignoreBuilderǁbuild__mutmut_22, 
        'xǁGitignoreBuilderǁbuild__mutmut_23': xǁGitignoreBuilderǁbuild__mutmut_23, 
        'xǁGitignoreBuilderǁbuild__mutmut_24': xǁGitignoreBuilderǁbuild__mutmut_24, 
        'xǁGitignoreBuilderǁbuild__mutmut_25': xǁGitignoreBuilderǁbuild__mutmut_25, 
        'xǁGitignoreBuilderǁbuild__mutmut_26': xǁGitignoreBuilderǁbuild__mutmut_26, 
        'xǁGitignoreBuilderǁbuild__mutmut_27': xǁGitignoreBuilderǁbuild__mutmut_27, 
        'xǁGitignoreBuilderǁbuild__mutmut_28': xǁGitignoreBuilderǁbuild__mutmut_28, 
        'xǁGitignoreBuilderǁbuild__mutmut_29': xǁGitignoreBuilderǁbuild__mutmut_29, 
        'xǁGitignoreBuilderǁbuild__mutmut_30': xǁGitignoreBuilderǁbuild__mutmut_30, 
        'xǁGitignoreBuilderǁbuild__mutmut_31': xǁGitignoreBuilderǁbuild__mutmut_31, 
        'xǁGitignoreBuilderǁbuild__mutmut_32': xǁGitignoreBuilderǁbuild__mutmut_32, 
        'xǁGitignoreBuilderǁbuild__mutmut_33': xǁGitignoreBuilderǁbuild__mutmut_33, 
        'xǁGitignoreBuilderǁbuild__mutmut_34': xǁGitignoreBuilderǁbuild__mutmut_34, 
        'xǁGitignoreBuilderǁbuild__mutmut_35': xǁGitignoreBuilderǁbuild__mutmut_35, 
        'xǁGitignoreBuilderǁbuild__mutmut_36': xǁGitignoreBuilderǁbuild__mutmut_36, 
        'xǁGitignoreBuilderǁbuild__mutmut_37': xǁGitignoreBuilderǁbuild__mutmut_37, 
        'xǁGitignoreBuilderǁbuild__mutmut_38': xǁGitignoreBuilderǁbuild__mutmut_38, 
        'xǁGitignoreBuilderǁbuild__mutmut_39': xǁGitignoreBuilderǁbuild__mutmut_39, 
        'xǁGitignoreBuilderǁbuild__mutmut_40': xǁGitignoreBuilderǁbuild__mutmut_40, 
        'xǁGitignoreBuilderǁbuild__mutmut_41': xǁGitignoreBuilderǁbuild__mutmut_41, 
        'xǁGitignoreBuilderǁbuild__mutmut_42': xǁGitignoreBuilderǁbuild__mutmut_42, 
        'xǁGitignoreBuilderǁbuild__mutmut_43': xǁGitignoreBuilderǁbuild__mutmut_43, 
        'xǁGitignoreBuilderǁbuild__mutmut_44': xǁGitignoreBuilderǁbuild__mutmut_44, 
        'xǁGitignoreBuilderǁbuild__mutmut_45': xǁGitignoreBuilderǁbuild__mutmut_45, 
        'xǁGitignoreBuilderǁbuild__mutmut_46': xǁGitignoreBuilderǁbuild__mutmut_46, 
        'xǁGitignoreBuilderǁbuild__mutmut_47': xǁGitignoreBuilderǁbuild__mutmut_47, 
        'xǁGitignoreBuilderǁbuild__mutmut_48': xǁGitignoreBuilderǁbuild__mutmut_48, 
        'xǁGitignoreBuilderǁbuild__mutmut_49': xǁGitignoreBuilderǁbuild__mutmut_49, 
        'xǁGitignoreBuilderǁbuild__mutmut_50': xǁGitignoreBuilderǁbuild__mutmut_50, 
        'xǁGitignoreBuilderǁbuild__mutmut_51': xǁGitignoreBuilderǁbuild__mutmut_51, 
        'xǁGitignoreBuilderǁbuild__mutmut_52': xǁGitignoreBuilderǁbuild__mutmut_52, 
        'xǁGitignoreBuilderǁbuild__mutmut_53': xǁGitignoreBuilderǁbuild__mutmut_53, 
        'xǁGitignoreBuilderǁbuild__mutmut_54': xǁGitignoreBuilderǁbuild__mutmut_54, 
        'xǁGitignoreBuilderǁbuild__mutmut_55': xǁGitignoreBuilderǁbuild__mutmut_55, 
        'xǁGitignoreBuilderǁbuild__mutmut_56': xǁGitignoreBuilderǁbuild__mutmut_56, 
        'xǁGitignoreBuilderǁbuild__mutmut_57': xǁGitignoreBuilderǁbuild__mutmut_57, 
        'xǁGitignoreBuilderǁbuild__mutmut_58': xǁGitignoreBuilderǁbuild__mutmut_58, 
        'xǁGitignoreBuilderǁbuild__mutmut_59': xǁGitignoreBuilderǁbuild__mutmut_59, 
        'xǁGitignoreBuilderǁbuild__mutmut_60': xǁGitignoreBuilderǁbuild__mutmut_60, 
        'xǁGitignoreBuilderǁbuild__mutmut_61': xǁGitignoreBuilderǁbuild__mutmut_61
    }
    
    def build(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreBuilderǁbuild__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreBuilderǁbuild__mutmut_mutants"), args, kwargs, self)
        return result 
    
    build.__signature__ = _mutmut_signature(xǁGitignoreBuilderǁbuild__mutmut_orig)
    xǁGitignoreBuilderǁbuild__mutmut_orig.__name__ = 'xǁGitignoreBuilderǁbuild'

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_orig(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_1(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_2(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(None)
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_3(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(None)

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_4(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = None

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_5(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = None
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_6(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = None

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_7(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = True

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_8(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split(None):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_9(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("XX\nXX"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_10(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line and "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_11(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "XX=== Custom Rules ===XX" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_12(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== custom rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_13(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== CUSTOM RULES ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_14(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" not in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_15(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "XX# CustomXX" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_16(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_17(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# CUSTOM" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_18(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" not in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_19(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = None
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_20(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = False
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_21(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                break
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_22(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section or line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_23(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith(None):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_24(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("XX# ===XX"):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_25(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                return
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_26(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section or line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_27(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(None)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_28(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(None)
            self.add_custom_rules(custom_rules)

        return self.build()

    def xǁGitignoreBuilderǁmerge_with_existing__mutmut_29(self, existing_path: Path) -> str:
        """
        Merge with an existing gitignore file, preserving custom rules.

        Args:
            existing_path: Path to existing gitignore file

        Returns:
            Merged gitignore content
        """
        if not existing_path.exists():
            logger.debug(f"No existing file at {existing_path}")
            return self.build()

        logger.info(f"Merging with existing gitignore at {existing_path}")

        existing_content = existing_path.read_text()

        # Try to extract custom rules from existing file
        custom_rules = []
        in_custom_section = False

        for line in existing_content.split("\n"):
            if "=== Custom Rules ===" in line or "# Custom" in line:
                in_custom_section = True
                continue
            elif in_custom_section and line.strip().startswith("# ==="):
                # End of custom section
                break
            elif in_custom_section and line.strip():
                custom_rules.append(line)

        if custom_rules:
            logger.debug(f"Preserved {len(custom_rules)} custom rules from existing file")
            self.add_custom_rules(None)

        return self.build()
    
    xǁGitignoreBuilderǁmerge_with_existing__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreBuilderǁmerge_with_existing__mutmut_1': xǁGitignoreBuilderǁmerge_with_existing__mutmut_1, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_2': xǁGitignoreBuilderǁmerge_with_existing__mutmut_2, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_3': xǁGitignoreBuilderǁmerge_with_existing__mutmut_3, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_4': xǁGitignoreBuilderǁmerge_with_existing__mutmut_4, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_5': xǁGitignoreBuilderǁmerge_with_existing__mutmut_5, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_6': xǁGitignoreBuilderǁmerge_with_existing__mutmut_6, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_7': xǁGitignoreBuilderǁmerge_with_existing__mutmut_7, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_8': xǁGitignoreBuilderǁmerge_with_existing__mutmut_8, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_9': xǁGitignoreBuilderǁmerge_with_existing__mutmut_9, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_10': xǁGitignoreBuilderǁmerge_with_existing__mutmut_10, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_11': xǁGitignoreBuilderǁmerge_with_existing__mutmut_11, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_12': xǁGitignoreBuilderǁmerge_with_existing__mutmut_12, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_13': xǁGitignoreBuilderǁmerge_with_existing__mutmut_13, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_14': xǁGitignoreBuilderǁmerge_with_existing__mutmut_14, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_15': xǁGitignoreBuilderǁmerge_with_existing__mutmut_15, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_16': xǁGitignoreBuilderǁmerge_with_existing__mutmut_16, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_17': xǁGitignoreBuilderǁmerge_with_existing__mutmut_17, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_18': xǁGitignoreBuilderǁmerge_with_existing__mutmut_18, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_19': xǁGitignoreBuilderǁmerge_with_existing__mutmut_19, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_20': xǁGitignoreBuilderǁmerge_with_existing__mutmut_20, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_21': xǁGitignoreBuilderǁmerge_with_existing__mutmut_21, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_22': xǁGitignoreBuilderǁmerge_with_existing__mutmut_22, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_23': xǁGitignoreBuilderǁmerge_with_existing__mutmut_23, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_24': xǁGitignoreBuilderǁmerge_with_existing__mutmut_24, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_25': xǁGitignoreBuilderǁmerge_with_existing__mutmut_25, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_26': xǁGitignoreBuilderǁmerge_with_existing__mutmut_26, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_27': xǁGitignoreBuilderǁmerge_with_existing__mutmut_27, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_28': xǁGitignoreBuilderǁmerge_with_existing__mutmut_28, 
        'xǁGitignoreBuilderǁmerge_with_existing__mutmut_29': xǁGitignoreBuilderǁmerge_with_existing__mutmut_29
    }
    
    def merge_with_existing(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreBuilderǁmerge_with_existing__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreBuilderǁmerge_with_existing__mutmut_mutants"), args, kwargs, self)
        return result 
    
    merge_with_existing.__signature__ = _mutmut_signature(xǁGitignoreBuilderǁmerge_with_existing__mutmut_orig)
    xǁGitignoreBuilderǁmerge_with_existing__mutmut_orig.__name__ = 'xǁGitignoreBuilderǁmerge_with_existing'


# 🧰🌍🔚
