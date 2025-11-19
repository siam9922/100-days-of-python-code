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



#Python Code
#-------------------------------------------------------------------

# PAUSE 2 - Check Odd or Even

user_input = int(input("Type a number: "))
completed_calculation = user_input % 2

if completed_calculation == 0:
    print("This number is even.")
else:
    print("This number is odd.")


# Angela Way

number_to_check = int(input("What is the number you want to check?"))

if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")



# Programmer Notes
#-------------------------------------------------------------------

# - Operators like the modulo operator % is a symbol in programming
#   that has a specific function.

# - The Modulo Operator gives you the remainder of a division.
#   Ex: 10 % 5 = 0 remainder

#   PAUSE 1 - What is 10 % 3?
# - If we use 10 % 3 it will equal to 1 remainder because 3 does not
#   cleanly cut into 10 which only gives us the remaining.