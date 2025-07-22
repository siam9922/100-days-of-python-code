# -----------------------------------------------
# Mini Project: “Number Classifier 9000”
# -----------------------------------------------

# DESCRIPTION:
# Loop through a list of numbers and classify each one.
# For every number, determine:
# - If it is even
# - If it is odd
# - If it is divisible by both 3 and 5
# - (Optional) If it is a prime number
# Print a message for each number explaining what type it is.
# After processing all numbers, display a summary count of:
# - Even numbers
# - Odd numbers
# - Numbers divisible by both 3 and 5
# - (Optional) Prime numbers

# SAMPLE OUTPUT:
# -----------------------------------------------
# Analyzing list of numbers...
# 17 is odd
# 18 is even
# 15 is divisible by both 3 and 5
# 7 is prime and odd
# 20 is even
#
# SUMMARY:
# Evens: 2
# Odds: 2
# Divisible by both 3 and 5: 1
# Primes: 1
# -----------------------------------------------

# REQUIREMENTS:
# - Use a predefined list of numbers
# - Use a for loop to process each number
# - Use if/elif/else statements to:
#   - Check if a number is even or odd
#   - Check if a number is divisible by both 3 and 5
# - Use counters to keep track of each category
# - Print clear formatted messages for each result

# EXTRA CHALLENGE:
# - Use a for loop to check if a number is prime
# - Do not use functions or import statements
# - Stay within concepts from Day 1 to Day 5


print("WELCOME TO NUMBER CLASSIFIER 1000")
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 
            10, 11, 12, 13, 14, 15]



prime_count = 0
even_count = 0
odd_count = 0
divisible_count = 0

for num in num_list:

    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} is divisible by 3 and 5")
        divisible_count += 1 

    elif num % 2 == 0:
        print(f"{num} is Even")
        even_count += 1

    else:
        print(f"{num} is Odd")
        odd_count += 1  #Keeps track of the loop with the counters

    for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
    else:
       print(num,"is a prime number")
       prime_count += 1 


print("\n--- SUMMARY ---")
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
print(f"Divisible by 3 and 5: {divisible_count}")
print(f"Prime numbers: {prime_count}")