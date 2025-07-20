# -----------------------------------------------
# 🎮 Mini Project: “Mood Machine 3000: Deluxe Overdrive Edition”
# -----------------------------------------------

# 📄 DESCRIPTION:
# You’re building a futuristic sass-powered mood analyzer.
# The user enters their name, and the Mood Machine delivers:
# - A randomly selected **mood**
# - A mood-specific **action** (custom to that mood)
# - A random **bonus message** for extra flavor
# - Option to **run again** or exit the simulation
# - Secret **easter egg behavior** if a special name is entered
# - (Optional) A silly emoji-based **Mood Meter** to represent the vibe visually

# 🖥️ SAMPLE OUTPUT:
# -----------------------------------------------
# WELCOME TO MOOD MACHINE 3000: DELUXE OVERDRIVE EDITION!
# What's your name? > Siam

# 🎯 Mood Detected: Chaotic
# 🧠 Advice: Rearrange your room at 3am. Trust the process.
# 💬 Bonus Message: No refunds.
# 📊 Mood Meter: [💥💥💥💥💥💥💥]

# Siam, go conquer the chaos.

# Wanna go again? (Y/N): >
# -----------------------------------------------

# ✅ REQUIREMENTS:
# - Use input() to get the user’s name
# - Use the random module
# - Use lists to store:
#     - Moods
#     - Mood-specific actions
#     - Bonus messages
# - Use conditionals (if/elif) to:
#     - Choose the action based on the selected mood
#     - Show secret content if a specific name is entered
# - Use a loop to let the user run the program multiple times
# - Use string formatting to display custom messages
# - (Optional) Add an emoji “Mood Meter” based on the mood

# 🚀 EXTRA CHALLENGE:
# - Keep it all under Day 1–4 concepts (no functions, no imports beyond random, no advanced stuff)

import random

print("WELCOME TO MOOD MACHINE 3000!\n")

name = input("What is your name? ")

mood = ["tired", "excited" , "chaotic" , "lazy", "grumpy"]
mood = random.choice(mood)

tired = ["Go to Sleep", "Drink Coffee", "Take a Break"]
excited = ["Eat favorite meal", "Play Games", "Hangout with friends"]
chaotic = ["Breathe", "Self-talk", "Practice your skills"]
lazy = ["Do a small task", "Go outside", "Clean your room"]
grumpy = ["Go for a walk", "Buy Popeye's", "Do coding"]


action = [tired, excited, chaotic, lazy, grumpy]

if mood == "tired":
    action = random.choice(tired)
    print(action)
elif mood == "grumpy":
    action = random.choice(grumpy)
    print(action)
elif mood == "excited":
    action = random.choice(excited)
    print(action)
elif mood == "lazy":
    action = random.choice(lazy)
    print(action)
elif mood == "chaotic":
    action = random.choice(chaotic)
    print(action)


option = input("Do you want to stay or leave? Pick Y/N")
if option == "Y":
    print("You have exited the program!")
else:
    print("We will provide updates to your mood!")

print(f"WELCOME TO MOOD MACHINE 3000!")
print(f"Name: {name}")
print(f"Mood Detected: {mood.capitalize()}")
print(f"Action Needed: {action}")
print(f"Bonus Message: Gotta stay healthy brother.")

