# PROJECT: Adventure Story Generator
# 
# Create a program that generates a personalized adventure story using user input.
# This project will help you practice all Day 1 fundamentals:
#
# REQUIREMENTS:
# 1. Welcome the user with a greeting message
# 2. Ask for the user's name and store it in a variable
# 3. Ask for their age and store it in a variable  
# 4. Ask for their favorite animal and store it in a variable
# 5. Ask for a magical power they'd like to have and store it in a variable
# 6. Ask for their dream destination and store it in a variable
# 7. Use string concatenation to create a short adventure story that includes:
#    - Their name as the hero
#    - Their age
#    - The animal as their companion
#    - The magical power they possess
#    - The destination as where their adventure takes place
# 8. Print the complete story with proper formatting (use \n for line breaks)
# 9. End with a personalized goodbye message
#
# EXAMPLE OUTPUT FORMAT:
# "Once upon a time, there was a brave [age]-year-old adventurer named [name].
# They had a loyal [animal] companion and possessed the amazing power of [power].
# Together, they embarked on an epic journey to [destination]..."
#
# BONUS CHALLENGES (if you want extra practice):
# - Create a cool adventure title using their name
# - Add more interactive questions for story elements
# - Use creative formatting with symbols and spacing


print("WELCOME TO THE ADVENTURE STORY GENERATOR!!!")
name = input("What is your name? ")
age = input("What is your age? ")
favorite_animal = input("What is your favorite animal? ")
magical_power = input("What magical power would you like to have? ")
dream_destination = input("What dream destination would you prefer? \n")

print("There used to be a human. In the forest living alone. His name was" + " " + name + ".\n")
print("He was around" + " " + age + " " + "years old.\n")
print("The human had a pet companion that was a" + " " + favorite_animal + ".\n")
print("The man used his power" + " " + magical_power + " " + "to feed his animal companion.\n")
print("This event took place 10 years ago in the" + " " + dream_destination + ".\n")

print("THANK YOU FOR ENJOYING THE ADVENTURE STORY GENERATOR!")

