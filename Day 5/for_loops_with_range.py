
#Instructor Notes
#------------------------------------------------------------------------------------------
# The combination of the range() function with the Python For Loop allows us to run a loop for as many times as we wish. Instead of looping through each item in a List, we can loop through a range of numbers.

# Range Function
# range(1, 10)

# This code doesn't do anything by itself. For example, if you tried to print it, it would not give you individual numbers.

# But it can be used in conjunction with For Loops. e.g.

# for number in range(1, 10):
#     print(number)
# This will print out each of the numbers 1 - 9. So the range can also be expressed like this:

# a <= range(a, b) < b

# Where the range of numbers is inclusive of the lower bound but not inclusive of the upper bound.

# PAUSE 1 - The Gauss Challenge
# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.
#------------------------------------------------------------------------------------------

# Range Function with for loop

# for number in range(1, 10):
#     print(number)

#Task 1: Work out the total of the numbers
# between 1 and 100, inclusive of both 1 and 100.

# amount = 0
# for i in range (1, 101):
#     amount += i
# print(amount)


#"i" is the int from the range and since amount is 0 it adds together.

# Programmer Notes
# -------------------------------------------------------------------------------------------------------------------------------------

"""
- When you use the range function, it does not include the last digit.
  For example, range(1, 10) will go from 1 to 9.

- The range function doesn't do anything on its own—you need to use it in something like a loop.

- You can also add a step. For example, range(1, 10, 3) will give: 1, 4, 7.
"""

# -------------------------------------------------------------------------------------------------------------------------------------


# FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"


#Challenge FizzBuzz Code:
for number in range(1, 101):
    if number % 3 == 0 and number % 5 ==0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
