# 🎯 SIMPLE PRACTICE: "Magic 8-Ball"
#
# What it does:
# - Ask user's name
# - Keep asking them yes/no questions 
# - Give random answers like "Yes!", "No way!", "Ask again later"
# - Let them ask as many questions as they want
# - Stop when they type "quit"
#
# Why it's simple:
# - Just one function (give random answer)
# - Simple while loop (keep going until "quit")
# - Easy to understand and fun to use

import random

def random_answers():
    answers = ["Yes!", "No way!", "Ask again later"]
    print(random.choice(answers))
    return answers

name = input("What is your name? ")
questions = input("Ask a yes or no question!\n")

while questions != "quit":
    random_answers()
    questions = input("Ask a yes or no question!\n")
print("Bye")

