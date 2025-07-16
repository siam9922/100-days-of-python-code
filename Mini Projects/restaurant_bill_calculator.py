
#=====================================================================
# Project: Restaurant Bill Calculator
# Project Description:
# Create a program that calculates the total cost of a restaurant bill including tax and tip, then splits it among friends.

# What You'll Practice:
# Data Types: Get user input as strings, convert to numbers
# Mathematical Operations: Addition, multiplication, division using PEMDAS
# Number Manipulation: Round final amounts to 2 decimal places
# F-strings: Display results in a clean format


# Required Inputs:
# Bill amount (before tax)
# Tax percentage (e.g., 8.5 for 8.5%)
# Tip percentage (e.g., 18 for 18%)
# Number of people splitting the bill

# Calculations Needed:
# Tax Amount = Bill × (Tax % ÷ 100)
# Tip Amount = Bill × (Tip % ÷ 100)
# Total Bill = Bill + Tax + Tip
# Per Person = Total ÷ Number of People

# Sample Output:
# Bill Amount: $45.00
# Tax (8.5%): $3.83
# Tip (18%): $8.10
# Total: $56.93
# Split 4 ways: $14.23 per person

# Bonus Challenge:
# # Show the step-by-step math calculations using f-strings and demonstrate type conversion by showing the data types before and after conversion.
#=====================================================================

print("WElCOME TO SIAM'S RESTAURANT\n")
bill = float(input(("Enter your bill: ")))
tax_percentage =  float(input("Type a percentage between 1-10%. Enter a tax percentage: "))
tip_percentage = float(input("Type a percentage between 10-20%: Enter the tip amount: "))
splitting_bill = int(input("Enter how many people are splitting the bill: "))

tax_amount = bill * (tax_percentage / 100)
tip_amount = bill * (tip_percentage / 100)
total_bill = bill + tax_amount + tip_amount
per_person = total_bill / splitting_bill

#Bonus
print("\nHow formula's were calculated?")
print(f"Tax Calculation: \"{bill}\" x ({tax_percentage} ÷ 100) = {tax_amount}  ")
print(f"Tip Calculation: \"{bill}\" x ({tip_percentage} ÷ 100) = {tip_amount}  ")
print(f"${bill} + {tip_amount} + {tax_amount} = ${total_bill}")


print("SUMMARY")
print(f"\nBill Amount: ${bill}")
print(f"Tax ({tax_percentage}): ${round(tax_amount, 2)}")
print(f"Tip ({tip_percentage}): ${round(tip_amount, 2)}")
print(f"Total: {round(total_bill, 2)}")
print(f"Split {splitting_bill} ways: ${round(per_person, 2)} per person\n")