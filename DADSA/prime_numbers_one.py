"""
Name: Ahmed Affaan                                  
Title: prime_numbers_one.py                         
Date: 15/11/2021                                    
Country: Maldives                                   
Description:                                        
Note: Uncomment codes to execute and comment
them when not in use.                         
"""

# Variable declared that accepts an input and also changes its data type
prime_number = int(input("Enter any number: "))

# If Loop initialized to check if the number given is a prime number
if prime_number > 1:
    # For Loop initialised to check the prime number within a range
    for i in range(2, prime_number):
        # If the input value after dividing is equal to validation
        if prime_number % i == 0:
            # If it is not a prime number it prints this
            print(prime_number, " is not Prime Number :(")
            break
        else:
            print(prime_number, " is indeed a Prime Number!")
            break

# If upper validations are not correct the one below prints out that is not a prime number as well
else:
    print(prime_number, " is not a Prime Number :(")