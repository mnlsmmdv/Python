"""
Name: Ahmed Affaan                                  
Title: greatest_common_divisor.py                   
Date: 15/11/2021                                    
Country: Maldives
Code version: 3.8.10                                    
Description:                                        
Note: Uncomment codes to execute and comment        
them when not in use.                         
"""

# Program start

# Function declared with parameters as variables to check the GCD
# Passes two variables x and y
def greatest_common_divisor (x, y):
    # If y is equal to 0 it will give out the x's value
    if y == 0:
        return x
    else:
        # If x is not equal to 0 it will calculate the GCD
        return greatest_common_divisor(y, x % y)

# Accepting input from the user for input field 01
input_one = int(input("Enter value 01: "))

# Accepting input from the user for input field 01
input_two = int(input("Enter value 02: "))

# Checks if "input_two" is equal to 0 if not prints out the GCD
if input_two == 0:
    print(input_one)
else:
    print(greatest_common_divisor(input_one, input_two))

# Program end
