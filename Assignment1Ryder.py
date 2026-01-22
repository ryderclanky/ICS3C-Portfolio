"""
===============================================
Assignment 1 – Python Programming
Student Name: Ryder Armstrong
Date: 2025-09-20

By typing my name above, I confirm that this is my own work
and I have not plagiarized or copied code from others or AI sources.
===============================================
"""

# =======================================================
# Question 1: Say Hello
# Write a program that asks the user for their name
# and prints: Hello, <name>!
# =======================================================

# --- Put your code here ---

name = str(input("Hello, What's Your Name?"))

print (f"Hey{name}")

# =======================================================
# Question 2: Adding Numbers
# Ask the user to enter two numbers. Add them together
# and print the result.
# =======================================================

# --- Put your code here ---

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print (num1 + num2) 

# =======================================================
# Question 3: Average of Three Numbers
# Ask the user to enter three numbers. Calculate the
# average and print it.
# =======================================================

# --- Put your code here ---
 
num4 = int(input("Enter first number:"))
num5 = int(input("Enter second number:"))
num6 = int(input("Finally, enter third number:"))
average = (num4 + num5 + num6 / 3) 
print("The average is:", average)


# =======================================================
# Question 4: Pizza Shop – Calculate Tax
# Ask the user to enter the total cost of their order.
# Calculate 13% tax and print the total amount including tax.
# ===============

# --- Put your code here ---

cost = input("Enter the total cost of your order: $")
total = float(cost) * 1.13
print(total)








# =======================================================
# Question 5: Ask the user to enter the length and width of a rectangle.
# Calculate the area of the rectangle.
# Print the result in a clear message.
# Remember area = length * width
# ===============

length = input("Enter the length: ")
width = input("Enter the width: ")
area = float(length) * float(width)
print("The area of the rectangle is", area)

# =======================================================
# Question 6: Tip Calculator
# Ask the user to enter the total bill amount at a restaurant.
# Ask the user to enter a tip percentage (e.g., 15 for 15%).
# Calculate the tip amount and the total bill including tip.
# Print both values clearly.
# =======================================================

# --- Put your code here ---

bill = input("Enter the total bill amount: $")
tip_percent = input("Enter tip percentage: ")
tip = float(bill) * float(tip_percent) / 100
total = float(bill) + tip
print(tip)
print(total)
