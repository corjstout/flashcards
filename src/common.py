#!/usr/bin/python3

from pathlib import Path
from typing import Final

PROJECT_ROOT_DIR: Final[Path] = Path(__file__).resolve().parent.parent
CACHE_FILE: Final[Path] = Path.home() / ".flashcards"

def snake_to_title(snake_case_string):
    """Converts a snake_case string to a Title Case string."""
    words = snake_case_string.split('_')
    return ' '.join(word.capitalize() for word in words)
