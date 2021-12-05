#######################################################
# Name: Ahmed Affaan                                  #
# Title: reading_files.py                             #
# Date: 18/11/2021                                    #
# Country: Maldives                                   #
# Description: Understanding how to read file content #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start

# "r" is defined because we only want to read contents of the file and not modify it.
employee_file = open("employees.txt", "r")

# Print statement which a functionality that will verify if the file is readable.
# If readable True and if not readable it will be False.
print(employee_file.readable())
# Empty print statement given for spacing.
print("")

# Print statement that will read the contents of the file and display it.
#print(employee_file.read())
# Empty print statement given for spacing.
#print("")

# Print statement that will read specific lines and will display them.
# By default this will read the contents of the first line of a file.
print(employee_file.readline())
# Empty print statement given for spacing.
print("")

# Program end
