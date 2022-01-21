"""
Name: Ahmed Affaan                                  
Title: guessing_game.py                             
Date: 17/10/2021                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description: While Loop basics                      
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start

# Variable that will store the secret word
secret_word = "giraffe"

# Variable that will store the user response
# Note: Variable's value kept empty to keep incoming response
user_guess = ""

# Variable that will count the amount of user guesses
# Note: Variable value kept as 0 default starting value
user_guess_count = 0

# Variable declared that will limit the amount of guesses from the user
# Note: Variable value changed to 3 to indicate the amount of guesses allowed
user_guess_limit = 3

# Variable declared that will validate if user has used up the guess limit
# Note: Variable value kept as a Boolean value as starting value. When the
#       variable is True the program will terminate and the user will use
user_guess_limit_verify = False

# While loop implemented to urge the user to guess until they guess it correct
while user_guess != secret_word and not (user_guess_limit_verify):

    # If loop implemented to check if user has not exceeded guess limit
    if user_guess_count < user_guess_limit:

        # Empty variable declared above now implemented as a input function
        user_guess = input("Enter Guess: ")

        # Variable will increment each time a user has guessed
        user_guess_count += 1

    # If user has exceeded the guess limit given they will get no more guesses
    else:
        user_guess_limit_verify = True

# If loop implemented to print win and lost statements
# If the user has lost then a lost statement is printed out
if user_guess_limit_verify:
    # Empty print statement given for one line after spacing
    print("")

    # Message declared when the user has guessed correctly
    print("Maximum guesses reached, YOU LOST!")

# If the user has won a win statement will be printed out
else:
    print("YOU WON!")

# Program end
