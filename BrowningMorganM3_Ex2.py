"""
Author: Morgan Browning
Date written: 01/30/2025
Assignment: Module 3 Programming Assignment Part 2

This program generates a series of random numbers and writes them to a file. The user specifies how many numbers should be generated. Each number is between 1 and 500. The program then displays the numbers on the screen.
"""

import random 

# Ask the user how many numbers to generate
num_count = int(input("Enter the number of randome numbers to generate: "))

# Generate the random numbers and store them in a list
random_numbers = [random.randint(1, 500) for _ in range(num_count)]

# Open a file to write the numbers
with open("random_numbers.txt", "w") as file:
    # Write each number to the file, one per line
    for number in random_numbers:
        file.write(f"{number}\n")

# Display the random numbers on the screen
print("Random numbers generated:")
for number in random_numbers:
    print(number)
    
