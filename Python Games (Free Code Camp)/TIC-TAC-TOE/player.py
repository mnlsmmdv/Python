#######################################################
# Name: Ahmed Affaan                                  #
# Title: player.py                                    #
# Folder: TIC-TAC-TOE                                 #
# Date: 10/01/2022                                    #
# Country: Republic of Maldives                       #
# Code version: 3.8.10                                #
# Description:                                        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start.

# Python module to use mathematical tasks.
import math
# Python module to use random values.
import random

# Main program class to define the player.
class Player:
    # Main program function to define Player's letter (X or O).
    def __init__(self, letter):
        # Letter is X or O.
        self.letter = letter

    # Function to help Player's get their next move.
    def get_move(self, game):
        # Null statement.
        pass

# Random computer player made with inheritance.
class RandomComputerPlayer(Player):
    # Main function for this class. Super class.
    def __init__(self, letter):
        
# Program end.
