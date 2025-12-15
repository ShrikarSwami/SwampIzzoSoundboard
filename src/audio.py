"""Audio playback with caching for low-latency cross-platform support."""

import logging
from pathlib import Path
from typing import Dict, Optional
import threading
import queue
import time
import wave
import io

try:
    import simpleaudio as sa
    SIMPLEAUDIO_AVAILABLE = True
except ImportError:
    SIMPLEAUDIO_AVAILABLE = False

try:
    import sounddevice as sd
    import numpy as np
    SOUNDDEVICE_AVAILABLE = True
except ImportError:
    SOUNDDEVICE_AVAILABLE = False

logger = logging.getLogger(__name__)


class AudioCache:
    """Cache audio data to avoid reload lag."""
    
    def __init__(self):
        self._cache: Dict[str, bytes] = {}
        self._running = True
    
    def load_audio_file(self, file_path: str) -> bytes:
        """Load audio file into cache.
        
        Args:
            file_path: Path to WAV file
            
        Returns:
            Raw audio bytes
        """
        file_path = str(file_path)
        
        if file_path in self._cache:
            logger.debug(f"Audio cache hit: {file_path}")
            return self._cache[file_path]
        
        try:
            path = Path(file_path)
            if not path.exists():
                logger.error(f"Audio file not found: {file_path}")
                return b''
            
            with open(file_path, 'rb') as f:
                data = f.read()
            
            self._cache[file_path] = data
            logger.info(f"Loaded audio to cache: {file_path} ({len(data)} bytes)")
            return data
        
        except Exception as e:
            logger.error(f"Error loading audio file {file_path}: {e}")
            return b''
    
    def play_audio(self, file_path: str) -> bool:
        """Play audio file using best available method.
        
        Args:
            file_path: Path to WAV file
            
        Returns:
            True if playback started successfully
        """
        try:
            audio_data = self.load_audio_file(file_path)
            
            if not audio_data:
                logger.warning(f"No audio data to play for {file_path}")
                return False
            
            if SOUNDDEVICE_AVAILABLE:
                return self._play_with_sounddevice(file_path, audio_data)
            elif SIMPLEAUDIO_AVAILABLE:
                return self._play_with_simpleaudio(file_path, audio_data)
            else:
                logger.error("No audio playback library available")
                return False
        
        except Exception as e:
            logger.error(f"Error playing audio: {e}")
            return False
    
    def _parse_wav(self, audio_data: bytes) -> tuple:
        """Parse WAV file data.
        
        Returns:
            Tuple of (frames, channels, sample_width, framerate)
        """
        try:
            with io.BytesIO(audio_data) as f:
                with wave.open(f, 'rb') as wav_file:
                    frames = wav_file.readframes(wav_file.getnframes())
                    channels = wav_file.getnchannels()
                    sample_width = wav_file.getsampwidth()
                    framerate = wav_file.getframerate()
                    return frames, channels, sample_width, framerate
        except Exception as e:
            logger.error(f"Error parsing WAV file: {e}")
            return None, None, None, None
    
    def _play_with_simpleaudio(self, file_path: str, audio_data: bytes) -> bool:
        """Play audio using simpleaudio."""
        try:
            frames, channels, sample_width, framerate = self._parse_wav(audio_data)
            if frames is None:
                return False
            
            play_obj = sa.play_buffer(
                frames,
                channels,
                sample_width,
                framerate
            )
            logger.debug(f"Started playback with simpleaudio: {file_path}")
            return True
        
        except Exception as e:
            logger.error(f"Error with simpleaudio playback: {e}")
            return False
    
    def _play_with_sounddevice(self, file_path: str, audio_data: bytes) -> bool:
        """Play audio using sounddevice."""
        try:
            frames, channels, sample_width, framerate = self._parse_wav(audio_data)
            if frames is None:
                return False
            
            # Convert byte frames to numpy array for sounddevice
            if sample_width == 1:
                dtype = np.uint8
            elif sample_width == 2:
                dtype = np.int16
            elif sample_width == 3:
                # 24-bit audio - convert to 16-bit
                dtype = np.int16
                # Simplified 24-bit to 16-bit conversion
                frames_array = np.frombuffer(frames, dtype=np.int8).reshape(-1, 3)
                frames_16bit = frames_array[:, :2].astype(np.int16)
                frames_array = frames_16bit
            else:
                dtype = np.int32
            
            if sample_width != 3:
                frames_array = np.frombuffer(frames, dtype=dtype)
            
            # Reshape for stereo/mono
            if channels > 1:
                frames_array = frames_array.reshape(-1, channels)
            
            # Play in background thread
            threading.Thread(
                target=lambda: sd.play(frames_array, framerate),
                daemon=True
            ).start()
            
            logger.debug(f"Started playback with sounddevice: {file_path}")
            return True
        
        except Exception as e:
            logger.error(f"Error with sounddevice playback: {e}")
            return False
    
    def stop_all(self):
        """Stop all playback and cleanup."""
        self._running = False
        if SIMPLEAUDIO_AVAILABLE:
            try:
                sa.stop_all()
            except:
                pass
        if SOUNDDEVICE_AVAILABLE:
            try:
                sd.stop()
            except:
                pass
    
    def __del__(self):
        self.stop_all()


# Global audio cache instance
_audio_cache: Optional[AudioCache] = None


def get_audio_cache() -> AudioCache:
    """Get or create the global audio cache."""
    global _audio_cache
    if _audio_cache is None:
        _audio_cache = AudioCache()
    return _audio_cache


def play_audio(file_path: str) -> bool:
    """Play an audio file.
    
    Args:
        file_path: Path to WAV file
        
    Returns:
        True if playback started successfully
    """
    return get_audio_cache().play_audio(file_path)


def preload_audio(file_path: str) -> None:
    """Preload audio file into cache.
    
    Args:
        file_path: Path to WAV file
    """
    get_audio_cache().load_audio_file(file_path)
