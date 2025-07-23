# 🧠 Mini Challenge: Number Guessing Game

# 1. Import the 'random' module so you can generate a random number.

# 2. Generate a random number between 1 and 10 and store it in a variable (e.g., secret_number).

# 3. Create a variable to keep track of how many guesses the user has made.

# 4. Print a welcome message to the user.

# 5. Use a while loop to let the user keep guessing until they guess correctly.

    # Inside the loop:
    # - Ask the user to guess a number between 1 and 10 using input().
    # - Convert the input to an integer.
    # - Add 1 to the guess counter.
    # - If the guess is correct:
        # - Print a success message and show how many guesses it took.
        # - Use break or change the condition to end the loop.
    # - If the guess is wrong:
        # - Tell the user it's wrong and let them guess again.

# 🏁 Done! You’ve built a basic guessing game using a while loop.


import random

secret_number = random.randint(1, 10)
guess_tracker = 0

print("WELCOME TO THE NAME GUESSING GAME USER!")


while guess_tracker < 10:
    random_number = (int(input("Guess any number between 1 to 10: ")))
    guess_tracker += 1
    if random_number == secret_number:
        print(f"Good Job! you got the guess.")
        print(f"This is how many times it took {guess_tracker}")
        break
    else:
        print("The guess is wrong!")
        answer = input("Do you want to play again? Y/N ")
        if answer == 'N':
           break
        
        