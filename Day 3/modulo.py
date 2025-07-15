#Instructor Notes
#------------------------------------------------------------------------------------------
# The modulo operator gives you the remainder of a division.

# 6 % 2 #will be 0

# 6 % 5 #will be 1

# 6 % 4 #will be 2

# PAUSE 1 - What is 10 % 3?
# What do you think this will output?

# print(10 % 3)

# PAUSE 2 - Check Odd or Even
# Write some code using what you have learnt about the modulo operator and conditional checks in Python to check if the number in he input area is odd or even. If it's odd print out the word "Odd" otherwise printout "Even".

#-----------------------------------------------------------------------------------------

#If the modulo is cleanly its always 0 and has a == operator
#Even number 12 % 2 == 0

#Task 1: What is 10 % 3?
#How Modulo works
num = 10 % 3
print(num)

#Task 2: Check Odd or even

number_to_check = int(input("What is the number you want to check? "))

if number_to_check % 2 == 0:
    print("It is an even number")
else:
    print("It is an odd number ")






# Programmer Notes
# -------------------------------------------------------------------------------------------------------------------------------------

"""
- An operator is a symbol in programming that has a specific function.

- The modulo operator provides the remainder. 
Performs division and then gives out the remaining. 

"""

# -------------------------------------------------------------------------------------------------------------------------------------
