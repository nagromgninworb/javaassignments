"""
Author: Morgan Browning
Date written: 01/19/2025
Assignment: Module 01 Programming Assignment - Part 2

This program calculates the total cost of a meal, including an 18% tip and 7% sales tax. The user is prompted to input the cost of the meal, and the program calculates and display the tip, tax, and total cost.

"""

#Ask the user to enter the charge for the food
food_charge = float(input("Enter the charge for the food: $"))

# Calculate the tip, tax, and total cost
tip = food_charge * 0.18
tax = food_charge * 0.07
total_cost = food_charge + tip + tax

#Display the results
print(f"Tip amount: ${tip:.2f}")
print(f"Tax amount: ${tax:.2f}")
print(f"Total cost: ${total_cost:.2f}")

