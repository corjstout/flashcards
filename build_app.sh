#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SCRIPT_NAME="$(basename ${BASH_SOURCE[0]})"
BUILD_DIR="$SCRIPT_DIR/app"

function clean_workspace() {
    rm -r "${BUILD_DIR}/.eggs"
    rm -r "${BUILD_DIR}/build"
    rm -r "${BUILD_DIR}/dist"
}

function generate_app() {
    cd "${BUILD_DIR}"
    python3 setup.py py2app -A
}

function main() {
    clean_workspace
    generate_app
}

if [ "$(basename -- "$0")" = "${SCRIPT_NAME}" ]; then
  main $@
fi
