"""
Name: Ahmed Affaan                                  
Title: main.py                                 
Date: 07/02/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description:                                        
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start.

# Importing modules.
import tkinter
from tkinter import *

# This functions helps press buttons.
def button_press(num):
    # Temporary statement.
    pass

# This function calculates expressions.
def equals():
    # Temporary statement.
    pass

# This function clears the calculator.
def clear():
    # Temporary statement.
    pass

# Creating the main GUI window.
window = Tk()
# Window title.
window.title("Calculator")
# Size of the window.
window.geometry("500x500")

# Will display the equation.
equation_text = ""

# String variable.
equation_label = StringVar

# Adding label to the window.
label = Label(window, textvariable = equation_label, font = ("consolas", 20), bg = "white", width = 24, height = 2)
label.pack()

# Main frame to house GUI contents.
frame = Frame(window)
frame.pack()

# Button configurations.
# Button 1.
button1 = Button(frame, text = 1, height = 4, width = 9, font = 35, command = lambda: button_press(1))
button1.grid(row = 0, column = 0)

# Window end point.
window.mainloop()

# Program end.
