#######################################################
# Name: Ahmed Affaan                                  #
# Title: app.py                                       #
# Folder: Object Functions                            #
# Date: 03/01/2022                                    #
# Country: Reublic of Maldives                        #
# Code version: 3.8.10                                #
# Description:                                        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start.

# Importing the Student class from the Student file.
from Student import Student

# Creating the students.
student_1 = Student("Affaan", "Computer Science", 3.1)
student_2 = Student("Ahmed", "Business Administration", 3.8)

"""
# Testing output.
# Prints student_1's name.
print(student_1.name)
# Prints student_2's major.
print(student_2.major)
# Prints student_3's gpa.
print(student_3.gpa)
# Prints student_4's probation status.
print(student_4.is_on_probation)
"""

# Testing output.
# Checks student's honor roll status.
print(student_1.on_honor_roll())
print(student_2.on_honor_roll())

# Program end.
