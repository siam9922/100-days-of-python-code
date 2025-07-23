# 🔁 WHILE LOOP COMBINATIONS REFERENCE (Written Fully in Comments)

# 🧠 BASIC STRUCTURE
# while condition_is_true:
#     do something

# ──────────────────────────────────────────────────────────────

# 1️⃣ Simple counter loop
# Count from 1 to 5

# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# ──────────────────────────────────────────────────────────────

# 2️⃣ Countdown loop
# Count from 5 to 1

# count = 5
# while count >= 1:
#     print(count)
#     count -= 1

# ──────────────────────────────────────────────────────────────

# 3️⃣ Infinite loop with break
# Keep asking the user until they say "stop"

# while True:
#     answer = input("Type 'stop' to quit: ")
#     if answer == 'stop':
#         break

# ──────────────────────────────────────────────────────────────

# 4️⃣ Input validation loop
# Ask the user to enter a number between 1 and 10

# number = int(input("Enter a number (1-10): "))
# while number < 1 or number > 10:
#     print("Invalid. Try again.")
#     number = int(input("Enter a number (1-10): "))

# ──────────────────────────────────────────────────────────────

# 5️⃣ Sentinel-controlled loop
# Loop until user enters a specific value (like 0 to quit)

# num = int(input("Enter a number (0 to quit): "))
# while num != 0:
#     print("You entered:", num)
#     num = int(input("Enter a number (0 to quit): "))

# ──────────────────────────────────────────────────────────────

# 6️⃣ While loop using a flag
# Good for handling more complex "on/off" logic

# keep_running = True
# while keep_running:
#     command = input("Enter command (q to quit): ")
#     if command == "q":
#         keep_running = False

# ──────────────────────────────────────────────────────────────

# 7️⃣ While + Function Call
# Keep looping until the function returns True

# def is_correct(answer):
#     return answer == "yes"

# while True:
#     reply = input("Say yes to continue: ")
#     if is_correct(reply):
#         break

# ──────────────────────────────────────────────────────────────

# 8️⃣ While loop with multiple conditions
# Loop while x is less than 5 AND y is greater than 0

# x = 0
# y = 3
# while x < 5 and y > 0:
#     print(x, y)
#     x += 1
#     y -= 1

# ──────────────────────────────────────────────────────────────

# ✅ USE THIS LIST WHENEVER YOU'RE STUCK
# If you're ever confused:
# - Check which type of loop you're trying to build
# - Match it to the pattern here
# - Adjust the variables or logic to fit your program
