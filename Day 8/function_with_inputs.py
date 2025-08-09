#Instructor Notes
#------------------------------------------------------------------------------------------

# Previously, we've seen that functions allow us to package code into a named block which can be used repeatedly at a later point.

# PAUSE 1 - Review
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# Inputs
# By adding a variable name inside the parentheses when we create (define) a new function, it allows that function to take inputs when called.

# That means we can modify how the function behaves each time by passing in different inputs.

# # Creating the function
# def myFunction(input):
#     print(f"Hey! {input}")
# # Using the function
# myFunction("Tommy") 
# # Will output "Hey! Tommy"
# Inputs are Variables
# When you create a function with inputs, you are defining a variable name that will be given to the data that is passed in.

# The name of the input variable, e.g. name in this code here: def greet(name): is called the parameter.

# The value of the value of the input variable, e.g. Angela when you call the previous g

#------------------------------------------------------------------------------------------




# def greet():
#     print("My name is Siam Hasan")
#     print("I love Popeyes. It helps me survive.")
#     print("I have a friend who is getting master's degree in concrete building.")
# greet()

#Function that allows for inputs

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")

greet_with_name("Angela")






#Programmer Notes

# Functions are really handy ways of taking a complex set of instructions and packaging it
#with a block of code that has a name given to it

#To give functions input we can add a variable inside the parenthesis.
#The data you put inside the parenthesis needs to be declared in order to be used.
#I am assuming when you call the function

#Parameter and Arguments (something = 123)
#The argument is the actual piece of data
#that's going to be passed over to this function

#The parameter is the name of that data. We use the parameter inside the function
# to refer to it and do things with it

#Struggled with we can 100% convert data types inside functions

#What I learned

#We don't have to print the function when we call it. You will still get all the things inside.
#The way the parenthesis work -> when we add a variable name inside the
#function parameter, the variable gets defined when we call.
# Ex. Used name variable but when we typed "Angela" in the name call
# function Angela becomes the data that name will use