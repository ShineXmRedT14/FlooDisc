#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Error: run with sudo!" >&2
    exit 1
fi

cd "$(dirname "$0")" || exit 1
DIRECTORY=$(pwd)
USER=${SUDO_USER:-$(whoami)}

echo "Searching Python..."

if ! command -v python3 >/dev/null 2>&1; then
    echo "Python not found. Installing..."

    if command -v apk >/dev/null 2>&1; then
        apk update
        apk add python3 py3-pip py3-virtualenv 2>&1
    elif command -v apt >/dev/null 2>&1; then
        apt update
        apt install -y python3 python3-pip python3-venv 2>&1
    else
        echo "Unsupported package manager: available only apt, apk" >&2
        exit 1
    fi
fi

echo "Python found."
python3 --version

echo "Creating virtual environment..."
sudo -u "$USER" python3 -m venv .venv

echo "Creating linker..."
sudo -u "$USER" .venv/bin/python3 -m pip install .

echo "Creating global linker..."
GLOBAL="/usr/local/bin/floodisc"
rm -f "$GLOBAL"
ln -s "${DIRECTORY}/.venv/bin/floodisc" "$GLOBAL_BIN"

echo "Successfully created global linker."
echo "Clears build and .egg-info directories"
rm -rf build
rm -rf *.egg-info