"""
Author: Morgan Browning
Date: 01/24/2025
Assignment: Module 02 Practice Exercise 3-10

This program calculates and displays a payment schedule for a loan, based on the purchase price provided by the user.
"""

# Inputs
purchase_price = float(input("Enter the purchase price: "))

# Constants
ANNUAL_RATE = 0.12
MONTHLY_RATE = ANNUAL_RATE / 12
DOWNPAYMENT_RATE = 0.10
MONTHLY_PAYMENT_RATE = 0.05

# Initialize variables
down_payment = purchase_price * DOWNPAYMENT_RATE
monthly_payment = purchase_price * MONTHLY_PAYMENT_RATE
balance = purchase_price - down_payment
month = 1

# Output: Table header
print(f"{'Month':<8}{'Start Balance':<15}{'Interest':<12}{'Principal':<12}{'Payment':<10}{'End Balance':<12}")
print("-" * 65)

# Loop: Calculate and display schedule
while balance > 0:
    # Calculate interest
    interest = balance * MONTHLY_RATE

    # Adjust payment if it's the last payment
    if monthly_payment > balance:
        monthly_payment = balance + interest

    # Calculate principle and ending balance
    principal = monthly_payment - interest
    end_balance = balance - principal

    # Display the details for the current month
    print(f"{month:<8}{balance:<15.2f}{interest:<12.2f}{principal:<12.2f}{monthly_payment:<10.2f}{end_balance:<12.2f}")

    # Update balance and increment month
    balance = end_balance
    month += 1
    