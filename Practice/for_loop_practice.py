# import random

# letters = ['a', 'b', 'c', 'd', 'e']

# # Step 1: Make an empty string to store the password
# # Step 2: Loop 3 times using range()
# # Step 3: In each loop, choose a random letter from the list
# # Step 4: Add it to the password string
# # Step 5: Print the password at the end

# password = ""

# for letter in range(1,4):
#     letter = random.choice(letters)
#     password += letter

# print(password)

# # STEP-BY-STEP SYMBOL TASK

# # Step 1: You already have a password that contains letters.

# # Step 2: Now you need to add 2 random symbols to that same password.

# # Step 3: Use a for loop that runs 2 times.

# # Step 4: In each loop:
# #   - Use random.choice() on the 'symbols' list to get a random symbol.
# #   - Add that symbol to the existing password string using +=

# # Step 5: After the loop is done, print the final password just once.

# # Provided symbols list:

# symbols = ['!', '@', '#', '$', '%']

# for symbol in range(3):
#     symbol = random.choice(letters)
#     password += symbol
# print(password)


# # QUESTION: Lucky Draw Picker

# # DESCRIPTION:
# # You have a list of participants. Write a program that randomly selects 3 **different** names from the list
# # and combines them into a single string called `winners`. Each name should be separated by a space.
# # Then print the `winners` string.

# # PROVIDED LIST:
# import random

# participants = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George']

# winners = ""
# for human in range(3):
#     human = random.sample(participants)
#     winners += human + " "
# print({winners})



# 1. Print all numbers from 1 to 10
# Your code:

print("Question 1:")
for num in range(1, 11):
    print(num)



# 2. Print each letter in the word "python"
# Your code:

print("Question 2:")
word = "python"
for letter in word:
    print(letter)




# 3. Print only even numbers from 2 to 20
# Your code:

num = 0
print("Question 3:")
for num in range(2, 21, 2):
    print(num)


# 4. Loop through a list of names and print only the ones longer than 4 characters
# names = ["Sam", "Jordan", "Lily", "Chris", "Amy", "Stephanie"]
# Your code:

print("Question 4:")
names = ["Sam", "Jordan", "Lily", "Chris", "Amy", "Stephanie"]

name = 0
for name in names:
    if len(name) > 4 :
        print(name)


# 5. Print every second number from 10 to 0 going backwards
# Your code:

print("Question 5:")
for num1 in range(10, 0, -1):
    if num1 % 2 == 0:
        print(num1)





# 6. Print each item in this list on a separate line with a dash in front: 
items = ["apple", "banana", "orange"]
# Your code:
print("Question 6:")
for fruit in items:
    print("-", fruit)
   






# 7. Use a for loop to add up all the numbers in this list and print the total
numbers = [5, 8, 12, 3, 7]
# Your code:

print("Question 7:")
total = 0
for num in numbers:
    total += num
print(total)




# 8. Print the square of each number from 1 to 5
# Your code:
import math

print("Question 8:")

for num in range(1, 5):
    print(num**2)




# 9. Loop through the string "success" and print each character only once (no duplicates)
# Your code:


print("Question 9")
word = "success"
for letter in word:
    print(letter)





# 10. Print a countdown from 5 to 1, then print "Blast off!" after the loop ends
# Your code:

print("Question 10:")
num = 0
for num in range(5):
    print(num)
print("Blast off")




#Instructor Notes
#------------------------------------------------------------------------------------------
# The program will ask:

# How many letters would you like in your password?
# How many symbols would you like?
# How many numbers would you like?
# The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.

# Demo
# https://appbrewery.github.io/python-day5-demo/

# Easy Version
# Generate the password in sequence. Letters, then symbols, then numbers. If the user wants

# 4 letters 2 symbols and 3 numbers then the password might look like this:

# fgdx$*924

# You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.

#  Hint 1 
# Remember you can use the random.choice() function to get a random item from a List! But you need to import the random module first.
# Hard Version
# When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:

# x$d24g*f9

# And every time you generate a password, the positions of the symbols, numbers, and letters are different. This will make the password more difficult for hackers to crack.

# The essential skill of a good programmer is using Google to find what you need. Your brain is for thinking, not memorising functions! You will need to Google to solve this project on the hard level. If you get stuck, check the hint below for what to Google.

#  Hint 2 
# Try googling: "How to shuffle items in a List in Python"
#------------------------------------------------------------------------------------------


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for char in range(0, nr_letters):
    password += random.choice(letters)
    
for char in range(0, nr_symbols):
    password += random.choice(symbols)
   
for char in range(0, nr_numbers):
    password += random.choice(numbers)
   
print(password)