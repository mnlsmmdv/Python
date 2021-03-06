"""
Name: Ahmed Affaan                                  
Title: file_extension_getter.py                     
Folder: Modules & Pip                               
Date: 14/12/2021                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description:                                        
Note: Uncomment codes to execute and comment        
them when not in use.                         
"""

# Program start.

# Importing file as a module.
import useful_tools

# Getting input from user (File Type)
user_input = input("Enter file type: ")

# Printing the file type extension
print("The file type extension is: " + useful_tools.get_file_ext(user_input))

# Program end.
