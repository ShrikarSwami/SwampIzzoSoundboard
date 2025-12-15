#!/usr/bin/env python3
"""Entry point for running the Swamp Izzo Soundboard application."""

import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from src.app import main

if __name__ == '__main__':
    main()
