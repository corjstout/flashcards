
from pathlib import Path
from typing import Final

PROJECT_ROOT_DIR: Final[Path] = Path(__file__).resolve().parent.parent
CARD_SET_DIR: Final[Path] = PROJECT_ROOT_DIR / "card_sets"

def snake_to_title(snake_case_string):
    """Converts a snake_case string to a Title Case string."""
    words = snake_case_string.split('_')
    return ' '.join(word.capitalize() for word in words)
