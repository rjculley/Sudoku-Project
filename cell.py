import pygame

class Cell:
    #consturctor to make the board 9x9
    rows = 9
    cols = 9

    COLOR_GRAY = (128, 128, 128)
    COLOR_BLACK = (0, 0, 0)
    COLOR_RED = (255, 0, 0)
    COLOR_WHITE = (255, 255, 255)

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch = 0

    def set_cell_value(self, value):  #Setter for this cell’s value
        self.value = value

    def set_sketched_value(self, value):
        self.sketch = value

    def draw(self, screen):
        font = pg.font.SysFont('arial', 36)
        space = self.width / 9

        # Calculate drawing position relative to this box in board
        x = self.col * space
        y = self.row * space

        if self.temp != 0 and self.value == 0:
            text = font.render(str(self.temp), 1, self.COLOR_GRAY)
            screen.blit(text, (x + 3, y + 3))  # Draw small number in upper-left corner
        elif self.value != 0:
            text = font.render(str(self.value), 1, self.COLOR_WHITE)
            screen.blit(text, (x + (space / 2 - text.get_width() / 2), y + (space / 2 - text.get_height() / 2)))  # Draw number in the middle

        if self.selected:
            pg.draw.rect(screen, self.COLOR_RED, (x, y, space, space), 3)  # If this box selected, draw red box./

    def set_temp(self, val):
        self.temp = val




