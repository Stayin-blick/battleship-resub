"""
Battleship Game resub
--------------
This is a command-line implementation of the Battleship game. 
The Player takes turns against the computer in guessing the 
positions of ships on the opponents board and try to sink 
their battleships. The player is given the option of changing 
the grid size as well as how many battleships populate 
the grid.
"""

from random import randint

# M represents missed shot
# H represents hit shot
"""
board and ship placement
"""


class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [["."] * size for _ in range(size)]


class ShipBoard(Board):
    def place_ships(self, num_ships):
        for _ in range(num_ships):
            while True:
                random_row = randint(0, self.size - 1)
                random_column = randint(0, self.size - 1)
                if self.grid[random_row][random_column] != "@":
                    self.grid[random_row][random_column] = "@"
                    break


"""
GuessBoard class will keeps track of the user's guesses
initializes the game by creating the user's board, computer's board, hidden board
welcome message and a method to get the player's name
"""


class GuessBoard(Board):
    def __init__(self, size):
        super().__init__(size)
        self.hits = 0

class Game:
    def __init__(self, board_size, num_ships):
        self.board_size = board_size
        self.num_ships = num_ships
        self.user_board = ShipBoard(board_size)
        self.computer_board = ShipBoard(board_size)
        self.hidden_board = GuessBoard(board_size)
        self.player_score = 0
        self.computer_score = 0
        self.round = 0

    def welcome_message(self):
        print("----------------------------------")
        print("Welcome to ULTIMATE BATTLESHIPS!!")
        print("Board Size:", self.board_size, "Number of ships:", self.num_ships)
        print("Top left corner is row: 0, col: 0")
        print("------------------------------------")

    def get_name(self):
        name = input("Please enter your name: ")
        return name

    def get_guess(self):
        while True:
            try:
                user_guess_row = int(input("Guess a row: "))
                user_guess_column = int(input("Guess a column: "))
                if (
                    0 <= user_guess_row < self.board_size
                    and 0 <= user_guess_column < self.board_size
                ):
                    return user_guess_row, user_guess_column
                else:
                    print("Invalid row or column input. Try again.")
            except ValueError:
                print("Invalid input. Please enter numeric values.")


"""
promots user to input gueses with error handling
tracking hits ships
"""

class Game:
    def __init__(self, board_size, num_ships):
        self.board_size = board_size
        self.num_ships = num_ships
        self.user_board = ShipBoard(board_size)
        self.computer_board = ShipBoard(board_size)
        self.hidden_board = GuessBoard(board_size)
        self.player_score = 0
        self.computer_score = 0
        self.round = 0

    def welcome_message(self):
        print("----------------------------------")
        print("Welcome to ULTIMATE BATTLESHIPS!!")
        print("Board Size:", self.board_size, "Number of ships:", self.num_ships)
        print("Top left corner is row: 0, col: 0")
        print("------------------------------------")

    def get_name(self):
        name = input("Please enter your name: ")
        return name

    def get_guess(self):
        while True:
            try:
                user_guess_row = int(input("Guess a row: "))
                user_guess_column = int(input("Guess a column: "))
                if (
                    0 <= user_guess_row < self.board_size
                    and 0 <= user_guess_column < self.board_size
                ):
                    return user_guess_row, user_guess_column
                else:
                    print("Invalid row or column input. Try again.")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [["."] * size for _ in range(size)]

class ShipBoard(Board):
    def place_ships(self, num_ships):
        for _ in range(num_ships):
            while True:
                random_row = randint(0, self.size - 1)
                random_column = randint(0, self.size - 1)
                if self.grid[random_row][random_column] != "@":
                    self.grid[random_row][random_column] = "@"
                    break

def main():
    while True:
        try:
            board_size = int(input("Please enter board size: "))
            max_ships = int(board_size * board_size * 0.6)
            while True:
                num_ships = int(input(f"Please enter number of ships (1-{max_ships}): "))
                if 1 <= num_ships <= max_ships:
                    break
                else:
                    print(f"Invalid number of ships. Please choose a number between 1 and {max_ships}.")

            game = Game(board_size, num_ships)
            game.play()
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")


class GuessBoard(Board):
    def __init__(self, size):
        super().__init__(size)
        self.hits = 0


def main():
    while True:
        try:
            board_size = int(input("Please enter board size: "))
            max_ships = int(board_size * board_size * 0.6)
            while True:
                num_ships = int(input(f"Please enter number of ships (1-{max_ships}): "))
                if 1 <= num_ships <= max_ships:
                    break
                else:
                    print(f"Invalid number of ships. Please choose a number between 1 and {max_ships}.")

            game = Game(board_size, num_ships)
            game.play()
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

