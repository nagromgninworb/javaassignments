"""
Author: Morgan Browning
Date written: 01/19/2025
Assignment: Module 01 Programming Assignment - Part 1

This program converts a temperature in Celcius to Fahrenheit. The user is prompted to put in a Celcius temperature, and the program calculates and displays the equivalent Fahrenheit temperature.
"""

# Ask the user to enter a temperature in Celcius
celsius = float(input("Enter the temperature in Celcius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (9 / 5) * celsius + 32

# Display the result
print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")
