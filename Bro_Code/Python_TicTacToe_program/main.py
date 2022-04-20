"""
Name: Ahmed Affaan                                  
Title: main.py
Folder: Python_TicTacToe_program                            
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

# This function will handle the next turn.
def next_turn(row, column):
    # Temporary statement.
    pass

# This function will check who's the winner.
def check_winner():
    # Temporary statement.
    pass

# This function will check for any empty spaces.
def empty_spaces():
    # Temporary statement.
    pass

# This function will launch a new game.
def new_game():
    # Temporary statement.
    pass

# Window initialization.
window = Tk()
# Window's title.
window.title("Tic-Tac-Toe")

# List of players.
players = ["x", "o"]
# Picking a random player to begin.
player = random.choice(players)

# 2D List of buttons.
buttons = [[0,0,0],
            [0,0,0],
            [0,0,0]]

# Label to display turn.
label = Label(text=player + " turn", font=("Monospace", 40))
label.pack(side="top")

# Reset game button.
reset_button = Button(text="Restart", font=("Monospace", 20), command = new_game)
reset_button.pack(side="top")

# Frame to display 2D buttons.
frame = Frame(window)
frame.pack()

# To display buttons (Row - Column).
for row in range(3):
    for column in range(3):
        # Creates new buttons and adds it to the grid.
        buttons[row][column] = Button(frame, text="", font=("Monospace",40), width=5, height=2, command = lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row, column=column) 

# Window initialization end.
window.mainloop()

# Program end.
