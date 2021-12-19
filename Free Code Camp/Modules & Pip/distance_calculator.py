#######################################################
# Name: Ahmed Affaan                                  #
# Title: distance_calculator.py                       #
# Folder: Modules & Pip                               #
# Date: 19/11/2021                                    #
# Country: Reublic of Maldives                        #
# Code version: 3.8.10                                #
# Description:                                        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start.

# Importing file as a module.
import useful_tools

# Declaring variables.
miles_in_feet = 5280
kilometers_in_meters = 1000

# Getting input from user.
# Initial user input will be a String value. Changed to Integer using concatenation.
user_input = int(input("Enter a number: "))

# Function declared to calculate Miles to Feet.
def miles_to_feet (user_input, miles_in_feet):
    return user_input * miles_in_feet



# Program end.
