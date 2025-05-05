#!/opt/homebrew/bin/python3

from pathlib import Path
import sys
import tkinter as tk
from typing import Final, List, Optional

from src.common import CARD_SET_DIR, snake_to_title

MENU_WIDTH_PX: Final[int] = 400
MENU_HEIGHT_PX: Final[int] = 250
PADDING_PX: Final[int] = 10
ROOT_LABEL: Final[str] = "Flashcards"
MENU_LABEL: Final[str] = "Card Sets"

class MainMenu():
    #: Populated with paths to json files in the flashcards/card_sets directory
    card_set_path_list: List[Path] = []
    #: Will be populated with a path to a card set if one is selected
    selection: Optional[Path] = None

    def __init__(self, card_set_directory: Path) -> None:
        """Create, populate, and initiate the UI."""
        self.root = tk.Tk()
        self.root.title(ROOT_LABEL)

        # Use the screen width and height to set the root in the center
        menu_left_px = (self.root.winfo_screenwidth()/2) - (MENU_WIDTH_PX/2)
        menu_top_px = (self.root.winfo_screenheight()/2) - (MENU_HEIGHT_PX/2)
        self.root.geometry('%dx%d+%d+%d' %
            (MENU_WIDTH_PX, MENU_HEIGHT_PX,menu_left_px, menu_top_px))

        # Create the label for the menu
        label = tk.Label(self.root, text=MENU_LABEL)

        # Create and fill the menu
        self.menu = tk.Listbox(self.root)
        self.fill_card_set_list(card_set_directory)
        for card_set_path in self.card_set_path_list:
            self.menu.insert(tk.END, snake_to_title(card_set_path.stem))
            self.menu.itemconfigure(tk.END)
        self.menu.select_set(0)
        self.menu.focus_set()

        # Create a scrollbar
        scrollbar = tk.Scrollbar(self.root)

        # Configure the scrollbar to scroll through the menu
        self.menu.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.menu.yview)

        # Set up key bindings
        self.menu.bind('<Double-Button>', self.on_select)
        self.menu.bind('<Return>', self.on_select)
        self.root.bind('<Escape>', self.on_escape)

        # Assemble the elements in the root via packing
        label.pack(pady=PADDING_PX)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.menu.pack()

        # Start the interactive loop to enable user interface
        self.root.mainloop()

    def fill_card_set_list(self, card_set_directory: Path) -> None:
        """Populate a list of snake case names for each file in the provided directory.

        :param card_set_directory: Path to a directory with card set jsons
        """
        self.card_set_path_list = sorted(card_set_directory.glob("*.json"))

    def on_select(self, event: tk.Event) -> None:
        """Set the value of the menu to the currently selected card set and exit the menu.

        :param event: Object associated with a binding that the user has triggered
        """
        index = int(event.widget.curselection()[0])
        self.selection = self.card_set_path_list[index]
        self.on_escape(event)

    def on_escape(self, event: tk.Event) -> None:
        """Destroy the menu

        :param event: Object associated with a binding that the user has triggered
        """
        self.root.destroy()


if __name__ == "__main__":
    menu = MainMenu(CARD_SET_DIR)
    print(f"menu.value: {menu.selection}")

    
