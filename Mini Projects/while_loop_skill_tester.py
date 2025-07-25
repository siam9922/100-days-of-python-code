# WHILE LOOP BEGINNER SKILL TESTER - MINI PROJECT
# (Based on Angela Yu's Course - Day 6 Level)
#=============================================================================
# PROJECT: "Simple Games Collection"
#
# OBJECTIVE: Test your while loop skills using only Day 1-6 concepts
#
# REQUIREMENTS:
# 1. Ask user for their name 
# 2. Create a simple counting game (count from 1 to their chosen number)
# 3. Make a "guess my number" game (you pick 1-10, they guess)
# 4. Create a password game (keep asking until they type "secret")
# 5. Build a simple menu that keeps running until they choose "exit"
#
# CONCEPTS YOU'LL USE (Day 1-6 Only):
# - while loops with simple conditions
# - if/elif/else statements
# - input() and print()
# - Variables and basic math
# - Lists (basic usage)
# - Random module (from Day 4)
#
# EXAMPLE OUTPUT:
# "Hi Alice! Welcome to the games!"
# 
# "=== COUNTING GAME ==="
# "Count to what number? 5"
# "Let's count: 1, 2, 3, 4, 5. Done!"
#
# "=== GUESSING GAME ==="
# "I'm thinking of a number 1-10..."
# "Your guess: 7"
# "Too high!"
# "Your guess: 4" 
# "Correct!"
#
# "=== PASSWORD GAME ==="
# "Enter the secret password: hello"
# "Wrong! Try again."
# "Enter the secret password: secret"
# "Access granted!"
#
# DEBUGGING TIPS:
# - Watch out for infinite loops!
# - Use simple conditions like: while answer != "exit"
# - Test your exit conditions
# - Keep it simple - no complex logic needed
#=============================================================================

# YOUR CODE STARTS HERE:

name = input("What is your name? ")
value = (int(input("Pick a number to use: ")))
print(f"Hi {name}! Welcome to the games! ")

print("\n===COUNTING GAME===")
print(f"Count to what number: {value}")
print(f"Let's count: ", end="")

count = 1
while count <= value:
    print(count, end=", ")
    count += 1
print(f"Done!")

import random
print("\n===GUESSING GAME===")
print(f"I am thinking of a number between 1-10...")
computer_guess = random.randint(1,10)
user = int(input("Your guess is: "))

while user != computer_guess:
    if user < computer_guess:
        print("Too Low!")
        new_guess = int(input("Your guess is: "))
        user = new_guess
    else:
        print("Too High!")
        new_guess = int(input("Your guess is: "))
        user = new_guess
print("Correct")

print("\n===PASSWORD GAME===")        
password = "secret"
secret_password = input("Enter the secret password: ")

while secret_password != password:
    print("Wrong! Try again")
    retry_password = input("Enter the secret password: ")
    secret_password = retry_password    
print("Access Granted!")