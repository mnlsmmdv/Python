"""
Name: Ahmed Affaan                                  
Title: quiz_game.py                                 
Date: 19/01/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description:                                        
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start.

# Displays as welcome message.
print("Welcome to my computer quiz!")

# Asks user's choice.
playing = input("Do you want to play?: ")

# Given for one line spacing.
print("")

# This will ask user's choice to continue the game.
if playing != "Yes" or "yes":
    quit()

# Displayed when the user agrees to continue the game.
print("Okay! Let's play :)")

# Given for one line spacing.
print("")

# This will store the user's answer. Question #1.
answer = input("What does CPU stand for?: ")
# Validates the answer for Question #1.
if answer == "central processing unit":
    # Displays if user's answer is correct.
    print("Correct!")
else:
    # Displays if user's answer if incorrect.
    print("Incorrect!")

# Given for one line spacing.
print("")

# This will store the user's answer. Question #2.
answer = input("What does GPU stand for?: ")
# Validates the answer for Question #2.
if answer == "graphics processing unit":
    # Displays if user's answer if correct.
    print("Correct!")
else:
    # Displays if user's answer is incorrect.
    print("Incorrect!")

# Given for one line spacing.
print("")

# This will store the user's answer. Question #3.
answer = input("What does RAM stand for?: ")
# Validates the answer for Question #3.
if answer == "random access memory":
    # Displays if user's answer if correct.
    print("Correct!")
else:
    # Displays if user's answer is incorrect.
    print("Incorrect!")

# Given for one line spacing.
print("")



# Program end.
