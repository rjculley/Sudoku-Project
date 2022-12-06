import pygame
from cell import Cell
from sudoku_generator import generate_sudoku
#This class represents an entire Sudoku board. A Board object has 81 Cell objects.
class Board:

    def __init__(self, rows, cols, width, height, screen, difficulty):
        if difficulty == "easy":
            self.board = generate_sudoku(9, 30) #clears 30 sqaures
        elif difficulty == "medium":
            self.board = generate_sudoku(9, 40) #clears 40 squares
        else:
            self.board = generate_sudoku(9, 50) #clears 50 squares (hard)

        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(self.board[i][j], i, j, width, height)
                       for j in range(cols)] for i in range(rows)]
        self.selected = None
        self.board_reset = self.board.copy() # makes a copy of the original board to be used when board is reset


    def draw(self):
        # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        # Draws every cell on this board.
        # https://stackoverflow.com/questions/73587924/creating-a-bold-line-in-pygame
        gap = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * gap),
                             (self.width, i * gap), thick)
            pygame.draw.line(self.screen, (0, 0, 0), (i * gap, 0),
                             (i * gap, self.height), thick)

        # draw cell and text in cells
        # v2
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(self.screen)




    def select(self, row, col):
        #Marks the cell at (row, col) in the board as the current selected cell.
        # reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].selected = False

        self.cells[row][col].selected = True
        self.selected = (row, col)


    def click(self, pos):
        #If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
        # of the cell which was clicked. Otherwise, this function returns None.
        if pos[0] < self.width and pos[1] < self.height:
            space = self.width / 9
            row = int(pos[1] // space)
            col = int(pos[0] // space)
            return (row, col)
        else:
            return None



    def clear(self):
        row, col = self.selected
        if self.board_reset[row][col] == 0:
            self.cells[row][col].set_temp(0)
            self.cells[row][col].set(0)
        #Clears  the  value  cell.  Note  that  the  user  can  only  remove  the  cell  values  and  sketched  value  that  are filled by themselves.


    def sketch(self, value):
        #Sets the sketched value of the current selected cell equal to user entered value.
        #It will be displayed at the top left corner of the cell using the draw() function.
        row, col = self.selected
        self.cells[row][col].set_temp(value)

    def place_number(self, value):
        #Sets the value of the current selected cell equal to user entered value.
        # Called when the user presses the Enter key.
        row, col = self.selected

        if self.cells[row][col].value == 0:
            self.cells[row][col].set(value)
            self.update_board()

            if self.check_board(self.board, value, (row, col)) and self.solve():
                return True
            else:
                self.cells[row][col].set(0)
                self.cells[row][col].set_temp(0)
                self.update_board()
                return False

    def reset_to_original(self):
        #Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
        for i in range(self.rows):
            for j in range(self.cols):
                self.board[i][j] = self.board_reset[i][j]

        self.cells = [[Cell(self.board[i][j], i, j, screen)
                       for j in range(self.cols)] for i in range(self.rows)]

    def is_full(self):
        #Returns a Boolean value indicating whether the board is full or not.
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def update_board(self):
        #Updates the underlying 2D board with the values in all cells.
        self.board = [[self.cells[i][j].value for j in range(self.cols)]
                      for i in range(self.rows)]

    def find_empty(self):
        #Finds an empty cell and returns its row and col as a tuple (x, y).
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    return (row, col)

        return False

    def check_board():
        #Check whether the Sudoku board is solved correctly.
        #https://python.plainenglish.io/solve-a-sudoku-puzzle-using-backtracking-in-python-8e9eb58e57e6
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.valid(self.model, i, (row, col)):
                self.model[row][col] = i

                if self.solve():
                    return True
                self.model[row][col] = 0
        return False






