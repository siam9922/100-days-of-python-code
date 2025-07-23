#Instructor Notes
#----------------------------------------------------------------------
# # A function in its simplest form is just a wrapper name for a block of code. You give it name and then when you call the function by that name, all the code within the function block will be executed. It can help us save time and reduce repeated code.

# Defining a new Function
# def <function name>():
#     print("Hello")
#     # Do something else
#     # Do something else ...
# Calling a Function
# Calling a function just means triggering the function. We can call a function at any point in our code in Python.

# <function name>()
# Putting everything together e.g.

# #Creating the function
# def get_user_name():
#     name = input("What is your name? ")
#     print("Hello, " + name)
#     # Inside the function

# #Outside the function
# print("Hello")
# get_user_name() # Calling the function
# This code will result in the following sequence of output:

# Hello
# What is your name? #I type Angela
#----------------------------------------------------------------------


# ------------------------ #
#        FUNCTIONS         #
# ------------------------ #

#  Built-in Functions
print("Hello")
num_char = len("Hello")
print(num_char)


#  Own Function (User-defined)
def my_functions():
    print("Hello")
    print("Bye")

#  Calling the function
my_functions()


# ----------------------------- #
#   HURDLE LOOP CHALLENGE       #
# ----------------------------- #
# Used with Reeborg's World

#  Repeated action made reusable
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

#  Option A: Break on a condition
# for robot in range(1, 13):
#     jump()
#     if robot == 6:
#         break

#  Option B: Simpler fixed loop
# for step in range(6):
#     jump()



# ----------------------------- #
#         WHILE-LOOPS           #
# ----------------------------- #

#switching out of the for loops in the hurdles challenge we do this

# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)



# ----------------------------- #
#   HURDLE LOOP CHALLENGE   2   #
# ----------------------------- #

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#

# while not at_goal():
#     jump()

#  You could use this != or not

# while at_goal() != True:
#     jump()



# ----------------------------- #
#   HURDLE LOOP CHALLENGE   3   #
# ----------------------------- #

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# def avoid_wall():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# while not at_goal():
#     if wall_in_front():
#         avoid_wall()
#     else:
#         move()


# ----------------------------- #
#   HURDLE LOOP CHALLENGE   4   #
# ----------------------------- #

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# def avoid_wall():
#     turn_left()
#     while wall_on_right():
#         move()
#
#     turn_right()
#     move()
#     turn_right()
#
#     while front_is_clear():
#         move()
#     turn_left()
#
#
# while not at_goal():
#     if wall_in_front():
#         avoid_wall()
#     else:
#         move()

# ------------------------------- #
#       PROGRAMMER NOTES          #
# ------------------------------- #

"""
 FUNCTION NOTES:

- When creating functions, we use the keyword `def` (stands for "define").

- Syntax: def function_name():
             # indented block of code

- Functions are created ahead of time to run **only when needed** (called using my_function()).

- Benefits:
   Reusability — write once, use many times.
   Cleaner code — break big problems into small steps.
   Readability — gives purpose to code blocks.

- Tip: To indent a whole block of code, highlight it and press Tab.

- When we test while loops we always set a condition after the while, then colon. 
  Basically it would just repeat the cycle until the condition becomes false.
  
- How do we know when to use a for loop or while loop:
    for loops are good for iterating 
    something with each thing your iterating over.
    
    Ex. 
    
    fruits = ["Apple", "Pear", "Orange"]
    for fruits in fruits:
        print(fruit)
        
    for n in range(1, 6):
        print(n)
    
    while loops are good when you don't care if your 
    in a list or just wanna carry out a simple functionality.
    
    while loops are more dangerous because in for loops your 
    setting up how many times something will run. It will stop when 
    it reaches the item. But while loops will run until it reaches false. 
    
    If the while loop never reaches true it will turn into an infinite loop

"""
