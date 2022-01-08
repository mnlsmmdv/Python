#######################################################
# Name: Ahmed Affaan                                  #
# Title: guess_number_computer.py                     #
# Date: 06/01/2022                                    #
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

# Function for the computer to conduct guesses.
# x passed as parameter to get random number function.
def computer_guess(x):
    # Defining the guess parameters
    # Variable for lowest starting point.
    low = 1
    # Variable for highest point (user specified)
    high = x
    # Feedback variable. Default value is an empty string.
    feedback = ''

    # While Loop checks for user feedback.
    # Checks for "c" as in "correct" to verify the guess was correct.
    while feedback != 'c':
        # Getting the random guess number.
        guess = random.randint(low, high)
        # Getting the users feedback as input.
        # Will input all inputs as lower case.
        feedback = input(f'Is {guess} too high (H), or too low (L), or correct (C)?? ').lower()

        # If Elif statements to value feedback.
        # This will set the upper bound.
        if feedback == 'h':
            # If feedback guess is high it will decrease by 1.
            high = guess - 1
        # This will set the lower bound.
        elif feedback == 'l':
            # If feedback guess is low it will add by 1.
            low = guess + 1

        # If computer guesses correctly this will print.
        print(f"Yay! The computer guessed your number, {guess}, correctly!!")

# Calling the computer_guess function.
# Parameter given up to the number 10.
computer_guess(10)

# Program end.
