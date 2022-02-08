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
import os
import tkinter
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

# This function will change the font colour.
def change_colour(self):
    # Asks to choose colour.
    colour = colorchooser.askcolor(title = "pick a colour")
    # Picks one type of colour type.
    text_area.config(fg = colour[1])

# This function will change the font.
def change_font(*args):
    # Temporary statement.
    pass

# This function will help create new files.
def new_file():
    # Temporary statement.
    pass

# This function will help open files.
def open_file():
    # Temporary statement.
    pass

# This function will help save files.
def save_file():
    # Temporary statement.
    pass

# This function will help cut.
def cut():
    # Temporary statement.
    pass

# This function will help copy.
def copy():
    # Temporary statement.
    pass

# This function will help paste.
def paste():
    # Temporary statement.
    pass

# This function will display the about section.
def about():
    # Temporary statement.
    pass

# This function will help quit the text editor.
def quit():
    # Temporary statement.
    pass

# Creating the main window.
window = Tk()
# Window title.
window.title("Text Editor program")
# File used.
file = None

# Window height and width.
window_height = 500
window_width = 500

# This will get the screen height and width.
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Setting the x and y axis.
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

# Windows display geometry.
# Will make it show in the middle.
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# This will set font name and type.
font_name = StringVar(window)
font_name.set("Arial")

# This will set the font's size.
font_size = StringVar(window)
font_size.set("12")

# This will create and configure the text area.
text_area = Text(window, font = (font_name.get(), font_size.get()))

# This will create the window scroll bar.
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight = 1)
window.grid_columnconfigure(0, weight = 1)
text_area.grid(sticky = N + E + S + W)

# Widgets placed within a frame.
frame = Frame(window)
frame.grid()

# Button to change font colour.
colour_button = Button(frame, text = "colour", command = change_colour)
colour_button.grid(row = 0, column = 0)

# Option menu to display fonts.
font_box = OptionMenu(frame, font_name, *font.families(), command = change_font)
font_box.grid(row = 0, column = 1)

# Helps select font size.
size_box = Spinbox(frame, from_ =1, to = 100, textvariable = font_size, command = change_font)
size_box.grid(row = 0, column = 2)

# This will help initialise the scroll bar.
scroll_bar.pack(side = RIGHT, fill = Y)
text_area.config(yscrollcommand = scroll_bar.set)

# Window end point.
window.mainloop()

# Program end.
