#!/Users/cstout16/Library/CloudStorage/OneDrive-Personal/Education/chinese/flashcards/myenv/bin/python

import tkinter as tk
from tkinter import ttk
from pathlib import Path
import sys

from src.common import snake_to_title

class MainMenu():
    value = None
    card_set_path_list = []

    def __init__(self, card_set_directory: Path):
        self.root = tk.Tk()
        self.root.title("Flashcards")

        w = 400 # width for the Tk root
        h = 250 # height for the Tk root

        # get screen width and height
        ws = self.root.winfo_screenwidth() # width of the screen
        hs = self.root.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        label = tk.Label(self.root, text = "Card Sets") 

        # Create the Listbox
        self.menu = tk.Listbox(self.root)
        self.fill_card_set_list(card_set_directory)
        for card_set_path in self.card_set_path_list:
            self.menu.insert(tk.END, snake_to_title(card_set_path.stem))
            self.menu.itemconfigure(tk.END)
        self.menu.select_set(0)


        # Add a scrollbar if needed
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.menu.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.menu.yview)


        self.menu.bind('<Double-Button>', self.on_select)
        self.menu.bind('<Return>', self.on_select)
        self.root.bind('<Escape>', self.on_escape)

        label.pack(pady=10)
        self.menu.pack()

        # Bind the selection event
        self.menu.bind("<<ListboxSelect>>", self.on_single_click)

        self.menu.focus_set()
        self.root.mainloop()
        print("tkinter main loop done")

    def fill_card_set_list(self, card_set_directory):
        self.card_set_path_list = sorted(card_set_directory.glob("*.json"))

    def on_single_click(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        value = self.card_set_path_list[index]
        print(f"Highlighted: {value}")


    def on_select(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        self.value = self.card_set_path_list[index]
        print(f"Selected: {self.value}")
        self.root.destroy()


    def on_escape(self, event):
        print(f"Quitting")
        root = event.widget.winfo_toplevel()
        root.destroy()


if __name__ == "__main__":
    menu = MainMenu(Path("/Users/cstout16/OneDrive/Education/chinese/flashcards/card_sets"))
    print("got here")
    print(f"menu.value: {menu.value}")

    
