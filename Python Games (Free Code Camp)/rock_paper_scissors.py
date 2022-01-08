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

# Importing random module.
import random

# Function to play the game.
def play():
    # Asking for user input.
    user = input("'r' for rock, 'p' for paper, 's' for scissors")
    # Computer randomly chooses one of these choices.
    computer = random.choice(['r', 'p', 's'])

# Program end.
