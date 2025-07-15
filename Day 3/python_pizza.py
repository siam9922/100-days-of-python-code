#Instructor Notes
#------------------------------------------------------------------------------------------
# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1

# Example Interaction
# Welcome to Python Pizza Deliveries!
# What size pizza do you want? S, M or L: L
# Do you want pepperoni on your pizza? Y or N: Y
# Do you want extra cheese? Y or N: N
# Your final bill is: $28.


#-----------------------------------------------------------------------------------------


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0


# if size == "S":
#     bill = 15
#     if pepperoni == "Y":
#         bill += 2
#     else:
#         print("Your final bill is: $17 ")
#     if extra_cheese == "Y":
#         bill += 1
#     else:
#         bill = 15
#         print("Your final bill is: $15 ")
# elif size == "M":
#     bill = 20
#     if pepperoni == "Y":
#         bill += 3
#     else:
#         bill += 20
#         print("Your final bill is: $23 ")
#     if extra_cheese == "Y":
#         bill += 1
#     else:
#         bill = 15
#         print("Your final bill is: $20 ")
# elif size == "L":
#     bill = 25
#     if pepperoni == "N":
#         pass
#     else:
#         bill += 2
#         print("Your final bill is: $23 ")
#     if extra_cheese == "N":
#         print("Your final bill is: $25")
#     else:
#         bill += 1
#         print("Your final bill is: $28")
# else:
#     print("Please choose a size!")


#Correct Version
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Please choose the right size!")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3


if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")