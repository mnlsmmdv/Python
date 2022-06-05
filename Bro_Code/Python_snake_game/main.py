"""
Name: Ahmed Affaan                                  
Title: main.py
Folder: Python_snake_game                            
Date: 01/06/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description: Simple snake game written in Python.                                       
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start.

# Importing libraries.
from tkinter import *
import random

# Variable declarations.
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

# Class for the Snake object.
class Snake:
    # Placeholder.
    pass

# Class for the Food object.
class Food:
    # Constructs our Food object.
    def __init__(self):
        # Places Food object randomly on canvas.
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        # Sets the Food object displaying coordinates.
        self.coordinates = [x, y]

        # Draws Food object on the canvas.
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# This function will decide the next turn.
def next_turn():
    # Placeholder.
    pass

# This function will decide which direction to go.
def change_direction(new_direction):
    # Placeholder.
    pass

# This function will check for collisions.
def check_collisions():
    # Placeholder.
    pass

# This function will check if the user has lost the game.
def game_over():
    # Placeholder.
    pass

# GUI window settings.
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

# Variable to store score and the initial direction.
score = 0
direction = 'down'

# Score label for the GUI window.
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

# Canvas for the game on the GUI window.
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Settings to center the GUI window on initial run.
window.update() # Refreshes the window.
window_width = window.winfo_width() # Gets the GUI window width.
window_height = window.winfo_height() # Gets the GUI window height.
screen_width = window.winfo_screenwidth() # Gets the screen's width.
screen_height = window.winfo_screenheight() # Gets the screen's width.
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Creating objects for Snake and Food and assigning them to classes.
snake = Snake()
food = Food()

# Looping the window.
window.mainloop()

# Program end.
