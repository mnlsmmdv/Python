"""
Name: Ahmed Affaan                                  
Title: main.py
Folder: Python_calculator                            
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

# This function will help press the button.
def button_press(num):
    pass

# This function will handle calculations.
def equals():
    pass

# This function will help clear the screen.
def clear():
    pass

# Window initialized.
window = Tk()
# Window title and geometry.
window.title("Calculator")
window.geometry("500x500")

# Stores equation text.
equation_text = ""

# Helps store the equation label.
equation_label = StringVar()

# Window label.
label = Label(window, textvariable=equation_label, font=("consolas",20), bg="white", width=24, height=2)
label.pack()

# Window frame.
frame = Frame(window)
frame.pack()

# BUTTONS
button1 = Button(frame, text=1, height=4, width=9, font=35, command= lambda: button_press(1))
button2 = Button(frame, text=1, height=4, width=9, font=35, command= lambda: button_press(2))
button3 = Button(frame, text=1, height=4, width=9, font=35, command= lambda: button_press(3))
button4 = Button(frame, text=1, height=4, width=9, font=35, command= lambda: button_press(4))


# Helps loop the window.
window.mainloop()

# Program end.
