# 🎯 Simple Challenge: "Personal Assistant Bot"
# 
# Description: Create a mini personal assistant that keeps running until the user says goodbye. 
# The assistant can do different helpful tasks, and each task is its own function.
#
# What it does:
# - Greets the user and asks their name
# - Shows a menu of services (like a restaurant menu)
# - User picks what they want help with
# - Assistant does the task using the appropriate function
# - Keeps offering help until user chooses to leave
# - Says a personalized goodbye
#
# Possible services your assistant could offer:
# - Calculate how many days until their birthday
# - Generate a random motivational quote
# - Count how many vowels are in a word they give you
# - Create a simple shopping list
# - Tell them a random fact about their favorite number
# - Make a pattern with their initials
#
# The fun part: Each service is a separate function, but the while loop keeps the 
# "conversation" going. The user feels like they're chatting with a helpful bot 
# that remembers their name and keeps offering new services.
#
# Why it's cool: It feels like a real program someone might actually use, not just 
# a coding exercise. Plus you can add any creative services you want!
#
#=============================================================================

# YOUR CODE STARTS HERE:
from datetime import datetime
import random

name = input("Hello user! What is your name? ")

print("----------------")
print("|   SERVICES   |")
print("----------------")

print("========================================================")
print("A. Bot Suggestion: How many days until your birthday?   ")
print("B. Generate a random motivational quote                 ")
print("C. Count how many vowels they give you                  ")
print("D. Create a simple Shopping list                        ")
print("E. Quit                                                 ")
print("========================================================")


def days_until_birthday():
    year = int(input('When is your birthday? [YY] '))
    month = int(input('When is your birthday? [MM] '))
    day = int(input('When is your birthday? [DD] '))

    birthday = datetime(year,month,day)
    return birthday

def calculate_dates(birthday):
    now = datetime.now()
    birthday = datetime(now.year, birthday.month, birthday.day)
    return (birthday - now.today()).days + 1

def motivational_quote():

    quote1 = "\n “The only way to do great work is to love what you do.” - Steve Jobs "
    quote2 = "\n“The journey of a thousand miles begins with a single step.” - Lao Tzu"
    quote3 = "\n “It always seems impossible until it's done.” - Nelson Mandela"
    quote4 = "\n“Don't watch the clock; do what it does. Keep going.” - Sam Levenson "
    quote5 = "\n“The only person you are destined to become is the person you decide to be.” - Ralph Waldo Emerson "

    quote_list = [quote1, quote2, quote3, quote4, quote5]

    random_quote = random.choice(quote_list)
    print(random_quote)

def count_vowels():
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O' ,'U']
    Sentence = input("Enter a phrase: ")
    count = 0
    for letter in Sentence:
        if letter in vowel:
         count += 1
    print(f"The number of vowels found from sentence is {count}")

def shopping():
    
    shopping_list = []
    while True:
        item = input("Enter an item to add to your shopping list (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        shopping_list.append(item)

    print("\nYour shopping list:")
    for item in shopping_list:
        print(f"- {item}")

service = ""

while service != "E":

    service = input("\nWhat kind of services do you want? Pick any number from A-F: ")

    if service == "A":
        bd = days_until_birthday()
        days = calculate_dates(bd)
        print(f"Your birthday is in {days}")

    elif service == "B":
        motivational_quote()
        
    elif service == "C":
        count_vowels()
            
    elif service == "D":
        shopping()
    else:
        print(f"\nPick a valid input {name}")
        break

print("\nThank you for using our program!")


#How do you repeat a loop if you have a input inside the loop the loop will automatically repeat if you put on an empty string