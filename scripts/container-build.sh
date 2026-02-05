#!/bin/bash
set -e

IMAGE_NAME="kivy/buildozer:latest"
CONTAINER_ENGINE="${CONTAINER_ENGINE:-podman}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get the project root (parent of scripts dir)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo -e "${GREEN}Using container engine: ${CONTAINER_ENGINE}${NC}"

# Create cache directories if they don't exist
mkdir -p "$HOME/.buildozer"
mkdir -p "$HOME/.android"

# Pull the image if not present
if ! $CONTAINER_ENGINE image exists "$IMAGE_NAME" 2>/dev/null; then
    echo -e "${YELLOW}Pulling buildozer image...${NC}"
    $CONTAINER_ENGINE pull "$IMAGE_NAME"
fi

# Default command
CMD="${@:-android debug}"

echo -e "${GREEN}Running: buildozer ${CMD}${NC}"

# Detect TTY for interactive flag
TTY_FLAG=""
if [ -t 0 ]; then
    TTY_FLAG="-it"
fi

# Run the container
# - Mount project directory
# - Mount buildozer cache for faster rebuilds
# - BUILDOZER_WARN_ON_ROOT=0 skips the root warning prompt
# Note: kivy/buildozer image expects the command without 'buildozer' prefix
$CONTAINER_ENGINE run --rm $TTY_FLAG \
    -e BUILDOZER_WARN_ON_ROOT=0 \
    -v "$PROJECT_DIR:/home/user/hostcwd:Z" \
    -v "$HOME/.buildozer:/home/user/.buildozer:Z" \
    -v "$HOME/.android:/home/user/.android:Z" \
    "$IMAGE_NAME" \
    $CMD
