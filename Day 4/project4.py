
#ROCK PAPER SCISSORS PROJECT

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
print("You chose:\n")
if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
elif choose == 2:
    print(scissors)
else:
    print("Invalid input")

print("Computer Chose: \n")
computer_chose = random.choice([rock, paper, scissors])
print(computer_chose)

if choose == 0 and computer_chose == scissors:
    print("You won")
elif choose == 1 and computer_chose == rock:
    print("You won")
elif choose == 2 and computer_chose == paper:
    print("You won")
elif choose == 0 and computer_chose == rock:
    print("It's a draw")
elif choose == 1 and computer_chose == paper:
    print("It's a draw")
elif choose == 2 and computer_chose == scissors:
    print("It's a draw")
else:
     print("You lost. Computer won!")