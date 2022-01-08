#######################################################
# Name: Ahmed Affaan                                  #
# Title: rock_paper_scissors.py                       #
# Date: 08/01/2022                                    #
# Country: Republic of Maldives                       #
# Code version: 3.8.10                                #
# Description:                                        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start.

# Simple use case how the game works.
# r > s, s > p, p > r

# Importing random module.
import random

# Function to play the game.
def play():
    # Asking for user input.
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    # Computer randomly chooses one of these choices.
    computer = random.choice(['r', 'p', 's'])

    # This will return the tie if both choices are the same.
    if user == computer:
        # If the two sides give the same choice this will print.
        return 'It\'s a tie'

    # This will ask if the user has won.
    if is_win(user, computer):
        # If the user won this will print.
        return 'You won!'

    # If the computer won and you lose this will print.
    return 'You lost!'

# Function to see who wins.
def is_win(player, opponent):
    # This will return True if the player wins.
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        # If the player wins will return True.
        return True

# Calling the function.
# Called using a print statement.
print(play())

# Program end.
