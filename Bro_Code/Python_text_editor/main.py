"""
Name: Ahmed Affaan                                  
Title: main.py
Folder: Python_text_editor                            
Date: 23/03/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description: Simple text editor written in Python.                                       
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
    # Gets the font name and font size.
    text_area.config(font=(font_name.get(), size_box.get()))

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
    # Message box to show information.
    showinfo("About this program", "This is a program written by Ahmed Affaan. Credits to Bro Code")

# This function will help quit the text editor.
def quit():
    # Helps close out of the window.
    window.destroy()

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
# Scrollbar visual settings.
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

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

# Menu bar for text editor.
menu_bar = Menu(window)
window.config(menu=menu_bar)

# File menu for text editor with drop downs.
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=new_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save File", command=save_file)
# Separator.
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

# Edit menu for text editor.
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
# Buttons for Cut, Copy and Paste.
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

# Help menu for text editor.
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
# Buttons for About.
help_menu.add_command(label="About", command=about)

# Looping the window.
window.mainloop()

# Program end.
