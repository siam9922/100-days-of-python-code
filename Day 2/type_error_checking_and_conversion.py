#Instructor Notes
#-------------------------------------------------------------------------------------------------------------------------------------
# TypeError
# These errors occur when you are using the wrong data type. e.g. len(12345)

# Because you can only give the len() function Strings, it will refuse to work and give you a TypeError if you give it a number (Integer).

# PAUSE 1. Fix the len() function so it has no more warnings or errors.
# Type Checking
# You can check the data type of any value or variable in python using the type() function.

# print(type("abc")) #will give you <class 'str'>

# PAUSE 2. Write out 4 type checks to print all 4 data types
# Using the type() and print() functions to print out 4 lines into the output area so we get the full collection of data types that we learnt about. <class 'str'> <class 'int'> <class 'float'> and <class 'bool'>

# Type Conversion
# You can convert data into different data types using special functions. e.g.

# float()

# int()

# str()

# PAUSE 3. Make this line of code run without errors
# print("Number of letters in your name: " + len(input("Enter your name")))
#-------------------------------------------------------------------------------------------------------------------------------------



#Task 1: Fix the len function
print(len("Siam"))

#How type checking works>
print(type("Hello"))

#Task 2: Use type to show data types
print(type("String"))
print(type(2))
print(type(5.14))
print(type(True))

#How typecasting works>
print(int("123") + int("456"))
int()
float()
str()
bool()

#Task 3: Make this line of code run without errors
#Check the error and figure out the mistake

name_of_the_user = str(input("Enter your name: "))
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) #str
print(type(length_of_name)) #int

print("Number of letters in your name: " + str(length_of_name) )

#Programmer Notes
#-------------------------------------------------------------------------------------------------------------------------------------

"""
- The official python documentation isn't very reliable because it 
doesn't have a lot of examples and it's very short. 
- In python each functions likes to work with certain data types 
- Value error there is an invalid literal for the int which is abc

"""

#-------------------------------------------------------------------------------------------------------------------------------------