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
window.geometry("500x550")

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
button1.grid(row=0, column=0)
button2 = Button(frame, text=2, height=4, width=9, font=35, command= lambda: button_press(2))
button2.grid(row=0, column=1)
button3 = Button(frame, text=3, height=4, width=9, font=35, command= lambda: button_press(3))
button3.grid(row=0, column=2)
button4 = Button(frame, text=4, height=4, width=9, font=35, command= lambda: button_press(4))
button4.grid(row=1, column=0)
button5 = Button(frame, text=5, height=4, width=9, font=35, command= lambda: button_press(5))
button5.grid(row=1, column=1)
button6 = Button(frame, text=6, height=4, width=9, font=35, command= lambda: button_press(6))
button6.grid(row=1, column=2)
button7 = Button(frame, text=7, height=4, width=9, font=35, command= lambda: button_press(7))
button7.grid(row=2, column=0)
button8 = Button(frame, text=8, height=4, width=9, font=35, command= lambda: button_press(8))
button8.grid(row=2, column=1)
button9 = Button(frame, text=9, height=4, width=9, font=35, command= lambda: button_press(9))
button9.grid(row=2, column=2)
button0 = Button(frame, text=0, height=4, width=9, font=35, command= lambda: button_press(0))
button0.grid(row=3, column=0)
plus = Button(frame, text="+", height=4, width=9, font=35, command= lambda: button_press("+"))
plus.grid(row=0, column=3)
minus = Button(frame, text="-", height=4, width=9, font=35, command= lambda: button_press("-"))
minus.grid(row=1, column=3)
multiply = Button(frame, text="*", height=4, width=9, font=35, command= lambda: button_press("*"))
multiply.grid(row=2, column=3)
divide = Button(frame, text="/", height=4, width=9, font=35, command= lambda: button_press("/"))
divide.grid(row=3, column=3)
equal = Button(frame, text="=", height=4, width=9, font=35, command=equals)
equal.grid(row=3, column=2)
decimal = Button(frame, text=".", height=4, width=9, font=35, command= button_press("."))
decimal.grid(row=3, column=1)
clear = Button(frame, text="AC", height=4, width=9, font=35, command=clear)
clear.grid(row=4, column=3)

# Helps loop the window.
window.mainloop()

# Program end.
