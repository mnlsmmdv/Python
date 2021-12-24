#######################################################
# Name: Ahmed Affaan                                  #
# Title: useful_tools.py                              #
# Folder: Modules & Pip                               #
# Date: 14/12/2021                                    #
# Country: Reublic of Maldives                        #
# Code version: 3.8.10                                #
# Description:                                        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start.

# Importing "random" module.
import random

# How many Feet are in a Mile.
feet_in_miles = 5280
# How many Meters are in a Kilometer.
meters_in_kilometers = 1000
# List declared with names of Beatles band member names.
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

# This function gives back the file extension type.
def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

# This function simulates rolling a dice when given a random number to roll.
# For example: A 10 sided dice.
def roll_dice(num):
    return random.randint(1, num)

# Program end.
