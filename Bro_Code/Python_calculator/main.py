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
    # Making Equation Text public.
    global equation_text

    # These will display content on the calculator label.
    # Initialising Equation Text.
    equation_text = equation_text + str(num)

    # Displays the content.
    equation_label.set(equation_text)

# This function calculates expressions.
def equals():
    # Making Equation Text public.
    global equation_text

    # Will get rid of ZeroDivisionError
    try:
        # Converts values to strings.
        total = str(eval(equation_text))
        
        # Displays the content.
        equation_label.set(total)

        # Calculates the total.
        equation_text = total

    # Error message for Syntax Errors.
    except SyntaxError:
        # Error message.
        equation_label.set("Syntax Error!")

        # Clears the screen.
        equation_text = ""

    # Error message for ZeroDivisonError's
    except ZeroDivisionError:
        # Error message.
        equation_label.set("Arithmetic Error!")
        
        # Clears the screen.
        equation_text = ""

# This function clears the calculator.
def clear():
    # Temporary statement.
    pass

# Creating the main GUI window.
window = Tk()
# Window title.
window.title("Calculator")
# Size of the window.
window.geometry("550x550")
# Keeping window at constant size.
window.resizable(0, 0)
# Window main colour.
window.configure(bg = "#303952")

# Will display the equation.
equation_text = ""

# String variable.
equation_label = StringVar()

# Adding label to the window.
label = Label(window, textvariable = equation_label, font = ("consolas", 20), bg = "#596275", fg = "#42ada6", width = 29, height = 2)
label.pack()

# Main frame to house GUI contents.
frame = Frame(window)
frame.pack()

# Main frame general colour.
frame.configure(bg = "#303952")

# Button configurations.
# Button 1.
button1 = Button(frame, text = 1, height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = lambda: button_press(1))
button1.grid(row = 0, column = 0)

# Button 2.
button2 = Button(frame, text = 2, height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = lambda: button_press(2))
button2.grid(row = 0, column = 1)

# Button 3.
button3 = Button(frame, text = 3, height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = lambda: button_press(3))
button3.grid(row = 0, column = 2)

# Button 4 (plus)
plus = Button(frame, text = "+", height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = lambda: button_press("+"))
plus.grid(row = 0, column = 3)

# Button 5.
button5 = Button(frame, text = 4, height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = lambda: button_press(4))
button5.grid(row = 1, column = 0)

# Button 6.
button6 = Button(frame, text = 5, height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = lambda: button_press(5))
button6.grid(row = 1, column = 1)

# Button 7.
button7 = Button(frame, text = 6, height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = lambda: button_press(6))
button7.grid(row = 1, column = 2)

# Button 8 (minus)
minus = Button(frame, text = "-", height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = lambda: button_press("-"))
minus.grid(row = 1, column = 3)

# Button 9.
button9 = Button(frame, text = 7, height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = lambda: button_press(7))
button9.grid(row = 2, column = 0)

# Button 10.
button10 = Button(frame, text = 8, height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = lambda: button_press(8))
button10.grid(row = 2, column = 1)

# Button 11.
button11 = Button(frame, text = 9, height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = lambda: button_press(9))
button11.grid(row = 2, column = 2)

# Button 12 (multiply)
multiply = Button(frame, text = "*", height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = lambda: button_press("*"))
multiply.grid(row = 2, column = 3)

# Button 13.
button13 = Button(frame, text = "0", height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = lambda: button_press(0))
button13.grid(row = 4, column = 0)

# Button 14 (decimal)
decimal = Button(frame, text = ".", height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = lambda: button_press("."))
decimal.grid(row = 4, column = 1)

# Button 15 (equal)
equal = Button(frame, text = "=", height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = equals)
equal.grid(row = 4, column = 2)

# Button 16 (divide)
divide = Button(frame, text = "/", height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = lambda: button_press("/"))
divide.grid(row = 4, column = 3)

# Button 17 (clear)
clear_screen = Button(frame, text = "AC", height = 4, width = 9, font = 35, bg = "#303952", fg = "#42ada6", command = clear)
clear_screen.grid(row = 5, column = 3)

# Window end point.
window.mainloop()

# Program end.
