"""
Author: Morgan Browning
Date: 01/24/2025
Assignment: Module 02 Practice Exercise 3-1

This program prompts the user to enter numbers, caluclates their sums and average, and displays the results. The user can stop the program by pressing enter. 
"""

# Inititalize variables
theSum = 0
count = 0

# Loop for user input
while True:
    number = input("Enter a number or press Enter to quit: ")
    if number == "":  # If the user presses Enter without input
        break  # Exit the loop

    try:
        number = float(number)  # Convert input to a floating-point number
        theSum += number  # Add the valid number to the total sum
        count += 1  # Increment the count of valid numbers entered
    except ValueError:
        print("Invalid input. Please enter a valid number.")  # Catch invalid inputs

# Display the results
print("The sum is:", theSum)
if count > 0: 
    average = theSum / count  # Calculate the average
    print("The average is:", average)
else: 
    print("No numbers were entered.") 




