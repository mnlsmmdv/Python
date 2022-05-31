"""
Name: Ahmed Affaan                                  
Title: main.py
Folder: Python_text_editor                            
Date: 23/03/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description:                                        
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start.

# Importing needed libraries.
import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

# This function will change the colours of the font.
def change_colour():
    # Helps choose a colour.
    colour = colorchooser.askcolor(title="Pick a colour")
    # Chooses only one colour.
    text_area.config(fg=colour[1])

# This function will help change the font.
def change_font(*args):
    # Placeholder
    pass

# This function will help create new files.
def new_file():
    # Placeholder.
    pass

# This function will help open files.
def open_file():
    # Placeholder.
    pass

# This function will help save files.
def save_file():
    # Placeholder.
    pass

# This function will help cut contents.
def cut():
    # Placeholder.
    pass

# This function will help copy contents.
def copy():
    # Placeholder.
    pass

# This function will help paste contents.
def paste():
    # Placeholder.
    pass

# This function will help store the about section.
def about():
    # Placeholder.
    pass

# This function will help quit the text editor.
def quit():
    # Placeholder.
    pass

# Opening the main window.
window = Tk()
# Title for window.
window.title("Text Editor")

# Window width and height.
window_width = 500
window_height = 500
# This will calculate the screen's size (x and y axis) and sets the geometry.
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2 ) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
# File to work with.
file = None

"""
font_name : Stores font names
font_name.set() : Sets the initial font
font_size : Stores the font sizes
font_size.set() : Sets the initial font size
"""
font_name = StringVar(window)
font_name.set("Times New Roman")
font_size = StringVar(window)
font_size.set("25")

# Text area to write content on the text editor.
text_area = Text(window, font = (font_name.get(), font_size.get()))

# Scrollbar for the text editor.
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
# This will spread the text area to the whole window.
text_area.grid(sticky=N + E + S + W)

# Spin box for font colour, size and style.
frame = Frame(window)
frame.grid()
# Change colour button settings.
colour_button = Button(frame, text="colour", command=change_colour)
colour_button.grid(row=0, column=0)

# This will display different fonts available.
font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

# This will let the user change the font size.
size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

# Scrollbar visual settings.
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

# Looping the window.
window.mainloop()

# Program end.
