"""
Author: Morgan Browning
Date: 01/24/2025
Assignment: Module 02 Programming Assignment

This program takes two primary colors from the user and displays the resulting secondary color. If the user inputs invalid colors, it shows an error message. 
"""

# Get user input
color1 = input("Enter the first primary color (red, blue, yellow): ").strip().lower()
color2 = input("Enter the second primary color (red, blue, yellow): ").strip().lower()

# Validate input
valid_colors = ["red", "blue", "yellow"]

if color1 not in valid_colors or color2 not in valid_colors:
    print("Error: Both colors must be primary colors (red, blue, yellow).")
else:
    if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
        result = purple
    elif (color1 == "red" and color2 == "yellow") or (color 1 == "yellow" and color2 == "red"):
        result = orange
    elif (color 1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
        result = "green"
    else: 
        result = None

    # Display the result
    if result:
        print(f"The result of mixing {color1} and {color2} is {result}.")


