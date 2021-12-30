#######################################################
# Name: Ahmed Affaan                                  #
# Title: multiple_choice_quiz.py                      #
# Folder: Multiple Choice Quiz                        #
# Date: 29/12/2021                                    #
# Country: Reublic of Maldives                        #
# Code version: 3.8.10                                #
# Description:                                        #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

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
        

# Program end.
