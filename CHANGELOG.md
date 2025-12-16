# Changelog

All notable changes to the Swamp Izzo Soundboard project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Coming Soon
- Support for MP3 and OGG audio formats
- Customizable hotkeys (not limited to 1-9)
- Per-button volume control
- Custom UI themes
- In-app audio recording
- Sound stacking (simultaneous playback)
- Linux support
- Custom key combinations (Shift+number, Ctrl+number, etc.)

## [1.0.0] - 2025-12-15

### Added
- Core application framework with PySide6
- Global hotkey listener supporting number keys 1-9 and numpad keys
- Audio playback system with caching for zero-latency triggering
- Type B multi-clip cycling for each button (each key cycles through audio files)
- Glass-styled UI with PNG-based asset system
- 3x3 button grid interface (9 keys total)
- Configuration system with JSON-based setup
- Always-on-top window that stays focused
- System tray integration with minimize to tray
- Audio file preloading and memory caching
- Non-blocking audio playback (background threads)
- Reset timer functionality (clip cycle resets after idle time)
- Comprehensive logging to soundboard.log
- Professional error handling and validation

### Build System
- PyInstaller spec files for macOS and Windows
- Cross-platform build scripts (bash for macOS, PowerShell for Windows)
- GitHub Actions workflows for CI/CD
- Automated builds and releases on version tags
- DMG installer support for macOS
- Windows executable and batch installer

### Documentation
- Comprehensive README with installation and usage guides
- Development guide with setup instructions
- Configuration examples and advanced usage
- Project structure documentation
- Troubleshooting guide
- Contributing guidelines

### Testing
- Comprehensive test suite covering all modules
- Asset verification
- Configuration validation
- Audio module testing
- UI initialization testing
- 100% test pass rate

### Assets
- 4 PNG images for UI (glass panel, 3 button states)
- 10 WAV audio files (startup sound + 9 button sounds)
- Placeholder audio generator script

### Features
- **Global Hotkeys**: Works with number keys 1-9 and numpad
- **Type B Cycling**: Each button cycles through multiple audio files
- **Audio Caching**: All audio loaded once and cached for instant playback
- **Non-Blocking**: Audio plays in background, UI remains responsive
- **Always-on-Top**: Window stays above other applications
- **Tray Icon**: Minimize to system tray for unobtrusive operation
- **Configuration**: JSON-based customization of sounds and labels
- **Cross-Platform**: Supports both macOS and Windows
- **Logging**: Comprehensive logging for debugging

### Technical Details
- Python 3.11+ support
- PySide6 (Qt) for UI
- pynput for global hotkeys
- sounddevice for audio playback
- numpy for audio processing
- PyInstaller for packaging

### Known Limitations
- Audio format: WAV only (can be extended)
- Keys: Limited to 1-9 (extendable)
- Window size: 420x420 fixed (configurable in code)
- macOS: Requires accessibility permissions for global hotkeys

## Versioning

The project uses semantic versioning:
- MAJOR: Breaking changes or major new features
- MINOR: New features, backwards compatible
- PATCH: Bug fixes and minor improvements

## Release Process

1. Update version in `src/__init__.py`
2. Update this CHANGELOG with new version section
3. Test thoroughly on both macOS and Windows
4. Commit changes with message "Release v1.x.x"
5. Create git tag: `git tag v1.x.x`
6. Push to GitHub: `git push origin main --tags`
7. GitHub Actions will automatically build and create release
8. Add release notes on GitHub Releases page

## Future Versions

### 1.1.0 (Planned)
- [ ] MP3 and OGG format support
- [ ] Per-button volume adjustment
- [ ] Sound preview functionality
- [ ] Configuration UI (in-app settings)

### 1.2.0 (Planned)
- [ ] Customizable hotkeys
- [ ] Custom key combinations
- [ ] Sound stacking (multiple sounds at once)
- [ ] Recording functionality

### 2.0.0 (Long-term)
- [ ] Linux support
- [ ] Custom themes
- [ ] Plugin system
- [ ] Network features (remote control)
- [ ] Advanced scheduling

## Contributing

See DEVELOPMENT.md for contribution guidelines.

## License

See LICENSE file for details.
