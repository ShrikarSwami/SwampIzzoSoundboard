# Swamp Izzo Soundboard 🩸

ALIVV ALIVV 🗣️ desktop soundboard yuh yuh

nine buttons 🔥 nine sounds 🔥 hotkeys work work work 😈

macOS Windows both both both 💫 click or press 1-9 WHAT WHAT 🧛‍♂️

## Features 🔥

- **Global Hotkeys**: Number keys 1-9 and numpad work work work 🗣️ even when other apps focused SLATT
- **Type B Cycling**: Each key cycles cycles CYCLES through audio clips 💫
- **Glass-Styled UI**: Modern always-on-top window PNG assets 🖤
- **Low-Latency Audio**: Caching baby caching 🩸 instant playback WHAT
- **Background Operation**: Keep running running running while u do other stuff 😈
- **System Tray**: Minimize to tray yuh yuh 🧛‍♂️
- **Easy Installation**: Installer for Windows DMG for macOS WHAT 🔥

## Installation 🗣️

### macOS

1. Go GitHub Releases go go 🔥
2. Download SwampIzzo.dmg WHAT WHAT
3. Drag app to Applications folder yuh 💫
4. Open Applications double-click Swamp Izzo 🧛‍♂️
5. SECURITY PROMPT click Open okay okay OKAY 😈
6. Accessibility Permission grant grant GRANT 🩸

#### macOS Accessibility Setup (If not prompted)

1. System Preferences Security & Privacy Accessibility 🔥
2. Click lock unlock yuh 🗣️
3. Click "+" select Swamp Izzo 💫
4. Restart app ALIVV ALIVV 🖤

### Windows

1. GitHub Releases download download 🔥
2. Get SwampIzzoSoundboard_Setup.exe installer WHAT
3. Right-click installer "Run as administrator" OKAY 🗣️
4. Follow prompts follow follow FOLLOW 😈
5. Installed to Program Files yuh 🩸
6. Start Menu or run executable LETS GO 🔥

## Usage 🔥

### Starting the App

- **macOS**: Applications double-click Swamp Izzo 🗣️
- **Windows**: Start Menu shortcut or run executable LETS GO 😈

### Triggering Sounds 🩸

1. **Hotkeys**: Press 1-9 or numpad WHAT WHAT WHAT
   - Works even when other apps focused yuh 💫
   - Each key cycle cycle CYCLES through audio clips 🔥

2. **Mouse Clicks**: Click buttons in soundboard window ALIVV 🧛‍♂️

### Configuration 🖤

Edit config.json in app directory customize customize CUSTOMIZE 🗣️

- Audio file paths for each key 🔥
- Button labels yuh 💫
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

1. Place WAV files in assets/audio/ 🗣️
2. Edit config.json reference your files 💫
3. Restart app WHAT WHAT 😈
4. Press keys ALIVV ALIVV 🩸

## Development 🔥

### Requirements WHAT

- Python 3.10 or higher yuh yuh
- Virtual environment (recommended SLATT)

### Setup Steps 🗣️

1. Clone the repository clone clone:
```bash
git clone https://github.com/ShrikarSwami/SwampIzzoSoundboard.git
cd SwampIzzoSoundboard
```

2. Create and activate virtual environment activate activate:
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies install install:
```bash
pip install -r requirements.txt
```

4. Run the app run run:
```bash
python -m src.app
```

### Project Structure 💫

```
SwampIzzoSoundboard/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── app.py               # Main app entry point and lifecycle
│   ├── ui.py                # UI window and widgets
│   ├── audio.py             # Audio playback with caching
│   ├── config.py            # Configuration loading and validation
│   └── hotkeys.py           # Global hotkey listener
├── assets/
│   ├── ui/                  # UI images (backgrounds, buttons, icons)
│   │   └── icons/          # Application icons
│   └── audio/               # Audio files
├── scripts/
│   ├── create_assets.py     # Generate PNG assets
│   ├── generate_audio.py    # Generate test audio files
│   ├── generate_png_assets.py # Generate PNG UI assets
│   ├── build_mac.sh         # macOS build script
│   └── build_win.ps1        # Windows build script
├── config.json              # Application configuration
├── swampizz_mac.spec        # PyInstaller spec for macOS
├── swampizz_windows.spec    # PyInstaller spec for Windows
├── installer_windows.iss    # Inno Setup installer script
└── requirements.txt         # Python dependencies
```

### Building Distributables 🖤

#### macOS

```bash
chmod +x build_mac.sh
./build_mac.sh
```

Output: `dist/Swamp Izzo.app` and optional DMG yuh

#### Windows

```powershell
.\build_win.ps1
```

Output: `dist/swamp_izzo/` directory WHAT

Create installer (needs Inno Setup):
```powershell
iscc installer_windows.iss
```

Output: `dist/SwampIzzoSoundboard_Setup.exe` 🔥

## Troubleshooting 😈

### Global hotkeys not working on macOS WHAT

Swamp Izzo needs accessibility permissions to listen for global hotkeys yuh yuh.

1. Open System Preferences/Settings open open
2. Go to Security & Privacy > Accessibility go go
3. Add the Swamp Izzo app to the list add add
4. Restart the application restart restart

### Audio not playing 🩸

1. Check that audio files exist at the paths specified in `config.json` check check
2. Verify the audio files are valid WAV format verify verify
3. Check system volume is not muted check check
4. Review `soundboard.log` for error messages review review

### App crashes on startup 💫

1. Check `soundboard.log` for error details check check
2. Ensure all asset files exist in the correct locations ensure ensure
3. Verify Python 3.10+ is installed verify verify
4. Try reinstalling dependencies: `pip install -r requirements.txt --force-reinstall` try try

## Audio Playback 🔥

The app supports multiple audio backends for maximum compatibility SLATT:

1. **QMediaPlayer** (PySide6 built-in, preferred yuh)
2. **sounddevice** (fallback option WHAT)

App automatically selects the best available backend at runtime 🗣️

### Supported Audio Format

- **WAV files** (PCM, any sample rate and bit depth) 💫

## Performance 🖤

- **Audio Caching**: All audio files cached in memory on first play for instant playback caching caching 🩸
- **Non-Blocking Playback**: Audio plays in background threads without UI lag non-blocking non-blocking 🔥
- **Responsive UI**: Global hotkeys and mouse clicks respond instantly responsive responsive 😈
- **Low Latency**: Optimized for sub-100ms trigger-to-sound latency low latency WHAT 💫

## License 🗣️

This project is provided as-is for personal use yuh yuh.

## Contributing 🔥

Contributions are welcome welcome! Please feel free to submit pull requests or open issues for bugs and feature requests SLATT 💫

## Technical Details 🖤

### Global Hotkey Implementation

Uses the `pynput` library for cross-platform global hotkey support WHAT:
- Listens for key press events system-wide listen listen 🗣️
- Maps numpad and number keys 1-9 to callbacks map map 🔥
- Runs in background thread to avoid blocking UI runs runs 💫

### Audio Implementation

Custom audio playback system supporting multiple backends yuh:
- **Caching**: Loads audio files once and keeps them in memory caching caching 🩸
- **Non-blocking**: Uses background threads for playback non-blocking non-blocking 😈
- **Multiple Backends**: Automatically selects available audio library auto select WHAT 🔥
- **Cross-Platform**: Works on macOS, Windows, and Linux cross-platform cross-platform 💫

### UI Architecture

Built with PySide6 (Qt for Python) SLATT:
- Frameless, always-on-top window frameless frameless 🗣️
- PNG-based glass-styled UI glass glass 🖤
- System tray integration tray integration 🔥
- Responsive button states responsive responsive 💫

### Distribution

PyInstaller packages the app into WHAT:
- **macOS**: .app bundle (optional: + DMG for distribution) yuh yuh 🩸
- **Windows**: Standalone directory + Inno Setup installer standalone standalone 😈

## System Requirements 🔥

### macOS
- macOS 10.13 or later yuh
- Accessibility permissions (for global hotkeys) WHAT
- Audio output device 💫

### Windows
- Windows 10 or later yuh
- Administrator privileges (for installer, optional) SLATT
- Audio output device 🔥

## Known Limitations 🖤

1. **macOS**: Requires accessibility permissions for global hotkeys yuh yuh 🗣️
2. **Audio Format**: Only WAV files are supported (easily expandable) WHAT 💫
3. **UI**: Fixed 420x420 window size (configurable in code) fixed fixed 🔥
4. **Keys**: Limited to number keys 1-9 (extendable via code) limited limited 😈

## Future Enhancements 💫

- [ ] Support for MP3 and OGG audio formats WHAT 🔥
- [ ] Customizable hotkeys (not just number keys) customizable customizable 🗣️
- [ ] Volume control per key volume volume 🩸
- [ ] Custom UI themes custom themes 🖤
- [ ] Recording audio directly in the app recording recording 😈
- [ ] Sound stacking (play multiple sounds simultaneously) stacking stacking 💫
- [ ] Linux support SLATT 🔥
