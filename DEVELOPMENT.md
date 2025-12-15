# Development Guide

This guide covers setting up the development environment and building the Swamp Izzo Soundboard from source.

## Prerequisites

- Python 3.11 or later
- Git
- macOS or Windows
- Audio output device

## macOS Setup

### 1. Install Python 3.11+

Using Homebrew (recommended):
```bash
brew install python@3.11
```

Or download from [python.org](https://www.python.org)

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/SwampIzzo.git
cd SwampIzzo
```

### 3. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run from Source

```bash
python soundboard.py
```

### 6. Grant Accessibility Permissions

For global hotkeys to work:
1. Go to System Preferences > Security & Privacy > Accessibility
2. Click the lock icon to unlock
3. Click "+" and add the Python executable from your venv
4. Restart the app

## Windows Setup

### 1. Install Python 3.11+

Download from [python.org](https://www.python.org) and run the installer.
Make sure to check "Add Python to PATH" during installation.

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/SwampIzzo.git
cd SwampIzzo
```

### 3. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run from Source

```bash
python soundboard.py
```

## Building Distributables

### macOS - Create DMG

```bash
./scripts/build_mac.sh
```

Output:
- `dist/SwampIzzo.dmg` - DMG installer
- `dist/Swamp Izzo.app` - Standalone app bundle

### Windows - Create Installer

```powershell
powershell -ExecutionPolicy Bypass -File scripts/build_win.ps1
```

Output:
- `dist/swamp_izzo/` - Application directory
- `dist/SwampIzzo_Installer.bat` - Simple batch installer

## Project Structure

```
SwampIzzo/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── app.py               # Main application entry point
│   ├── ui.py                # UI window and buttons
│   ├── audio.py             # Audio playback engine
│   ├── config.py            # Configuration management
│   └── hotkeys.py           # Global hotkey listener
├── assets/
│   ├── ui/                  # PNG button and panel images
│   │   ├── glass_panel.png
│   │   ├── button_default.png
│   │   ├── button_hover.png
│   │   └── button_pressed.png
│   └── audio/               # Audio files
│       ├── startup_swamp_izzo.wav
│       └── sound_1.wav through sound_9.wav
├── scripts/
│   ├── create_assets.py     # Generate PNG assets
│   ├── generate_audio.py    # Generate test audio
│   ├── generate_png_assets.py # PNG generator without PIL
│   ├── build_mac.sh         # macOS build script
│   └── build_win.ps1        # Windows build script
├── .github/
│   └── workflows/
│       ├── build-macos.yml  # GitHub Actions for macOS
│       └── build-windows.yml # GitHub Actions for Windows
├── config.json              # Application configuration
├── soundboard.py            # Entry point script
├── swampizz_mac.spec        # PyInstaller spec for macOS
├── swampizz_windows.spec    # PyInstaller spec for Windows
├── requirements.txt         # Python dependencies
└── README.md                # User documentation
```

## Configuration

Edit `config.json` to customize the soundboard:

```json
{
  "startup_audio": "assets/audio/startup_swamp_izzo.wav",
  "app": {
    "window_width": 420,
    "window_height": 420
  },
  "keys": {
    "1": {
      "label": "My Sound",
      "clips": [
        "assets/audio/sound_1.wav",
        "assets/audio/sound_1_alternate.wav"
      ],
      "reset_seconds": 10
    }
  }
}
```

### Configuration Options

- **startup_audio**: Path to audio file played on app startup
- **window_width/height**: Size of the main window in pixels
- **keys**: Dictionary mapping key numbers (1-9) to configurations
  - **label**: Display text on button
  - **clips**: Array of audio file paths for cycling
  - **reset_seconds**: Time before cycling resets (idle timer)

## Adding Custom Audio

1. Place your WAV files in `assets/audio/`
2. Update `config.json` to reference the files
3. Restart the application

### Supported Audio Format

- WAV files (any sample rate and bit depth)

## Testing

### Manual Testing

1. Start the app: `python soundboard.py`
2. Test hotkeys: Press number keys 1-9
3. Test mouse clicks: Click buttons in the window
4. Test audio cycling: Press same key multiple times
5. Test cycle reset: Wait configured seconds then press key again

### Logging

The app writes logs to `soundboard.log` in the working directory.

Check logs for troubleshooting:
```bash
tail -f soundboard.log
```

## Troubleshooting

### "No module named 'PySide6'"

Install dependencies:
```bash
pip install -r requirements.txt
```

### Global hotkeys not working (macOS)

Add Python to Accessibility permissions:
1. System Preferences > Security & Privacy > Accessibility
2. Add your Python executable
3. Restart the app

### Audio not playing

Check `soundboard.log` for errors. Common issues:
- Audio file path incorrect in config.json
- File doesn't exist or isn't readable
- System volume is muted
- Audio device is disconnected

### Window won't appear

Check that PySide6 is installed correctly:
```bash
python -c "from PySide6.QtWidgets import QApplication; print('OK')"
```

## Code Style

This project uses:
- Python 3.11+ type hints
- Docstrings for all public functions
- Clear variable and function names
- Logging for debugging

## Performance Optimization

Key optimizations implemented:

1. **Audio Caching**: Audio files loaded once and cached in memory
2. **Non-Blocking Playback**: Uses background threads for playback
3. **Responsive UI**: Global hotkeys don't block UI thread
4. **Lazy Loading**: Assets loaded on demand

## Dependencies

### Core Dependencies

- **PySide6**: Qt framework for cross-platform UI
- **pynput**: Global hotkey listener for all platforms
- **sounddevice**: Low-latency audio playback
- **soundfile**: WAV file reading

### Development Dependencies

- **PyInstaller**: Packaging and distribution

## Building for Distribution

### Step 1: Update Version

Edit `src/__init__.py`:
```python
__version__ = '1.0.1'
```

### Step 2: Test Thoroughly

```bash
python soundboard.py
```

### Step 3: Build Binaries

macOS:
```bash
./scripts/build_mac.sh
```

Windows:
```powershell
./scripts/build_win.ps1
```

### Step 4: Test Installer

Install and run the packaged version to verify it works.

### Step 5: Create GitHub Release

1. Push changes and tag:
```bash
git add .
git commit -m "Release v1.0.1"
git tag v1.0.1
git push origin main --tags
```

2. GitHub Actions will automatically build and create release artifacts

3. Manually create release notes on GitHub

## Common Development Tasks

### Adding a New Button

1. Modify `config.json` (already has 9 buttons, this would extend)
2. Update UI grid layout if changing from 3x3
3. Test hotkey and click functionality

### Changing UI Colors

1. Edit button PNG files in `assets/ui/`
2. Or regenerate with `scripts/generate_png_assets.py`
3. Modify `src/ui.py` stylesheets for other UI elements

### Adding Audio Formats

1. Modify `src/audio.py` to use soundfile for loading
2. Update requirements.txt if needed
3. Test with sample files

## Getting Help

If you run into issues:

1. Check `soundboard.log` for error messages
2. Review error output in terminal
3. Check that all dependencies are installed
4. Verify asset files exist and are readable
5. Try running with verbose output

## Contributing

When contributing changes:

1. Test on both macOS and Windows if possible
2. Follow the code style conventions
3. Update documentation if behavior changes
4. Add logging for debugging
5. Test both UI and hotkey functionality

## Release Checklist

- [ ] Update version in `src/__init__.py`
- [ ] Update CHANGELOG with new features/fixes
- [ ] Test on macOS
- [ ] Test on Windows
- [ ] Build macOS DMG
- [ ] Build Windows installer
- [ ] Test installed versions
- [ ] Create GitHub release with artifacts
- [ ] Update README if needed
- [ ] Announce release
