#!/usr/bin/env python3
#
# wrkenv/workenv/scripts/terraform-wrapper.py
#
"""
Terraform Wrapper Script
========================
This script acts as a 'terraform' command that delegates to the
developer's chosen terraform flavor (terraform or opentofu).
"""

import os
import pathlib
import sys


def get_workenv_root():
    """Find the workenv root directory."""
    # Start from the script's location
    current = pathlib.Path(sys.argv[0]).resolve().parent

    # Look for workenv directory pattern
    while current != current.parent:
        if current.name.startswith("workenv") and "_" in current.name:
            return current
        if current.name == "bin" and current.parent.name.startswith("workenv"):
            return current.parent
        current = current.parent

    return None


def get_terraform_flavor():
    """Get the configured terraform flavor from wrkenv.toml."""
    # Check for wrkenv.toml
    wrkenv_toml = None
    current = pathlib.Path.cwd()
    while current != current.parent:
        candidate = current / "wrkenv.toml"
        if candidate.exists():
            wrkenv_toml = candidate
            break
        current = current.parent

    if wrkenv_toml:
        try:
            import tomllib

            with open(wrkenv_toml, "rb") as f:
                config = tomllib.load(f)

            # Check for terraform_flavor setting
            if "workenv" in config and "terraform_flavor" in config["workenv"]:
                return config["workenv"]["terraform_flavor"]
        except:
            pass

    return "terraform"  # Default to HashiCorp Terraform


def main():
    """Main entry point."""
    flavor = get_terraform_flavor()

    # Find the actual binary
    workenv_root = get_workenv_root()
    if workenv_root:
        bin_dir = workenv_root / "bin"

        # Look for the flavor binary
        if flavor == "opentofu":
            binary_name = "tofu"
        else:
            binary_name = "hctf"  # HashiCorp Terraform

        if os.name == "nt":
            binary_name += ".exe"

        binary_path = bin_dir / binary_name

        if binary_path.exists():
            # Execute the actual binary with all arguments
            os.execv(str(binary_path), [binary_name] + sys.argv[1:])
        else:
            print(f"Error: {flavor} binary not found at {binary_path}", file=sys.stderr)
            if flavor == "opentofu":
                print(
                    "Run 'wrkenv tf <version>' to install OpenTofu",
                    file=sys.stderr,
                )
            else:
                print(
                    "Run 'wrkenv tf <version> --terraform' to install Terraform",
                    file=sys.stderr,
                )
            sys.exit(1)
    else:
        print("Error: Could not determine workenv directory", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()


# 🍲🥄📄🪄
