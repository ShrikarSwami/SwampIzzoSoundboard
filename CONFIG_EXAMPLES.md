# Example Configuration

This file demonstrates advanced configuration options for the Swamp Izzo Soundboard.

## Basic Configuration

```json
{
  "startup_audio": "assets/audio/startup_swamp_izzo.wav",
  "app": {
    "window_width": 420,
    "window_height": 420
  },
  "keys": {
    "1": {
      "label": "Bass Drop",
      "clips": ["assets/audio/sound_1.wav"],
      "reset_seconds": 10
    }
  }
}
```

## Multi-Clip Configuration (Type B Cycling)

Each button can cycle through multiple audio files:

```json
{
  "keys": {
    "1": {
      "label": "Laughs",
      "clips": [
        "assets/audio/laugh1.wav",
        "assets/audio/laugh2.wav",
        "assets/audio/laugh3.wav"
      ],
      "reset_seconds": 15
    },
    "2": {
      "label": "Cheers",
      "clips": [
        "assets/audio/cheer_short.wav",
        "assets/audio/cheer_long.wav"
      ],
      "reset_seconds": 10
    }
  }
}
```

## Advanced Features

### Reset Timer

The `reset_seconds` value determines how long the button waits before resetting the clip cycle back to the first clip.

Example: If `reset_seconds` is 10, pressing the button will cycle through clips. If you wait more than 10 seconds and press again, it resets to the first clip.

```json
{
  "1": {
    "label": "Quick Clips",
    "clips": ["clip1.wav", "clip2.wav", "clip3.wav"],
    "reset_seconds": 5
  }
}
```

### Custom Audio Paths

Audio files can be in any subdirectory:

```json
{
  "1": {
    "label": "My Sounds",
    "clips": [
      "assets/audio/custom/my_sound_1.wav",
      "assets/audio/custom/my_sound_2.wav"
    ],
    "reset_seconds": 10
  }
}
```

## Full Example Configuration

```json
{
  "startup_audio": "assets/audio/startup_swamp_izzo.wav",
  "app": {
    "window_width": 420,
    "window_height": 420
  },
  "keys": {
    "1": {
      "label": "Laughs",
      "clips": [
        "assets/audio/laugh1.wav",
        "assets/audio/laugh2.wav",
        "assets/audio/laugh3.wav"
      ],
      "reset_seconds": 10
    },
    "2": {
      "label": "Cheers",
      "clips": [
        "assets/audio/cheer_short.wav",
        "assets/audio/cheer_long.wav"
      ],
      "reset_seconds": 10
    },
    "3": {
      "label": "Effects",
      "clips": [
        "assets/audio/whoosh.wav",
        "assets/audio/pop.wav",
        "assets/audio/beep.wav"
      ],
      "reset_seconds": 8
    },
    "4": {
      "label": "Music",
      "clips": ["assets/audio/music_clip.wav"],
      "reset_seconds": 10
    },
    "5": {
      "label": "Vocals",
      "clips": [
        "assets/audio/vocal1.wav",
        "assets/audio/vocal2.wav"
      ],
      "reset_seconds": 15
    },
    "6": {
      "label": "Reactions",
      "clips": ["assets/audio/reaction.wav"],
      "reset_seconds": 10
    },
    "7": {
      "label": "Notifications",
      "clips": [
        "assets/audio/notif1.wav",
        "assets/audio/notif2.wav"
      ],
      "reset_seconds": 10
    },
    "8": {
      "label": "Ambient",
      "clips": ["assets/audio/ambient.wav"],
      "reset_seconds": 10
    },
    "9": {
      "label": "Special",
      "clips": [
        "assets/audio/special1.wav",
        "assets/audio/special2.wav",
        "assets/audio/special3.wav",
        "assets/audio/special4.wav"
      ],
      "reset_seconds": 20
    }
  }
}
```

## Tips and Tricks

### Creating a "Random" Feel

Add multiple variations of the same sound to make it feel less repetitive:

```json
{
  "1": {
    "label": "Reactions",
    "clips": [
      "assets/audio/yeah1.wav",
      "assets/audio/yeah2.wav",
      "assets/audio/yeah3.wav",
      "assets/audio/yeah4.wav",
      "assets/audio/yeah5.wav"
    ],
    "reset_seconds": 5
  }
}
```

### Long Clips vs Short Clips

Use different reset timers based on clip length:

```json
{
  "1": {
    "label": "Short Clips",
    "clips": ["short1.wav", "short2.wav", "short3.wav"],
    "reset_seconds": 3
  },
  "2": {
    "label": "Long Clips",
    "clips": ["long1.wav", "long2.wav"],
    "reset_seconds": 30
  }
}
```

### Organizing by Category

Use labels and custom paths to organize sounds:

```json
{
  "1": {
    "label": "Effects",
    "clips": [
      "assets/audio/effects/whoosh.wav",
      "assets/audio/effects/pop.wav"
    ],
    "reset_seconds": 10
  },
  "2": {
    "label": "Voices",
    "clips": [
      "assets/audio/voices/hello.wav",
      "assets/audio/voices/goodbye.wav"
    ],
    "reset_seconds": 10
  }
}
```

## Audio Requirements

- **Format**: WAV (Waveform Audio File Format)
- **Sample Rate**: Any (8kHz to 192kHz)
- **Bit Depth**: Any (8-bit to 32-bit)
- **Channels**: Mono or Stereo
- **Compression**: PCM (uncompressed)

## Converting Audio Files

To convert MP3 or other formats to WAV:

### Using FFmpeg (recommended)

```bash
# Convert MP3 to WAV
ffmpeg -i input.mp3 output.wav

# Convert MP4 video to WAV (audio only)
ffmpeg -i input.mp4 -vn output.wav

# Adjust sample rate if needed
ffmpeg -i input.mp3 -ar 44100 output.wav
```

### Using Audacity (GUI)

1. Open Audacity
2. File > Open your audio file
3. File > Export > Export as WAV
4. Choose quality settings
5. Save to assets/audio/

## Troubleshooting Configuration

### Keys not appearing

Make sure your `config.json` is valid JSON:
- Use double quotes for strings
- Check for missing commas
- Validate at [jsonlint.com](https://www.jsonlint.com/)

### Audio files not found

- Check file paths are correct (case-sensitive on macOS/Linux)
- Use forward slashes / not backslashes
- Place files in assets/audio/ subdirectory
- Verify files exist before starting app

### Clips not cycling

- Make sure you have multiple clips in the array
- Wait for reset_seconds before pressing again
- Check soundboard.log for errors

## Performance Considerations

- **File Size**: Smaller files = faster loading (< 5MB each recommended)
- **Sample Rate**: 44100 Hz is standard
- **Bit Depth**: 16-bit or 24-bit is standard
- **Quantity**: Each clip is loaded into memory on first play

For 9 keys with 5 clips each at ~1MB per clip = ~45MB total memory usage.
