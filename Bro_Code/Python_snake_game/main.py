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
import random

# Setting program constants.
# Game Height.
GAME_HEIGHT = 700
# Game Width.
GAME_WIDTH = 700
# Speed of the snake.
SPEED = 50
# Object sizes (Food and body parts etc).
SPACE_SIZE = 50
# Snake's default body size.
BODY_PARTS = 3
# Snake's Colour.
SNAKE_COLOR = "#00FF00"
# Food Colour.
FOOD_COLOR = "#FF0000"
# Background Colour.
BACKGROUND_COLOR = "#000000"

# Class for Snake object.
class Snake:
    # Temporary statement.
    pass

# Class for Food object.
class Food:
    # Initializes the Food object.
    def __init__(self):
        

# This function will handle the next turn.
def next_turn():
    # Temporary statement.
    pass

# Handles changing Snake's direction.
def change_direction(new_direction):
    # Temporary statement.
    pass

# Handles checking object collisions.
def check_collisions():
    # Temporary statement.
    pass

# Function to check if the user has lost.
def game_over():
    # Temporary statement.
    pass

# Creating the main GUI window.
window = Tk()
# Window's title.
window.title("Snake Game")
# Keeps GUI window size constant.
window.resizable(0, 0)

# Game default score.
score = 0
# Game default direction.
direction = "down"

# Adding label to the window.
label = Label(window, text="Score:{}".format(score), font=("consolas", 40))
label.pack()

# Main Canvas where the  game will be displayed.
# Creating a new Canvas.
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Refreshes the window.
window.update()

# Centers the window on default on opening.
# This will find the exact dimensions.
window_height = window.winfo_height()
window_width = window.winfo_width()
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

# Setting the x and y axis.
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

# Windows display geometry.
# Will make it show in the middle.
window.geometry(f"{window_height}x{window_width}+{x}+{y}")

# Creating Snake and Food objects.
snake = Snake()
food = Food()

# Window end point.
window.mainloop()

# Program end.
