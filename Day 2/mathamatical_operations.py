
#Instructor Notes
#------------------------------------------------------------------------------------------------
# Basic Operators
# Learn to use the basic mathematical operators, +, -, *, /, // and **

# PEMDAS
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

# PAUSE 1. What is the output of this code?
# print(3 * 3 + 3 / 3 - 3)

# PAUSE 2. Change the code so it outputs 3?
# print(3 * 3 + 3 / 3 - 3)
#------------------------------------------------------------------------------------------------



#Python Code: 
#-------------------------------------------------------------------------------
print("My age: " + str(12))

#Mathematical Operations
print(123 + 456)    # Addition
print(7-3)          # Subtraction
print(3 * 2)        # Multiplication
print(6/7)          # provides a float
print(6//3)         # provides an integer
print(2**3)         # Exponents

# PAUSE 1. What is the output of this code?
print((3 * 3) + (3 / 3) - 3) # Output is 7.0

# PAUSE 2. Change the code so it outputs 3?
print((3 * (3 + 3)) / 3 - 3) # Output is 3.0


#Coding Exercise 4: BMI Calculator Answer

height = 1.65
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.

bmi = weight / (height**2)
print(bmi)



# Programmer Notes
#-------------------------------------------------------------------------------

# - Python has mathematical operations: (+, -, /, *, **)

# - Implicit typecasting is the default python behaviour.
#   When dividing it will always show a float.

# - Some Mathematical Operations take priority over the other
#   we use BEDMAS. Which is the order of priorities.
#   (), **, *, /, +, -