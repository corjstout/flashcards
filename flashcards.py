import pygame
import sys
import json
import random

pygame.init()

SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Quiz App")

BG_COLOUR = "#0a092d"
FLASHCARD_COLOUR = "#2e3856"
FLIPPED_COLOUR = "#595e6d"
FONT = pygame.font.SysFont("STHeiti Medium", 30)
SCREEN.fill(BG_COLOUR)

with open("card_set_general.json") as file:
    demo_quiz_data = json.load(file)
keys = list(demo_quiz_data.keys())
random.shuffle(keys)
demo_quiz_data = {key: demo_quiz_data[key] for key in keys}

card_turned = False
index = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                card_turned = not card_turned
            elif pygame.key.get_pressed()[pygame.K_RIGHT] and index < len(demo_quiz_data) - 1:
                index += 1
                card_turned = False
            elif pygame.key.get_pressed()[pygame.K_LEFT] and index > 0:
                index -= 1
                card_turned = False
    
    SCREEN.fill(BG_COLOUR)
    pygame.draw.rect(SCREEN, FLASHCARD_COLOUR, (150, 250, 500, 300))

    if not card_turned:
        current_question = list(demo_quiz_data)[index]
        current_question_object = FONT.render(current_question, True, "white")
        current_question_rect = current_question_object.get_rect(center=(400, 400))
        SCREEN.blit(current_question_object, current_question_rect)
    else:
        current_answer = list(demo_quiz_data.values())[index]
        current_answer_object = FONT.render(current_answer, True, "white")
        current_answer_rect = current_answer_object.get_rect(center=(400, 400))
        SCREEN.blit(current_answer_object, current_answer_rect)
    
    current_index_object = FONT.render(f"{index+1}/{len(demo_quiz_data)}", True, "white")
    current_index_rect = current_index_object.get_rect(center=(400, 600))
    SCREEN.blit(current_index_object, current_index_rect)
    
    pygame.display.update()