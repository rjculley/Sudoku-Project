import pygame
import sys
from board import Board
import button


# Initialize pygame
pygame.init()
pygame.font.init()

#create game window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#game variables
menu_state = "main"
difficulty = "easy"

# Display title and window screen
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku Game")

# Set a sudoku icon
img = pygame.image.load("images/icon.png")
pygame.display.set_icon(img)

# Set a background image for screen
background_img = pygame.image.load("images/start_screen.png")
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))


# def startScreen():
#     surface.blit(background_img, (0, 0))
#     mouse_pos = pygame.mouse.get_pos()
#     # Set font and position for the welcome text
#     font = pygame.font.SysFont("arial", 70)
#     text = font.render("Welcome to Sudoku", 1, (255, 255, 255))
#     text_rect = text.get_rect(center=(600//2, 110))
#     # Set font and position for the select game mode text
#     font2 = pygame.font.SysFont("arial", 60)
#     text2 = font2.render("Select Game Mode:", 1, (255, 255, 255))
#     text2_rect = text2.get_rect(center=(600 // 2, 200))
#     # Display diff buttons
#     easy_btn = pygame.transform.smoothscale(easy_img, (100, 50))
#     easy_btn_rect = easy_btn.get_rect(center=(600//2, 275))
#     med_btn = pygame.transform.smoothscale(medium_img, (100, 50))
#     med_btn_rect = med_btn.get_rect(center=(600 // 2, 350))
#     hard_btn = pygame.transform.smoothscale(hard_img, (100, 50))
#     hard_btn_rect = hard_btn.get_rect(center=(600 // 2, 425))
#
#     surface.blit(text, text_rect)
#     surface.blit(text2, text2_rect)
#     surface.blit(easy_btn, easy_btn_rect)
#     surface.blit(med_btn, med_btn_rect)
#     surface.blit(hard_btn, hard_btn_rect)
#
#     pygame.display.update()


def start_screen(screen, easy_button, medium_button, hard_button, background_img):
    global difficulty
    global menu_state

    #set font for menu text
    font = pygame.font.SysFont("arial", 75)
    text = font.render("Let's play Sudoku!", 1, (0, 0, 0))
    text2 = font.render("Select Game difficulty:", 1, (0, 0, 0))

    #set background image for this screen
    screen.blit(background_img, (0, 0))

    screen.blit(text, (25, 100))
    screen.blit(text2, (70, 275))
    pygame.display.update()
    #wait 500 milliseconds
    pygame.time.wait(500)

    while True:
        # This is needed to check for a key press and to not brick the game
        key_pressed = check_key_press()
        # Render the buttons and move to next screen if clicked
        if easy_button.draw(screen):
            print('EASY')
            difficulty = "easy"
            pygame.display.update()
            menu_state = "board"
            return

        if medium_button.draw(screen):
            print('MEDIUM')
            difficulty = "medium"
            pygame.display.update()
            menu_state = "board"
            return

        if hard_button.draw(screen):
            print('HARD')
            difficulty = "hard"
            pygame.display.update()
            menu_state = "board"
            return

        pygame.display.update()


def game_over_screen(screen, restart_button_2, background_img):
    global menu_state
    #set font for screen text
    font = pygame.font.SysFont("arial", 100)

    text = font.render("Game Over! Try again?", 1, (0, 0, 0))
    screen.blit(background_img, (0, 0))
    screen.blit(text, (50, 150))
    pygame.display.update()
    pygame.time.wait(500)

    while True:
        key_pressed = check_key_press()
        if restart_button.draw(screen):
            menu_state = "start"
            print('RESTART')
            pygame.display.update()
            return
        pygame.display.update()

def game_won_screen(screen, exit_button_2, background_img):
    global menu_state
    fnt = pygame.font.SysFont("arial", 100)
    text = fnt.render("SUDOKU NINJA! YOU WIN!", 1, (0, 0, 0))
    screen.blit(background_img, (0, 0))
    screen.blit(text, (70, 150))
    pygame.display.update()
    pygame.time.wait(500)

    while True:
        key_pressed = check_key_press()
        if exit_button_2.draw(screen):
            screen = "start"
            print('EXIT')
            pygame.display.update()
            return
        pygame.display.update()
    pass

def check_key_press(): # source- https://inventwithpython.com/chapter18.html
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

def terminate(): # method to terminate game
    pygame.quit()
    sys.exit()

def game_on(screen, reset_button, exit_button, restart_button, background_img):
    global menu_state
    board = Board(9, 9, 540, 540, screen, difficulty)
    playing = True
    key = None
    start = time.time()
    strikes = 0
    while playing:
        play_time = round(time.time() - start)

        #source for pygame.events https://www.geeksforgeeks.org/building-and-visualizing-sudoku-game-using-pygame/
        for event in pygame.event.get():
            # If the exit button gets pressed
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                elif event.key == pygame.K_2:
                    key = 2
                elif event.key == pygame.K_3:
                    key = 3
                elif event.key == pygame.K_4:
                    key = 4
                elif event.key == pygame.K_5:
                    key = 5
                elif event.key == pygame.K_6:
                    key = 6
                elif event.key == pygame.K_7:
                    key = 7
                elif event.key == pygame.K_8:
                    key = 8
                elif event.key == pygame.K_9:
                    key = 9

                if event.key == pygame.K_LEFT:
                    row, col = board.selected
                    if col > 0:
                        col -= 1
                        board.select(row, col)
                elif event.key == pygame.K_RIGHT:
                    row, col = board.selected
                    if col < board.cols - 1:
                        col += 1
                        board.select(row, col)
                elif event.key == pygame.K_UP:
                    row, col = board.selected
                    if row > 0:
                        row -= 1
                        board.select(row, col)
                elif event.key == pygame.K_DOWN:
                    row, col = board.selected
                    if row < board.rows - 1:
                        row += 1
                        board.select(row, col)

                if event.key == pygame.K_BACKSPACE:
                    board.clear()
                    key = None

                if event.key == pygame.K_RETURN:
                    select = board.selected
                    if select:
                        row, col = select
                        if board.cells[row][col].temp != 0:
                            if board.place(board.cells[row][col].temp):
                                print("Success!")
                            else:
                                print("Wrong")
                                strikes += 1
                            key = None

                            if board.is_finished():
                                screen = "won"
                                print("Game Over! YOU WON!")
                                return
            if reset_button.draw(screen):
                print('RESET BOARD 1')
                strikes = 0
                board.reset_to_original()
                pygame.display.update()
            if restart_button.draw(screen):
                print('RESTART GAME')
                screen = "start"
                pygame.display.update()
                return

        if board.selected and key:
            board.sketch(key)
            key = None

        redraw_window(screen, board, play_time, strikes,
                      restart_button_2, background_img)
        # If menu state is reset to start screen
        if menu_state == "start":
            return
        if reset_button.draw(screen):
            print("Reset board 2")
            strikes = 0
            board.reset_to_original()
            pygame.display.update()
        restart_button.draw(screen)

        if exit_button.draw(screen):
            pygame.display.update()
            playing = False
            pygame.quit()
            sys.exit()
        pygame.display.update()


def main(): # source - https://github.com/russs123/pygame_tutorials/blob/main/Menu/main.py
    #initialize pygame
    pygame.init()

    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # load button images
    # Set difficultness buttons
    #https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert
    """Creates a new copy of the surface with the desired pixel format. 
    The new surface will be in a format suited for quick blitting to the given format with per pixel alpha. 
    If no surface is given, the new surface will be optimized for blitting to the current display."""

    easy_img = pygame.image.load("images/easy.png").convert_alpha()
    medium_img = pygame.image.load("images/medium.png").convert_alpha()
    hard_img = pygame.image.load("images/hard.png").convert_alpha()
    exit_img = pygame.image.load('images/exit.png').convert_alpha()
    restart_img = pygame.image.load('images/restart.png').convert_alpha()
    reset_img = pygame.image.load('images/reset.png').convert_alpha()
    background_img = pygame.image.load('images/start_screen.png').convert_alpha()
    background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # create button instances
    easy_button = button.Button(304, 125, easy_img, 1)
    medium_button = button.Button(297, 250, medium_img, 1)
    hard_button = button.Button(336, 375, hard_img, 1)
    exit_button = button.Button(226, 75, exit_img, 1)
    restart_button = button.Button(225, 200, restart_img, 1)
    reset_button = button.Button(246, 325, reset_img, 1)

    pygame.display.set_caption('Sudoku')

    start_screen(screen, easy_button, medium_button, hard_button, background_img)
    while menu_state != "start":
        game_on(screen, reset_button, exit_button, restart_button, background_img)
        # This is for when the user clicks 'reset' from the board screen
        if (menu_state == "start"):
            showStartScreen(screen, easy_button, medium_button,
                            hard_button, background_img)
        elif (menu_state == "won"):
            showGameWonScreen(screen, exit_button, background_img)
        else:
            showGameOverScreen(screen, restart_button, background_img)


main()



