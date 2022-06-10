"""
Name: Ahmed Affaan
Title: main.py
Folder: GUI_Frontends
Date: 07/06/2022
Country: Republic of Maldives
Code version: 3.8.10
Description: GUI frontend for a quiz game in English.
Credits to: Bro Code
Credits to link: https://www.youtube.com/watch?v=yriw5Zh406s
Note: Uncomment codes to execute and comment them when not in use.
"""

# Program start.

# Importing libraries.
from tkinter import *

# This function will help press buttons.
def press_button(letter):
    # Placeholder.
    pass

# This function will validate button presses.
def validate_option():
    # Placeholder.
    pass

# This function will help clear the screen.
def clear_screen():
    # Placeholder.
    pass

# Splash GUI window settings.
splash_screen = Tk()
splash_screen.title("Quiz Game") # GUI window title.Learn Linux Tv
splash_screen.geometry("300x200") # GUI window dimensions.
splash_screen.resizable(False, False) # Keeping constant dimension size.
#splash_screen.overrideredirect(True) # Hides the GUI window title bar.
splash_screen.configure(bg="#2d3436") # Background colour.

# Splash screen label.
splash_screen_label = Label(splash_screen, text="Splash Screen", font=("consolas", 20), bg="#b2bec3")
splash_screen_label.pack() # Displaying label on window.

# Settings to center the splash GUI window on initial run.
splash_screen.update() # Refreshes the window.
splash_width = splash_screen.winfo_width() # Gets the GUI window width.
splash_height = splash_screen.winfo_height() # Gets the GUI window height.
screen_width = splash_screen.winfo_screenwidth() # Gets the screen width.
screen_height = splash_screen.winfo_screenheight() # Gets the screen height.
x = int((screen_width / 2) - (splash_width / 2)) # Calculates the x-axis.
y = int((screen_height / 2) - (splash_height / 2)) # Calculates the y-axis.
splash_screen.geometry(f"{splash_width}x{splash_height}+{x}+{y}") # Sets the window size to the screen center.

# This function will hold main window settings.
def main_window():
    # Main GUI window settings.
    window = Tk()
    window.title("Quiz Game") # GUI window title.
    window.geometry("600x600") # GUI window dimensions.
    window.resizable(False, False) # Keeping constant dimension size.
    window.configure(bg="#2d3436") # Background colour.

    # Stores the quiz text.
    quiz_text = ""
    # Helps store the quiz label.
    quiz_label = StringVar()

    # GUI window label.
    label = Label(window, textvariable=quiz_label, font=("faruma",20), bg="#b2bec3", fg="#2d3436", width=24, height=2)
    label.pack() # Displaying label on the window.

    # Window frame to house buttons.
    frame = Frame(window) # Adding frame to the window.
    frame.pack() # Displaying frame in the window.

    # Settings to center the GUI window on initial run.
    window.update() # Refreshes the window.
    window_width = window.winfo_width() # Gets the GUI window width.
    window_height = window.winfo_height() # Gets the GUI window height.
    screen_width = window.winfo_screenwidth() # Gets the screen width.
    screen_height = window.winfo_screenheight() # Gets the screen height.
    x = int((screen_width / 2) - (window_width / 2)) # Calculates the x-axis.
    y = int((screen_height / 2) - (window_height / 2)) # Calculates the y-axis.
    window.geometry(f"{window_width}x{window_height}+{x}+{y}") # Sets the window size to the screen center.

# Looping the window.
mainloop()

# Program end.
