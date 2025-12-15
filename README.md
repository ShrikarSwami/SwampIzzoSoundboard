# Swamp Izzo Soundboard 🩸

ALIVV ALIVV 🗣️ desktop soundboard yo

nine buttons 🔥 nine sounds 🔥 hotkeys work work work 😈

macOS Windows both both both 💫 click or press 1-9 WHAT WHAT 🧛‍♂️

## Features 🔥

- **Global Hotkeys**: Number keys 1-9 and numpad work work work 🗣️ even other apps focused
- **Type B Cycling**: Each key cycles cycles CYCLES through audio clips 💫
- **Glass-Styled UI**: Modern always-on-top window PNG assets 🖤
- **Low-Latency Audio**: Caching baby caching 🩸 instant playback
- **Background Operation**: Keep running running running while u do other stuff 😈
- **System Tray**: Minimize to tray yo 🧛‍♂️
- **Easy Installation**: Installer Windows DMG macOS WHAT 🔥

## Installation 🗣️

### macOS

1. GitHub Releases go go 🔥
2. Download SwampIzzo.dmg WHAT WHAT
3. Drag app Applications folder yo 💫
4. Open Applications double-click Swamp Izzo 🧛‍♂️
5. SECURITY PROMPT click Open okay okay OKAY 😈
6. Accessibility Permission grant grant GRANT 🩸

#### macOS Accessibility Setup (If not prompted)

1. System Preferences Security & Privacy Accessibility 🔥
2. Click lock unlock yo 🗣️
3. Click "+" select Swamp Izzo 💫
4. Restart app ALIVV ALIVV 🖤

### Windows

1. GitHub Releases download download 🔥
2. Get SwampIzzo_Installer.bat swamp_izzo folder WHAT
3. Right-click installer "Run as administrator" OKAY 🗣️
4. Follow prompts follow follow FOLLOW 😈
5. Installed APPDATA SwampIzzo yo 🩸
6. Start Menu or run executable LETS GO 🔥

## Usage 🔥

### Starting the App

- **macOS**: Applications double-click Swamp Izzo 🗣️
- **Windows**: Start Menu shortcut or run executable LETS GO 😈

### Triggering Sounds 🩸

1. **Hotkeys**: Press 1-9 or numpad WHAT WHAT WHAT
   - Works even other apps focused yo 💫
   - Each key cycle cycle CYCLES through audio clips 🔥

2. **Mouse Clicks**: Click buttons soundboard window ALIVV 🧛‍♂️

### Configuration 🖤

Edit config.json app directory customize customize CUSTOMIZE 🗣️

- Audio file paths each key 🔥
- Button labels yo 💫
- Window size 😈
- Clip reset timers (idle time until cycle reset) 🩸

Example configuration:
```json
{
  "keys": {
    "1": {
      "label": "Sound 1",
      "clips": ["assets/audio/sound_1.wav", "assets/audio/alternate_1.wav"],
      "reset_seconds": 10
    }
  }
}
```

### Custom Audio Files 🔥

1. Place WAV files assets/audio/ 🗣️
2. Edit config.json reference your files 💫
3. Restart app WHAT WHAT 😈
4. Press keys ALIVV ALIVV 🩸

## Development

### Requirements

- Python 3.11 or higher
- Virtual environment (recommended)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/SwampIzzo.git
cd SwampIzzo
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python -m src.app
```

### Project Structure

```
SwampIzzo/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── app.py               # Main app entry point and lifecycle
│   ├── ui.py                # UI window and widgets
│   ├── audio.py             # Audio playback with caching
│   ├── config.py            # Configuration loading and validation
│   └── hotkeys.py           # Global hotkey listener
├── assets/
│   ├── ui/                  # UI images (glass_panel.png, buttons)
│   └── audio/               # Audio files
├── scripts/
│   ├── create_assets.py     # Generate PNG assets
│   ├── generate_audio.py    # Generate test audio files
│   ├── build_mac.sh         # macOS build script
│   └── build_win.ps1        # Windows build script
├── .github/
│   └── workflows/
│       ├── build-macos.yml  # GitHub Actions for macOS builds
│       └── build-windows.yml # GitHub Actions for Windows builds
├── config.json              # Application configuration
├── swampizz_mac.spec        # PyInstaller spec for macOS
├── swampizz_windows.spec    # PyInstaller spec for Windows
└── requirements.txt         # Python dependencies
```

### Building Distributables

#### macOS

```bash
chmod +x scripts/build_mac.sh
./scripts/build_mac.sh
```

Output: `dist/SwampIzzo.dmg` and `dist/Swamp Izzo.app`

#### Windows

```powershell
powershell -ExecutionPolicy Bypass -File scripts/build_win.ps1
```

Output: `dist/swamp_izzo/` directory and installer batch file

## Troubleshooting

### Global hotkeys not working on macOS

Swamp Izzo requires accessibility permissions to listen for global hotkeys.

1. Open System Preferences/Settings
2. Go to Security & Privacy > Accessibility
3. Add the Swamp Izzo app to the list
4. Restart the application

### Audio not playing

1. Check that audio files exist at the paths specified in `config.json`
2. Verify the audio files are valid WAV format
3. Check system volume is not muted
4. Review `soundboard.log` for error messages

### App crashes on startup

1. Check `soundboard.log` for error details
2. Ensure all asset files exist in the correct locations
3. Verify Python 3.11+ is installed
4. Try reinstalling dependencies: `pip install -r requirements.txt --force-reinstall`

## Audio Playback

The app supports multiple audio backends for maximum compatibility:

1. **simpleaudio** (preferred on Windows and Linux)
2. **sounddevice** (preferred on macOS)

The app automatically selects the best available backend at runtime.

### Supported Audio Format

- **WAV files** (PCM, any sample rate and bit depth)

## Performance

- **Audio Caching**: All audio files are cached in memory on first play for instant playback
- **Non-Blocking Playback**: Audio plays in background threads without UI lag
- **Responsive UI**: Global hotkeys and mouse clicks respond instantly
- **Low Latency**: Optimized for sub-100ms trigger-to-sound latency

## License

This project is provided as-is for personal use.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Technical Details

### Global Hotkey Implementation

Uses the `pynput` library for cross-platform global hotkey support:
- Listens for key press events system-wide
- Maps numpad and number keys 1-9 to callbacks
- Runs in background thread to avoid blocking UI

### Audio Implementation

Custom audio playback system supporting multiple backends:
- **Caching**: Loads audio files once and keeps them in memory
- **Non-blocking**: Uses background threads for playback
- **Multiple Backends**: Automatically selects available audio library
- **Cross-Platform**: Works on macOS, Windows, and Linux

### UI Architecture

Built with PySide6 (Qt for Python):
- Frameless, always-on-top window
- PNG-based glass-styled UI
- System tray integration
- Responsive button states

### Distribution

PyInstaller packages the app into:
- **macOS**: .app bundle + DMG (for distribution)
- **Windows**: Standalone directory + optional installer batch file

GitHub Actions automatically builds and releases on tag push.

## System Requirements

### macOS
- macOS 10.13 or later
- Accessibility permissions (for global hotkeys)
- Audio output device

### Windows
- Windows 7 or later
- Administrator privileges (for installer, optional)
- Audio output device

## Known Limitations

1. **macOS**: Requires accessibility permissions for global hotkeys
2. **Audio Format**: Only WAV files are supported (easily expandable)
3. **UI**: Fixed 420x420 window size (configurable in code)
4. **Keys**: Limited to number keys 1-9 (extendable via code)

## Future Enhancements

- [ ] Support for MP3 and OGG audio formats
- [ ] Customizable hotkeys (not just number keys)
- [ ] Volume control per key
- [ ] Custom UI themes
- [ ] Recording audio directly in the app
- [ ] Sound stacking (play multiple sounds simultaneously)
- [ ] Linux support
