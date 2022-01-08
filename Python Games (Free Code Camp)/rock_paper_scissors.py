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
    user = input("'r' for rock, 'p' for paper, 's' for scissors")
    # Computer randomly chooses one of these choices.
    computer = random.choice(['r', 'p', 's'])

    # This will return the tie if both choices are the same.
    if user == computer:
        return 'tie'

# Function to see who wins.
def is_win(player, opponent):
    # This will return True if the player wins.
    # r > s, s > p, p > r
    

# Program end.