
from pathlib import Path
from typing import Final, List
import sys

from src.menu import MainMenu
from src.flashcards import CardGame


PROJECT_ROOT_DIR: Path = Path(__file__).resolve().parent
DEFAULT_CARD_SET_DIR: Final = PROJECT_ROOT_DIR / "card_sets"


def main(argv: List[str]) -> int:
	main_menu = MainMenu(DEFAULT_CARD_SET_DIR)
	if main_menu.value:
		card_game = CardGame(main_menu.value)
		card_game.play()

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
