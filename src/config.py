"""Configuration loading and validation for the soundboard app."""

import json
import logging
from pathlib import Path
from typing import Dict, List, Any

logger = logging.getLogger(__name__)


class Config:
    """Load and validate soundboard configuration."""
    
    def __init__(self, config_path: str = None):
        """Initialize config from JSON file.
        
        Args:
            config_path: Path to config.json. Defaults to config.json in app root.
        """
        if config_path is None:
            # Try to find config.json in the app root
            app_root = Path(__file__).parent.parent
            config_path = app_root / 'config.json'
        
        self.config_path = Path(config_path)
        self.data = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load and validate configuration from JSON."""
        if not self.config_path.exists():
            logger.warning(f"Config file not found at {self.config_path}, using defaults")
            return self._get_default_config()
        
        try:
            with open(self.config_path, 'r') as f:
                data = json.load(f)
            logger.info(f"Loaded config from {self.config_path}")
            return data
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration."""
        return {
            "keys": {
                "1": {
                    "label": "Clip 1",
                    "clips": ["assets/audio/sound_1.wav"],
                    "reset_seconds": 10
                },
                "2": {
                    "label": "Clip 2",
                    "clips": ["assets/audio/sound_2.wav"],
                    "reset_seconds": 10
                },
                "3": {
                    "label": "Clip 3",
                    "clips": ["assets/audio/sound_3.wav"],
                    "reset_seconds": 10
                },
                "4": {
                    "label": "Clip 4",
                    "clips": ["assets/audio/sound_4.wav"],
                    "reset_seconds": 10
                },
                "5": {
                    "label": "Clip 5",
                    "clips": ["assets/audio/sound_5.wav"],
                    "reset_seconds": 10
                },
                "6": {
                    "label": "Clip 6",
                    "clips": ["assets/audio/sound_6.wav"],
                    "reset_seconds": 10
                },
                "7": {
                    "label": "Clip 7",
                    "clips": ["assets/audio/sound_7.wav"],
                    "reset_seconds": 10
                },
                "8": {
                    "label": "Clip 8",
                    "clips": ["assets/audio/sound_8.wav"],
                    "reset_seconds": 10
                },
                "9": {
                    "label": "Clip 9",
                    "clips": ["assets/audio/sound_9.wav"],
                    "reset_seconds": 10
                }
            }
        }
    
    def get_key_config(self, key: str) -> Dict[str, Any]:
        """Get configuration for a specific key.
        
        Args:
            key: The key identifier (string 1-9)
            
        Returns:
            Dictionary with label, clips, and reset_seconds
        """
        keys = self.data.get('keys', {})
        if key not in keys:
            logger.warning(f"Key {key} not found in config, returning default")
            return {"label": f"Key {key}", "clips": [], "reset_seconds": 10}
        return keys[key]
    
    def get_all_keys(self) -> List[str]:
        """Get all configured keys."""
        return sorted(self.data.get('keys', {}).keys())
    
    def get_startup_audio(self) -> str:
        """Get path to startup audio file."""
        return self.data.get('startup_audio', 'assets/audio/startup_swamp_izzo.wav')
    
    def get_window_size(self) -> tuple:
        """Get window size (width, height)."""
        app = self.data.get('app', {})
        return (app.get('window_width', 420), app.get('window_height', 420))
