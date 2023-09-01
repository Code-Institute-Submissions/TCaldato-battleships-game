import random #Built-in module to make random numbers.

class Board:
    """
    Main Board class that is reponsible for managing the game board
    """
    def __init__(self, size):
        self.size = size
        self.grid = [['*'] * size for s in range(size)]

    def display(self):
        for row in self.grid:
            print(" ".join(row))

    def is_valid(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size
    
    def mark_guess(self, row, col, mark):
        self.grid[row][col] = mark


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


class ComputerBoard(Board):
    """
    Class for managing the computer's board, including the user's ship display
    """
    def __init__(self, size, battleship=None, user_battleship=None):
        super().__init__(size)
        self.user_battleship = user_battleship
        if battleship:
            self.battleship = battleship
            self.grid[self.battleship.row][self.battleship.col] = '@'


    def mark_guess(self, row, col, mark):
        self.grid[row][col] = mark

class Game:
    """
    Class responsible for managing the game flow and player interaction
    """
    def __init__(self, board_size):
        self.user_board = Board(board_size)
        self.user_battleship = Battleship(board_size)
        self.user_attempts = 1
        self.user_prev_attempt = None # Variable to store the previous user's attempts
        
        # Create a battleship object for the computer
        computer_battleship = Battleship(board_size)
        self.computer_board = ComputerBoard(board_size, computer_battleship)
        self.computer_battleship = computer_battleship
        

    def unique_random_guess(self):
        """"
        Function responsible for creating an unique random guess for the computer.
        """
        while True:
            guess_row = random.randint(0, self.computer_board.size - 1)
            guess_col = random.randint(0, self.computer_board.size - 1)
            if self.computer_board.grid[guess_row][guess_col] == '*': 
                return guess_row, guess_col
            
    
    def play(self):
        """
        Function responsible for interaction with user and computer
        """
        while True:
            # User's turn
            print("\nYour turn! You have 5 Guesses: Attempt", self.user_attempts)
            self.user_board.display()
            guess_row = int(input("Guess a Row: "))
            guess_col = int(input("Guess a Column: "))

            # Check if the current attempt is the same as the previous attempt
            if self.user_prev_attempt == (guess_row, guess_col):
                print("Same Attempt as Before, Try Again:")
                continue  # Skip the rest of the loop and ask for a new attempt

            self.user_prev_attempt = (guess_row, guess_col)  # Store the current attempt
            self.user_attempts += 1       
            
            # Validate user's guess
            if not self.user_board.is_valid(guess_row, guess_col):
                print("Oops, Values must be between 0 and 4!")
            else:
                result = self.user_battleship.check_guess(guess_row, guess_col)
                # Process user's guess
                if result == "hit":
                    print("Congratulations! You sunk my battleship!")
                    self.user_board.mark_guess(guess_row, guess_col, 'X')
                    self.restart_game()
                    return
                else:
                    print("You missed my battleship!")
                    self.user_board.mark_guess(guess_row, guess_col, 'O')
                
                if self.user_attempts >= 6:
                    print("Game Over! You've used all your attempts.")
                    print("The battleship was located at row", self.user_battleship.row, "and column", self.user_battleship.col)
                    self.restart_game()
                    return

                print("\nComputer's turn")
                guess_row, guess_col = self.unique_random_guess()
                result = self.computer_battleship.check_guess(guess_row, guess_col)
                self.computer_board.mark_guess(guess_row, guess_col, 'X')

                self.computer_board.display()  # Display the computer's board
                # Process computer's guess and update computer's board
                
                if result == "hit":
                    print("Oh no! The computer hit your battleship!")
                    self.restart_game()
                    return
                else:
                    print("Phew! The computer missed your battleship!")
                    self.computer_board.mark_guess(guess_row, guess_col, 'X')  
                    # Mark the guess on the computer's board


    def display_user_ship(self):
        """
        This Function display the location of the user's ship on the computer's board
        """
        print("\nYour ship's location on Computer's Board:")
        self.computer_board.grid[self.computer_battleship.row][self.computer_battleship.col] = 'S'  # Mark the user's ship
        self.computer_board.display()  # Display the user's board


    def restart_game(self):
        """
        Restart the game when Computer or User ship sink or when user 
        has used up all their attempts.
        """
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == 'yes':
            main()
        else:
            print("Thank you for playing! Goodbye!")
            exit()

                    
def main():
    """
    Main function to start the game
    """
    print("\nWelcome to Battleship Game")
    print("In this game you have 5 attempts to try sink computer's ship")
    print("Do you think you can do it???")
    print("Let's play!!!")
    board_size = 5
    game = Game(board_size)
    game.display_user_ship()
    game.play()

# Main function to start the game
main()