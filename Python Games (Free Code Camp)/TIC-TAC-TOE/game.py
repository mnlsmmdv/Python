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

    # This function will print the board.
    def print_board(self):
        # This splits it in to the rows.
        for row in [self.board[i * 3: (i + 3) * 3] for i in range(3)]:
            # This will print the separators on the board.
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    
    # Tells us what number corresponds to what box.
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        # This will do it for the whole board.
        for row in number_board:
            # This will print the separators on the board.
            print('| ' + ' | '.join(row) + ' |')

    # This function will check what moves available after a move.
    def available_moves(self):
        # This will return a list of indices.
        return [i for i, spot in enumerate(self.board) if spot == ' ']

# Program end.
