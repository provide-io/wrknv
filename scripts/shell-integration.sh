#!/bin/bash
#
# wrkenv Shell Integration Script
# ===============================
# Sets up shell aliases and environment for wrkenv development
#

# Detect shell type
CURRENT_SHELL=$(basename "$SHELL")
RC_FILE=""

case "$CURRENT_SHELL" in
    bash)
        RC_FILE="$HOME/.bashrc"
        ;;
    zsh)
        RC_FILE="$HOME/.zshrc"
        ;;
    *)
        echo "⚠️  Unsupported shell: $CURRENT_SHELL"
        echo "Please manually add the aliases to your shell configuration"
        exit 1
        ;;
esac

# Define aliases
ALIASES='
# wrkenv aliases
alias wrkenv="wrkenv"
alias we="wrkenv"  # Short alias

# Tool installation shortcuts
alias tf-install="wrkenv tf"
alias tofu-install="wrkenv tf"
alias terraform-install="wrkenv terraform"
alias go-install="wrkenv go"
alias uv-install="wrkenv uv"

# Status and sync
alias wrkenv-status="wrkenv status"
alias wrkenv-sync="wrkenv sync"

# Container shortcuts
alias wrkenv-container="wrkenv container"
alias wec="wrkenv container"  # Short alias (wrkenv container)
alias wec-start="wrkenv container start"
alias wec-enter="wrkenv container enter"
alias wec-stop="wrkenv container stop"
alias wec-status="wrkenv container status"

# Package shortcuts
alias wrkenv-build="wrkenv package build"
alias wrkenv-verify="wrkenv package verify"
alias wrkenv-publish="wrkenv package publish"

# Development helpers
alias activate-wrkenv="source $(wrkenv env-path)/bin/activate 2>/dev/null || echo \"No wrkenv virtual environment found\""
'

# Check if aliases already exist
if grep -q "# wrkenv aliases" "$RC_FILE" 2>/dev/null; then
    echo "✅ wrkenv aliases already configured in $RC_FILE"
else
    echo "📝 Adding wrkenv aliases to $RC_FILE..."
    echo "$ALIASES" >> "$RC_FILE"
    echo "✅ Aliases added successfully!"
fi

# Display next steps
echo ""
echo "🎉 Shell integration complete!"
echo ""
echo "To activate the aliases, run:"
echo "  source $RC_FILE"
echo ""
echo "Available shortcuts:"
echo "  we              - Short for wrkenv"
echo "  wec             - Short for wrkenv container"
echo "  tf-install      - Install OpenTofu"
echo "  go-install      - Install Go"
echo "  wec-start       - Start development container"
echo "  wec-enter       - Enter development container"
echo ""
echo "Run 'alias | grep wrkenv' to see all available aliases"