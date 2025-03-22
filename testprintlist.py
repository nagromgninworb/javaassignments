"""
Author: Morgan Browning
Date: 02/17/2025
Assignment: Module 05 Practice Exercise 7-5

This script tests a recursive function that prints all elements in a sequence 
and traces the argument passed during each call.

The `printAll()` function prints the first element, then calls itself with the 
remaining elements, stopping when the sequence is empty.
"""

# Recursive function with argument tracing
def printAll(seq):
    if seq:
        # Print the current sequence and the first element
        print(f"Calling printAll() with sequence: {seq}")
        print(seq, "->", seq[0])

        # Recursive call with the rest of the sequence
        printAll(seq[1:])


# Test the function with a sample list
test_sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Testing printAll() with:", test_sequence)
printAll(test_sequence)
