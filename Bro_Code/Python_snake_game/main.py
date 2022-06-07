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
GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 10
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

# Class for the Snake object.
class Snake:
    # Contrustor for our Snake object.
    def __init__(self):
        # Sets the Snake's body size.
        self.body_size = BODY_PARTS
        # List for coordinates and squares.
        self.coordinates = []
        self.squares = []

        # Creating a list of coordinates.
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0]) # Snake appears in the top left corner.

        # Creating a list of squares.
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            # Appending each square in to the list.
            self.squares.append(square)

# Class for the Food object.
class Food:
    # Constructor for our Food object.
    def __init__(self):
        # Places Food object randomly on canvas.
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        # Sets the Food object displaying coordinates.
        self.coordinates = [x, y]

        # Draws Food object on the canvas.
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# This function will decide the next turn.
def next_turn(snake, food):
    # Unpacking the head of the Snake.
    x, y = snake.coordinates[0]
    
    # This will check the initial direction.
    if direction == "up":
        # Moves one space up.
        y -= SPACE_SIZE
    elif direction == "down":
        # Moves one space down.
        y += SPACE_SIZE
    elif direction == "left":
        # Moves one space to the left.
        x -= SPACE_SIZE
    elif direction == "right":
        # Moves one space to the right.
        x += SPACE_SIZE

    # Updates coordinates for the head of the Snake.
    snake.coordinates.insert(0, (x, y))

    # Creates new graphic for the head of the Snake.
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    # Updates Snake's list of squares.
    snake.squares.insert(0, square)

    # This will update the Snake's score after the food has been eaten.
    if x == food.coordinates[0] and y == food.coordinates[1]:
        # Accesses the score and increments by 1.
        global score
        score += 1

        # Changes the label with the current score.
        label.config(text="Score:{}".format(score))

        # Deletes the food object and creates a new one.
        canvas.delete("food")
        food = Food()
    # Deletes the body part if the food is not eaten.
    else:
        # Deletes the last body part of the Snake while moving.
        del snake.coordinates[-1]

        # Updates the canvas.
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Checks if any collisions have occured.
    if check_collisions(snake):
        # Function called and user loses the game.
        game_over()
    # If there is no collisions updates the next turn.
    else:
        # Calling the next turn function.
        window.after(SPEED, next_turn, snake, food)

# This function will decide which direction to go.
def change_direction(new_direction):
    # Accesses the initial direction.
    global direction

    # Changes the directions.
    # Left direction.
    if new_direction == 'left':
        if direction != 'right':
            # Sets direction to left.
            direction = new_direction
    # Right direction.
    elif new_direction == 'right':
        if direction != 'left':
            # Sets direction to right.
            direction = new_direction
    # Up direction.
    elif new_direction == 'up':
        if direction != 'down':
            # Sets direction to up.
            direction = new_direction
    # Down direction.
    elif new_direction == 'down':
        if direction != 'up':
            # Sets direction to down.
            direction = new_direction

# This function will check for collisions.
def check_collisions(snake):
    # Unpacking the head of the Snake.
    x, y = snake.coordinates[0]

    # Checks if the left or right border of canvas was crossed.
    if x < 0 or x >= GAME_WIDTH:
        # Game over if left and right border is crossed.
        return True
    if y < 0 or y >= GAME_HEIGHT:
        # Game over if top or bottom border is crossed.
        return True

    # Checks if the Snake has touched it's tail or another body part.
    for body_part in snake.coordinates[1:]:
        # Game over if Snake has collided with a body part.
        if x == body_part[0] and y == body_part[1]:
            return True
    # Returns false if this action has not happend.
    return False

# This function will check if the user has lost the game.
def game_over():
    # Clears objects from the canvas.
    canvas.delete(ALL)
    # Text to display that the game is over.
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('consolas', 70), text="GAME OVER!", fill="red", tag="gameover")

# GUI window settings.
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

# Variables to store score and the initial direction.
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

# Binding keys for the Snake to move.
window.bind('<Left>', lambda event: change_direction('left')) # Left arrow key.
window.bind('<Right>', lambda event: change_direction('right')) # Right arrow key.
window.bind('<Up>', lambda event: change_direction('up')) # Up arrow key.
window.bind('<Down>', lambda event: change_direction('down')) # Down arrow key.

# Creating objects for Snake and Food and assigning them to classes.
snake = Snake()
food = Food()

# Calling function with parameters.
next_turn(snake, food)

# Looping the window.
window.mainloop()

# Program end.
