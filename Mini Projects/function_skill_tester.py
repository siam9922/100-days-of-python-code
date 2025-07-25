# FUNCTION BEGINNER SKILL TESTER - MINI PROJECT  
# (Based on Angela Yu's Course - Day 6 Level)
#=============================================================================
# PROJECT: "My First Function Collection"
#
# OBJECTIVE: Test your function skills using only Day 1-6 concepts
#
# REQUIREMENTS:
# 1. Create a function that prints a welcome message
# 2. Make a function that takes a name and prints a greeting
# 3. Build a function that adds two numbers and prints the result
# 4. Create a function that prints a simple pattern
# 5. Make a function that picks a random number and prints it
# 6. Call all your functions from a main program
#
# FUNCTION EXAMPLES TO CREATE:
# def say_hello():
#     # Print a simple welcome message
#
# def greet_person(name):
#     # Print "Hello [name]!"
#
# def add_numbers(num1, num2):
#     # Print the sum of the two numbers
#
# def make_pattern():
#     # Print a simple pattern like stars or letters
#
# def random_picker():
#     # Use random to pick and print a number
#
# CONCEPTS YOU'LL USE (Day 1-6 Only):
# - def to create functions
# - Function parameters (simple ones)
# - print() statements inside functions
# - Calling functions
# - Basic variables
# - Random module usage
#
# EXAMPLE OUTPUT:
# "=== MY FUNCTION COLLECTION ==="
# "Welcome to my program!"
# "Hello Alice!"
# "5 + 3 = 8"
# "Here's a pattern:
# ***
# ***
# ***"
# "Random number: 7"
#
# DEBUGGING TIPS:
# - Define functions before calling them
# - Check your indentation carefully
# - Functions in Day 6 mostly just print things (no return yet)
# - Test each function separately
# - Keep functions simple and focused
#=============================================================================

# YOUR FUNCTIONS START HERE:

#1.
def say_hello():
    print("Hello World!")
say_hello()

#2.
name = "Siam"
def greet_person(name):
      print(f"Hello {name}!")
greet_person(name)

#3.
num1 = 6
num2 = 2
def add_numbers(num1, num2):
    result = num1 + num2
    print(result)
add_numbers(num1, num2)

#4.
def make_pattern():
     print("*")
     print("**")
     print("***")
     print("****")
     print("*****")
make_pattern()

#5.
import random

def random_picker():
     value = random.randint(1, 10) 
     print(value)
random_picker()     


# YOUR MAIN PROGRAM HERE:




#=============================================================================