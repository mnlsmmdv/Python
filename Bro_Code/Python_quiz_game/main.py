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
        correct_guesses += check_answer(questions.get(key),guess)
        # Increments question number.
        question_number += 1
    
    # This will display the final score.
    display_score(correct_guesses, guesses)

# ---------------------------------------------------------

# This function will check answers to guesses.
def check_answer(answer,guess):
    if answer == guess:
        # Increments user point.
        print("CORRECT!")
        return 1
    else:
        # Decreases user point.
        print("WRONG")
        return 0

# ---------------------------------------------------------

# This function will display the score.
def display_score(correct_guesses, guesses):
    print("---------------------------------------------------------")
    print("RESULTS")
    print("---------------------------------------------------------")
    
    # Will display all the answers.
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    # Will display all the guesses.
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    
    # Calculates the final score and prints it.
    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "% ") 

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
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]

# Calling the new game function.
new_game()

# Program end.
