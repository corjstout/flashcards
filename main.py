
from pathlib import Path
from typing import Final, List
import sys

from src.menu import MainMenu
from src.flashcards import CardGame
from src.common import CACHE_FILE
from src.cache import retrieve_card_set_dir

def main(argv: List[str]) -> int:
	card_set_dir = retrieve_card_set_dir()
	main_menu = MainMenu(card_set_dir)
	if main_menu.selected_card_sets:
		card_game = CardGame(main_menu.selected_card_sets)
		card_game.play()

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
