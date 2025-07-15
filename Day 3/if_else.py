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

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

#How if-else works
if height >= 120:
    print("You can ride the rollercoaster.")
else:
    print("You have to grow taller before you can ride")

#Using equal to
if height == 120:
    print("You can ride the rollercoaster.")
else:
    print("You have to grow taller before you can ride")






#Programmer Notes
#-------------------------------------------------------------------------------------------------------------------------------------

"""
-   If-else depending on a particular condition if we do option a or b. 
    Like true and false
    
-   Spacing and indentation is important 

-   Indentation error is one of the errors 

-   Why this is important >= when we want to equal the exact number 
    that is 120 then this code will run. While instead not worrying 
    about making 120 false because of this >.
    
-   Equal signs are interpreted differently one is for assignment 
    the other is for check equality
"""


#-------------------------------------------------------------------------------------------------------------------------------------