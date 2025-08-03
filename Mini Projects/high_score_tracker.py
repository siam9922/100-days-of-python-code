# ===============================
# Mini Project: High Score Tracker
# ===============================

# Scenario:
# You are given a list of student scores.
# Your task is to loop through the list and figure out which student has the highest score.

# Tasks:
# 1. Create a list called "student_scores" with several random integers (scores).
# 2. Do NOT use the built-in max() function.
# 3. Write a for loop to iterate through each score in the list.
# 4. Compare each score to a variable "highest_score" to track the highest one.
# 5. After looping through all scores, print out "The highest score in the class is: X".

# Rules:
# - You must use a for loop (no fancy shortcuts or built-ins like max()).
# - Initialize "highest_score" before the loop.
# - Each time you find a score higher than "highest_score", update it.
# - After the loop finishes, print the result.

# Bonus Challenge:
# - Can you modify it to also find the lowest score without using min()?







# Create a list of student scores
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]


# Initialize 'highest_score' to the first score in the list.
# This gives us a starting point to compare every other score.
# Initialize 'lowest_score' to the first score in the list as well.
# We'll compare all other scores to this to find the lowest one.
highest_score = student_scores[0]
lowest_score = student_scores[0]


# Start a for loop to go through each score in the 'student_scores' list
for score in student_scores:
# If the current score is higher than 'highest_score', update 'highest_score' to this score     

    if score > highest_score:
        highest_score = score
        
# If the current score is lower than 'lowest_score', update 'lowest_score' to this score   
    elif score < lowest_score:
        lowest_score = score
# If the current score is lower than 'lowest_score', update 'lowest_score' to this score

        
# After looping through all scores, print the highest score found
print(f"The highest score in the class is {highest_score}%.") 

# Also print the lowest score found
print(f"The lowest score in the class is {lowest_score}%.")



