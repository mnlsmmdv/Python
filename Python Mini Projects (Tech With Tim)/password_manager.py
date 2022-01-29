"""
Name: Ahmed Affaan                                  
Title: password_manager.py                                 
Date: 29/01/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description:                                        
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start.

# Asks the user a master password.
master_pwd = input("What is the master password?: ")

# Will keep iterating until True.
while True:
    # Giving the user choices. Add or View passwords.
    mode = input("Would you like to add or view existing passwords (add/view)? press q to quit: ").lower()

    # Checks what the user has chosen.
    # If the user has chosen add this will happen.
    if mode == "add":
        pass
    # If the user has chosen view this will happen.
    elif mode == "view":
        pass
    # If the user has given an invalid mode this will happen.
    else:
        # Error message.
        print("Invalid mode.")
        # Iterates the loop.
        continue
    
# Program end.
