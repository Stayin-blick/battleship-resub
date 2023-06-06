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

"""
setting up the game
board size
user board
computer board
tally of ships hit
"""

board_size = int(input("Please enter board size:\n"))
num_ships = int(input("Please enter number of boats:\n"))
user_board = [["."] * board_size for x in range(board_size)]
computer_board = [["."] * board_size for x in range(board_size)]
hidden_board = [["."] * board_size for x in range(board_size)]

def display_board(board):
    for row in board:
        print (" ".join(row))


def welcomeMessage():
    print("----------------------------------")
    print("Welcome to ULTIMATE BATTLESHIPS!!")
    print("Board Size: ",board_size,"Number of ships :",num_ships)
    print("Top left corner is row: 0, col: 0")
    print("------------------------------------")

def getName():
    name = str(input("Please enter your name: \n"))
    return name


def guesses(board_size):
    user_guess_row = str(input("Guess a row: \n"))
    user_guess_column = str(input("Guess a column: \n"))
    int_user_guess_row = int(user_guess_row)
    int_user_guess_column = int(user_guess_column)
    computer_guess_row = randint(0,board_size-1)
    computer_guess_column = randint(0,board_size-1)
    while int_user_guess_row > board_size-1:
        print("Invalid row input, try again")
        user_guess_row = str(input("Guess a row: \n"))
        int_user_guess_row = int(user_guess_row)
    while int_user_guess_column > board_size-1:
        print("Invalid column input, try again")
        user_guess_column = str(input("Guess a column: \n"))
        int_user_guess_column = int(user_guess_column)

    return user_guess_row, user_guess_column, computer_guess_row, computer_guess_column

def count_ships_hit(board):
    count = 0
    for row in board:
        for column in row:
            if column == "-":
                count += 1
    return (count)


def main(board_for_user, board_for_computer, hidden_board):
    """
    Placement of ships on the board
    user
    computer
    confirmation of hits
    """
    welcomeMessage()
    name = getName()
    print(name + "'s Board:")


    for i in range(num_ships):
        random_row, random_column = randint(0,num_ships), randint(0,num_ships)
        while board_for_user[random_row][random_column] == "@":
            random_row, random_column = randint(0,num_ships), randint(0,num_ships)
        board_for_user[random_row][random_column] = "@"

    for i in range(num_ships):
        random_row, random_column = randint(0,num_ships), randint(0,num_ships)
        while hidden_board[random_row][random_column] == "@":
            random_row, random_column = randint(0,num_ships), randint(0,num_ships)
        hidden_board[random_row][random_column] = "@"

    display_board(board_for_user)

    print("Computer's Board: ")
    display_board(board_for_computer)

    player_score = 0
    computer_score = 0

    while count_ships_hit(user_board) < num_ships:
        """
        loop to determine winner
        """
        
        user_guess_row, user_guess_column, computer_guess_row, computer_guess_column = guesses(board_size)
        
        int_user_guess_row = int(user_guess_row)
        int_user_guess_column = int(user_guess_column)
        int_computer_guess_row = int(computer_guess_row)
        int_computer_guess_column = int(computer_guess_column)
        if board_for_computer[int_user_guess_row][int_user_guess_column] == "X":
            print("You guessed that one already")
            print("-----------------------------")
        else:
            if hidden_board[int_user_guess_row][int_user_guess_column] != "@":
                board_for_computer[int_user_guess_row][int_user_guess_column] = "X"
                print("Player missed this time")
            else:
                board_for_computer[int_user_guess_row][int_user_guess_column] = "-"
                print("You scored a point")
                player_score = player_score + 1
                print(name,"overall score is", player_score)

        if board_for_user[int_user_guess_row][int_user_guess_column] == "X":
            print("Computer guessed that one already")
            print("-----------------------------")
        else:
            if board_for_user[int_computer_guess_row][int_computer_guess_column] != "@":
                print("Computer missed this time")
                board_for_user[int_computer_guess_row][int_computer_guess_column] = "X"
            else:
                board_for_user[int_computer_guess_row][int_computer_guess_column] = "-"
                print("Computer scored a point")
                computer_score = computer_score + 1
                print("Computer overall score is", computer_score)

        print(name,"'s board'")
        display_board(user_board)
        print("---------------------------------------")
        print("Computer_board")
        display_board(computer_board)
        print("---------------------------------------")
        if count_ships_hit(computer_board) == num_ships:
            print(name,"wins")
            break
        if count_ships_hit(user_board) == num_ships:
            print("Computer wins")
            break

main(user_board,computer_board,hidden_board)