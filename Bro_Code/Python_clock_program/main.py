"""
Name: Ahmed Affaan                                  
Title: main.py
Folder: Python_clock_program                            
Date: 23/03/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description:                                        
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start.

# Importing modules.
from tkinter import *
from time import *

# This function will update the time.
def update():
    # Assigning string to time function.
    time_string = strftime("%I:%M:%S %p")
    # Updating the time label.
    time_label.config(text=time_string)

# Initializing the window.
window = Tk()
# Window title.
window.title("Clock")

# Label to display time.
time_label = Label(window, font=("Ariel", 50), fg="#00FF00", bg="#000000")
time_label.pack()

# Recursive function to update the time.
update()

# Label to display day of the week.


# Label to display date.


# Closing the window.
window.mainloop()

# Program end.
