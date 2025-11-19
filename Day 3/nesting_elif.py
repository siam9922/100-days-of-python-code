#Instructor Notes
#------------------------------------------------------------------------------------------
# You can put if/else statements inside other if/else statements. This is known as nesting. e.g.

# if maths_score >= 90:
#     if english_score >= 90:
#         print("You're good at everything")
#     else:
#         print("You're good at maths")
# if english_score >= 90:
#     print("You're good at english)
# In this case only when a student has over 90 on maths and english, do they get "You are good at everything".

# Note: You can also have if statements that don't have a paired else statement.

#-----------------------------------------------------------------------------------------




#Python Code
#--------------------------------------------------------------------------------

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:

    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")


# Coding Exercise 5: BMI Calculator with Interpretations Answer

weight = 85
height = 1.85

bmi = weight / (height ** 2)


# 🚨 Do not modify the values above
# Write your code below 👇



if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi >= 24:
    print("normal weight")
else:
    print("overweight")



# Programmer Notes
#--------------------------------------------------------------------------------

# - PRO TIP: Inputs and variables can be written inside the if statements

# - Nested if statements in Python involve placing one if statement
#   (or if-else, if-elif-else block) inside another if statement (or else block).
#   This allows for checking multiple conditions sequentially,
#   where the inner condition is only evaluated if the outer condition is true.

# - the elif statement, short for "else if," is used to check for multiple conditions
#   sequentially after an initial if statement. It provides a way to execute different
#   blocks of code based on various mutually exclusive conditions.


