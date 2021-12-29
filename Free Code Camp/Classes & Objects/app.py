#######################################################
# Name: Ahmed Affaan                                  #
# Title: app.py                                       #
# Folder: Classes & Objects                           #
# Date: 25/12/2021                                    #
# Country: Reublic of Maldives                        #
# Code version: 3.8.10                                #
# Description:                                        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start.

# Importing the Student class from the Student file.
from Student import Student

# Creating the student.
student_1 = Student("Affaan", "Computer Science", 3.1, False)
student_2 = Student("Ahmed", "Business Administration", 3.0, True)
student_3 = Student("Naail", "Computer Science", 3.1, False)
student_4 = Student("Nashath", "Computer Science", 3.7, True)

# Testing output
print(student_1.name)
print(student_2.major)
print(student_3.gpa)

# Program end.
