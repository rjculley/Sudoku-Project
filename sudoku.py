import pygame
import sys
from board import Board


# Initialize pygame
pygame.init()
pygame.font.init()
# Display title and window screen
pygame.display.set_caption("Sudoku Game")
screen = pygame.display.set_mode((600, 600))
# Set a sudoku icon
img = pygame.image.load("images/icon.png")
pygame.display.set_icon(img)
# Set a background image for screen
background_img = pygame.image.load("images/start_screen.png")
background_img = pygame.transform.scale(background_img, (600, 600))
# Set difficultness buttons
easy_img = pygame.image.load("images/easy.png")
medium_img = pygame.image.load("images/medium.png")
hard_img = pygame.image.load("images/hard.png")

def startScreen():
    screen.blit(background_img, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    # Set font and position for the welcome text
    font = pygame.font.Font(None, 70)
    text = font.render("Welcome to Sudoku", 1, (255, 255, 255))
    text_rect = text.get_rect(center=(600//2, 110))
    # Set font and position for the select game mode text
    font2 = pygame.font.Font(None, 60)
    text2 = font2.render("Select Game Mode:", 1, (255, 255, 255))
    text2_rect = text2.get_rect(center=(600 // 2, 200))
    # Display diff buttons
    easy_btn = pygame.transform.smoothscale(easy_img, (100, 50))
    easy_btn_rect = easy_btn.get_rect(center=(600//2, 275))
    med_btn = pygame.transform.smoothscale(medium_img, (100, 50))
    med_btn_rect = med_btn.get_rect(center=(600 // 2, 350))
    hard_btn = pygame.transform.smoothscale(hard_img, (100, 50))
    hard_btn_rect = hard_btn.get_rect(center=(600 // 2, 425))

    screen.blit(text, text_rect)
    screen.blit(text2, text2_rect)
    screen.blit(easy_btn, easy_btn_rect)
    screen.blit(med_btn, med_btn_rect)
    screen.blit(hard_btn, hard_btn_rect)

    pygame.display.update()
"""
    while True:
        key_press = check_key_press()
        if easy_btn.draw(screen):
            difficulty = "easy"
            pygame.display.update()
            return
        elif med_btn.board.draw(screen):
            difficulty = "medium"
            pygame.display.update()
        elif hard_btn.board.draw(screen):
            difficulty = "hard"
            pygame.display.update()
"""
def gameOverScreen():
    pass

def gameWonScreen():
    pass

# This code source is taken from https://github.com/dhruv2000/temp-Sudoku/blob/main/main.py
def check_key_press():
    if len(pygame.event.get(pygame.QUIT)) > 0:
        pygame.quit()
        sys.exit()

    keyUpEvents = pygame.event.get(pygame.KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
    return keyUpEvents[0].key

while True:
    startScreen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


