# Quick Start Guide

Get Swamp Izzo Soundboard up and running in minutes!

## For Users (Install & Run)

### macOS

1. **Download**: Visit [GitHub Releases](../../releases)
2. **Install**: Download and open `SwampIzzo.dmg`
3. **Drag**: Drag the app to your Applications folder
4. **Launch**: Open Applications and double-click Swamp Izzo
5. **Permissions**: Grant accessibility access when prompted
6. **Use**: Press number keys 1-9!

### Windows

1. **Download**: Visit [GitHub Releases](../../releases)
2. **Install**: Download `SwampIzzo_Installer.bat` and `swamp_izzo` folder
3. **Run**: Right-click installer and choose "Run as administrator"
4. **Complete**: Installation completes, app is ready to use
5. **Use**: Press number keys 1-9!

## For Developers (Build from Source)

### Quick Setup

```bash
# Clone repository
git clone https://github.com/yourusername/SwampIzzo.git
cd SwampIzzo

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python soundboard.py

# Run tests
python test_app.py
```

### Customizing Audio

1. Place your WAV files in `assets/audio/`
2. Edit `config.json` to map keys to your files
3. Example:
```json
{
  "1": {
    "label": "My Sound",
    "clips": ["assets/audio/my_sound.wav"]
  }
}
```

### Building Installers

**macOS:**
```bash
./scripts/build_mac.sh
# Output: dist/SwampIzzo.dmg
```

**Windows:**
```powershell
powershell -ExecutionPolicy Bypass -File scripts/build_win.ps1
# Output: dist/swamp_izzo/ directory
```

## Key Bindings

| Key | Action |
|-----|--------|
| 1-9 | Trigger sound (cycles through clips) |
| Numpad 1-9 | Same as above |
| Click button | Same as above |

## Features

- **3x3 Grid**: 9 buttons for 9 sounds
- **Cycling**: Each button cycles through multiple audio files
- **Global**: Hotkeys work even when other apps are focused
- **Always-On-Top**: Window stays above other windows
- **Tray**: Minimize to system tray
- **Fast**: Audio caching for instant playback

## Configuration Tips

### Type B Cycling

Each button can have multiple clips:
```json
{
  "1": {
    "label": "Laugh Track",
    "clips": [
      "assets/audio/laugh1.wav",
      "assets/audio/laugh2.wav",
      "assets/audio/laugh3.wav"
    ],
    "reset_seconds": 10
  }
}
```

Press key 1: plays laugh1
Press key 1 again: plays laugh2
Press key 1 again: plays laugh3
Press key 1 again: plays laugh1 (cycles back)
Wait 10 seconds, press key 1: resets to laugh1

### Reset Timer

The `reset_seconds` value determines how long to wait before the cycle resets.
- Shorter (e.g., 5): Resets quickly, useful for rapid clips
- Longer (e.g., 30): Stays in cycle longer, good for varied sounds

## Troubleshooting

### Global hotkeys not working (macOS)

1. System Preferences > Security & Privacy > Accessibility
2. Add the Swamp Izzo app
3. Restart the app

### Audio not playing

1. Check `config.json` has correct file paths
2. Verify audio files exist in `assets/audio/`
3. Check system volume is not muted
4. Review `soundboard.log` for errors

### App won't start

1. Ensure Python 3.11+ is installed
2. Run `python test_app.py` to diagnose issues
3. Check `soundboard.log` for error details

## Converting Audio Files

Use FFmpeg to convert MP3 or other formats to WAV:

```bash
# MP3 to WAV
ffmpeg -i input.mp3 output.wav

# MP4 to WAV (audio only)
ffmpeg -i input.mp4 -vn output.wav

# Adjust sample rate if needed
ffmpeg -i input.mp3 -ar 44100 output.wav
```

## Resources

- **README.md** - Full user documentation
- **DEVELOPMENT.md** - Developer guide
- **CONFIG_EXAMPLES.md** - Configuration examples
- **PROJECT_SUMMARY.md** - Complete project overview

## Getting Help

1. Check the relevant documentation file above
2. Review error messages in `soundboard.log`
3. Run `python test_app.py` to validate installation
4. Check GitHub Issues for similar problems

## Next Steps

1. **Customize**: Edit `config.json` with your sounds
2. **Test**: Press keys 1-9 to verify operation
3. **Share**: Build installers and distribute
4. **Release**: Tag and push to GitHub for automated builds

## Tips & Tricks

- Use short, punchy sounds (< 1 second) for quick clips
- Name buttons clearly in the label field
- Test cycling by pressing the same key multiple times
- Use different reset times for different sound types
- Check system volume before troubleshooting audio issues

---

**Questions?** Check the documentation or run `python test_app.py` for diagnostics.
