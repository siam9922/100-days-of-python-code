# 🧮 Project: Simple Calculator with Functions and While Loop

# 1. Define four functions:
#    - add(a, b): returns the sum
#    - subtract(a, b): returns the difference
#    - multiply(a, b): returns the product
#    - divide(a, b): handles division and checks for divide-by-zero

# 2. Start a while loop that runs forever (until the user wants to quit)

# 3. Inside the loop:
#    a. Ask the user which operation they want to perform: +, -, *, or /
#    b. Ask for two numbers (convert input to float or int)
#    c. Based on the chosen operation, call the appropriate function and store the result
#    d. Print the result (or error if divide by 0)
#    e. Ask the user if they want to do another calculation (Y/N)

# 4. If the user says 'N', break the loop

# 5. After the loop ends, print a goodbye message

a = 0
b= 0

def add(a, b):
    result = a + b    # Store the calculation
    return result

def subtract(a, b):
    result = a - b    # Store the calculation
    return result

def multiply(a, b):
    result = a * b    # Store the calculation
    return result


def divide(a, b):
    result = a / b    # Store the calculation
    return result


while True:
    operation = ((input("Which operation do you want? (+, -, *, /): " )))
    a = (float(input("Type in a value for A: ")))
    b = (float(input("Type in a value for B: ")))


    if operation == "+":
        result = add(a, b)
        print(result)
        
    elif operation == "-":
        result = subtract(a, b)
        print(result)
        
    elif operation == "*":
        result = multiply(a, b)
        print(result)
        
    elif operation == "/":
        if b == 0:
            print("Error! Cannot divide by zero!")
        else:
            result = divide(a, b)
            print(result)
        
    else:
        print("Wrong input!")

    user = input("Do you want to try again? Y/N ")
    if user == "N":
        break        

print("Thanks for using the calculator! Goodbye!")