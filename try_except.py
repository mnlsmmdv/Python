#######################################################
# Name: Ahmed Affaan                                  #
# Title: try_except.py                                #
# Date: 18/11/2021                                    #
# Country: Maldives                                   #
# Description: Understanding how to catch errors.     #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start

try:
    # Creating a variable that accepts an integer input from the user
    number = float(int(input("Enter a number: ")))

    # This print function will print out the integer number that was recieved.
    # The print function is executed with a quoted statement with spacing.
    print(number)

except:
    # Empty print statement given before the invalid input statement to give spacing
    print("")
    # This will print out a statement if the user does not enters a float
    print("The input you gave is invalid!")


# Program end
