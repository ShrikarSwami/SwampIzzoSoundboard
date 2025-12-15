"""UI module for the soundboard application."""

import logging
import time
from pathlib import Path
from typing import Dict, Callable, Optional
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QGridLayout, QPushButton, QLabel,
    QVBoxLayout, QSystemTrayIcon, QMenu, QApplication
)
from PySide6.QtGui import QIcon, QPixmap, QFont, QColor
from PySide6.QtCore import Qt, QTimer, QSize

from .config import Config
from .audio import play_audio

logger = logging.getLogger(__name__)


class SoundboardButton(QPushButton):
    """Custom button for soundboard with state management."""
    
    def __init__(self, key: str, label: str, assets_path: str):
        """Initialize a soundboard button.
        
        Args:
            key: Key identifier (1-9)
            label: Display label
            assets_path: Path to assets directory
        """
        super().__init__(label)
        self.key = key
        self.label = label
        self.assets_path = Path(assets_path)
        self.pressed_state = False
        self.press_timer: Optional[QTimer] = None
        
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup button appearance."""
        self.setMinimumSize(QSize(120, 120))
        self.setMaximumSize(QSize(120, 120))
        
        # Load default image
        default_pixmap = QPixmap(str(self.assets_path / 'button_default.png'))
        if not default_pixmap.isNull():
            self.default_icon = QIcon(default_pixmap)
            self.setIcon(self.default_icon)
            self.setIconSize(QSize(120, 120))
        
        # Load hover and pressed images
        hover_pixmap = QPixmap(str(self.assets_path / 'button_hover.png'))
        if not hover_pixmap.isNull():
            self.hover_icon = QIcon(hover_pixmap)
        
        pressed_pixmap = QPixmap(str(self.assets_path / 'button_pressed.png'))
        if not pressed_pixmap.isNull():
            self.pressed_icon = QIcon(pressed_pixmap)
        
        # Style text
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.setFont(font)
        
        self.setStyleSheet("""
            QPushButton {
                color: white;
                border: none;
                border-radius: 8px;
                padding: 0px;
            }
            QPushButton:hover {
                background-color: rgba(50, 130, 230, 50);
            }
        """)
    
    def show_pressed_state(self, duration_ms: int = 100):
        """Show pressed state briefly.
        
        Args:
            duration_ms: Duration to show pressed state in milliseconds
        """
        if hasattr(self, 'pressed_icon'):
            self.setIcon(self.pressed_icon)
        
        self.pressed_state = True
        
        if self.press_timer is not None:
            self.press_timer.stop()
        
        self.press_timer = QTimer()
        self.press_timer.setSingleShot(True)
        self.press_timer.timeout.connect(self._reset_state)
        self.press_timer.start(duration_ms)
    
    def _reset_state(self):
        """Reset to default state."""
        if hasattr(self, 'default_icon'):
            self.setIcon(self.default_icon)
        self.pressed_state = False


class SoundboardWindow(QMainWindow):
    """Main soundboard window."""
    
    def __init__(self, config: Config, on_hotkey_triggered: Callable = None):
        """Initialize the soundboard window.
        
        Args:
            config: Configuration object
            on_hotkey_triggered: Callback for hotkey events
        """
        super().__init__()
        self.config = config
        self.on_hotkey_triggered = on_hotkey_triggered
        self.button_states: Dict[str, int] = {}  # Track cycle index for each key
        self.last_press_time: Dict[str, float] = {}  # Track last press time
        self.buttons: Dict[str, SoundboardButton] = {}
        self.assets_path = Path(__file__).parent.parent / 'assets' / 'ui'
        
        self._setup_ui()
        self._setup_tray_icon()
    
    def _setup_ui(self):
        """Setup the main UI."""
        self.setWindowTitle("Swamp Izzo Soundboard")
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        
        # Window size
        width, height = self.config.get_window_size()
        self.setFixedSize(width, height)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(5)
        
        # Add background glass panel if available
        bg_pixmap = QPixmap(str(self.assets_path / 'glass_panel.png'))
        if not bg_pixmap.isNull():
            central_widget.setStyleSheet(f"""
                QWidget {{
                    background-image: url({str(self.assets_path / 'glass_panel.png')});
                    background-repeat: no-repeat;
                    background-position: center;
                }}
            """)
        
        # Grid for buttons
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)
        
        # Create 3x3 button grid
        keys = self.config.get_all_keys()
        for idx, key in enumerate(sorted(keys)):
            if idx >= 9:  # Only 9 buttons
                break
            
            key_config = self.config.get_key_config(key)
            label = key_config.get('label', f'Key {key}')
            
            button = SoundboardButton(key, label, self.assets_path)
            button.clicked.connect(lambda checked, k=key: self._on_button_clicked(k))
            
            self.buttons[key] = button
            self.button_states[key] = 0
            self.last_press_time[key] = 0
            
            row = idx // 3
            col = idx % 3
            grid_layout.addWidget(button, row, col)
        
        main_layout.addLayout(grid_layout)
        main_layout.addStretch()
        
        # Style the window
        self.setStyleSheet("""
            QMainWindow {
                background-color: rgba(20, 20, 30, 220);
            }
        """)
    
    def _setup_tray_icon(self):
        """Setup system tray icon."""
        try:
            tray_menu = QMenu()
            quit_action = tray_menu.addAction("Quit")
            quit_action.triggered.connect(self._quit_app)
            
            self.tray_icon = QSystemTrayIcon(self)
            self.tray_icon.setContextMenu(tray_menu)
            
            # Use a simple icon from Qt
            icon = self.style().standardIcon(self.style().SP_MediaPlay)
            self.tray_icon.setIcon(icon)
            self.tray_icon.show()
        
        except Exception as e:
            logger.warning(f"Could not setup tray icon: {e}")
    
    def trigger_sound(self, key: str) -> None:
        """Trigger sound for a key.
        
        Args:
            key: Key identifier (1-9)
        """
        key_config = self.config.get_key_config(key)
        clips = key_config.get('clips', [])
        reset_seconds = key_config.get('reset_seconds', 10)
        
        if not clips:
            logger.warning(f"No clips configured for key {key}")
            return
        
        # Check if we should reset the cycle
        current_time = time.time()
        last_press = self.last_press_time.get(key, 0)
        if current_time - last_press > reset_seconds:
            self.button_states[key] = 0
        
        self.last_press_time[key] = current_time
        
        # Get current clip
        clip_idx = self.button_states[key]
        clip_path = clips[clip_idx]
        
        # Advance to next clip for next press
        self.button_states[key] = (clip_idx + 1) % len(clips)
        
        # Show button pressed state
        if key in self.buttons:
            self.buttons[key].show_pressed_state()
        
        # Play audio
        logger.info(f"Key {key}: Playing clip {clip_idx}/{len(clips)} - {clip_path}")
        play_audio(clip_path)
    
    def _on_button_clicked(self, key: str):
        """Handle button click.
        
        Args:
            key: Key identifier
        """
        self.trigger_sound(key)
    
    def on_hotkey(self, key: str):
        """Handle hotkey event.
        
        Args:
            key: Key identifier
        """
        self.trigger_sound(key)
        if self.on_hotkey_triggered:
            self.on_hotkey_triggered(key)
    
    def _quit_app(self):
        """Quit the application."""
        QApplication.quit()
    
    def closeEvent(self, event):
        """Handle window close event - minimize to tray instead."""
        self.hide()
        event.ignore()
    
    def changeEvent(self, event):
        """Handle window state changes."""
        if event.type() == event.Type.WindowStateChange:
            if self.isMinimized():
                self.hide()
                event.ignore()
