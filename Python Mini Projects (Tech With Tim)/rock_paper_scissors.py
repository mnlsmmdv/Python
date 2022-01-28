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

# This will store the game options in a list.
options = ["rock", "paper", "scissors"]

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
    if user_input not in options:
        # If what user entered is not valid we will urge them to loops back.
        continue 

    # Generates random number for the computer to play the game.
    # 0 - rock, 1 - paper, 2 - scissors
    random_number = random.randint(0, 2)

    # This will go through the list for the computer to choose.
    computer_pick = options[random_number]
    # This will print what the computer chose.
    print("Computer picked", computer_pick + ".")

    # Compares computer and user's picks.
    # Picks the winning conditions.
    # Condition rock VS scissors
    if user_input == "rock" and computer_pick == "scissors":
        # Tells the user they have won.
        print("You won!")
        # Increments one point to the user.
        user_wins += 1
        # Loops back to the start of the While Loop.
        continue

    # Condition paper VS rock
    elif user_input == "paper" and computer_pick == "rock":
        # Tells the user they have won.
        print("You won!")
        # Increments one point to the user.
        user_wins += 1
        # Loops back to the start of the While Loop.
        continue

    # Condition scissors VS paper
    elif user_input == "scissors" and computer_pick == "paper":
        # Tells the user they have won.
        print("You won!")
        # Increments one point to the user.
        user_wins += 1
        # Loops back to the start of the While Loop.
        continue

    # If the conditions are the same for the user and the computer.
    else:
        # Tells the user they have lost.
        print("You lost!")
        # Increments one point to the computer.
        computer_wins += 1

# This is the final end message.
print("Goodbye.")

# Program end.
