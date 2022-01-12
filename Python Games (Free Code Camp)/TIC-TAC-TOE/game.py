#######################################################
# Name: Ahmed Affaan                                  #
# Title: game.py                                      #
# Folder: TIC-TAC-TOE                                 #
# Date: 10/01/2022                                    #
# Country: Republic of Maldives                       #
# Code version: 3.8.10                                #
# Description:                                        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start.

# Main program class.
class TicTacToe:
    # This function will house the board.
    def __init__(self):
        # Board variable.
        # Single list used to represent 3x3 board.
        self.board = [' ' for _ in range(9)]
        # Keeps track of winner.
        self.current_winner = None

# Program end.
