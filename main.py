
from pathlib import Path
from typing import Final, List
import sys

from src.menu import MainMenu
from src.flashcards import CardGame
from src.common import CARD_SET_DIR

def main(argv: List[str]) -> int:
	main_menu = MainMenu(CARD_SET_DIR)
	if main_menu.selected_card_sets:
		card_game = CardGame(main_menu.selected_card_sets)
		card_game.play()

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
