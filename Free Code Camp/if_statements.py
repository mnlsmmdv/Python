#######################################################
# Name: Ahmed Affaan                                  #
# Title: if_statement.py                              #
# Date: 21/09/2021                                    #
# Country: Reublic of Maldives                        #
# Code version: 3.8.10                                #
# Description: -                                      #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start
# Creation of Boolean variable to check gender
is_Male = True
is_Tall = False

# If-Statement to check gender
"""
if is_Male:
    print("You are a male.")
else:
    print("You are not a male.")
"""

# Checks gender and height to confirm with OR operator
"""
if is_Male or is_Tall:
    print("You are a male or tall or both.")
else:
    print("You are neither male nor tall.")
"""

# Checks gender and height to confirm with AND operator
# Once Boolean values change it will become either True or False
"""
if is_Male or is_Tall:
    print("You are a tall male.")
else:
    print("You are either not male or tall or both.")
"""

# Checks gender and height to confirm using AND and OR operator
# Code below uses conditions in placed in brackets (parantheses)
if is_Male or is_Tall:
    print("You are a tall male.")
elif is_Male and not (is_Tall):
    print("You are a short male.")
elif not (is_Male) and is_Tall:
    print("You are not a male but are tall.")
else:
    print("You are either not male or tall or both.")
# Program end
