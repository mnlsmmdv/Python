#######################################################
# Name: Ahmed Affaan                                  #
# Title: lists_and_loops.py                           #
# Date: 14/11/2021                                    #
# Country: Reublic of Maldives                        #
# Code version: 3.8.10                                #
# Description: 2D Lists & Nested Loops                #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start

"""
# Creation of a basic list with elements
number_grid = [
    1, 2, 3, 4
]
"""

# Creation of basic list with nested lists (2D List)
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

"""
# This will print the whole number grid
print(number_grid)
"""

"""
# Printing an individual element from the number grid
# First [] is for row and second [] is for column
print(number_grid[0][0])
print(number_grid[2][1])
print(number_grid[3][0])
"""

# For Loop implemented to print out all the elements of the 2D List
for row in number_grid:
    # Doing this it will print out the 2D List as defined above
    #print(row)
    for col in row:
        print(col)

# Program end
