#!/usr/bin/env python3
"""Generate minimal PNG assets without PIL dependency."""

import struct
import zlib
import os

def create_png(width, height, r, g, b, alpha, filename):
    """Create a simple solid color PNG without PIL."""
    
    # PNG signature
    png_signature = b'\x89PNG\r\n\x1a\n'
    
    # IHDR chunk
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)  # RGBA
    ihdr_crc = zlib.crc32(b'IHDR' + ihdr_data) & 0xffffffff
    ihdr_chunk = struct.pack('>I', 13) + b'IHDR' + ihdr_data + struct.pack('>I', ihdr_crc)
    
    # IDAT chunk (image data) - simple solid color
    raw_data = b''
    for y in range(height):
        raw_data += b'\x00'  # filter type for this row
        for x in range(width):
            raw_data += struct.pack('BBBB', r, g, b, alpha)
    
    compressed = zlib.compress(raw_data)
    idat_crc = zlib.crc32(b'IDAT' + compressed) & 0xffffffff
    idat_chunk = struct.pack('>I', len(compressed)) + b'IDAT' + compressed + struct.pack('>I', idat_crc)
    
    # IEND chunk
    iend_crc = zlib.crc32(b'IEND') & 0xffffffff
    iend_chunk = struct.pack('>I', 0) + b'IEND' + struct.pack('>I', iend_crc)
    
    with open(filename, 'wb') as f:
        f.write(png_signature + ihdr_chunk + idat_chunk + iend_chunk)

def main():
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    os.makedirs('assets/ui', exist_ok=True)
    
    # Glass panel (dark, semi-transparent)
    create_png(420, 420, 20, 20, 30, 200, 'assets/ui/glass_panel.png')
    print("Created glass_panel.png")
    
    # Button default (blue)
    create_png(120, 120, 30, 100, 200, 180, 'assets/ui/button_default.png')
    print("Created button_default.png")
    
    # Button hover (lighter blue)
    create_png(120, 120, 50, 130, 230, 200, 'assets/ui/button_hover.png')
    print("Created button_hover.png")
    
    # Button pressed (darker blue)
    create_png(120, 120, 20, 80, 180, 220, 'assets/ui/button_pressed.png')
    print("Created button_pressed.png")
    
    print("All PNG assets generated!")

if __name__ == '__main__':
    main()
