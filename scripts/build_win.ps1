# Build script for Windows
# Usage: powershell -ExecutionPolicy Bypass -File scripts/build_win.ps1

Write-Host "Building Swamp Izzo for Windows..."

# Check if Python is available
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is required but not installed."
    exit 1
}

# Create virtual environment
Write-Host "Creating virtual environment..."
python -m venv venv
& .\venv\Scripts\Activate.ps1

# Install dependencies
Write-Host "Installing dependencies..."
pip install -r requirements.txt

# Build with PyInstaller
Write-Host "Building application..."
pyinstaller swampizz_windows.spec

# Create a simple installer batch file
$installerContent = @'
@echo off
REM Swamp Izzo Installer for Windows

setlocal enabledelayedexpansion

set SOURCE_DIR=%~dp0swamp_izzo
set INSTALL_DIR=%APPDATA%\SwampIzzo

echo Creating installation directory...
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

echo Copying files...
xcopy "%SOURCE_DIR%\*" "%INSTALL_DIR%\" /Y /I /E

echo Creating Start Menu shortcut...
set SHORTCUT=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Swamp Izzo.lnk
powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%INSTALL_DIR%\swamp_izzo.lnk'); $Shortcut.TargetPath = '%INSTALL_DIR%\swamp_izzo.exe'; $Shortcut.Save()"

echo Installation complete!
echo You can now run Swamp Izzo from Start Menu or %INSTALL_DIR%\swamp_izzo.exe
pause
'@

$installerPath = "dist\SwampIzzo_Installer.bat"
$installerContent | Set-Content $installerPath

Write-Host "Build complete!"
Write-Host "Output directory: dist\swamp_izzo"
Write-Host "Installer script: $installerPath"
