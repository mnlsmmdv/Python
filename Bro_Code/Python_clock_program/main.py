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

# Window initialization.
window = Tk()
# Window title.
window.title("Clock")

# Label for time.
time_label = Label(window, font=("Ariel", 50), fg="#42ada6", bg="#111111")
time_label.pack()

# Calling the update time function.
update()

# Label for day of the week.


# Label for date.


# Window initialization end.
window.mainloop()

# Program end.
