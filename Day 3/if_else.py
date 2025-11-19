#Instructor Notes
#------------------------------------------------------------------------------------------

# Condition Check
# Learn to use conditionals in Python to check a conditions and tell the computer what to do in each case. e.g.

# if <this condition is true>:

#     <then execute this line of code>

# What if the condition is false?
# The else keyword is used to define a block of code that will execute if the condition checked in the if statement is false.

# if pigs can fly:

#     <Some code that will never execute>

# else:

#     print("This is real life")

# Python Indentation
# Understand the importance of indentation in Python as a way to make certain lines of code subsidaries of other lines of code.

# e.g.

# if 5 > 2: #This is a parent line of code

#     print("yes") #this is a child line of code

# Comparator Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

#-----------------------------------------------------------------------------------------



#Python Code 
#---------------------------------------------------------------------------------------------

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")





# Programmer Notes
#---------------------------------------------------------------------------------------------

# - Conditional statements in Python are control flow statements that allow a program to make
#   decisions and execute different blocks of code based on whether certain conditions are met.
#   Depending on a condition we either go A or B.

# - In python spacing and indentation are really important.
#   Everything that is indented after is a block of code.

# - Comparator Operators
#       > Greater than
#       < Less than
#       >= Greater than or equal to
#       <= Less than or equal to
#       == Equal to
#       != Not equal to

# - Assignment and Equality are two different things.
#   One equal sign represents = just an assignment for adding and subtracting.
#   Equality is comparing values, and we use two equal signs.