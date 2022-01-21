"""
Name: Ahmed Affaan                                  
Title: try_except.py                                
Date: 18/11/2021                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description: Understanding how to catch errors.     
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start

"""
try:
    # Creating a variable that accepts an integer input from the user
    number = float(int(input("Enter a number: ")))

    # This print function will print out the integer number that was recieved.
    # The print function is executed with a quoted statement with spacing.
    print(number)

except:
    # Empty print statement given before the invalid input statement to give spacing
    print("")

    # This will print out a statement if the user does not enter a float
    print("The input you gave is invalid!")
"""

# This code block will check how the "ZeroDivisionError" and "ValueError" is implemented in a basic manner.
# Uncommenting code below and running it will give a "ZeroDivisionError"
# Any value can not be divisible by zero.
"""
try: 
    # Uncommenting the code below will give a "Invalid Input" as shown in the except portion because there is no except specified.
    # "ValueError"
    value = 10 / 0

    # Creating variable that accepts an integer input from the user.
    number = float(int(input("Enter a number: ")))

    # This print function will print out the integer number that was recieved.
    # The print function is executed with a quoted statement with spacing.
    print(number)

# This except block is for the "ZeroDivisionError"
except ZeroDivisionError as err:
    # Empty print statement given before the print statement to give spacing.
    print("")

    # Print statement for the error.
    print("Zero Division Error!")

    # Print statement which directly prints out error type.
    print(err)

# This except block is for the "ValueError"
except ValueError as err:
    # Empty print statement given before the print statement to give spacing.
    print("")

    # Print statement for the error.
    print("Value Error!")

    # Print statement which directly prints out error type.
    print(err)
"""

# Program end
