"""
Name: Ahmed Affaan                                  
Title: player.py                                    
Folder: TIC-TAC-TOE                                 
Date: 10/01/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description:                                        
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

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
# Super class is Player.
class RandomComputerPlayer(Player):
    # Main function for this class. Initialisation function.
    def __init__(self, letter):
        # Calls initialisation in the super class.
        super().__init__(letter)

    # To be edited later.
    def get_move(self, game):
        # This selects a random empty spot to make our next move.
        square = random.choice(game.available_moves())
        # Returns an empty square.
        return square

# Human player made with inheritance.
# Super class is Player.
class HumanPlayer(Player):
    # Main function for this class. Initialisation function.
    def __init__(self, letter):
        # Calls initialisation in the super class.
        super().__init__(letter)

    # To be edited later.
    def get_move(self, game):
        # Keeps iterating until they get a valid square.
        valid_square = False
        val = None

        # While valid square is False this will iterate.
        while not valid_square:
            # User input for move.
            square = input(self.letter + '\' turn. Input move (0-8): ')

            """
            We're going to check that this is a correct value by trying to cast
            it to an integer, and if it's not, then we say it's invalid if that
            spot is not available on the board, we also say it's invalid.
            """
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                # If these are succesful, then it's good.
                valid_square = True
            except ValueError:
                print('Invalid square. Try again!')
        
        # Returns the HumanPlayer 's value.
        return val

# Program end.
