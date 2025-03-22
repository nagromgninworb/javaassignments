"""
Author: Morgan Browning
Date: 02/17/2025
Assignment: Module 05 Programming Assignment Part 1

This program calculates and displays the amount of county sales tax, 
state sales tax, and total sales tax based on user input. 
"""

# Function to calculate and display sales taxes
def calculateSalesTax():
    # Tax rates as constants
    STATE_TAX_RATE = 0.05
    COUNTY_TAX_RATE = 0.025

    # Input validation loop to ensure non-negative sales
    while True:
        try:
            total_sales = float(input("Enter the total sales for the month: $"))
            if total_sales < 0:
                print("Error: Sales cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Calculate sales taxes
    state_tax = total_sales * STATE_TAX_RATE
    county_tax = total_sales * COUNTY_TAX_RATE
    total_tax = state_tax + county_tax

    # Display the results
    print("\nSales Tax Report:")
    print(f"Total Sales: ${total_sales:.2f}")
    print(f"State Sales Tax (5%): ${state_tax:.2f}")
    print(f"County Sales Tax (2.5%): ${county_tax:.2f}")
    print(f"Total Sales Tax: ${total_tax:.2f}")


# Run the program
calculateSalesTax()
