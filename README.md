![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Stayin_blick,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
# Ultimate Battleships

This is a command-line implementation of the Battleship game. The player takes turns against the computer in guessing the positions of ships on the opponent's board and tries to sink their battleships. The player is given the option of changing the grid size as well as the number of battleships that populate the grid.

-----

![Screenshot 2023-06-08 at 07 06 03](https://github.com/Stayin-blick/battleship-resub/assets/109948932/d598612e-18e2-4944-9939-cef64044857d)

## Rules
- M represents a missed shot
- H represents a hit shot
- Players take alternate turns at guessing ship locations

Follow the on-screen instructions to play the game. Enter the board size and the number of ships, and then take turns guessing the positions of the ships.

The game will continue until either the player or the computer has sunk all the ships. The final scores will be displayed, and you will have the option to play again by entering either yes or no.

## Features

- random ship placement

![Screenshot 2023-06-08 at 07 28 28](https://github.com/Stayin-blick/battleship-resub/assets/109948932/e01e996d-3202-4be4-a835-c8fd7ed48148)

- accept user input tracks number of ships hit and round number

![Screenshot 2023-06-08 at 07 30 22](https://github.com/Stayin-blick/battleship-resub/assets/109948932/d0cadc21-425d-462a-992c-142e77b0e2fc)
![Screenshot 2023-06-08 at 07 31 02](https://github.com/Stayin-blick/battleship-resub/assets/109948932/220339fb-76d6-4dd2-bafb-e035697f5cce)

- input validation and error checking
  - cannot enter coordinates outside of the grid
  - must be numbers 
  - prompts that youve already guessed that
  - limits the max number of ships on the grid

![Screenshot 2023-06-08 at 07 32 13](https://github.com/Stayin-blick/battleship-resub/assets/109948932/c33cf752-42e6-4b19-ba73-6ba174432325)

- data maintained in class instances

# Future features

- a difficulty setting (easy, medium, hard) this will limit the amount of rounds played in each game so user is under pressure
- allow different ship sizes
- allow the user to place ships themselves 

# Data model

The Board class serves as the base class, representing the game board itself. It contains a grid that holds the state of each cell on the board. The ShipBoard class extends the Board class and represents the player's ship board. It allows for the random placement of ships on the board. The GuessBoard class also extends the Board class and represents the computer's hidden board, where the player's guesses and hits are tracked. Finally, the Game class orchestrates the main game flow. It takes user inputs for board size and the number of ships, initializes the player and computer boards, and manages the game rounds. The data model provides a structured representation of the game elements and enables the game logic to be implemented effectively.

# Testing 

I have manaully tested this project by:

- passing the code through PEP8 linter and confirmed there are no problems
- given invalid inputs:
  - coordinates off the grid
  - non numerical inputs
  - repeated inputs
- tested in my local terminal as well as hosted site 

# Validator testing

- PEP8
  - f strings are above character limit but readable 

# Deployment 

this project was deployed using code insitutes mock terminal for heroku

- steps for deployment
  - fork or clone this repository 
  - create a new heroku app 
  - set the build packs Python and NodeJS
  - link heroku to repository 
  - click deploy 

# credits

- code insitute for deployment terminal 

