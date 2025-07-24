# 🚀 Mini Project: Countdown with a Twist (For Loop Edition)

# 📄 Description:
# This program will count down from 5 to 1 using a for loop.
# After the countdown, it will print "Blast off!"

# ✅ Requirements:
# - Use a for loop that counts DOWN from 5 to 1
# - Print each number on its own line
# - After the loop ends, print "Blast off!"
# - Use range() with a negative step to go backwards

# 🖥️ Sample Output:
# 5
# 4
# 3
# 2
# 1
# Blast off!

# 🧩 Steps:
# 1. Start a for loop using range() from 5 down to 1 (inclusive)
#    - Example: range(start=5, stop=0, step=-1)
# 2. Inside the loop, print the current number
# 3. After the loop is done, print "Blast off!"


num = 5
for num in range(5, 0, -1):
    print(num)
print("Blast off!")
