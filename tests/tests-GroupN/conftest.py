"""
Shared pytest configuration for the Group N Zero2Neuro unit tests.

Zero2Neuro stores its Python source modules in the project's `src`
directory. This file adds that directory to Python's import path so the
unit tests can import and test the existing Zero2Neuro modules.
"""

import sys
from pathlib import Path

# Locate the Zero2Neuro project root and its source directory.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = PROJECT_ROOT / "src"

# Allow test files to import modules directly from Zero2Neuro's src folder.
sys.path.insert(0, str(SRC_DIR))
