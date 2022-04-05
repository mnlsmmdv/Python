"""
Name: Ahmed Affaan                                  
Title: main.py
Folder: Python_snake_game                           
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
import random

# Constants.
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

# Class for Snake object.
class Snake:
    pass

# Class for Food object.
class Food:
    pass

# Function takes the next turn.
def next_turn():
    pass

# Function changes snakes direction.
def change_direction(new_direction):
    pass

# Function checks collisions.
def check_collisions():
    pass

def game_over():
    pass

# Initializing the window.
window = Tk()

# Window title.
window.title("Snake Game")
window.resizable(False, False)

# This will store the users score and snake initial direction.
score = 0
direction = "down"

# Score label.
label = Label(window, text="Score:{}".format(score), font=("consolas", 40))
label.pack()

# Canvas for the snake game.
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Displays the window initially centered.
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Calling objects.
snake = Snake()
food = Food()

# Window loops the whole program.
window.mainloop()

# Program end.
