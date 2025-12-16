# Build script for Windows executable

Write-Host "🔨 Building Swamp Izzo Soundboard for Windows..." -ForegroundColor Cyan

# Ensure we're in the project root
Set-Location $PSScriptRoot

# Activate venv if it exists
if (Test-Path "venv\Scripts\Activate.ps1") {
    & "venv\Scripts\Activate.ps1"
}

# Install PyInstaller if not present
try {
    python -c "import PyInstaller" 2>$null
} catch {
    Write-Host "📦 Installing PyInstaller..." -ForegroundColor Yellow
    pip install pyinstaller
}

# Clean previous builds
Write-Host "🧹 Cleaning previous builds..." -ForegroundColor Yellow
if (Test-Path "build") { Remove-Item -Recurse -Force "build" }
if (Test-Path "dist") { Remove-Item -Recurse -Force "dist" }

# Build the exe
Write-Host "⚙️  Building executable..." -ForegroundColor Yellow
pyinstaller swampizz_windows.spec

# Check if build succeeded
if (Test-Path "dist\swamp_izzo\swamp_izzo.exe") {
    Write-Host "✅ Build successful!" -ForegroundColor Green
    Write-Host "📂 Executable created at: dist\swamp_izzo\" -ForegroundColor Green
    Write-Host ""
    Write-Host "To test the app, run:" -ForegroundColor Cyan
    Write-Host "  .\dist\swamp_izzo\swamp_izzo.exe" -ForegroundColor White
    Write-Host ""
    Write-Host "To create an installer, use Inno Setup or NSIS" -ForegroundColor Cyan
} else {
    Write-Host "❌ Build failed!" -ForegroundColor Red
    exit 1
}
