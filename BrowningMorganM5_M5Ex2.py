"""
Author: Morgan Browning
Date: 02/17/2025
Assignment: Module 05 Programming Assignment Part 2

This program generates a random number between 1 and 100 
and asks the user to guess it. 

Feedback is provided for each guess:
- "Too high, try again."
- "Too low, try again."
- "Congratulations!" if guessed correctly.

The game continues by generating a new number after each correct guess.
"""

import random

# Function for the number guessing game
def guessingGame():
    while True:
        # Generate a new random number between 1 and 100
        target_number = random.randint(1, 100)
        print("\nA new number has been generated! Try to guess it.")

        # Loop until the user guesses correctly
        while True:
            try:
                guess = int(input("Enter your guess (1-100): "))

                # Validate guess range
                if guess < 1 or guess > 100:
                    print("Guess must be between 1 and 100. Try again.")
                    continue

                # Provide feedback
                if guess > target_number:
                    print("Too high, try again.")
                elif guess < target_number:
                    print("Too low, try again.")
                else:
                    print(f"🎉 Congratulations! You guessed the number {target_number} correctly! 🎯")
                    break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        # Ask if the user wants to play again
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


# Run the program
guessingGame()
