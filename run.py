import random 
#Built-in module to make random numbers.

# Constants
USER_SHIP = "U"
COMP_SHIP = "C"
HIT = "X"
GRID_SIZE_MIN = 5
GRID_SIZE_MAX = 9


class Board:
    """
    Main Board class that is reponsible for managing the game board
    """
    def __init__(self, size):
        self.size = size
        self.grid = [['*'] * size for _ in range(size)]

    def mark_hit(self, row, col):
        """
        Mark the grid cell with 'X' mark
        """
        self.grid[row - 1][col - 1] = HIT

    def display_grid(self):
        """
        Display the grid with row and column numbering
        """
        print("    " + " ".join(str(i + 1) for i in range(self.size)))
        for i, row in enumerate(self.grid):
            print(str(i + 1) + " | " + " ".join(row))


# Class representing the user's board
class UserBoard(Board):
    def __init__(self, size):
        super().__init__(size)
        self.num_ships = size * 2

    def place_ships(self):
        for _ in range(self.num_ships):
            while True:
                row = random.randint(1, self.size)
                col = random.randint(1, self.size)
                if self.grid[row - 1][col - 1] == '*':
                    self.grid[row - 1][col - 1] = USER_SHIP
                    break

# Class representing the computer's board
class ComputerBoard(Board):
    def __init__(self, size):
        super().__init__(size)
        self.num_ships = size * 2

    def place_ships(self):
        for _ in range(self.num_ships):
            while True:
                row = random.randint(1, self.size)
                col = random.randint(1, self.size)
                if self.grid[row - 1][col - 1] == '*':
                    self.grid[row - 1][col - 1] = COMP_SHIP
                    break

# Class to manage the game
class Game:
    def __init__(self, size):
        self.user_board = UserBoard(size)
        self.comp_board = ComputerBoard(size)
        self.user_board.place_ships()
        self.comp_board.place_ships()

        self.user_hits = 0  # Initialize user hits
        self.comp_hits = 0  # Initialize computer hits

    def play(self, user_name):
        while True:
            print(f"\nCaptain {user_name} try to HIT the Computer's SHIP on the computer board:")
            self.comp_board.display_grid()
            print(f"\nComputer try to HIT {user_name}'s SHIP on the user board :")
            self.user_board.display_grid()

            while True:
                try:
                    user_row = int(input(f"Enter row (1 to {self.user_board.size}): "))
                    user_col = int(input(f"Enter column (1 to {self.user_board.size}): "))
                    if user_row or user_col != int:
                        break
                except ValueError: 
                    print(f"It is not a number between 1 to {self.user_board.size}, try again.")

            if (
                1 <= user_row <= self.user_board.size
                and 1 <= user_col <= self.user_board.size
            ):
                # User's turn
                if self.comp_board.grid[user_row - 1][user_col - 1] == COMP_SHIP:
                    print(f"\nCaptain {user_name} hit a computer ship!")
                    self.comp_board.mark_hit(user_row, user_col)
                    self.user_hits += 1  # Increment user hits
                else:
                    print(f"\n{user_name} missed.")
                    self.comp_board.mark_hit(user_row, user_col)

                # Computer's turn
                comp_row = random.randint(1, self.user_board.size)
                comp_col = random.randint(1, self.user_board.size)
                if self.user_board.grid[comp_row - 1][comp_col - 1] == USER_SHIP:
                    print(f"Computer hit {user_name}'s ship!")
                    self.user_board.mark_hit(comp_row, comp_col)
                    self.comp_hits += 1  # Increment computer hits
                else:
                    print("Computer missed.")
                    self.user_board.mark_hit(comp_row, comp_col)
                
            else:
                print("Invalid input. Row and column must be within range.")

            # Display the scoreboard with current hits
            print("\n----------------------------------------------------")
            print(f"----------------- {user_name} Hits: {self.user_hits}")
            print(f"----------------- Computer Hits: {self.comp_hits}")
            print("----------------------------------------------------")

            # Check for the game end condition
            if self.user_hits == 5:
                print(f"\nCongratulations {user_name}! You sank 5 of computer's ships. You win!")
                self.restart_game()
                return
            elif self.comp_hits == 5:
                print(f"\nGame Over! The computer sank 5 of your ships. Sorry {user_name}You lose!")
                self.restart_game()
                return

    
    def restart_game(self):
        """
        Restart the game when Computer or User ship sink or when user 
        has used up all their attempts.
        """
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == 'yes':
            main()
        else:
            print("Thank you Captain! See you next time")
            exit()

# Main program
def main():
    print("\n-----x------------x----------------*----------------")
    print("\n-x---------- WELCOME TO BATTLESHIP GAME ---------*--")
    print("\n---------*----------------x-------------x-----------")
    print("\nIn this game you are the Captain, and your goal is to sink 5 SHIPS.")
    print("\nIf you are a great Captain and HIT 5 SHIPS FIRST, You WIN the GAME ")
    print("If you are not so Great as a Captain and the COMPUTER HIT 5 of your SHIPS FIRST, You LOSE")
    print("Do you think you can do it???")
    
    while True:
        user_name = input("\nLet's start with your name Captain: ")
    
        # Check if the name consists of only letters and its length is within the desired limit
        if user_name.isalpha() and 1 <= len(user_name) <= 15:
            break
        else:
            print("Are you sure this is your name Captain?")
            print("Please enter a name that contains LETTERS between 1 to 15 characters.") 
            
    print("\nNow you have to choose the size of the grid to play the game.")
    print("The size of the grid will determine the amount of the ships")
    print("The amount will be 2X the grid, e.g., Grid size 5 will display 10 ships on both boards")
    print("So if you increase the grid size the game will become more difficult!!!")
    print("\nLets start???")

    while True:
        try:
            size = int(input(f"\nChoose the Size of the grid, it must be between {GRID_SIZE_MIN} to {GRID_SIZE_MAX} (e.g., 5 for a 5x5 grid): "))
            if GRID_SIZE_MIN <= size <= GRID_SIZE_MAX:
                break
            else:
                print("Grid size must be between 5 and 9. Please try again.")
        except ValueError: 
            print("It is not a number, try again.")
               
    print("\n------------------ Let's play!!! ------------------")

    game = Game(size)
    game.play(user_name)

if __name__ == "__main__":
    main()