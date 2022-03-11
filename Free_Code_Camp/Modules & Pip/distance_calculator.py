"""
Name: Ahmed Affaan                                  
Title: distance_calculator.py                       
Folder: Modules & Pip                               
Date: 19/12/2021                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description:                                        
Note: Uncomment codes to execute and comment        
them when not in use.                         
"""

# Program start.

# Importing file as a module.
import useful_tools

# Variable declaration Miles in Feet.
miles_in_feet = 5280
# Variable declaration Kilometers in Meters.
kilometers_in_meters = 1000

# Giving user broad choices.
print("Please select desired operation!")
print("--------------------------------")
print("1. Miles to Feet")
print("2. Kilometers to Meters")
print("--------------------------------")

# Take input from the user 
user_choice = input("Enter Choice, 1 or 2: ")
user_input = float(input("Enter Number: "))

# Check if choice is suitable.
if user_choice in ('1', '2'):

    if user_choice == '1':
        print(str(user_input) + " Miles in Feet is: " + str(user_input * miles_in_feet) + " Feet")

    elif user_choice == '2':
        print(str(user_input) + "Kilometers in Meters is: " + str(user_input * kilometers_in_meters) + " Meters")

    else:
        print("Invalid Input")
        

# Program end.
