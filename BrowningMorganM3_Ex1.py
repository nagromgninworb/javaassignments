"""
Author: Morgan Browning
Date written: 01/30/2025
Assignment: Module 3 Programming Assignment Part 1

This program asks the user to enter a series of single-digit numbers without spaces.
It then calculates and displays the sum of those digits.
"""

# Ask the user to enter a series of single-digit numbers
num_string = input("Enter a series of single-digit numbers with no spaces: ")

# Calculate the sum of the digits
digit_sum = sum(int(digit) for digit in num_string)

# Display the result
print(f"The sum of digits is: {digit_sum}")


