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

    # This function will check if the game still have empty squares.
    def empty_squares(self):
        # This will function as a Boolean.
        return ' ' in self.board

    # This function will check the number of empty squares.
    def num_empty_squares(self):
        return self.board.count(' ')

    """
    This function will make a move.
    If valid move, then make the move (assign square to letter)
    then return true, if invalid, return false.
    """
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    # This function will specify the winner.
    def winner(self, square, letter):
        # Checks row index for winning streak.
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Checks the column for winning streak.
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        """
        Checks diagonals
        but only if the square is an even number (0, 2, 4, 6, 8)
        these are the only moves possible to win a diagonal.
        """
        if square % 2 == 0:
            # Left to right diagonal.
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            # Right to left diagonal.
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        # If all checks fail.
        return False

# This function helps get rest of the functions.
def play(game, x_player, o_player, print_game = True):
    # Printing the game.
    if print_game:
        # Defines which numbers corresponds to which spot.
        game.print_board_nums()
    
    # The starting letter.
    letter = 'X'

    """
    Iterate while the game still has empty squares
    (we don't have to worry about winner because we'll just return that
    which breaks the loop)
    """
    while game.empty_squares():
        # Get the move from the appropriate player.
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # This function will make a move.
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' make a move to square {square}')
                # This will print the updated board.
                game.print_board()
                # Empty line.
                print('')
            
            # Specifies the letter that made us win.
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                # Returns the letter that made us win.
                return letter

            # After we make a move, we need to alternate our letters.
            letter = 'O' if letter == 'X' else 'X'

        # This will display the tie.
        if print_game:
            print('It\'s a tie!')
            
# Program end.
