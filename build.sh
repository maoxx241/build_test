#!/bin/bash
set -euo pipefail

# Root build directory
BUILD_DIR="$(dirname "$0")/build"

# Packages to build
PACKAGES=(
    "."
    "mindie_turbo/adapter/sglang_turbo"
    "mindie_turbo/adapter/vllm_turbo"
)

# Prepare build directory
if [ -d "$BUILD_DIR" ] && [ "$(ls -A "$BUILD_DIR" 2>/dev/null)" ]; then
    echo "Performing incremental build in $BUILD_DIR"
else
    echo "Performing full rebuild"
    rm -rf "$BUILD_DIR"
    mkdir -p "$BUILD_DIR"
fi

# Build each package and move wheels into build directory
for pkg in "${PACKAGES[@]}"; do
    echo "Building package $pkg"
    pkg_name=$(basename "$pkg")
    tmp_dir="build_temp_${pkg_name//\./_}"
    (cd "$pkg" && python setup.py build --build-base "$tmp_dir" \
        bdist_wheel -b "$tmp_dir/bdist" -d dist)
    rm -rf "$pkg/$tmp_dir" "$pkg/tmp_build" "$pkg/tmp_bdist"

    for whl in "$pkg"/dist/*.whl; do
        [ -e "$whl" ] || continue
        dest="$BUILD_DIR/$(basename "$whl")"
        if [ -f "$dest" ]; then
            if cmp -s "$whl" "$dest"; then
                echo "Artifact $(basename "$whl") is up to date"
                continue
            fi
        fi
        echo "Updating $(basename "$whl")"
        cp "$whl" "$dest"
    done
    rm -rf "$pkg"/dist "$pkg"/*.egg-info
done

