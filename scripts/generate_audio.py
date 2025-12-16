#!/usr/bin/env python3
"""Generate startup audio file without external dependencies."""

import struct
import math

def create_wav_tone(filename, duration=2.0, frequency=440, sample_rate=44100):
    """Generate a simple WAV file with a tone."""
    
    num_samples = int(duration * sample_rate)
    
    # WAV header
    channels = 1
    bytes_per_sample = 2
    byte_rate = sample_rate * channels * bytes_per_sample
    block_align = channels * bytes_per_sample
    
    audio_data = b''
    
    # Generate sine wave
    for i in range(num_samples):
        sample = math.sin(2 * math.pi * frequency * i / sample_rate) * 32767 * 0.8
        audio_data += struct.pack('<h', int(sample))
    
    # Build WAV file
    wav = b'RIFF'
    wav += struct.pack('<I', 36 + len(audio_data))  # file size - 8
    wav += b'WAVE'
    
    # fmt sub-chunk
    wav += b'fmt '
    wav += struct.pack('<I', 16)  # subchunk size
    wav += struct.pack('<HHIIHH', 1, channels, sample_rate, byte_rate, block_align, 16)
    
    # data sub-chunk
    wav += b'data'
    wav += struct.pack('<I', len(audio_data))
    wav += audio_data
    
    with open(filename, 'wb') as f:
        f.write(wav)

def main():
    import os
    os.makedirs('assets/audio', exist_ok=True)
    
    # Create startup sound (ascending tones: SWAMP IZZO pattern)
    # S - 440 Hz, W - 550 Hz, A - 660 Hz, M - 770 Hz, P - 880 Hz
    create_wav_tone('assets/audio/startup_swamp_izzo.wav', duration=3.0, frequency=550)
    print("Created startup_swamp_izzo.wav")
    
    # Create placeholder sounds for each button (different frequencies)
    frequencies = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25, 587.33]
    for i in range(1, 10):
        create_wav_tone(f'assets/audio/sound_{i}.wav', duration=0.5, frequency=frequencies[i-1])
        print(f"Created sound_{i}.wav")

if __name__ == '__main__':
    main()
