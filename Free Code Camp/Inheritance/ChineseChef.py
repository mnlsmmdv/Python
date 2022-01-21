"""
Name: Ahmed Affaan                                  
Title: ChineseChef.py                                       
Folder: Inheritance                                 
Date: 03/01/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description:                                        
Note: Uncomment codes to execute and comment        
them when not in use.                         
"""

# Program start.

# Importing the Chef class from Chef the file.
from Chef import Chef

# Program's main class.
# This class describes the function of a Chinese Chef.
# The Chinese Chef can do what a normal Chef does and even more.
class ChineseChef(Chef):
    # Function to describe a chef's specific job.
    # This will override the special dish in Chef class.
    def make_special_dish(self):
        # Describes what exactly the chef does.
        print("The chef makes orange chicken")
    
    # Function to describe a chef's specific job.
    def make_fried_rice(self):
        # Describes what exactly the chef does.
        print("The chef makes fried rice")

# Program end.
