#######################################################
# Name: Ahmed Affaan                                  #
# Title: quiz_game.py                                 #
# Date: 19/01/2022                                    #
# Country: Republic of Maldives                       #
# Code version: 3.8.10                                #
# Description:                                        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start.

# Welcome message.
print("Welcome to my computer quiz!")

# Variable to ask user if they want to play.
# This variable will also get the user's input.
playing = input("Do you want to play?: ")

# This will check if the user answered "yes" or "no".
# If it's not yes it will quit the game.
if playing != "YES" and "Yes" or "yes":
    quit()

# If the answer is yes then this displays.
print("Okay! Let's play :)")

# Variable to ask user a question. Question 1.
# This variable will also get the user's input.
answer = input("What does CPU stand for?: ")
# Checks the user's given answer.
# If it's correct or incorrect it will be displayed.
if answer == "Central Processing Unit" or "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")

# Variable to ask user a question. Question 2.
# This variable will also get the user's input.
answer = input("What does GPU stand for?: ")
# Checks the user's given answer.
# If it's correct or incorrect it will be displayed.
if answer == "Graphical Processing Unit" or "graphical processing unit":
    print("Correct!")
else:
    print("Incorrect!")

# Variable to ask user a question. Question 3.
# This variable will also get the user's input.
answer = input("What does RAM stand for?: ")
# Checks the user's given answer.
# If it's correct or incorrect it will be displayed.
if answer == "Random Access Memory" or "random access memory":
    print("Correct!")
else:
    print("Incorrect!")

# Variable to ask user a question. Question 4.
# This variable will also get the user's input.
answer = input("What does PSU stand for?: ")
# Checks the user's given answer.
# If it's correct or incorrect it will be displayed.
if answer == "Power Supply Unit" or "power supply unit":
    print("Correct!")
else:
    print("Incorrect!")



# Program end.
