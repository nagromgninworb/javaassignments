"""

Author: Morgan Browning
Date written: 01/19/2025
Assignment: Module 01 Practice Exercise 2-1

This script calculates the surface area of a cube. The user inputs the edge length of the cube, and the program calculates and displays the surface area.
"""

# Prompt the user to input the cube's edge length
cube_edge = int(input("Enter the edge length of the cube (as an integer): "))

# Calculate the surface area of the cube
surface_area = 6 * (cube_edge ** 2)

# Display the calculated surface area
print(f"The surface area of the cube is: {surface_area} square units")

