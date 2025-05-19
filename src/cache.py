#!/usr/bin/python3

import json
from pathlib import Path
from tkinter import filedialog
from typing import Final

from src.common import CACHE_FILE

CARD_SET_PATH_KEY: Final[str] = "card_set_path"

def prompt_for_card_set_dir_to_save() -> None:
    """Create a GUI to prompt the user for a directory to load card sets from."""
    cache_dict = {}
    cache_dict[CARD_SET_PATH_KEY] = filedialog.askdirectory() # Opens a dialog box to select a directory
    if not cache_dict[CARD_SET_PATH_KEY] or not Path(cache_dict[CARD_SET_PATH_KEY]).is_dir():
        raise ValueError("please select a directory")

    with open(CACHE_FILE, "w") as file:
        json.dump(cache_dict, file, indent=4)

def retrieve_card_set_dir() -> Path:
    """Prompt the user for a workspace directory if one is not yet set, then
    return that directory.

    :return: Path to a workspace directory.
    """
    if not CACHE_FILE.exists():
        prompt_for_card_set_dir_to_save()
    with open(CACHE_FILE, encoding='utf-8') as file:
        cache_dict = json.load(file)
    return Path(cache_dict.get(CARD_SET_PATH_KEY))
