"""
Name: Ahmed Affaan                                  
Title: lists.py                                     
Date: 17/09/2021                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description: Lists creation and modification        
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start

# List declaration
# Note: Booleans can be placed inside lists as well
friends = ["Karen", "Karen", "Jim", "Oscar", "Toby"]

# Code below prints the whole list as declared above in square brackets
print(friends)

"""
Code below accesses the list to a specific index
Lists starts from index 0
Define list variable name + [] and place the index you want given out inside the square brackets
Code one executes a normal index print from a list
Code two executes indexes with negative values
"""
print(friends[0])
# If correct code below will show "Jim"
print(friends[-1])

# Code below selects and prints starting specific index following a range
# Define list variable + [] and place index + : to specify index you want
print(friends[1:])
# Code below selects only specific indexes
print(friends[1:3])

# Modifying index
# This will change value of index 1
friends[1] = "Affaan"
print(friends[1])

# Program end
