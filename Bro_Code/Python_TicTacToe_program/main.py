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
    # Access to our player.
    global player

    # Checks if button clicked is empty.
    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]["text"] = player

            # Checks winner after button fill and swaps player.
            # Checks if winner is false.
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))

            # Checks if any player won.
            elif check_winner() is True:
                label.config(text=players[0] + " wins")

            # Checks for a tie.
            elif check_winner() == "Tie":
                label.config(text="Tie")

        else:
            buttons[row][column]["text"] = player

            # Checks winner after button fill and swaps player.
            # Checks if winner is false.
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))

            # Checks if any player won.
            elif check_winner() is True:
                label.config(text=players[1] + " wins")

            # Checks for a tie.
            elif check_winner() == "Tie":
                label.config(text="Tie")
            
# This function will check who's the winner.
def check_winner():
    # Horizontal win conditions.
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            # Somebody won horizontally.
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    # Vertical win conditions.
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            # Somebody won vertically.
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    # First Diagonal win conditions.
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        # Someone wins diagonally.
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    # Second Diagonal win condition.
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        # Somebody wins diagonally.
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    # Checks for remaining spaces.
    elif empty_spaces() is False:
        # Returns there is a tie.
        return "Tie"

    # No winner and no tie.
    else:
        return False


# This function will check for any empty spaces.
def empty_spaces():
    # Local variable for buttons.
    spaces = 9
  
    # Checks the text of each button.
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -=1

    # No empty spaces left.
    if spaces == 0:
        return False
    else:
        return True

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
