"""
 Name: Ahmed Affaan                                  
 Title: bubble_sort.py                               
 Date: 29/09/2021                                    
 Country: Republic of Maldives                       
 Code version: 3.8.10                                
 Description:                                        
 Note: Uncomment codes to execute and comment        
       them when not in use.                         
"""

# Program start

# Importing the needed modules
import math

# Defining the main function
# Within the parameters the variable that will be returned is declared
def bubble_sort (sort):

    # Boolean value assigned which starts off as False
    bubble = False

    # Variable defined where it's value is calculated by substracting one incrementation from the Sort variable
    flag = len(sort) - 1

    # If the number sets are not arranged correctly it go through this until all of it gets arranged
    while not bubble:

        # This makes the Boolean value which was False before True because the numbers aren't flipped correctly
        bubble = True

        # Range starts from 0 to the amount of the flag calculated value
        for j in range (0, flag):

            # If the value on the left is greater than the value on the right it needs to be flipped
            if sort[j] > sort[j + 1]:

                # Now the Boolean value becomes False to do the flipping of values
                bubble = False

                # Defines that cause the value on the left is greater than the right so it needs to be flipped after the equal sign
                # Flipping is done easily where the greater value is pushed to the right side and the lesser value is pushed to the left
                sort[j], sort[j + 1] = sort[j + 1], sort[j]
    
    # When all the conditions have been met and the values have been checked it will return the flipped number set
    return sort

# The Bubble Sort implementation will run through this number set and re-arrange everything in the correct order
print(bubble_sort([10, 17, 18, 15, 13, 12, 19, 20, 14, 16, 11]))

# Program end
