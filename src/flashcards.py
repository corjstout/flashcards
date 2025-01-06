#!/usr/bin/python3

import pygame
import sys
import json
import random
from pathlib import Path
from typing import Final

from src.common import snake_to_title

BG_COLOR: Final = "#0a092d"
FLASHCARD_COLOR: Final = "#2e3856"
FLIPPED_COLOR: Final = "#595e6d"
TEXT_COLOR: Final = "white"
FONT_PACKAGE: Final = "STHeiti Medium"

class CardGame:
    def __init__(self, card_set: Path):
        self.card_turned = False
        self.index = 0
        self.quit_requested = False
        pygame.init()
        pygame.display.set_caption(snake_to_title(card_set.stem))
        self.font = pygame.font.SysFont(FONT_PACKAGE, 30)
        self.screen = pygame.display.set_mode((800, 800))
        self.screen.fill(BG_COLOR)

        with open(card_set, encoding='utf-8') as file:
            unshuffled_demo_quiz_data = json.load(file)
        keys = list(unshuffled_demo_quiz_data.keys())
        random.shuffle(keys)
        self.demo_quiz_data = {key: unshuffled_demo_quiz_data[key] for key in keys}

    def blit_text(self, text: str, height: int):
        text_object = self.font.render(text, True, TEXT_COLOR)
        text_rect = text_object.get_rect(center=(400, height))
        self.screen.blit(text_object, text_rect)

    def get_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.card_turned = not self.card_turned
                elif pygame.key.get_pressed()[pygame.K_RIGHT] and self.index < len(self.demo_quiz_data) - 1:
                    self.index += 1
                    self.card_turned = False
                elif pygame.key.get_pressed()[pygame.K_LEFT] and self.index > 0:
                    self.index -= 1
                    self.card_turned = False
                elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    self.quit_requested = True

    def play(self):
        while not self.quit_requested:
            # Get any user keypresses
            self.get_user_input()

            # Generate text strings
            progress_text = f"{self.index+1}/{len(self.demo_quiz_data)}"
            if not self.card_turned:
                card_text = list(self.demo_quiz_data)[self.index]
            else:
                card_text = list(self.demo_quiz_data.values())[self.index]
            
            # Render the card and its text strings
            self.screen.fill(BG_COLOR)
            pygame.draw.rect(self.screen, FLASHCARD_COLOR, (150, 250, 500, 300))
            self.blit_text(text=card_text, height=400)
            self.blit_text(text=progress_text, height=600)
            pygame.display.update()

        # Quit the game if requested
        pygame.quit()

def main():
    card_set = Path("/Users/cstout16/OneDrive/Education/chinese/flashcards/card_sets/cantonese_general.json")
    game = CardGame(card_set)
    game.play()

if __name__ == "__main__":
    main()