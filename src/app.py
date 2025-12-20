"""Main entry point for the Swamp Izzo Soundboard application."""

import sys
import os
import logging
import time
from pathlib import Path
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

# Support running both as a package (python -m src.app) and as a frozen app bundle
try:
    from .config import Config
    from .ui import SoundboardWindow
    from .hotkeys import start_hotkeys, register_hotkey, stop_hotkeys
    from .audio import play_audio, preload_audio, get_audio_cache
except Exception:
    # Fallback for PyInstaller where relative imports don't resolve
    root_dir = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(root_dir.parent))  # allow `import src.*`
    from src.config import Config  # type: ignore
    from src.ui import SoundboardWindow  # type: ignore
    from src.hotkeys import start_hotkeys, register_hotkey, stop_hotkeys  # type: ignore
    from src.audio import play_audio, preload_audio, get_audio_cache  # type: ignore

# Setup logging to a user-writable location
def _log_file_path() -> Path:
    try:
        if sys.platform == 'darwin':
            base = Path.home() / 'Library' / 'Logs' / 'SwampIzzo'
        elif sys.platform.startswith('win'):
            base = Path(os.environ.get('APPDATA', Path.home())) / 'SwampIzzo' / 'Logs'
        else:
            base = Path.home() / '.swamp_izzo' / 'logs'
        base.mkdir(parents=True, exist_ok=True)
        return base / 'soundboard.log'
    except Exception:
        return Path('soundboard.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(_log_file_path())
    ]
)
logger = logging.getLogger(__name__)


class LoadingScreen(QWidget):
    """Custom loading screen."""
    
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(420, 420)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Determine assets path (works for both dev and frozen build)
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            base_path = Path(getattr(sys, '_MEIPASS'))
        else:
            base_path = Path(__file__).parent.parent
        assets_path = base_path / 'assets' / 'ui'
        bg_path = assets_path / 'glass_panel.png'
        
        if bg_path.exists():
            self.setStyleSheet(f"""
                QWidget {{
                    background-image: url({str(bg_path)});
                    background-repeat: no-repeat;
                    background-position: center;
                }}
            """)
        else:
            self.setStyleSheet("""
                QWidget {
                    background-color: rgba(20, 20, 30, 220);
                }
            """)
        
        # Loading text
        label = QLabel("Loading Swamp Izzo...")
        label.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        label.setFont(font)
        label.setStyleSheet("color: white;")
        
        layout.addStretch()
        layout.addWidget(label)
        layout.addStretch()
        
        # Center on screen
        self.move(100, 100)


class SoundboardApp:
    """Main application controller."""
    
    def __init__(self):
        """Initialize the application."""
        self.app = QApplication.instance() or QApplication(sys.argv)
        self.config = Config()
        self.main_window = None
        self.loading_screen = None
    
    def show_loading_screen(self):
        """Display loading screen."""
        logger.info("Showing loading screen")
        self.loading_screen = LoadingScreen()
        self.loading_screen.show()
        self.app.processEvents()
        time.sleep(0.5)  # Show for 0.5 seconds
    
    def hide_loading_screen(self):
        """Hide loading screen."""
        if self.loading_screen:
            self.loading_screen.close()
            self.loading_screen = None
            self.app.processEvents()
    
    def play_startup_sound(self):
        """Play the startup sound."""
        logger.info("Playing startup sound")
        startup_audio = self.config.get_startup_audio()
        play_audio(startup_audio)
        
        # Give it time to play
        time.sleep(1.0)
    
    def preload_audio_assets(self):
        """Preload all configured audio files."""
        logger.info("Preloading audio assets")
        
        for key in self.config.get_all_keys():
            key_config = self.config.get_key_config(key)
            clips = key_config.get('clips', [])
            
            for clip_path in clips:
                try:
                    preload_audio(clip_path)
                except Exception as e:
                    logger.error(f"Error preloading {clip_path}: {e}")
        
        logger.info("Audio preloading complete")
    
    def setup_hotkeys(self):
        """Setup global hotkeys."""
        logger.info("Setting up global hotkeys")
        
        for key in self.config.get_all_keys():
            register_hotkey(key, self._on_hotkey)
        
        start_hotkeys()
        logger.info("Global hotkeys activated")
    
    def _on_hotkey(self, key: str):
        """Handle global hotkey event.
        
        Args:
            key: Key identifier (1-9)
        """
        logger.debug(f"Hotkey triggered: {key}")
        if self.main_window:
            self.main_window.on_hotkey(key)
    
    def create_main_window(self):
        """Create and show the main window."""
        logger.info("Creating main window")
        # Determine assets root for UI package API (expects assets directory)
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            base_path = Path(getattr(sys, '_MEIPASS'))
        else:
            base_path = Path(__file__).parent.parent
        assets_root = base_path / 'assets'
        try:
            self.main_window = SoundboardWindow(assets_root)
        except TypeError:
            # Fallback to legacy signature SoundboardWindow(config, callback)
            self.main_window = SoundboardWindow(self.config)
        self.main_window.show()
    
    def run(self):
        """Run the application."""
        logger.info("Starting Swamp Izzo Soundboard")
        
        try:
            # Show loading screen
            self.show_loading_screen()
            
            # Preload assets
            self.preload_audio_assets()
            
            # Play startup sound
            self.play_startup_sound()
            
            # Hide loading screen
            self.hide_loading_screen()
            
            # Create and show main window first so users see UI even if hotkeys fail
            self.create_main_window()
            
            # Setup hotkeys (skip by default on macOS to avoid TCC crash without permissions)
            enable_hotkeys = True
            if sys.platform == 'darwin' and os.environ.get('SWAMP_IZZO_ENABLE_HOTKEYS', '0') != '1':
                enable_hotkeys = False
                logger.warning("Hotkeys disabled by default on macOS. Grant Accessibility permission and set SWAMP_IZZO_ENABLE_HOTKEYS=1 to enable.")
            
            if enable_hotkeys:
                try:
                    self.setup_hotkeys()
                except Exception as e:
                    logger.error(f"Failed to start global hotkeys: {e}")
            
            logger.info("Application ready")
            
            # Run the event loop
            return self.app.exec()
        
        except Exception as e:
            logger.error(f"Fatal error: {e}", exc_info=True)
            return 1
        
        finally:
            # Cleanup
            stop_hotkeys()
            get_audio_cache().stop_all()
            logger.info("Application shutdown complete")


def main():
    """Entry point for the application."""
    app = SoundboardApp()
    sys.exit(app.run())


if __name__ == '__main__':
    main()
