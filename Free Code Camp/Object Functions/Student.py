#######################################################
# Name: Ahmed Affaan                                  #
# Title: Student.py                                   #
# Folder: Object Functions                            #
# Date: 03/01/2022                                    #
# Country: Reublic of Maldives                        #
# Code version: 3.8.10                                #
# Description:                                        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start.

# Creating specific class.
class Student:
    # Creating the initialised function.
    # After comma in self are variable names.
    def __init__(self, name, major, gpa):
        # Assigning values to the function.
        self.name = name
        self.major = major
        self.gpa = gpa
    
    # Function to validate student is on the honor roll.
    # Honor roll eligible only for gpa's 3.5 and above.
    def on_honor_roll(self):
        # This will check the validity of the student's gpa.
        if self.gpa >= 3.5:
            # If the gpa is 3.5 or above honor status is True.
            return True

# Program end.
