# Building the App

## macOS

1. Install PyInstaller in your venv:
   ```bash
   pip install pyinstaller
   ```

2. Run the build script:
   ```bash
   ./build_mac.sh
   ```

3. The app bundle will be created at `dist/Swamp Izzo.app`

4. To test it:
   ```bash
   open "dist/Swamp Izzo.app"
   ```

### Creating a DMG Installer (macOS)

1. Install create-dmg:
   ```bash
   brew install create-dmg
   ```

2. Create the DMG:
   ```bash
   create-dmg \
     --volname "Swamp Izzo" \
     --window-pos 200 120 \
     --window-size 600 400 \
     --icon-size 100 \
     --app-drop-link 450 150 \
     "dist/SwampIzzo.dmg" \
     "dist/Swamp Izzo.app"
   ```

## Windows

1. Install PyInstaller in your venv:
   ```powershell
   pip install pyinstaller
   ```

2. Run the build script:
   ```powershell
   .\build_win.ps1
   ```

3. The executable will be in `dist\swamp_izzo\`

4. To test it:
   ```powershell
   .\dist\swamp_izzo\swamp_izzo.exe
   ```

### Creating a Windows Installer

1. Download and install [Inno Setup](https://jrsoftware.org/isinfo.php)

2. After building with `.\build_win.ps1`, compile the installer:
   ```powershell
   iscc installer_windows.iss
   ```

3. The installer will be created at `dist\SwampIzzoSoundboard_Setup.exe`

## Distribution

- **macOS**: Share the `.dmg` file
- **Windows**: Share the installer `.exe` or zip the `dist\swamp_izzo\` folder
