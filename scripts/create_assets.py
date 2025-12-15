#!/usr/bin/env python3
"""Create placeholder PNG assets for the soundboard."""

from PIL import Image, ImageDraw
import os

def create_glass_panel():
    """Create a frosted glass panel background."""
    img = Image.new('RGBA', (420, 420), (20, 20, 30, 200))
    draw = ImageDraw.Draw(img)
    
    # Add subtle glass effect with semi-transparent overlays
    for i in range(0, 420, 40):
        draw.line([(i, 0), (i, 420)], fill=(255, 255, 255, 5))
        draw.line([(0, i), (420, i)], fill=(255, 255, 255, 5))
    
    # Add border
    draw.rectangle([(5, 5), (415, 415)], outline=(200, 200, 255, 100), width=2)
    
    img.save('assets/ui/glass_panel.png')
    print("Created glass_panel.png")

def create_button(filename, color, alpha):
    """Create a button image."""
    size = (120, 120)
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw rounded rectangle with gradient-like effect
    margin = 5
    # Outer edge
    draw.rectangle(
        [(margin, margin), (size[0] - margin, size[1] - margin)],
        fill=(*color, alpha),
        outline=(100, 150, 255, 150)
    )
    
    # Inner highlight
    draw.rectangle(
        [(margin + 2, margin + 2), (size[0] - margin - 2, margin + 8)],
        fill=(255, 255, 255, 60)
    )
    
    img.save(f'assets/ui/{filename}')
    print(f"Created {filename}")

def main():
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    create_glass_panel()
    create_button('button_default.png', (30, 100, 200), 180)
    create_button('button_hover.png', (50, 130, 230), 200)
    create_button('button_pressed.png', (20, 80, 180), 220)
    
    print("All assets created successfully!")

if __name__ == '__main__':
    main()
