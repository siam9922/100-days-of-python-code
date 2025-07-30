#Instructor Notes
#------------------------------------------------------------------------------------------
# Your goal is to build a Hangman game using everything you have learnt about Python programming.

# Demo Final Project
# https://appbrewery.github.io/python-day7-demo/

# The project is split into 5 major steps. In each step, there will be multiple TODOs. Your goal is to go through each todo in order and complete them.

# You can view all the todos easily in PyCharm by going to View -> Tool Windows -> TODOs

# TODO-1
# Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2
# Ask the user to guess a letter and assign their answer to a variable called guess. Make the String stored in guess lowercase.

#  Hint 1 
# Search Google for the lower() function in Python.
# TODO-3
# Check if the letter the user guessed guess is one of the letters in the chosen_word. Loop through each of the letters in the chosen_word and print "Right" if the letter is a match, "Wrong" if it's not.

#  Hint 2 
# You can loop through Strings the same way you can loop through Lists - by using the `for in` loop. Try Googling: "Loop through strings python"
#------------------------------------------------------------------------------------------


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

guess = (input("Guess a letter: ")).lower()
i = 0
for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        print("Right!")
    else:
        print("Wrong!")

range(len(chosen_word))


#low complexity
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")
#





# ------------------------------- #
#       PROGRAMMER NOTES          #
# ------------------------------- #

# How I think we will build hangman:

#Start with initializing a word into a variable
#Then create a while loop to make sure the word fits into the right category
#While loop should be not equal to word and compare would be the word i declared
#if word is wrong the print hangman will start coming and we will lose the lives
#else: word is right
#print you won to end the loop