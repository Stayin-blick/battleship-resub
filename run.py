"""
Battleship Game resub
--------------
This is a command-line implementation of the Battleship game
The Player takes turns against the computer in guessing the
positions of ships on the opponents board and try to sink
their battleships. The player is given the option of changing
the grid size as well as how many battleships populate
the grid.
# M represents missed shot
# H represents hit shot
"""
from random import randint


class Board:
    """
    Represents the game board.
    """

    def __init__(self, size):
        """
        Initialize the game board with the given size.
        """
        self.size = size
        self.grid = [["."] * size for _ in range(size)]


class ShipBoard(Board):
    """
    Represents the player's ship board.
    Places ships randomly on the ship board.
    """

    def place_ships(self, num_ships):
        """
        Randomly place ships on the board based on num_ships.
        """
        for _ in range(num_ships):
            while True:
                random_row = randint(0, self.size - 1)
                random_column = randint(0, self.size - 1)
                if self.grid[random_row][random_column] != "@":
                    self.grid[random_row][random_column] = "@"
                    break


class GuessBoard(Board):
    """
    Computer's hidden board.
    """

    def __init__(self, size):
        """
        Create the computer's hidden board with the given size.
        """
        super().__init__(size)
        self.hits = 0


class Game:
    """
    Main game class.
    Manages the game flow, user input, and scoring.
    """

    def __init__(self, board_size, num_ships):
        """
        Creates the game with the board size and number of ships.
        """
        self.board_size = board_size
        self.num_ships = num_ships
        self.user_board = ShipBoard(board_size)
        self.computer_board = ShipBoard(board_size)
        self.hidden_board = GuessBoard(board_size)
        self.player_score = 0
        self.computer_score = 0
        self.round = 0

    def welcome_message(self):
        """
        Display the welcome message and game setup information.
        """
        print("----------------------------------")
        print("Welcome to ULTIMATE BATTLESHIPS!!")
        print(
            "Board Size:", self.board_size, "Number of ships:", self.num_ships
        )
        print("Top left corner is row: 0, col: 0")
        print("------------------------------------")

    def get_name(self):
        """
        Get the player's name as input.
        """
        name = input("Please enter your name: ")
        return name

    def get_guess(self):
        """
        Get the player's row and column guess.
        """
        while True:
            try:
                user_guess_row = int(input("Guess a row:\n"))
                user_guess_column = int(input("Guess a column:\n"))
                if (
                    0 <= user_guess_row < self.board_size
                    and 0 <= user_guess_column < self.board_size
                ):
                    if (
                        self.computer_board.grid[user_guess_row][
                            user_guess_column
                        ]
                        == "M"
                        or self.computer_board.grid[user_guess_row][
                            user_guess_column
                        ]
                        == "H"
                    ):
                        print("You guessed that one already. Try again.")
                    else:
                        return user_guess_row, user_guess_column
                else:
                    print("Invalid row or column input. Try again.")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

    def count_ships_hit(self, board):
        """
        Count the number of ships hit on the given board.
        """
        count = 0
        for row in board.grid:
            count += row.count("H")
        return count

    def play(self):
        """
        Main game loop to play Battleship.
        """
        self.welcome_message()
        name = self.get_name()
        print(name + "'s Board:")
        self.user_board.place_ships(self.num_ships)
        for row in self.user_board.grid:
            print(" ".join(row))

        print("Computer's Board:")
        for row in self.computer_board.grid:
            print(" ".join(row))

        while True:
            self.round += 1
            print(f"\nRound: {self.round}")

            print(name + "'s turn")
            try:
                user_guess_row, user_guess_column = self.get_guess()

                if (
                    self.user_board.grid[user_guess_row][user_guess_column]
                    == "@"
                ):
                    print("You scored a point")
                    self.player_score += 1
                    self.hidden_board.grid[user_guess_row][
                        user_guess_column
                    ] = "H"
                    self.computer_board.grid[user_guess_row][
                        user_guess_column
                    ] = "H"
                else:
                    print(name + " missed this time")
                    self.computer_board.grid[user_guess_row][
                        user_guess_column
                    ] = "M"

                print(name + "'s board'")
                for row in self.user_board.grid:
                    print(" ".join(row))
                print("---------------------------------------")
                print("Computer's board")
                for row in self.computer_board.grid:
                    print(" ".join(row))
                print("---------------------------------------")

                if self.count_ships_hit(self.computer_board) == self.num_ships:
                    print(name + " wins")
                    break

                print("Computer's turn")
                while True:
                    computer_guess_row = randint(0, self.board_size - 1)
                    computer_guess_column = randint(0, self.board_size - 1)
                    if (
                        self.hidden_board.grid[computer_guess_row][
                            computer_guess_column
                        ]
                        != "M"
                    ):
                        break

                if (
                    self.user_board.grid[computer_guess_row][
                        computer_guess_column
                    ]
                    == "@"
                ):
                    print("Computer scored a point")
                    self.computer_score += 1
                    self.user_board.grid[computer_guess_row][
                        computer_guess_column
                    ] = "H"
                else:
                    print("Computer missed this time")
                    self.user_board.grid[computer_guess_row][
                        computer_guess_column
                    ] = "M"

                print(name + "'s board'")
                for row in self.user_board.grid:
                    print(" ".join(row))
                print("---------------------------------------")
                print("Computer's board")
                for row in self.computer_board.grid:
                    print(" ".join(row))
                print("---------------------------------------")

                if self.count_ships_hit(self.user_board) == self.num_ships:
                    print("Computer wins")
                    break

                print(
                    f"\n{name} has {self.num_ships - self.count_ships_hit(self.user_board)} ships left."
                )
                print(
                    f"\nComputer has {self.num_ships - self.count_ships_hit(self.computer_board)} ships left."
                )

            except ValueError:
                print("Invalid input. Please enter numeric values.")
            except IndexError:
                print("Invalid row or column input. Try again.")


def main():
    """
    Main function to start the Battleship game.
    """
    while True:
        try:
            board_size = int(input("Please enter board size:\n"))
            max_ships = int(board_size * board_size * 0.6)
            while True:
                num_ships = int(
                    input(f"Please enter number of ships (1-{max_ships}):\n")
                )
                if 1 <= num_ships <= max_ships:
                    break
                else:
                    print(
                        f"Invalid number of ships. Please choose a number between 1 and {max_ships}."
                    )

            game = Game(board_size, num_ships)
            game.play()
            play_again = input("Do you want to play again? (yes/no):\n")
            if play_again.lower() != "yes":
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
