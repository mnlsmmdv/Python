##################################################
# Author: Ahmed Affaan                           #
# Title:  strings.py                             #
# Status: 08/09/2021                             #
# Desc: String creation and modification         #
##################################################

# Prints values after the backslash n it into a new line using "\n"
print("Giraffe\nAcademy")

# Prints a single quotation mark using " \" "
print("Giraffe\"Academy")

# Prints a normal backslash inside the print statement
print("Giraffe\Academy")

# Creation of a string variable and insertion into print statement
phrase = "Giraffe Academy"
print(phrase)

# String concatenation - Temporarily changing data types
# Example 01
print(phrase + " is cool.")

# Function - Get info and modify function using " . "
# Example 02 - Converts everything to lower case
print(phrase.lower())

# Example 03 - Converts everything to upper case
print(phrase.upper())

# Example 04 - Checks if entire string is upper case and gives output with True or False
print(phrase.isupper())

# Example 05 - Checks if entire string is lower case and gives output with True or False
print(phrase.islower())


'''
Example 06 - Two functions used at the same time ex: uppercase + isupper.
By executing code below it first changes the whole string to uppercase and then checks if it is uppercase.
The answer will come as True if it is.
'''
print(phrase.upper().isupper())


# Checking length of a string or print statement using " len() "
# Print function is initialised to count the length of characters inside the string variable
print(len(phrase))

'''
 Character selection using " [] ".
 Character index's start always at 0 and not at 1.
 Giving character index it brings back the character value as output.
 Code below selects index 0 "G".
'''
print(phrase[0])

# Code below selects index 3 "a"
print(phrase[3])

# Index Function - Gives back exact location of string or index
print(phrase.index("G"))
print(phrase.index("a"))

'''
Can be used to locate words as well
Code below finds exact location where a specific character or string is located
This is called passing a parameter
Code below finds index of uppercase G which is index 0
'''
print(phrase.index("G"))

# Code below finds index of the given set of characters and where it starts off which is index 8
print(phrase.index("Acad"))

# When passed with value not present in string variable an error is given out
# Example 01 - Uncomment code to execute
#print(phrase.index("z"))

'''
Replace function - Can give two parameters
First give the characters you want to append. Then give it's replacement
Output now will be "Elephant Academy"
'''
print(phrase.replace("Giraffe", "Elephant"))
