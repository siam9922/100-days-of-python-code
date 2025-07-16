#=============================================================================
# DAY 2 FUNDAMENTALS REVIEW PROJECT
# Personal Finance Calculator
#=============================================================================
# This project combines all Day 2 concepts:
# - Data Types (str, int, float, bool)
# - Mathematical Operations (+, -, *, /, //, **)
# - Type Conversion (int(), float(), str())
# - Type Checking (type())
# - Number Manipulation (round(), int())
# - PEMDAS/Order of Operations
# - f-strings for formatting
# - Assignment Operators (+=, -=, etc.)
#=============================================================================

# PROJECT: Personal Budget & Expense Calculator
# 
# Create a comprehensive financial calculator that helps someone manage their money.
# This will reinforce all your Day 2 learning!
#
# REQUIREMENTS:
# 1. Welcome message and collect user's name
# 2. Ask for their monthly income (convert to float)
# 3. Ask for their age (convert to int)
# 4. Collect 3 different monthly expenses:
#    - Rent/Housing (float)
#    - Food budget (float) 
#    - Entertainment budget (float)
# 5. Calculate total expenses using mathematical operations
# 6. Calculate remaining money (income - expenses)
# 7. Calculate what percentage of income is spent (use division and multiplication)
# 8. Use PEMDAS to calculate a "savings recommendation" formula:
#    savings_goal = (income - expenses) * 0.2 + 100
# 9. Use type checking to show data types of key variables
# 10. Use number manipulation (round(), int()) to format money values
# 11. Use f-strings to display a formatted budget report
# 12. Use assignment operators (+=) to add a bonus to their savings if they're under 25
#
# BONUS CHALLENGES:
# - Add error checking by using type() to verify inputs
# - Create a "financial health score" using complex mathematical formulas
# - Use boolean logic to determine if they're "financially healthy" (True/False)
# - Add more expense categories and let user choose how many to enter
# - Calculate daily/weekly spending averages using division
# - Use ** (exponent) to calculate compound interest on their savings
#
# EXAMPLE OUTPUT:
# "Hi John! Here's your financial summary:
# Monthly Income: $3,500.00
# Total Expenses: $2,800.00
# Money Left: $700.00
# You spend 80.0% of your income.
# Recommended savings: $240.00"
#
# Remember to practice:
# - Converting between data types
# - Using all mathematical operators
# - Applying PEMDAS correctly
# - Formatting numbers with round()
# - Using f-strings for clean output
#=============================================================================

print("WELCOME TO THE PERSONAL FINANCE  CALCULATOR\n")
name = input("Enter your name: ")
income = float(input("Enter your monthly income: "))
age = int(input("Enter your age: "))
monthly_expense1 = float(input("Enter your monthly expense for rent: "))  
monthly_expense2 = float(input("Enter your monthly expense for food: ")) 
monthly_expense3 = float(input("Enter your monthly expense for housing: "))

total_expenses = float(monthly_expense1 + monthly_expense2 + monthly_expense3)
remaining_income = income - total_expenses
percentage_of_income = ((total_expenses/income) * 100)
savings_goal = (income - total_expenses) * 0.2 + 100


print(f"\nHi {name}! Here's your financial summary!")
print(f"Monthly Income: ${round(income, 2)}")
print(f"Total Expenses: ${round(total_expenses, 2)}")
print(f"Remaining Income: ${round(remaining_income, 2)}")
print(f"You spent {percentage_of_income}% of your income")
print(f"Recommended Savings Goal: ${round(savings_goal, 2)}")