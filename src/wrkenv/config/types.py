#
# wrkenv/config/types.py
#
"""
Configuration Type Definitions
==============================
Cty type definitions for wrkenv configuration.
"""


try:
    from pyvider.cty import (
        CtyBool,
        CtyDynamic,
        CtyList,
        CtyMap,
        CtyNumber,
        CtyObject,
        CtyString,
        CtyType,
    )

    HAS_CTY = True
except ImportError:
    HAS_CTY = False
    # Fallback types for when cty is not available
    CtyObject = dict
    CtyString = str
    CtyNumber = float
    CtyBool = bool
    CtyList = list
    CtyMap = dict
    CtyType = type
    CtyDynamic = object


# Tool configuration type
if HAS_CTY:
    ToolType = CtyObject(
        {
            "version": CtyString(),
            "constraints": CtyObject(
                {
                    "min": CtyString(),
                    "max": CtyString(),
                },
                optional_attributes={"min", "max"},
            ),
            "features": CtyList(CtyString()),
            "env": CtyMap(CtyString()),
        },
        optional_attributes={"constraints", "features", "env"},
    )

    # Profile type
    ProfileType = CtyObject(
        {
            "inherit": CtyList(CtyString()),
            "tools": CtyMap(ToolType),
            "env": CtyMap(CtyString()),
        },
        optional_attributes={"inherit", "tools", "env"},
    )

    # Package configuration type
    PackageConfigType = CtyObject(
        {
            "default_out_dir": CtyString(),
            "signing_curve": CtyString(),
            "verify_on_build": CtyBool(),
            "auto_sign": CtyBool(),
            "metadata": CtyMap(CtyString()),
        },
        optional_attributes={
            "default_out_dir",
            "signing_curve",
            "verify_on_build",
            "auto_sign",
            "metadata",
        },
    )

    # Matrix configuration type
    MatrixConfigType = CtyMap(
        CtyObject(
            {
                "tools": CtyMap(CtyList(CtyString())),
                "command": CtyMap(CtyString()),
            }
        )
    )

    # Complete workenv configuration type
    WorkenvConfigType = CtyObject(
        {
            "tools": CtyMap(CtyDynamic()),  # Can be string or ToolType
            "profiles": CtyMap(ProfileType),
            "package": PackageConfigType,
            "matrix": MatrixConfigType,
            "settings": CtyMap(CtyDynamic()),
        },
        optional_attributes={"tools", "profiles", "package", "matrix", "settings"},
    )

    # Provider configuration type (for package integration)
    ProviderConfigType = CtyObject(
        {
            "name": CtyString(),
            "namespace": CtyString(),
            "version": CtyString(),
            "protocols": CtyList(CtyString()),
            "features": CtyObject(
                {
                    "mux": CtyBool(),
                    "debug": CtyBool(),
                    "async": CtyBool(),
                },
                optional_attributes={"mux", "debug", "async"},
            ),
        },
        optional_attributes={"namespace", "protocols", "features"},
    )

else:
    # Fallback when cty is not available
    ToolType = dict
    ProfileType = dict
    PackageConfigType = dict
    MatrixConfigType = dict
    WorkenvConfigType = dict
    ProviderConfigType = dict


# Export specific tool types for easier access
class ToolConfigType:
    """Tool-specific configuration types."""

    terraform = ToolType
    tofu = ToolType
    go = ToolType
    uv = ToolType
    python = ToolType
    node = ToolType


def normalize_tool_config(value: any) -> dict[str, any]:
    """Normalize tool configuration value.

    Converts string values to proper tool config format.
    """
    if isinstance(value, str):
        return {"version": value}
    elif isinstance(value, dict):
        return value
    else:
        raise ValueError(f"Invalid tool config type: {type(value)}")


# 🧰🌍🖥️🪄
