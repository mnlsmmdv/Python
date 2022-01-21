"""
Name: Ahmed Affaan                                  
Title: if_statement_and_comparisons.py              
Date: 29/09/2021                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description: -                                      
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start
#
"""
This program will use comparisons instead of boolean values to compare different values. A new function will be created.
This will give out the maximum number passed into it. It inputs 3 numbers and gives back biggest number out of 3.
"""
# Defining we want 3 numbers in the parameters
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Printing out the result of the function
print(max_num(300, 4, 5))

# Program end
