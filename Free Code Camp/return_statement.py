#######################################################
# Name: Ahmed Affaan                                  #
# Title: return_statement.py                          #
# Date: 21/09/2021                                    #
# Country: Republic of Maldives                       #
# Code version: 3.8.10                                #
# Description: -                                      #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start
# Returning functions (Return Statements)

# Functions declaration
# Functions declared for each basic Arithmetic Operations
def cube(cube):
    return cube * cube * cube

def add(add):
    return add + add + add

def subtract(subtract):
    return subtract - subtract

def divide(divide):
    return divide / divide

# Executing the function (Calling the Function)
# Examples of code that won't work
# After adding "return" inside the function it will work
#cube(3)
#print(cube(3))

# Another variation
print("the answers are!: ".isupper())
# Finding the cube value
result_cube = cube(4)
print("The cube value is: " + str(result_cube))

# Finding the add value
result_add = add(4)
print("The added value is: " + str(result_add))

# Finding the subtract value
result_subtract = subtract(2)
print("The subtract value is: " + str(result_subtract))

# Finding the divide value
result_divide = divide(2)
print("The divide value is: " + str(result_divide))

# Program end
