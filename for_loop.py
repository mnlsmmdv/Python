#######################################################
# Name: Ahmed Affaan                                  #
# Title: for_loop.py                                  #
# Date: 21/10/2021                                    #
# Country: Maldives                                   #
# Description: For Loop basics                        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start

# Array created to store the values of friends for the for loops below
friends = ["Jim", "Karen", "Kevin"]

"""
# For loop implemented to print each letter during each iteration
for letters in "Giraffe Academy":

    # Printing out the letters one by one as it is included with the space
    print(letters)

    # Empty print statement given for one line spacing
    print("")

"""

"""
# For loop implemented to print each word from an array
for friend in friends:
    print(friend)
    
"""

"""
# For loop implemented with range function to print the integer values 0-9 by passing single digit range
for index in range(10):

    # Printing out the range of integers
    print(index)
    
"""

"""
# For loop implemented with range function to print even more specific range (3-9)
for index in range(3, 10):

    # Printing out the range of integers
    print(index)

"""

"""
# For loop implemented to print out the values using range and length function
for index in range(len(friends)):
    print(friends[index])
"""

#
for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")


# Program end
