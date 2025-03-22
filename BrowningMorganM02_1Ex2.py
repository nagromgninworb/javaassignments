"""
Author: Morgan Browning
Date: 01/25/25
Assignment: Module 02 Prorgamming Assignment

This program calculats the factorial of a nonnegative integer entered by the user.
"""

# Get user input
num = int(input("Enter a nonnegative integer: "))

# Validate input
if num < 0:
    print("Error: The number must be a nonnegative integer.")
else:
    # Calculate the factorial
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    # Display the result
    print(f"The factorial of {num} is {factorial}.")
