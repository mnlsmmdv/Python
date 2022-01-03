#######################################################
# Name: Ahmed Affaan                                  #
# Title: list_functions.py                            #
# Date: 17/09/2021                                    #
# Country: Republic of Maldives                       #
# Code version: 3.8.10                                #
# Description: Lists creation and modification        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start

# Variable declaration for lists
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Affaan", "Karen", "Jim", "Oscar", "Toby", "Affaan"]
# Printing the list
print(friends)

"""
Extend function
Adding a list to another to append
List the default list name + ".extend()" and place the list to add in the brackets (parentheses)
"""
#friends.extend(lucky_numbers)
# Now when you print it will have values from the list you added in the default list
print(friends)

# Adding individual elements to a list
# Using the ".append()" function to add a new item to the list
friends.append("Mary")
print(friends)
# Now when you print "Mary" will be added to the most end of the list
# The list will now be printed whole with a new appended item
print(friends)

"""
Inserting new item to specific index in a list
Two parameters will be needed to change this new insert. The index you want to change + the item to be added
As seen below the code will insert the new element to index 1 of the list
"""
friends.insert(1, "bobo")
print(friends)

"""
Removing an element - Remove Function
Removing a function in a specific index
To remove a specific index we will define ".remove()" and add the index which you want to remove
Code below will remove "bobo"
"""
friends.remove("bobo")
print(friends)

# To fully clear a list uncomment the code below
# This deletes all the elements inside the list
#print(friends.clear())


"""
Clear Function -Removing all elements inside a list
To remove all elements from a specific list define list name + ".clear()"
This will clear all the elements inside the whole list.
Uncomment codes to execute and comment it again when not in use.
"""
#friends.clear()
#print(friends)

"""
Pop Function
Removes the most last element off a list
Doing this if the code is correct it will remove "Mary" from the list
"""
friends.pop()
print(friends)

# Find index number of list item
# If code correct will give off as index "1"
print(friends.index("Karen"))

# When we insert to check index of an unknown list item will give off an error
# Uncomment code to execute and comment after execution check
#print(friends.index("Bobo"))

# Counting same elements inside list
#print(friends.count("Affaan"))

# Sort and Reverse Function
# Sorts and reverses list items
friends.sort()
lucky_numbers.reverse()
print(friends)
print(lucky_numbers)

# Copy Function
# Now we have created a brand new list as a copy of the old one referenced
# Uncomment code to execute
friends2 = friends.copy()
print(friends2)

# Program end
