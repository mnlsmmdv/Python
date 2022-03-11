"""
Name: Ahmed Affaan                                  
Title: appending_files.py                           
Folder: File Manipulation                           
Date: 12/12/2021                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description: Understanding how to append to files   
Note: Uncomment codes to execute and comment        
them when not in use.                         
"""

# Program start.

# "a" is defined because we only want to append contents to a new/current file.
# Giving an unknown file name will generate that new file in the program folder.
employee_file = open("employees_two.txt", "a")

# Print statements declared to append new data to files.
employee_file.write("\nAhmed Affaan - CTO")
employee_file.write("\nAhmed Affaan - Designer") 

# Closing the variable created generally to read/write and append the file.
employee_file.close()

# Program end.
