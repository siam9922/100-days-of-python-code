
#Instructor Notes
#-------------------------------------------------------------------------------------------------------------------------------------
# Create a greeting for your program.
# Ask the user for the city that they grew up in and store it in a variable.
# Ask the user for the name of a pet and store it in a variable.
# Combine the name of their city and pet and show them their band name.
#  Hint 1 
# You can use String Concatenation to combine strings with variables too! e.g. print("My name is " + name)
# Make sure the input cursor shows on a new line:
#  Hint 2 
# Think about how you used \n to add a new line to a string. Try putting it in some different places in your code until it does what you expect. Note, when you click into the output area you will be able to click on the end of the line as well as the new line. See the video solution for how it looks on my system.
#-------------------------------------------------------------------------------------------------------------------------------------



#PYTHON DAY 1: FINAL PROJECT
print("Welcome to BAND NAME GENERATOR!")
user = (input("What city did you grew up in?\n"))
pet_name = input("What is the name of your pet?\n")
print(pet_name)
print("Your band name could be " +  user + " " + pet_name)