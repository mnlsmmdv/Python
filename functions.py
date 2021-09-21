#######################################################
# Name: Ahmed Affaan                                  #
# Title: functions.py                                 #
# Date: 20/09/2021                                    #
# Country: Maldives                                   #
# Description: Functions creation and modification    #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start

"""
Creating a Function
We use the Python related keyword: "def" + name.
Function can be created as follows: "def affaan():".
Code will only work if there is indentation after declaring a function.
For a function to work after declaration it needs to be called or else a blank output screen will be displayed.
Code below after function declaration it is being called as: "{Function Name}()". Indentation is not needed.
"""
def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))

# Calls the function we created above
#sayhi()

# Calls the function created above + example of using print statements
print("Top")
# When the function is called it goes back to the function declaration to get the data stored in the function
#say_hi()
#print("Bottom")

# Code below will call a function once a name is given
say_hi("Ahmed", 22)
say_hi("Affaan", 22)

# Program end
