import random
#Built-in module to make random numbers.

class Board:
    """
    Main Board class that is reponsible for managing the game board
    """
    def __init__(self, size):
        self.size = size
        self.grid = [['0'] * size for _ in range(size)]

    def display(self):
        for row in self.grid:
            print(" ".join(row))

    def is_valid(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size
    
class Battelship:
    """
    Class responsible for managing the battleship's location and checking 
    guesses
    """
    def __init__(self, board_size):
        self.row = random.randint(0, board_size - 1)
        