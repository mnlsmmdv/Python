"""
Name: Ahmed Affaan                                  
Title: rock_paper_scissors.py                                 
Date: 28/01/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description:                                        
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start.

# This module will generate random values.
import random

# This will store the user's score.
# Default value kept as 0.
user_wins = 0

# This will store the computer's score.
# Default value kept as 0.
computer_wins = 0

# This will iterate through the whole game.
while True:
    # This will store user's input.
    user_input = input("Rock/Paper/Scissors or Q to quit: ").lower()

    # This will check if the user wants to quit, continues the game.
    if user_input == "q":
        # Breaks out of the program.
        break

    # Checks for the choices in the game.
    # Choices are kept in a list and checked.
    if user_input not in ["rock", "paper", "scissors"]:
        # If what user entered is not valid we will urge them to loops back.
        continue 

    # Generates random number for the computer to play the game.
    # 0 - rock, 1 - paper, 2 - scissors
    random_number = random.randint(0, 2)

# This is the final end message.
print("Goodbye.")

# Program end.
