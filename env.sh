#!/bin/bash
#
# env.sh - wrkenv Development Environment Setup
#
# This script sets up a clean, isolated development environment for wrkenv
# using 'uv' for high-performance virtual environment and dependency management.
#
# Usage: source ./env.sh
#

# --- Configuration ---
COLOR_BLUE='\033[0;34m'
COLOR_GREEN='\033[0;32m'
COLOR_YELLOW='\033[0;33m'
COLOR_RED='\033[0;31m'
COLOR_NC='\033[0m'

# Spinner animation for long operations
spinner() {
    local pid=$1
    local delay=0.1
    local spinstr='⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'
    while ps -p $pid > /dev/null 2>&1; do
        local temp=${spinstr#?}
        printf " [%c]  " "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
}

print_header() {
    echo -e "\n${COLOR_BLUE}--- ${1} ---${COLOR_NC}"
}

print_success() {
    echo -e "${COLOR_GREEN}✅ ${1}${COLOR_NC}"
}

print_error() {
    echo -e "${COLOR_RED}❌ ${1}${COLOR_NC}"
}

print_warning() {
    echo -e "${COLOR_YELLOW}⚠️  ${1}${COLOR_NC}"
}

# --- Cleanup Previous Environment ---
print_header "🧹 Cleaning Previous Environment"

# Remove any existing Python aliases
unalias python 2>/dev/null
unalias python3 2>/dev/null
unalias pip 2>/dev/null
unalias pip3 2>/dev/null

# Clear existing PYTHONPATH
unset PYTHONPATH

# Store original PATH for restoration if needed
ORIGINAL_PATH="${PATH}"

print_success "Cleared Python aliases and PYTHONPATH"

# --- Project Validation ---
if [ ! -f "pyproject.toml" ]; then
    print_error "No 'pyproject.toml' found in current directory"
    echo "Please run this script from the wrkenv root directory"
    return 1 2>/dev/null || exit 1
fi

PROJECT_NAME=$(basename "$(pwd)")
if [ "$PROJECT_NAME" != "wrkenv" ]; then
    print_warning "This script is optimized for wrkenv but running in '${PROJECT_NAME}'"
fi

# --- UV Installation ---
print_header "🚀 Checking UV Package Manager"

if ! command -v uv &> /dev/null; then
    echo "Installing UV..."
    curl -LsSf https://astral.sh/uv/install.sh | sh > /tmp/uv_install.log 2>&1 &
    spinner $!
    
    UV_ENV_PATH_LOCAL="$HOME/.local/bin/env"
    UV_ENV_PATH_CARGO="$HOME/.cargo/env"
    
    if [ -f "$UV_ENV_PATH_LOCAL" ]; then
        source "$UV_ENV_PATH_LOCAL"
    elif [ -f "$UV_ENV_PATH_CARGO" ]; then
        source "$UV_ENV_PATH_CARGO"
    fi
    
    if command -v uv &> /dev/null; then
        print_success "UV installed successfully"
    else
        print_error "UV installation failed. Check /tmp/uv_install.log"
        return 1 2>/dev/null || exit 1
    fi
else
    print_success "UV already installed"
fi

# --- Platform Detection ---
WRKENV_OS=$(uname -s | tr '[:upper:]' '[:lower:]')
WRKENV_ARCH=$(uname -m)
case "$WRKENV_ARCH" in
    x86_64) WRKENV_ARCH="amd64" ;;
    aarch64|arm64) WRKENV_ARCH="arm64" ;;
esac

# Workenv directory setup (compatible with wrkenv naming)
PROFILE="${WRKENV_PROFILE:-default}"
if [ "$PROFILE" = "default" ]; then
    VENV_DIR="workenv/wrkenv_${WRKENV_OS}_${WRKENV_ARCH}"
else
    VENV_DIR="workenv/${PROFILE}_wrkenv_${WRKENV_OS}_${WRKENV_ARCH}"
fi

export UV_PROJECT_ENVIRONMENT="${VENV_DIR}"

# --- Virtual Environment ---
print_header "🐍 Setting Up Virtual Environment"
echo "Directory: ${VENV_DIR}"

if [ -d "${VENV_DIR}" ] && [ -f "${VENV_DIR}/bin/activate" ] && [ -f "${VENV_DIR}/bin/python" ]; then
    print_success "Virtual environment exists"
else
    echo -n "Creating virtual environment..."
    uv venv "${VENV_DIR}" > /tmp/uv_venv.log 2>&1 &
    spinner $!
    print_success "Virtual environment created"
fi

# Activate virtual environment
source "${VENV_DIR}/bin/activate"
export VIRTUAL_ENV="$(pwd)/${VENV_DIR}"

# --- Dependency Installation ---
print_header "📦 Installing Dependencies"

# Create log directory
mkdir -p /tmp/wrkenv_setup

echo -n "Syncing dependencies..."
uv sync --all-groups > /tmp/wrkenv_setup/sync.log 2>&1 &
SYNC_PID=$!
spinner $SYNC_PID
wait $SYNC_PID
if [ $? -eq 0 ]; then
    print_success "Dependencies synced"
else
    print_error "Dependency sync failed. Check /tmp/wrkenv_setup/sync.log"
    return 1 2>/dev/null || exit 1
fi

echo -n "Installing wrkenv in editable mode..."
uv pip install --no-deps -e . > /tmp/wrkenv_setup/install.log 2>&1 &
spinner $!
print_success "wrkenv installed"

# --- Sibling Packages ---
print_header "🤝 Checking for Sibling Packages"

PARENT_DIR=$(dirname "$(pwd)")
SIBLING_COUNT=0

# Check for pyvider packages that wrkenv might need
for dir in "${PARENT_DIR}"/pyvider*; do
    if [ -d "${dir}" ] && [ -f "${dir}/pyproject.toml" ]; then
        SIBLING_NAME=$(basename "${dir}")
        echo -n "Installing ${SIBLING_NAME}..."
        uv pip install --no-deps -e "${dir}" > /tmp/wrkenv_setup/${SIBLING_NAME}.log 2>&1 &
        spinner $!
        print_success "${SIBLING_NAME} installed"
        ((SIBLING_COUNT++))
    fi
done

if [ $SIBLING_COUNT -eq 0 ]; then
    print_warning "No sibling packages found (this is OK for standalone development)"
fi

# --- Environment Configuration ---
print_header "🔧 Configuring Environment"

# Set clean PYTHONPATH
export PYTHONPATH="${PWD}/src:${PWD}"
echo "PYTHONPATH: ${PYTHONPATH}"

# Clean up PATH - remove duplicates
NEW_PATH="${VENV_DIR}/bin"
OLD_IFS="$IFS"
IFS=':'
for p in $PATH; do
    case ":$NEW_PATH:" in
        *":$p:"*) ;;
        *) NEW_PATH="$NEW_PATH:$p" ;;
    esac
done
IFS="$OLD_IFS"
export PATH="$NEW_PATH"

# --- Tool Verification ---
print_header "🔍 Verifying Installation"

echo -e "\n${COLOR_GREEN}Tool Locations & Versions:${COLOR_NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# UV
if command -v uv &> /dev/null; then
    UV_PATH=$(command -v uv 2>/dev/null || which uv 2>/dev/null || echo "uv")
    printf "%-12s: %s\n" "UV" "$UV_PATH"
    printf "%-12s  %s\n" "" "$(uv --version 2>/dev/null || echo "not found")"
fi

# Python
PYTHON_PATH="${VENV_DIR}/bin/python"
if [ -f "$PYTHON_PATH" ]; then
    printf "%-12s: %s\n" "Python" "$PYTHON_PATH"
    printf "%-12s  %s\n" "" "$($PYTHON_PATH --version 2>&1)"
fi

# Python3
PYTHON3_PATH="${VENV_DIR}/bin/python3"
if [ -f "$PYTHON3_PATH" ]; then
    printf "%-12s: %s\n" "Python3" "$PYTHON3_PATH"
    printf "%-12s  %s\n" "" "$($PYTHON3_PATH --version 2>&1)"
fi

# Pytest
PYTEST_PATH="${VENV_DIR}/bin/pytest"
if [ -f "$PYTEST_PATH" ]; then
    printf "%-12s: %s\n" "Pytest" "$PYTEST_PATH"
    PYTEST_VERSION=$($PYTEST_PATH --version 2>&1 | head -n1)
    printf "%-12s  %s\n" "" "$PYTEST_VERSION"
fi

# wrkenv
WRKENV_PATH="${VENV_DIR}/bin/wrkenv"
if [ -f "$WRKENV_PATH" ]; then
    printf "%-12s: %s\n" "wrkenv" "$WRKENV_PATH"
    WRKENV_VERSION=$($WRKENV_PATH --version 2>&1 | grep -E "version|wrkenv" | head -n1 || echo "development")
    printf "%-12s  %s\n" "" "$WRKENV_VERSION"
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# --- Final Summary ---
print_header "✅ Environment Ready!"

echo -e "\n${COLOR_GREEN}🧰🌍 wrkenv development environment activated${COLOR_NC}"
echo "Virtual environment: ${VENV_DIR}"
echo "Profile: ${PROFILE}"
echo -e "\nUseful commands:"
echo "  wrkenv --help     # wrkenv CLI"
echo "  wrkenv status     # Show tool status"
echo "  wrkenv install    # Install a tool"
echo "  pytest            # Run tests"
echo "  deactivate        # Exit environment"

# --- Cleanup ---
# Remove temporary log files older than 1 day
find /tmp/wrkenv_setup -name "*.log" -mtime +1 -delete 2>/dev/null

# Return success
return 0 2>/dev/null || exit 0

# 🧰🌍🖥️🪄