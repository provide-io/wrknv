#!/usr/bin/env python3
"""Quick migration helper to convert Click commands to @register_command."""

import re
from pathlib import Path

# Simple conversion templates for common patterns
IMPORTS_TEMPLATE = """from provide.foundation.hub import register_command
from provide.foundation.cli import echo_error, echo_info, echo_success, echo_warning
from provide.foundation import logger
"""

def convert_command_decorator(content: str) -> str:
    """Convert Click decorators to @register_command."""
    
    # Replace Click imports
    content = re.sub(
        r'import click.*?\n',
        '',
        content
    )
    content = re.sub(
        r'from click import.*?\n',
        '',
        content
    )
    
    # Add new imports at the top (after docstring)
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if '"""' in line and i > 5:  # End of module docstring
            lines.insert(i+2, IMPORTS_TEMPLATE)
            break
    content = '\n'.join(lines)
    
    # Replace click.echo with echo_info
    content = content.replace('click.echo(', 'echo_info(')
    content = content.replace('click.echo(f"Error:', 'echo_error(f"')
    content = content.replace('click.echo(f"Warning:', 'echo_warning(f"')
    content = content.replace('click.secho(', 'echo_info(')
    content = content.replace(', err=True)', ')')
    
    # Replace print_* functions
    content = content.replace('print_error(', 'echo_error(')
    content = content.replace('print_info(', 'echo_info(')
    content = content.replace('print_success(', 'echo_success(')
    content = content.replace('print_warning(', 'echo_warning(')
    
    return content

# Read and convert profile.py
profile_path = Path("src/wrknv/cli/commands/profile.py")
content = profile_path.read_text()
content = convert_command_decorator(content)
print("Converted profile.py")
print("=" * 40)
print(content[:500])