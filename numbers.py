##################################################
# Name: Ahmed Affaan                             #
# Title: numbers.py                              #
# Date: 15/09/2021                               #
# Country: Maldives                              #
# Description: number creation and manipulation. #
# Note: Uncomment codes to execute and comment   #
#       them when not in use.                    #
##################################################

# Program start
# Importing math related functions (Python Modules)
from math import *

# Printing a simple number
print(2)

# Printing a simple decimal number
print(2.0987)

# Printing a simple negative number
print(-2.0987)

# Python can also execute basic Arithmetics
# Addition
print(3 + 4)
print(3 + 4.5)

# Subtraction
print(3 - 4)

# Division
# Answer will be given back in decimal point number
print(8 / 2)

# Multiplication
print(2 * 3)

# Order of operations
# Executes first one and goes to the rest.
print(3 * 4 + 5)
# If you put values inside a bracket (parentheses) it will process values in brackets first.
print(3 * (4 + 5))

"""
Modulas Operator (Mod)
Modulas Operator is defined as the percentage symbol (%)
Modulas Operator helps to divide values and output the remainder
If correct the answer will be "1"
"""
print(10 % 3)

# Storing numbers inside variable containers and printing
my_num = 5
print(my_num)

"""
Converting numbers in to a string
Variable container defined above will be used
Define the type and place within brackets
"""
print(str(my_num))

"""
Absolute value
Finds the Absolute Value of defined values
Variable container defined below will be used
Define "abs()" then add the variable container inside the brackets
"""
my_new_num = -5
print(abs(my_new_num))

"""
Power Function
Finds the power value of given values
Define "pow()" and place the values inside the brackets (parentheses) with commas to separate
If correct the answer will be "9"
"""
print(pow(3, 2))


"""
Max Function
Finds the largest (maximum) of two values given
Define "max()" and place the values inside the brackets (parentheses) with commas to separate
If correct the answer will be "12"
"""
print(max(6, 12))

"""
Min Function
Finds the smallest (minimum) of two values given
Define "min()" and place the values inside the brackets (parentheses) with commas to separate
If correct the answer will be "2"
"""
print(min(2, 13))

"""
Round Function
Finds the rounded off value of a given decimal point number
Define "round()" and place values inside the brackets (parentheses) with commas to separate
Anything before .5 of a value will be a smaller value
and anything after .5 will be a higher value
If correct the answer in the first code the will be "3"
If correct the answer in the second code will be "4"
"""
print(round(3.2))
print(round(3.5))

"""
Floor Function
Finds the smallest value inside a given decimal point number
Define "floor()" and place values inside the brackets (parentheses) with commas to separate
If value is "3.5" then the output value will be "3"
"""
print(floor(3.5))

"""
Ceil Function
Does the same function as the Round Function
Define "ceil()" and place values inside the brackets (parentheses) with commas to separate
If correct the answer will be "4"
"""
print(ceil(3.5))

"""
Square Function
Finds the square root of given values
Define "sqrt()" and place values inside the brackets (parentheses) with commas to separate
Answer will be given back as a decimal point number
If correct the answer will be "6.0"
"""
print(sqrt(36))

# Program end
