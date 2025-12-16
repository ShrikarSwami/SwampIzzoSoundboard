#!/bin/bash
# Build script for macOS

set -e

echo "Building Swamp Izzo for macOS..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed."
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Build with PyInstaller
echo "Building application..."
pyinstaller swampizz_mac.spec

# Create DMG
echo "Creating DMG..."
mkdir -p dist/dmg
cp -r dist/Swamp\ Izzo.app dist/dmg/
hdiutil create -volname "Swamp Izzo" -srcfolder dist/dmg -ov -format UDZO dist/SwampIzzo.dmg

echo "Build complete!"
echo "Output: dist/SwampIzzo.dmg"
echo "App bundle: dist/Swamp Izzo.app"
