# 🐍 PYTHON BEGINNER TASK 01: Print, Variables, and Input

# 1. Create a variable called `name` and assign it a string value (your name).
# 2. Create another variable called `age` and assign it your age (as a number).
# 3. Print a greeting message using both variables. Example: "Hello, my name is John and I am 25 years old."
# 4. Ask the user to input their favorite color using `input()`, and store it in a variable called `fav_color`.
# 5. Print a message that says: "Your favorite color is blue!" (but replace blue with whatever the user typed).

# 🎯 Your goal is to combine all of the above using variables, input, and print statements.
# 🚫 Do not use any advanced functions yet — just the basics: variables, input(), and print().



# name = "Siam Hasan"
# age = 22
# print(f"Hello, my name is {name} and I am {age} years old.")

# fav_color = input("What is your favorite colour? ").strip()
# print(f"Your favorite colour is {fav_color}.")

#Additional: Tried strip() to remove extra spaces



# 🐍 PYTHON TASK 02: IF STATEMENTS

# 1. Ask the user to enter their age using input(), and convert it to an integer.
# 2. If the age is 18 or older, print: "You're an adult!"
# 3. If the age is less than 18, print: "You're still a minor."
# 4. Add a second condition: if the age is exactly 100, print: "Whoa! A century old!"
# 5. BONUS: If the user enters something that's not a number, show a friendly error message.

# 🎯 Focus on: if, elif, else statements and basic input validation.



# try:
#     age = int(input("What is your age? "))
#     if age == 100:
#         print("Whoa! A century old!")
#     elif age >= 18:
#         print("You're an adult!")
#     else:
#         print("You're still a minor.")
# except:
#     print("That is not a number")

#Additional: Used try and except to catch the error 



# 🐍 PYTHON TASK 03: WHILE LOOPS + GUESSING GAME

# 1. Create a secret number (e.g., 7).
# 2. Ask the user to guess the number using input().
# 3. If the guess is wrong, keep asking until they guess correctly.
# 4. After a correct guess, print "Correct! You guessed it!"
# 5. BONUS: Count how many tries it took them to guess right, and show it in the final message.
# 6. EXTRA BONUS: If the user types something that's not a number, show an error message (like in your previous task) but don’t crash.

# 🎯 Focus on: while loops, input(), int conversion, try/except, and a counter variable.

# secret_number = 7

# while True:
#     try:
#         guess = int(input("Guess a number: "))
#         tries = 1
#         while guess != secret_number:
#             guess = int(input("Guess again: "))
#             tries += 1
#         print(f"Correct! You guessed it! It only took {tries} tries")

#     except:
#         print("That is not a number!")



# 🐍 PYTHON TASK 04: BUILDING FUNCTIONS

# 1. Create a function called `greet_user` that takes one parameter: name
#    - Inside the function, print: "Hello, <name>! Welcome back."

# 2. Create another function called `calculate_area` that takes two parameters: width and height
#    - It should return the area (width × height)
#    - Print the result outside the function using return value

# 3. BONUS: Ask the user for their name and pass it to `greet_user`
#    Then ask the user for width and height (as numbers), pass those to `calculate_area`,
#    and print the final area.

# 🎯 Focus on: Defining functions, passing arguments, using return, and reusing your code
# 📌 Optional: Add error handling (try/except) when getting user inputs for width and height


# def greet_user(name):
#     print(f"Hello, {name}! Welcome back.")

# user_input = input("What is your favorite animal? ")
# greet_user( user_input)


# def calculate_area(width, height ):
#     area = width * height
#     print(f"The area is {area}")

# width_input = int(input("What is the width? "))
# height_input = int(input("What is the height? "))
# calculate_area( width_input, height_input )


# 🐍 PYTHON TASK 05: LISTS + FOR LOOPS

# 1. Create a list of at least 5 of your favorite foods.
# 2. Use a for loop to print each food from the list, one by one.
# 3. Ask the user to add a new food to the list (using input).
# 4. Print the updated list after adding the new item.
# 5. BONUS: Loop through the list and print a message for each, like:
#    "I like pizza." or "I like sushi."
