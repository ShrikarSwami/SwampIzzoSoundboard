"""Swamp Izzo Soundboard - A cross-platform desktop soundboard application."""

__version__ = '1.0.0'
__author__ = 'Swamp Izzo'

from .app import main, SoundboardApp
from .config import Config
from .audio import play_audio, preload_audio
from .hotkeys import start_hotkeys, stop_hotkeys, register_hotkey
from .ui import SoundboardWindow

__all__ = [
    'main',
    'SoundboardApp',
    'Config',
    'play_audio',
    'preload_audio',
    'start_hotkeys',
    'stop_hotkeys',
    'register_hotkey',
    'SoundboardWindow',
]
