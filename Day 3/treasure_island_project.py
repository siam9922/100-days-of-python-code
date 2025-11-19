#Instructor Notes
#------------------------------------------------------------------------------------------
# Your goal today is to build a "Chose your own adventure game". Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.

# Use the flow chart linked here to create the game logic.

# Once you've completed the project, you can always extend the game and make it more interesting!

#  Hint 
# Demo
# https://appbrewery.github.io/python-day3-demo/

#------------------------------------------------------------------------------------------


#PYTHON DAY 3: FINAL PROJECT

#Search ASCII Art to find art like this
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')



print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go?")
road = input("Type 'left' or 'right'\n ").lower()

if road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")

    choice_1 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if choice_1 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")

        choice_2 = input("One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if choice_2 == "yellow":
            print("You Win!")
        elif choice_2 == "red":
            print("GAME OVER. Burned by fire!")
        elif choice_2 == "blue":
            print("GAME OVER. Eaten by beasts.")
        else:
            print("GAME OVER. You chose a door that doesn't exist.")

    elif choice_1 == "swim":
        print("GAME OVER. Attacked by trout.")
else:
    print("GAME OVER: You fell into a hole!")




# Programmer Notes
#--------------------------------------------------------------------------------------

# - Multi-Block string is another way to comment. If you want to cover something
#   like the art above you need triple quotations.

# - Sometimes in python double quotes are used normally for a sentence, and it overlaps
#   with the string quotation. To counter this we use a "\" backlash to escape the quotation.
#   So that it doesn't intercept it as code. For Example:
#   print('You\'ve come to a lake. There is an island in the middle of the lake.')

# - .lower() is used to make sure whatever letter we enter it will always be in lowercase.

# - The else case can work as long as it doesn't match the option.

# - Use elif only if the code has more options in it.