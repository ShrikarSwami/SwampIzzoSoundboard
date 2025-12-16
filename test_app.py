#!/usr/bin/env python3
"""Test script for Swamp Izzo Soundboard."""

import sys
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_imports():
    """Test that all required modules can be imported."""
    logger.info("Testing imports...")
    
    try:
        import PySide6
        logger.info("PySide6: OK")
    except ImportError as e:
        logger.error(f"PySide6: FAILED - {e}")
        return False
    
    try:
        import pynput
        logger.info("pynput: OK")
    except ImportError as e:
        logger.error(f"pynput: FAILED - {e}")
        return False
    
    try:
        import sounddevice
        logger.info("sounddevice: OK")
    except ImportError as e:
        logger.error(f"sounddevice: FAILED - {e}")
        return False
    
    try:
        import numpy
        logger.info("numpy: OK")
    except ImportError as e:
        logger.error(f"numpy: FAILED - {e}")
        return False
    
    try:
        from src import config, audio, hotkeys, ui, app
        logger.info("All source modules: OK")
    except ImportError as e:
        logger.error(f"Source modules: FAILED - {e}")
        return False
    
    return True


def test_assets():
    """Test that all required assets exist."""
    logger.info("Testing assets...")
    
    required_files = [
        'assets/ui/glass_panel.png',
        'assets/ui/button_default.png',
        'assets/ui/button_hover.png',
        'assets/ui/button_pressed.png',
        'assets/audio/startup_swamp_izzo.wav',
        'assets/audio/sound_1.wav',
        'assets/audio/sound_2.wav',
        'assets/audio/sound_3.wav',
        'assets/audio/sound_4.wav',
        'assets/audio/sound_5.wav',
        'assets/audio/sound_6.wav',
        'assets/audio/sound_7.wav',
        'assets/audio/sound_8.wav',
        'assets/audio/sound_9.wav',
        'config.json',
    ]
    
    missing = []
    for file in required_files:
        path = Path(file)
        if not path.exists():
            missing.append(file)
            logger.error(f"Missing: {file}")
        else:
            size = path.stat().st_size
            logger.info(f"OK: {file} ({size} bytes)")
    
    return len(missing) == 0


def test_config():
    """Test configuration loading."""
    logger.info("Testing configuration...")
    
    try:
        from src.config import Config
        config = Config()
        
        # Test key loading
        keys = config.get_all_keys()
        logger.info(f"Loaded {len(keys)} keys: {keys}")
        
        # Test key config
        for key in ['1', '2', '3']:
            key_config = config.get_key_config(key)
            logger.info(f"Key {key}: {key_config.get('label')}")
        
        # Test startup audio
        startup = config.get_startup_audio()
        logger.info(f"Startup audio: {startup}")
        
        # Test window size
        size = config.get_window_size()
        logger.info(f"Window size: {size}")
        
        return True
    
    except Exception as e:
        logger.error(f"Config test failed: {e}")
        return False


def test_audio():
    """Test audio loading and caching."""
    logger.info("Testing audio module...")
    
    try:
        from src.audio import get_audio_cache, preload_audio
        
        cache = get_audio_cache()
        logger.info("Audio cache initialized")
        
        # Try preloading a file
        preload_audio('assets/audio/sound_1.wav')
        logger.info("Audio preload: OK")
        
        return True
    
    except Exception as e:
        logger.error(f"Audio test failed: {e}")
        return False


def test_hotkeys():
    """Test hotkey module initialization."""
    logger.info("Testing hotkeys module...")
    
    try:
        from src.hotkeys import get_listener
        
        listener = get_listener()
        logger.info("Hotkey listener created")
        
        # Register a test callback
        listener.register_callback('1', lambda x: logger.info(f"Hotkey callback for {x}"))
        logger.info("Hotkey registration: OK")
        
        return True
    
    except Exception as e:
        logger.error(f"Hotkey test failed: {e}")
        return False


def test_ui():
    """Test UI module initialization (without displaying)."""
    logger.info("Testing UI module...")
    
    try:
        from PySide6.QtWidgets import QApplication
        from src.config import Config
        from src.ui import SoundboardWindow
        
        # Create app instance if needed
        app = QApplication.instance() or QApplication([])
        
        config = Config()
        window = SoundboardWindow(config)
        logger.info("SoundboardWindow created: OK")
        
        # Check buttons created
        if len(window.buttons) == 9:
            logger.info(f"Buttons created: {len(window.buttons)} buttons")
        else:
            logger.warning(f"Expected 9 buttons, got {len(window.buttons)}")
        
        return True
    
    except Exception as e:
        logger.error(f"UI test failed: {e}")
        return False


def main():
    """Run all tests."""
    logger.info("Starting Swamp Izzo test suite...")
    
    tests = [
        ("Imports", test_imports),
        ("Assets", test_assets),
        ("Configuration", test_config),
        ("Audio Module", test_audio),
        ("Hotkeys Module", test_hotkeys),
        ("UI Module", test_ui),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
            status = "PASSED" if result else "FAILED"
            logger.info(f"{name}: {status}")
        except Exception as e:
            logger.error(f"{name}: EXCEPTION - {e}")
            results.append((name, False))
    
    # Summary
    logger.info("\n" + "="*50)
    logger.info("Test Summary")
    logger.info("="*50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "PASS" if result else "FAIL"
        logger.info(f"{name:30} {status}")
    
    logger.info("="*50)
    logger.info(f"Total: {passed}/{total} passed")
    
    return 0 if passed == total else 1


if __name__ == '__main__':
    sys.exit(main())
