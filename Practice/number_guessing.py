
#===============================================================================================#
# Challenge: Number Guessing Game

# Task:
# 1. Set a fixed secret number between 1 and 10 (e.g., 7).
# 2. Ask the user to input their guess using input().
# 3. Use a while loop to keep asking the user until they guess the correct number.
# 4. Inside the loop:
#    - If the guess is greater than the secret number, print "Too high. Try again."
#    - If the guess is less than the secret number, print "Too low. Try again."
# 5. Once the user guesses the number correctly, exit the loop and print "Correct! You win!"

# Bonus (optional):
# - Count how many guesses it took the user to find the correct number and print it at the end.
# - Allow the user to type "exit" to quit the game early.
# - Use a randomly generated number instead of a fixed one (you'll need the random module).
#===============================================================================================#



import random #random module                        COMMENTS FOR EACH LINE OF CODE


secret_number = random.randint(1, 10)               #Gives a random number between 1-10
print(secret_number)                                #Printing the number for testing
print("To start type an initial guess ")           #Just a message for the user
guess = int(input(("Guess the number: ")))      #Initial guess to define guess inside the loop

counter = 1                                       #We start at one since we guessed before and also                                              to have the loop to track we have to set a variable 
while guess != secret_number:                     #When guess is not equal to secret_number
    guess = int(input(("Guess the number: ")))    #We ask the guess again
                                                  
    if guess > secret_number:                     #When the guess is greater than secret_number
        print("Too high. Try again.")             #Prints too high
        counter += 1                              #If you want to track a loop user counter
        print(f"The number of guesses it took {counter}.")  #Checks how many guesses 

    elif guess < secret_number:                   #When the guess is less than secret_number
        print("Too low. Try again")               #Prints too low
        counter += 1                              # Used the counter to track in each iteration
        print(f"The number of guesses it took {counter}.") #Checks how many guesses 
                                                 
else:                                      #To complete the loop we can put else outside                 
    print("Correct! You win!")             #When user guesses the right number
    counter += 1                                  #if its correct we win
    print(f"The number of guesses it took {counter}.")




#What I learned:
#we can use else outside a if statement of a while so we can end the program
#Before we use a input like guess. For it to loop it needs to be defined and then used again in a loop
#If you want to track the loop set a variable with an input like counter = 0 and set this counter += 1 to a loop iteration to track 