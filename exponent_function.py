#######################################################
# Name: Ahmed Affaan                                  #
# Title: exponent_function.py                         #
# Date: 09/11/2021                                    #
# Country: Maldives                                   #
# Description: Exponent Function in Python            #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start

"""
# The method below is the easiest way to calculate the exponent function in Python
# This is the same as 2^3 (two cube)
print(2 ** 3)
Maldives National Defence Force
"""

# Function created  to calculate the exponent function
def to_the_power(base_number, power_number):
    # Variable created to store the result
    result = 1
    
    # For Loop created to loop through until the cube value is found
    for index in range(power_number):
        
        # Calculating the result until it hits the cube value
        result = result * base_number

    # returning the answer that was calculated    
    return result

# Printing the answer
print(to_the_power(3, 4))
# Test comment


# Program end
