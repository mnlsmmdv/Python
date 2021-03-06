"""
Name: Ahmed Affaan                                  
Title: number_guesser.py                                 
Date: 27/01/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description:                                        
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start.

# This module will generate random values.
import random

# Collects input from user to guess.
top_of_range = input("Type a number: ")

# Checks if the value passed is a digit.
if top_of_range.isdigit():
    # Changes the string input to an integer.
    top_of_range = int(top_of_range)
    
    # Checks if the digit is greater than 0.
    if top_of_range <= 0:
        # Message displayed to enter a larger number & quits the program.
        print("Please enter a number larger than 0 next time!")
        quit()

# Displayed when value passed is not a number & quits.
else:
    print("Please type a number next time!")
    quit()

# This variable will store the random value.
random_number = random.randint(0, top_of_range)

# This will keep track how many guesses a user makes.
# Default value kept as 0.
guesses = 0

# This will iterate until user's guess is correct.
while True:
    # Increments the user's guess count.
    guesses += 1

    # Asks the user's a number to guess.
    # This variable will store the user's guess.
    user_guess = input("Make a guess: ")
    
    # This will check what the user entered was a number.
    # Checks if passed value is a digit.
    if user_guess.isdigit():
        # If it's a digit changes the value to an integer.
        user_guess = int(user_guess)
    # If the value passed is not a digit this message is shown.
    else:
        print("Please type a number next time!")
        # This will go back to the loop and iterate again.
        continue

    # Displayed when the user guessed it correct or incorrect.
    if user_guess == random_number:
        # Message displayed when correct.
        print("You guessed it correct!")
        # Stops the iteration when you get it correct.
        break
    # This will display if the user's guess was above or below.
    elif user_guess > random_number:
        # If user's guess above the number.
        print("You were above the number.")
    else:
        # If user's guess above the number.
        print("You were below the number.")

# Given for one line spacing.
print("")
# Divider print statement.
print("--------------------------------")
# This will display how many guesses the user attempted.
print("You got in", guesses, "guesses.")
# Divider print statement.
print("--------------------------------") 

# Program end.
