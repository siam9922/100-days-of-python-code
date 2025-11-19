#Instructor Notes
#------------------------------------------------------------------------------------------

# You can write as many if statements as you need to check for different conditions that are unrelated to each other. Compare the code blocks below:

# # If/elif/else
# if <condition 1 is true>
#     <do A>
# elif <condition 2 is true>
#     <do B>
# else
#     <do C>
# # Nested if statements
# if <condition 1 is true>
#     <do A>
#     if <condition 2 is true>
#         <do B>
#         if <condition 3 is true>
#             <do C>
# # Multiple if statements
# if <condition 1 is true>
#     <do A>
# if <condition 2 is true>
#     <do B>
# if <condition 3 is true>
#     <do C>
# In the if/elif/else block, only one of A, B, or C can happen, because if/elif/else are mutually exclusive. The first condition has to fail to go into the elif and the elif (or multiple elif) have to fail to go into the else. Condition 2 is only checked if condition 1 is false.

# In the nested if statements, A, B and C can all happen, but conditions 1, 2 and 3 must all be true. The computer will only check condition 2 if condition 1 is true.

# In the multiple if statements, A, B, and C can all happen. But they are completely independent of each other. C can happen even if A and B don't. Every condition is checked, no matter the result of the others.


#-----------------------------------------------------------------------------------------


#Python Code 
#--------------------------------------------------------------------------------
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child Tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No. ")
    if wants_photo == "y":
         bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")




# Programmer Notes
#--------------------------------------------------------------------------------

#  - Certain conditions require multiple outputs, and so we keep using if statements

#  - This structure is used when you want multiple conditions to be checked and potentially
#    have multiple, independent actions occur.The conditions are not mutually
#    exclusive(e.g., applying  multiple, unrelated filters or checking for
#    multiple characteristics)

# - When adding inputs in a conditional statement
#   it needs to be added in the same indentation as the conditions

# - In Python, variables are essential for conditions because
#   they provide a way to store and name the data that the condition
#   will evaluate. Without variables, conditions would be limited to
#   evaluating only literal values, which would severely restrict
#   the flexibility and power of your programs.