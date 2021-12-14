#######################################################
# Name: Ahmed Affaan                                  #
# Title: useful_tools.py                              #
# Folder: Modules & Pip                               #
# Date: 14/11/2021                                    #
# Country: Reublic of Maldives                        #
# Code version: 3.8.10                                #
# Description:                                        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start.

# Importing "random" module.
import random

feet_in_miles = 5280
meters_in_kilometers = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)



# Program end.
