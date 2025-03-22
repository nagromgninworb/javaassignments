"""
Author: Morgan Browning
Date: 02/17/2025
Assignment: Module 05 Practice Exercise 6-6

This program defines a custom `myRange()` function that mimics Python's built-in `range()` function. 
It accepts up to three parameters: start, stop, and step, and returns a list of numbers. 
The function will handle missing parameters and default values appropriately.
"""

def myRange(start=None, stop=None, step=None):
    # Handle default values based on the number of arguments
    if stop is None and step is None:
        stop = start
        start = 0
        step = 1
    elif step is None:
        step = 1

    # Validate that step is not zero
    if step == 0:
        raise ValueError("Step cannot be zero.")

    numbers = []

    # Generate numbers for ascending or descending range
    if step > 0:
        current = start
        while current < stop:
            numbers.append(current)
            current += step

    elif step < 0:
        current = start
        while current > stop:
            numbers.append(current)
            current += step

    return numbers


# Test cases
print(myRange(10))         # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myRange(1, 10))      # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myRange(1, 10, 2))   # [1, 3, 5, 7, 9]
print(myRange(10, 1, -2))  # [10, 8, 6, 4, 2]

# Invalid step test
try:
    print(myRange(1, 10, 0))  # Step cannot be zero
except ValueError as e:
    print(f"Error: {e}")


