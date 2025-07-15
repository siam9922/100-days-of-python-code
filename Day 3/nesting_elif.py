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



#How nested if/else and elif statements work:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    #Nested loop starts when the first condition is true
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
       print("Please pay $7.")
    elif age <= 22:
        print("Please pay $10")
    else:
        print("Please pay $12")

else:
    print("Sorry you have to grow taller before you can ride.")



# Programmer Notes
# -------------------------------------------------------------------------------------------------------------------------------------

"""
- Nested if-else means it checks inside the if statements in a code. 
  We can do another if or else. 
  
- elif is other conditions we can check 


"""

# -------------------------------------------------------------------------------------------------------------------------------------