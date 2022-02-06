"""
Name: Ahmed Affaan                                  
Title: car.py                                 
Date: 07/02/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description:                                        
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start.

# Main class.
class Car:

    # Cars functions.
    # Constructor.
    def __init__(self, make, model, year, colour):
        # Cars attributes.
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    # Cars drive function.
    def drive(self):
        # Prints message of cars function.
        print("This " + self.model + " is driving")

    # Cars stop function.
    def stop(self):
        # Prints message of cars function.
        print("This car is stopped")

# Program end.
