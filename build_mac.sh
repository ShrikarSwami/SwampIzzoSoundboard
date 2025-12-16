#!/bin/bash
# Build script for macOS app bundle

set -e

echo "🔨 Building Swamp Izzo Soundboard for macOS..."

# Ensure we're in the project root
cd "$(dirname "$0")"

# Activate venv if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Install PyInstaller if not present
if ! python -c "import PyInstaller" 2>/dev/null; then
    echo "📦 Installing PyInstaller..."
    pip install pyinstaller
fi

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build dist

# Build the app
echo "⚙️  Building app bundle..."
pyinstaller swampizz_mac.spec

# Check if build succeeded
if [ -f "dist/Swamp Izzo.app/Contents/MacOS/swamp_izzo" ]; then
    echo "✅ Build successful!"
    echo "📂 App bundle created at: dist/Swamp Izzo.app"
    echo ""
    echo "To test the app, run:"
    echo "  open 'dist/Swamp Izzo.app'"
    echo ""
    echo "To create a DMG installer, install create-dmg:"
    echo "  brew install create-dmg"
    echo "  create-dmg --volname 'Swamp Izzo' --window-pos 200 120 --window-size 600 400 --icon-size 100 --app-drop-link 450 150 'dist/SwampIzzo.dmg' 'dist/Swamp Izzo.app'"
else
    echo "❌ Build failed!"
    exit 1
fi
