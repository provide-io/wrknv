#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Gitignore Manager
=================
Central manager for gitignore operations."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from provide.foundation import logger

from .builder import GitignoreBuilder
from .detector import ProjectDetector
from .templates import TemplateHandler

if TYPE_CHECKING:
    from wrknv.wenv.schema import GitignoreConfig
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


class GitignoreManager:
    """Manages gitignore file generation and updates."""

    def xǁGitignoreManagerǁ__init____mutmut_orig(
        self,
        project_dir: Path | None = None,
        output_path: Path | None = None,
        cache_dir: Path | None = None,
    ) -> None:
        """
        Initialize the manager.

        Args:
            project_dir: Project directory to work with
            output_path: Custom output path for gitignore file
            cache_dir: Custom cache directory for templates
        """
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.gitignore_path = output_path or self.project_dir / ".gitignore"
        self.template_handler = TemplateHandler(cache_dir=cache_dir)
        self.detector = ProjectDetector()

        logger.debug(f"GitignoreManager initialized for project: {self.project_dir}")
        logger.debug(f"Gitignore path: {self.gitignore_path}")

    def xǁGitignoreManagerǁ__init____mutmut_1(
        self,
        project_dir: Path | None = None,
        output_path: Path | None = None,
        cache_dir: Path | None = None,
    ) -> None:
        """
        Initialize the manager.

        Args:
            project_dir: Project directory to work with
            output_path: Custom output path for gitignore file
            cache_dir: Custom cache directory for templates
        """
        self.project_dir = None
        self.gitignore_path = output_path or self.project_dir / ".gitignore"
        self.template_handler = TemplateHandler(cache_dir=cache_dir)
        self.detector = ProjectDetector()

        logger.debug(f"GitignoreManager initialized for project: {self.project_dir}")
        logger.debug(f"Gitignore path: {self.gitignore_path}")

    def xǁGitignoreManagerǁ__init____mutmut_2(
        self,
        project_dir: Path | None = None,
        output_path: Path | None = None,
        cache_dir: Path | None = None,
    ) -> None:
        """
        Initialize the manager.

        Args:
            project_dir: Project directory to work with
            output_path: Custom output path for gitignore file
            cache_dir: Custom cache directory for templates
        """
        self.project_dir = Path(None) if project_dir else Path.cwd()
        self.gitignore_path = output_path or self.project_dir / ".gitignore"
        self.template_handler = TemplateHandler(cache_dir=cache_dir)
        self.detector = ProjectDetector()

        logger.debug(f"GitignoreManager initialized for project: {self.project_dir}")
        logger.debug(f"Gitignore path: {self.gitignore_path}")

    def xǁGitignoreManagerǁ__init____mutmut_3(
        self,
        project_dir: Path | None = None,
        output_path: Path | None = None,
        cache_dir: Path | None = None,
    ) -> None:
        """
        Initialize the manager.

        Args:
            project_dir: Project directory to work with
            output_path: Custom output path for gitignore file
            cache_dir: Custom cache directory for templates
        """
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.gitignore_path = None
        self.template_handler = TemplateHandler(cache_dir=cache_dir)
        self.detector = ProjectDetector()

        logger.debug(f"GitignoreManager initialized for project: {self.project_dir}")
        logger.debug(f"Gitignore path: {self.gitignore_path}")

    def xǁGitignoreManagerǁ__init____mutmut_4(
        self,
        project_dir: Path | None = None,
        output_path: Path | None = None,
        cache_dir: Path | None = None,
    ) -> None:
        """
        Initialize the manager.

        Args:
            project_dir: Project directory to work with
            output_path: Custom output path for gitignore file
            cache_dir: Custom cache directory for templates
        """
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.gitignore_path = output_path and self.project_dir / ".gitignore"
        self.template_handler = TemplateHandler(cache_dir=cache_dir)
        self.detector = ProjectDetector()

        logger.debug(f"GitignoreManager initialized for project: {self.project_dir}")
        logger.debug(f"Gitignore path: {self.gitignore_path}")

    def xǁGitignoreManagerǁ__init____mutmut_5(
        self,
        project_dir: Path | None = None,
        output_path: Path | None = None,
        cache_dir: Path | None = None,
    ) -> None:
        """
        Initialize the manager.

        Args:
            project_dir: Project directory to work with
            output_path: Custom output path for gitignore file
            cache_dir: Custom cache directory for templates
        """
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.gitignore_path = output_path or self.project_dir * ".gitignore"
        self.template_handler = TemplateHandler(cache_dir=cache_dir)
        self.detector = ProjectDetector()

        logger.debug(f"GitignoreManager initialized for project: {self.project_dir}")
        logger.debug(f"Gitignore path: {self.gitignore_path}")

    def xǁGitignoreManagerǁ__init____mutmut_6(
        self,
        project_dir: Path | None = None,
        output_path: Path | None = None,
        cache_dir: Path | None = None,
    ) -> None:
        """
        Initialize the manager.

        Args:
            project_dir: Project directory to work with
            output_path: Custom output path for gitignore file
            cache_dir: Custom cache directory for templates
        """
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.gitignore_path = output_path or self.project_dir / "XX.gitignoreXX"
        self.template_handler = TemplateHandler(cache_dir=cache_dir)
        self.detector = ProjectDetector()

        logger.debug(f"GitignoreManager initialized for project: {self.project_dir}")
        logger.debug(f"Gitignore path: {self.gitignore_path}")

    def xǁGitignoreManagerǁ__init____mutmut_7(
        self,
        project_dir: Path | None = None,
        output_path: Path | None = None,
        cache_dir: Path | None = None,
    ) -> None:
        """
        Initialize the manager.

        Args:
            project_dir: Project directory to work with
            output_path: Custom output path for gitignore file
            cache_dir: Custom cache directory for templates
        """
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.gitignore_path = output_path or self.project_dir / ".GITIGNORE"
        self.template_handler = TemplateHandler(cache_dir=cache_dir)
        self.detector = ProjectDetector()

        logger.debug(f"GitignoreManager initialized for project: {self.project_dir}")
        logger.debug(f"Gitignore path: {self.gitignore_path}")

    def xǁGitignoreManagerǁ__init____mutmut_8(
        self,
        project_dir: Path | None = None,
        output_path: Path | None = None,
        cache_dir: Path | None = None,
    ) -> None:
        """
        Initialize the manager.

        Args:
            project_dir: Project directory to work with
            output_path: Custom output path for gitignore file
            cache_dir: Custom cache directory for templates
        """
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.gitignore_path = output_path or self.project_dir / ".gitignore"
        self.template_handler = None
        self.detector = ProjectDetector()

        logger.debug(f"GitignoreManager initialized for project: {self.project_dir}")
        logger.debug(f"Gitignore path: {self.gitignore_path}")

    def xǁGitignoreManagerǁ__init____mutmut_9(
        self,
        project_dir: Path | None = None,
        output_path: Path | None = None,
        cache_dir: Path | None = None,
    ) -> None:
        """
        Initialize the manager.

        Args:
            project_dir: Project directory to work with
            output_path: Custom output path for gitignore file
            cache_dir: Custom cache directory for templates
        """
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.gitignore_path = output_path or self.project_dir / ".gitignore"
        self.template_handler = TemplateHandler(cache_dir=None)
        self.detector = ProjectDetector()

        logger.debug(f"GitignoreManager initialized for project: {self.project_dir}")
        logger.debug(f"Gitignore path: {self.gitignore_path}")

    def xǁGitignoreManagerǁ__init____mutmut_10(
        self,
        project_dir: Path | None = None,
        output_path: Path | None = None,
        cache_dir: Path | None = None,
    ) -> None:
        """
        Initialize the manager.

        Args:
            project_dir: Project directory to work with
            output_path: Custom output path for gitignore file
            cache_dir: Custom cache directory for templates
        """
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.gitignore_path = output_path or self.project_dir / ".gitignore"
        self.template_handler = TemplateHandler(cache_dir=cache_dir)
        self.detector = None

        logger.debug(f"GitignoreManager initialized for project: {self.project_dir}")
        logger.debug(f"Gitignore path: {self.gitignore_path}")

    def xǁGitignoreManagerǁ__init____mutmut_11(
        self,
        project_dir: Path | None = None,
        output_path: Path | None = None,
        cache_dir: Path | None = None,
    ) -> None:
        """
        Initialize the manager.

        Args:
            project_dir: Project directory to work with
            output_path: Custom output path for gitignore file
            cache_dir: Custom cache directory for templates
        """
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.gitignore_path = output_path or self.project_dir / ".gitignore"
        self.template_handler = TemplateHandler(cache_dir=cache_dir)
        self.detector = ProjectDetector()

        logger.debug(None)
        logger.debug(f"Gitignore path: {self.gitignore_path}")

    def xǁGitignoreManagerǁ__init____mutmut_12(
        self,
        project_dir: Path | None = None,
        output_path: Path | None = None,
        cache_dir: Path | None = None,
    ) -> None:
        """
        Initialize the manager.

        Args:
            project_dir: Project directory to work with
            output_path: Custom output path for gitignore file
            cache_dir: Custom cache directory for templates
        """
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.gitignore_path = output_path or self.project_dir / ".gitignore"
        self.template_handler = TemplateHandler(cache_dir=cache_dir)
        self.detector = ProjectDetector()

        logger.debug(f"GitignoreManager initialized for project: {self.project_dir}")
        logger.debug(None)
    
    xǁGitignoreManagerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreManagerǁ__init____mutmut_1': xǁGitignoreManagerǁ__init____mutmut_1, 
        'xǁGitignoreManagerǁ__init____mutmut_2': xǁGitignoreManagerǁ__init____mutmut_2, 
        'xǁGitignoreManagerǁ__init____mutmut_3': xǁGitignoreManagerǁ__init____mutmut_3, 
        'xǁGitignoreManagerǁ__init____mutmut_4': xǁGitignoreManagerǁ__init____mutmut_4, 
        'xǁGitignoreManagerǁ__init____mutmut_5': xǁGitignoreManagerǁ__init____mutmut_5, 
        'xǁGitignoreManagerǁ__init____mutmut_6': xǁGitignoreManagerǁ__init____mutmut_6, 
        'xǁGitignoreManagerǁ__init____mutmut_7': xǁGitignoreManagerǁ__init____mutmut_7, 
        'xǁGitignoreManagerǁ__init____mutmut_8': xǁGitignoreManagerǁ__init____mutmut_8, 
        'xǁGitignoreManagerǁ__init____mutmut_9': xǁGitignoreManagerǁ__init____mutmut_9, 
        'xǁGitignoreManagerǁ__init____mutmut_10': xǁGitignoreManagerǁ__init____mutmut_10, 
        'xǁGitignoreManagerǁ__init____mutmut_11': xǁGitignoreManagerǁ__init____mutmut_11, 
        'xǁGitignoreManagerǁ__init____mutmut_12': xǁGitignoreManagerǁ__init____mutmut_12
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreManagerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁGitignoreManagerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁGitignoreManagerǁ__init____mutmut_orig)
    xǁGitignoreManagerǁ__init____mutmut_orig.__name__ = 'xǁGitignoreManagerǁ__init__'

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_orig(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_1(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = True,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_2(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(None)

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_3(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = None

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_4(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_5(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=None)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_6(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = None
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_7(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(None)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_8(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = None
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_9(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split(None)
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_10(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("XX\nXX")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_11(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = None
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_12(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_13(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(None):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_14(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern not in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_15(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(None)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_16(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = None

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_17(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(None)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_18(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "XX\nXX".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_19(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(None, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_20(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, None)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_21(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_22(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, )
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_23(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(None)
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_24(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(None)

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_25(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(None)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_26(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append or self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_27(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = None
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_28(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = None
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_29(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = None
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_30(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" - new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_31(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content - "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_32(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "XX\n\nXX" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_33(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = None
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_34(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(None)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_35(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = None

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_36(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(None)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_37(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(None)

        return True

    def xǁGitignoreManagerǁbuild_from_templates__mutmut_38(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        append: bool = False,
        project_name: str | None = None,
    ) -> bool:
        """
        Build gitignore from specified templates.

        Args:
            templates: List of template names
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude from templates
            append: Whether to append to existing file
            project_name: Project name for header

        Returns:
            True if successful
        """
        logger.info(f"Building gitignore from templates: {templates}")

        builder = GitignoreBuilder()

        # Add header unless appending
        if not append:
            builder.add_header(project_name=project_name)

        # Add template sections
        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                # Filter excluded patterns
                if exclude_patterns:
                    lines = content.split("\n")
                    filtered_lines = []
                    for line in lines:
                        if not any(pattern in line for pattern in exclude_patterns):
                            filtered_lines.append(line)
                    content = "\n".join(filtered_lines)

                builder.add_template_section(template_name, content)
                logger.debug(f"Added template: {template_name}")
            else:
                logger.warning(f"Template '{template_name}' not found")

        # Add wrknv section
        builder.add_wrknv_section()

        # Add provide ecosystem section
        builder.add_provide_section()

        # Add custom rules
        if custom_rules:
            builder.add_custom_rules(custom_rules)

        # Build or merge
        if append and self.gitignore_path.exists():
            # Append mode - merge with existing
            existing_content = self.gitignore_path.read_text()
            new_content = builder.build()
            final_content = existing_content + "\n\n" + new_content
        elif self.gitignore_path.exists():
            # Overwrite mode but preserve custom rules
            final_content = builder.merge_with_existing(self.gitignore_path)
        else:
            # New file
            final_content = builder.build()

        # Write the file
        self.gitignore_path.write_text(final_content)
        logger.info(f"Successfully wrote gitignore to {self.gitignore_path}")

        return False
    
    xǁGitignoreManagerǁbuild_from_templates__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreManagerǁbuild_from_templates__mutmut_1': xǁGitignoreManagerǁbuild_from_templates__mutmut_1, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_2': xǁGitignoreManagerǁbuild_from_templates__mutmut_2, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_3': xǁGitignoreManagerǁbuild_from_templates__mutmut_3, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_4': xǁGitignoreManagerǁbuild_from_templates__mutmut_4, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_5': xǁGitignoreManagerǁbuild_from_templates__mutmut_5, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_6': xǁGitignoreManagerǁbuild_from_templates__mutmut_6, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_7': xǁGitignoreManagerǁbuild_from_templates__mutmut_7, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_8': xǁGitignoreManagerǁbuild_from_templates__mutmut_8, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_9': xǁGitignoreManagerǁbuild_from_templates__mutmut_9, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_10': xǁGitignoreManagerǁbuild_from_templates__mutmut_10, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_11': xǁGitignoreManagerǁbuild_from_templates__mutmut_11, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_12': xǁGitignoreManagerǁbuild_from_templates__mutmut_12, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_13': xǁGitignoreManagerǁbuild_from_templates__mutmut_13, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_14': xǁGitignoreManagerǁbuild_from_templates__mutmut_14, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_15': xǁGitignoreManagerǁbuild_from_templates__mutmut_15, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_16': xǁGitignoreManagerǁbuild_from_templates__mutmut_16, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_17': xǁGitignoreManagerǁbuild_from_templates__mutmut_17, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_18': xǁGitignoreManagerǁbuild_from_templates__mutmut_18, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_19': xǁGitignoreManagerǁbuild_from_templates__mutmut_19, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_20': xǁGitignoreManagerǁbuild_from_templates__mutmut_20, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_21': xǁGitignoreManagerǁbuild_from_templates__mutmut_21, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_22': xǁGitignoreManagerǁbuild_from_templates__mutmut_22, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_23': xǁGitignoreManagerǁbuild_from_templates__mutmut_23, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_24': xǁGitignoreManagerǁbuild_from_templates__mutmut_24, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_25': xǁGitignoreManagerǁbuild_from_templates__mutmut_25, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_26': xǁGitignoreManagerǁbuild_from_templates__mutmut_26, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_27': xǁGitignoreManagerǁbuild_from_templates__mutmut_27, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_28': xǁGitignoreManagerǁbuild_from_templates__mutmut_28, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_29': xǁGitignoreManagerǁbuild_from_templates__mutmut_29, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_30': xǁGitignoreManagerǁbuild_from_templates__mutmut_30, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_31': xǁGitignoreManagerǁbuild_from_templates__mutmut_31, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_32': xǁGitignoreManagerǁbuild_from_templates__mutmut_32, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_33': xǁGitignoreManagerǁbuild_from_templates__mutmut_33, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_34': xǁGitignoreManagerǁbuild_from_templates__mutmut_34, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_35': xǁGitignoreManagerǁbuild_from_templates__mutmut_35, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_36': xǁGitignoreManagerǁbuild_from_templates__mutmut_36, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_37': xǁGitignoreManagerǁbuild_from_templates__mutmut_37, 
        'xǁGitignoreManagerǁbuild_from_templates__mutmut_38': xǁGitignoreManagerǁbuild_from_templates__mutmut_38
    }
    
    def build_from_templates(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreManagerǁbuild_from_templates__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreManagerǁbuild_from_templates__mutmut_mutants"), args, kwargs, self)
        return result 
    
    build_from_templates.__signature__ = _mutmut_signature(xǁGitignoreManagerǁbuild_from_templates__mutmut_orig)
    xǁGitignoreManagerǁbuild_from_templates__mutmut_orig.__name__ = 'xǁGitignoreManagerǁbuild_from_templates'

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_orig(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_1(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 6,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_2(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info(None)

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_3(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("XXBuilding gitignore from auto-detectionXX")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_4(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_5(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("BUILDING GITIGNORE FROM AUTO-DETECTION")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_6(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(None, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_7(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=None)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_8(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_9(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, )

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_10(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = None

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_11(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_12(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning(None)
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_13(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("XXNo templates detectedXX")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_14(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("no templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_15(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("NO TEMPLATES DETECTED")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_16(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return True

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_17(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(None)

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_18(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=None,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_19(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=None,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_20(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=None,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_21(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=None,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_22(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_23(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            exclude_patterns=exclude_patterns,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_24(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            project_name=self.project_dir.name,
        )

    def xǁGitignoreManagerǁbuild_from_detection__mutmut_25(
        self,
        custom_rules: list[str] | None = None,
        exclude_patterns: list[str] | None = None,
        max_depth: int = 5,
    ) -> bool:
        """
        Build gitignore from auto-detection.

        Args:
            custom_rules: Custom rules to add
            exclude_patterns: Patterns to exclude
            max_depth: Maximum scan depth

        Returns:
            True if successful
        """
        logger.info("Building gitignore from auto-detection")

        # Scan project
        self.detector.reset()
        self.detector.scan_directory(self.project_dir, max_depth=max_depth)

        # Get suggested templates
        templates = self.detector.suggest_templates()

        if not templates:
            logger.warning("No templates detected")
            return False

        logger.info(f"Auto-detected templates: {templates}")

        # Build from detected templates
        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            exclude_patterns=exclude_patterns,
            )
    
    xǁGitignoreManagerǁbuild_from_detection__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreManagerǁbuild_from_detection__mutmut_1': xǁGitignoreManagerǁbuild_from_detection__mutmut_1, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_2': xǁGitignoreManagerǁbuild_from_detection__mutmut_2, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_3': xǁGitignoreManagerǁbuild_from_detection__mutmut_3, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_4': xǁGitignoreManagerǁbuild_from_detection__mutmut_4, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_5': xǁGitignoreManagerǁbuild_from_detection__mutmut_5, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_6': xǁGitignoreManagerǁbuild_from_detection__mutmut_6, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_7': xǁGitignoreManagerǁbuild_from_detection__mutmut_7, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_8': xǁGitignoreManagerǁbuild_from_detection__mutmut_8, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_9': xǁGitignoreManagerǁbuild_from_detection__mutmut_9, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_10': xǁGitignoreManagerǁbuild_from_detection__mutmut_10, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_11': xǁGitignoreManagerǁbuild_from_detection__mutmut_11, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_12': xǁGitignoreManagerǁbuild_from_detection__mutmut_12, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_13': xǁGitignoreManagerǁbuild_from_detection__mutmut_13, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_14': xǁGitignoreManagerǁbuild_from_detection__mutmut_14, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_15': xǁGitignoreManagerǁbuild_from_detection__mutmut_15, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_16': xǁGitignoreManagerǁbuild_from_detection__mutmut_16, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_17': xǁGitignoreManagerǁbuild_from_detection__mutmut_17, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_18': xǁGitignoreManagerǁbuild_from_detection__mutmut_18, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_19': xǁGitignoreManagerǁbuild_from_detection__mutmut_19, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_20': xǁGitignoreManagerǁbuild_from_detection__mutmut_20, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_21': xǁGitignoreManagerǁbuild_from_detection__mutmut_21, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_22': xǁGitignoreManagerǁbuild_from_detection__mutmut_22, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_23': xǁGitignoreManagerǁbuild_from_detection__mutmut_23, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_24': xǁGitignoreManagerǁbuild_from_detection__mutmut_24, 
        'xǁGitignoreManagerǁbuild_from_detection__mutmut_25': xǁGitignoreManagerǁbuild_from_detection__mutmut_25
    }
    
    def build_from_detection(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreManagerǁbuild_from_detection__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreManagerǁbuild_from_detection__mutmut_mutants"), args, kwargs, self)
        return result 
    
    build_from_detection.__signature__ = _mutmut_signature(xǁGitignoreManagerǁbuild_from_detection__mutmut_orig)
    xǁGitignoreManagerǁbuild_from_detection__mutmut_orig.__name__ = 'xǁGitignoreManagerǁbuild_from_detection'

    def xǁGitignoreManagerǁbuild_from_config__mutmut_orig(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_1(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info(None)

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_2(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("XXBuilding gitignore from configurationXX")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_3(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_4(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("BUILDING GITIGNORE FROM CONFIGURATION")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_5(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=None,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_6(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_7(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_8(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=None,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_9(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_10(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_11(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_12(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_13(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(None, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_14(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, None) else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_15(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr("custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_16(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, ) else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_17(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "XXcustom_rulesXX") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_18(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "CUSTOM_RULES") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_19(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(None, "exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_20(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, None) else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_21(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr("exclude_patterns") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_22(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, ) else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_23(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "XXexclude_patternsXX") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_24(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "EXCLUDE_PATTERNS") else None,
            append=False,
        )

    def xǁGitignoreManagerǁbuild_from_config__mutmut_25(self, config: GitignoreConfig) -> bool:
        """
        Build gitignore from configuration object.

        Args:
            config: GitignoreConfig object

        Returns:
            True if successful
        """
        logger.info("Building gitignore from configuration")

        return self.build_from_templates(
            templates=config.templates,
            custom_rules=config.custom_rules if hasattr(config, "custom_rules") else None,
            exclude_patterns=config.exclude_patterns if hasattr(config, "exclude_patterns") else None,
            append=True,
        )
    
    xǁGitignoreManagerǁbuild_from_config__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreManagerǁbuild_from_config__mutmut_1': xǁGitignoreManagerǁbuild_from_config__mutmut_1, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_2': xǁGitignoreManagerǁbuild_from_config__mutmut_2, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_3': xǁGitignoreManagerǁbuild_from_config__mutmut_3, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_4': xǁGitignoreManagerǁbuild_from_config__mutmut_4, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_5': xǁGitignoreManagerǁbuild_from_config__mutmut_5, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_6': xǁGitignoreManagerǁbuild_from_config__mutmut_6, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_7': xǁGitignoreManagerǁbuild_from_config__mutmut_7, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_8': xǁGitignoreManagerǁbuild_from_config__mutmut_8, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_9': xǁGitignoreManagerǁbuild_from_config__mutmut_9, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_10': xǁGitignoreManagerǁbuild_from_config__mutmut_10, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_11': xǁGitignoreManagerǁbuild_from_config__mutmut_11, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_12': xǁGitignoreManagerǁbuild_from_config__mutmut_12, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_13': xǁGitignoreManagerǁbuild_from_config__mutmut_13, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_14': xǁGitignoreManagerǁbuild_from_config__mutmut_14, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_15': xǁGitignoreManagerǁbuild_from_config__mutmut_15, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_16': xǁGitignoreManagerǁbuild_from_config__mutmut_16, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_17': xǁGitignoreManagerǁbuild_from_config__mutmut_17, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_18': xǁGitignoreManagerǁbuild_from_config__mutmut_18, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_19': xǁGitignoreManagerǁbuild_from_config__mutmut_19, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_20': xǁGitignoreManagerǁbuild_from_config__mutmut_20, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_21': xǁGitignoreManagerǁbuild_from_config__mutmut_21, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_22': xǁGitignoreManagerǁbuild_from_config__mutmut_22, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_23': xǁGitignoreManagerǁbuild_from_config__mutmut_23, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_24': xǁGitignoreManagerǁbuild_from_config__mutmut_24, 
        'xǁGitignoreManagerǁbuild_from_config__mutmut_25': xǁGitignoreManagerǁbuild_from_config__mutmut_25
    }
    
    def build_from_config(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreManagerǁbuild_from_config__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreManagerǁbuild_from_config__mutmut_mutants"), args, kwargs, self)
        return result 
    
    build_from_config.__signature__ = _mutmut_signature(xǁGitignoreManagerǁbuild_from_config__mutmut_orig)
    xǁGitignoreManagerǁbuild_from_config__mutmut_orig.__name__ = 'xǁGitignoreManagerǁbuild_from_config'

    def xǁGitignoreManagerǁadd_templates__mutmut_orig(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> bool:
        """
        Add templates to existing gitignore.

        Args:
            templates: Templates to add
            custom_rules: Additional custom rules

        Returns:
            True if successful
        """
        logger.info(f"Adding templates to existing gitignore: {templates}")

        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            append=True,
        )

    def xǁGitignoreManagerǁadd_templates__mutmut_1(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> bool:
        """
        Add templates to existing gitignore.

        Args:
            templates: Templates to add
            custom_rules: Additional custom rules

        Returns:
            True if successful
        """
        logger.info(None)

        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            append=True,
        )

    def xǁGitignoreManagerǁadd_templates__mutmut_2(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> bool:
        """
        Add templates to existing gitignore.

        Args:
            templates: Templates to add
            custom_rules: Additional custom rules

        Returns:
            True if successful
        """
        logger.info(f"Adding templates to existing gitignore: {templates}")

        return self.build_from_templates(
            templates=None,
            custom_rules=custom_rules,
            append=True,
        )

    def xǁGitignoreManagerǁadd_templates__mutmut_3(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> bool:
        """
        Add templates to existing gitignore.

        Args:
            templates: Templates to add
            custom_rules: Additional custom rules

        Returns:
            True if successful
        """
        logger.info(f"Adding templates to existing gitignore: {templates}")

        return self.build_from_templates(
            templates=templates,
            custom_rules=None,
            append=True,
        )

    def xǁGitignoreManagerǁadd_templates__mutmut_4(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> bool:
        """
        Add templates to existing gitignore.

        Args:
            templates: Templates to add
            custom_rules: Additional custom rules

        Returns:
            True if successful
        """
        logger.info(f"Adding templates to existing gitignore: {templates}")

        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            append=None,
        )

    def xǁGitignoreManagerǁadd_templates__mutmut_5(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> bool:
        """
        Add templates to existing gitignore.

        Args:
            templates: Templates to add
            custom_rules: Additional custom rules

        Returns:
            True if successful
        """
        logger.info(f"Adding templates to existing gitignore: {templates}")

        return self.build_from_templates(
            custom_rules=custom_rules,
            append=True,
        )

    def xǁGitignoreManagerǁadd_templates__mutmut_6(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> bool:
        """
        Add templates to existing gitignore.

        Args:
            templates: Templates to add
            custom_rules: Additional custom rules

        Returns:
            True if successful
        """
        logger.info(f"Adding templates to existing gitignore: {templates}")

        return self.build_from_templates(
            templates=templates,
            append=True,
        )

    def xǁGitignoreManagerǁadd_templates__mutmut_7(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> bool:
        """
        Add templates to existing gitignore.

        Args:
            templates: Templates to add
            custom_rules: Additional custom rules

        Returns:
            True if successful
        """
        logger.info(f"Adding templates to existing gitignore: {templates}")

        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            )

    def xǁGitignoreManagerǁadd_templates__mutmut_8(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> bool:
        """
        Add templates to existing gitignore.

        Args:
            templates: Templates to add
            custom_rules: Additional custom rules

        Returns:
            True if successful
        """
        logger.info(f"Adding templates to existing gitignore: {templates}")

        return self.build_from_templates(
            templates=templates,
            custom_rules=custom_rules,
            append=False,
        )
    
    xǁGitignoreManagerǁadd_templates__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreManagerǁadd_templates__mutmut_1': xǁGitignoreManagerǁadd_templates__mutmut_1, 
        'xǁGitignoreManagerǁadd_templates__mutmut_2': xǁGitignoreManagerǁadd_templates__mutmut_2, 
        'xǁGitignoreManagerǁadd_templates__mutmut_3': xǁGitignoreManagerǁadd_templates__mutmut_3, 
        'xǁGitignoreManagerǁadd_templates__mutmut_4': xǁGitignoreManagerǁadd_templates__mutmut_4, 
        'xǁGitignoreManagerǁadd_templates__mutmut_5': xǁGitignoreManagerǁadd_templates__mutmut_5, 
        'xǁGitignoreManagerǁadd_templates__mutmut_6': xǁGitignoreManagerǁadd_templates__mutmut_6, 
        'xǁGitignoreManagerǁadd_templates__mutmut_7': xǁGitignoreManagerǁadd_templates__mutmut_7, 
        'xǁGitignoreManagerǁadd_templates__mutmut_8': xǁGitignoreManagerǁadd_templates__mutmut_8
    }
    
    def add_templates(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreManagerǁadd_templates__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreManagerǁadd_templates__mutmut_mutants"), args, kwargs, self)
        return result 
    
    add_templates.__signature__ = _mutmut_signature(xǁGitignoreManagerǁadd_templates__mutmut_orig)
    xǁGitignoreManagerǁadd_templates__mutmut_orig.__name__ = 'xǁGitignoreManagerǁadd_templates'

    def xǁGitignoreManagerǁlist_available_templates__mutmut_orig(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter

        Returns:
            List of template names
        """
        return self.template_handler.list_templates(category=category)

    def xǁGitignoreManagerǁlist_available_templates__mutmut_1(self, category: str | None = None) -> list[str]:
        """
        List available templates.

        Args:
            category: Optional category filter

        Returns:
            List of template names
        """
        return self.template_handler.list_templates(category=None)
    
    xǁGitignoreManagerǁlist_available_templates__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreManagerǁlist_available_templates__mutmut_1': xǁGitignoreManagerǁlist_available_templates__mutmut_1
    }
    
    def list_available_templates(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreManagerǁlist_available_templates__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreManagerǁlist_available_templates__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list_available_templates.__signature__ = _mutmut_signature(xǁGitignoreManagerǁlist_available_templates__mutmut_orig)
    xǁGitignoreManagerǁlist_available_templates__mutmut_orig.__name__ = 'xǁGitignoreManagerǁlist_available_templates'

    def xǁGitignoreManagerǁsearch_templates__mutmut_orig(self, pattern: str) -> list[str]:
        """
        Search for templates.

        Args:
            pattern: Search pattern

        Returns:
            List of matching template names
        """
        return self.template_handler.search_templates(pattern)

    def xǁGitignoreManagerǁsearch_templates__mutmut_1(self, pattern: str) -> list[str]:
        """
        Search for templates.

        Args:
            pattern: Search pattern

        Returns:
            List of matching template names
        """
        return self.template_handler.search_templates(None)
    
    xǁGitignoreManagerǁsearch_templates__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreManagerǁsearch_templates__mutmut_1': xǁGitignoreManagerǁsearch_templates__mutmut_1
    }
    
    def search_templates(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreManagerǁsearch_templates__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreManagerǁsearch_templates__mutmut_mutants"), args, kwargs, self)
        return result 
    
    search_templates.__signature__ = _mutmut_signature(xǁGitignoreManagerǁsearch_templates__mutmut_orig)
    xǁGitignoreManagerǁsearch_templates__mutmut_orig.__name__ = 'xǁGitignoreManagerǁsearch_templates'

    def xǁGitignoreManagerǁupdate_templates__mutmut_orig(self, force: bool = False) -> bool:
        """
        Update template cache from GitHub.

        Args:
            force: Force update even if cache is valid

        Returns:
            True if updated
        """
        logger.info("Updating gitignore templates")
        return self.template_handler.update_cache(force=force)

    def xǁGitignoreManagerǁupdate_templates__mutmut_1(self, force: bool = True) -> bool:
        """
        Update template cache from GitHub.

        Args:
            force: Force update even if cache is valid

        Returns:
            True if updated
        """
        logger.info("Updating gitignore templates")
        return self.template_handler.update_cache(force=force)

    def xǁGitignoreManagerǁupdate_templates__mutmut_2(self, force: bool = False) -> bool:
        """
        Update template cache from GitHub.

        Args:
            force: Force update even if cache is valid

        Returns:
            True if updated
        """
        logger.info(None)
        return self.template_handler.update_cache(force=force)

    def xǁGitignoreManagerǁupdate_templates__mutmut_3(self, force: bool = False) -> bool:
        """
        Update template cache from GitHub.

        Args:
            force: Force update even if cache is valid

        Returns:
            True if updated
        """
        logger.info("XXUpdating gitignore templatesXX")
        return self.template_handler.update_cache(force=force)

    def xǁGitignoreManagerǁupdate_templates__mutmut_4(self, force: bool = False) -> bool:
        """
        Update template cache from GitHub.

        Args:
            force: Force update even if cache is valid

        Returns:
            True if updated
        """
        logger.info("updating gitignore templates")
        return self.template_handler.update_cache(force=force)

    def xǁGitignoreManagerǁupdate_templates__mutmut_5(self, force: bool = False) -> bool:
        """
        Update template cache from GitHub.

        Args:
            force: Force update even if cache is valid

        Returns:
            True if updated
        """
        logger.info("UPDATING GITIGNORE TEMPLATES")
        return self.template_handler.update_cache(force=force)

    def xǁGitignoreManagerǁupdate_templates__mutmut_6(self, force: bool = False) -> bool:
        """
        Update template cache from GitHub.

        Args:
            force: Force update even if cache is valid

        Returns:
            True if updated
        """
        logger.info("Updating gitignore templates")
        return self.template_handler.update_cache(force=None)
    
    xǁGitignoreManagerǁupdate_templates__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreManagerǁupdate_templates__mutmut_1': xǁGitignoreManagerǁupdate_templates__mutmut_1, 
        'xǁGitignoreManagerǁupdate_templates__mutmut_2': xǁGitignoreManagerǁupdate_templates__mutmut_2, 
        'xǁGitignoreManagerǁupdate_templates__mutmut_3': xǁGitignoreManagerǁupdate_templates__mutmut_3, 
        'xǁGitignoreManagerǁupdate_templates__mutmut_4': xǁGitignoreManagerǁupdate_templates__mutmut_4, 
        'xǁGitignoreManagerǁupdate_templates__mutmut_5': xǁGitignoreManagerǁupdate_templates__mutmut_5, 
        'xǁGitignoreManagerǁupdate_templates__mutmut_6': xǁGitignoreManagerǁupdate_templates__mutmut_6
    }
    
    def update_templates(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreManagerǁupdate_templates__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreManagerǁupdate_templates__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update_templates.__signature__ = _mutmut_signature(xǁGitignoreManagerǁupdate_templates__mutmut_orig)
    xǁGitignoreManagerǁupdate_templates__mutmut_orig.__name__ = 'xǁGitignoreManagerǁupdate_templates'

    def xǁGitignoreManagerǁpreview__mutmut_orig(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> str:
        """
        Preview what would be generated.

        Args:
            templates: Templates to preview
            custom_rules: Custom rules to include

        Returns:
            Preview content
        """
        if not templates:
            return "No templates specified"

        builder = GitignoreBuilder()
        builder.add_header()

        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                builder.add_template_section(template_name, content)

        builder.add_wrknv_section()
        builder.add_provide_section()

        if custom_rules:
            builder.add_custom_rules(custom_rules)

        return builder.build()

    def xǁGitignoreManagerǁpreview__mutmut_1(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> str:
        """
        Preview what would be generated.

        Args:
            templates: Templates to preview
            custom_rules: Custom rules to include

        Returns:
            Preview content
        """
        if templates:
            return "No templates specified"

        builder = GitignoreBuilder()
        builder.add_header()

        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                builder.add_template_section(template_name, content)

        builder.add_wrknv_section()
        builder.add_provide_section()

        if custom_rules:
            builder.add_custom_rules(custom_rules)

        return builder.build()

    def xǁGitignoreManagerǁpreview__mutmut_2(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> str:
        """
        Preview what would be generated.

        Args:
            templates: Templates to preview
            custom_rules: Custom rules to include

        Returns:
            Preview content
        """
        if not templates:
            return "XXNo templates specifiedXX"

        builder = GitignoreBuilder()
        builder.add_header()

        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                builder.add_template_section(template_name, content)

        builder.add_wrknv_section()
        builder.add_provide_section()

        if custom_rules:
            builder.add_custom_rules(custom_rules)

        return builder.build()

    def xǁGitignoreManagerǁpreview__mutmut_3(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> str:
        """
        Preview what would be generated.

        Args:
            templates: Templates to preview
            custom_rules: Custom rules to include

        Returns:
            Preview content
        """
        if not templates:
            return "no templates specified"

        builder = GitignoreBuilder()
        builder.add_header()

        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                builder.add_template_section(template_name, content)

        builder.add_wrknv_section()
        builder.add_provide_section()

        if custom_rules:
            builder.add_custom_rules(custom_rules)

        return builder.build()

    def xǁGitignoreManagerǁpreview__mutmut_4(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> str:
        """
        Preview what would be generated.

        Args:
            templates: Templates to preview
            custom_rules: Custom rules to include

        Returns:
            Preview content
        """
        if not templates:
            return "NO TEMPLATES SPECIFIED"

        builder = GitignoreBuilder()
        builder.add_header()

        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                builder.add_template_section(template_name, content)

        builder.add_wrknv_section()
        builder.add_provide_section()

        if custom_rules:
            builder.add_custom_rules(custom_rules)

        return builder.build()

    def xǁGitignoreManagerǁpreview__mutmut_5(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> str:
        """
        Preview what would be generated.

        Args:
            templates: Templates to preview
            custom_rules: Custom rules to include

        Returns:
            Preview content
        """
        if not templates:
            return "No templates specified"

        builder = None
        builder.add_header()

        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                builder.add_template_section(template_name, content)

        builder.add_wrknv_section()
        builder.add_provide_section()

        if custom_rules:
            builder.add_custom_rules(custom_rules)

        return builder.build()

    def xǁGitignoreManagerǁpreview__mutmut_6(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> str:
        """
        Preview what would be generated.

        Args:
            templates: Templates to preview
            custom_rules: Custom rules to include

        Returns:
            Preview content
        """
        if not templates:
            return "No templates specified"

        builder = GitignoreBuilder()
        builder.add_header()

        for template_name in templates:
            content = None
            if content:
                builder.add_template_section(template_name, content)

        builder.add_wrknv_section()
        builder.add_provide_section()

        if custom_rules:
            builder.add_custom_rules(custom_rules)

        return builder.build()

    def xǁGitignoreManagerǁpreview__mutmut_7(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> str:
        """
        Preview what would be generated.

        Args:
            templates: Templates to preview
            custom_rules: Custom rules to include

        Returns:
            Preview content
        """
        if not templates:
            return "No templates specified"

        builder = GitignoreBuilder()
        builder.add_header()

        for template_name in templates:
            content = self.template_handler.get_template(None)
            if content:
                builder.add_template_section(template_name, content)

        builder.add_wrknv_section()
        builder.add_provide_section()

        if custom_rules:
            builder.add_custom_rules(custom_rules)

        return builder.build()

    def xǁGitignoreManagerǁpreview__mutmut_8(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> str:
        """
        Preview what would be generated.

        Args:
            templates: Templates to preview
            custom_rules: Custom rules to include

        Returns:
            Preview content
        """
        if not templates:
            return "No templates specified"

        builder = GitignoreBuilder()
        builder.add_header()

        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                builder.add_template_section(None, content)

        builder.add_wrknv_section()
        builder.add_provide_section()

        if custom_rules:
            builder.add_custom_rules(custom_rules)

        return builder.build()

    def xǁGitignoreManagerǁpreview__mutmut_9(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> str:
        """
        Preview what would be generated.

        Args:
            templates: Templates to preview
            custom_rules: Custom rules to include

        Returns:
            Preview content
        """
        if not templates:
            return "No templates specified"

        builder = GitignoreBuilder()
        builder.add_header()

        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                builder.add_template_section(template_name, None)

        builder.add_wrknv_section()
        builder.add_provide_section()

        if custom_rules:
            builder.add_custom_rules(custom_rules)

        return builder.build()

    def xǁGitignoreManagerǁpreview__mutmut_10(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> str:
        """
        Preview what would be generated.

        Args:
            templates: Templates to preview
            custom_rules: Custom rules to include

        Returns:
            Preview content
        """
        if not templates:
            return "No templates specified"

        builder = GitignoreBuilder()
        builder.add_header()

        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                builder.add_template_section(content)

        builder.add_wrknv_section()
        builder.add_provide_section()

        if custom_rules:
            builder.add_custom_rules(custom_rules)

        return builder.build()

    def xǁGitignoreManagerǁpreview__mutmut_11(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> str:
        """
        Preview what would be generated.

        Args:
            templates: Templates to preview
            custom_rules: Custom rules to include

        Returns:
            Preview content
        """
        if not templates:
            return "No templates specified"

        builder = GitignoreBuilder()
        builder.add_header()

        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                builder.add_template_section(template_name, )

        builder.add_wrknv_section()
        builder.add_provide_section()

        if custom_rules:
            builder.add_custom_rules(custom_rules)

        return builder.build()

    def xǁGitignoreManagerǁpreview__mutmut_12(
        self,
        templates: list[str],
        custom_rules: list[str] | None = None,
    ) -> str:
        """
        Preview what would be generated.

        Args:
            templates: Templates to preview
            custom_rules: Custom rules to include

        Returns:
            Preview content
        """
        if not templates:
            return "No templates specified"

        builder = GitignoreBuilder()
        builder.add_header()

        for template_name in templates:
            content = self.template_handler.get_template(template_name)
            if content:
                builder.add_template_section(template_name, content)

        builder.add_wrknv_section()
        builder.add_provide_section()

        if custom_rules:
            builder.add_custom_rules(None)

        return builder.build()
    
    xǁGitignoreManagerǁpreview__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreManagerǁpreview__mutmut_1': xǁGitignoreManagerǁpreview__mutmut_1, 
        'xǁGitignoreManagerǁpreview__mutmut_2': xǁGitignoreManagerǁpreview__mutmut_2, 
        'xǁGitignoreManagerǁpreview__mutmut_3': xǁGitignoreManagerǁpreview__mutmut_3, 
        'xǁGitignoreManagerǁpreview__mutmut_4': xǁGitignoreManagerǁpreview__mutmut_4, 
        'xǁGitignoreManagerǁpreview__mutmut_5': xǁGitignoreManagerǁpreview__mutmut_5, 
        'xǁGitignoreManagerǁpreview__mutmut_6': xǁGitignoreManagerǁpreview__mutmut_6, 
        'xǁGitignoreManagerǁpreview__mutmut_7': xǁGitignoreManagerǁpreview__mutmut_7, 
        'xǁGitignoreManagerǁpreview__mutmut_8': xǁGitignoreManagerǁpreview__mutmut_8, 
        'xǁGitignoreManagerǁpreview__mutmut_9': xǁGitignoreManagerǁpreview__mutmut_9, 
        'xǁGitignoreManagerǁpreview__mutmut_10': xǁGitignoreManagerǁpreview__mutmut_10, 
        'xǁGitignoreManagerǁpreview__mutmut_11': xǁGitignoreManagerǁpreview__mutmut_11, 
        'xǁGitignoreManagerǁpreview__mutmut_12': xǁGitignoreManagerǁpreview__mutmut_12
    }
    
    def preview(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreManagerǁpreview__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreManagerǁpreview__mutmut_mutants"), args, kwargs, self)
        return result 
    
    preview.__signature__ = _mutmut_signature(xǁGitignoreManagerǁpreview__mutmut_orig)
    xǁGitignoreManagerǁpreview__mutmut_orig.__name__ = 'xǁGitignoreManagerǁpreview'

    def xǁGitignoreManagerǁget_detection_report__mutmut_orig(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_1(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(None)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_2(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = None

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_3(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["XXProject Detection ReportXX", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_4(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["project detection report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_5(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["PROJECT DETECTION REPORT", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_6(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" / 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_7(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "XX=XX" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_8(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 25, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_9(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, "XXXX"]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_10(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(None)

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_11(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(None)}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_12(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {'XX, XX'.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_13(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(None))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_14(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(None)

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_15(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(None)}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_16(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {'XX, XX'.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_17(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(None))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_18(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(None)

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_19(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(None)}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_20(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {'XX, XX'.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_21(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(None))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_22(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(None)

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_23(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(None)}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_24(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {'XX, XX'.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_25(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(None))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_26(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_27(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            None
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_28(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append(None)

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_29(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("XXNo project characteristics detectedXX")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_30(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("no project characteristics detected")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_31(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("NO PROJECT CHARACTERISTICS DETECTED")

        return "\n".join(report_lines)

    def xǁGitignoreManagerǁget_detection_report__mutmut_32(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "\n".join(None)

    def xǁGitignoreManagerǁget_detection_report__mutmut_33(self) -> str:
        """
        Get a report of detected project characteristics.

        Returns:
            Detection report as string
        """
        self.detector.reset()
        self.detector.scan_directory(self.project_dir)

        report_lines = ["Project Detection Report", "=" * 24, ""]

        if self.detector.detected_languages:
            report_lines.append(f"Languages: {', '.join(sorted(self.detector.detected_languages))}")

        if self.detector.detected_frameworks:
            report_lines.append(f"Frameworks: {', '.join(sorted(self.detector.detected_frameworks))}")

        if self.detector.detected_tools:
            report_lines.append(f"Tools: {', '.join(sorted(self.detector.detected_tools))}")

        if self.detector.detected_os:
            report_lines.append(f"OS: {', '.join(sorted(self.detector.detected_os))}")

        if not any(
            [
                self.detector.detected_languages,
                self.detector.detected_frameworks,
                self.detector.detected_tools,
                self.detector.detected_os,
            ]
        ):
            report_lines.append("No project characteristics detected")

        return "XX\nXX".join(report_lines)
    
    xǁGitignoreManagerǁget_detection_report__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGitignoreManagerǁget_detection_report__mutmut_1': xǁGitignoreManagerǁget_detection_report__mutmut_1, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_2': xǁGitignoreManagerǁget_detection_report__mutmut_2, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_3': xǁGitignoreManagerǁget_detection_report__mutmut_3, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_4': xǁGitignoreManagerǁget_detection_report__mutmut_4, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_5': xǁGitignoreManagerǁget_detection_report__mutmut_5, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_6': xǁGitignoreManagerǁget_detection_report__mutmut_6, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_7': xǁGitignoreManagerǁget_detection_report__mutmut_7, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_8': xǁGitignoreManagerǁget_detection_report__mutmut_8, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_9': xǁGitignoreManagerǁget_detection_report__mutmut_9, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_10': xǁGitignoreManagerǁget_detection_report__mutmut_10, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_11': xǁGitignoreManagerǁget_detection_report__mutmut_11, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_12': xǁGitignoreManagerǁget_detection_report__mutmut_12, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_13': xǁGitignoreManagerǁget_detection_report__mutmut_13, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_14': xǁGitignoreManagerǁget_detection_report__mutmut_14, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_15': xǁGitignoreManagerǁget_detection_report__mutmut_15, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_16': xǁGitignoreManagerǁget_detection_report__mutmut_16, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_17': xǁGitignoreManagerǁget_detection_report__mutmut_17, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_18': xǁGitignoreManagerǁget_detection_report__mutmut_18, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_19': xǁGitignoreManagerǁget_detection_report__mutmut_19, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_20': xǁGitignoreManagerǁget_detection_report__mutmut_20, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_21': xǁGitignoreManagerǁget_detection_report__mutmut_21, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_22': xǁGitignoreManagerǁget_detection_report__mutmut_22, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_23': xǁGitignoreManagerǁget_detection_report__mutmut_23, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_24': xǁGitignoreManagerǁget_detection_report__mutmut_24, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_25': xǁGitignoreManagerǁget_detection_report__mutmut_25, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_26': xǁGitignoreManagerǁget_detection_report__mutmut_26, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_27': xǁGitignoreManagerǁget_detection_report__mutmut_27, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_28': xǁGitignoreManagerǁget_detection_report__mutmut_28, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_29': xǁGitignoreManagerǁget_detection_report__mutmut_29, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_30': xǁGitignoreManagerǁget_detection_report__mutmut_30, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_31': xǁGitignoreManagerǁget_detection_report__mutmut_31, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_32': xǁGitignoreManagerǁget_detection_report__mutmut_32, 
        'xǁGitignoreManagerǁget_detection_report__mutmut_33': xǁGitignoreManagerǁget_detection_report__mutmut_33
    }
    
    def get_detection_report(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGitignoreManagerǁget_detection_report__mutmut_orig"), object.__getattribute__(self, "xǁGitignoreManagerǁget_detection_report__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_detection_report.__signature__ = _mutmut_signature(xǁGitignoreManagerǁget_detection_report__mutmut_orig)
    xǁGitignoreManagerǁget_detection_report__mutmut_orig.__name__ = 'xǁGitignoreManagerǁget_detection_report'


# 🧰🌍🔚
