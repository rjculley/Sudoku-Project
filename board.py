
#This class represents an entire Sudoku board. A Board object has 81 Cell objects.
class Board:

    def __init__(self, width, height, screen, difficulty):
       self.width = width
       self.height = height
       self.screen = screen
       self.difficulty = difficulty

    def draw(self):
        pass
        #Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        #Draws every cell on this board.


    def select(self, row, col):
        pass
        #Marks the cell at (row, col) in the board as the current selected cell.


    def click(self, x, y):
        pass
        #If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
        # of the cell which was clicked. Otherwise, this function returns None.


    def clear(self):
        pass
        #Clears  the  value  cell.  Note  that  the  user  can  only  remove  the  cell  values  and  sketched  value  that  are filled by themselves.


    def sketch(self, value):
        #Sets the sketched value of the current selected cell equal to user entered value.
        #It will be displayed at the top left corner of the cell using the draw() function.
        pass

    def place_number(self, value):
        #Sets the value of the current selected cell equal to user entered value.
        # Called when the user presses the Enter key.
        pass

    def reset_to_original(self):
        pass
        #Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).

    def is_full(self):
        #Returns a Boolean value indicating whether the board is full or not.
        pass

    def update_board(self):
        #Updates the underlying 2D board with the values in all cells.
        pass

    def find_empty(self):
        #Finds an empty cell and returns its row and col as a tuple (x, y).
        pass

    def check_board(self):
        #Check whether the Sudoku board is solved correctly.
        pass






