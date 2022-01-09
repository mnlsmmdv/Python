#######################################################
# Name: Ahmed Affaan                                  #
# Title: hangman.py                                   #
# Folder: Hangman                                     #
# Date: 08/01/2022                                    #
# Country: Republic of Maldives                       #
# Code version: 3.8.10                                #
# Description:                                        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start.

# Importing module to use random values.
import random
# Importing entire file as a module.
from words import words

# This print statement will test if the word list displays.
#print(words)

# This will go through until we get a valid word from the word list.
# The parameter will be the list of words.
def get_valid_word(words):
    # Assigning the word to random selection and word list.
    word = random.choice(words)

    # While a "-" is in the word list this will iterate.
    while '-' in word or ' ' in word:
        # Iterates and give back random words until condition is met.
        word = random.choice(words)

    # When conditions have been met will return a word.
    # Returned words will be uppercase.
    return word

# Program end.
