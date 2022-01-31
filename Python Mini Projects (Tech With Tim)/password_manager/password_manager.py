"""
Name: Ahmed Affaan                                  
Title: password_manager.py
Folder: password_manager                            
Date: 29/01/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description:                                        
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

### IMPORTANT ###
"""
Note: Use entries below as the test data.
------------------------------------------
Master Password: hello@123
Account Name: Aff
Password: hello@321
"""

# Program start.

# Asks the user to enter a master password.
master_pwd = input("What is the master password?: ")

# This will work out the add password function.
def add():
    # Asks the user for their account's name.
    name = input("Account Name: ")
    # Asks the user for their account's password.
    pwd = input("Password: ")

    # Creates a file and adds the passwords.
    # "a" means append.
    with open("./Python Mini Projects (Tech With Tim)/password_manager/" + "password.txt", 'a') as f:
        # Writes the new password.
        # Will now go to a new line after writing a new password.
        f.write(name + "|" + pwd + "\n")

# This will work out the view existing passwords function.
def view():
    # Creates a file and adds the password.
    # "r" means read.
    with open("./Python Mini Projects (Tech With Tim)/password_manager/" + "password.txt", 'r') as f:
        # Will read through the file's lines.
        for line in f.readlines():
            # Prints the lines it's read through.
            # Will split username and password.
            data = line.rstrip()
            # Splits the variables containing specific data.
            user, passw = data.split("|")
            # Printing the data in splitted format.
            print("User:", user, "Password:", passw)
            
# Will keep iterating until True.
while True:
    # Giving the user choices. Add or View passwords.
    mode = input("Would you like to add or view existing passwords (add/view)? press q to quit: ").lower()

    # This will check if the user chose to quit.
    if mode == "q":
        # Breaks out of the program.
        break

    # Checks what the user has chosen.
    # If the user has chosen add this will happen.
    if mode == "add":
        # Calling the function
        add()
    # If the user has chosen view this will happen.
    elif mode == "view":
        # Calling the function.
        view()
    # If the user has given an invalid mode this will happen.
    else:
        # Error message.
        print("Invalid mode.")
        # Iterates the loop.
        continue
    
# Program end.
