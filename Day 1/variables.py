
#Instructor Notes
#------------------------------------------------------------------------------------------------
# Learn to store values in containers for later use. Variables is a concept in programming that allows us to give a label to a piece of data so that we can refer or reference that data using the chosen variable name. We will see in this lesson how to create variables and how to use the variables to access the contained value.

# PAUSE 1. Check the length of the user input
# Using what you have learnt about the len() function and the input() function. Try to print out the number of characters in the user input. Write everything in just 1 line of code.

# PAUSE 2. Split everything into variables.
# Split each step in the previous exercise into a separate variable. One variable called username and one called length. Use the variable username in the len calculation

#------------------------------------------------------------------------------------------------



#Python Code 
#-------------------------------------------------------------------------------

# name = input("What is your name? ")
name = "Jack"
print(name)

name = "Angela"
print(name)


#Pause 1:  Check the length of the user input

user = len(input("Tell me your name: "))
print(user)

# PAUSE 2. Split everything into variables

username = input("Tell me your name: ")
length = len(username)
print(length)


#Coding Exercise 3: Variables Answer

glass1 = "milk"
glass2 = "juice"

glass1, glass2 = glass2 , glass1
print(glass1)
print(glass2)


# Programmer Notes
#-------------------------------------------------------------------------------

# - Python Variables:  is a concept in programming that allows us
#   to give a label to a piece of data so that we can refer or
#   reference that data using the chosen variable name.
#   Ex. james = 01253456789

# - Googling answers is a useful skill when trying to be a programmer.
# - Brain is for thinking not for storing.

# - To find the length of a string we use an in-built function called len().