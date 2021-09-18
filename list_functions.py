#######################################################
# Name: Ahmed Affaan                                  #
# Title: list_functions.py                            #
# Date: 17/09/2021                                    #
# Country: Maldives                                   #
# Description: Lists creation and modification        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start

# Variable declaration for lists
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Karen", "Karen", "Jim", "Oscar", "Toby"]
# Printing the list
print(friends)

"""
Extend function
Adding a list to another to append
List the default list name + ".extend()" and place the list to add in the brackets (parentheses)
"""
friends.extend(lucky_numbers)
# Now when you print it will have values from the list you added in the default list
print(friends)

# Adding individual elements to a list
# Using the ".append()" function to add a new item to the list
print(friends.append("Mary"))
# Now when you print "Mary" will be added to the most end of the list
# The list will now be printed whole with a new appended item
print(friends)

# Program end
