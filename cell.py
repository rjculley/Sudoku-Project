

class Cell:
    #consturctor to make the board 9x9
    rows = 9
    cols = 9

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

    def draw(self):
        pass




