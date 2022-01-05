#######################################################
# Name: Ahmed Affaan                                  #
# Title: ItalianChef.py                               #
# Folder: Inheritance                                 #
# Date: 05/01/2022                                    #
# Country: Republic of Maldives                       #
# Code version: 3.8.10                                #
# Description:                                        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start.

# Importing the Chef class from the Chef file.
from Chef import Chef
# Importing the ChineseChef class from the ChineseChef file.
from ChineseChef import ChineseChef

# Program's main class.
# This class describes the functions of a Italian Chef.
# The Italian Chef can do what a Chef and Chinese Chef does and even more.
class ItalianChef(ChineseChef):
    # Function to describe a chef's specific job.
    # This will override the dish in the dish in the ChineseChef class.
    def make_special_dish(self):
        # Describes what exactly the chef does.
        print("The Chef makes Lasagna")
    
    # Function to describe a chef's specific job.
    def make_italian_pizza(self):
        # Describes what exactly the chef does.
        print("The Chef makes Italian pizza")

# Program end.
