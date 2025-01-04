#!/Users/cstout16/Library/CloudStorage/OneDrive-Personal/Education/chinese/flashcards/myenv/bin/python

import tkinter as tk
from tkinter import ttk
from pathlib import Path
import sys

class MainMenu():
    value = None

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Run Flashcards")

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
        self.menu = tk.Listbox(self.root, selectforeground="red")
        for i in range(20):
            self.menu.insert(tk.END, f"Option {i+1}")
            self.menu.itemconfigure(tk.END, background="grey")

        # Add a scrollbar if needed
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.menu.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.menu.yview)


        self.menu.bind('<Double-Button>', self.on_double_click)
        self.root.bind('<Escape>', self.on_escape)

        label.pack(pady=10)
        self.menu.pack()

        # Bind the selection event
        self.menu.bind("<<ListboxSelect>>", self.on_select)

        self.root.mainloop()
        print("tkinter main loop done")

    def on_select(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print(f"Highlighted: {value}")


    def on_double_click(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        self.value = w.get(index)
        print(f"Selected: {self.value}")
        self.root.destroy()


    def on_escape(self, event):
        print(f"Quitting")
        root = event.widget.winfo_toplevel()
        root.destroy()
        # sys.exit()


if __name__ == "__main__":
    menu = MainMenu()
    print("got here")
    print(f"menu.value: {menu.value}")

    
