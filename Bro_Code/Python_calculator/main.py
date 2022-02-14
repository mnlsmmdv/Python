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
window.geometry("500x550")

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

# Button 2.
button2 = Button(frame, text = 2, height = 4, width = 9, font = 35, command = lambda: button_press(2))
button2.grid(row = 0, column = 1)

# Button 3.
button3 = Button(frame, text = 3, height = 4, width = 9, font = 35, command = lambda: button_press(3))
button3.grid(row = 0, column = 2)

# Button 4.
button4 = Button(frame, text = 4, height = 4, width = 9, font = 35, command = lambda: button_press(4))
button4.grid(row = 1, column = 0)

# Button 5.
button5 = Button(frame, text = 5, height = 4, width = 9, font = 35, command = lambda: button_press(5))
button5.grid(row = 1, column = 1)

# Button 6.
button6 = Button(frame, text = 6, height = 4, width = 9, font = 35, command = lambda: button_press(6))
button6.grid(row = 1, column = 2)

# Button 7.
button7 = Button(frame, text = 7, height = 4, width = 9, font = 35, command = lambda: button_press(7))
button7.grid(row = 2, column = 0)

# Button 8.
button8 = Button(frame, text = 8, height = 4, width = 9, font = 35, command = lambda: button_press(8))
button8.grid(row = 2, column = 1)

# Button 9.
button9 = Button(frame, text = 9, height = 4, width = 9, font = 35, command = lambda: button_press(9))
button9.grid(row = 2, column = 2)

# Button 10.
button10 = Button(frame, text = "+", height = 4, width = 9, font = 35, command = lambda: button_press(10))
button10.grid(row = 3, column = 0)

# Button 11.
button11 = Button(frame, text = "-", height = 4, width = 9, font = 35, command = lambda: button_press(11))
button11.grid(row = 3, column = 1)

# Button 12.
button12 = Button(frame, text = "*", height = 4, width = 9, font = 35, command = lambda: button_press(12))
button12.grid(row = 3, column = 2)

# Button 13.
button13 = Button(frame, text = "/", height = 4, width = 9, font = 35, command = lambda: button_press(13))
button13.grid(row = 4, column = 0)

# Window end point.
window.mainloop()

# Program end.
