"""
Name: Ahmed Affaan                                  
Title: main.py
Folder: Python_clock_program                            
Date: 23/03/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description: Simple clock GUI in Python.                                        
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start.

# Importing modules.
from tkinter import *
from time import *

# This function will update the time.
def update_clock():
    # Calling the get time function.
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    # Calling the get day function.
    day_string = strftime("%A")
    day_label.config(text=day_string)

    # Calling the get date function.
    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    # Updates label every one second.
    window.after(1000, update_clock)

# Window initialization.
window = Tk()
# Window title.
window.title("Clock")
# Window background colour.
window.configure(bg="#111111")

# Label for time.
time_label = Label(window, font=("Monospace", 50), fg="#42ada6", bg="#111111")
time_label.pack()

# Label for day of the week.
day_label = Label(window, font=("Monospace", 50), fg="#42ada6", bg="#111111")
day_label.pack()

# Label for the date.
date_label = Label(window, font=("Monospace", 50), fg="#42ada6", bg="#111111")
date_label.pack()

# Calling the update time function.
update_clock()

# Window initialization end.
window.mainloop()

# Program end.
