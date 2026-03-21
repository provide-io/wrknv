#
# SPDX-FileCopyrightText: Copyright (c) provide.io llc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#

"""Visual UX Enhancements
======================
Emoji and color support for enhanced CLI output."""

from __future__ import annotations

from rich.console import Console
from rich.theme import Theme

# Custom theme with colors
WRKENV_THEME = Theme(
    {
        "info": "blue",
        "success": "green",
        "warning": "yellow",
        "error": "red",
        "dim": "dim white",
        "highlight": "cyan",
    }
)
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


# Emoji constants for consistent visual feedback
class Emoji:
    """Emoji constants for visual feedback."""

    # Tool emojis
    TERRAFORM = "🔷"
    OPENTOFU = "🌿"
    GO = "🐹"

    # Action emojis
    BUILD = "🔨"
    START = "🚀"
    STOP = "⏹️"
    CLEAN = "🧹"
    STATUS = "📊"
    SYNC = "🔄"
    DOWNLOAD = "⬇️"
    INSTALL = "📥"

    # Container emojis
    CONTAINER = "🐳"

    # Status emojis
    ERROR = "❌"
    WARNING = "⚠️"
    INFO = "ⓘ"
    SUCCESS = "✅"
    RUNNING = "🟢"
    STOPPED = "🟡"

    # Environment emojis
    PROFILE = "👤"
    WORKBENCH = "🧰"
    CONFIG = "⚙️"

    # Language emojis
    PYTHON = "🐍"
    UV = "📦"
    PACKAGE = "📦"


def x_get_console__mutmut_orig() -> Console:
    """Get a configured Rich console with theme."""
    return Console(theme=WRKENV_THEME)


def x_get_console__mutmut_1() -> Console:
    """Get a configured Rich console with theme."""
    return Console(theme=None)

x_get_console__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_console__mutmut_1': x_get_console__mutmut_1
}

def get_console(*args, **kwargs):
    result = _mutmut_trampoline(x_get_console__mutmut_orig, x_get_console__mutmut_mutants, args, kwargs)
    return result 

get_console.__signature__ = _mutmut_signature(x_get_console__mutmut_orig)
x_get_console__mutmut_orig.__name__ = 'x_get_console'


def x_print_header__mutmut_orig(text: str, emoji: str | None = None) -> None:
    """Print a styled header."""
    console = get_console()
    if emoji:
        text = f"{emoji} {text}"
    console.print(f"[highlight]{text}[/highlight]")
    console.print(f"[highlight]{'=' * len(text)}[/highlight]")


def x_print_header__mutmut_1(text: str, emoji: str | None = None) -> None:
    """Print a styled header."""
    console = None
    if emoji:
        text = f"{emoji} {text}"
    console.print(f"[highlight]{text}[/highlight]")
    console.print(f"[highlight]{'=' * len(text)}[/highlight]")


def x_print_header__mutmut_2(text: str, emoji: str | None = None) -> None:
    """Print a styled header."""
    console = get_console()
    if emoji:
        text = None
    console.print(f"[highlight]{text}[/highlight]")
    console.print(f"[highlight]{'=' * len(text)}[/highlight]")


def x_print_header__mutmut_3(text: str, emoji: str | None = None) -> None:
    """Print a styled header."""
    console = get_console()
    if emoji:
        text = f"{emoji} {text}"
    console.print(None)
    console.print(f"[highlight]{'=' * len(text)}[/highlight]")


def x_print_header__mutmut_4(text: str, emoji: str | None = None) -> None:
    """Print a styled header."""
    console = get_console()
    if emoji:
        text = f"{emoji} {text}"
    console.print(f"[highlight]{text}[/highlight]")
    console.print(None)


def x_print_header__mutmut_5(text: str, emoji: str | None = None) -> None:
    """Print a styled header."""
    console = get_console()
    if emoji:
        text = f"{emoji} {text}"
    console.print(f"[highlight]{text}[/highlight]")
    console.print(f"[highlight]{'=' / len(text)}[/highlight]")


def x_print_header__mutmut_6(text: str, emoji: str | None = None) -> None:
    """Print a styled header."""
    console = get_console()
    if emoji:
        text = f"{emoji} {text}"
    console.print(f"[highlight]{text}[/highlight]")
    console.print(f"[highlight]{'XX=XX' * len(text)}[/highlight]")

x_print_header__mutmut_mutants : ClassVar[MutantDict] = {
'x_print_header__mutmut_1': x_print_header__mutmut_1, 
    'x_print_header__mutmut_2': x_print_header__mutmut_2, 
    'x_print_header__mutmut_3': x_print_header__mutmut_3, 
    'x_print_header__mutmut_4': x_print_header__mutmut_4, 
    'x_print_header__mutmut_5': x_print_header__mutmut_5, 
    'x_print_header__mutmut_6': x_print_header__mutmut_6
}

def print_header(*args, **kwargs):
    result = _mutmut_trampoline(x_print_header__mutmut_orig, x_print_header__mutmut_mutants, args, kwargs)
    return result 

print_header.__signature__ = _mutmut_signature(x_print_header__mutmut_orig)
x_print_header__mutmut_orig.__name__ = 'x_print_header'


def x_print_info__mutmut_orig(text: str, emoji: str = Emoji.INFO) -> None:
    """Print an info message."""
    console = get_console()
    console.print(f"{emoji} [info]{text}[/info]")


def x_print_info__mutmut_1(text: str, emoji: str = Emoji.INFO) -> None:
    """Print an info message."""
    console = None
    console.print(f"{emoji} [info]{text}[/info]")


def x_print_info__mutmut_2(text: str, emoji: str = Emoji.INFO) -> None:
    """Print an info message."""
    console = get_console()
    console.print(None)

x_print_info__mutmut_mutants : ClassVar[MutantDict] = {
'x_print_info__mutmut_1': x_print_info__mutmut_1, 
    'x_print_info__mutmut_2': x_print_info__mutmut_2
}

def print_info(*args, **kwargs):
    result = _mutmut_trampoline(x_print_info__mutmut_orig, x_print_info__mutmut_mutants, args, kwargs)
    return result 

print_info.__signature__ = _mutmut_signature(x_print_info__mutmut_orig)
x_print_info__mutmut_orig.__name__ = 'x_print_info'


def x_print_success__mutmut_orig(text: str, emoji: str = Emoji.SUCCESS) -> None:
    """Print a success message."""
    console = get_console()
    console.print(f"{emoji} [success]{text}[/success]")


def x_print_success__mutmut_1(text: str, emoji: str = Emoji.SUCCESS) -> None:
    """Print a success message."""
    console = None
    console.print(f"{emoji} [success]{text}[/success]")


def x_print_success__mutmut_2(text: str, emoji: str = Emoji.SUCCESS) -> None:
    """Print a success message."""
    console = get_console()
    console.print(None)

x_print_success__mutmut_mutants : ClassVar[MutantDict] = {
'x_print_success__mutmut_1': x_print_success__mutmut_1, 
    'x_print_success__mutmut_2': x_print_success__mutmut_2
}

def print_success(*args, **kwargs):
    result = _mutmut_trampoline(x_print_success__mutmut_orig, x_print_success__mutmut_mutants, args, kwargs)
    return result 

print_success.__signature__ = _mutmut_signature(x_print_success__mutmut_orig)
x_print_success__mutmut_orig.__name__ = 'x_print_success'


def x_print_warning__mutmut_orig(text: str, emoji: str = Emoji.WARNING) -> None:
    """Print a warning message."""
    console = get_console()
    console.print(f"{emoji} [warning]{text}[/warning]")


def x_print_warning__mutmut_1(text: str, emoji: str = Emoji.WARNING) -> None:
    """Print a warning message."""
    console = None
    console.print(f"{emoji} [warning]{text}[/warning]")


def x_print_warning__mutmut_2(text: str, emoji: str = Emoji.WARNING) -> None:
    """Print a warning message."""
    console = get_console()
    console.print(None)

x_print_warning__mutmut_mutants : ClassVar[MutantDict] = {
'x_print_warning__mutmut_1': x_print_warning__mutmut_1, 
    'x_print_warning__mutmut_2': x_print_warning__mutmut_2
}

def print_warning(*args, **kwargs):
    result = _mutmut_trampoline(x_print_warning__mutmut_orig, x_print_warning__mutmut_mutants, args, kwargs)
    return result 

print_warning.__signature__ = _mutmut_signature(x_print_warning__mutmut_orig)
x_print_warning__mutmut_orig.__name__ = 'x_print_warning'


def x_print_error__mutmut_orig(text: str, emoji: str = Emoji.ERROR) -> None:
    """Print an error message."""
    console = get_console()
    console.print(f"{emoji} [error]{text}[/error]", style="error")


def x_print_error__mutmut_1(text: str, emoji: str = Emoji.ERROR) -> None:
    """Print an error message."""
    console = None
    console.print(f"{emoji} [error]{text}[/error]", style="error")


def x_print_error__mutmut_2(text: str, emoji: str = Emoji.ERROR) -> None:
    """Print an error message."""
    console = get_console()
    console.print(None, style="error")


def x_print_error__mutmut_3(text: str, emoji: str = Emoji.ERROR) -> None:
    """Print an error message."""
    console = get_console()
    console.print(f"{emoji} [error]{text}[/error]", style=None)


def x_print_error__mutmut_4(text: str, emoji: str = Emoji.ERROR) -> None:
    """Print an error message."""
    console = get_console()
    console.print(style="error")


def x_print_error__mutmut_5(text: str, emoji: str = Emoji.ERROR) -> None:
    """Print an error message."""
    console = get_console()
    console.print(f"{emoji} [error]{text}[/error]", )


def x_print_error__mutmut_6(text: str, emoji: str = Emoji.ERROR) -> None:
    """Print an error message."""
    console = get_console()
    console.print(f"{emoji} [error]{text}[/error]", style="XXerrorXX")


def x_print_error__mutmut_7(text: str, emoji: str = Emoji.ERROR) -> None:
    """Print an error message."""
    console = get_console()
    console.print(f"{emoji} [error]{text}[/error]", style="ERROR")

x_print_error__mutmut_mutants : ClassVar[MutantDict] = {
'x_print_error__mutmut_1': x_print_error__mutmut_1, 
    'x_print_error__mutmut_2': x_print_error__mutmut_2, 
    'x_print_error__mutmut_3': x_print_error__mutmut_3, 
    'x_print_error__mutmut_4': x_print_error__mutmut_4, 
    'x_print_error__mutmut_5': x_print_error__mutmut_5, 
    'x_print_error__mutmut_6': x_print_error__mutmut_6, 
    'x_print_error__mutmut_7': x_print_error__mutmut_7
}

def print_error(*args, **kwargs):
    result = _mutmut_trampoline(x_print_error__mutmut_orig, x_print_error__mutmut_mutants, args, kwargs)
    return result 

print_error.__signature__ = _mutmut_signature(x_print_error__mutmut_orig)
x_print_error__mutmut_orig.__name__ = 'x_print_error'


def x_print_dim__mutmut_orig(text: str) -> None:
    """Print dimmed text."""
    console = get_console()
    console.print(f"[dim]{text}[/dim]")


def x_print_dim__mutmut_1(text: str) -> None:
    """Print dimmed text."""
    console = None
    console.print(f"[dim]{text}[/dim]")


def x_print_dim__mutmut_2(text: str) -> None:
    """Print dimmed text."""
    console = get_console()
    console.print(None)

x_print_dim__mutmut_mutants : ClassVar[MutantDict] = {
'x_print_dim__mutmut_1': x_print_dim__mutmut_1, 
    'x_print_dim__mutmut_2': x_print_dim__mutmut_2
}

def print_dim(*args, **kwargs):
    result = _mutmut_trampoline(x_print_dim__mutmut_orig, x_print_dim__mutmut_mutants, args, kwargs)
    return result 

print_dim.__signature__ = _mutmut_signature(x_print_dim__mutmut_orig)
x_print_dim__mutmut_orig.__name__ = 'x_print_dim'


def x_get_tool_emoji__mutmut_orig(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "terraform": Emoji.TERRAFORM,
        "tofu": Emoji.OPENTOFU,
        "opentofu": Emoji.OPENTOFU,
        "go": Emoji.GO,
        "python": Emoji.PYTHON,
        "uv": Emoji.UV,
    }
    return tool_emojis.get(tool_name.lower(), Emoji.WORKBENCH)


def x_get_tool_emoji__mutmut_1(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = None
    return tool_emojis.get(tool_name.lower(), Emoji.WORKBENCH)


def x_get_tool_emoji__mutmut_2(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "XXterraformXX": Emoji.TERRAFORM,
        "tofu": Emoji.OPENTOFU,
        "opentofu": Emoji.OPENTOFU,
        "go": Emoji.GO,
        "python": Emoji.PYTHON,
        "uv": Emoji.UV,
    }
    return tool_emojis.get(tool_name.lower(), Emoji.WORKBENCH)


def x_get_tool_emoji__mutmut_3(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "TERRAFORM": Emoji.TERRAFORM,
        "tofu": Emoji.OPENTOFU,
        "opentofu": Emoji.OPENTOFU,
        "go": Emoji.GO,
        "python": Emoji.PYTHON,
        "uv": Emoji.UV,
    }
    return tool_emojis.get(tool_name.lower(), Emoji.WORKBENCH)


def x_get_tool_emoji__mutmut_4(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "terraform": Emoji.TERRAFORM,
        "XXtofuXX": Emoji.OPENTOFU,
        "opentofu": Emoji.OPENTOFU,
        "go": Emoji.GO,
        "python": Emoji.PYTHON,
        "uv": Emoji.UV,
    }
    return tool_emojis.get(tool_name.lower(), Emoji.WORKBENCH)


def x_get_tool_emoji__mutmut_5(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "terraform": Emoji.TERRAFORM,
        "TOFU": Emoji.OPENTOFU,
        "opentofu": Emoji.OPENTOFU,
        "go": Emoji.GO,
        "python": Emoji.PYTHON,
        "uv": Emoji.UV,
    }
    return tool_emojis.get(tool_name.lower(), Emoji.WORKBENCH)


def x_get_tool_emoji__mutmut_6(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "terraform": Emoji.TERRAFORM,
        "tofu": Emoji.OPENTOFU,
        "XXopentofuXX": Emoji.OPENTOFU,
        "go": Emoji.GO,
        "python": Emoji.PYTHON,
        "uv": Emoji.UV,
    }
    return tool_emojis.get(tool_name.lower(), Emoji.WORKBENCH)


def x_get_tool_emoji__mutmut_7(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "terraform": Emoji.TERRAFORM,
        "tofu": Emoji.OPENTOFU,
        "OPENTOFU": Emoji.OPENTOFU,
        "go": Emoji.GO,
        "python": Emoji.PYTHON,
        "uv": Emoji.UV,
    }
    return tool_emojis.get(tool_name.lower(), Emoji.WORKBENCH)


def x_get_tool_emoji__mutmut_8(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "terraform": Emoji.TERRAFORM,
        "tofu": Emoji.OPENTOFU,
        "opentofu": Emoji.OPENTOFU,
        "XXgoXX": Emoji.GO,
        "python": Emoji.PYTHON,
        "uv": Emoji.UV,
    }
    return tool_emojis.get(tool_name.lower(), Emoji.WORKBENCH)


def x_get_tool_emoji__mutmut_9(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "terraform": Emoji.TERRAFORM,
        "tofu": Emoji.OPENTOFU,
        "opentofu": Emoji.OPENTOFU,
        "GO": Emoji.GO,
        "python": Emoji.PYTHON,
        "uv": Emoji.UV,
    }
    return tool_emojis.get(tool_name.lower(), Emoji.WORKBENCH)


def x_get_tool_emoji__mutmut_10(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "terraform": Emoji.TERRAFORM,
        "tofu": Emoji.OPENTOFU,
        "opentofu": Emoji.OPENTOFU,
        "go": Emoji.GO,
        "XXpythonXX": Emoji.PYTHON,
        "uv": Emoji.UV,
    }
    return tool_emojis.get(tool_name.lower(), Emoji.WORKBENCH)


def x_get_tool_emoji__mutmut_11(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "terraform": Emoji.TERRAFORM,
        "tofu": Emoji.OPENTOFU,
        "opentofu": Emoji.OPENTOFU,
        "go": Emoji.GO,
        "PYTHON": Emoji.PYTHON,
        "uv": Emoji.UV,
    }
    return tool_emojis.get(tool_name.lower(), Emoji.WORKBENCH)


def x_get_tool_emoji__mutmut_12(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "terraform": Emoji.TERRAFORM,
        "tofu": Emoji.OPENTOFU,
        "opentofu": Emoji.OPENTOFU,
        "go": Emoji.GO,
        "python": Emoji.PYTHON,
        "XXuvXX": Emoji.UV,
    }
    return tool_emojis.get(tool_name.lower(), Emoji.WORKBENCH)


def x_get_tool_emoji__mutmut_13(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "terraform": Emoji.TERRAFORM,
        "tofu": Emoji.OPENTOFU,
        "opentofu": Emoji.OPENTOFU,
        "go": Emoji.GO,
        "python": Emoji.PYTHON,
        "UV": Emoji.UV,
    }
    return tool_emojis.get(tool_name.lower(), Emoji.WORKBENCH)


def x_get_tool_emoji__mutmut_14(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "terraform": Emoji.TERRAFORM,
        "tofu": Emoji.OPENTOFU,
        "opentofu": Emoji.OPENTOFU,
        "go": Emoji.GO,
        "python": Emoji.PYTHON,
        "uv": Emoji.UV,
    }
    return tool_emojis.get(None, Emoji.WORKBENCH)


def x_get_tool_emoji__mutmut_15(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "terraform": Emoji.TERRAFORM,
        "tofu": Emoji.OPENTOFU,
        "opentofu": Emoji.OPENTOFU,
        "go": Emoji.GO,
        "python": Emoji.PYTHON,
        "uv": Emoji.UV,
    }
    return tool_emojis.get(tool_name.lower(), None)


def x_get_tool_emoji__mutmut_16(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "terraform": Emoji.TERRAFORM,
        "tofu": Emoji.OPENTOFU,
        "opentofu": Emoji.OPENTOFU,
        "go": Emoji.GO,
        "python": Emoji.PYTHON,
        "uv": Emoji.UV,
    }
    return tool_emojis.get(Emoji.WORKBENCH)


def x_get_tool_emoji__mutmut_17(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "terraform": Emoji.TERRAFORM,
        "tofu": Emoji.OPENTOFU,
        "opentofu": Emoji.OPENTOFU,
        "go": Emoji.GO,
        "python": Emoji.PYTHON,
        "uv": Emoji.UV,
    }
    return tool_emojis.get(tool_name.lower(), )


def x_get_tool_emoji__mutmut_18(tool_name: str) -> str:
    """Get emoji for a specific tool."""
    tool_emojis = {
        "terraform": Emoji.TERRAFORM,
        "tofu": Emoji.OPENTOFU,
        "opentofu": Emoji.OPENTOFU,
        "go": Emoji.GO,
        "python": Emoji.PYTHON,
        "uv": Emoji.UV,
    }
    return tool_emojis.get(tool_name.upper(), Emoji.WORKBENCH)

x_get_tool_emoji__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_tool_emoji__mutmut_1': x_get_tool_emoji__mutmut_1, 
    'x_get_tool_emoji__mutmut_2': x_get_tool_emoji__mutmut_2, 
    'x_get_tool_emoji__mutmut_3': x_get_tool_emoji__mutmut_3, 
    'x_get_tool_emoji__mutmut_4': x_get_tool_emoji__mutmut_4, 
    'x_get_tool_emoji__mutmut_5': x_get_tool_emoji__mutmut_5, 
    'x_get_tool_emoji__mutmut_6': x_get_tool_emoji__mutmut_6, 
    'x_get_tool_emoji__mutmut_7': x_get_tool_emoji__mutmut_7, 
    'x_get_tool_emoji__mutmut_8': x_get_tool_emoji__mutmut_8, 
    'x_get_tool_emoji__mutmut_9': x_get_tool_emoji__mutmut_9, 
    'x_get_tool_emoji__mutmut_10': x_get_tool_emoji__mutmut_10, 
    'x_get_tool_emoji__mutmut_11': x_get_tool_emoji__mutmut_11, 
    'x_get_tool_emoji__mutmut_12': x_get_tool_emoji__mutmut_12, 
    'x_get_tool_emoji__mutmut_13': x_get_tool_emoji__mutmut_13, 
    'x_get_tool_emoji__mutmut_14': x_get_tool_emoji__mutmut_14, 
    'x_get_tool_emoji__mutmut_15': x_get_tool_emoji__mutmut_15, 
    'x_get_tool_emoji__mutmut_16': x_get_tool_emoji__mutmut_16, 
    'x_get_tool_emoji__mutmut_17': x_get_tool_emoji__mutmut_17, 
    'x_get_tool_emoji__mutmut_18': x_get_tool_emoji__mutmut_18
}

def get_tool_emoji(*args, **kwargs):
    result = _mutmut_trampoline(x_get_tool_emoji__mutmut_orig, x_get_tool_emoji__mutmut_mutants, args, kwargs)
    return result 

get_tool_emoji.__signature__ = _mutmut_signature(x_get_tool_emoji__mutmut_orig)
x_get_tool_emoji__mutmut_orig.__name__ = 'x_get_tool_emoji'


# 🧰🌍🔚
