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
    # Placeholder.
    pass

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

# Looping the window.
window.mainloop()

# Program end.
