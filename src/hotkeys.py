"""Global hotkey listener for cross-platform support."""

import logging
import threading
from typing import Callable, Dict, Optional
from pynput import keyboard

logger = logging.getLogger(__name__)


class GlobalHotKeyListener:
    """Listen for global hotkeys using pynput."""
    
    def __init__(self):
        """Initialize the hotkey listener."""
        self._listener: Optional[keyboard.Listener] = None
        self._callbacks: Dict[str, Callable] = {}
        
        # Build numpad key map - handle platform differences
        self._numpad_map = {}
        try:
            # Try standard numpad key names
            self._numpad_map.update({
                keyboard.Key.kp_1: '1',
                keyboard.Key.kp_2: '2',
                keyboard.Key.kp_3: '3',
                keyboard.Key.kp_4: '4',
                keyboard.Key.kp_5: '5',
                keyboard.Key.kp_6: '6',
                keyboard.Key.kp_7: '7',
                keyboard.Key.kp_8: '8',
                keyboard.Key.kp_9: '9',
            })
        except AttributeError:
            # Fallback for platforms that don't have these names
            logger.warning("Standard numpad keys not available on this platform")
        
        self._number_map = {
            '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
            '6': '6', '7': '7', '8': '8', '9': '9',
        }
    
    def register_callback(self, key: str, callback: Callable) -> None:
        """Register a callback for a key.
        
        Args:
            key: The key identifier ('1'-'9')
            callback: Function to call when key is pressed
        """
        self._callbacks[key] = callback
        logger.info(f"Registered hotkey callback for {key}")
    
    def start(self) -> None:
        """Start listening for global hotkeys."""
        if self._listener is not None:
            logger.warning("Listener already started")
            return
        
        self._listener = keyboard.Listener(on_press=self._on_key_press)
        self._listener.start()
        logger.info("Global hotkey listener started")
    
    def stop(self) -> None:
        """Stop listening for global hotkeys."""
        if self._listener is not None:
            self._listener.stop()
            self._listener = None
            logger.info("Global hotkey listener stopped")
    
    def _on_key_press(self, key) -> None:
        """Handle key press events."""
        try:
            key_str = None
            
            # Check if it's a numpad key
            if key in self._numpad_map:
                key_str = self._numpad_map[key]
                logger.debug(f"Numpad key pressed: {key_str}")
            
            # Check if it's a regular number key
            elif isinstance(key, keyboard.KeyCode):
                char = key.char
                if char in self._number_map:
                    key_str = self._number_map[char]
                    logger.debug(f"Number key pressed: {key_str}")
            
            # Call registered callback if exists
            if key_str and key_str in self._callbacks:
                callback = self._callbacks[key_str]
                threading.Thread(target=callback, args=(key_str,), daemon=True).start()
        
        except Exception as e:
            logger.error(f"Error handling key press: {e}")
    
    def __del__(self):
        """Cleanup on deletion."""
        self.stop()


# Global listener instance
_listener: Optional[GlobalHotKeyListener] = None


def get_listener() -> GlobalHotKeyListener:
    """Get or create the global hotkey listener."""
    global _listener
    if _listener is None:
        _listener = GlobalHotKeyListener()
    return _listener


def register_hotkey(key: str, callback: Callable) -> None:
    """Register a global hotkey callback.
    
    Args:
        key: The key identifier ('1'-'9')
        callback: Function to call when key is pressed
    """
    get_listener().register_callback(key, callback)


def start_hotkeys() -> None:
    """Start listening for global hotkeys."""
    get_listener().start()


def stop_hotkeys() -> None:
    """Stop listening for global hotkeys."""
    get_listener().stop()
