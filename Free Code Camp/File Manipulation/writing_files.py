#######################################################
# Name: Ahmed Affaan                                  #
# Title: writing_files.py                             #
# Folder: File Manipulation                           #
# Date: 11/12/2021                                    #
# Country: Republic of Maldives                       #
# Code version: 3.8.10                                #
# Description: Understanding how to write to files    #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start.

# "w" is defined because we only want to write contents to a new/current file.
# Giving an unknown file name will generate that new file in the program folder.
employee_file = open("employees_one.txt", "w")

# This will write new content on to our new file.
employee_file.write("Toby - Human Resources")
# This will add a second line to our new file.
employee_file.write("\nKelly - Public Relations")
# This will add a third line to our new file.
employee_file.write("\nMohamed - DevOps")
# This will add a fourth line to our new file.
employee_file.write("\nHashim - Designer")
# This will add a fifth line to our new file.
employee_file.write("\nMicheal - CTO")

# Closing the variable created generally to read/write the file.
employee_file.close()

# Program end.
