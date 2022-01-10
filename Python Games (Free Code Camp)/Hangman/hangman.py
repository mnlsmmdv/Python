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
# Importing module.
import string

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
    # Returned words will be in uppercase.
    return word.upper()

# This will check the validity of words.
def hangman():
    # This will store valid words from the random selection.
    word = get_valid_word(words)
    # This will save all the letters in a word.
    word_letters = set(word)
    # This will set letters in uppercase as in the dictionary.
    alphabet = set(string.ascii_uppercase)
    # Keeps track of user's guess.
    used_letters = set()
    # The amount of lives a user has.
    lives = 6

    # Getting the user's initial input.
    # Will keep iterating if the word letters and lives are greater than 0.
    while len(word_letters) > 0 and lives > 0:
        # Letters used.
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # Checks what the current word is.
        # (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        # Checked word will be added to word list.
        print('Current word: ', ' '.join(word_list))

        # Asks the user to guess a letter.
        # User's guess will be turned to uppercase.
        user_letter = input('Guess a letter: ').upper()
        


# Program end.
