# ===========================
# Challenge: PIN Code Lock
# ===========================

# Scenario:
# You're building a digital lock system that requires the user to enter the correct 4-digit PIN to unlock.

# Task:
# 1. Set a fixed 4-digit PIN (e.g., 4321).
# 2. Prompt the user to enter the PIN.
# 3. Use a while loop to keep asking for the PIN until the correct one is entered.
# 4. If the input is incorrect, print "Incorrect PIN. Try again."
# 5. If the correct PIN is entered, print "Access granted. Welcome!"

# Bonus:
# - Count how many attempts the user took to get the PIN right.
# - After 5 incorrect attempts, lock the user out by printing "Too many incorrect attempts. Access denied." and end the loop.


#Sets a fixed PIN number
fixed_pin = 2478                    

#Enter the 4 digit PIN from an input
type_pin = int(input("Please Enter the 4-digit PIN: "))

#Sets one variable to track the loop and another to lock the counter after a certain number of attempts
counter = 1
max_attempts = 5 

#When the type pin is not equal to fixed pin
#The loop checks if the typed pin is right
while type_pin != fixed_pin:

    #Typing the input again to loop 
    type_pin = int(input("Enter the PIN once more: "))

    #This is the condition that checks if the loop is right
    if type_pin != fixed_pin:
        print("Incorrect PIN. Try again.")                #Print incorrect when the if is not equal
        counter += 1                                      #When the PIN is wrong add it to the counter
        print(f"Attempts used: {counter}/{max_attempts}") #Prints the counter and the max number attempts

    #This condition checks if the counter reached a certain limit which is max_attempts
    if counter == max_attempts: 
        #prints the condition when the attempt limit is reached                          
        print("Too many incorrect attempts. Access denied.") 
        break  #To stop the loop
#Ending the loop completely if the PIN is correct
else:
    print("Access granted. Welcome!")




#What I learned:
# To write cleaner code, you can use "not in" to check if a value is not part of a group.
# "not in" works with non-integers like strings, lists, and other iterable types.
# Instead of using else, you can place your condition at the end of the loop to control when it exits.
# The "in" keyword is used to check for membership in iterables such as strings, lists, or tuples.
