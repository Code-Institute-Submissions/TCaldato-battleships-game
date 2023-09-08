# Libraries
import random  # Built-in module to make random numbers.
import sys  # credit to pylint.readthedocs.io

# Constants
USER_SHIP = "U"
COMP_SHIP = "C"
HIT = "X"
MISS = "O"
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

    def mark_missed(self, row, col):
        """
        Mark the grid cell with 'X' mark
        """
        self.grid[row - 1][col - 1] = MISS

    def display_grid(self):
        """
        Display the grid with row and column numbering
        """
        print("    " + " ".join(str(i + 1) for i in range(self.size)))
        # This line is credited to
        # https://realpython.com/python-enumerate/
        for i, row in enumerate(self.grid):
            print(str(i + 1) + " | " + " ".join(row))

 
class UserBoard(Board):
    """
    Class representing the user's board
    """
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



class ComputerBoard(Board):
    """
    Class representing the computer's board
    """
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



class Game:
    """
    Class responsible for managing the game flow and player interaction
    """
    def __init__(self, size):
        self.user_board = UserBoard(size)
        self.comp_board = ComputerBoard(size)
        self.user_board.place_ships()
        self.comp_board.place_ships()
        self.user_prev_attempt = [] # List to store user's attempts

        self.user_hits = 0  # Initialize user hits
        self.comp_hits = 0  # Initialize computer hits

    def play(self, user_name):
        """
        Function responsible for interaction with user and computer
        """
        while True:
            self.display_game_boards(user_name)

            user_row, user_col = self.get_user_input()
            if not self.is_valid_user_input(user_row, user_col):
                print(f"Row and column must be within the range 1 to {self.user_board.size}. Try again.")
                continue

            if self.is_duplicate_attempt(user_row, user_col):
                print("----------------------------------------------")
                print("You've already made this attempt. Try again.")
                print("----------------------------------------------")
                continue

            self.user_prev_attempt.append((user_row, user_col))

            self.user_turn(user_row, user_col, user_name)

            if self.check_game_over(user_name):
                self.restart_game()

    def display_game_boards(self, user_name):
        print(f"\nCaptain {user_name} try to HIT the Computer's SHIP on the computer board:")
        self.comp_board.display_grid()
        print(f"\nComputer try to HIT {user_name}'s SHIP on the user board :")
        self.user_board.display_grid()

    def get_user_input(self):
        while True:
            try:
                user_row = int(input(f"\nEnter row (1 to {self.user_board.size}): "))
                user_col = int(input(f"Enter column (1 to {self.user_board.size}): "))
                return user_row, user_col
            except ValueError:
                print(f"It is not a number between 1 to {self.user_board.size}, try again.")

    def is_valid_user_input(self, row, col):
        return 1 <= row <= self.user_board.size and 1 <= col <= self.user_board.size

    def is_duplicate_attempt(self, row, col):
        return (row, col) in self.user_prev_attempt

    def user_turn(self, user_row, user_col, user_name):
        if self.comp_board.grid[user_row - 1][user_col - 1] == COMP_SHIP:
            print(f"\nCaptain {user_name} hit a computer ship!")
            self.comp_board.mark_hit(user_row, user_col)
            self.user_hits += 1  # Increment user hits
        else:
            print(f"\nCaptain {user_name} missed.")
            self.comp_board.mark_missed(user_row, user_col)

        self.computer_turn(user_name)

    def computer_turn(self, user_name):
        comp_row = random.randint(1, self.user_board.size)
        comp_col = random.randint(1, self.user_board.size)
        if self.user_board.grid[comp_row - 1][comp_col - 1] == USER_SHIP:
            print(f"Computer hit {user_name}'s ship!")
            self.user_board.mark_hit(comp_row, comp_col)
            self.comp_hits += 1  # Increment computer hits
        else:
            print("Computer missed.")

        self.display_scoreboard(user_name)

    def display_scoreboard(self, user_name):
        print("\n----------------------------------------------------")
        print(f"                  {user_name} Hits: {self.user_hits}")
        print(f"                 Computer Hits: {self.comp_hits}")
        print("----------------------------------------------------")

    def check_game_over(self, user_name):
        if self.user_hits == 5:
            print(f"\nCongratulations {user_name}! You sank 5 of the computer's ships. You win!")
            return True
        if self.comp_hits == 5:
            print(f"\nGame Over! The computer sank 5 of your ships. Sorry {user_name}, You lose!")
            return True
        return False

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
            # This line is credited to
            # https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-sys-exit.html
            sys.exit(0)

# Main program


def main():
    """
    Main Function that starts the game and give the game rules
    """
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
        # This line is credited to
        # https://bobbyhadz.com/blog/python-input-only-accept-one-character#:~:text=To%20only%20allow%20letters%20when,the%20user%20entered%20only%20letters.
        if user_name.isalpha() and 3 <= len(user_name) <= 15:
            break
        else:
            print("Are you sure this is your name Captain?")
            print("Please enter a name that contains LETTERS between 3 to 15 characters.")

    print("\nNow you have to choose the size of the grid to play the game.")
    print("The size of the grid will determine the amount of the ships")
    print("The amount will be 2X the grid, e.g., Grid size 5 will display 10 ships on both boards")
    print("So if you increase the grid size the game will become more difficult!!!")
    print("\nLets start???")

    while True:
        try:
            size = int(input(
                f"\nChoose the Size of the grid, it must be between {GRID_SIZE_MIN} to {GRID_SIZE_MAX} (e.g., 5 for a 5x5 grid): "))
            if GRID_SIZE_MIN <= size <= GRID_SIZE_MAX:
                break
            else:
                print("Grid size must be between 5 and 9. Please try again.")
        except ValueError:
            print("It is not a number, try again.")

    print("\n------------------ Let's play!!! ------------------")

    game = Game(size)
    game.play(user_name)


# Sugested while searching for better practices on internet and implemented
# This line is credited to
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    main()
