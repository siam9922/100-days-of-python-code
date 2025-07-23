# 🔁 FOR LOOP COMBINATIONS REFERENCE (Written Fully in Comments)

# 🧠 BASIC STRUCTURE
# for variable in something:
#     do something

# ──────────────────────────────────────────────────────────────

# 1️⃣ Loop through a range (counting up)
# Print numbers 1 to 5

# for i in range(1, 6):
#     print(i)

# ──────────────────────────────────────────────────────────────

# 2️⃣ Loop through a range (counting down)
# Print numbers 5 to 1

# for i in range(5, 0, -1):
#     print(i)

# ──────────────────────────────────────────────────────────────

# 3️⃣ Loop through a list

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# ──────────────────────────────────────────────────────────────

# 4️⃣ Loop through a string (character by character)

# word = "hello"
# for char in word:
#     print(char)

# ──────────────────────────────────────────────────────────────

# 5️⃣ Loop using index (with range and len)

# numbers = [10, 20, 30]
# for i in range(len(numbers)):
#     print(f"Index {i} has value {numbers[i]}")

# ──────────────────────────────────────────────────────────────

# 6️⃣ Nested for loop
# Useful for grids, patterns, or combinations

# for row in range(3):
#     for col in range(3):
#         print(f"Row {row}, Col {col}")

# ──────────────────────────────────────────────────────────────

# 7️⃣ Loop with if-condition inside

# for i in range(1, 6):
#     if i % 2 == 0:
#         print(f"{i} is even")

# ──────────────────────────────────────────────────────────────

# 8️⃣ Loop with break
# Stops the loop early when a condition is met

# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)

# ──────────────────────────────────────────────────────────────

# 9️⃣ Loop with continue
# Skips current iteration and moves to next

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# ──────────────────────────────────────────────────────────────

# 🔁 Bonus: Loop with zip (multiple sequences at once)

# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old")

# ──────────────────────────────────────────────────────────────

# ✅ USE THIS LIST WHEN YOU GET STUCK
# These patterns cover 95% of what you'll use for loops for.
# Once you understand these, you’ll stop guessing and start recognizing them like muscle memory.
