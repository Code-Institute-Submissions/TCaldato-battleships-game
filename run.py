import random
#Built-in module to make random numbers.

class Board:
    """
    Main Board class that is reponsible for managing the game board
    """
    def __init__(self, size):
        self.size = size
        self.grid = [['*'] * size for _ in range(size)]

    def display(self):
        for row in self.grid:
            print(" ".join(row))

    def is_valid(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size

    
class Battleship:
    """
    Class responsible for managing the battleship's location and checking 
    guesses
    """
    def __init__(self, board_size):
        self.row = random.randint(0, board_size - 1)
        self.col = random.randint(0, board_size - 1)

    def check_guess(self, guess_row, guess_col):
        """
        Function to check if the guess hit or missed the ship
        """
        if guess_row == self.row and guess_col == self.col:
            return "hit"
        else:
            return "miss"


class Game:
    """
    Class responsible for managing the game flow and player interaction
    """
    def __init__(self, board_size):
        self.board = Board(board_size)
        self.battleship = Battleship(board_size)
        self.attempts = 1
        
    def play(self):
        while True:
            print("\nYou have 5 Guesses: Attempt", self.attempts)
            self.board.display()

            guess_row = int(input("Guess a Row: "))
            guess_col = int(input("Guess a Column: "))
            
            if not self.board.is_valid(guess_row, guess_col):
                print("Oops, Values must be between 0 and 4!")
            else:
                self.attempts += 1
                result = self.battleship.check_guess(guess_row, guess_col)
                
                if result == "hit":
                    print("Congratulations! You sunk my battleship!")
                    break
                else:
                    print("You missed my battleship!")
                    self.board.grid[guess_row][guess_col] = 'X'
                
                if self.attempts >= 6:
                    print("Game Over! You've used all your attempts.")
                    print("The battleship was located at row", self.battleship.row, "and column", self.battleship.col)
                    break
                    
def main():
    board_size = 5
    game = Game(board_size)
    game.play()

# Call the main function to start the game
main()