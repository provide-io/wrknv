#
# wrknv/workenv/operations/platform.py
#
"""
wrknv Platform Detection
===================================
Platform and architecture information using provide.foundation.
"""

from provide.foundation.platform import (
    get_os_name,
    get_arch_name,
    get_platform_string,
    get_system_info,
)


def get_platform_info() -> dict[str, str]:
    """Get platform information for tool downloads.
    
    Returns:
        Dictionary with platform details for tool compatibility.
    """
    # Get comprehensive system info from foundation
    sys_info = get_system_info()
    
    return {
        "os": sys_info.os_name,
        "arch": sys_info.arch,
        "platform": sys_info.platform,
        "python_platform": sys_info.platform,
        "machine": sys_info.arch,
        "system": sys_info.os_name,
    }


def get_architecture() -> str:
    """Get normalized architecture name for tool downloads.
    
    Returns:
        Architecture string suitable for tool downloads (amd64, arm64, etc).
    """
    return get_arch_name()


def get_workenv_platform() -> str:
    """Get platform string for workenv directory naming.
    
    Returns:
        Platform string in format: {os}_{arch}
    """
    return get_platform_string()


def is_arm_mac() -> bool:
    """Check if running on Apple Silicon Mac.
    
    Returns:
        True if running on ARM-based Mac (M1/M2/M3).
    """
    from provide.foundation.platform import is_macos, is_arm
    return is_macos() and is_arm()


def is_windows() -> bool:
    """Check if running on Windows.
    
    Returns:
        True if running on Windows.
    """
    from provide.foundation.platform import is_windows as foundation_is_windows
    return foundation_is_windows()


# Re-export for backward compatibility (remove these later)
def get_os_name() -> str:
    """Get normalized OS name for tool downloads.
    
    DEPRECATED: Use provide.foundation.platform.get_os_name directly.
    """
    from provide.foundation.platform import get_os_name as foundation_get_os_name
    return foundation_get_os_name()


# 🧰🌍🔍🪄