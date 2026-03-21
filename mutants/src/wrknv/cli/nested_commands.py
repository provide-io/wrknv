#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Enhanced command registration with nested group support.

This module extends the Foundation Hub to support nested command groups,
allowing natural CLI structures like `wrknv container status` instead of
`wrknv container-status`."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
import inspect
from typing import Any, TypeVar

import click
from provide.foundation import logger
from provide.foundation.hub import get_hub
from provide.foundation.hub.commands import CommandInfo

F = TypeVar("F", bound=Callable[..., Any])
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


def x__extract_click_type__mutmut_orig(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_1(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None and annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_2(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is not None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_3(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is not type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_4(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = None
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_5(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(None)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_6(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is not type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_7(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin not in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_8(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(None, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_9(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, None, None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_10(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr("UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_11(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_12(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", )):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_13(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "XXUnionTypeXX", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_14(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "uniontype", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_15(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UNIONTYPE", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_16(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = None
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_17(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(None)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_18(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_19(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(None)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_20(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is not str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_21(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is not int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_22(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is not float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_23(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is not bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_24(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path and (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_25(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is not Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_26(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) or issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_27(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(None, Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_28(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, None)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_29(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(Path)):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_30(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, )):
        return click.Path()

    # Handle list/tuple
    if origin in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str


def x__extract_click_type__mutmut_31(annotation: Any) -> Any:
    """Extract Click-compatible type from a Python type annotation.

    Args:
        annotation: Python type annotation (e.g., str, int, Path, Optional[str])

    Returns:
        Click-compatible type for the annotation
    """
    from pathlib import Path
    from typing import get_args, get_origin

    # Handle None/NoneType
    if annotation is None or annotation is type(None):
        return str

    # Handle Optional types (Union[X, None])
    origin = get_origin(annotation)
    if origin is type(None):
        return str

    # Handle Union types - extract first non-None type
    import typing

    if origin in (typing.Union, getattr(typing, "UnionType", None)):
        args = get_args(annotation)
        for arg in args:
            if arg is not type(None):
                return _extract_click_type(arg)
        return str

    # Handle basic types
    if annotation is str:
        return str
    if annotation is int:
        return int
    if annotation is float:
        return float
    if annotation is bool:
        return bool
    if annotation is Path or (isinstance(annotation, type) and issubclass(annotation, Path)):
        return click.Path()

    # Handle list/tuple
    if origin not in (list, tuple):
        return str  # Click handles lists differently

    # Default to string
    return str

x__extract_click_type__mutmut_mutants : ClassVar[MutantDict] = {
'x__extract_click_type__mutmut_1': x__extract_click_type__mutmut_1, 
    'x__extract_click_type__mutmut_2': x__extract_click_type__mutmut_2, 
    'x__extract_click_type__mutmut_3': x__extract_click_type__mutmut_3, 
    'x__extract_click_type__mutmut_4': x__extract_click_type__mutmut_4, 
    'x__extract_click_type__mutmut_5': x__extract_click_type__mutmut_5, 
    'x__extract_click_type__mutmut_6': x__extract_click_type__mutmut_6, 
    'x__extract_click_type__mutmut_7': x__extract_click_type__mutmut_7, 
    'x__extract_click_type__mutmut_8': x__extract_click_type__mutmut_8, 
    'x__extract_click_type__mutmut_9': x__extract_click_type__mutmut_9, 
    'x__extract_click_type__mutmut_10': x__extract_click_type__mutmut_10, 
    'x__extract_click_type__mutmut_11': x__extract_click_type__mutmut_11, 
    'x__extract_click_type__mutmut_12': x__extract_click_type__mutmut_12, 
    'x__extract_click_type__mutmut_13': x__extract_click_type__mutmut_13, 
    'x__extract_click_type__mutmut_14': x__extract_click_type__mutmut_14, 
    'x__extract_click_type__mutmut_15': x__extract_click_type__mutmut_15, 
    'x__extract_click_type__mutmut_16': x__extract_click_type__mutmut_16, 
    'x__extract_click_type__mutmut_17': x__extract_click_type__mutmut_17, 
    'x__extract_click_type__mutmut_18': x__extract_click_type__mutmut_18, 
    'x__extract_click_type__mutmut_19': x__extract_click_type__mutmut_19, 
    'x__extract_click_type__mutmut_20': x__extract_click_type__mutmut_20, 
    'x__extract_click_type__mutmut_21': x__extract_click_type__mutmut_21, 
    'x__extract_click_type__mutmut_22': x__extract_click_type__mutmut_22, 
    'x__extract_click_type__mutmut_23': x__extract_click_type__mutmut_23, 
    'x__extract_click_type__mutmut_24': x__extract_click_type__mutmut_24, 
    'x__extract_click_type__mutmut_25': x__extract_click_type__mutmut_25, 
    'x__extract_click_type__mutmut_26': x__extract_click_type__mutmut_26, 
    'x__extract_click_type__mutmut_27': x__extract_click_type__mutmut_27, 
    'x__extract_click_type__mutmut_28': x__extract_click_type__mutmut_28, 
    'x__extract_click_type__mutmut_29': x__extract_click_type__mutmut_29, 
    'x__extract_click_type__mutmut_30': x__extract_click_type__mutmut_30, 
    'x__extract_click_type__mutmut_31': x__extract_click_type__mutmut_31
}

def _extract_click_type(*args, **kwargs):
    result = _mutmut_trampoline(x__extract_click_type__mutmut_orig, x__extract_click_type__mutmut_mutants, args, kwargs)
    return result 

_extract_click_type.__signature__ = _mutmut_signature(x__extract_click_type__mutmut_orig)
x__extract_click_type__mutmut_orig.__name__ = 'x__extract_click_type'


@dataclass
class CommandGroup:
    """Represents a command group that can contain subcommands."""

    name: str
    description: str | None = None
    commands: dict[str, CommandInfo | CommandGroup] = field(default_factory=dict)
    parent: CommandGroup | None = None
    hidden: bool = False

    def add_command(self, name: str, info: CommandInfo | CommandGroup) -> None:
        """Add a subcommand to this group."""
        self.commands[name] = info
        if isinstance(info, CommandGroup):
            info.parent = self

    def get_command(self, path: list[str]) -> CommandInfo | CommandGroup | None:
        """Get a command by path (e.g., ['container', 'status'])."""
        if not path:
            return self

        name = path[0]
        if name not in self.commands:
            return None

        cmd = self.commands[name]
        if len(path) == 1:
            return cmd

        if isinstance(cmd, CommandGroup):
            return cmd.get_command(path[1:])

        return None

    def to_click_group(self) -> click.Group:
        """Convert this command group to a Click group."""
        group = click.Group(
            name=self.name,
            help=self.description,
            hidden=self.hidden,
        )

        for _cmd_name, cmd_info in self.commands.items():
            if isinstance(cmd_info, CommandGroup):
                # Add subgroup
                subgroup = cmd_info.to_click_group()
                group.add_command(subgroup)
            else:
                # Add command
                click_cmd = self._build_click_command(cmd_info)
                if click_cmd:
                    group.add_command(click_cmd)

        return group

    def _build_click_command(self, info: CommandInfo) -> click.Command | None:
        """Build a Click command from CommandInfo."""
        if info.click_command:
            return info.click_command

        func = info.func
        if not callable(func):
            return None

        # Build Click command from function signature
        sig = inspect.signature(func)
        click_func = func

        # Add parameters as Click options/arguments
        for param_name, param in sig.parameters.items():
            if param_name in ("self", "cls", "ctx"):
                continue

            has_default = param.default != inspect.Parameter.empty

            if has_default:
                # Create option
                option_name = f"--{param_name.replace('_', '-')}"
                if param.annotation != inspect.Parameter.empty:
                    param_type = _extract_click_type(param.annotation)

                    if param_type is bool:
                        click_func = click.option(
                            option_name,
                            is_flag=True,
                            default=param.default,
                            help=f"{param_name} flag",
                        )(click_func)
                    else:
                        click_func = click.option(
                            option_name,
                            type=param_type,
                            default=param.default,
                            help=f"{param_name} option",
                        )(click_func)
                else:
                    click_func = click.option(
                        option_name,
                        default=param.default,
                        help=f"{param_name} option",
                    )(click_func)
            # Create argument
            elif param.annotation != inspect.Parameter.empty:
                param_type = _extract_click_type(param.annotation)
                click_func = click.argument(
                    param_name,
                    type=param_type,
                )(click_func)
            else:
                click_func = click.argument(param_name)(click_func)

        return click.Command(
            name=info.name,
            callback=click_func,
            help=info.description,
            hidden=info.hidden,
        )


class NestedCommandRegistry:
    """Registry that supports nested command groups."""

    def xǁNestedCommandRegistryǁ__init____mutmut_orig(self) -> None:
        self.root = CommandGroup(name="cli", description="CLI root")
        self._flat_registry: dict[str, CommandInfo | CommandGroup] = {}

    def xǁNestedCommandRegistryǁ__init____mutmut_1(self) -> None:
        self.root = None
        self._flat_registry: dict[str, CommandInfo | CommandGroup] = {}

    def xǁNestedCommandRegistryǁ__init____mutmut_2(self) -> None:
        self.root = CommandGroup(name=None, description="CLI root")
        self._flat_registry: dict[str, CommandInfo | CommandGroup] = {}

    def xǁNestedCommandRegistryǁ__init____mutmut_3(self) -> None:
        self.root = CommandGroup(name="cli", description=None)
        self._flat_registry: dict[str, CommandInfo | CommandGroup] = {}

    def xǁNestedCommandRegistryǁ__init____mutmut_4(self) -> None:
        self.root = CommandGroup(description="CLI root")
        self._flat_registry: dict[str, CommandInfo | CommandGroup] = {}

    def xǁNestedCommandRegistryǁ__init____mutmut_5(self) -> None:
        self.root = CommandGroup(name="cli", )
        self._flat_registry: dict[str, CommandInfo | CommandGroup] = {}

    def xǁNestedCommandRegistryǁ__init____mutmut_6(self) -> None:
        self.root = CommandGroup(name="XXcliXX", description="CLI root")
        self._flat_registry: dict[str, CommandInfo | CommandGroup] = {}

    def xǁNestedCommandRegistryǁ__init____mutmut_7(self) -> None:
        self.root = CommandGroup(name="CLI", description="CLI root")
        self._flat_registry: dict[str, CommandInfo | CommandGroup] = {}

    def xǁNestedCommandRegistryǁ__init____mutmut_8(self) -> None:
        self.root = CommandGroup(name="cli", description="XXCLI rootXX")
        self._flat_registry: dict[str, CommandInfo | CommandGroup] = {}

    def xǁNestedCommandRegistryǁ__init____mutmut_9(self) -> None:
        self.root = CommandGroup(name="cli", description="cli root")
        self._flat_registry: dict[str, CommandInfo | CommandGroup] = {}

    def xǁNestedCommandRegistryǁ__init____mutmut_10(self) -> None:
        self.root = CommandGroup(name="cli", description="CLI ROOT")
        self._flat_registry: dict[str, CommandInfo | CommandGroup] = {}

    def xǁNestedCommandRegistryǁ__init____mutmut_11(self) -> None:
        self.root = CommandGroup(name="cli", description="CLI root")
        self._flat_registry: dict[str, CommandInfo | CommandGroup] = None
    
    xǁNestedCommandRegistryǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNestedCommandRegistryǁ__init____mutmut_1': xǁNestedCommandRegistryǁ__init____mutmut_1, 
        'xǁNestedCommandRegistryǁ__init____mutmut_2': xǁNestedCommandRegistryǁ__init____mutmut_2, 
        'xǁNestedCommandRegistryǁ__init____mutmut_3': xǁNestedCommandRegistryǁ__init____mutmut_3, 
        'xǁNestedCommandRegistryǁ__init____mutmut_4': xǁNestedCommandRegistryǁ__init____mutmut_4, 
        'xǁNestedCommandRegistryǁ__init____mutmut_5': xǁNestedCommandRegistryǁ__init____mutmut_5, 
        'xǁNestedCommandRegistryǁ__init____mutmut_6': xǁNestedCommandRegistryǁ__init____mutmut_6, 
        'xǁNestedCommandRegistryǁ__init____mutmut_7': xǁNestedCommandRegistryǁ__init____mutmut_7, 
        'xǁNestedCommandRegistryǁ__init____mutmut_8': xǁNestedCommandRegistryǁ__init____mutmut_8, 
        'xǁNestedCommandRegistryǁ__init____mutmut_9': xǁNestedCommandRegistryǁ__init____mutmut_9, 
        'xǁNestedCommandRegistryǁ__init____mutmut_10': xǁNestedCommandRegistryǁ__init____mutmut_10, 
        'xǁNestedCommandRegistryǁ__init____mutmut_11': xǁNestedCommandRegistryǁ__init____mutmut_11
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNestedCommandRegistryǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁNestedCommandRegistryǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁNestedCommandRegistryǁ__init____mutmut_orig)
    xǁNestedCommandRegistryǁ__init____mutmut_orig.__name__ = 'xǁNestedCommandRegistryǁ__init__'

    def xǁNestedCommandRegistryǁregister_command__mutmut_orig(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_1(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = True,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_2(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = True,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_3(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = None

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_4(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = None
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_5(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(None):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_6(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:+1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_7(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-2]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_8(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_9(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = None
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_10(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=None,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_11(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=None,
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_12(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_13(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_14(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(None, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_15(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, None)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_16(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_17(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, )
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_18(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(None)

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_19(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = None
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_20(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = None
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_21(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(None)

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_22(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(None)}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_23(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {'XX XX'.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_24(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i - 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_25(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 2])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_26(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = None

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_27(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[+1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_28(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-2]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_29(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group and func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_30(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is not None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_31(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = None
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_32(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=None,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_33(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=None,
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_34(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=None,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_35(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_36(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_37(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_38(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description and f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_39(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(None, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_40(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, None)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_41(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_42(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, )
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_43(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = None
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_44(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(None)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_45(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry["XX XX".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_46(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(None)
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_47(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(None)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_48(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {'XX XX'.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_49(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = None
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_50(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=None,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_51(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=None,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_52(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=None,
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_53(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=None,
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_54(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=None,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_55(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_56(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_57(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_58(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_59(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_60(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_61(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_62(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description and (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_63(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases and [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_64(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(None) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_65(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category="XX XX".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_66(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:+1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_67(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-2]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_68(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) >= 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_69(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 2 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_70(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(None, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_71(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, None)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_72(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_73(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, )
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_74(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = None
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_75(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(None)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_76(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry["XX XX".join(path)] = info
            logger.info(f"Registered command: {' '.join(path)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_77(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(None)

    def xǁNestedCommandRegistryǁregister_command__mutmut_78(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {' '.join(None)}")

    def xǁNestedCommandRegistryǁregister_command__mutmut_79(
        self,
        name: str,
        func: Callable[..., Any] | None = None,
        description: str | None = None,
        group: bool = False,
        parent: str | None = None,
        hidden: bool = False,
        aliases: list[str] | None = None,
    ) -> None:
        """
        Register a command or command group.

        Args:
            name: Command name (can include spaces for nested commands)
            func: Function to execute (None for groups)
            description: Command/group description
            group: Whether this is a command group
            parent: Parent group name (alternative to space-separated name)
            hidden: Whether to hide from help
            aliases: Command aliases
        """
        # Parse the command path
        path = [*parent.split(), name] if parent else name.split()

        # Get or create parent groups
        current = self.root
        for i, part in enumerate(path[:-1]):
            if part not in current.commands:
                # Create intermediate group
                intermediate = CommandGroup(
                    name=part,
                    description=f"{part} commands",
                )
                current.add_command(part, intermediate)
                if logger.is_debug_enabled():
                    logger.debug(f"Created intermediate group: {part}")

            cmd = current.commands[part]
            if isinstance(cmd, CommandGroup):
                current = cmd
            else:
                raise ValueError(f"Cannot nest under non-group command: {' '.join(path[: i + 1])}")

        # Register the final command or group
        final_name = path[-1]

        if group or func is None:
            # Register as a group
            cmd_group = CommandGroup(
                name=final_name,
                description=description or f"{final_name} commands",
                hidden=hidden,
            )
            current.add_command(final_name, cmd_group)
            self._flat_registry[" ".join(path)] = cmd_group
            logger.info(f"Registered command group: {' '.join(path)}")
        else:
            # Register as a command
            info = CommandInfo(
                name=final_name,
                func=func,
                description=description or (func.__doc__ if func else None),
                aliases=aliases or [],
                hidden=hidden,
                category=" ".join(path[:-1]) if len(path) > 1 else None,
            )
            current.add_command(final_name, info)
            self._flat_registry[" ".join(path)] = info
            logger.info(f"Registered command: {'XX XX'.join(path)}")
    
    xǁNestedCommandRegistryǁregister_command__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNestedCommandRegistryǁregister_command__mutmut_1': xǁNestedCommandRegistryǁregister_command__mutmut_1, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_2': xǁNestedCommandRegistryǁregister_command__mutmut_2, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_3': xǁNestedCommandRegistryǁregister_command__mutmut_3, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_4': xǁNestedCommandRegistryǁregister_command__mutmut_4, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_5': xǁNestedCommandRegistryǁregister_command__mutmut_5, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_6': xǁNestedCommandRegistryǁregister_command__mutmut_6, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_7': xǁNestedCommandRegistryǁregister_command__mutmut_7, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_8': xǁNestedCommandRegistryǁregister_command__mutmut_8, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_9': xǁNestedCommandRegistryǁregister_command__mutmut_9, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_10': xǁNestedCommandRegistryǁregister_command__mutmut_10, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_11': xǁNestedCommandRegistryǁregister_command__mutmut_11, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_12': xǁNestedCommandRegistryǁregister_command__mutmut_12, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_13': xǁNestedCommandRegistryǁregister_command__mutmut_13, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_14': xǁNestedCommandRegistryǁregister_command__mutmut_14, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_15': xǁNestedCommandRegistryǁregister_command__mutmut_15, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_16': xǁNestedCommandRegistryǁregister_command__mutmut_16, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_17': xǁNestedCommandRegistryǁregister_command__mutmut_17, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_18': xǁNestedCommandRegistryǁregister_command__mutmut_18, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_19': xǁNestedCommandRegistryǁregister_command__mutmut_19, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_20': xǁNestedCommandRegistryǁregister_command__mutmut_20, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_21': xǁNestedCommandRegistryǁregister_command__mutmut_21, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_22': xǁNestedCommandRegistryǁregister_command__mutmut_22, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_23': xǁNestedCommandRegistryǁregister_command__mutmut_23, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_24': xǁNestedCommandRegistryǁregister_command__mutmut_24, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_25': xǁNestedCommandRegistryǁregister_command__mutmut_25, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_26': xǁNestedCommandRegistryǁregister_command__mutmut_26, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_27': xǁNestedCommandRegistryǁregister_command__mutmut_27, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_28': xǁNestedCommandRegistryǁregister_command__mutmut_28, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_29': xǁNestedCommandRegistryǁregister_command__mutmut_29, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_30': xǁNestedCommandRegistryǁregister_command__mutmut_30, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_31': xǁNestedCommandRegistryǁregister_command__mutmut_31, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_32': xǁNestedCommandRegistryǁregister_command__mutmut_32, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_33': xǁNestedCommandRegistryǁregister_command__mutmut_33, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_34': xǁNestedCommandRegistryǁregister_command__mutmut_34, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_35': xǁNestedCommandRegistryǁregister_command__mutmut_35, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_36': xǁNestedCommandRegistryǁregister_command__mutmut_36, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_37': xǁNestedCommandRegistryǁregister_command__mutmut_37, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_38': xǁNestedCommandRegistryǁregister_command__mutmut_38, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_39': xǁNestedCommandRegistryǁregister_command__mutmut_39, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_40': xǁNestedCommandRegistryǁregister_command__mutmut_40, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_41': xǁNestedCommandRegistryǁregister_command__mutmut_41, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_42': xǁNestedCommandRegistryǁregister_command__mutmut_42, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_43': xǁNestedCommandRegistryǁregister_command__mutmut_43, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_44': xǁNestedCommandRegistryǁregister_command__mutmut_44, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_45': xǁNestedCommandRegistryǁregister_command__mutmut_45, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_46': xǁNestedCommandRegistryǁregister_command__mutmut_46, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_47': xǁNestedCommandRegistryǁregister_command__mutmut_47, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_48': xǁNestedCommandRegistryǁregister_command__mutmut_48, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_49': xǁNestedCommandRegistryǁregister_command__mutmut_49, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_50': xǁNestedCommandRegistryǁregister_command__mutmut_50, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_51': xǁNestedCommandRegistryǁregister_command__mutmut_51, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_52': xǁNestedCommandRegistryǁregister_command__mutmut_52, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_53': xǁNestedCommandRegistryǁregister_command__mutmut_53, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_54': xǁNestedCommandRegistryǁregister_command__mutmut_54, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_55': xǁNestedCommandRegistryǁregister_command__mutmut_55, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_56': xǁNestedCommandRegistryǁregister_command__mutmut_56, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_57': xǁNestedCommandRegistryǁregister_command__mutmut_57, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_58': xǁNestedCommandRegistryǁregister_command__mutmut_58, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_59': xǁNestedCommandRegistryǁregister_command__mutmut_59, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_60': xǁNestedCommandRegistryǁregister_command__mutmut_60, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_61': xǁNestedCommandRegistryǁregister_command__mutmut_61, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_62': xǁNestedCommandRegistryǁregister_command__mutmut_62, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_63': xǁNestedCommandRegistryǁregister_command__mutmut_63, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_64': xǁNestedCommandRegistryǁregister_command__mutmut_64, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_65': xǁNestedCommandRegistryǁregister_command__mutmut_65, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_66': xǁNestedCommandRegistryǁregister_command__mutmut_66, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_67': xǁNestedCommandRegistryǁregister_command__mutmut_67, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_68': xǁNestedCommandRegistryǁregister_command__mutmut_68, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_69': xǁNestedCommandRegistryǁregister_command__mutmut_69, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_70': xǁNestedCommandRegistryǁregister_command__mutmut_70, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_71': xǁNestedCommandRegistryǁregister_command__mutmut_71, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_72': xǁNestedCommandRegistryǁregister_command__mutmut_72, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_73': xǁNestedCommandRegistryǁregister_command__mutmut_73, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_74': xǁNestedCommandRegistryǁregister_command__mutmut_74, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_75': xǁNestedCommandRegistryǁregister_command__mutmut_75, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_76': xǁNestedCommandRegistryǁregister_command__mutmut_76, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_77': xǁNestedCommandRegistryǁregister_command__mutmut_77, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_78': xǁNestedCommandRegistryǁregister_command__mutmut_78, 
        'xǁNestedCommandRegistryǁregister_command__mutmut_79': xǁNestedCommandRegistryǁregister_command__mutmut_79
    }
    
    def register_command(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNestedCommandRegistryǁregister_command__mutmut_orig"), object.__getattribute__(self, "xǁNestedCommandRegistryǁregister_command__mutmut_mutants"), args, kwargs, self)
        return result 
    
    register_command.__signature__ = _mutmut_signature(xǁNestedCommandRegistryǁregister_command__mutmut_orig)
    xǁNestedCommandRegistryǁregister_command__mutmut_orig.__name__ = 'xǁNestedCommandRegistryǁregister_command'

    def xǁNestedCommandRegistryǁget_command__mutmut_orig(self, name: str) -> CommandInfo | CommandGroup | None:
        """Get a command by name (space-separated path)."""
        return self._flat_registry.get(name)

    def xǁNestedCommandRegistryǁget_command__mutmut_1(self, name: str) -> CommandInfo | CommandGroup | None:
        """Get a command by name (space-separated path)."""
        return self._flat_registry.get(None)
    
    xǁNestedCommandRegistryǁget_command__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNestedCommandRegistryǁget_command__mutmut_1': xǁNestedCommandRegistryǁget_command__mutmut_1
    }
    
    def get_command(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNestedCommandRegistryǁget_command__mutmut_orig"), object.__getattribute__(self, "xǁNestedCommandRegistryǁget_command__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_command.__signature__ = _mutmut_signature(xǁNestedCommandRegistryǁget_command__mutmut_orig)
    xǁNestedCommandRegistryǁget_command__mutmut_orig.__name__ = 'xǁNestedCommandRegistryǁget_command'

    def to_click_group(self) -> click.Group:
        """Convert the entire registry to a Click group."""
        return self.root.to_click_group()


# Global nested registry
_nested_registry = NestedCommandRegistry()


def x_register_nested_command__mutmut_orig(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_1(
    name: str,
    *,
    description: str | None = None,
    group: bool = True,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_2(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = True,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_3(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=None,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_4(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_5(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=None,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_6(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=None,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_7(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=None,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_8(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=None,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_9(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=None,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_10(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_11(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_12(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_13(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_14(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_15(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_16(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_17(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_18(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = None
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_19(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = None
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_20(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = None

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_21(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(None, "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_22(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", None)

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_23(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace("-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_24(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", )

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_25(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace("XX XX", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_26(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "XX-XX")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_27(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=None,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_28(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=None,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_29(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension=None,
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_30(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata=None,
        )

        return func

    return decorator


def x_register_nested_command__mutmut_31(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_32(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_33(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_34(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            )

        return func

    return decorator


def x_register_nested_command__mutmut_35(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="XXcommandXX",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_36(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="COMMAND",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_37(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "XXnested_pathXX": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_38(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "NESTED_PATH": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_39(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "XXis_groupXX": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_40(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "IS_GROUP": group,
                "description": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_41(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "XXdescriptionXX": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_42(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "DESCRIPTION": description,
                "hidden": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_43(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "XXhiddenXX": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_44(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "HIDDEN": hidden,
                "aliases": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_45(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "XXaliasesXX": aliases,
            },
        )

        return func

    return decorator


def x_register_nested_command__mutmut_46(
    name: str,
    *,
    description: str | None = None,
    group: bool = False,
    parent: str | None = None,
    hidden: bool = False,
    aliases: list[str] | None = None,
) -> Callable[[F], F]:
    """
    Register a command with support for nested groups.

    Examples:
        # Register a simple command
        @register_nested_command("status")
        def status():
            pass

        # Register a command group
        @register_nested_command("container", group=True)
        def container_group():
            pass

        # Register a subcommand (two ways)
        @register_nested_command("container status")
        def container_status():
            pass

        # Or using parent parameter
        @register_nested_command("status", parent="container")
        def container_status():
            pass

    Args:
        name: Command name (can be space-separated for nesting)
        description: Command description
        group: Whether this is a command group
        parent: Parent group (alternative to space-separated name)
        hidden: Hide from help
        aliases: Command aliases

    Returns:
        Decorator function
    """

    def decorator(func: F) -> F:
        _nested_registry.register_command(
            name=name,
            func=func if not group else None,
            description=description,
            group=group,
            parent=parent,
            hidden=hidden,
            aliases=aliases,
        )

        # Also register in the Foundation Hub for compatibility
        hub = get_hub()
        full_name = f"{parent} {name}" if parent else name
        flat_name = full_name.replace(" ", "-")

        hub.register(
            name=flat_name,
            value=func,
            dimension="command",
            metadata={
                "nested_path": full_name,
                "is_group": group,
                "description": description,
                "hidden": hidden,
                "ALIASES": aliases,
            },
        )

        return func

    return decorator

x_register_nested_command__mutmut_mutants : ClassVar[MutantDict] = {
'x_register_nested_command__mutmut_1': x_register_nested_command__mutmut_1, 
    'x_register_nested_command__mutmut_2': x_register_nested_command__mutmut_2, 
    'x_register_nested_command__mutmut_3': x_register_nested_command__mutmut_3, 
    'x_register_nested_command__mutmut_4': x_register_nested_command__mutmut_4, 
    'x_register_nested_command__mutmut_5': x_register_nested_command__mutmut_5, 
    'x_register_nested_command__mutmut_6': x_register_nested_command__mutmut_6, 
    'x_register_nested_command__mutmut_7': x_register_nested_command__mutmut_7, 
    'x_register_nested_command__mutmut_8': x_register_nested_command__mutmut_8, 
    'x_register_nested_command__mutmut_9': x_register_nested_command__mutmut_9, 
    'x_register_nested_command__mutmut_10': x_register_nested_command__mutmut_10, 
    'x_register_nested_command__mutmut_11': x_register_nested_command__mutmut_11, 
    'x_register_nested_command__mutmut_12': x_register_nested_command__mutmut_12, 
    'x_register_nested_command__mutmut_13': x_register_nested_command__mutmut_13, 
    'x_register_nested_command__mutmut_14': x_register_nested_command__mutmut_14, 
    'x_register_nested_command__mutmut_15': x_register_nested_command__mutmut_15, 
    'x_register_nested_command__mutmut_16': x_register_nested_command__mutmut_16, 
    'x_register_nested_command__mutmut_17': x_register_nested_command__mutmut_17, 
    'x_register_nested_command__mutmut_18': x_register_nested_command__mutmut_18, 
    'x_register_nested_command__mutmut_19': x_register_nested_command__mutmut_19, 
    'x_register_nested_command__mutmut_20': x_register_nested_command__mutmut_20, 
    'x_register_nested_command__mutmut_21': x_register_nested_command__mutmut_21, 
    'x_register_nested_command__mutmut_22': x_register_nested_command__mutmut_22, 
    'x_register_nested_command__mutmut_23': x_register_nested_command__mutmut_23, 
    'x_register_nested_command__mutmut_24': x_register_nested_command__mutmut_24, 
    'x_register_nested_command__mutmut_25': x_register_nested_command__mutmut_25, 
    'x_register_nested_command__mutmut_26': x_register_nested_command__mutmut_26, 
    'x_register_nested_command__mutmut_27': x_register_nested_command__mutmut_27, 
    'x_register_nested_command__mutmut_28': x_register_nested_command__mutmut_28, 
    'x_register_nested_command__mutmut_29': x_register_nested_command__mutmut_29, 
    'x_register_nested_command__mutmut_30': x_register_nested_command__mutmut_30, 
    'x_register_nested_command__mutmut_31': x_register_nested_command__mutmut_31, 
    'x_register_nested_command__mutmut_32': x_register_nested_command__mutmut_32, 
    'x_register_nested_command__mutmut_33': x_register_nested_command__mutmut_33, 
    'x_register_nested_command__mutmut_34': x_register_nested_command__mutmut_34, 
    'x_register_nested_command__mutmut_35': x_register_nested_command__mutmut_35, 
    'x_register_nested_command__mutmut_36': x_register_nested_command__mutmut_36, 
    'x_register_nested_command__mutmut_37': x_register_nested_command__mutmut_37, 
    'x_register_nested_command__mutmut_38': x_register_nested_command__mutmut_38, 
    'x_register_nested_command__mutmut_39': x_register_nested_command__mutmut_39, 
    'x_register_nested_command__mutmut_40': x_register_nested_command__mutmut_40, 
    'x_register_nested_command__mutmut_41': x_register_nested_command__mutmut_41, 
    'x_register_nested_command__mutmut_42': x_register_nested_command__mutmut_42, 
    'x_register_nested_command__mutmut_43': x_register_nested_command__mutmut_43, 
    'x_register_nested_command__mutmut_44': x_register_nested_command__mutmut_44, 
    'x_register_nested_command__mutmut_45': x_register_nested_command__mutmut_45, 
    'x_register_nested_command__mutmut_46': x_register_nested_command__mutmut_46
}

def register_nested_command(*args, **kwargs):
    result = _mutmut_trampoline(x_register_nested_command__mutmut_orig, x_register_nested_command__mutmut_mutants, args, kwargs)
    return result 

register_nested_command.__signature__ = _mutmut_signature(x_register_nested_command__mutmut_orig)
x_register_nested_command__mutmut_orig.__name__ = 'x_register_nested_command'


def x_create_nested_cli__mutmut_orig(
    name: str = "wrknv",
    version: str = "0.3.0",
    help: str | None = None,
) -> click.Group:
    """
    Create a CLI with nested command groups.

    Args:
        name: CLI name
        version: CLI version
        help: CLI help text

    Returns:
        Click Group with nested commands
    """
    cli = _nested_registry.root.to_click_group()
    cli.name = name

    if help:
        cli.help = help

    # Add version option
    @cli.command(hidden=True)
    @click.option("--version", is_flag=True, help="Show version")
    def version_cmd(version: bool) -> None:
        if version:
            click.echo(f"{name} {version}")

    return cli


def x_create_nested_cli__mutmut_1(
    name: str = "XXwrknvXX",
    version: str = "0.3.0",
    help: str | None = None,
) -> click.Group:
    """
    Create a CLI with nested command groups.

    Args:
        name: CLI name
        version: CLI version
        help: CLI help text

    Returns:
        Click Group with nested commands
    """
    cli = _nested_registry.root.to_click_group()
    cli.name = name

    if help:
        cli.help = help

    # Add version option
    @cli.command(hidden=True)
    @click.option("--version", is_flag=True, help="Show version")
    def version_cmd(version: bool) -> None:
        if version:
            click.echo(f"{name} {version}")

    return cli


def x_create_nested_cli__mutmut_2(
    name: str = "WRKNV",
    version: str = "0.3.0",
    help: str | None = None,
) -> click.Group:
    """
    Create a CLI with nested command groups.

    Args:
        name: CLI name
        version: CLI version
        help: CLI help text

    Returns:
        Click Group with nested commands
    """
    cli = _nested_registry.root.to_click_group()
    cli.name = name

    if help:
        cli.help = help

    # Add version option
    @cli.command(hidden=True)
    @click.option("--version", is_flag=True, help="Show version")
    def version_cmd(version: bool) -> None:
        if version:
            click.echo(f"{name} {version}")

    return cli


def x_create_nested_cli__mutmut_3(
    name: str = "wrknv",
    version: str = "XX0.3.0XX",
    help: str | None = None,
) -> click.Group:
    """
    Create a CLI with nested command groups.

    Args:
        name: CLI name
        version: CLI version
        help: CLI help text

    Returns:
        Click Group with nested commands
    """
    cli = _nested_registry.root.to_click_group()
    cli.name = name

    if help:
        cli.help = help

    # Add version option
    @cli.command(hidden=True)
    @click.option("--version", is_flag=True, help="Show version")
    def version_cmd(version: bool) -> None:
        if version:
            click.echo(f"{name} {version}")

    return cli


def x_create_nested_cli__mutmut_4(
    name: str = "wrknv",
    version: str = "0.3.0",
    help: str | None = None,
) -> click.Group:
    """
    Create a CLI with nested command groups.

    Args:
        name: CLI name
        version: CLI version
        help: CLI help text

    Returns:
        Click Group with nested commands
    """
    cli = None
    cli.name = name

    if help:
        cli.help = help

    # Add version option
    @cli.command(hidden=True)
    @click.option("--version", is_flag=True, help="Show version")
    def version_cmd(version: bool) -> None:
        if version:
            click.echo(f"{name} {version}")

    return cli


def x_create_nested_cli__mutmut_5(
    name: str = "wrknv",
    version: str = "0.3.0",
    help: str | None = None,
) -> click.Group:
    """
    Create a CLI with nested command groups.

    Args:
        name: CLI name
        version: CLI version
        help: CLI help text

    Returns:
        Click Group with nested commands
    """
    cli = _nested_registry.root.to_click_group()
    cli.name = None

    if help:
        cli.help = help

    # Add version option
    @cli.command(hidden=True)
    @click.option("--version", is_flag=True, help="Show version")
    def version_cmd(version: bool) -> None:
        if version:
            click.echo(f"{name} {version}")

    return cli


def x_create_nested_cli__mutmut_6(
    name: str = "wrknv",
    version: str = "0.3.0",
    help: str | None = None,
) -> click.Group:
    """
    Create a CLI with nested command groups.

    Args:
        name: CLI name
        version: CLI version
        help: CLI help text

    Returns:
        Click Group with nested commands
    """
    cli = _nested_registry.root.to_click_group()
    cli.name = name

    if help:
        cli.help = None

    # Add version option
    @cli.command(hidden=True)
    @click.option("--version", is_flag=True, help="Show version")
    def version_cmd(version: bool) -> None:
        if version:
            click.echo(f"{name} {version}")

    return cli

x_create_nested_cli__mutmut_mutants : ClassVar[MutantDict] = {
'x_create_nested_cli__mutmut_1': x_create_nested_cli__mutmut_1, 
    'x_create_nested_cli__mutmut_2': x_create_nested_cli__mutmut_2, 
    'x_create_nested_cli__mutmut_3': x_create_nested_cli__mutmut_3, 
    'x_create_nested_cli__mutmut_4': x_create_nested_cli__mutmut_4, 
    'x_create_nested_cli__mutmut_5': x_create_nested_cli__mutmut_5, 
    'x_create_nested_cli__mutmut_6': x_create_nested_cli__mutmut_6
}

def create_nested_cli(*args, **kwargs):
    result = _mutmut_trampoline(x_create_nested_cli__mutmut_orig, x_create_nested_cli__mutmut_mutants, args, kwargs)
    return result 

create_nested_cli.__signature__ = _mutmut_signature(x_create_nested_cli__mutmut_orig)
x_create_nested_cli__mutmut_orig.__name__ = 'x_create_nested_cli'


def get_nested_registry() -> NestedCommandRegistry:
    """Get the global nested command registry."""
    return _nested_registry


# 🧰🌍🔚
