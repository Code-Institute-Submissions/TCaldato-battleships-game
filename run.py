import random #Built-in module to make random numbers.

class Board:
    """
    Main Board class that is reponsible for managing the game board
    """
    def __init__(self, size):
        self.size = size
        self.grid = [['*'] * size for s in range(size)]

    def display(self):
        print("   " + " ".join(str(i + 1) for i in range(self.size)))
        for i, row in enumerate(self.grid):
            print(str(i + 1) + " | " + " ".join(row))

    def is_valid(self, row, col):
        return 1 <= row <= self.size and 1 <= col <= self.size

    def mark_guess(self, row, col, mark):
        self.grid[row - 1][col - 1] = mark


class Battleship:
    """
    Class responsible for managing the battleship's location and checking 
    guesses
    """
    def __init__(self, board_size):
        self.row = random.randint(1, board_size)
        self.col = random.randint(1, board_size)

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
    def __init__(self, size):
        super().__init__(size)
        self.user_battleship = None
        self.battleships = []

        # Determine the number of battleships based on grid size
        num_battleships = size * 2  # For example, 5x5 grid will have 10 battleships, 6x6 will have 12, and so on.

        # Create and place battleships
        for _ in range(num_battleships):
            battleship = Battleship(size)
            self.battleships.append(battleship)
            self.grid[battleship.row - 1][battleship.col - 1] = '@'

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
        self.computer_board = ComputerBoard(board_size)
        self.computer_battleship = computer_battleship
        

    def unique_random_guess(self):
        """"
        Function responsible for creating an unique random guess for the computer.
        """
        while True:
            guess_row = random.randint(1, self.computer_board.size)
            guess_col = random.randint(1, self.computer_board.size)
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
                print("Oops, Values MUST be between the Grid Size you Chose")
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
    print("\nWelcome to Battleship Game")
    print("In this game, you have 5 attempts to try to sink the computer's ship.")
    print("Do you think you can do it???")
    while True:
        try:
            board_size = int(input("Enter the grid size between 5 to 10 (e.g., 5 for a 5x5 grid): "))
            if 5 <= board_size <= 10:
                break
            else:
                print("Grid size must be between 5 and 10. Please try again.")
        except ValueError: 
            print("It is not a number, try again.")
            
    print("\nLet's play!!!")
    
    game = Game(board_size)
    game.display_user_ship()
    game.play()

if __name__ == "__main__":
    main()