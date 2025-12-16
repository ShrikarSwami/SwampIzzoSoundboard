"""Main entry point for the Swamp Izzo Soundboard application."""

import sys
import logging
import time
from pathlib import Path
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from .config import Config
from .ui import SoundboardWindow
from .hotkeys import start_hotkeys, register_hotkey, stop_hotkeys
from .audio import play_audio, preload_audio, get_audio_cache

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('soundboard.log')
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
        
        # Try to use glass panel as background
        assets_path = Path(__file__).parent.parent / 'assets' / 'ui'
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
        self.main_window = SoundboardWindow(self.config, self._on_hotkey)
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
            
            # Setup hotkeys
            self.setup_hotkeys()
            
            # Create and show main window
            self.create_main_window()
            
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
