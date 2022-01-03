#######################################################
# Name: Ahmed Affaan                                  #
# Title: calculator.py                                #
# Date: 29/09/2021                                    #
# Country: Republic of Maldives                       #
# Code version: 3.8.10                                #
# Description: -                                      #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start
# Calculator program which functions all 3 major arithmetic functions
# Declaring 3 variables
num1 = float(input("Enter number 1: "))
operator = input("Enter operator: ")
num2 = float(input("Enter number 2: "))

# If statement declared to check number by operator
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("INVALID OPERATION!!!")


# Program end
