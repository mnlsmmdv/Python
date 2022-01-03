##################################################
# Name: Ahmed Affaan                             #
# Title: user_input.py                           #
# Date: 16/09/2021                               #
# Country: Republic of Maldives                  #
# Code version: 3.8.10                           #
# Description: User input and modification       #
# Note: Uncomment codes to execute and comment   #
#       them when not in use.                    #
##################################################

# Program start
# Getting simple input from a user
# "input("")" is defined as the input prompt
"""
Getting simple input from a user
Define "input("")" and place your message to get input within the quotation marks
Uncomment first code to execute and check
Uncomment second code to execute and check
In the second code the input prompt is placed within a variable container
"""
#input("Enter your name: ")
name = input("Enter your name: ")
age = input("Enter your age: ")

# Printing out the user input
# This will print out a message + the user input we got
print("Your name is " + name + ", and your age is " + str(age) + " years old.")

# Simple calculator program example
num1 = input("Enter number 01: ")
num2 = input("Enter number 02: ")
result = int(num1) + int(num2)
# The same code above and below can be used for multiplication, division and subtraction
# String concatenation is used to change data type temporarily
print("The answer is = " + str(result))

# Program end
