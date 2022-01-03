##################################################
# Name: Ahmed Affaan                             #
# Title: strings.py                              #
# Date: 15/09/2021                               #
# Country: Republic of Maldives                  #
# Code version: 3.8.10                           #
# Description: String creation and manipulation. #
# Note: Uncomment codes to execute and comment   #
#       them when not in use.                    #
##################################################

# Program start

# Normal string
print("Giraffe Academy")

# This string prints into a new line
print("Giraffe\nAcademy")

# Prints out a single quotation mark
print("Giraffe\"Academy")

# Prints out a single backslash
print("Giraffe\Academy")

# Printing a string variable
# String variable creation
phrase = "Ahmed Affaan"
print(phrase)

# String concatenation
print(phrase + " is bald.")

"""
String functions.
Add "." after adding string variable.
Code below makes code lower case
"""
print(phrase.lower())

# Code below makes code uppercase
print(phrase.upper())

# Code below checks if all characters are lower
# If all is lower it will comes at True (T) if not False (F)
print(phrase.islower())

# Code below checks if all characters are upper case
# If all is upper it will come as True (T) if not False (F)
print(phrase.isupper())

# Changing string fully to uppercase and checking if it is
# If it has been changed to uppercase it will come as True (T) if not False (F)
print(phrase.upper().isupper())

# Changing string fully to lowercase and checking if it is
# If it has been changed to lowercase it will come as True (T) if not False (F)
print(phrase.lower().islower())

"""
Checks the length of a given function.
Counts the number of characters inside a string variable.
The answer will be "12".
"""
print(len(phrase))

# Character location (Index)
# Checks string character location and states what it is
print(phrase[0])

"""
Finds exact index.
The answer will be "1".
Note that empty spaces also hold the index.
"""
print(phrase.index("h"))

# Finding exact index (Words)
# The answer will be "6"
print(phrase.index("Affa"))

"""
Replaces items in string variable in print statement.
First quotation specifies what needs to changed
Second quotation mark is what will be replaced with as.
"""
print(phrase.replace("Ahmed", "LOL"))


"""
Checks for character index.
Gives back an error cause the string character does not exist.
Uncomment code to execute.
"""
#print(phrase.index("z"))

# Program end
