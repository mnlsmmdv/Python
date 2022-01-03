#######################################################
# Name: Ahmed Affaan                                  #
# Title: roll_dice.py                                 #
# Folder: Modules & Pip                               #
# Date: 14/12/2021                                    #
# Country: Republic of Maldives                       #
# Code version: 3.8.10                                #
# Description:                                        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start.

# Importing module.
import useful_tools

# Variable declared asking for user input.
# Initial user input will be a String value.
user_input = int(input("Enter a number: "))

# Printing the user input we got as an integer.
# Each turn will be random.
print("The number from the rolled dice is: " + str(useful_tools.roll_dice(user_input)))

# Program end.
