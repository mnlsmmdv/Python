#######################################################
# Name: Ahmed Affaan                                  #
# Title: guess_number_user.py                         #
# Date: 08/01/2022                                    #
# Country: Republic of Maldives                       #
# Code version: 3.8.10                                #
# Description:                                        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start.

# Importing a module.
# This module generates random numbers.
import random

# Function to conduct guesses.
# x passed as parameter to get random get number function.
def guess(x):
    # Getting the random number.
    # Will return a random number to guess.
    random_number = random.randint(1, x)
    # Guess variable. Default value starts at 0.
    guess = 0

     # If the guess is not equal to random number this will iterate in a While Loop. 
    while guess != random_number:
        # Getting the users guess as input.
        # Casted the input as integer to recieve as an integer as well.
        guess = int(input(f'Guess a number between 1 and {x}: '))

# Program end.
