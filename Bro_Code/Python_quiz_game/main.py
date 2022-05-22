"""
Name: Ahmed Affaan                                  
Title: main.py
Folder: Python_quiz_game                            
Date: 21/04/2022                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description: Simple clock GUI in Python.                                        
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start.

# --------------------------------------------------------- 

# This function will create new quiz game.
def new_game():
    # This will store users guesses.
    guesses = []
    # Stores correct guesses.
    correct_guesses = 0
    # Stores the current question number.
    question_number = 1
    
    # Will display all questions inside "questions" dictionary.
    for key in questions:
        print("--------------------------------------------------------- ")
        print(key)
        # Will display options for questions.
        for i in options[question_number - 1]:
            print(i)
        # Gets the user input.
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        # Adding to our "guesses" list.
        guesses.append(guess)

        # Calling function to check answer.
        check_answer(questions.get(key),guess)
        # Increments question number.
        question_number += 1

# ---------------------------------------------------------

# This function will check answers.
def check_answer():
    # Temporary statement.
    pass

# ---------------------------------------------------------

# This function will display the score.
def display_score():
    # Temporary statement.
    pass

# ---------------------------------------------------------

# This function will let the user play the game again.
def play_again():
    # Temporary statement.
    pass

# ---------------------------------------------------------

# Dictionary created to store data.
questions = {
    "Who created Python?: " : "A",
    "What year was Python created?" : "B",
    "Python is tributed to which comedy group?: " : "C",
    "Is the Earth round?: " : "A"
}

# 2D list to hold answer combinations.
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "1991", "2000", "2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]

# Calling the new game function.
new_game()

# Program end.
