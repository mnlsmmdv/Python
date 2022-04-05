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

# Program constants.
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
    # Constructor.
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Creates lists of coordinates.
        for i in range(0, BODY_PARTS):
            # Appears in the top left corner.
            self.coordinates.append([0, 0])

        # Creates squares.
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

# Class for Food object.
class Food:
    # Constructor.
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE
        self.coordinates = [x, y]
        
        # Food object attributes.
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# Function takes the next turn.
def next_turn(snake, food):
    # Snake head coordinates.
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    # Deletes snakes body parts.
    del snake.coordinates[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]

    window.after(SPEED, next_turn, snake, food)

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

# Calling function.
next_turn(snake, food)

# Window loops the whole program.
window.mainloop()

# Program end.
