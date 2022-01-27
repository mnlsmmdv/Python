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

# Displays a welcome message.
print("Welcome to my computer quiz!")
# Divider print statement.
print("--------------------------------")

# Asks user's choice.
playing = input("Do you want to play?: ")

# Given for one line spacing.
print("")

# This will ask user's choice to continue the game.
# Inputs are changed to lower case.
if playing.lower() != "yes":
    quit()

# Displayed when the user agrees to continue the game.
print("Okay! Let's play :)")
# Divider print statement.
print("--------------------------------")

# Given for one line spacing.
print("")

# This will store the user's answer. Question #1.
answer = input("What does CPU stand for?: ")
# Validates the answer for Question #1.
if answer == "central processing unit":
    # Displays if user's answer is correct.
    print("Correct!")
else:
    # Displays if user's answer is incorrect.
    print("Incorrect!")

# Given for one line spacing.
print("")

# This will store the user's answer. Question #2.
answer = input("What does GPU stand for?: ")
# Validates the answer for Question #2.
if answer == "graphics processing unit":
    # Displays if user's answer is correct.
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
    # Displays if user's answer is correct.
    print("Correct!")
else:
    # Displays if user's answer is incorrect.
    print("Incorrect!")

# Given for one line spacing.
print("")

# This will store the user's answer. Question #4.
answer = input("What does PSU stand for?: ")
# Validates the user's answer for Question #4.
if answer == "power supply unit":
    # Displays if user's answer is correct.
    print("Correct!")
else:
    # Displays if user's answer is incorrect.
    print("Incorrect!")



# Program end.
