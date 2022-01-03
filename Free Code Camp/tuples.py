#######################################################
# Name: Ahmed Affaan                                  #
# Title: tuples.py                                    #
# Date: 20/09/2021                                    #
# Country: Republic of Maldives                       #
# Code version: 3.8.10                                #
# Description: Tuples creation and modification       #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start


"""
Tuples - Structures that can contain various values.
Common types of Tuples are "Coordinates".
Create a variable and define as example "variable = (4, 15)"
and add values inside the brackets (parentheses).
Tuples after creation can not be changed or modified.
"""
maldives = (2, 13)


"""
Code below will print attributes inside the Tuples
Note: Printing Tuples will work similar same as printing specific indexes in lists
Define Tuple's variable name and place the index to be printed inside square brackets as shown "print(variable[1])"
"""
print(maldives[1])


"""
List of Tuples
Create a variable and define as example "variable = [(13, 21), (2, 15), (5, 17), (20, 11)]"
This also can not be changed after creation
Below a new variable is created + print statement to display Tuple list
"""
alphago = [(13, 21), (2, 15), (5, 17), (20, 11)]
# Code below will print the whole Tuple coordinates inside brackets
print(alphago[3])

# Code below will print a specific index of the Tuple coordinate
print(alphago[3][1])

# Code below will print a specific index of the Tuple coordinate with a message
print("How messages can be displayed with Tuples. The Tuple coordinate is: " + str(alphago[3][1]))

# Program end
