import pygame

class Cell:
    #consturctor to make the board 9x9
    rows = 9
    cols = 9

    COLOR_GRAY = (128, 128, 128)
    COLOR_BLACK = (0, 0, 0)
    COLOR_RED = (255, 0, 0)
    COLOR_WHITE = (255, 255, 255)

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.sketch = 0
        self.selected = False

    def draw(self, screen):
        # https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.sketch != 0 and self.value == 0:
            text = fnt.render(str(self.sketch), 1, (128, 128, 128))
            screen.blit(text, (x + 5, y + 5))
        elif not (self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            screen.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        if self.selected:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, gap, gap), 3)

    def set_cell_value(self, value):  #Setter for this cell’s value
        self.value = value

    def set_sketched_value(self, value):
        self.sketch = value







