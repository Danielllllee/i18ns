#!/usr/bin/env bash
# Rebuild the illustration from the source photo.
# usage: ./run.sh PHOTO.jpg [BUILD_DIR]
# needs: python3 with opencv-python-headless, numpy, pillow; node with playwright (+ chromium)
set -euo pipefail
PHOTO=$(realpath "${1:?usage: run.sh PHOTO.jpg [BUILD_DIR]}")
BUILD=${2:-build}
SRC=$(cd "$(dirname "$0")/src" && pwd)
mkdir -p "$BUILD"
cd "$BUILD"
python3 "$SRC/prepare.py" "$PHOTO"
python3 "$SRC/person.py"
python3 "$SRC/draw.py"
NODE_PATH="${NODE_PATH:-$(npm root -g)}" node "$SRC/render.js" drawing.svg drawing.png
