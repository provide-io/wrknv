#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Display convenience helpers for `WorkenvConfig`."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wrknv.config.core import WorkenvConfig
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


class WorkenvConfigDisplay:
    """Handles displaying configuration information."""

    def xǁWorkenvConfigDisplayǁ__init____mutmut_orig(self, config: WorkenvConfig) -> None:
        """Initialize display handler with config instance."""
        self.config = config

    def xǁWorkenvConfigDisplayǁ__init____mutmut_1(self, config: WorkenvConfig) -> None:
        """Initialize display handler with config instance."""
        self.config = None
    
    xǁWorkenvConfigDisplayǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvConfigDisplayǁ__init____mutmut_1': xǁWorkenvConfigDisplayǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvConfigDisplayǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁWorkenvConfigDisplayǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁWorkenvConfigDisplayǁ__init____mutmut_orig)
    xǁWorkenvConfigDisplayǁ__init____mutmut_orig.__name__ = 'xǁWorkenvConfigDisplayǁ__init__'

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_orig(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_1(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(None)

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_2(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = None
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_3(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name and "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_4(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "XX(not set)XX"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_5(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(NOT SET)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_6(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = None
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_7(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version and "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_8(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "XX(not set)XX"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_9(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(NOT SET)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_10(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(None)

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_11(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(None)

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_12(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info(None)
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_13(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("XX\n  Tools:XX")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_14(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_15(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  TOOLS:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_16(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = None
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_17(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get(None, "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_18(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", None) if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_19(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_20(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", ) if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_21(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("XXversionXX", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_22(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("VERSION", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_23(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "XXlatestXX") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_24(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "LATEST") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_25(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(None)

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_26(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info(None)
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_27(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("XX\n  Profiles:XX")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_28(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_29(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  PROFILES:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_30(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(None)

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_31(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info(None)
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_32(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("XX\n  Settings:XX")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_33(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_34(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  SETTINGS:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_35(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(None)
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_36(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(None)
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_37(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(None)
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_38(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(None)
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_39(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(None)
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_40(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(None)

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_41(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info(None)
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_42(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("XX\n  Container:XX")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_43(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_44(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  CONTAINER:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_45(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(None)
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_46(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(None)
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_47(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(None)
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_48(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(None)
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_49(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(None)

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_50(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info(None)
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_51(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("XX\n  Environment:XX")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_52(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_53(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  ENVIRONMENT:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_54(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(None)
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_55(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(None)

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_56(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info(None)
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_57(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("XX\n  Gitignore:XX")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_58(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_59(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  GITIGNORE:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_60(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(None)
                else:
                    echo_info(f"    {key}: {value}")

    def xǁWorkenvConfigDisplayǁshow_config__mutmut_61(self) -> None:
        """Display configuration in a readable format."""
        from provide.foundation.cli import echo_info, echo_success

        echo_success(f"Configuration: {self.config.config_path}")

        # Project metadata
        project_name = self.config.project_name or "(not set)"
        version = self.config.version or "(not set)"
        echo_info(f"  Project: {project_name} v{version}")

        if self.config.description:
            echo_info(f"  Description: {self.config.description}")

        if self.config.tools:
            echo_info("\n  Tools:")
            for tool, config in self.config.tools.items():
                version = config.get("version", "latest") if isinstance(config, dict) else config
                echo_info(f"    {tool}: {version}")

        if self.config.profiles:
            echo_info("\n  Profiles:")
            for profile in self.config.profiles:
                echo_info(f"    - {profile}")

        echo_info("\n  Settings:")
        echo_info(f"    auto_install: {self.config.workenv.auto_install}")
        echo_info(f"    use_cache: {self.config.workenv.use_cache}")
        echo_info(f"    cache_ttl: {self.config.workenv.cache_ttl}")
        echo_info(f"    log_level: {self.config.workenv.log_level}")
        echo_info(f"    container_runtime: {self.config.workenv.container_runtime}")
        echo_info(f"    container_registry: {self.config.workenv.container_registry}")

        if self.config.container:
            echo_info("\n  Container:")
            echo_info(f"    enabled: {self.config.container.enabled}")
            echo_info(f"    base_image: {self.config.container.base_image}")
            echo_info(f"    python_version: {self.config.container.python_version}")
            if self.config.container.volumes:
                echo_info(f"    volumes: {len(self.config.container.volumes)} configured")
            if self.config.container.environment:
                echo_info(f"    environment: {len(self.config.container.environment)} variables")

        if self.config.env:
            echo_info("\n  Environment:")
            for key, value in self.config.env.items():
                if isinstance(value, dict):
                    echo_info(f"    {key}: {len(value)} items")
                else:
                    echo_info(f"    {key}: {value}")

        if self.config.gitignore:
            echo_info("\n  Gitignore:")
            for key, value in self.config.gitignore.items():
                if isinstance(value, list):
                    echo_info(f"    {key}: {len(value)} patterns")
                else:
                    echo_info(None)
    
    xǁWorkenvConfigDisplayǁshow_config__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWorkenvConfigDisplayǁshow_config__mutmut_1': xǁWorkenvConfigDisplayǁshow_config__mutmut_1, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_2': xǁWorkenvConfigDisplayǁshow_config__mutmut_2, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_3': xǁWorkenvConfigDisplayǁshow_config__mutmut_3, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_4': xǁWorkenvConfigDisplayǁshow_config__mutmut_4, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_5': xǁWorkenvConfigDisplayǁshow_config__mutmut_5, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_6': xǁWorkenvConfigDisplayǁshow_config__mutmut_6, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_7': xǁWorkenvConfigDisplayǁshow_config__mutmut_7, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_8': xǁWorkenvConfigDisplayǁshow_config__mutmut_8, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_9': xǁWorkenvConfigDisplayǁshow_config__mutmut_9, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_10': xǁWorkenvConfigDisplayǁshow_config__mutmut_10, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_11': xǁWorkenvConfigDisplayǁshow_config__mutmut_11, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_12': xǁWorkenvConfigDisplayǁshow_config__mutmut_12, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_13': xǁWorkenvConfigDisplayǁshow_config__mutmut_13, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_14': xǁWorkenvConfigDisplayǁshow_config__mutmut_14, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_15': xǁWorkenvConfigDisplayǁshow_config__mutmut_15, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_16': xǁWorkenvConfigDisplayǁshow_config__mutmut_16, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_17': xǁWorkenvConfigDisplayǁshow_config__mutmut_17, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_18': xǁWorkenvConfigDisplayǁshow_config__mutmut_18, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_19': xǁWorkenvConfigDisplayǁshow_config__mutmut_19, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_20': xǁWorkenvConfigDisplayǁshow_config__mutmut_20, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_21': xǁWorkenvConfigDisplayǁshow_config__mutmut_21, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_22': xǁWorkenvConfigDisplayǁshow_config__mutmut_22, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_23': xǁWorkenvConfigDisplayǁshow_config__mutmut_23, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_24': xǁWorkenvConfigDisplayǁshow_config__mutmut_24, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_25': xǁWorkenvConfigDisplayǁshow_config__mutmut_25, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_26': xǁWorkenvConfigDisplayǁshow_config__mutmut_26, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_27': xǁWorkenvConfigDisplayǁshow_config__mutmut_27, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_28': xǁWorkenvConfigDisplayǁshow_config__mutmut_28, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_29': xǁWorkenvConfigDisplayǁshow_config__mutmut_29, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_30': xǁWorkenvConfigDisplayǁshow_config__mutmut_30, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_31': xǁWorkenvConfigDisplayǁshow_config__mutmut_31, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_32': xǁWorkenvConfigDisplayǁshow_config__mutmut_32, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_33': xǁWorkenvConfigDisplayǁshow_config__mutmut_33, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_34': xǁWorkenvConfigDisplayǁshow_config__mutmut_34, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_35': xǁWorkenvConfigDisplayǁshow_config__mutmut_35, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_36': xǁWorkenvConfigDisplayǁshow_config__mutmut_36, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_37': xǁWorkenvConfigDisplayǁshow_config__mutmut_37, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_38': xǁWorkenvConfigDisplayǁshow_config__mutmut_38, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_39': xǁWorkenvConfigDisplayǁshow_config__mutmut_39, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_40': xǁWorkenvConfigDisplayǁshow_config__mutmut_40, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_41': xǁWorkenvConfigDisplayǁshow_config__mutmut_41, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_42': xǁWorkenvConfigDisplayǁshow_config__mutmut_42, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_43': xǁWorkenvConfigDisplayǁshow_config__mutmut_43, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_44': xǁWorkenvConfigDisplayǁshow_config__mutmut_44, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_45': xǁWorkenvConfigDisplayǁshow_config__mutmut_45, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_46': xǁWorkenvConfigDisplayǁshow_config__mutmut_46, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_47': xǁWorkenvConfigDisplayǁshow_config__mutmut_47, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_48': xǁWorkenvConfigDisplayǁshow_config__mutmut_48, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_49': xǁWorkenvConfigDisplayǁshow_config__mutmut_49, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_50': xǁWorkenvConfigDisplayǁshow_config__mutmut_50, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_51': xǁWorkenvConfigDisplayǁshow_config__mutmut_51, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_52': xǁWorkenvConfigDisplayǁshow_config__mutmut_52, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_53': xǁWorkenvConfigDisplayǁshow_config__mutmut_53, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_54': xǁWorkenvConfigDisplayǁshow_config__mutmut_54, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_55': xǁWorkenvConfigDisplayǁshow_config__mutmut_55, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_56': xǁWorkenvConfigDisplayǁshow_config__mutmut_56, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_57': xǁWorkenvConfigDisplayǁshow_config__mutmut_57, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_58': xǁWorkenvConfigDisplayǁshow_config__mutmut_58, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_59': xǁWorkenvConfigDisplayǁshow_config__mutmut_59, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_60': xǁWorkenvConfigDisplayǁshow_config__mutmut_60, 
        'xǁWorkenvConfigDisplayǁshow_config__mutmut_61': xǁWorkenvConfigDisplayǁshow_config__mutmut_61
    }
    
    def show_config(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWorkenvConfigDisplayǁshow_config__mutmut_orig"), object.__getattribute__(self, "xǁWorkenvConfigDisplayǁshow_config__mutmut_mutants"), args, kwargs, self)
        return result 
    
    show_config.__signature__ = _mutmut_signature(xǁWorkenvConfigDisplayǁshow_config__mutmut_orig)
    xǁWorkenvConfigDisplayǁshow_config__mutmut_orig.__name__ = 'xǁWorkenvConfigDisplayǁshow_config'


# 🧰🌍🔚
