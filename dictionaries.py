#######################################################
# Name: Ahmed Affaan                                  #
# Title: dictionaries.py                              #
# Date: 29/09/2021                                    #
# Country: Maldives                                   #
# Description: -                                      #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start

# Declare a dictionary similar as so "monthConversion = {} "
# Data (keys) and key values pairs of a dictionary are all stored inside the curly brackets
monthConversions = {

# Now we create the key value pairs and associate the keys
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

}

# Printing the dictionary values
# The code below will print the correct dictionary value

getKey = input("Input the value you want: ")
if getKey == "Jan" or "January":
    print(monthConversions["Jan"])
elif getKey == "Feb" or "February":
    print(monthConversions["Feb"])
elif getKey == "Mar" or "March":
    print(monthConversions["Mar"])
elif getKey == "Apr" or "April":
    print(monthConversions["Apr"])
elif getKey == "May" or "May":
    print(monthConversions["May"])
elif getKey == "Jun" or "June":
    print(monthConversions["June"])
elif getKey == "Jul" or "July":
    print(monthConversions["Jul"])
elif getKey == "Aug" or "August":
    print(monthConversions["Aug"])
elif getKey == "Sept" or "September":
    print(monthConversions["Sept"])
elif getKey == "Nov" or "November":
    print(monthConversions["Nov"])
elif getKey == "Dec" or "December":
    print(monthConversions["Dec"])
else:
    print("Incorrect value or not found!!!")
# Program end
