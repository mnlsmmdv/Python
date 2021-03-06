"""
Name: Ahmed Affaan                                  
Title: multiple_choice_quiz.py                      
Folder: Multiple Choice Quiz                        
Date: 29/12/2021                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description:                                        
Note: Uncomment codes to execute and comment
them when not in use.                         
"""

# Program start.

# Importing the Question class.
from Question import Question

# Question Prompt array.
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

# This will create question objects.
questions = [
    # This will be the question index and answer for the first question.
    Question(question_prompts[0], "a"),
    # This will be the question index and answer for the second question.
    Question(question_prompts[1], "c"),
    # This will be the question index and answer for the third question.
    Question(question_prompts[2], "b")
]

# This will loop through all the questions.
def run_test(question):
    # This variable will increment user's correct answers.
    score = 0
    # This For Loop will loop through each question in the questions object.
    for question in questions:
        # This variable will store the user's given answers.
        answer = input(question.prompt)
        # This IF Loop will check if the user's answer is correct.
        if answer == question.answer:
            # If the answer is true it will increment the score.
            score += 1
    # If the user's answer is correct it will display how many questions got right.
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")

# Calling the run_test function to run the program.
run_test(questions)

# Program end.
