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
Master Password: test
Account Name: admin
Password: test@321
"""

# Program start.

# Module used for text encryption.
from cryptography.fernet import Fernet

"""
These functions will fudge the master password using the
key. Key + Password needed to decrypt the text.
---------------------------------------------------------- 
"""
# Uncomment from below.
"""
# This function will help generate the keys.
def write_key():
    # Assigning text encryption method.
    key = Fernet.generate_key()
    # This will generate a new key file.
    # "wb" means "write byte mode".
    with open("./Python Mini Projects (Tech With Tim)/password_manager/" + "key.key", 'wb') as key_file:
        # Writes the data to the generated key file.
        key_file.write(key)

# Calling the function.
write_key()
"""

# This function will help load the keys.
def load_key():
    # Loads the generated key file.
    # "rb" means "read bytes".
    file = open("./Python Mini Projects (Tech With Tim)/password_manager/" + "key.key", 'rb')
    # Reads contents of key file.
    key = file.read()
    # Closes the read file method.
    file.close()
    # Returns the key file contents.
    return key

# Asks the user to enter a master password.
master_pwd = input("What is the master password?: ")
# Calling the function.
key = load_key()
# Initialising the encryption module.
fer = Fernet(key)

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
        # Will go to a new line after writing a new password.
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
            print("User:", user, "| Password:", passw)
            
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
