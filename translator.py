#######################################################
# Name: Ahmed Affaan                                  #
# Title: translator.py                                #
# Date: 14/11/2021                                    #
# Country: Maldives                                   #
# Description: Basic translator in Python             #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start

# Defining a translate function
def translate(phrase):

    # Variable declared that will return the translation
    # Variable kept empty cause no values are passed
    translation = ""

    # For Loop declared to loop through. If it's a vowel it will translate, if it's not it will be kept the same.
    for letter in phrase:
        # If there is a specified letter as shown below it is a vowel and will add a "g" where ever the letter is
        if letter in "AEIOUaeiou":
            # Validating if the translation variable passed has a vowel. If it does passes a "g"
            translation = translation + "g"

        # If the input phrase is not a vowel it will print out as normal
        else:
            # If there is no vowel in the phrase passed the phrase will be kept the same
            translation = translation + letter

    # Returning the translation if all the conditions are met
    return translation

# Print statement will accept the input phrase and print out the translation right after it below
print(translate(input("Enter a phrase: ")))

# Program end
