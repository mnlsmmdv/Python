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

# Function declared to calculate Miles to Feet.
def miles_to_feet (user_input, miles_in_feet):
    return user_input * miles_in_feet

# Function declared to calculate Kilometers to Meters.
def kilometeres_to_meters(user_input, kilometers_in_meters):
    return user_input * kilometers_in_meters

# Giving user broad choices.
print("Please select desired operation!")
print("--------------------------------")
print("1. Miles to Feet")
print("2. Kilometers to Meters")
print("--------------------------------")

# Taking specific choice input from the user.
while True:
    # Taking user input.
    user_choice = input("Enter Choice(1/2): ")


# Program end.
