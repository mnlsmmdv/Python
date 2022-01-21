"""
Name: Ahmed Affaan                                  
Title: prime_numbers_two.py                         
Date: 15/11/2021                                    
Country: Maldives                                   
Description:                                        
Note: Uncomment codes to execute and comment
them when not in use.                         
"""

# Program start

# Variable set up to get user input that also changes its data type
prime_number_input = int(input("Enter a number: "))

# Flag set as a pointer
flag = 0

for i in range (2, prime_number_input):
    # If statement declared where it uses the modular operator to find the divisor and checks if it is equal to 0
    if (prime_number_input % i == 0):
        # If it is the flag is now set to 1 and breaks the code
        flag = 1
        break

# If statement declared to check the flag if it is equal to 0. If it is it's a Prime Number and if not it isn't
if (flag == 0):
    print(prime_number_input, " is indeed a Prime Number")
else:
    print(prime_number_input, " is not a Prime Number :(")

# Program end
