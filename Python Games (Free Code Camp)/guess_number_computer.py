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

        # If Elif statements to value guesses.
        # If guess is less than the random number this will print.
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        # If guess is greater than the random number this will print.
        elif guess > random_number:
            print("Sorry, guess again. Too high.")

    # If guess is equal to random number this will print.
    print(f"Yay, congrats. You have guessed the number {random_number} correctly!!")

# Function for the computer to conduct guesses.
# x passed as parameter to get random number function.
def computer_guess(x):
    

# Calling the guess function.
# Parameter given up to the number 10.
guess(10)

# Program end.
