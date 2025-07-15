#Instructor Notes
#------------------------------------------------------------------------------------------
# Your goal today is to build a "Chose your own adventure game". Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.

# Use the flow chart linked here to create the game logic.

# Once you've completed the project, you can always extend the game and make it more interesting!

#  Hint 
# Demo
# https://appbrewery.github.io/python-day3-demo/

#------------------------------------------------------------------------------------------



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
decision = input("      Type left or right: ").lower()

if decision == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")

    decision2 = input("\nType 'wait' to wait for the both. Type 'swim' to swim across. ").lower()
    if decision2 == "wait":
        print("\nYou arrived at the island unharmed. There is a house with 3 doors. "
              "\nOne red, one yellow, and one blue.")

        decision3 = input("\nWhich color do you choose? ").lower()
        if decision3 == "yellow":
            print("\nYou won! You have the treasure.")
            decision4 = input("The treasure is heavy and you have a choice to take one bag or two bags. "
                              "Type 'one bag', 'two bag' 'no bag':")

            if decision4 == "one bag" or decision4 == "no bag":
                print("\nYou have managed to escape on time!")
            else:
                print("\nThe rubble crushed you along with the treasure")

        elif decision3 == "blue":
            print("\nEaten by beasts")

        elif decision3 == "red":
            print("\nYou were burned by fire")

        else:
            print("\nGame Over: You weren't able to pick a color. ")
    else:
        print("\nYou are dead. The sharks ate you.")
else:
    print("\nYou fell in the hole to your doom!")


# Programmer Notes
# -------------------------------------------------------------------------------------------

"""
#print('She said: "Hello".')
#if you want to use double quotes as a string you should use single quotes and then double quotes inside single quotes. 
#Use this \' before a comma for example:
print('You\'re name is Siam') #This is an escape 
#If you use .lower it does make it so you can use capital and lowercase for choosing decisions
#If the paragraphs are long just put it in the next line there is no problem the code remains same.
"""

# -------------------------------------------------------------------------------------------\