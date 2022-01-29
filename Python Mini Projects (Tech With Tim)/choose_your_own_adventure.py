"""
Name: Ahmed Affaan                                  
Title: choose_your_own_adventure.py                                 
Date: 29/01/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description:                                        
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start.

# Asks for the user's name.
name = input("Type your name: ")

# Welcoming the user.
print("Welcome", name, "to this adventure!")

# Giving the user choices.
answer = input("You are on a dirt road, it has come to an end and you can go left and right. Which way would you like to go?: ").lower()

# Checks what choice the user has chosen.
# If the user chose left this will happen.
if answer == "left":
    # Giving the user choices.
    answer = input("You've come to a river, you can walk around it or swim across. Type walk to walk and swim to swim across: ").lower()

    # Checks what choices the user has chosen.
    # If the user chose to swim across it this will happen.
    if answer == "swim":
        # Tells the user outcome of their choice.
        print("You swam across and was eaten by an alligator!")
    # If the user chose to walk around it this will happen.
    elif answer == "walk":
        # Tells the user outcome of their choice.
        print("You walked for many miles, ran out of water and you lost the game.")
    # If the user has given an invalid choice this will happen.
    else:
        # Error message.
        print("Not a valid option. You lose!")

# If the user chose right this will happen.
elif answer == "right":
    # Giving the user choices.
    answer = input("You've come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)?: ").lower()
    
    # Checks what choices the user has chosen.
    # If the user chose to go back this will happen.
    if answer == "back":
        # Tells the user outcome of their choice.
        print("You go back, you lose!")
    # If the user chose to cross this will happen.
    elif answer == "cross":
        # Giving the user choices.
        answer = input("You cross the bridge and meet a stranger. Do you talk with them (yes/no)?: ").lower()

        # Checks what choices the user has chosen.
        # If the user chose yes this will happen.
        if answer == "yes":

        # If the user chose no this will happen.
        elif answer == "no":

        # If the user has given an invalid option this will happen.
        else:
            # Error message.
            print("Not a valid option. You lose!")
    # If the user has given an invalid option this will happen.
    else:
        # Error message.
        print("Not a valid option. You lose!")

# If the user has given an invalid choice this will happen.
else:
    # Error message.
    print("Not a valid option. You lose!")


# Program end.
