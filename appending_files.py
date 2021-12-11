#######################################################
# Name: Ahmed Affaan                                  #
# Title: appending_files.py                           #
# Date: 12/12/2021                                    #
# Country: Reublic of Maldives                        #
# Code version: 3.8.10                                #
# Description: Understanding how to append to files   #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start.

# "a" is defined because we only want to append contents to a new/current file.
# Giving an unknown file name will generate that new file in the program folder.
employee_file = open("employees_two.txt", "a")

# Closing the variable created generally to read/write and append the file.
employee_file.close()

# Program end.
